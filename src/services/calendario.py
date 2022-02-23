# # -*- coding: utf-8 -*-
# import sys
# import os
# from flask import Blueprint, render_template, request, make_response
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.acao_empresa_provento import ACAOEmpresaProvento
# from app.models.fii_fundoimob_provento import FiiFundoImobProvento
# from app.models.bdr_empresa_provento import BDREmpresaProvento
# from app.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamento
# from app.models.usuario_fii_fundoimob_lancamento import UsuarioFiiFundoImobLancamento
# from app.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamento
# from app.models.usuario_bdr_empresa_lancamento import UsuarioBDREmpresaLancamento
# from app.util.util_json import get_json_retorno_grid
# from app.util.util_formatacao import decimal_to_str, inteiro_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str
#
#
# bp_calendario = Blueprint('calendario', __name__, url_prefix='/calendario')
#
#
# @bp_calendario.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# # @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     return render_template(template_name_or_list="calendario.html")
#
#
# def format_data_xml(data: str = ''):
#     return converter_datetime_str(data=converter_str_to_datetime(data=data, fmt='%Y%m%d'), fmt='%Y-%m-%d')
#
#
# @bp_calendario.route('/lista', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista():
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
#             tipo_invest = data.get('TipoInvest')
#             tipo_lista = data.get('TpLista')
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         dt_ini = str(dt_ini).replace('-', '') if dt_ini is not None else dt_ini
#         dt_fim = str(dt_fim).replace('-', '') if dt_fim is not None else dt_fim
#
#         if not tipo_lista: return make_response(get_json_retorno_grid(msg='Tipo Lista não informado.'), 200)
#         if not dt_ini: return make_response(get_json_retorno_grid(msg='Data Inicio não informada.'), 200)
#         if not dt_fim: return make_response(get_json_retorno_grid(msg='Data Fim não informada.'), 200)
#
#         lista = []
#
#         if str(tipo_lista) == 'DTEX' or str(tipo_lista) == 'DTPAGTO' or str(tipo_lista) == 'OUTROS':
#
#             id_empr = None
#             codigo = None
#             dt_ex_ini = None
#             dt_ex_fim = None
#             dt_pagto_ini = None
#             dt_pagto_fim = None
#
#             if str(tipo_lista) == 'DTEX' or str(tipo_lista) == 'OUTROS':
#                 dt_ex_ini = dt_ini
#                 dt_ex_fim = dt_fim
#             elif str(tipo_lista) == 'DTPAGTO':
#                 dt_pagto_ini = dt_ini
#                 dt_pagto_fim = dt_fim
#
#             if str(tipo_lista) == 'DTEX' or str(tipo_lista) == 'DTPAGTO':
#
#                 if tipo_invest == 'ACAO':
#                     rows = ACAOEmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='D', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # D-Dividendos
#                     lista += [[str(row['ID']), str(row['CODATIVO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = ACAOEmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='J', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # J-Juros Sobre Capital Proprio
#                     lista += [[str(row['ID']), str(row['CODATIVO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = ACAOEmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='R', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # R-Restituição de Capital Social em Dinheiro
#                     lista += [[str(row['ID']), str(row['CODATIVO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#
#                 elif tipo_invest == 'FII':
#                     rows = FiiFundoImobProvento.buscar_todos(id_fundo=id_empr, codigo=codigo, tipo='R', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # R-Rendimento
#                     lista += [[str(row['ID']), str(row['CODIGOFUNDO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#
#                 elif tipo_invest == 'BDR':
#                     rows = BDREmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='D', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # D-Dividendos
#                     lista += [[str(row['ID']), str(row['CODIGOBDR']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = BDREmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='J', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # J-Juros Sobre Capital Proprio
#                     lista += [[str(row['ID']), str(row['CODIGOBDR']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = BDREmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='R', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # R-Restituição de Capital Social em Dinheiro
#                     lista += [[str(row['ID']), str(row['CODIGOBDR']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#
#             elif str(tipo_lista) == 'OUTROS':
#
#                 if tipo_invest == 'ACAO':
#                     rows = ACAOEmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='E', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # E-DESDOBRAMENTO
#                     lista += [[str(row['ID']), str(row['CODATIVO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = ACAOEmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='G', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # G-GRUPAMENTO
#                     lista += [[str(row['ID']), str(row['CODATIVO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = ACAOEmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='B', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # B-BONIFICACAO
#                     lista += [[str(row['ID']), str(row['CODATIVO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#
#                 elif tipo_invest == 'FII':
#                     rows = FiiFundoImobProvento.buscar_todos(id_fundo=id_empr, codigo=codigo, tipo='E', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # E-DESDOBRAMENTO
#                     lista += [[str(row['ID']), str(row['CODIGOFUNDO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = FiiFundoImobProvento.buscar_todos(id_fundo=id_empr, codigo=codigo, tipo='G', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # G-GRUPAMENTO
#                     lista += [[str(row['ID']), str(row['CODIGOFUNDO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = FiiFundoImobProvento.buscar_todos(id_fundo=id_empr, codigo=codigo, tipo='B', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # B-BONIFICACAO
#                     lista += [[str(row['ID']), str(row['CODIGOFUNDO']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#
#                 elif tipo_invest == 'BDR':
#                     rows = BDREmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='E', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # E-DESDOBRAMENTO
#                     lista += [[str(row['ID']), str(row['CODIGOBDR']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = BDREmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='G', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # G-GRUPAMENTO
#                     lista += [[str(row['ID']), str(row['CODIGOBDR']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#                     rows = BDREmpresaProvento.buscar_todos(id_empr=id_empr, codigo=codigo, tipo='B', dt_ex_ini=dt_ex_ini, dt_ex_fim=dt_ex_fim, dt_pagto_ini=dt_pagto_ini, dt_pagto_fim=dt_pagto_fim)  # B-BONIFICACAO
#                     lista += [[str(row['ID']), str(row['CODIGOBDR']), str(row['TIPO']), format_data_xml(data=str(row['DATAEX'])), format_data_xml(data=str(row['DATAPAGTO'])), str(row['VLRPRECO'])] for row in rows]
#
#         elif tipo_lista == 'COMPRA' or tipo_lista == 'VENDA':
#
#             codigo = None
#             tipo = None
#             ordem = None
#             id_corretora = None
#             id_usuario = current_user.id
#
#             if tipo_lista == 'COMPRA': tipo = 'C'
#             if tipo_lista == 'VENDA': tipo = 'V'
#
#             if tipo_invest == 'ACAO':
#                 rows = UsuarioACAOEmpresaLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim, tipo=tipo, ordem=ordem, id_corretora=id_corretora)
#                 lista += [[str(row['ID']), str(row['CODIGOATIVO']), UsuarioACAOEmpresaLancamento.descricao_tipo(tipo=str(row['TIPO'])), format_data_xml(data=str(row['DATA'])), inteiro_to_str(valor=row['QUANT']), decimal_to_str(valor=row['VLRPRECO']), decimal_to_str(valor=row['TOTVLR'])] for row in rows]
#
#             elif tipo_invest == 'FII':
#                 rows = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim, tipo=tipo, ordem=ordem, id_corretora=id_corretora)
#                 lista += [[str(row['ID']), str(row['CODIGOFUNDO']), UsuarioFiiFundoImobLancamento.descricao_tipo(tipo=str(row['TIPO'])), format_data_xml(data=str(row['DATA'])), inteiro_to_str(valor=row['QUANT']), decimal_to_str(valor=row['VLRPRECO']), decimal_to_str(valor=row['TOTVLR'])] for row in rows]
#
#             elif tipo_invest == 'ETF':
#                 rows = UsuarioETFIndiceLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim, tipo=tipo, ordem=ordem, id_corretora=id_corretora)
#                 lista += [[str(row['ID']), str(row['CODIGOINDICE']), UsuarioETFIndiceLancamento.descricao_tipo(tipo=str(row['TIPO'])), format_data_xml(data=str(row['DATA'])), inteiro_to_str(valor=row['QUANT']), decimal_to_str(valor=row['VLRPRECO']), decimal_to_str(valor=row['TOTVLR'])] for row in rows]
#
#             elif tipo_invest == 'BDR':
#                 rows = UsuarioBDREmpresaLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim, tipo=tipo, ordem=ordem, id_corretora=id_corretora)
#                 lista += [[str(row['ID']), str(row['CODIGOBDR']), UsuarioBDREmpresaLancamento.descricao_tipo(tipo=str(row['TIPO'])), format_data_xml(data=str(row['DATA'])), inteiro_to_str(valor=row['QUANT']), decimal_to_str(valor=row['VLRPRECO']), decimal_to_str(valor=row['TOTVLR'])] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_calendario.route('/grid', methods=['GET', 'POST'])
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
#             tipo_invest = data.get('TipoInvest')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not codigo:
#             return make_response(get_json_retorno_grid(msg='Ativo não informado.'), 200)
#
#         lista = []
#
#         if tipo_invest == 'ACAO':
#             rows = ACAOEmpresaProvento.buscar_todos(codigo=codigo)
#             lista = [[str(row['ID']), str(row['CODATIVO']), str(row['TIPO']), str(row['DATAEX']), str(row['DATAPAGTO']), decimal_to_str(valor=row['VLRPRECO'])] for row in rows]
#
#         elif tipo_invest == 'FII':
#             rows = FiiFundoImobProvento.buscar_todos(codigo=codigo)
#             lista = [[str(row['ID']), str(row['CODIGOFUNDO']), str(row['TIPO']), str(row['DATAEX']), str(row['DATAPAGTO']), decimal_to_str(valor=row['VLRPRECO'])] for row in rows]
#
#         elif tipo_invest == 'BDR':
#             rows = BDREmpresaProvento.buscar_todos(codigo=codigo)
#             lista = [[str(row['ID']), str(row['CODIGOBDR']), str(row['TIPO']), str(row['DATAEX']), str(row['DATAPAGTO']), decimal_to_str(valor=row['VLRPRECO'])] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
