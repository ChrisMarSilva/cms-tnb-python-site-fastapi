# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.alerta import Alerta
# from app.models.usuario import Usuario
# from app.models.usuario_hash import UsuarioHash
# from app.models.usuario_carteira import UsuarioCarteira
# from app.util.util_datahora import pegar_data_atual
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_grid
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="/investidor", tags=['admin_investidor'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
# @login_required
# @flask_optimize.optimize(cache='GET-1')  # 600seg/10Min
async def get_index(request: _fastapi.Request):
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="admin_investidor.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


# @bp_admin_investidor.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_grid(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
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
#             situacao = data.get('Situacao')
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if dt_ini: dt_ini = str(dt_ini).replace('-', '') + "000000000"
#         if dt_fim: dt_fim = str(dt_fim).replace('-', '') + "235959000"
#
#         lista = get_lista_grid(situacao=situacao, dt_ini=dt_ini, dt_fim=dt_fim)
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# def get_lista_grid(situacao: str = None, dt_ini: str = None, dt_fim: str = None):
#     try:
#
#         # rows = Usuario.buscar_todosr(situacao=situacao, dt_ini=dt_ini, dt_fim=dt_fim)
#         rows = Usuario.buscar_todos_grid_investidor(situacao=situacao, dt_ini=dt_ini, dt_fim=dt_fim)
#
#         lista = [
#             [
#                 str(current_app.config['IMAGE_UPLOADS']) + '/' + str(row['FOTO']) if row['FOTO'] else '',
#                 '(' + str(row['ID']) + ') ' + str(row['NOME']),
#                 str(row['EMAIL']),
#                 str(row['DTREGISTRO']),
#                 str(row['QTDE_EMPR_LANC']) if row['QTDE_EMPR_LANC'] and row['QTDE_EMPR_LANC'] > 0.0 else '',
#                 str(row['QTDE_EMPR_PROV']) if row['QTDE_EMPR_PROV'] and row['QTDE_EMPR_PROV'] > 0.0 else '',
#                 str(row['QTDE_FII_LANC']) if row['QTDE_FII_LANC'] and row['QTDE_FII_LANC'] > 0.0 else '',
#                 str(row['QTDE_FII_PROV']) if row['QTDE_FII_PROV'] and row['QTDE_FII_PROV'] > 0.0 else '',
#                 str(row['QTDE_ETF_LANC']) if row['QTDE_ETF_LANC'] and row['QTDE_ETF_LANC'] > 0.0 else '',
#                 str(row['QTDE_BDR_LANC']) if row['QTDE_BDR_LANC'] and row['QTDE_BDR_LANC'] > 0.0 else '',
#                 str(row['QTDE_BDR_PROV']) if row['QTDE_BDR_PROV'] and row['QTDE_BDR_PROV'] > 0.0 else '',
#                 str(row['QTDE_CRIPTO_LANC']) if row['QTDE_CRIPTO_LANC'] and row['QTDE_CRIPTO_LANC'] > 0.0 else '',
#                 str(row['DATA_HORA_SITE']) if row['DATA_HORA_SITE'] else '',
#                 str(row['DATA_HORA_APP']) if row['DATA_HORA_APP'] else '',
#                 Usuario.descricao_situacao(situacao=str(row['SITUACAO'])),
#                 str(row['ID'])
#             ]
#             for row in rows
#         ]
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return []
#
#
# @bp_admin_investidor.route('/alterarsituacao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def alterar_situacao():
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
#             id_user = data.get('IdUsuario')
#             situacao = data.get('Situacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_user: return make_response(get_json_retorno_metodo(msg='Id. Usuário não informado.'), 200)
#         if not situacao: return make_response(get_json_retorno_metodo(msg='"Situação não informada.'), 200)
#
#         usuario = Usuario.get_by_id(id=int(id_user))
#         if not usuario:
#             return make_response(get_json_retorno_metodo(msg='Usuário não localizado.'), 200)
#
#         hash_mail = UsuarioHash.get_by_usuario(id_usuario=usuario.id)
#         if not hash_mail:
#             raise Exception('Hash do Usuário não foi encontrado.')
#
#         usuario.situacao = str(situacao)
#         usuario.salvar()
#
#         if situacao != 'X':
#             hash_mail.situacao = str(situacao)
#             hash_mail.salvar()
#
#         if str(situacao) == 'A': Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-03', mensagem='Usuário Ativado pelo Admin.')
#         if str(situacao) == 'I': Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-03', mensagem='Usuário Inativado pelo Admin.')
#         if str(situacao) == 'X': Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-03', mensagem='Usuário Bloqueado pelo Admin.')
#
#         if str(situacao) == 'A': msg = 'Usuário Ativado'
#         if str(situacao) == 'I': msg = 'Usuário Inativado'
#         if str(situacao) == 'X': msg = 'Usuário Bloqueado'
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg=msg), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_investidor.route('/alterarnome', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def alterar_nome():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(
#                 get_json_retorno_metodo(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
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
#             id_user = data.get('IdUsuario')
#             nome = data.get('NomeUsuario')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_user: return make_response(get_json_retorno_metodo(msg='Id. Usuário não informado.'), 200)
#         if not nome: return make_response(get_json_retorno_metodo(msg='"Nome não informado.'), 200)
#
#         usuario = Usuario.get_by_id(id=int(id_user))
#         if not usuario:
#             return make_response(get_json_retorno_metodo(msg='Usuário não localizado.'), 200)
#
#         usuario.nome = nome
#         usuario.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Nome Alterado!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_investidor.route('/excluir', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir():
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
#             id_user = data.get('IdUsuario')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_user: return make_response(get_json_retorno_metodo(msg='Id. Usuário não informado.'), 200)
#
#         usuario = Usuario.get_by_id(id=int(id_user))
#         if not usuario: return make_response(get_json_retorno_metodo(msg='Usuário não localizado.'), 200)
#
#         usuario.excluir_tudo()
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Usuario Excluido'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_investidor.route('/gerarcarteira', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def gerar_carteira():
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
#             id_user = data.get('IdUsuario')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_user: return make_response(get_json_retorno_metodo(msg='Id. Usuário não informado.'), 200)
#
#         usuario = Usuario.get_by_id(id=int(id_user))
#         if not usuario:
#             return make_response(get_json_retorno_metodo(msg='Usuário não localizado.'), 200)
#
#         UsuarioCarteira.zerar(id_usuario=int(id_user))
#         UsuarioCarteira.gerar(id_usuario=int(id_user))
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
