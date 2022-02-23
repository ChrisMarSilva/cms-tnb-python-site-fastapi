# # -*- coding: utf-8 -*-
# import sys
# import os
# from flask import Blueprint, render_template, make_response, request
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.usuario_acao_empresa_aluguel import UsuarioACAOEmpresaAluguel
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_formatacao import decimal_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str
#
#
# bp_aluguel = Blueprint('aluguel', __name__, url_prefix='/aluguel')
#
#
# @bp_aluguel.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# # @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     return render_template(template_name_or_list="aluguel.html")
#
#
# @bp_aluguel.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         try:
#             cod_ativo = data.get('CodAtivo')
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         id_usuario = current_user.id
#
#         rows = UsuarioACAOEmpresaAluguel.buscar_todos(id_usuario=id_usuario, codigo=cod_ativo, dt_ini=dt_ini, dt_fim=dt_fim)
#
#         lista = [
#             [
#                 aluguel['DATA'],
#                 aluguel['CODIGOATIVO'],
#                 decimal_to_str(valor=aluguel['VLRBRUTO']),
#                 decimal_to_str(valor=aluguel['VLRIR']),
#                 decimal_to_str(valor=aluguel['VLRLIQUIDO']),
#                 aluguel['ID'],
#             ]
#             for aluguel in rows
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_aluguel.route('/carregar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar():
#     try:
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
#             id = data.get('IdAlug')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id:
#             return make_response(get_json_retorno_dados(msg='Id Aluguel não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         aluguel = UsuarioACAOEmpresaAluguel.buscar_por_id(id=id, id_usuario=id_usuario)
#
#         if not aluguel:
#             return make_response(get_json_retorno_dados(msg='Aluguel não localizado!'), 200)
#
#         dados = dict(
#             {
#                 "Id": aluguel['ID'],
#                 "Data": converter_datetime_str(data=converter_str_to_datetime(data=aluguel['DATA'], fmt='%Y%m%d'), fmt='%Y-%m-%d'),
#                 "CodAtivo": aluguel['CODIGOATIVO'],
#                 "VlrBruto": decimal_to_str(valor=aluguel['VLRBRUTO']),
#                 "VlrIR": decimal_to_str(valor=aluguel['VLRIR']),
#                 "VlrLiquido": decimal_to_str(valor=aluguel['VLRLIQUIDO'])
#             }
#         )
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_aluguel.route('/salvar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar():
#     try:
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
#             id = data.get('Id')
#             dt = data.get('Data')
#             codigo = data.get('CodAtivo')
#             valor_bruto = data.get('VlrBruto')
#             valor_ir = data.get('VlrIR')
#             valor_liquido = data.get('VlrLiquido')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if str(id).strip() == '':
#             id = None
#
#         if not dt:
#             return make_response(get_json_retorno_metodo(msg='Data não informada.'), 200)
#
#         if not codigo:
#             return make_response(get_json_retorno_metodo(msg='Ativo não informado.'), 200)
#
#         if not valor_bruto:
#             return make_response(get_json_retorno_metodo(msg='Valor Bruto não informado.'), 200)
#
#         empresa_ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=codigo)
#         if not empresa_ativo:
#             return make_response(get_json_retorno_metodo(msg='Ativo não localizado'), 200)
#
#         id_usuario = current_user.id
#
#         if not id:
#             aluguel = UsuarioACAOEmpresaAluguel(id_usuario=id_usuario)
#         else:
#             aluguel = UsuarioACAOEmpresaAluguel.get_by_usuario(id=id, id_usuario=id_usuario)
#
#         if not aluguel:
#             return make_response(get_json_retorno_metodo(msg='Aluguel não localizado.'), 200)
#
#         aluguel.id_ativo = empresa_ativo.id
#         aluguel.data = dt.replace('-', '')
#         aluguel.valor_bruto = 0.00 if valor_ir is None or str(valor_bruto).strip() == '' else float(valor_bruto.replace('.', '').replace(',', '.'))
#         aluguel.valor_ir = 0.00 if valor_ir is None or str(valor_ir).strip() == '' else float(valor_ir.replace('.', '').replace(',', '.'))
#         aluguel.valor_liquido = 0.00 if valor_liquido is None or str(valor_liquido).strip() == ''else float(valor_liquido.replace('.', '').replace(',', '.'))
#         aluguel.situacao = 'A'  # A-Ativo
#         aluguel.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_aluguel.route('/excluir', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir():
#     try:
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
#             id = data.get('IdAlug')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id:
#             return make_response(get_json_retorno_metodo(msg='Id. Aluguel Inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         aluguel = UsuarioACAOEmpresaAluguel.get_by_usuario(id=id, id_usuario=id_usuario)
#         if not aluguel:
#             return make_response(get_json_retorno_metodo(msg='Aluguel não localizada.'), 200)
#
#         aluguel.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
