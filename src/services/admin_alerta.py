# # -*- coding: utf-8 -*-
# import sys
# import os
# from flask import Blueprint, make_response, request, render_template, redirect, url_for
# from flask_login import login_required, current_user
# import opentracing
# #from app.tracing import tracing
# from app.optimize import flask_optimize
# from app.cache import cache
# from app.models.log_erro import LogErro
# from app.models.alerta import Alerta
# from app.models.usuario_alerta_assinatura import UsuarioAlertaAssinatura
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_grid
# from app.util.util_datahora import pegar_data_hora_atual
#
#
# bp_admin_alerta = Blueprint('admin_alerta', __name__, url_prefix='/alerta')
#
#
# # span1 = tracing.start_span('top_level_function')
# # try:
# # finally:
# #     span1.finish()
# # span2 = get_current_span().start_child('function2') \
# #     if get_current_span() else None
# # try:
# # finally:
# #     if span2:
# #         span2.finish()
# #  parent_span = get_current_span()
# # # with tracing.scope_manager.active() as parent_span:
# # with tracing.get_span() as parent_span:
# #     with opentracing.tracer.start_span('principal', child_of=parent_span) as span:
# #         with opentracing.tracer.start_span('pegar_user_atual', child_of=span) as span_child:
# #             id_usuario = current_user.id
# #         with opentracing.tracer.start_span('pegar_todas_assinaturas', child_of=span) as span_child:
# #             rows = UsuarioAlertaAssinatura.find_all_by_usuario(id_usuario=id_usuario)
# #         with opentracing.tracer.start_span('montar_lista', child_of=span) as span_child:
# #             lista = [[assinatura.tipo_assinatura, assinatura.tipo_alerta, assinatura.situacao, str(assinatura.id)] for assinatura in rows]
# #         with opentracing.tracer.start_span('montar_json', child_of=span) as span_child:
# #             return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#
# @bp_admin_alerta.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
# def index():
#     if str(current_user.tipo) != 'A':
#         return redirect(location=url_for('principal.index'))
#     return render_template(template_name_or_list="admin_alerta.html")
#
#
# @bp_admin_alerta.route('/grid', methods=['GET', 'POST'])
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
#         if not data: return make_response(get_json_retorno_grid(msg='Dados n??o informado!'), 200)
#
#         try:
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#             tipo = data.get('Tipo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados n??o informado!'), 200)
#
#         if dt_ini: dt_ini = str(dt_ini).replace('-', '')
#         if dt_fim: dt_fim = str(dt_fim).replace('-', '')
#
#         rows = Alerta.buscar_todos(tipo=tipo, dt_ini=dt_ini, dt_fim=dt_fim)
#
#         lista = [
#             [
#                 str(row['DTHRREGISTRO']),
#                 str(row['DTENVIO']),
#                 str(row['NMUSUARIO']),
#                 Alerta.descricao_tipo(tipo=str(row['TIPO'])),
#                 str(row['MENSAGEM']),
#                 Alerta.descricao_situacao_telegram(situacao_telegram=str(row['SITUACAO_TELEGRAM'])),
#                 Alerta.descricao_situacao_email(situacao_email=str(row['SITUACAO_EMAIL'])),
#                 str(row['IDUSUARIO']),
#                 str(row['ID']),
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
# @bp_admin_alerta.route('/griduserassinatura', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_user_assinatura():
#     try:
#
#         rows = UsuarioAlertaAssinatura.buscar_todos()
#
#         lista = [
#             [
#                 str(row['NMUSUARIO']),
#                 UsuarioAlertaAssinatura.descricao_tipo_alerta(tipo_alerta=str(row['TIPO_ALERTA'])),
#                 UsuarioAlertaAssinatura.descricao_tipo_assinatura(tipo_assinatura=str(row['TIPO_ASSINATURA'])),
#                 str(row['IDUSUARIO']),
#                 str(row['ID']),
#                 str(row['SITUACAO']),
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
# @bp_admin_alerta.route('/carregarassinaturas', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_assinaturas():
#     try:
#
#         id_usuario = current_user.id
#
#         rows = UsuarioAlertaAssinatura.get_all_by_usuario(id_usuario=id_usuario)
#
#         lista = [[str(assinatura.tipo_assinatura), str(assinatura.tipo_alerta), str(assinatura.situacao), str(assinatura.id)] for assinatura in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_alerta.route('/salvarassinatura', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_assinatura():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         try:
#             tipo_assinatura = data.get('tipo_assinatura')
#             tipo_alerta = data.get('tipo_alerta')
#             situacao = data.get('situacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         if not tipo_assinatura: return make_response(get_json_retorno_metodo(msg='Tipo Assinatura n??o informado.'), 200)
#         if not tipo_alerta: return make_response(get_json_retorno_metodo(msg='Tipo Alerta n??o informado..'), 200)
#         if not situacao: return make_response(get_json_retorno_metodo(msg='Situa????o n??o informada.'), 200)
#
#         id_usuario = current_user.id
#
#         assinatura = UsuarioAlertaAssinatura.get_by_tipos(id_usuario=id_usuario, tipo_assinatura=tipo_assinatura, tipo_alerta=tipo_alerta)
#         if not assinatura:
#             assinatura = UsuarioAlertaAssinatura(id_usuario=id_usuario, dthr_registro=pegar_data_hora_atual(fmt='%Y%m%d%H%M%S'), tipo_assinatura=tipo_assinatura, tipo_alerta=tipo_alerta)
#
#         assinatura.dthr_alteracao = pegar_data_hora_atual(fmt='%Y%m%d%H%M%S')
#         assinatura.situacao = situacao
#         assinatura.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         # import traceback
#         # logging.error(msg=f'Falha Geral: {traceback.format_exc()}')
#         # etype, value, tb = sys.exc_info()
#         # logging.error(msg=f'Falha Geral: {traceback.print_exception(etype, value, tb)}')
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_alerta.route('/salvar', methods=['GET', 'POST'])
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
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         try:
#             tipo = data.get('txtTipo')
#             id_user = data.get('txtUser')
#             mensagem = data.get('txtMsg')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         if not tipo: return make_response(get_json_retorno_metodo(msg='Tipo do Alerta n??o informado.'), 200)
#         if str(tipo) == 'ADMIN-01': id_user = None
#         if str(tipo) == 'ADMIN-02' and not id_user: return make_response(get_json_retorno_metodo(msg='Usu??rio do Alerta n??o informado.'), 200)
#         if not mensagem: return make_response(get_json_retorno_metodo(msg='Mensagem do Alerta n??o informada.'), 200)
#
#         if str(tipo) == 'ADMIN-01':
#             rows = UsuarioAlertaAssinatura.buscar_lista_user()
#             for row in rows:
#                 Alerta.registrar(id_usuario=int(rows['ID']), tipo=str(tipo), mensagem=str(mensagem))
#
#         elif str(tipo) == 'ADMIN-02':
#             Alerta.registrar(id_usuario=int(id_user), tipo=str(tipo), mensagem=str(mensagem))
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_alerta.route('/alterarassinatura', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def alterar_assinatura():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         try:
#             id_assinatura = data.get('id_assinatura')
#             situacao = data.get('situacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         if not id_assinatura: return make_response(get_json_retorno_metodo(msg='Id. Assinatura n??o informado.'), 200)
#         if not situacao: return make_response(get_json_retorno_metodo(msg='"Situa????o n??o informada.'), 200)
#
#         assinatura = UsuarioAlertaAssinatura.get_by_id(id=int(id_assinatura))
#         if not assinatura:
#             return make_response(get_json_retorno_metodo(msg='Assinatura n??o Localizada.'), 200)
#
#         assinatura.dthr_alteracao = pegar_data_hora_atual(fmt='%Y%m%d%H%M%S')
#         assinatura.situacao = situacao
#         assinatura.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_alerta.route('/excluir', methods=['GET', 'POST'])
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
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         try:
#             id_alerta = data.get('IdAlerta')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         if not id_alerta: return make_response(get_json_retorno_metodo(msg='Id. Alerta n??o informado.'), 200)
#
#         alerta = Alerta.get_by_id(id=int(id_alerta))
#         if not alerta:
#             return make_response(get_json_retorno_metodo(msg='Alerta n??o Localizado.'), 200)
#
#         alerta.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
