# # -*- coding: utf-8 -*-
# import sys
# import os
# from flask import Blueprint, render_template, make_response, redirect, url_for
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_grid, get_json_retorno_lista_erro
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str
#
#
# bp_admin_log_erros = Blueprint('logerro', __name__, url_prefix='/logErro')
#
#
# @bp_admin_log_erros.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
# def index():
#     if str(current_user.tipo) != 'A':
#         return redirect(location=url_for('principal.index'))
#     return render_template(template_name_or_list="admin_log_erros.html")
#
#
# @bp_admin_log_erros.route('/montarMenu', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def montar_menu():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_lista_erro(msg='Somente para Administradores.'), 200)
#
#         rows = LogErro.buscar_todos(situacao='N')  # N - NAO
#
#         lista = [
#             [
#                 str(row['ARQUIVO']) if row['ARQUIVO'] else '',
#                 converter_datetime_str(data=converter_str_to_datetime(data=str(row['DATAHORA'])[0:14], fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S'),
#                 str(row['TEXTO'])[0:40]
#              ]
#             for indx, row in enumerate(rows) if indx < 5
#         ]
#
#         existe = 'SIM' if lista else 'NAO'
#
#         return make_response(get_json_retorno_lista_erro(rslt='OK', existe=existe, lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista_erro(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_log_erros.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_grid(msg='Somente para Administradores.'), 200)
#
#         rows = LogErro.buscar_todos()
#
#         lista = [
#             [
#                 str(row['DATAHORA']),
#                 str(row['ARQUIVO']) if row['ARQUIVO'] else '',
#                 str(row['NOMEUSUARIO']) if row['NOMEUSUARIO'] else '',
#                 str(row['LINHA']) if row['LINHA'] else '',
#                 str(row['CODIGO']) if row['CODIGO'] else '',
#                 str(row['TEXTO']),
#                 str(row['ID']),
#                 str(row['SITUACAO'])
#              ]
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
# @bp_admin_log_erros.route('/excluir', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_metodo(msg='Somente para Administradores.'), 200)
#
#         LogErro.excluir_tudo()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_log_erros.route('/marcar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def marcar():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_metodo(msg='Somente para Administradores.'), 200)
#
#         LogErro.marcar_tudo()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
