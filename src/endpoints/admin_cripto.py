# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# # from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.cripto_empresa import CriptoEmpresa
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_datahora import pegar_data_atual, pegar_data_hora_atual


router = _fastapi.APIRouter(prefix="/cripto", tags=['admin_cripto'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @login_required
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
async def get_index():
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="admin_cripto.html")
    return {"result": "ok"}


# @bp_admin_cripto.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_grid(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
#
#         rows = CriptoEmpresa.buscar_todos()
#
#         lista = [
#             [
#                 str(row['CODIGO']) if row['CODIGO'] else '',
#                 str(row['NOME']),
#                 CriptoEmpresa.descricao_situacao(situacao=str(row['SITUACAO'])),
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
# @bp_admin_cripto.route('/salvar', methods=['GET', 'POST'])
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
#             id_cripto = data.get('criptoId')
#             nome = data.get('criptoNome')
#             codigo = data.get('criptoCodigo')
#             situacao = data.get('criptoSituacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not nome: return make_response(get_json_retorno_metodo(msg='Nome não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Codigo não informado.'), 200)
#
#         if not id_cripto:
#             if CriptoEmpresa.buscar_por_codigo(codigo=str(codigo)):
#                 return make_response(get_json_retorno_metodo(msg='Cripto já cadastrada.'), 200)
#
#         cripto = CriptoEmpresa()
#         if id_cripto:
#             cripto = CriptoEmpresa.get_by_id(id=int(id_cripto))
#             if not cripto: return make_response(get_json_retorno_metodo(msg='Cripto não localizada.'), 200)
#
#         cripto.nome = str(nome)
#         cripto.codigo = str(codigo)
#         cripto.vlr_preco_fechamento = 0.0
#         cripto.vlr_preco_anterior = 0.0
#         cripto.vlr_variacao = 0.0
#         cripto.data_hora_alteracao = pegar_data_hora_atual()
#         cripto.situacao = str(situacao)
#         cripto.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_cripto.route('/carregar', methods=['GET', 'POST'])
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
#             id_cripto = data.get('criptoId')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_cripto:
#             return make_response(get_json_retorno_dados(msg='Id. não informado.'), 200)
#
#         cripto = CriptoEmpresa.buscar_por_id(id=int(id_cripto))
#         if not cripto:
#             return make_response(get_json_retorno_dados(msg='Cripto não localizada!'), 200)
#
#         dados = dict(
#             {
#                 "Id": str(cripto['ID']),
#                 "Nome": str(cripto['NOME']) if cripto['NOME'] else '',
#                 "Codigo": str(cripto['CODIGO']) if cripto['CODIGO'] else '',
#                 "Situacao": str(cripto['SITUACAO']) if cripto['SITUACAO'] else '',
#             }
#         )
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
