# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.acao_empresa_provento import ACAOEmpresaProvento
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="/empresaProv", tags=['admin_empresa_proventos'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
# @login_required
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
async def get_index(request: _fastapi.Request):
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="admin_empresa_proventos.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


# @bp_admin_empresa_proventos.route('/grid', methods=['GET', 'POST'])
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
#             codigo = data.get('CodAtivo')
#             tipo = data.get('Tipo')
#             dt_ex_ini = data.get('ProvDtExIni')
#             dt_ex_fim = data.get('ProvDtExFim')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         rows = ACAOEmpresaProvento.buscar_todos(codigo=codigo, tipo=tipo, dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim)
#
#         lista = [[str(row['DATAEX']), str(row['DATAPAGTO']), str(row['CODATIVO']), ACAOEmpresaProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['VLRPRECO']) if row['VLRPRECO'] else '0', str(row['ID'])] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_empresa_proventos.route('/salvar', methods=['GET', 'POST'])
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
#             id_empresa_provento = data.get('Id')
#             codigo = data.get('CodAtivo')
#             tipo = data.get('Tipo')
#             categoria = data.get('Categ')
#             data_aprov = data.get('DtAprov')
#             data_com = data.get('DtCom')
#             data_ex = data.get('DtEx')
#             data_pagto = data.get('DtPagto')
#             vlr_preco = data.get('Preco')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Ativo não informado.'), 200)
#         if not data_aprov: return make_response(get_json_retorno_metodo(msg='Dt. Aprov. não informada.'), 200)
#         if not data_ex: return make_response(get_json_retorno_metodo(msg='Dt. Ex. não informada.'), 200)
#         if not vlr_preco: return make_response(get_json_retorno_metodo(msg='Preço não informado.'), 200)
#
#         if data_aprov: data_aprov = str(data_aprov).replace('-', '')
#         if data_com: data_com = str(data_com).replace('-', '')
#         if data_ex: data_ex = str(data_ex).replace('-', '')
#         if data_pagto: data_pagto = str(data_pagto).replace('-', '')
#
#         ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#         if not ativo:
#             return make_response(get_json_retorno_metodo(msg='Ativo não localizado.'), 200)
#
#         if not ativo.codigo_isin:
#             return make_response(get_json_retorno_metodo(msg='Cod ISIN do Ativo não localizado.'), 200)
#
#         empr_prov = None
#         if id_empresa_provento:
#             empr_prov = ACAOEmpresaProvento.get_by_id(id=int(id_empresa_provento))
#         else:
#             empr_prov = ACAOEmpresaProvento()
#
#         if not empr_prov:
#             return make_response(get_json_retorno_metodo(msg='Empresa Provento não localizada!'), 200)
#
#         empr_prov.id_empresa = int(ativo.id_empresa)  # if empr_prov.id_empresa and int(empr_prov.id_empresa) != int(ativo.id_empresa) else empr_prov.id_empresa
#         empr_prov.tipo = str(tipo)
#         empr_prov.categoria = str(categoria)
#         empr_prov.codigo_isin = str(ativo.codigo_isin)
#         empr_prov.data_aprov = str(data_aprov) if data_aprov else ''
#         empr_prov.data_com = str(data_com) if data_com else ''
#         empr_prov.data_ex = str(data_ex) if data_ex else ''
#         empr_prov.data_pagto = str(data_pagto) if data_aprov else ''
#         empr_prov.vlr_preco = float(str(vlr_preco).replace('.', '').replace(',', '.')) if vlr_preco else 0.0
#         empr_prov.situacao = 'A' # A-Ativo
#         empr_prov.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_empresa_proventos.route('/carregar', methods=['GET', 'POST'])
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
#             id_empresa_provento = data.get('IdEmprProv')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_empresa_provento: return make_response(get_json_retorno_dados(msg='Id. Empresa Provento não informado.'), 200)
#
#         empr_prov = ACAOEmpresaProvento.buscar_por_id(id=int(id_empresa_provento))
#         if not empr_prov:
#             return make_response(get_json_retorno_dados(msg='Empresa Provento não localizada!'), 200)
#
#         dados = dict(
#             {
#                 "Id": str(empr_prov['ID']),
#                 "CodAtivo": str(empr_prov['CODATIVO']),
#                 "Tipo": str(empr_prov['TIPO']),
#                 "Categ": str(empr_prov['CATEGORIA']),
#                 "DtAprov": converter_datetime_str(data=converter_str_to_datetime(data=empr_prov['DATAAPROV'], fmt='%Y%m%d'), fmt='%Y-%m-%d') if empr_prov['DATAAPROV'] else '',
#                 "DtCom": converter_datetime_str(data=converter_str_to_datetime(data=empr_prov['DATACOM'], fmt='%Y%m%d'), fmt='%Y-%m-%d') if empr_prov['DATACOM'] else '',
#                 "DtEx": converter_datetime_str(data=converter_str_to_datetime(data=empr_prov['DATAEX'], fmt='%Y%m%d'), fmt='%Y-%m-%d') if empr_prov['DATAEX'] else '',
#                 "DtPagto": converter_datetime_str(data=converter_str_to_datetime(data=empr_prov['DATAPAGTO'], fmt='%Y%m%d'), fmt='%Y-%m-%d') if empr_prov['DATAPAGTO'] else '',
#                 "Preco": str(empr_prov['VLRPRECO']),
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
# @bp_admin_empresa_proventos.route('/excluir', methods=['GET', 'POST'])
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
#             id_empresa_provento = data.get('EmprProvId')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_empresa_provento: return make_response(get_json_retorno_metodo(msg='Id. Empresa Provento não informado.'), 200)
#
#         empr_prov = ACAOEmpresaProvento.get_by_id(id=int(id_empresa_provento))
#         if not empr_prov:
#             return make_response(get_json_retorno_metodo(msg='Empresa Provento não localizada!'), 200)
#
#         empr_prov.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Operação Excluída!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
