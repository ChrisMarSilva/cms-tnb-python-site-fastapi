# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
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
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="/alerta", tags=['admin_alerta'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
#@login_required
#@flask_optimize.optimize(cache='GET-84600')
async def get_index(request: _fastapi.Request):
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="admin_alerta.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


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
#         if not data: return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         try:
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#             tipo = data.get('Tipo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
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
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         try:
#             tipo_assinatura = data.get('tipo_assinatura')
#             tipo_alerta = data.get('tipo_alerta')
#             situacao = data.get('situacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not tipo_assinatura: return make_response(get_json_retorno_metodo(msg='Tipo Assinatura não informado.'), 200)
#         if not tipo_alerta: return make_response(get_json_retorno_metodo(msg='Tipo Alerta não informado..'), 200)
#         if not situacao: return make_response(get_json_retorno_metodo(msg='Situação não informada.'), 200)
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
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         try:
#             tipo = data.get('txtTipo')
#             id_user = data.get('txtUser')
#             mensagem = data.get('txtMsg')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not tipo: return make_response(get_json_retorno_metodo(msg='Tipo do Alerta não informado.'), 200)
#         if str(tipo) == 'ADMIN-01': id_user = None
#         if str(tipo) == 'ADMIN-02' and not id_user: return make_response(get_json_retorno_metodo(msg='Usuário do Alerta não informado.'), 200)
#         if not mensagem: return make_response(get_json_retorno_metodo(msg='Mensagem do Alerta não informada.'), 200)
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
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         try:
#             id_assinatura = data.get('id_assinatura')
#             situacao = data.get('situacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_assinatura: return make_response(get_json_retorno_metodo(msg='Id. Assinatura não informado.'), 200)
#         if not situacao: return make_response(get_json_retorno_metodo(msg='"Situação não informada.'), 200)
#
#         assinatura = UsuarioAlertaAssinatura.get_by_id(id=int(id_assinatura))
#         if not assinatura:
#             return make_response(get_json_retorno_metodo(msg='Assinatura não Localizada.'), 200)
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
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         try:
#             id_alerta = data.get('IdAlerta')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_alerta: return make_response(get_json_retorno_metodo(msg='Id. Alerta não informado.'), 200)
#
#         alerta = Alerta.get_by_id(id=int(id_alerta))
#         if not alerta:
#             return make_response(get_json_retorno_metodo(msg='Alerta não Localizado.'), 200)
#
#         alerta.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
