# -*- coding: utf-8 -*-
import sys
import os
from validate_docbr import CNPJ
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.corretora_lista import CorretoraLista
# from app.models.usuario_corretora import UsuarioCorretora
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid


router = _fastapi.APIRouter(prefix="/corretora", tags=['corretora'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @login_required
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index():
    # return render_template(template_name_or_list="corretora.html")
    return {"result": "ok"}


# @bp_corretora.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         id_usuario = current_user.id
#
#         rows = UsuarioCorretora.get_all_by_usuario(id_usuario=id_usuario)
#         lista = [[str(corretora.nome), str(corretora.cnpj), corretora.valor_format(), str(corretora.id)] for corretora in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_corretora.route('/carregar', methods=['GET', 'POST'])
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
#             id = data.get('IdCorret')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id:
#             return make_response(get_json_retorno_dados(msg='Id Corretora não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         corretora = UsuarioCorretora.get_by_usuario(id=id, id_usuario=id_usuario)
#         if not corretora:
#             return make_response(get_json_retorno_dados(msg='Corretora não localizada.'), 200)
#
#         dados = dict({
#             "Id": str(corretora.id),
#             "IdCorretoraLista": str(corretora.id_corretora_lista) if corretora.id_corretora_lista else '',
#             "Nome": str(corretora.nome),
#             "CNPJ": str(corretora.cnpj),
#             "Valor": corretora.valor_format()
#         })
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_corretora.route('/carregarcorretorageral', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_corretora_geral():
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
#             id_corretora_lista = data.get('corretora')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_corretora_lista: return make_response(get_json_retorno_dados(msg='Id Corretora não informado.'), 200)
#
#         corretora_lista = CorretoraLista.get_by_id(id=int(id_corretora_lista))
#         if not corretora_lista:
#             return make_response(get_json_retorno_dados(msg='Corretora não localizada.'), 200)
#
#         dados = dict({
#             "Id": str(corretora_lista.id),
#             "Nome": str(corretora_lista.nome),
#             "CNPJ": str(corretora_lista.cnpj)
#         })
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_corretora.route('/salvar', methods=['GET', 'POST'])
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
#             id_corretora_lista = data.get('IdCorretoraLista')
#             nome = data.get('Nome')
#             cnpj = data.get('CNPJ')
#             valor = data.get('Valor')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if str(id).strip() == '': id = None
#
#         if not nome: return make_response(get_json_retorno_metodo(msg='Nome não informado.'), 200)
#         if not valor: return make_response(get_json_retorno_metodo(msg='Valor não informado'), 200)
#         if not cnpj: return make_response(get_json_retorno_metodo(msg='CNPJ não informado.'), 200)
#         if not CNPJ().validate(doc=cnpj): return make_response(get_json_retorno_metodo(msg='CNPJ inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         if not id and UsuarioCorretora.get_by_cnpj(cnpj=str(cnpj), id_usuario=id_usuario):
#             return make_response(get_json_retorno_metodo(msg='Corretora já cadastrada.'), 200)
#
#         if not id and id_corretora_lista and UsuarioCorretora.get_by_id_corretora_lista(id_corretora_lista=int(id_corretora_lista), id_usuario=id_usuario):
#             return make_response(get_json_retorno_metodo(msg='Corretora já cadastrada.'), 200)
#
#         if not id:
#             corretora = UsuarioCorretora(id_usuario=id_usuario)
#         else:
#             corretora = UsuarioCorretora.get_by_usuario(id=id, id_usuario=id_usuario)
#
#         if not corretora:
#             return make_response(get_json_retorno_metodo(msg='Corretora não localizada.'), 200)
#
#         corretora.id_corretora_lista = int(id_corretora_lista) if id_corretora_lista else None
#         corretora.nome = nome
#         corretora.cnpj = cnpj
#         corretora.valor = float(valor.replace('.', '').replace(',', '.'))
#         corretora.situacao = 'A'  # A-Ativo
#         corretora.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_corretora.route('/excluir', methods=['GET', 'POST'])
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
#             id = data.get('IdCorret')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id:
#             return make_response(get_json_retorno_metodo(msg='Id. Corretora Inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         corretora = UsuarioCorretora.get_by_usuario(id=id, id_usuario=id_usuario)
#
#         if not corretora:
#             return make_response(get_json_retorno_metodo(msg='Corretora não localizada.'), 200)
#
#         corretora.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Corretora Excluída!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
