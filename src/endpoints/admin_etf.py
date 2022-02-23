# # -*- coding: utf-8 -*-
# import sys
# import os
# from flask import Blueprint, render_template, make_response, redirect, url_for, request
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.etf_indice import ETFIndice
# from app.models.etf_indice_cotacao import ETFIndiceCotacao
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_datahora import pegar_data_atual, pegar_data_hora_atual
#
#
# bp_admin_etf = Blueprint('admin_etf', __name__, url_prefix='/etf')
#
#
# @bp_admin_etf.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
# def index():
#     if str(current_user.tipo) != 'A':
#         return redirect(location=url_for('principal.index'))
#     return render_template(template_name_or_list="admin_etf.html")
#
#
# @bp_admin_etf.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_grid(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
#
#         rows = ETFIndice.buscar_todos()
#
#         lista = [
#             [
#                 str(row['CODIGO']) if row['CODIGO'] else '',
#                 str(row['FUNDO']),
#                 str(row['RAZAOSOCIAL']),
#                 str(row['CNPJ']) if row['CNPJ'] else '',
#                 ETFIndice.descricao_situacao(situacao=str(row['SITUACAO'])),
#                 str(row['ID'])
#             ]
#             for row in rows
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_etf.route('/salvar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_metodo(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
#
#         data = None
#         if request.method == 'POST': data = request.form
#         elif request.method == 'GET': data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         try:
#             id_etf = data.get('etfId')
#             razao_social = data.get('etfRazao')
#             fundo = data.get('etfFundo')
#             indice = data.get('etfIndice')
#             nome = data.get('etfNome')
#             cnpj = data.get('etfCNPJ')
#             codigo = data.get('etfCodigo')
#             codigo_isin = data.get('etfIsin')
#             situacao = data.get('etfSituacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not fundo: return make_response(get_json_retorno_metodo(msg='Fundo não informado.'), 200)
#         if not razao_social: return make_response(get_json_retorno_metodo(msg='Razão Social não informado.'), 200)
#         if not cnpj: return make_response(get_json_retorno_metodo(msg='CNPJ não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Codigo não informado.'), 200)
#
#         if not id_etf:
#             if ETFIndice.buscar_por_codigo(codigo=str(codigo)):
#                 return make_response(get_json_retorno_metodo(msg='Etf já cadastrado.'), 200)
#
#         etf = None
#         if id_etf: etf = ETFIndice.get_by_id(id=int(id_etf))
#         else: etf = ETFIndice()
#         if not etf: return make_response(get_json_retorno_metodo(msg='Etf não localizado.'), 200)
#
#         etf.razao_social = str(razao_social)
#         etf.fundo = str(fundo)
#         etf.indice = str(indice)
#         etf.nome = str(nome)
#         etf.cnpj = str(cnpj)
#         etf.codigo = str(codigo)
#         etf.codigo_isin = str(codigo_isin) if codigo_isin else None
#         etf.situacao = str(situacao)
#         etf.salvar()
#
#         cotacao = ETFIndiceCotacao.get_by_indice(id_indice=int(etf.id))
#         if not cotacao:
#             cotacao = ETFIndiceCotacao(id_indice=int(etf.id))
#
#         cotacao.data = pegar_data_atual()
#         cotacao.vlr_preco_abertura = 0.0
#         cotacao.vlr_preco_fechamento = 0.0
#         cotacao.vlr_preco_maximo = 0.0
#         cotacao.vlr_preco_minimo = 0.0
#         cotacao.vlr_preco_anterior = 0.0
#         cotacao.vlr_variacao = 0.0
#         cotacao.data_hora_alteracao = pegar_data_hora_atual()
#         cotacao.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_etf.route('/carregar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_dados(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         try:
#             id_etf = data.get('etfId')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_etf:
#             return make_response(get_json_retorno_dados(msg='Id. não informado.'), 200)
#
#         etf = ETFIndice.buscar_por_id(id=int(id_etf))
#         if not etf:
#             return make_response(get_json_retorno_dados(msg='Etf não localizada!'), 200)
#
#         dados = dict(
#             {
#                 "Id": str(etf['ID']),
#                 "Fundo": str(etf['FUNDO']) if etf['FUNDO'] else '',
#                 "RazaoSocial": str(etf['RAZAOSOCIAL']) if etf['RAZAOSOCIAL'] else '',
#                 "Indice": str(etf['INDICE']) if etf['INDICE'] else '',
#                 "Nome": str(etf['NOME']) if etf['NOME'] else '',
#                 "CNPJ": str(etf['CNPJ']) if etf['CNPJ'] else '',
#                 "Codigo": str(etf['CODIGO']) if etf['CODIGO'] else '',
#                 "Isin": str(etf['CODISIN']) if etf['CODISIN'] else '',
#                 "Situacao": str(etf['SITUACAO']) if etf['SITUACAO'] else '',
#             }
#         )
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
