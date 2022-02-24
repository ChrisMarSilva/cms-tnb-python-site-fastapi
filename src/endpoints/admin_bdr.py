# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.bdr_empresa import BDREmpresa
# from app.models.bdr_empresa_cotacao import BDREmpresaCotacao
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_datahora import pegar_data_atual, pegar_data_hora_atual
#
#
# bp_admin_bdr = Blueprint('admin_bdr', __name__, url_prefix='/bdr')
#
#
# @bp_admin_bdr.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
# def index():
#     if str(current_user.tipo) != 'A':
#         return redirect(location=url_for('principal.index'))
#     return render_template(template_name_or_list="admin_bdr.html")
#
#
# @bp_admin_bdr.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_grid(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
#
#         rows = BDREmpresa.buscar_todos()
#
#         lista = [
#             [
#                 str(row['CODIGO']) if row['CODIGO'] else '',
#                 str(row['NOME']),
#                 str(row['RAZAOSOCIAL']),
#                 str(row['CNPJ']) if row['CNPJ'] else '',
#                 BDREmpresa.descricao_situacao(situacao=str(row['SITUACAO'])),
#                 str(row['ID'])
#             ] for row in rows
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_bdr.route('/salvar', methods=['GET', 'POST'])
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
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         try:
#             id_bdr = data.get('bdrId')
#             id_setor = data.get('bdrSetor')
#             id_subsetor = data.get('bdrSubSetor')
#             id_segmento = data.get('bdrSegmento')
#             nome = data.get('bdrNome')
#             razao_social = data.get('bdrRazao')
#             cnpj = data.get('bdrCNPJ')
#             cod_cvm = data.get('bdrCodCVM')
#             codigo = data.get('bdrCodigo')
#             codigo_isin = data.get('bdrIsin')
#             tipo = data.get('bdrTipo')
#             situacao = data.get('bdrSituacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not nome: return make_response(get_json_retorno_metodo(msg='Nome não informado.'), 200)
#         if not razao_social: return make_response(get_json_retorno_metodo(msg='Razão Social não informado.'), 200)
#         if not cnpj: return make_response(get_json_retorno_metodo(msg='CNPJ não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Codigo não informado.'), 200)
#
#         if not id_bdr:
#             if BDREmpresa.buscar_por_codigo(codigo=str(codigo)):
#                 return make_response(get_json_retorno_metodo(msg='Bdr já cadastrada.'), 200)
#
#         bdr = BDREmpresa()
#         if id_bdr:
#             bdr = BDREmpresa.get_by_id(id=int(id_bdr))
#             if not bdr: return make_response(get_json_retorno_metodo(msg='Bdr não localizada.'), 200)
#
#         bdr.id_setor = id_setor if id_setor else None
#         bdr.id_subsetor = id_subsetor if id_subsetor else None
#         bdr.id_segmento = id_segmento if id_segmento else None
#         bdr.nome = str(nome).strip() if nome else None
#         bdr.razao_social = str(razao_social).strip() if razao_social else None
#         bdr.cnpj = str(cnpj).strip() if cnpj else None
#         bdr.atividade = None
#         bdr.cod_cvm = str(cod_cvm).strip() if cod_cvm else None
#         bdr.sit_cvm = None
#         bdr.codigo = str(codigo).strip() if codigo else None
#         bdr.codigo_isin = str(codigo_isin).strip() if codigo_isin else None
#         bdr.tipo = str(tipo).strip() if tipo else None
#         bdr.situacao = str(situacao).strip() if situacao else None
#         bdr.salvar()
#
#         cotacao = BDREmpresaCotacao.get_by_ativo(id_bdr=int(bdr.id))
#         if not cotacao:
#             cotacao = BDREmpresaCotacao(id_bdr=int(bdr.id))
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
# @bp_admin_bdr.route('/carregar', methods=['GET', 'POST'])
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
#             id_bdr = data.get('bdrId')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_bdr:
#             return make_response(get_json_retorno_dados(msg='Id. não informado.'), 200)
#
#         bdr = BDREmpresa.buscar_por_id(id=int(id_bdr))
#         if not bdr:
#             return make_response(get_json_retorno_dados(msg='Bdr não localizada!'), 200)
#
#         dados = dict(
#             {
#                 "Id": str(bdr['ID']),
#                 "Nome": str(bdr['NOME']) if bdr['NOME'] else '',
#                 "RazaoSocial": str(bdr['RAZAOSOCIAL']) if bdr['RAZAOSOCIAL'] else '',
#                 "CNPJ": str(bdr['CNPJ']) if bdr['CNPJ'] else '',
#                 "Codigo": str(bdr['CODIGO']) if bdr['CODIGO'] else '',
#                 "Isin": str(bdr['CODISIN']) if bdr['CODISIN'] else '',
#                 "CodCVM": str(bdr['CODCVM']) if bdr['CODCVM'] else '',
#                 "Tipo": str(bdr['TIPO']) if bdr['TIPO'] else '',
#                 "Situacao": str(bdr['SITUACAO']) if bdr['SITUACAO'] else '',
#                 "SetorId": str(bdr['IDSETOR']) if bdr['IDSETOR'] else '',
#                 "SubSetorId": str(bdr['IDSUBSETOR']) if bdr['IDSUBSETOR'] else '',
#                 "SegmentoId": str(bdr['IDSEGMENTO']) if bdr['IDSEGMENTO'] else '',
#             }
#         )
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
