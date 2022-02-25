# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.fii_fundoimob import FiiFundoImob
# from app.models.fii_fundoimob_cotacao import FiiFundoImobCotacao
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_datahora import pegar_data_atual, pegar_data_hora_atual


router = _fastapi.APIRouter(prefix="/FiiFundoImob", tags=['admin_fundoimob'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @login_required
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
async def get_index():
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="admin_fundoimob.html")
    return {"result": "ok"}


# @bp_admin_fundoimob.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_grid(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
#
#         rows = FiiFundoImob.buscar_todos()
#
#         lista = [
#             [
#                 str(row['CODIGO']) if row['CODIGO'] else '',
#                 str(row['NOME']),
#                 str(row['RAZAOSOCIAL']),
#                 str(row['CNPJ']) if row['CNPJ'] else '',
#                 FiiFundoImob.descricao_situacao(situacao=str(row['SITUACAO'])),
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
# @bp_admin_fundoimob.route('/salvar', methods=['GET', 'POST'])
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
#             id_fundo = data.get('fiiFundoId')
#             id_admin = data.get('fiiFundoIdAdmin')
#             id_tipo = data.get('fiiFundoIdTipo')
#             nome = data.get('fiiFundoNome')
#             razao_social = data.get('fiiFundoRazao')
#             cnpj = data.get('fiiFundoCNPJ')
#             codigo = data.get('fiiFundoCodigo')
#             codigo_isin = data.get('fiiFundoIsin')
#             situacao = data.get('fiiFundoSituacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not nome: return make_response(get_json_retorno_metodo(msg='Nome não informado.'), 200)
#         if not razao_social: return make_response(get_json_retorno_metodo(msg='Razão Social não informado.'), 200)
#         if not cnpj: return make_response(get_json_retorno_metodo(msg='CNPJ não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Codigo não informado.'), 200)
#
#         if not id_fundo:
#             if FiiFundoImob.buscar_por_codigo(codigo=str(codigo)):
#                 return make_response(get_json_retorno_metodo(msg='Fundo já cadastrado.'), 200)
#
#         fundo = FiiFundoImob()
#         if id_fundo:
#             fundo = FiiFundoImob.get_by_id(id=int(id_fundo))
#             if not fundo: return make_response(get_json_retorno_metodo(msg='Fundo não localizada.'), 200)
#
#         fundo.id_tipo = int(id_tipo) if id_tipo else None
#         fundo.id_admin = int(id_admin) if id_admin else None
#         fundo.nome = str(nome)
#         fundo.razao_social = str(razao_social)
#         fundo.cnpj = str(cnpj)
#         fundo.codigo = str(codigo)
#         fundo.codigo_isin = str(codigo_isin) if codigo_isin else None
#         fundo.situacao = str(situacao)
#         fundo.salvar()
#
#         cotacao = FiiFundoImobCotacao.get_by_fundo(id_fundo=int(fundo.id))
#         if not cotacao:
#             cotacao = FiiFundoImobCotacao(id_fundo=int(fundo.id))
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
# @bp_admin_fundoimob.route('/carregar', methods=['GET', 'POST'])
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
#             id_fundo = data.get('fiiFundoId')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_fundo:
#             return make_response(get_json_retorno_dados(msg='Id. Fundo Imob. não informado.'), 200)
#
#         fundo = FiiFundoImob.buscar_por_id(id=int(id_fundo))
#         if not fundo:
#             return make_response(get_json_retorno_dados(msg='Fundo Imob. não localizada!'), 200)
#
#         dados = dict(
#             {
#                 "Id": str(fundo['ID']),
#                 "Nome": str(fundo['NOME']) if fundo['NOME'] else '',
#                 "RazaoSocial": str(fundo['RAZAOSOCIAL']) if fundo['RAZAOSOCIAL'] else '',
#                 "CNPJ": str(fundo['CNPJ']) if fundo['CNPJ'] else '',
#                 "Codigo": str(fundo['CODIGO']) if fundo['CODIGO'] else '',
#                 "Isin": str(fundo['CODISIN']) if fundo['CODISIN'] else '',
#                 "Situacao": str(fundo['SITUACAO']) if fundo['SITUACAO'] else '',
#                 "AdminId": str(fundo['IDFIITIPO']) if fundo['IDFIITIPO'] else '',
#                 "TipoId": str(fundo['IDFIIADMIN']) if fundo['IDFIIADMIN'] else '',
#             }
#         )
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
