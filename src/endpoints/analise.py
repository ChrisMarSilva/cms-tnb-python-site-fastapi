# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from copy import deepcopy
# from app.models.log_erro import LogErro
# from app.models.usuario_config import UsuarioConfig
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.acao_empresa_ativo_cotacao import ACAOEmpresaAtivoCotacao
# from app.models.acao_empresa_ativo_cotacao_hist import ACAOEmpresaAtivoCotacaoHist
# from app.models.fii_fundoimob import FiiFundoImob
# from app.models.fii_fundoimob_cotacao import FiiFundoImobCotacao
# from app.models.etf_indice import ETFIndice
# from app.models.etf_indice_cotacao import ETFIndiceCotacao
# from app.models.bdr_empresa import BDREmpresa
# from app.models.bdr_empresa_cotacao import BDREmpresaCotacao
# from app.models.usuario_bdr_empresa_lancamento import UsuarioBDREmpresaLancamento
# from app.models.cripto_empresa import CriptoEmpresa
# from app.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamento
# from app.models.usuario_acao_empresa_operacao import UsuarioACAOEmpresaOperacao
# from app.models.usuario_acao_empresa_provento import UsuarioACAOEmpresaProvento
# from app.models.usuario_fii_fundoimob_lancamento import UsuarioFiiFundoImobLancamento
# from app.models.usuario_fii_fundoimob_provento import UsuarioFiiFundoImobProvento
# from app.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamento
# from app.models.usuario_etf_indice_operacao import UsuarioETFIndiceOperacao
# from app.models.usuario_bdr_empresa_operacao import UsuarioBDREmpresaOperacao
# from app.models.usuario_bdr_empresa_provento import UsuarioBDREmpresaProvento
# from app.models.usuario_cripto_lancamento import UsuarioCriptoLancamento
# from app.models.usuario_carteira import UsuarioCarteira
# from app.models.usuario_carteira_acao import UsuarioCarteiraAcao
# from app.models.usuario_carteira_fii import UsuarioCarteiraFii
# from app.models.usuario_carteira_etf import UsuarioCarteiraEtf
# from app.models.usuario_carteira_bdr import UsuarioCarteiraBdr
# from app.models.usuario_carteira_cripto import UsuarioCarteiraCripto
# from app.models.usuario_carteira_projecao import UsuarioCarteiraProjecao
# from app.models.usuario_carteira_projecao_item import UsuarioCarteiraProjecaoItem
# from app.models.usuario_radar_acao import UsuarioRadarAcao
# from app.models.usuario_radar_fii import UsuarioRadarFii
# from app.models.usuario_radar_etf import UsuarioRadarEtf
# from app.models.usuario_radar_bdr import UsuarioRadarBdr
# from app.models.usuario_radar_cripto import UsuarioRadarCripto
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_formatacao import decimal_to_str, decimal_cripto_to_str, decimal_prov_to_str, inteiro_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str, pegar_data_atual, buscar_nome_mes_resumido, adicionar_dias
#
# bp_analise = Blueprint('analise', __name__, url_prefix='/Analise')
#
#
# @bp_analise.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#
#     id_usuario = current_user.id
#     gerar_portoflio = False
#     if not gerar_portoflio and UsuarioACAOEmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#     if not gerar_portoflio and UsuarioFiiFundoImobLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#     if not gerar_portoflio and UsuarioETFIndiceLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#     if not gerar_portoflio and UsuarioBDREmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#     if not gerar_portoflio and UsuarioCriptoLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#
#     return render_template(template_name_or_list="analise.html", gerar_portoflio=gerar_portoflio)
#
#
# @bp_analise.route('/gridOper', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_oper():
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
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not codigo:
#             return make_response(get_json_retorno_grid(msg='Código do Ativo não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         tipo_invest = ''
#         operacoes = None
#
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=codigo):
#             tipo_invest = 'ACAO'
#             operacoes = UsuarioACAOEmpresaOperacao.buscar_todos(id_usuario=id_usuario, codigo=codigo)
#         elif FiiFundoImob.get_by_codigo(codigo=codigo):
#             tipo_invest = 'FII'
#             operacoes = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo)
#         elif ETFIndice.get_by_codigo(codigo=codigo):
#             tipo_invest = 'ETF'
#             operacoes = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, codigo=codigo)
#         elif BDREmpresa.get_by_codigo(codigo=codigo):
#             tipo_invest = 'BDR'
#             operacoes = UsuarioBDREmpresaOperacao.buscar_todos(id_usuario=id_usuario, codigo=codigo)
#         elif CriptoEmpresa.get_by_codigo(codigo=codigo):
#             tipo_invest = 'CRIPTO'
#             operacoes = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo)
#
#         if not tipo_invest:
#             return make_response(get_json_retorno_grid(msg='Código do Ativo não localizado.'), 200)
#
#         if not operacoes:
#             return make_response(get_json_retorno_grid(rslt='OK'), 200)
#
#         lista = []
#         qtde_compra = 0.0
#         qtde_bonus = 0.0
#         qtde_venda = 0.0
#         vlr_preco_medio = 0.0
#
#         for oper in operacoes:
#
#             if str(oper['TIPO']) == 'C':
#                 qtde_compra += float(oper['QUANT'])
#             elif str(oper['TIPO']) == 'B':
#                 qtde_bonus += float(oper['QUANT'])
#             elif str(oper['TIPO']) == 'V':
#                 qtde_venda += float(oper['QUANT'])
#                 if qtde_compra + qtde_bonus == qtde_venda:
#                     qtde_compra = 0.0
#                     qtde_bonus = 0.0
#                     qtde_venda = 0.0
#
#             vlr_preco_medio = float(oper['VLRPRECOMEDIO'])
#
#             descr_valorizacao = ""
#             if str(oper['TIPO'])  == "V" or str(oper['TIPO'])  == "P":
#                 vlr_valorizacao = 0.0
#                 perc_valorizacao = 0.0
#                 if tipo_invest == 'ACAO':
#                     vlr_valorizacao = UsuarioACAOEmpresaOperacao.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                     perc_valorizacao = UsuarioACAOEmpresaOperacao.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 elif tipo_invest == 'FII':
#                     vlr_valorizacao = UsuarioFiiFundoImobLancamento.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                     perc_valorizacao = UsuarioFiiFundoImobLancamento.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 elif tipo_invest == 'ETF':
#                     vlr_valorizacao = UsuarioETFIndiceOperacao.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                     perc_valorizacao = UsuarioETFIndiceOperacao.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 elif tipo_invest == 'BDR':
#                     vlr_valorizacao = UsuarioBDREmpresaOperacao.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                     perc_valorizacao = UsuarioBDREmpresaOperacao.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 elif tipo_invest == 'CRIPTO':
#                     vlr_valorizacao = UsuarioCriptoLancamento.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                     perc_valorizacao = UsuarioCriptoLancamento.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 descr_valorizacao = decimal_to_str(valor=float(vlr_valorizacao)) + " ( " + decimal_to_str(valor=float(perc_valorizacao)) + "% )"
#
#             if tipo_invest == 'ACAO':
#                 lista.append([UsuarioACAOEmpresaOperacao.descricao_tipo(tipo=str(oper['TIPO']), troca=str(oper['TROCA'])), 'Oper. ' + UsuarioACAOEmpresaOperacao.descricao_categoria(categoria=str(oper['CATEGORIA'])), str(oper['NOMECORRETORA']) if oper['NOMECORRETORA'] else '', converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'), fmt='%d/%m/%Y'), inteiro_to_str(valor=oper['QUANT']).replace(',00', ''), decimal_to_str(valor=oper['VLRCUSTO']), decimal_to_str(valor=oper['VLRPRECOMEDIO']), decimal_to_str(valor=oper['TOTVLRCUSTO']), descr_valorizacao])
#             elif tipo_invest == 'FII':
#                 lista.append([UsuarioFiiFundoImobLancamento.descricao_tipo(tipo=str(oper['TIPO']), troca=str(oper['TROCA'])), '', str(oper['NOMECORRETORA']) if oper['NOMECORRETORA'] else '', converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'),fmt='%d/%m/%Y'), inteiro_to_str(valor=oper['QUANT']).replace(',00', ''), decimal_to_str(valor=oper['VLRCUSTO']), decimal_to_str(valor=oper['VLRPRECOMEDIO']), decimal_to_str(valor=oper['TOTVLRCUSTO']), descr_valorizacao])
#             elif tipo_invest == 'ETF':
#                 lista.append([UsuarioETFIndiceOperacao.descricao_tipo(tipo=str(oper['TIPO']), troca=str(oper['TROCA'])), 'Oper. ' + UsuarioETFIndiceOperacao.descricao_categoria(categoria=str(oper['CATEGORIA'])), str(oper['NOMECORRETORA']) if oper['NOMECORRETORA'] else '', converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'), fmt='%d/%m/%Y'), inteiro_to_str(valor=oper['QUANT']).replace(',00', ''), decimal_to_str(valor=oper['VLRCUSTO']), decimal_to_str(valor=oper['VLRPRECOMEDIO']), decimal_to_str(valor=oper['TOTVLRCUSTO']), descr_valorizacao])
#             elif tipo_invest == 'BDR':
#                 lista.append([UsuarioBDREmpresaOperacao.descricao_tipo(tipo=str(oper['TIPO']), troca=str(oper['TROCA'])), 'Oper. ' + UsuarioBDREmpresaOperacao.descricao_categoria(categoria=str(oper['CATEGORIA'])), str(oper['NOMECORRETORA']) if oper['NOMECORRETORA'] else '', converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'), fmt='%d/%m/%Y'), inteiro_to_str(valor=oper['QUANT']).replace(',00', ''), decimal_to_str(valor=oper['VLRCUSTO']), decimal_to_str(valor=oper['VLRPRECOMEDIO']), decimal_to_str(valor=oper['TOTVLRCUSTO']), descr_valorizacao])
#             elif tipo_invest == 'CRIPTO':
#                 lista.append([UsuarioCriptoLancamento.descricao_tipo(tipo=str(oper['TIPO'])), '', str(oper['NOMECORRETORA']) if oper['NOMECORRETORA'] else '', converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'),fmt='%d/%m/%Y'), decimal_cripto_to_str(valor=float(oper['QUANT'])), decimal_cripto_to_str(valor=oper['VLRCUSTO']), decimal_cripto_to_str(valor=oper['VLRPRECOMEDIO']), decimal_to_str(valor=oper['TOTVLRCUSTO']), descr_valorizacao])
#
#         if int(qtde_compra) + float(qtde_bonus) > float(qtde_venda):
#             cot = None
#             if tipo_invest == 'ACAO':
#                 cot = ACAOEmpresaAtivoCotacao.buscar_por_codigo(codigo=codigo)
#             elif tipo_invest == 'FII':
#                 cot = FiiFundoImobCotacao.buscar_por_codigo(codigo=codigo)
#             elif tipo_invest == 'ETF':
#                 cot = ETFIndiceCotacao.buscar_por_codigo(codigo=codigo)
#             elif tipo_invest == 'BDR':
#                 cot = BDREmpresaCotacao.buscar_por_codigo(codigo=codigo)
#             elif tipo_invest == 'CRIPTO':
#                 cot = CriptoEmpresa.buscar_por_codigo(codigo=codigo)
#             vlr_cotacao = float(cot['VLRPRECOFECHAMENTO']) if cot and cot['VLRPRECOFECHAMENTO'] else 0.00
#
#             qtde_saldo = float(qtde_compra) - float(qtde_venda)
#             tot_investido = 0.0
#             if vlr_preco_medio > 0.0 and qtde_saldo > 0:
#                 tot_investido = (qtde_saldo + qtde_bonus) * vlr_preco_medio
#             tot_atual = 0.0
#             if (qtde_saldo + qtde_bonus > 0) and vlr_cotacao and vlr_cotacao > 0.0:
#                 tot_atual = (qtde_saldo + qtde_bonus) * vlr_cotacao
#             vlr_valorizacao = tot_atual - tot_investido
#             perc_valorizacao = 0.0
#             if vlr_valorizacao != 0.0 and tot_investido > 0.0:
#                 perc_valorizacao = (vlr_valorizacao / tot_investido) * 100
#             elif vlr_valorizacao != 0.0 and tot_investido == 0.0 and qtde_bonus > 0.0 and vlr_preco_medio > 0.0:
#                 perc_valorizacao = (vlr_valorizacao / (qtde_bonus * vlr_preco_medio)) * 100
#             descr_valorizacao = decimal_to_str(valor=float(vlr_valorizacao)) + " ( " + decimal_to_str(valor=float(perc_valorizacao)) + "% )"
#             if tipo_invest == 'CRIPTO':
#                 lista.append(['Projetado', '', '', pegar_data_atual(fmt='%d/%m/%Y'), decimal_cripto_to_str(valor=float(qtde_saldo) + float(qtde_bonus)), decimal_cripto_to_str(valor=float(vlr_cotacao)), decimal_cripto_to_str(valor=float(vlr_preco_medio)), decimal_to_str(valor=float(tot_atual)), descr_valorizacao])
#             else:
#                 lista.append(['Projetado', '', '', pegar_data_atual(fmt='%d/%m/%Y'), inteiro_to_str(valor=float(qtde_saldo) + float(qtde_bonus)), decimal_to_str(valor=float(vlr_cotacao)), decimal_to_str(valor=float(vlr_preco_medio)), decimal_to_str(valor=float(tot_atual)), descr_valorizacao])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/gridProv', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_prov():
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
#             codigo = data.get('CodAtivo')
#             tipo = data.get('TipoRend')
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#             id_corretora = data.get('Corretora')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         dt_ini = str(dt_ini).replace('-', '') if dt_ini is not None else dt_ini
#         dt_fim = str(dt_fim).replace('-', '') if dt_fim is not None else dt_fim
#
#         tipo_invest = ''
#         if codigo and codigo == 'ACAO': tipo_invest = 'ACAO'
#         if codigo and codigo == 'FII': tipo_invest = 'FII'
#         if codigo and codigo == 'BDR': tipo_invest = 'BDR'
#         if tipo_invest: codigo = ''
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         if tipo_invest == '' or str(tipo_invest) == 'ACAO':
#             if str(tipo) == "" or str(tipo) == "D" or str(tipo) == "J" or str(tipo) == "R":
#                 rows = UsuarioACAOEmpresaProvento.buscar_todos(id_usuario=id_usuario, codigo=codigo, tipo=tipo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#                 for prov in rows:
#                     lista.append([converter_datetime_str(data=converter_str_to_datetime(data=prov['DATAPAGTO'], fmt='%Y%m%d'), fmt='%d/%m/%Y'), str(prov['CODIGOATIVO']), UsuarioACAOEmpresaProvento.descricao_tipo(tipo=str(prov['TIPO'])), str(prov['NOMECORRETORA']) if prov['NOMECORRETORA'] else '', inteiro_to_str(valor=prov['QUANTIDADE']), decimal_prov_to_str(valor=prov['VLRPRECO']), decimal_to_str(valor=prov['TOTVLR'])])
#
#         if tipo_invest == '' or str(tipo_invest) == 'FII':
#             if str(tipo) == "" or str(tipo) == "FR":
#                 if str(tipo) == "FR": tipo = "R" # FR - FII RENDIMENTO
#                 rows = UsuarioFiiFundoImobProvento.buscar_todos(id_usuario=id_usuario, codigo=codigo, tipo=tipo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#                 for prov in rows:
#                     lista.append([converter_datetime_str(data=converter_str_to_datetime(data=prov['DATAPAGTO'], fmt='%Y%m%d'), fmt='%d/%m/%Y'), str(prov['CODIGOFUNDO']), UsuarioFiiFundoImobProvento.descricao_tipo(tipo=str(prov['TIPO'])), str(prov['NOMECORRETORA']) if prov['NOMECORRETORA'] else '', inteiro_to_str(valor=prov['QUANTIDADE']), decimal_prov_to_str(valor=prov['VLRPRECO']), decimal_to_str(valor=prov['TOTVLR'])])
#
#         if tipo_invest == '' or str(tipo_invest) == 'BDR':
#             if str(tipo) == "" or str(tipo) == "D" or str(tipo) == "J" or str(tipo) == "R":
#                 rows = UsuarioBDREmpresaProvento.buscar_todos(id_usuario=id_usuario, codigo=codigo, tipo=tipo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#                 for prov in rows:
#                     lista.append([converter_datetime_str(data=converter_str_to_datetime(data=prov['DATAPAGTO'], fmt='%Y%m%d'), fmt='%d/%m/%Y'), str(prov['CODIGOBDR']), UsuarioBDREmpresaProvento.descricao_tipo(tipo=str(prov['TIPO'])), str(prov['NOMECORRETORA']) if prov['NOMECORRETORA'] else '', inteiro_to_str(valor=prov['QUANTIDADE']), decimal_prov_to_str(valor=prov['VLRPRECO']), decimal_to_str(valor=prov['TOTVLR'])])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/gridCalProvOld', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_cal_prov_old():
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
#             ano = data.get('Ano')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not ano:
#             return make_response(get_json_retorno_grid(msg='Ano não informado.'), 200)
#
#         id_usuario = current_user.id
#         vlr_tot_jan, vlr_tot_fev, vlr_tot_mar, vlr_tot_abr, vlr_tot_mai, vlr_tot_jun, vlr_tot_jul, vlr_tot_ago, vlr_tot_set, vlr_tot_out, vlr_tot_nov, vlr_tot_dez, vlr_tot_total, vlr_tot_media = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#         lista = []
#
#         ativos = ACAOEmpresaAtivo.buscar_todos_codigos_proventos_com_fiis_bdrs(id_usuario=id_usuario, dt_ini=str(ano) + '0101', dt_fim=str(ano) + '1231')
#         for ativo in ativos:
#
#             id_ativo = int(ativo['ID'])
#             codigo = str(ativo['CODIGO'])
#             tipo_invest = str(ativo['TIPO'])
#
#             vlr_jan, vlr_fev, vlr_mar, vlr_abr, vlr_mai, vlr_jun, vlr_jul, vlr_ago, vlr_set, vlr_out, vlr_nov, vlr_dez = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#
#             if tipo_invest == 'ACAO':
#                 vlr_jan = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0101', dt_fim=str(ano) + '0131')
#                 vlr_fev = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0201', dt_fim=str(ano) + '0231')
#                 vlr_mar = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0301', dt_fim=str(ano) + '0331')
#                 vlr_abr = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0401', dt_fim=str(ano) + '0431')
#                 vlr_mai = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0501', dt_fim=str(ano) + '0531')
#                 vlr_jun = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0601', dt_fim=str(ano) + '0631')
#                 vlr_jul = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0701', dt_fim=str(ano) + '0731')
#                 vlr_ago = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0801', dt_fim=str(ano) + '0831')
#                 vlr_set = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0901', dt_fim=str(ano) + '0931')
#                 vlr_out = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '1001', dt_fim=str(ano) + '1031')
#                 vlr_nov = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '1101', dt_fim=str(ano) + '1131')
#                 vlr_dez = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '1201', dt_fim=str(ano) + '1231')
#             elif tipo_invest == 'FII':
#                 vlr_jan = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0101', dt_fim=str(ano)+'0131')
#                 vlr_fev = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0201', dt_fim=str(ano)+'0231')
#                 vlr_mar = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0301', dt_fim=str(ano)+'0331')
#                 vlr_abr = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0401', dt_fim=str(ano)+'0431')
#                 vlr_mai = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0501', dt_fim=str(ano)+'0531')
#                 vlr_jun = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0601', dt_fim=str(ano)+'0631')
#                 vlr_jul = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0701', dt_fim=str(ano)+'0731')
#                 vlr_ago = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0801', dt_fim=str(ano)+'0831')
#                 vlr_set = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0901', dt_fim=str(ano)+'0931')
#                 vlr_out = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'1001', dt_fim=str(ano)+'1031')
#                 vlr_nov = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'1101', dt_fim=str(ano)+'1131')
#                 vlr_dez = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'1201', dt_fim=str(ano)+'1231')
#             elif tipo_invest == 'BDR':
#                 vlr_jan = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '0101', dt_fim=str(ano) + '0131')
#                 vlr_fev = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '0201', dt_fim=str(ano) + '0231')
#                 vlr_mar = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '0301', dt_fim=str(ano) + '0331')
#                 vlr_abr = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '0401', dt_fim=str(ano) + '0431')
#                 vlr_mai = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '0501', dt_fim=str(ano) + '0531')
#                 vlr_jun = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '0601', dt_fim=str(ano) + '0631')
#                 vlr_jul = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '0701', dt_fim=str(ano) + '0731')
#                 vlr_ago = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '0801', dt_fim=str(ano) + '0831')
#                 vlr_set = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '0901', dt_fim=str(ano) + '0931')
#                 vlr_out = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '1001', dt_fim=str(ano) + '1031')
#                 vlr_nov = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '1101', dt_fim=str(ano) + '1131')
#                 vlr_dez = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano) + '1201', dt_fim=str(ano) + '1231')
#
#             vlr_total = float(vlr_jan) + float(vlr_fev) + float(vlr_mar) + float(vlr_abr) + float(vlr_mai) + float(vlr_jun) + float(vlr_jul) + float(vlr_ago) + float(vlr_set) + float(vlr_out) + float(vlr_nov) + float(vlr_dez)
#             vlr_media = vlr_total / 12 if vlr_total > 0.0 else 0.0
#
#             vlr_tot_jan += float(vlr_jan)
#             vlr_tot_fev += float(vlr_fev)
#             vlr_tot_mar += float(vlr_mar)
#             vlr_tot_abr += float(vlr_abr)
#             vlr_tot_mai += float(vlr_mai)
#             vlr_tot_jun += float(vlr_jun)
#             vlr_tot_jul += float(vlr_jul)
#             vlr_tot_ago += float(vlr_ago)
#             vlr_tot_set += float(vlr_set)
#             vlr_tot_out += float(vlr_out)
#             vlr_tot_nov += float(vlr_nov)
#             vlr_tot_dez += float(vlr_dez)
#             vlr_tot_total += float(vlr_total)
#
#             lista.append([str(codigo), decimal_to_str(valor=float(vlr_jan)), decimal_to_str(valor=float(vlr_fev)), decimal_to_str(valor=float(vlr_mar)), decimal_to_str(valor=float(vlr_abr)), decimal_to_str(valor=float(vlr_mai)), decimal_to_str(valor=float(vlr_jun)), decimal_to_str(valor=float(vlr_jul)), decimal_to_str(valor=float(vlr_ago)), decimal_to_str(valor=float(vlr_set)), decimal_to_str(valor=float(vlr_out)), decimal_to_str(valor=float(vlr_nov)), decimal_to_str(valor=float(vlr_dez)), decimal_to_str(valor=float(vlr_total)), decimal_to_str(valor=float(vlr_media))])
#
#         vlr_tot_media += vlr_tot_total / 12 if vlr_tot_total > 0.0 else 0.0
#
#         lista.append(['TOTAL', decimal_to_str(valor=float(vlr_tot_jan)), decimal_to_str(valor=float(vlr_tot_fev)), decimal_to_str(valor=float(vlr_tot_mar)), decimal_to_str(valor=float(vlr_tot_abr)), decimal_to_str(valor=float(vlr_tot_mai)), decimal_to_str(valor=float(vlr_tot_jun)), decimal_to_str(valor=float(vlr_tot_jul)), decimal_to_str(valor=float(vlr_tot_ago)), decimal_to_str(valor=float(vlr_tot_set)), decimal_to_str(valor=float(vlr_tot_out)), decimal_to_str(valor=float(vlr_tot_nov)), decimal_to_str(valor=float(vlr_tot_dez)), decimal_to_str(valor=float(vlr_tot_total)), decimal_to_str(valor=float(vlr_tot_media))])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/gridCalProv', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_cal_prov():
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
#             ano = data.get('Ano')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not ano:
#             return make_response(get_json_retorno_grid(msg='Ano não informado.'), 200)
#
#         id_usuario = current_user.id
#         lista = []
#         vlr_jan, vlr_fev, vlr_mar, vlr_abr, vlr_mai, vlr_jun, vlr_jul, vlr_ago, vlr_set, vlr_out, vlr_nov, vlr_dez = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#         vlr_tot_jan, vlr_tot_fev, vlr_tot_mar, vlr_tot_abr, vlr_tot_mai, vlr_tot_jun, vlr_tot_jul, vlr_tot_ago, vlr_tot_set, vlr_tot_out, vlr_tot_nov, vlr_tot_dez, vlr_tot_total, vlr_tot_media = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#         ult_codigo = ""
#
#         ativos = ACAOEmpresaAtivo.buscar_todos_codigos_proventos_com_fiis_bdrs_calendario(id_usuario=id_usuario, dt_ini=str(ano) + '0101', dt_fim=str(ano) + '1231')
#         for ativo in ativos:
#
#             #id_ativo = int(ativo['ID'])
#             codigo = str(ativo['CODIGO'])
#             # tipo_invest = str(ativo['TIPO'])
#             ano_mes_pagto = str(ativo['DATAPAGTO'])
#             tot_pagto = float(ativo['TOTVLR']) if ativo['TOTVLR'] and ativo['TOTVLR'] > 0.0 else 0.0
#
#             if ult_codigo != codigo:
#                 if ult_codigo != "":
#                     vlr_total = float(vlr_jan) + float(vlr_fev) + float(vlr_mar) + float(vlr_abr) + float(vlr_mai) + float(vlr_jun) + float(vlr_jul) + float(vlr_ago) + float(vlr_set) + float(vlr_out) + float(vlr_nov) + float(vlr_dez)
#                     vlr_media = vlr_total / 12 if vlr_total > 0.0 else 0.0
#                     lista.append([str(ult_codigo), decimal_to_str(valor=float(vlr_jan)), decimal_to_str(valor=float(vlr_fev)), decimal_to_str(valor=float(vlr_mar)), decimal_to_str(valor=float(vlr_abr)), decimal_to_str(valor=float(vlr_mai)), decimal_to_str(valor=float(vlr_jun)), decimal_to_str(valor=float(vlr_jul)), decimal_to_str(valor=float(vlr_ago)), decimal_to_str(valor=float(vlr_set)), decimal_to_str(valor=float(vlr_out)), decimal_to_str(valor=float(vlr_nov)), decimal_to_str(valor=float(vlr_dez)), decimal_to_str(valor=float(vlr_total)), decimal_to_str(valor=float(vlr_media))])
#                     vlr_tot_jan += float(vlr_jan)
#                     vlr_tot_fev += float(vlr_fev)
#                     vlr_tot_mar += float(vlr_mar)
#                     vlr_tot_abr += float(vlr_abr)
#                     vlr_tot_mai += float(vlr_mai)
#                     vlr_tot_jun += float(vlr_jun)
#                     vlr_tot_jul += float(vlr_jul)
#                     vlr_tot_ago += float(vlr_ago)
#                     vlr_tot_set += float(vlr_set)
#                     vlr_tot_out += float(vlr_out)
#                     vlr_tot_nov += float(vlr_nov)
#                     vlr_tot_dez += float(vlr_dez)
#                     vlr_tot_total += float(vlr_total)
#                 vlr_jan, vlr_fev, vlr_mar, vlr_abr, vlr_mai, vlr_jun, vlr_jul, vlr_ago, vlr_set, vlr_out, vlr_nov, vlr_dez = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#                 ult_codigo = codigo
#
#             if ano_mes_pagto == str(ano) + '01': vlr_jan = tot_pagto
#             elif ano_mes_pagto == str(ano) + '02': vlr_fev = tot_pagto
#             elif ano_mes_pagto == str(ano) + '03': vlr_mar = tot_pagto
#             elif ano_mes_pagto == str(ano) + '04': vlr_abr = tot_pagto
#             elif ano_mes_pagto == str(ano) + '05': vlr_mai = tot_pagto
#             elif ano_mes_pagto == str(ano) + '06': vlr_jun = tot_pagto
#             elif ano_mes_pagto == str(ano) + '07': vlr_jul = tot_pagto
#             elif ano_mes_pagto == str(ano) + '08': vlr_ago = tot_pagto
#             elif ano_mes_pagto == str(ano) + '09': vlr_set = tot_pagto
#             elif ano_mes_pagto == str(ano) + '10': vlr_out = tot_pagto
#             elif ano_mes_pagto == str(ano) + '11': vlr_nov = tot_pagto
#             elif ano_mes_pagto == str(ano) + '12': vlr_dez = tot_pagto
#
#         vlr_total = float(vlr_jan) + float(vlr_fev) + float(vlr_mar) + float(vlr_abr) + float(vlr_mai) + float(vlr_jun) + float(vlr_jul) + float(vlr_ago) + float(vlr_set) + float(vlr_out) + float(vlr_nov) + float(vlr_dez)
#         vlr_media = vlr_total / 12 if vlr_total > 0.0 else 0.0
#         lista.append([str(ult_codigo), decimal_to_str(valor=float(vlr_jan)), decimal_to_str(valor=float(vlr_fev)), decimal_to_str(valor=float(vlr_mar)), decimal_to_str(valor=float(vlr_abr)), decimal_to_str(valor=float(vlr_mai)), decimal_to_str(valor=float(vlr_jun)), decimal_to_str(valor=float(vlr_jul)), decimal_to_str(valor=float(vlr_ago)), decimal_to_str(valor=float(vlr_set)), decimal_to_str(valor=float(vlr_out)), decimal_to_str(valor=float(vlr_nov)), decimal_to_str(valor=float(vlr_dez)), decimal_to_str(valor=float(vlr_total)), decimal_to_str(valor=float(vlr_media))])
#
#         vlr_tot_jan += float(vlr_jan)
#         vlr_tot_fev += float(vlr_fev)
#         vlr_tot_mar += float(vlr_mar)
#         vlr_tot_abr += float(vlr_abr)
#         vlr_tot_mai += float(vlr_mai)
#         vlr_tot_jun += float(vlr_jun)
#         vlr_tot_jul += float(vlr_jul)
#         vlr_tot_ago += float(vlr_ago)
#         vlr_tot_set += float(vlr_set)
#         vlr_tot_out += float(vlr_out)
#         vlr_tot_nov += float(vlr_nov)
#         vlr_tot_dez += float(vlr_dez)
#         vlr_tot_total += float(vlr_total)
#
#         vlr_tot_media += vlr_tot_total / 12 if vlr_tot_total > 0.0 else 0.0
#
#         lista.append(['TOTAL', decimal_to_str(valor=float(vlr_tot_jan)), decimal_to_str(valor=float(vlr_tot_fev)), decimal_to_str(valor=float(vlr_tot_mar)), decimal_to_str(valor=float(vlr_tot_abr)), decimal_to_str(valor=float(vlr_tot_mai)), decimal_to_str(valor=float(vlr_tot_jun)), decimal_to_str(valor=float(vlr_tot_jul)), decimal_to_str(valor=float(vlr_tot_ago)), decimal_to_str(valor=float(vlr_tot_set)), decimal_to_str(valor=float(vlr_tot_out)), decimal_to_str(valor=float(vlr_tot_nov)), decimal_to_str(valor=float(vlr_tot_dez)), decimal_to_str(valor=float(vlr_tot_total)), decimal_to_str(valor=float(vlr_tot_media))])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/gridCalProvAtivo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_cal_prov_ativo():
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
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         tipo_invest = ''
#         if codigo and codigo == 'ACAO': tipo_invest = 'ACAO'
#         if codigo and codigo == 'FII': tipo_invest = 'FII'
#         if codigo and codigo == 'BDR': tipo_invest = 'BDR'
#         if tipo_invest: codigo = ''
#
#         id_ativo = None
#
#         if not tipo_invest and codigo:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'ACAO'
#             if not id_ativo:
#                 row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     id_ativo = int(row.id)
#                     tipo_invest = 'FII'
#             if not id_ativo:
#                 row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     id_ativo = int(row.id)
#                     tipo_invest = 'BDR'
#             if not id_ativo:
#                 return make_response(get_json_retorno_grid(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         anos = []
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             anos.append(UsuarioACAOEmpresaProvento.get_menor_ano(id_usuario=id_usuario, id_ativo=id_ativo)[0])
#             anos.append(UsuarioACAOEmpresaProvento.get_maior_ano(id_usuario=id_usuario, id_ativo=id_ativo)[0])
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             anos.append(UsuarioFiiFundoImobProvento.get_menor_ano(id_usuario=id_usuario, id_fundo=id_ativo)[0])
#             anos.append(UsuarioFiiFundoImobProvento.get_maior_ano(id_usuario=id_usuario, id_fundo=id_ativo)[0])
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             anos.append(UsuarioBDREmpresaProvento.get_menor_ano(id_usuario=id_usuario, id_bdr=id_ativo)[0])
#             anos.append(UsuarioBDREmpresaProvento.get_maior_ano(id_usuario=id_usuario, id_bdr=id_ativo)[0])
#
#         try:
#             menor = min(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#             maior = max(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#         except:
#             menor = None
#             maior = None
#
#         if not menor or not maior:
#             return make_response(get_json_retorno_grid(rslt='OK'), 200)
#
#         lista = []
#         vlr_tot_jan, vlr_tot_fev, vlr_tot_mar, vlr_tot_abr, vlr_tot_mai, vlr_tot_jun, vlr_tot_jul, vlr_tot_ago, vlr_tot_set, vlr_tot_out, vlr_tot_nov, vlr_tot_dez, vlr_tot_total, vlr_tot_media = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#         vlr_med_jan, vlr_med_fev, vlr_med_mar, vlr_med_abr, vlr_med_mai, vlr_med_jun, vlr_med_jul, vlr_med_ago, vlr_med_set, vlr_med_out, vlr_med_nov, vlr_med_dez, vlr_med_total, vlr_med_media = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#
#         for ano in range(menor, maior+1):
#
#             vlr_jan, vlr_fev, vlr_mar, vlr_abr, vlr_mai, vlr_jun, vlr_jul, vlr_ago, vlr_set, vlr_out, vlr_nov, vlr_dez, vlr_total, vlr_media = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#
#             ativos = ACAOEmpresaAtivo.buscar_todos_codigos_proventos_com_fiis_bdrs(id_usuario=id_usuario, codigo=codigo, dt_ini=str(ano) + '0101', dt_fim=str(ano) + '1231')
#
#             for ativo in ativos:
#
#                 id_ativo_local = int(ativo['ID'])
#                 codigo_local = str(ativo['CODIGO'])
#                 tipo_invest_local = str(ativo['TIPO'])
#
#                 if tipo_invest_local == 'ACAO' and (not tipo_invest or str(tipo_invest) == 'ACAO'):
#                     vlr_jan += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '0101', dt_fim=str(ano) + '0131')
#                     vlr_fev += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '0201', dt_fim=str(ano) + '0231')
#                     vlr_mar += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '0301', dt_fim=str(ano) + '0331')
#                     vlr_abr += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '0401', dt_fim=str(ano) + '0431')
#                     vlr_mai += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '0501', dt_fim=str(ano) + '0531')
#                     vlr_jun += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '0601', dt_fim=str(ano) + '0631')
#                     vlr_jul += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '0701', dt_fim=str(ano) + '0731')
#                     vlr_ago += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '0801', dt_fim=str(ano) + '0831')
#                     vlr_set += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '0901', dt_fim=str(ano) + '0931')
#                     vlr_out += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '1001', dt_fim=str(ano) + '1031')
#                     vlr_nov += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '1101', dt_fim=str(ano) + '1131')
#                     vlr_dez += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo_local, dt_ini=str(ano) + '1201', dt_fim=str(ano) + '1231')
#
#                 if tipo_invest_local == 'FII' and (not tipo_invest or str(tipo_invest) == 'FII'):
#                     vlr_jan += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'0101', dt_fim=str(ano)+'0131')
#                     vlr_fev += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'0201', dt_fim=str(ano)+'0231')
#                     vlr_mar += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'0301', dt_fim=str(ano)+'0331')
#                     vlr_abr += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'0401', dt_fim=str(ano)+'0431')
#                     vlr_mai += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'0501', dt_fim=str(ano)+'0531')
#                     vlr_jun += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'0601', dt_fim=str(ano)+'0631')
#                     vlr_jul += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'0701', dt_fim=str(ano)+'0731')
#                     vlr_ago += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'0801', dt_fim=str(ano)+'0831')
#                     vlr_set += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'0901', dt_fim=str(ano)+'0931')
#                     vlr_out += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'1001', dt_fim=str(ano)+'1031')
#                     vlr_nov += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'1101', dt_fim=str(ano)+'1131')
#                     vlr_dez += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo_local, dt_ini=str(ano)+'1201', dt_fim=str(ano)+'1231')
#
#                 if tipo_invest_local == 'BDR' and (not tipo_invest or str(tipo_invest) == 'BDR'):
#                     vlr_jan += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '0101', dt_fim=str(ano) + '0131')
#                     vlr_fev += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '0201', dt_fim=str(ano) + '0231')
#                     vlr_mar += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '0301', dt_fim=str(ano) + '0331')
#                     vlr_abr += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '0401', dt_fim=str(ano) + '0431')
#                     vlr_mai += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '0501', dt_fim=str(ano) + '0531')
#                     vlr_jun += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '0601', dt_fim=str(ano) + '0631')
#                     vlr_jul += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '0701', dt_fim=str(ano) + '0731')
#                     vlr_ago += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '0801', dt_fim=str(ano) + '0831')
#                     vlr_set += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '0901', dt_fim=str(ano) + '0931')
#                     vlr_out += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '1001', dt_fim=str(ano) + '1031')
#                     vlr_nov += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '1101', dt_fim=str(ano) + '1131')
#                     vlr_dez += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo_local, dt_ini=str(ano) + '1201', dt_fim=str(ano) + '1231')
#
#             vlr_total = float(vlr_jan) + float(vlr_fev) + float(vlr_mar) + float(vlr_abr) + float(vlr_mai) + float(vlr_jun) + float(vlr_jul) + float(vlr_ago) + float(vlr_set) + float(vlr_out) + float(vlr_nov) + float(vlr_dez)
#             vlr_media = vlr_total / 12 if vlr_total > 0.0 else 0.0
#
#             vlr_tot_jan += float(vlr_jan)
#             vlr_tot_fev += float(vlr_fev)
#             vlr_tot_mar += float(vlr_mar)
#             vlr_tot_abr += float(vlr_abr)
#             vlr_tot_mai += float(vlr_mai)
#             vlr_tot_jun += float(vlr_jun)
#             vlr_tot_jul += float(vlr_jul)
#             vlr_tot_ago += float(vlr_ago)
#             vlr_tot_set += float(vlr_set)
#             vlr_tot_out += float(vlr_out)
#             vlr_tot_nov += float(vlr_nov)
#             vlr_tot_dez += float(vlr_dez)
#             vlr_tot_total += float(vlr_total)
#
#             lista.append([str(ano), decimal_to_str(valor=float(vlr_jan)), decimal_to_str(valor=float(vlr_fev)), decimal_to_str(valor=float(vlr_mar)), decimal_to_str(valor=float(vlr_abr)), decimal_to_str(valor=float(vlr_mai)), decimal_to_str(valor=float(vlr_jun)), decimal_to_str(valor=float(vlr_jul)), decimal_to_str(valor=float(vlr_ago)), decimal_to_str(valor=float(vlr_set)), decimal_to_str(valor=float(vlr_out)), decimal_to_str(valor=float(vlr_nov)), decimal_to_str(valor=float(vlr_dez)), decimal_to_str(valor=float(vlr_total)), decimal_to_str(valor=float(vlr_media))])
#
#         vlr_tot_media += vlr_tot_total / 12 if vlr_tot_total > 0.0 else 0.0
#
#         lista.append(['TOTAL', decimal_to_str(valor=float(vlr_tot_jan)), decimal_to_str(valor=float(vlr_tot_fev)), decimal_to_str(valor=float(vlr_tot_mar)), decimal_to_str(valor=float(vlr_tot_abr)), decimal_to_str(valor=float(vlr_tot_mai)), decimal_to_str(valor=float(vlr_tot_jun)), decimal_to_str(valor=float(vlr_tot_jul)), decimal_to_str(valor=float(vlr_tot_ago)), decimal_to_str(valor=float(vlr_tot_set)), decimal_to_str(valor=float(vlr_tot_out)), decimal_to_str(valor=float(vlr_tot_nov)), decimal_to_str(valor=float(vlr_tot_dez)), decimal_to_str(valor=float(vlr_tot_total)), decimal_to_str(valor=float(vlr_tot_media))])
#
#         maior = int(maior) + 1
#         qtd_ano = int(maior) - int(menor) if int(maior) - int(menor) > 1 else 1
#
#         if qtd_ano > 0:
#             vlr_med_jan = vlr_tot_jan / qtd_ano if vlr_tot_jan else 0.0
#             vlr_med_fev = vlr_tot_fev / qtd_ano if vlr_tot_fev else 0.0
#             vlr_med_mar = vlr_tot_mar / qtd_ano if vlr_tot_mar else 0.0
#             vlr_med_abr = vlr_tot_abr / qtd_ano if vlr_tot_abr else 0.0
#             vlr_med_mai = vlr_tot_mai / qtd_ano if vlr_tot_mai else 0.0
#             vlr_med_jun = vlr_tot_jun / qtd_ano if vlr_tot_jun else 0.0
#             vlr_med_jul = vlr_tot_jul / qtd_ano if vlr_tot_jul else 0.0
#             vlr_med_ago = vlr_tot_ago / qtd_ano if vlr_tot_ago else 0.0
#             vlr_med_set = vlr_tot_set / qtd_ano if vlr_tot_set else 0.0
#             vlr_med_out = vlr_tot_out / qtd_ano if vlr_tot_out else 0.0
#             vlr_med_nov = vlr_tot_nov / qtd_ano if vlr_tot_nov else 0.0
#             vlr_med_dez = vlr_tot_dez / qtd_ano if vlr_tot_dez else 0.0
#             vlr_med_total = vlr_tot_total / qtd_ano if vlr_tot_total else 0.0
#             vlr_med_media = vlr_tot_media / qtd_ano if vlr_tot_media else 0.0
#
#         lista.append(['MÉDIA', decimal_to_str(valor=float(vlr_med_jan)), decimal_to_str(valor=float(vlr_med_fev)), decimal_to_str(valor=float(vlr_med_mar)), decimal_to_str(valor=float(vlr_med_abr)), decimal_to_str(valor=float(vlr_med_mai)), decimal_to_str(valor=float(vlr_med_jun)), decimal_to_str(valor=float(vlr_med_jul)), decimal_to_str(valor=float(vlr_med_ago)), decimal_to_str(valor=float(vlr_med_set)), decimal_to_str(valor=float(vlr_med_out)), decimal_to_str(valor=float(vlr_med_nov)), decimal_to_str(valor=float(vlr_med_dez)), decimal_to_str(valor=float(vlr_med_total)), decimal_to_str(valor=float(vlr_med_media))])
#
#         array_med = [float(vlr_med_jan), float(vlr_med_fev), float(vlr_med_mar), float(vlr_med_abr), float(vlr_med_mai), float(vlr_med_jun), float(vlr_med_jul), float(vlr_med_ago), float(vlr_med_set), float(vlr_med_out), float(vlr_med_nov), float(vlr_med_dez)]
#         array_med.sort(reverse=True)
#         # sorted(array_med, reverse=True)
#
#         lista.append(['RANKING', str(array_med.index(float(vlr_med_jan))+1) + 'º', str(array_med.index(float(vlr_med_fev))+1) + 'º', str(array_med.index(float(vlr_med_mar))+1) + 'º', str(array_med.index(float(vlr_med_abr))+1) + 'º', str(array_med.index(float(vlr_med_mai))+1) + 'º', str(array_med.index(float(vlr_med_jun))+1) + 'º', str(array_med.index(float(vlr_med_jul))+1) + 'º', str(array_med.index(float(vlr_med_ago))+1) + 'º', str(array_med.index(float(vlr_med_set))+1) + 'º', str(array_med.index(float(vlr_med_out))+1) + 'º', str(array_med.index(float(vlr_med_nov))+1) + 'º', str(array_med.index(float(vlr_med_dez))+1) + 'º', '', ''])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/graficoProvAno', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grafico_prov_ano():
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
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         tipo_invest = ''
#         if codigo and codigo == 'ACAO': tipo_invest = 'ACAO'
#         if codigo and codigo == 'FII': tipo_invest = 'FII'
#         if codigo and codigo == 'BDR': tipo_invest = 'BDR'
#         if tipo_invest: codigo = ''
#
#         id_ativo = None
#
#         if not tipo_invest and codigo:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'ACAO'
#             if not id_ativo:
#                 row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     id_ativo = int(row.id)
#                     tipo_invest = 'FII'
#             if not id_ativo:
#                 row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     id_ativo = int(row.id)
#                     tipo_invest = 'BDR'
#             if not id_ativo:
#                 return make_response(get_json_retorno_grid(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         anos = []
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             anos.append(UsuarioACAOEmpresaProvento.get_menor_ano(id_usuario=id_usuario, id_ativo=id_ativo)[0])
#             anos.append(UsuarioACAOEmpresaProvento.get_maior_ano(id_usuario=id_usuario, id_ativo=id_ativo)[0])
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             anos.append(UsuarioFiiFundoImobProvento.get_menor_ano(id_usuario=id_usuario, id_fundo=id_ativo)[0])
#             anos.append(UsuarioFiiFundoImobProvento.get_maior_ano(id_usuario=id_usuario, id_fundo=id_ativo)[0])
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             anos.append(UsuarioBDREmpresaProvento.get_menor_ano(id_usuario=id_usuario, id_bdr=id_ativo)[0])
#             anos.append(UsuarioBDREmpresaProvento.get_maior_ano(id_usuario=id_usuario, id_bdr=id_ativo)[0])
#
#         try:
#             menor = min(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#             maior = max(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#         except:
#             menor = None
#             maior = None
#
#         if not menor or not maior:
#             return make_response(get_json_retorno_grid(rslt='OK'), 200)
#
#         lista = []
#
#         for ano in range(menor, maior+1):
#             tot_prov = 0.0
#             if not tipo_invest or str(tipo_invest) == 'ACAO': tot_prov += UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_ativo=id_ativo, dt_ini=str(ano) + '0101', dt_fim=str(ano) + '1231')
#             if not tipo_invest or str(tipo_invest) == 'FII': tot_prov += UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_fundo=id_ativo, dt_ini=str(ano)+'0101', dt_fim=str(ano)+'1231')
#             if not tipo_invest or str(tipo_invest) == 'BDR': tot_prov += UsuarioBDREmpresaProvento.buscar_vlr_total_periodo(id_usuario=id_usuario, id_bdr=id_ativo, dt_ini=str(ano)+'0101', dt_fim=str(ano)+'1231')
#             if tot_prov: lista.append([str(ano), decimal_to_str(valor=float(tot_prov))])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/gridYieldOnCost', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_yield_on_cost():
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
#             codigo = data.get('CodAtivo')
#             ano_yoc = data.get('Ano')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         tipo_invest = ''
#         if codigo and codigo == 'ACAO': tipo_invest = 'ACAO'
#         if codigo and codigo == 'FII': tipo_invest = 'FII'
#         if codigo and codigo == 'BDR': tipo_invest = 'BDR'
#         if tipo_invest: codigo = ''
#
#         id_usuario = current_user.id
#
#         ano_atual = pegar_data_atual(fmt='%Y')
#         data_atual = pegar_data_atual()
#
#         lista = []
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             ativos = ACAOEmpresaAtivo.buscar_todos_codigos_proventos(id_usuario=id_usuario, codigo=codigo)
#             for ativo in ativos:
#                 menor = ano_yoc
#                 maior = ano_yoc
#                 if not ano_yoc:
#                     menor = UsuarioACAOEmpresaProvento.get_menor_ano_ex(id_usuario=id_usuario, id_ativo=int(ativo['ID']))[0]
#                     maior = UsuarioACAOEmpresaProvento.get_maior_ano_ex(id_usuario=id_usuario, id_ativo=int(ativo['ID']))[0]
#                     if menor: menor = str(menor)[:4]
#                     if maior: maior = str(maior)[:4]
#                     if maior and int(maior) < int(ano_atual):
#                         qtde_compra = UsuarioACAOEmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_ativo=int(ativo['ID']))
#                         qtde_bonus = UsuarioACAOEmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_ativo=int(ativo['ID']))
#                         qtde_venda = UsuarioACAOEmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_ativo=int(ativo['ID']))
#                         if qtde_compra + qtde_bonus > qtde_venda: maior = ano_atual
#                 if not menor or not maior:
#                     continue
#                 for ano in range(int(menor), int(maior)+1):
#                     yield_on_cost = 0.0
#                     dt_ini = str(ano)+'0101'
#                     dt_fim = str(ano)+'1231'
#                     if int(ano) == int(ano_atual): dt_fim = str(data_atual)
#                     dt_fim = UsuarioACAOEmpresaProvento.buscar_maior_data_ex(id_usuario=id_usuario, id_ativo=int(ativo['ID']), dt_fim=dt_fim)
#                     vlr_preco_medio = UsuarioACAOEmpresaOperacao.buscar_preco_medio_antes(id_usuario=id_usuario, id_ativo=int(ativo['ID']), dt_fim=dt_fim)
#                     vlr_prov = UsuarioACAOEmpresaProvento.buscar_vlr_preco_ex(id_usuario=id_usuario, id_ativo=int(ativo['ID']), dt_ini=dt_ini, dt_fim=dt_fim)
#                     tot_prov = UsuarioACAOEmpresaProvento.buscar_vlr_total_periodo_ex(id_usuario=id_usuario, id_ativo=int(ativo['ID']), dt_ini=dt_ini, dt_fim=dt_fim)
#                     if vlr_preco_medio > 0.0 and vlr_prov > 0.0: yield_on_cost = (vlr_prov / vlr_preco_medio) * 100
#                     if vlr_prov > 0.0: lista.append([str(ativo['CODIGO']), str(ano), 'R$ ' + decimal_to_str(valor=float(vlr_preco_medio)), 'R$ ' + decimal_to_str(valor=float(vlr_prov)), 'R$ ' + decimal_to_str(valor=float(tot_prov)), decimal_to_str(valor=float(yield_on_cost)) + '%'])
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             fundos = FiiFundoImob.buscar_todos_codigos_proventos(id_usuario=id_usuario, codigo=codigo)
#             for fundo in fundos:
#                 menor = ano_yoc
#                 maior = ano_yoc
#                 if not ano_yoc:
#                     menor = UsuarioFiiFundoImobProvento.get_menor_ano_ex(id_usuario=id_usuario, id_fundo=int(fundo['ID']))[0]
#                     maior = UsuarioFiiFundoImobProvento.get_maior_ano_ex(id_usuario=id_usuario, id_fundo=int(fundo['ID']))[0]
#                     if menor: menor = str(menor)[:4]
#                     if maior: maior = str(maior)[:4]
#                     if maior and int(maior) < int(ano_atual):
#                         qtde_compra = UsuarioFiiFundoImobLancamento.buscar_total_compra(id_usuario=id_usuario, id_fundo=int(fundo['ID']))
#                         qtde_bonus = UsuarioFiiFundoImobLancamento.buscar_total_bonus(id_usuario=id_usuario, id_fundo=int(fundo['ID']))
#                         qtde_venda = UsuarioFiiFundoImobLancamento.buscar_total_venda(id_usuario=id_usuario, id_fundo=int(fundo['ID']))
#                         if qtde_compra + qtde_bonus > qtde_venda: maior = ano_atual
#                 if not menor or not maior:
#                     continue
#                 for ano in range(int(menor), int(maior)+1):
#                     yield_on_cost = 0.0
#                     dt_ini = str(ano)+'0101'
#                     dt_fim = str(ano)+'1231'
#                     if int(ano) == int(ano_atual): dt_fim = str(data_atual)
#                     dt_fim = UsuarioFiiFundoImobProvento.buscar_maior_data_ex(id_usuario=id_usuario, id_fundo=int(fundo['ID']), dt_fim=dt_fim)
#                     vlr_preco_medio = UsuarioFiiFundoImobLancamento.buscar_preco_medio_antes(id_usuario=id_usuario, id_fundo=int(fundo['ID']), dt_fim=dt_fim)
#                     vlr_prov = UsuarioFiiFundoImobProvento.buscar_vlr_preco_ex(id_usuario=id_usuario, id_fundo=int(fundo['ID']), dt_ini=dt_ini, dt_fim=dt_fim)
#                     tot_prov = UsuarioFiiFundoImobProvento.buscar_vlr_total_periodo_ex(id_usuario=id_usuario, id_fundo=int(fundo['ID']), dt_ini=dt_ini, dt_fim=dt_fim)
#                     if vlr_preco_medio > 0.0 and vlr_prov > 0.0: yield_on_cost = (vlr_prov / vlr_preco_medio) * 100
#                     if vlr_prov > 0.0: lista.append([str(fundo['CODIGO']), str(ano), 'R$ ' + decimal_to_str(valor=float(vlr_preco_medio)), 'R$ ' + decimal_to_str(valor=float(vlr_prov)), 'R$ ' + decimal_to_str(valor=float(tot_prov)), decimal_to_str(valor=float(yield_on_cost)) + '%'])
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             ativos = BDREmpresa.buscar_todos_codigos_proventos(id_usuario=id_usuario, codigo=codigo)
#             for ativo in ativos:
#                 menor = ano_yoc
#                 maior = ano_yoc
#                 if not ano_yoc:
#                     menor = UsuarioBDREmpresaProvento.get_menor_ano_ex(id_usuario=id_usuario, id_bdr=int(ativo['ID']))[0]
#                     maior = UsuarioBDREmpresaProvento.get_maior_ano_ex(id_usuario=id_usuario, id_bdr=int(ativo['ID']))[0]
#                     if menor: menor = str(menor)[:4]
#                     if maior: maior = str(maior)[:4]
#                     if maior and int(maior) < int(ano_atual):
#                         qtde_compra = UsuarioBDREmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_bdr=int(ativo['ID']))
#                         qtde_bonus = UsuarioBDREmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_bdr=int(ativo['ID']))
#                         qtde_venda = UsuarioBDREmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_bdr=int(ativo['ID']))
#                         if qtde_compra + qtde_bonus > qtde_venda: maior = ano_atual
#                 if not menor or not maior:
#                     continue
#                 for ano in range(int(menor), int(maior)+1):
#                     yield_on_cost = 0.0
#                     dt_ini = str(ano)+'0101'
#                     dt_fim = str(ano)+'1231'
#                     if int(ano) == int(ano_atual): dt_fim = str(data_atual)
#                     dt_fim = UsuarioBDREmpresaProvento.buscar_maior_data_ex(id_usuario=id_usuario, id_bdr=int(ativo['ID']), dt_fim=dt_fim)
#                     vlr_preco_medio = UsuarioBDREmpresaOperacao.buscar_preco_medio_antes(id_usuario=id_usuario, id_bdr=int(ativo['ID']), dt_fim=dt_fim)
#                     vlr_prov = UsuarioBDREmpresaProvento.buscar_vlr_preco_ex(id_usuario=id_usuario, id_bdr=int(ativo['ID']), dt_ini=dt_ini, dt_fim=dt_fim)
#                     tot_prov = UsuarioBDREmpresaProvento.buscar_vlr_total_periodo_ex(id_usuario=id_usuario, id_bdr=int(ativo['ID']), dt_ini=dt_ini, dt_fim=dt_fim)
#                     if vlr_preco_medio > 0.0 and vlr_prov > 0.0: yield_on_cost = (vlr_prov / vlr_preco_medio) * 100
#                     if vlr_prov > 0.0: lista.append([str(ativo['CODIGO']), str(ano), 'R$ ' + decimal_to_str(valor=float(vlr_preco_medio)), 'R$ ' + decimal_to_str(valor=float(vlr_prov)), 'R$ ' + decimal_to_str(valor=float(tot_prov)), decimal_to_str(valor=float(yield_on_cost)) + '%'])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/graficoEvolucaoPratrimonio', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grafico_evolucao_pratrimonio():
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
#             codigo = data.get('CodAtivo')
#             tp_grafico = data.get('TpGrafico')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         tipo_invest = ""
#         if codigo and str(codigo) == "ACAO": tipo_invest = "ACAO"
#         if codigo and str(codigo) == "FII": tipo_invest = "FII"
#         if codigo and str(codigo) == "ETF": tipo_invest = "ETF"
#         if codigo and str(codigo) == "BDR": tipo_invest = "BDR"
#         if codigo and str(codigo) == "CRIPTO": tipo_invest = "CRIPTO"
#         if tipo_invest: codigo = ""
#         if codigo: codigo = str(codigo)
#
#         id_usuario = current_user.id
#
#         id_ativo = None
#         if not tipo_invest and codigo:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'ACAO'
#             if not id_ativo:
#                 row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     id_ativo = int(row.id)
#                     tipo_invest = 'FII'
#             if not id_ativo:
#                 row = ETFIndice.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     id_ativo = int(row.id)
#                     tipo_invest = 'ETF'
#             if not id_ativo:
#                 row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     id_ativo = int(row.id)
#                     tipo_invest = 'BDR'
#             if not id_ativo:
#                 row = CriptoEmpresa.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     id_ativo = int(row.id)
#                     tipo_invest = 'CRIPTO'
#             if not id_ativo:
#                 return make_response(get_json_retorno_grid(msg='Código não localizado.'), 200)
#
#         anos = []
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             anos.append(UsuarioACAOEmpresaLancamento.get_menor_ano(id_usuario=id_usuario, id_ativo=id_ativo)[0])
#             anos.append(UsuarioACAOEmpresaLancamento.get_maior_ano(id_usuario=id_usuario, id_ativo=id_ativo)[0])
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             anos.append(UsuarioFiiFundoImobLancamento.get_menor_ano(id_usuario=id_usuario, id_fundo=id_ativo)[0])
#             anos.append(UsuarioFiiFundoImobLancamento.get_maior_ano(id_usuario=id_usuario, id_fundo=id_ativo)[0])
#
#         if not tipo_invest or str(tipo_invest) == 'ETF':
#             anos.append(UsuarioETFIndiceLancamento.get_menor_ano(id_usuario=id_usuario, id_indice=id_ativo)[0])
#             anos.append(UsuarioETFIndiceLancamento.get_maior_ano(id_usuario=id_usuario, id_indice=id_ativo)[0])
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             anos.append(UsuarioBDREmpresaLancamento.get_menor_ano(id_usuario=id_usuario, id_bdr=id_ativo)[0])
#             anos.append(UsuarioBDREmpresaLancamento.get_maior_ano(id_usuario=id_usuario, id_bdr=id_ativo)[0])
#
#         if not tipo_invest or str(tipo_invest) == 'CRIPTO':
#             anos.append(UsuarioCriptoLancamento.get_menor_ano(id_usuario=id_usuario, id_cripto=id_ativo)[0])
#             anos.append(UsuarioCriptoLancamento.get_maior_ano(id_usuario=id_usuario, id_cripto=id_ativo)[0])
#
#         try:
#             menor = min(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#             maior = max(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#         except:
#             menor = None
#             maior = None
#
#         if not menor or not maior:
#             return make_response(get_json_retorno_grid(rslt='OK'), 200)
#
#         lista = []
#
#         if not tp_grafico or str(tp_grafico) == "A":
#             for ano in range(menor, maior+1):
#                 tot_invest = 0.0
#
#                 if not tipo_invest or str(tipo_invest) == "ACAO":
#                     rows = ACAOEmpresaAtivo.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                     for row in rows:
#                         opers = UsuarioACAOEmpresaOperacao.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano) + "1231", categoria="C")  # C - Comun
#                         qtde_atual = 0.0
#                         vlr_preco_medio = 0.0
#                         for oper in opers:
#                             vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                             if str(oper['TIPO']) == "C" or str(oper['TIPO']) == "B": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                         tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                 if not tipo_invest or str(tipo_invest) == "FII":
#                     rows = FiiFundoImob.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                     for row in rows:
#                         opers = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano)+"1231")
#                         qtde_atual = 0.0
#                         vlr_preco_medio = 0.0
#                         for oper in opers:
#                             vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                             if str(oper['TIPO']) == "C" or str(oper['TIPO']) == "B": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "A" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                         tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                 if not tipo_invest or str(tipo_invest) == "ETF":
#                     rows = ETFIndice.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                     for row in rows:
#                         opers = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano)+"1231", categoria="C")  # C - Comun
#                         qtde_atual = 0.0
#                         vlr_preco_medio = 0.0
#                         for oper in opers:
#                             vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                             if str(oper['TIPO']) == "C" or str(oper['TIPO']) == "B": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                         tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                 if not tipo_invest or str(tipo_invest) == "BDR":
#                     rows = BDREmpresa.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                     for row in rows:
#                         opers = UsuarioBDREmpresaOperacao.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano) + "1231", categoria="C")  # C - Comun
#                         qtde_atual = 0.0
#                         vlr_preco_medio = 0.0
#                         for oper in opers:
#                             vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                             if str(oper['TIPO']) == "C" or str(oper['TIPO']) == "B": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                         tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#                         tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                 if not tipo_invest or str(tipo_invest) == "CRIPTO":
#                     rows = CriptoEmpresa.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                     for row in rows:
#                         opers = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano)+"1231")
#                         qtde_atual = 0.0
#                         vlr_preco_medio = 0.0
#                         for oper in opers:
#                             vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                             if str(oper['TIPO']) == "C": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                         tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                 if tot_invest > 0.0: lista.append([str(ano), decimal_to_str(valor=float(tot_invest))])
#
#         elif str(tp_grafico) == "M":
#             ano_atual = pegar_data_atual(fmt='%Y')
#             mes_atual = pegar_data_atual(fmt='%m')
#             for ano in range(menor, maior+1):
#                 for mes in range(1, 13):
#                     if int(ano) == int(ano_atual) and int(mes) > int(mes_atual): break
#                     tot_invest = 0.0
#                     ano_mes = str(ano) + str(mes).zfill(2)
#                     ano_mes_formatado = str(mes).zfill(2) + "/" + str(ano)
#
#                     if not tipo_invest or str(tipo_invest) == "ACAO":
#                         rows = ACAOEmpresaAtivo.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                         for row in rows:
#                             opers = UsuarioACAOEmpresaOperacao.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano_mes) + "31", categoria="C")  # C - Comun
#                             qtde_atual = 0.0
#                             vlr_preco_medio = 0.0
#                             for oper in opers:
#                                 vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                                 if str(oper['TIPO']) == "C" or str(oper['TIPO']) == "B": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                                 elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                     if not tipo_invest or str(tipo_invest) == "FII":
#                         rows = FiiFundoImob.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                         for row in rows:
#                             opers = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano_mes)+"31")
#                             qtde_atual = 0.0
#                             vlr_preco_medio = 0.0
#                             for oper in opers:
#                                 vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                                 if str(oper['TIPO']) == "C" or str(oper['TIPO']) == "B": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                                 elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "A" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                     if not tipo_invest or str(tipo_invest) == "ETF":
#                         rows = ETFIndice.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                         for row in rows:
#                             opers = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano_mes)+"31", categoria="C")  # C - Comun
#                             qtde_atual = 0.0
#                             vlr_preco_medio = 0.0
#                             for oper in opers:
#                                 vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                                 if str(oper['TIPO']) == "C" or str(oper['TIPO']) == "B": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                                 elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                     if not tipo_invest or str(tipo_invest) == "BDR":
#                         rows = BDREmpresa.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                         for row in rows:
#                             opers = UsuarioBDREmpresaOperacao.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano_mes) + "31", categoria="C")  # C - Comun
#                             qtde_atual = 0.0
#                             vlr_preco_medio = 0.0
#                             for oper in opers:
#                                 vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                                 if str(oper['TIPO']) == "C" or str(oper['TIPO']) == "B": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                                 elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                     if not tipo_invest or str(tipo_invest) == "CRIPTO":
#                         rows = CriptoEmpresa.buscar_todos_codigos_comprados(id_usuario=id_usuario, codigo=codigo)
#                         for row in rows:
#                             opers = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, codigo=str(row['CODIGO']), dt_fim=str(ano_mes)+"31")
#                             qtde_atual = 0.0
#                             vlr_preco_medio = 0.0
#                             for oper in opers:
#                                 vlr_preco_medio = float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] and float(oper['VLRPRECOMEDIO']) > 0.0 else 0.0
#                                 if str(oper['TIPO']) == "C": qtde_atual += float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                                 elif str(oper['TIPO']) == "V" or str(oper['TIPO']) == "P": qtde_atual -= float(oper['QUANT']) if oper['QUANT'] and float(oper['QUANT']) > 0.0 else 0.0
#                             tot_invest += qtde_atual * vlr_preco_medio if qtde_atual > 0.0 and vlr_preco_medio > 0.00 else 0.0
#
#                     if tot_invest > 0.0: lista.append([str(ano_mes_formatado), decimal_to_str(valor=float(tot_invest))])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/gridBalancePercent', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_balance_percent():
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
#             id_portfolio = data.get('IdPortfolio')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         tipo_invest = ""
#         if str(id_portfolio) == "ACAO": tipo_invest = "ACAO"
#         if str(id_portfolio) == "FII": tipo_invest = "FII"
#         if str(id_portfolio) == "ETF": tipo_invest = "ETF"
#         if str(id_portfolio) == "BDR": tipo_invest = "BDR"
#         if str(id_portfolio) == "CRIPTO": tipo_invest = "CRIPTO"
#         if str(id_portfolio) == "ACAO" or str(id_portfolio) == "FII" or str(id_portfolio) == "ETF" or str(id_portfolio) == "BDR" or str(id_portfolio) == "CRIPTO": id_portfolio = ""
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         if tipo_invest == '' or tipo_invest == 'ACAO':
#             rows = UsuarioCarteiraAcao.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0) + (float(row['QUANTBONUS']) if row['QUANTBONUS'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_precent = float(row['PERCENTBALAC']) if row['PERCENTBALAC'] else 0.0
#                 lista.append([str(row['CODIGOATIVO']), inteiro_to_str(valor=float(tot_quant)), decimal_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_precent)), str(row['IDATIVO']), 'ACAO'])
#
#         if tipo_invest == '' or tipo_invest == 'FII':
#             rows = UsuarioCarteiraFii.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0) + (float(row['QUANTBONUS']) if row['QUANTBONUS'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_precent = float(row['PERCENTBALAC']) if row['PERCENTBALAC'] else 0.0
#                 lista.append([str(row['CODIGOFUNDO']), inteiro_to_str(valor=float(tot_quant)), decimal_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_precent)), str(row['IDFUNDO']), 'FII'])
#
#         if tipo_invest == '' or tipo_invest == 'ETF':
#             rows = UsuarioCarteiraEtf.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0) + (float(row['QUANTBONUS']) if row['QUANTBONUS'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_precent = float(row['PERCENTBALAC']) if row['PERCENTBALAC'] else 0.0
#                 lista.append([str(row['CODIGOINDICE']), inteiro_to_str(valor=float(tot_quant)), decimal_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_precent)), str(row['IDINDICE']), 'ETF'])
#
#         if tipo_invest == '' or tipo_invest == 'BDR':
#             rows = UsuarioCarteiraBdr.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0) + (float(row['QUANTBONUS']) if row['QUANTBONUS'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_precent = float(row['PERCENTBALAC']) if row['PERCENTBALAC'] else 0.0
#                 lista.append([str(row['CODIGOBDR']), inteiro_to_str(valor=float(tot_quant)), decimal_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_precent)), str(row['IDBDR']), 'BDR'])
#
#         if tipo_invest == '' or tipo_invest == 'CRIPTO':
#             rows = UsuarioCarteiraCripto.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_precent = float(row['PERCENTBALAC']) if row['PERCENTBALAC'] else 0.0
#                 lista.append([str(row['CODIGOCRIPTO']), decimal_cripto_to_str(valor=float(tot_quant)), decimal_cripto_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_precent)), str(row['IDCRIPTO']), 'CRIPTO'])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/salvarBalancePercent', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_balance_percent():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         # if not data: data = request.get_json(silent=True)
#         # if not data: return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         try:
#             lista = data.to_dict()
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#
#         if not lista:
#             return make_response(get_json_retorno_metodo(msg='Lisya não informada.'), 200)
#
#         id_usuario = current_user.id
#
#         idx = -1
#         while True:
#
#             try:
#                 idx += 1
#                 tipo_invest = str(lista['lista['+str(idx)+'][TipoInvest]'])
#                 codigo = str(lista['lista['+str(idx)+'][CodAtivo]'])
#                 percent = lista['lista['+str(idx)+'][Percent]']
#             except:
#                 break
#
#             if tipo_invest == 'ACAO':
#                 ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=codigo)
#                 if not ativo: return make_response(get_json_retorno_metodo(msg='Ação não localizada.'), 200)
#                 row = UsuarioCarteiraAcao.buscar_por_ativo(id_usuario=id_usuario, id_ativo=ativo.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='Ação não localizado no Portfólio.'), 200)
#                 UsuarioCarteiraAcao.atualizar_percent_balanc(id=int(row['ID']), percent_balac=float(percent) if percent else 0)
#
#             elif tipo_invest == 'FII':
#                 fundo = FiiFundoImob.get_by_codigo(codigo=codigo)
#                 if not fundo: return make_response(get_json_retorno_metodo(msg='FII não localizado.'), 200)
#                 row = UsuarioCarteiraFii.buscar_por_ativo(id_usuario=id_usuario, id_fundo=fundo.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='FII não localizado no Portfólio.'), 200)
#                 UsuarioCarteiraFii.atualizar_percent_balanc(id=int(row['ID']), percent_balac=float(percent) if percent else 0)
#
#             elif tipo_invest == 'ETF':
#                 indice = ETFIndice.get_by_codigo(codigo=codigo)
#                 if not indice: return make_response(get_json_retorno_metodo(msg='ETF não localizado.'), 200)
#                 row = UsuarioCarteiraEtf.buscar_por_ativo(id_usuario=id_usuario, id_indice=indice.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='ETF não localizado no Portfólio.'), 200)
#                 UsuarioCarteiraEtf.atualizar_percent_balanc(id=int(row['ID']), percent_balac=float(percent) if percent else 0)
#
#             elif tipo_invest == 'BDR':
#                 ativo = BDREmpresa.get_by_codigo(codigo=codigo)
#                 if not ativo: return make_response(get_json_retorno_metodo(msg='BDR não localizada.'), 200)
#                 row = UsuarioCarteiraBdr.buscar_por_ativo(id_usuario=id_usuario, id_bdr=ativo.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='BDR não localizada no Portfólio.'), 200)
#                 UsuarioCarteiraBdr.atualizar_percent_balanc(id=int(row['ID']), percent_balac=float(percent) if percent else 0)
#
#             elif tipo_invest == 'CRIPTO':
#                 cripto = CriptoEmpresa.get_by_codigo(codigo=codigo)
#                 if not cripto: return make_response(get_json_retorno_metodo(msg='Cripto não localizada.'), 200)
#                 row = UsuarioCarteiraCripto.buscar_por_ativo(id_usuario=id_usuario, id_cripto=cripto.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='Cripto não localizada no Portfólio.'), 200)
#                 UsuarioCarteiraCripto.atualizar_percent_balanc(id=int(row['ID']), percent_balac=float(percent) if percent else 0)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/gridBalanceNotas', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_balance_notas():
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
#             id_portfolio = data.get('IdPortfolio')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         tipo_invest = ""
#         if str(id_portfolio) == "ACAO": tipo_invest = "ACAO"
#         if str(id_portfolio) == "FII": tipo_invest = "FII"
#         if str(id_portfolio) == "ETF": tipo_invest = "ETF"
#         if str(id_portfolio) == "BDR": tipo_invest = "BDR"
#         if str(id_portfolio) == "CRIPTO": tipo_invest = "CRIPTO"
#         if str(id_portfolio) == "ACAO" or str(id_portfolio) == "FII" or str(id_portfolio) == "ETF" or str(id_portfolio) == "BDR" or str(id_portfolio) == "CRIPTO": id_portfolio = ""
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         if tipo_invest == '' or tipo_invest == 'ACAO':
#             rows = UsuarioCarteiraAcao.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0) + (float(row['QUANTBONUS']) if row['QUANTBONUS'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_nota = float(row['NOTABALAC']) if row['NOTABALAC'] else 0.0
#                 lista.append([str(row['CODIGOATIVO']), inteiro_to_str(valor=float(tot_quant)), decimal_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_nota)), str(row['IDATIVO']), 'ACAO'])
#
#         if tipo_invest == '' or tipo_invest == 'FII':
#             rows = UsuarioCarteiraFii.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0) + (float(row['QUANTBONUS']) if row['QUANTBONUS'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_nota = float(row['NOTABALAC']) if row['NOTABALAC'] else 0.0
#                 lista.append([str(row['CODIGOFUNDO']), inteiro_to_str(valor=float(tot_quant)), decimal_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_nota)), str(row['IDFUNDO']), 'FII'])
#
#         if tipo_invest == '' or tipo_invest == 'ETF':
#             rows = UsuarioCarteiraEtf.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0) + (float(row['QUANTBONUS']) if row['QUANTBONUS'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_nota = float(row['NOTABALAC']) if row['NOTABALAC'] else 0.0
#                 lista.append([str(row['CODIGOINDICE']), inteiro_to_str(valor=float(tot_quant)), decimal_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_nota)), str(row['IDINDICE']), 'ETF'])
#
#         if tipo_invest == '' or tipo_invest == 'BDR':
#             rows = UsuarioCarteiraBdr.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0) + (float(row['QUANTBONUS']) if row['QUANTBONUS'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_nota = float(row['NOTABALAC']) if row['NOTABALAC'] else 0.0
#                 lista.append([str(row['CODIGOBDR']), inteiro_to_str(valor=float(tot_quant)), decimal_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_nota)), str(row['IDBDR']), 'BDR'])
#
#         if tipo_invest == '' or tipo_invest == 'CRIPTO':
#             rows = UsuarioCarteiraCripto.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_quant = (float(row['QUANT']) if row['QUANT'] else 0.0)
#                 tot_atual = tot_quant * vlr_preco_atual if tot_quant > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_nota = float(row['NOTABALAC']) if row['NOTABALAC'] else 0.0
#                 lista.append([str(row['CODIGOCRIPTO']), decimal_cripto_to_str(valor=float(tot_quant)), decimal_cripto_to_str(valor=float(vlr_preco_atual)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(vlr_nota)), str(row['IDCRIPTO']), 'CRIPTO'])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/salvarBalanceNotas', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_balance_notas():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         # if not data: data = request.get_json(silent=True)
#         # if not data: return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         try:
#             # lista = data.getlist('lista')
#             # lista = data.getlist('lista[]')
#             lista = data.to_dict()
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not lista:
#             return make_response(get_json_retorno_metodo(msg='Lisya não informada.'), 200)
#
#         id_usuario = current_user.id
#
#         idx = -1
#         while True:
#
#             try:
#                 idx += 1
#                 tipo_invest = str(lista['lista['+str(idx)+'][TipoInvest]'])
#                 codigo = str(lista['lista['+str(idx)+'][CodAtivo]'])
#                 nota = lista['lista['+str(idx)+'][Nota]']
#             except:
#                 break
#
#             if tipo_invest == 'ACAO':
#                 ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=codigo)
#                 if not ativo: return make_response(get_json_retorno_metodo(msg='Código do Ativo não localizado.'), 200)
#                 row = UsuarioCarteiraAcao.buscar_por_ativo(id_usuario=id_usuario, id_ativo=ativo.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='Ativo não localizado no Portfólio.'), 200)
#                 UsuarioCarteiraAcao.atualizar_nota_balanc(id=int(row['ID']), nota_balac=int(nota) if nota else 0)
#
#             elif tipo_invest == 'FII':
#                 fundo = FiiFundoImob.get_by_codigo(codigo=codigo)
#                 if not fundo: return make_response(get_json_retorno_metodo(msg='Código do FII não localizado.'), 200)
#                 row = UsuarioCarteiraFii.buscar_por_ativo(id_usuario=id_usuario, id_fundo=fundo.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='Ativo não localizado no Portfólio.'), 200)
#                 UsuarioCarteiraFii.atualizar_nota_balanc(id=int(row['ID']), nota_balac=int(nota) if nota else 0)
#
#             elif tipo_invest == 'ETF':
#                 indice = ETFIndice.get_by_codigo(codigo=codigo)
#                 if not indice: return make_response(get_json_retorno_metodo(msg='Código do ETF não localizada.'), 200)
#                 row = UsuarioCarteiraEtf.buscar_por_ativo(id_usuario=id_usuario, id_indice=indice.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='ETF não localizada no Portfólio.'), 200)
#                 UsuarioCarteiraEtf.atualizar_nota_balanc(id=int(row['ID']), nota_balac=int(nota) if nota else 0)
#
#             elif tipo_invest == 'BDR':
#                 ativo = BDREmpresa.get_by_codigo(codigo=codigo)
#                 if not ativo: return make_response(get_json_retorno_metodo(msg='Código da BDR não localizado.'), 200)
#                 row = UsuarioCarteiraBdr.buscar_por_ativo(id_usuario=id_usuario, id_bdr=ativo.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='BDR não localizado no Portfólio.'), 200)
#                 UsuarioCarteiraBdr.atualizar_nota_balanc(id=int(row['ID']), nota_balac=int(nota) if nota else 0)
#
#             elif tipo_invest == 'CRIPTO':
#                 cripto = CriptoEmpresa.get_by_codigo(codigo=codigo)
#                 if not cripto: return make_response(get_json_retorno_metodo(msg='Código do Cripto não localizada.'), 200)
#                 row = UsuarioCarteiraCripto.buscar_por_ativo(id_usuario=id_usuario, id_cripto=cripto.id)
#                 if not row: return make_response(get_json_retorno_metodo(msg='Cripto não localizada no Portfólio.'), 200)
#                 UsuarioCarteiraCripto.atualizar_nota_balanc(id=int(row['ID']), nota_balac=int(nota) if nota else 0)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/extrato', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def extrato():
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
#             codigo = data.get('CodAtivo')
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         dt_ini = str(dt_ini).replace('-', '') if dt_ini is not None else dt_ini
#         dt_fim = str(dt_fim).replace('-', '') if dt_fim is not None else dt_fim
#
#         tipo_invest = ''
#         if codigo and codigo == 'ACAO': tipo_invest = 'ACAO'
#         if codigo and codigo == 'FII': tipo_invest = 'FII'
#         if codigo and codigo == 'ETF': tipo_invest = 'ETF'
#         if codigo and codigo == 'BDR': tipo_invest = 'BDR'
#         if codigo and codigo == 'CRIPTO': tipo_invest = 'CRIPTO'
#         if tipo_invest: codigo = ''
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         if tipo_invest == '' or tipo_invest == 'ACAO':
#             lancamentos = UsuarioACAOEmpresaLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim)
#             lista += [[str(lanc['DATA']), UsuarioACAOEmpresaLancamento.descricao_tipo(tipo=str(lanc['TIPO']), troca=str(lanc['TROCA'])), str(lanc['CODIGOATIVO']), int(lanc['QUANT']), decimal_to_str(valor=float(lanc['VLRPRECO'])), decimal_to_str(valor=float(lanc['TOTVLRTX'])), decimal_to_str(valor=float(lanc['TOTVLR'])), 'ACAO'] for lanc in lancamentos]
#
#         if tipo_invest == '' or tipo_invest == 'FII':
#             lancamentos = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo,dt_ini=dt_ini, dt_fim=dt_fim)
#             lista += [[str(lanc['DATA']), UsuarioFiiFundoImobLancamento.descricao_tipo(tipo=str(lanc['TIPO']), troca=str(lanc['TROCA'])), str(lanc['CODIGOFUNDO']), int(lanc['QUANT']), decimal_to_str(valor=float(lanc['VLRPRECO'])), decimal_to_str(valor=float(lanc['TOTVLRTX'])), decimal_to_str(valor=float(lanc['TOTVLR'])), 'FII'] for lanc in lancamentos]
#
#         if tipo_invest == '' or tipo_invest == 'ETF':
#             lancamentos = UsuarioETFIndiceLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo,dt_ini=dt_ini, dt_fim=dt_fim)
#             lista += [[str(lanc['DATA']), UsuarioETFIndiceLancamento.descricao_tipo(tipo=str(lanc['TIPO']), troca=str(lanc['TROCA'])), str(lanc['CODIGOINDICE']), int(lanc['QUANT']), decimal_to_str(valor=float(lanc['VLRPRECO'])), decimal_to_str(valor=float(lanc['TOTVLRTX'])), decimal_to_str(valor=float(lanc['TOTVLR'])), 'ETF'] for lanc in lancamentos]
#
#         if tipo_invest == '' or tipo_invest == 'BDR':
#             lancamentos = UsuarioBDREmpresaLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim)
#             lista += [[str(lanc['DATA']), UsuarioBDREmpresaLancamento.descricao_tipo(tipo=str(lanc['TIPO']), troca=str(lanc['TROCA'])), str(lanc['CODIGOBDR']), int(lanc['QUANT']), decimal_to_str(valor=float(lanc['VLRPRECO'])), decimal_to_str(valor=float(lanc['TOTVLRTX'])), decimal_to_str(valor=float(lanc['TOTVLR'])), 'BDR'] for lanc in lancamentos]
#
#         if tipo_invest == '' or tipo_invest == 'CRIPTO':
#             lancamentos = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo,dt_ini=dt_ini, dt_fim=dt_fim)
#             lista += [[str(lanc['DATA']), UsuarioCriptoLancamento.descricao_tipo(tipo=str(lanc['TIPO']),), str(lanc['CODIGOCRIPTO']), float(lanc['QUANT']), decimal_cripto_to_str(valor=float(lanc['VLRPRECO'])), decimal_to_str(valor=float(lanc['VLRTAXA'])), decimal_to_str(valor=float(lanc['TOTVLR'])), 'CRIPTO'] for lanc in lancamentos]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/gridResumoOper', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumo_oper():
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
#             id_portfolio = data.get('IdPortfolio')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         data_atual = pegar_data_atual()
#
#         tipo_invest = ""
#         if id_portfolio and str(id_portfolio) == "ACAO": tipo_invest = "ACAO"
#         if id_portfolio and str(id_portfolio) == "FII": tipo_invest = "FII"
#         if id_portfolio and str(id_portfolio) == "ETF": tipo_invest = "ETF"
#         if id_portfolio and str(id_portfolio) == "BDR": tipo_invest = "BDR"
#         if id_portfolio and str(id_portfolio) == "CRIPTO": tipo_invest = "CRIPTO"
#         if id_portfolio and str(id_portfolio) == "ACAO" or str(id_portfolio) == "FII" or str(id_portfolio) == "ETF" or str(id_portfolio) == "BDR" or str(id_portfolio) == "CRIPTO": id_portfolio = ""
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         if tipo_invest == '' or tipo_invest == 'ACAO':
#             rows = UsuarioCarteiraAcao.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio)
#             for row in rows:
#                 id_ativo = int(row['IDATIVO'])
#                 tot_compra = UsuarioACAOEmpresaOperacao.buscar_valor_total_compra(id_usuario=id_usuario, id_ativo=id_ativo)
#                 if tot_compra <= 0.0: continue
#                 tot_bonus = UsuarioACAOEmpresaOperacao.buscar_valor_total_bonus(id_usuario=id_usuario, id_ativo=id_ativo)
#                 tot_venda = UsuarioACAOEmpresaOperacao.buscar_valor_total_venda(id_usuario=id_usuario, id_ativo=id_ativo)
#                 tot_proventos = UsuarioACAOEmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_ativo=id_ativo, dt_fim=data_atual)
#                 if str(row['SITUACAO']) == "A":
#                      qtde_compra = UsuarioACAOEmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_ativo=id_ativo)
#                      qtde_bonus = UsuarioACAOEmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_ativo=id_ativo)
#                      qtde_venda = UsuarioACAOEmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_ativo=id_ativo)
#                      qtde_saldo = (float(qtde_compra) + float(qtde_bonus)) - float(qtde_venda)
#                      if qtde_saldo > 0.0 and row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0: tot_venda += qtde_saldo * float(row['VLRPRECOFECHAMENTO'])
#                 tot_valorizacao  = tot_venda - (tot_compra + tot_bonus)
#                 perc_valorizacao = ( tot_valorizacao / (tot_compra + tot_bonus)) * 100 if tot_valorizacao != 0.0 and (tot_compra + tot_bonus) != 0.0 else 0.0
#                 tot_ganho_perda  = float(tot_valorizacao) + float(tot_proventos)
#                 perc_ganho_perda = ( tot_ganho_perda / (tot_compra + tot_bonus)) * 100 if tot_ganho_perda != 0.0 and (tot_compra + tot_bonus) != 0.0 else 0.0
#                 situacao = ""
#                 if str(row['SITUACAO']) == "A" and tot_ganho_perda > 0.0: situacao = "ATIVA COM LUCRO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda < 0.0: situacao = "ATIVA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda == 0.0: situacao = "ATIVA SEM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda > 0.0: situacao= "ENCERRADA COM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda < 0.0: situacao = "ENCERRADA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda == 0.0: situacao= "ENCERRADA SEM LUCRO"
#                 lista.append(['ACAO', str(row['CODIGOATIVO']), decimal_to_str(valor=float(tot_compra)), decimal_to_str(valor=float(tot_bonus)), decimal_to_str(valor=float(tot_venda)), decimal_to_str(valor=float(tot_valorizacao)) +' ( ' + decimal_to_str(valor=float(perc_valorizacao)) + '% )', decimal_to_str(valor=float(tot_proventos)), decimal_to_str(valor=float(tot_ganho_perda)) +' ( ' + decimal_to_str(valor=float(perc_ganho_perda)) + '% )', str(situacao)])
#
#         if tipo_invest == '' or tipo_invest == 'FII':
#             rows = UsuarioCarteiraFii.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio)
#             for row in rows:
#                 id_fundo = int(row['IDFUNDO'])
#                 tot_compra = UsuarioFiiFundoImobLancamento.buscar_valor_total_compra(id_usuario=id_usuario, id_fundo=id_fundo)
#                 tot_compra -= UsuarioFiiFundoImobLancamento.buscar_valor_total_amortizacao(id_usuario=id_usuario, id_fundo=id_fundo)
#                 if tot_compra <= 0.0: continue
#                 tot_bonus = UsuarioFiiFundoImobLancamento.buscar_valor_total_bonus(id_usuario=id_usuario, id_fundo=id_fundo)
#                 tot_venda = UsuarioFiiFundoImobLancamento.buscar_valor_total_venda(id_usuario=id_usuario, id_fundo=id_fundo)
#                 tot_proventos = UsuarioFiiFundoImobProvento.buscar_vlr_total(id_usuario=id_usuario, id_fundo=id_fundo, dt_fim=data_atual)
#                 if str(row['SITUACAO']) == "A":
#                      qtde_compra = UsuarioFiiFundoImobLancamento.buscar_total_compra(id_usuario=id_usuario, id_fundo=id_fundo)
#                      qtde_bonus = UsuarioFiiFundoImobLancamento.buscar_total_bonus(id_usuario=id_usuario, id_fundo=id_fundo)
#                      qtde_venda = UsuarioFiiFundoImobLancamento.buscar_total_venda(id_usuario=id_usuario, id_fundo=id_fundo)
#                      qtde_saldo = (float(qtde_compra) + float(qtde_bonus)) - float(qtde_venda)
#                      if qtde_saldo > 0.0 and row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0: tot_venda += qtde_saldo * float(row['VLRPRECOFECHAMENTO'])
#                 tot_valorizacao  = tot_venda - (tot_compra + tot_bonus)
#                 perc_valorizacao = (tot_valorizacao / (tot_compra + tot_bonus)) * 100 if tot_valorizacao != 0.0 and (tot_compra + tot_bonus) != 0.0 else 0.0
#                 tot_ganho_perda  = float(tot_valorizacao) + float(tot_proventos)
#                 perc_ganho_perda = (tot_ganho_perda / (tot_compra + tot_bonus)) * 100 if tot_ganho_perda != 0.0 and (tot_compra + tot_bonus) != 0.0 else 0.0
#                 situacao = ""
#                 if str(row['SITUACAO']) == "A" and tot_ganho_perda > 0.0: situacao = "ATIVA COM LUCRO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda < 0.0: situacao = "ATIVA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda == 0.0: situacao = "ATIVA SEM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda > 0.0: situacao= "ENCERRADA COM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda < 0.0: situacao = "ENCERRADA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda == 0.0: situacao= "ENCERRADA SEM LUCRO"
#                 lista.append(['FII', str(row['CODIGOFUNDO']), decimal_to_str(valor=float(tot_compra)), decimal_to_str(valor=float(tot_bonus)), decimal_to_str(valor=float(tot_venda)), decimal_to_str(valor=float(tot_valorizacao)) +' ( ' + decimal_to_str(valor=float(perc_valorizacao)) + '% )', decimal_to_str(valor=float(tot_proventos)), decimal_to_str(valor=float(tot_ganho_perda)) +' ( ' + decimal_to_str(valor=float(perc_ganho_perda)) + '% )', str(situacao)])
#
#         if tipo_invest == '' or tipo_invest == 'ETF':
#             rows = UsuarioCarteiraEtf.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio)
#             for row in rows:
#                 id_indice = int(row['IDINDICE'])
#                 tot_compra = UsuarioETFIndiceOperacao.buscar_valor_total_compra(id_usuario=id_usuario, id_indice=id_indice)
#                 if tot_compra <= 0.0: continue
#                 tot_bonus = UsuarioETFIndiceOperacao.buscar_valor_total_bonus(id_usuario=id_usuario, id_indice=id_indice)
#                 tot_venda = UsuarioETFIndiceOperacao.buscar_valor_total_venda(id_usuario=id_usuario, id_indice=id_indice)
#                 tot_proventos = 0.0
#                 if str(row['SITUACAO']) == "A":
#                      qtde_compra = UsuarioETFIndiceOperacao.buscar_total_compra(id_usuario=id_usuario, id_indice=id_indice)
#                      qtde_bonus = UsuarioETFIndiceOperacao.buscar_total_bonus(id_usuario=id_usuario, id_indice=id_indice)
#                      qtde_venda = UsuarioETFIndiceOperacao.buscar_total_venda(id_usuario=id_usuario, id_indice=id_indice)
#                      qtde_saldo = (float(qtde_compra) + float(qtde_bonus)) - float(qtde_venda)
#                      if qtde_saldo > 0.0 and row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0: tot_venda += qtde_saldo * float(row['VLRPRECOFECHAMENTO'])
#                 tot_valorizacao  = tot_venda - (tot_compra + tot_bonus)
#                 perc_valorizacao = (tot_valorizacao / (tot_compra + tot_bonus)) * 100 if tot_valorizacao != 0.0 and (tot_compra + tot_bonus) != 0.0 else 0.0
#                 tot_ganho_perda  = float(tot_valorizacao) + float(tot_proventos)
#                 perc_ganho_perda = (tot_ganho_perda / (tot_compra + tot_bonus)) * 100 if tot_ganho_perda != 0.0 and (tot_compra + tot_bonus) != 0.0 else 0.0
#                 situacao = ""
#                 if str(row['SITUACAO']) == "A" and tot_ganho_perda > 0.0: situacao = "ATIVA COM LUCRO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda < 0.0: situacao = "ATIVA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda == 0.0: situacao = "ATIVA SEM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda > 0.0: situacao= "ENCERRADA COM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda < 0.0: situacao = "ENCERRADA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda == 0.0: situacao= "ENCERRADA SEM LUCRO"
#                 lista.append(['ETF', str(row['CODIGOINDICE']), decimal_to_str(valor=float(tot_compra)), decimal_to_str(valor=float(tot_bonus)), decimal_to_str(valor=float(tot_venda)), decimal_to_str(valor=float(tot_valorizacao)) +' ( ' + decimal_to_str(valor=float(perc_valorizacao)) + '% )', decimal_to_str(valor=float(tot_proventos)), decimal_to_str(valor=float(tot_ganho_perda)) +' ( ' + decimal_to_str(valor=float(perc_ganho_perda)) + '% )', str(situacao)])
#
#         if tipo_invest == '' or tipo_invest == 'BDR':
#             rows = UsuarioCarteiraBdr.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio)
#             for row in rows:
#                 id_ativo = int(row['IDBDR'])
#                 tot_compra = UsuarioBDREmpresaOperacao.buscar_valor_total_compra(id_usuario=id_usuario, id_bdr=id_ativo)
#                 if tot_compra <= 0.0: continue
#                 tot_bonus = UsuarioBDREmpresaOperacao.buscar_valor_total_bonus(id_usuario=id_usuario, id_bdr=id_ativo)
#                 tot_venda = UsuarioBDREmpresaOperacao.buscar_valor_total_venda(id_usuario=id_usuario, id_bdr=id_ativo)
#                 tot_proventos = UsuarioBDREmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_bdr=id_ativo, dt_fim=data_atual)
#                 if str(row['SITUACAO']) == "A":
#                      qtde_compra = UsuarioBDREmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_bdr=id_ativo)
#                      qtde_bonus = UsuarioBDREmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_bdr=id_ativo)
#                      qtde_venda = UsuarioBDREmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_bdr=id_ativo)
#                      qtde_saldo = (float(qtde_compra) + float(qtde_bonus)) - float(qtde_venda)
#                      if qtde_saldo > 0.0 and row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0: tot_venda += qtde_saldo * float(row['VLRPRECOFECHAMENTO'])
#                 tot_valorizacao  = tot_venda - (tot_compra + tot_bonus)
#                 perc_valorizacao = ( tot_valorizacao / (tot_compra + tot_bonus)) * 100 if tot_valorizacao != 0.0 and (tot_compra + tot_bonus) != 0.0 else 0.0
#                 tot_ganho_perda  = float(tot_valorizacao) + float(tot_proventos)
#                 perc_ganho_perda = ( tot_ganho_perda / (tot_compra + tot_bonus)) * 100 if tot_ganho_perda != 0.0 and (tot_compra + tot_bonus) != 0.0 else 0.0
#                 situacao = ""
#                 if str(row['SITUACAO']) == "A" and tot_ganho_perda > 0.0: situacao = "ATIVA COM LUCRO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda < 0.0: situacao = "ATIVA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda == 0.0: situacao = "ATIVA SEM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda > 0.0: situacao= "ENCERRADA COM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda < 0.0: situacao = "ENCERRADA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda == 0.0: situacao= "ENCERRADA SEM LUCRO"
#                 lista.append(['BDR', str(row['CODIGOBDR']), decimal_to_str(valor=float(tot_compra)), decimal_to_str(valor=float(tot_bonus)), decimal_to_str(valor=float(tot_venda)), decimal_to_str(valor=float(tot_valorizacao)) +' ( ' + decimal_to_str(valor=float(perc_valorizacao)) + '% )', decimal_to_str(valor=float(tot_proventos)), decimal_to_str(valor=float(tot_ganho_perda)) +' ( ' + decimal_to_str(valor=float(perc_ganho_perda)) + '% )', str(situacao)])
#
#         if tipo_invest == '' or tipo_invest == 'CRIPTO':
#             rows = UsuarioCarteiraCripto.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio)
#             for row in rows:
#                 id_cripto = int(row['IDCRIPTO'])
#                 tot_compra = UsuarioCriptoLancamento.buscar_valor_total_compra(id_usuario=id_usuario, id_cripto=id_cripto)
#                 if tot_compra <= 0.0: continue
#                 tot_venda = UsuarioCriptoLancamento.buscar_valor_total_venda(id_usuario=id_usuario, id_cripto=id_cripto)
#                 if str(row['SITUACAO']) == "A":
#                      qtde_compra = UsuarioCriptoLancamento.buscar_total_compra(id_usuario=id_usuario, id_cripto=id_cripto)
#                      qtde_venda = UsuarioCriptoLancamento.buscar_total_venda(id_usuario=id_usuario, id_cripto=id_cripto)
#                      qtde_saldo = float(qtde_compra) - float(qtde_venda)
#                      if qtde_saldo > 0.0 and row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0: tot_venda += qtde_saldo * float(row['VLRPRECOFECHAMENTO'])
#                 tot_valorizacao  = tot_venda - tot_compra
#                 perc_valorizacao = (tot_valorizacao / tot_compra) * 100 if tot_valorizacao != 0.0 and tot_compra != 0.0 else 0.0
#                 tot_ganho_perda  = float(tot_valorizacao)
#                 perc_ganho_perda = (tot_ganho_perda / tot_compra) * 100 if tot_ganho_perda != 0.0 and tot_compra != 0.0 else 0.0
#                 situacao = ""
#                 if str(row['SITUACAO']) == "A" and tot_ganho_perda > 0.0: situacao = "ATIVA COM LUCRO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda < 0.0: situacao = "ATIVA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "A" and tot_ganho_perda == 0.0: situacao = "ATIVA SEM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda > 0.0: situacao= "ENCERRADA COM LUCRO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda < 0.0: situacao = "ENCERRADA COM PREJUIZO"
#                 elif str(row['SITUACAO']) == "F" and tot_ganho_perda == 0.0: situacao= "ENCERRADA SEM LUCRO"
#                 lista.append(['CRIPTO', str(row['CODIGOCRIPTO']), decimal_to_str(valor=float(tot_compra)), decimal_to_str(valor=0.0), decimal_to_str(valor=float(tot_venda)), decimal_to_str(valor=float(tot_valorizacao)) + ' ( ' + decimal_to_str(valor=float(perc_valorizacao)) + '% )', decimal_to_str(valor=0.0), decimal_to_str(valor=float(tot_ganho_perda)) + ' ( ' + decimal_to_str(valor=float(perc_ganho_perda)) + '% )', str(situacao)])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/drawdown', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def drawdown():
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
#             qtd_dias = data.get('QtdDias')
#             margem = data.get('Margem')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         qtd_dias = int(qtd_dias) if qtd_dias and int(qtd_dias) > 0 else None
#         margem = float(str(margem).replace(',', '.')) if margem else None
#
#         if not qtd_dias: return make_response(get_json_retorno_grid(msg='Campo Dias não informado.'), 200)
#         if not margem: return make_response(get_json_retorno_grid(msg='Campo Margem não informada.'), 200)
#
#         if qtd_dias <= 0: return make_response(get_json_retorno_grid(msg='Campo Dias Inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo='DRAWDOWN_DIAS')
#         if not config: config = UsuarioConfig(id_usuario=id_usuario, tipo='DRAWDOWN_DIAS')
#         config.valor = str(qtd_dias)
#         config.salvar()
#
#         config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo='DRAWDOWN_MARGEM')
#         if not config: config = UsuarioConfig(id_usuario=id_usuario, tipo='DRAWDOWN_MARGEM')
#         config.valor = str(margem).replace('.', ',')
#         config.salvar()
#
#         id_portfolio = None
#         data_atual = pegar_data_atual(istext=False)
#         data_ini = converter_datetime_str(data=data_atual + adicionar_dias(dias=-qtd_dias))
#         data_fim = converter_datetime_str(data=data_atual)
#
#         lista = []
#
#         def adicionar_drawdown(atv_tipo: str, atv_tipo_descr: str, atv_codigo: str, atv_vlr_cotacao: float):
#             atv_vlr_maxima = ACAOEmpresaAtivoCotacaoHist.buscar_maxima(categoria=atv_tipo, codigo=atv_codigo, dt_ini=data_ini, dt_fim=data_fim)
#             if atv_vlr_cotacao > atv_vlr_maxima: atv_vlr_maxima = atv_vlr_cotacao
#             atv_vlr_dif = atv_vlr_maxima - atv_vlr_cotacao
#             atv_vlr_drawdown = atv_vlr_maxima - ((atv_vlr_maxima / 100) * margem) if margem > 0 else atv_vlr_maxima
#             atv_pct_margem = 0.0
#             if atv_vlr_dif != 0.0: atv_pct_margem = (float(atv_vlr_dif) / float(atv_vlr_maxima)) * 100.0
#             atv_pct_margem = float('%.2f' % float(atv_pct_margem))
#             return [atv_tipo_descr, atv_tipo, atv_codigo, atv_vlr_cotacao, atv_vlr_maxima, atv_vlr_drawdown, atv_pct_margem]
#
#         # PORTFOLIO - ACAO
#         rows = UsuarioCarteiraAcao.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#         lista += [adicionar_drawdown(atv_tipo='ACAO', atv_tipo_descr='PORTFÓLIO', atv_codigo=str(row['CODIGOATIVO']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0) for row in rows]
#
#         # PORTFOLIO - FII
#         rows = UsuarioCarteiraFii.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#         lista += [adicionar_drawdown(atv_tipo='FII', atv_tipo_descr='PORTFÓLIO', atv_codigo=str(row['CODIGOFUNDO']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0) for row in rows]
#
#         # PORTFOLIO - ETF
#         rows = UsuarioCarteiraEtf.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#         lista += [adicionar_drawdown(atv_tipo='ETF', atv_tipo_descr='PORTFÓLIO', atv_codigo=str(row['CODIGOINDICE']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0) for row in rows]
#
#         # PORTFOLIO - BDR
#         rows = UsuarioCarteiraBdr.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#         lista += [adicionar_drawdown(atv_tipo='BDR', atv_tipo_descr='PORTFÓLIO', atv_codigo=str(row['CODIGOBDR']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0) for row in rows]
#
#         # PORTFOLIO - CRIPTO
#         rows = UsuarioCarteiraCripto.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#         lista += [adicionar_drawdown(atv_tipo='CRIPTO', atv_tipo_descr='PORTFÓLIO', atv_codigo=str(row['CODIGOCRIPTO']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0) for row in rows]
#
#         # RADAR - ACAO
#         rows = UsuarioRadarAcao.buscar_dados_grid_port(id_usuario=id_usuario)
#         lista += [adicionar_drawdown(atv_tipo='ACAO', atv_tipo_descr='RADAR', atv_codigo=str(row['CODIGOATIVO']), atv_vlr_cotacao=float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0) for row in rows]
#
#         # RADAR - FII
#         rows = UsuarioRadarFii.buscar_dados_grid_port(id_usuario=id_usuario)
#         lista += [adicionar_drawdown(atv_tipo='FII', atv_tipo_descr='RADAR', atv_codigo=str(row['CODIGOATIVO']), atv_vlr_cotacao=float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0) for row in rows]
#
#         # RADAR - ETF
#         rows = UsuarioRadarEtf.buscar_dados_grid_port(id_usuario=id_usuario)
#         lista += [adicionar_drawdown(atv_tipo='ETF', atv_tipo_descr='RADAR', atv_codigo=str(row['CODIGOATIVO']), atv_vlr_cotacao=float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0) for row in rows]
#
#         # RADAR - BDR
#         rows = UsuarioRadarBdr.buscar_dados_grid_port(id_usuario=id_usuario)
#         lista += [adicionar_drawdown(atv_tipo='BDR', atv_tipo_descr='RADAR', atv_codigo=str(row['CODIGOBDR']), atv_vlr_cotacao=float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0) for row in rows]
#
#         # RADAR - CRIPTO
#         rows = UsuarioRadarCripto.buscar_dados_grid_port(id_usuario=id_usuario)
#         lista += [adicionar_drawdown(atv_tipo='CRIPTO', atv_tipo_descr='RADAR', atv_codigo=str(row['CODIGOATIVO']), atv_vlr_cotacao=float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0) for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/griddrawdown', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_drawdown():
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
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_grid(msg='Código do Ativo não informado.'), 200)
#
#         tipo_invest = ''
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=codigo): tipo_invest = 'ACAO'
#         elif FiiFundoImob.get_by_codigo(codigo=codigo): tipo_invest = 'FII'
#         elif ETFIndice.get_by_codigo(codigo=codigo): tipo_invest = 'ETF'
#         elif BDREmpresa.get_by_codigo(codigo=codigo): tipo_invest = 'BDR'
#         elif CriptoEmpresa.get_by_codigo(codigo=codigo): tipo_invest = 'CRIPTO'
#         if not tipo_invest: return make_response(get_json_retorno_grid(msg='Código do Ativo inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         qtd_dias = 120
#         config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo='DRAWDOWN_DIAS')
#         if config: qtd_dias = int(config.valor)
#
#         margem = 20
#         config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo='DRAWDOWN_MARGEM')
#         if config: margem = float(str(config.valor).replace(',', '.'))
#
#         data_atual = pegar_data_atual(istext=False)
#         data_ini = converter_datetime_str(data=data_atual + adicionar_dias(dias=-qtd_dias))
#         data_fim = converter_datetime_str(data=data_atual)
#
#         rows = ACAOEmpresaAtivoCotacaoHist.buscar_todos(categoria=tipo_invest, codigo=codigo, dt_ini=data_ini, dt_fim=data_fim)
#         if not rows: return make_response(get_json_retorno_grid(msg='Ativo sem Dados.'), 200)
#
#         lista = []
#         itemMaximo = 0.0
#
#         for row in rows:
#             itemData = str(row['DATA'])
#             itemCotacao = float(row['COTACAO']) if row['COTACAO'] else 0.00
#             itemMaximo = itemCotacao if itemCotacao > itemMaximo else itemMaximo
#             itemDiferenca = itemMaximo - itemCotacao
#             itemMargem = 0.0
#             if itemDiferenca != 0.0: itemMargem = (float(itemDiferenca) / float(itemMaximo)) * 100.0
#             itemMargem = float('%.2f' % float(itemMargem))
#             lista.append([itemData, itemCotacao, itemMaximo, itemMargem])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/EvolucaoDetalhada', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
# def evolucao_detalhada():
#     try:
#
#         result = ''
#
#         id_usuario = current_user.id
#         ano_mes_atual = pegar_data_atual(fmt="%Y%m")
#         anos = []
#
#         try:
#
#             anos.append(pegar_data_atual())
#             anos.append(UsuarioACAOEmpresaLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#             anos.append(UsuarioFiiFundoImobLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#             anos.append(UsuarioETFIndiceLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#             anos.append(UsuarioBDREmpresaLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#             anos.append(UsuarioCriptoLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#
#             menor = min(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#             maior = max(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#
#         except:
#             menor = None
#             maior = None
#
#         if not menor or not maior: return make_response(result, 200)
#
#         ativos = ACAOEmpresaAtivo.buscar_todos_codigos_comprados_com_fiis_etfs_bdrs_criptos(id_usuario=id_usuario)
#         if not ativos: return make_response(result, 200)
#
#         lista_cod_ativos = [{'ID': int(ativo['ID']), 'CODIGO': str(ativo['CODIGO']), 'TIPO': str(ativo['TIPO'])} for ativo in ativos]
#
#         # lista_cotacao = []
#         # for ativo in lista_cod_ativos:
#         #     lista_cotacao.append({})
#
#         lista_princ_ativos = []
#         lista_princ_oper = []
#
#         for ativo in lista_cod_ativos:
#             lista_princ_ativos.append({"ID": int(ativo['ID']), "CODIGO": str(ativo['CODIGO']), "TIPOINVEST": str(ativo['TIPO']), "QUANT": 0.0,"QUANTTOT": 0.0, 'PRECOMEDIO': 0.0, 'COTACAO': 0.0, 'TOTAL': 0.0})
#             if str(ativo['TIPO']) == 'ACAO':
#                 opers = UsuarioACAOEmpresaOperacao.buscar_todos(id_usuario=id_usuario, codigo=str(ativo['CODIGO']), dt_ini=str(menor) + "0101", dt_fim=str(maior) + "1231")
#                 lista_princ_oper += [{"ID": int(ativo['ID']), "CODIGO": str(ativo['CODIGO']), "TIPOINVEST": str(ativo['TIPO']), "DATA": str(oper['DATA']), "TIPO": str(oper['TIPO']), "QUANT": float(oper['QUANT']) if oper['QUANT'] else 0, "PRECOMEDIO": float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] else 0.0} for oper in opers]
#             elif str(ativo['TIPO']) == 'FII':
#                 opers = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, codigo=str(ativo['CODIGO']), dt_ini=str(menor) + "0101", dt_fim=str(maior) + "1231")
#                 lista_princ_oper += [{"ID": int(ativo['ID']), "CODIGO": str(ativo['CODIGO']), "TIPOINVEST": str(ativo['TIPO']), "DATA": str(oper['DATA']), "TIPO": str(oper['TIPO']), "QUANT": float(oper['QUANT']) if oper['QUANT'] else 0, "PRECOMEDIO": float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] else 0.0} for oper in opers]
#             elif str(ativo['TIPO']) == 'ETF':
#                 opers = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, codigo=str(ativo['CODIGO']), dt_ini=str(menor) + "0101", dt_fim=str(maior) + "1231")
#                 lista_princ_oper += [{"ID": int(ativo['ID']), "CODIGO": str(ativo['CODIGO']), "TIPOINVEST": str(ativo['TIPO']), "DATA": str(oper['DATA']), "TIPO": str(oper['TIPO']), "QUANT": float(oper['QUANT']) if oper['QUANT'] else 0, "PRECOMEDIO": float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] else 0.0} for oper in opers]
#             elif str(ativo['TIPO']) == 'BDR':
#                 opers = UsuarioBDREmpresaOperacao.buscar_todos(id_usuario=id_usuario, codigo=str(ativo['CODIGO']), dt_ini=str(menor) + "0101", dt_fim=str(maior) + "1231")
#                 lista_princ_oper += [{"ID": int(ativo['ID']), "CODIGO": str(ativo['CODIGO']), "TIPOINVEST": str(ativo['TIPO']), "DATA": str(oper['DATA']), "TIPO": str(oper['TIPO']), "QUANT": float(oper['QUANT']) if oper['QUANT'] else 0, "PRECOMEDIO": float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] else 0.0} for oper in opers]
#             elif str(ativo['TIPO']) == 'CRIPTO':
#                 opers = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, codigo=str(ativo['CODIGO']), dt_ini=str(menor) + "0101", dt_fim=str(maior) + "1231")
#                 lista_princ_oper += [{"ID": int(ativo['ID']), "CODIGO": str(ativo['CODIGO']), "TIPOINVEST": str(ativo['TIPO']), "DATA": str(oper['DATA']), "TIPO": str(oper['TIPO']), "QUANT": float(oper['QUANT']) if oper['QUANT'] else 0, "PRECOMEDIO": float(oper['VLRPRECOMEDIO']) if oper['VLRPRECOMEDIO'] else 0.0} for oper in opers]
#
#         lista_princ_meses = [{"NUMMES": str(mes).zfill(2), "NOMEMES": buscar_nome_mes_resumido(int(mes)), "ATIVOS": deepcopy(lista_princ_ativos), "TOTALACAO": 0.0, "TOTALFII": 0.0, "TOTALETF": 0.0, "TOTALBDR": 0.0, "TOTALCRIPTO": 0.0, "TOTALPORTFOLIO": 0.0, } for mes in range(1, 13)]
#
#         lista_princ = [{"ANO": str(ano), "MESES": deepcopy(lista_princ_meses)} for ano in range(menor, maior + 1)]
#
#         for ativo in lista_cod_ativos:
#             codigo_princ = str(ativo['CODIGO'])
#             qtde_tot_ativo = 0
#             preco_med_ativo = 0.0
#             for row_princ in lista_princ:
#                 num_ano = str(row_princ['ANO'])
#                 lista_princ_meses_local = deepcopy(row_princ['MESES'])
#                 for row_mes in lista_princ_meses_local:
#                     num_mes = str(row_mes['NUMMES'])
#                     lista_princ_ativos_local = deepcopy(row_mes['ATIVOS'])
#                     for row_ativo in lista_princ_ativos_local:
#                         codigo_mes = str(row_ativo['CODIGO'])
#                         if str(codigo_mes) == str(codigo_princ):
#                             qtde_ativo = 0
#                             for row_oper in lista_princ_oper:
#                                 codigo_oper = str(row_oper["CODIGO"])
#                                 dt_ativ_oper = str(row_oper["DATA"])
#                                 tp_ativ_oper = str(row_oper["TIPO"])
#                                 qtd_ativ_oper = float(row_oper["QUANT"])
#                                 dt_ini = str(num_ano)+str(num_mes)+'01'
#                                 dt_fim = str(num_ano)+str(num_mes)+'31'
#                                 if str(codigo_oper) == str(codigo_princ) and str(dt_ativ_oper) >= dt_ini and str(dt_ativ_oper) <= dt_fim:
#                                     if str(tp_ativ_oper) == 'C' or str(tp_ativ_oper) == 'B': qtde_ativo += float(qtd_ativ_oper)
#                                     elif str(tp_ativ_oper) == 'V' or str(tp_ativ_oper) == 'A' or str(tp_ativ_oper) == 'P': qtde_ativo -= float(qtd_ativ_oper)
#                                     preco_med_ativo = float(row_oper["PRECOMEDIO"])
#                             if str(num_ano)+str(num_mes) <= str(ano_mes_atual):
#                                 qtde_tot_ativo += float(qtde_ativo)
#                                 row_ativo['QUANT'] = float(qtde_ativo)
#                                 row_ativo['QUANTTOT'] = float(qtde_tot_ativo)
#                                 if qtde_tot_ativo > 0:
#                                     row_ativo['PRECOMEDIO'] = float(preco_med_ativo) if preco_med_ativo and float(preco_med_ativo) > 0.0 else 0.0
#                                     row_ativo['COTACAO'] = 0.0
#                                     row_ativo['TOTAL'] = (preco_med_ativo * float(qtde_tot_ativo)) if preco_med_ativo and float(preco_med_ativo) > 0.0 else 0.0
#                     row_mes['ATIVOS'] = lista_princ_ativos_local
#                 row_princ['MESES'] = lista_princ_meses_local
#
#         #lista_princ.sort(reverse=True)
#         if lista_princ: lista_princ = sorted(lista_princ, reverse=True, key=lambda k: k['ANO'])
#
#         result += '<!-- Div Row Accordion -->'
#         result += '<div id="DivA ccordion"  style="width: 100%">'
#
#         for row_princ in lista_princ:
#
#             num_ano = str(row_princ['ANO'])
#             lista_princ_meses = deepcopy(row_princ['MESES'])
#
#             result += '          <!-- Div Card Accordion Ano -->'
#             result += '          <div class="card border-dark" style="margin-bottom: 10px; ">'
#             result += '             <div class="card-header bg-dark" id="DivTitulo' + num_ano + '" style="padding: 0px; ">'
#             result += '                 <button class="btn btn-sm btn-link text-white ' + ('' if str(num_ano) == str(maior) else 'collapsed') + '" data-toggle="collapse" data-target="#DivConteudo' + num_ano + '" aria-expanded="' + ('true' if  str(num_ano) == str(maior) else 'false') + '" aria-controls="DivConteudo' + num_ano + '">Ano: ' + num_ano + ' </button> '
#             result += '             </div>'
#             result += '             <div id="DivConteudo' + num_ano + '" class="collapse ' + ('show' if str(num_ano) == str(maior) else '') + '" aria-labelledby="DivTitulo' + num_ano + '" data-parent="#DivAccordion" aria-expanded="' + ('true' if  str(num_ano) == str(maior) else 'false') + '">'
#             result += '               <!-- Div Card Body -->'
#             result += '               <div class="card-body" style="padding: 10px; ">'
#
#             result += '                  <br/>'
#             result += '                  <!-- Div Table Responsive -->'
#             result += '                  <div class="table-responsive">'
#             result += '                      <table class="table table-filter-cms table-sm table-hover tab le-condensed nowrap text-center" border="0" cellspacing="0" width="100%" style="font-size: 12px; margin: 0px;">'
#             result += '                          <col width="5">'
#             result += '                          <col width="8">'
#             result += ''.join(['                  <col width="10">' for mes in range(1, 13)])
#             result += '                          <thead class="table-info">'
#             result += '                          <tr>'
#             result += '                              <th scope="col">ATIVO</th>'
#             result += '                              <th scope="col">TIPO</th>'
#             result += ''.join([ '                    <th scope="col">' + buscar_nome_mes_resumido(int(mes)) + '</th>' for mes in range(1, 13)])
#             result += '                          </tr>'
#             result += '                          </thead>'
#             result += '                          <tbody>'
#
#             lista_ativos_por_mes = []
#
#             for ativo in lista_cod_ativos:
#                 cria_ativo = False
#                 lista_mensal_atv = []
#                 codigo = str(ativo['CODIGO'])
#                 tipo = str(ativo['TIPO'])
#                 for row_mes in lista_princ_meses:
#                     num_mes = str(row_mes['NUMMES'])
#                     lista_princ_ativos = deepcopy(row_mes['ATIVOS'])
#                     prc_tot_mensal_acao = 0.0
#                     prc_tot_mensal_fii = 0.0
#                     prc_tot_mensal_etf = 0.0
#                     prc_tot_mensal_bdr = 0.0
#                     prc_tot_mensal_cripto = 0.0
#                     for row_ativo in lista_princ_ativos:
#                         codigo_mes = str(row_ativo['CODIGO'])
#                         tp_ativo_mess = str(row_ativo['TIPOINVEST'])
#                         qtd_tot_ativo_mes = float(row_ativo['QUANTTOT']) if row_ativo['QUANTTOT'] else 0
#                         prc_medio_ativo_mes = float(row_ativo['PRECOMEDIO']) if row_ativo['PRECOMEDIO'] else 0
#                         prc_tot_ativo_mes = float(row_ativo['TOTAL']) if row_ativo['TOTAL'] else 0
#                         if str(codigo) == str(codigo_mes):
#                             lista_mensal_atv.append({"NUMMES": str(num_mes), "QUANTTOT": float(qtd_tot_ativo_mes), "PRECOMEDIO": float(prc_medio_ativo_mes), "COTACAO": 0.0, "TOTAL": float(prc_tot_ativo_mes), "TOTALATUAL": 0.0, "VALORIZACAO": 0.0})
#                             if qtd_tot_ativo_mes > 0: cria_ativo = True
#                         if str(num_ano)+str(num_mes) <= ano_mes_atual:
#                             if str(tp_ativo_mess) == 'ACAO': prc_tot_mensal_acao += float(prc_tot_ativo_mes)
#                             elif str(tp_ativo_mess) == 'FII': prc_tot_mensal_fii += float(prc_tot_ativo_mes)
#                             elif str(tp_ativo_mess) == 'ETF': prc_tot_mensal_etf += float(prc_tot_ativo_mes)
#                             elif str(tp_ativo_mess) == 'BDR': prc_tot_mensal_bdr += float(prc_tot_ativo_mes)
#                             elif str(tp_ativo_mess) == 'CRIPTO': prc_tot_mensal_cripto += float(prc_tot_ativo_mes)
#                     row_mes['TOTALACAO'] = float(prc_tot_mensal_acao)
#                     row_mes['TOTALFII'] = float(prc_tot_mensal_fii)
#                     row_mes['TOTALETF'] = float(prc_tot_mensal_etf)
#                     row_mes['TOTALBDR'] = float(prc_tot_mensal_bdr)
#                     row_mes['TOTALCRIPTO'] = float(prc_tot_mensal_cripto)
#                     row_mes['TOTALPORTFOLIO'] = float(prc_tot_mensal_acao) + float(prc_tot_mensal_fii) + float(prc_tot_mensal_etf) + float(prc_tot_mensal_bdr)+ float(prc_tot_mensal_cripto)
#                 if cria_ativo: lista_ativos_por_mes.append({"CODIGO": codigo, "TIPOINVEST": tipo, "MESES": lista_mensal_atv})
#
#             for row_ativo in lista_ativos_por_mes:
#                 codigo = str(row_ativo["CODIGO"])
#                 tp_ativo_mess = str(row_ativo['TIPOINVEST'])
#                 lista_mensal_atv = deepcopy(row_ativo["MESES"])
#                 result += '                          <tr>'
#                 result += '                              <th colspan="14" data-tipo="default"></th>'
#                 result += '                          </tr>'
#                 result += '                          <tr>'
#                 result += '                              <th scope="row" rowspan="3" class="xl-blue align-middle" data-tipo="default">' + codigo + '</th>'
#                 result += '                              <td class="xl-khaki font-weight-bold" data-tipo="qtde">Qtd. Total</td>'
#                 if tp_ativo_mess == 'CRIPTO':
#                     result += ''.join(['                     <td data-tipo="qtde">' + (decimal_cripto_to_str(valor=float(row_ativo_mes['QUANTTOT'])) if row_ativo_mes['QUANTTOT'] and float(row_ativo_mes['QUANTTOT']) > 0.0 else '') + '</td>'for row_ativo_mes in lista_mensal_atv])
#                 else:
#                     result += ''.join(['                     <td data-tipo="qtde">' + (inteiro_to_str(valor=float(row_ativo_mes['QUANTTOT'])) if row_ativo_mes['QUANTTOT'] and float(row_ativo_mes['QUANTTOT']) > 0.0 else '') + '</td>'for row_ativo_mes in lista_mensal_atv])
#                 result += '                          </tr>'
#                 result += '                          <tr>'
#                 result += '                              <td class="xl-khaki font-weight-bold" data-tipo="preco">Preço Médio</td>'
#                 if tp_ativo_mess == 'CRIPTO':
#                     result += ''.join(['                     <td data-tipo="preco">' + ('R$ ' + decimal_cripto_to_str(valor=float(row_ativo_mes['PRECOMEDIO'])) if row_ativo_mes['PRECOMEDIO'] and float(row_ativo_mes['PRECOMEDIO']) > 0.0 else '') + '</td>'for row_ativo_mes in lista_mensal_atv])
#                 else:
#                     result += ''.join(['                     <td data-tipo="preco">' + ('R$ ' + decimal_to_str(valor=float(row_ativo_mes['PRECOMEDIO'])) if row_ativo_mes['PRECOMEDIO'] and float(row_ativo_mes['PRECOMEDIO']) > 0.0 else '') + '</td>'for row_ativo_mes in lista_mensal_atv])
#                 result += '                          </tr>'
#                 result += '                          <tr>'
#                 result += '                              <td class="xl-khaki font-weight-bold" data-tipo="total">Tot. Invest.</td>'
#                 result += ''.join(['                     <td data-tipo="total">' + ('R$ ' + decimal_to_str(valor=float(row_ativo_mes['TOTAL'])) if row_ativo_mes['TOTAL'] and float(row_ativo_mes['TOTAL']) > 0.0 else '') + '</td>' for row_ativo_mes in lista_mensal_atv])
#                 result += '                          </tr>'
#
#             result += '                          <tr>'
#             result += '                              <td colspan="14" data-tipo="total"><br></td>'
#             result += '                          </tr>'
#             result += '                          <tr>'
#             result += '                              <td scope="row" rowspan="6" class="xl-blue align-middle  font-weight-bold" data-tipo="total">TOTAL R$</td>'
#             result += '                              <td class="xl-khaki font-weight-bold" data-tipo="total">AÇÕES</td>'
#             result += ''.join(['                     <td data-tipo="total">' + ('R$ ' + decimal_to_str(valor=float(row_mes['TOTALACAO'])) if row_mes['TOTALACAO'] and float(row_mes['TOTALACAO']) > 0.0 else '') + '</td>'for row_mes in lista_princ_meses])
#             result += '                          </tr>'
#             result += '                          <tr>'
#             result += '                              <td class="xl-khaki font-weight-bold" data-tipo="total">FIIs</td>'
#             result += ''.join(['                     <td data-tipo="total">' + ('R$ ' + decimal_to_str(valor=float(row_mes['TOTALFII'])) if row_mes['TOTALFII'] and float(row_mes['TOTALFII']) > 0.0 else '') + '</td>'for row_mes in lista_princ_meses])
#             result += '                          </tr>'
#             result += '                          <tr>'
#             result += '                              <td class="xl-khaki font-weight-bold" data-tipo="total">ETFs</td>'
#             result += ''.join(['                     <td data-tipo="total">' + ('R$ ' + decimal_to_str(valor=float(row_mes['TOTALETF'])) if row_mes['TOTALETF'] and float(row_mes['TOTALETF']) > 0.0 else '') + '</td>'for row_mes in lista_princ_meses])
#             result += '                          </tr>'
#             result += '                          <tr>'
#             result += '                              <td class="xl-khaki font-weight-bold" data-tipo="total">BDRs</td>'
#             result += ''.join(['                     <td data-tipo="total">' + ('R$ ' + decimal_to_str(valor=float(row_mes['TOTALBDR'])) if row_mes['TOTALBDR'] and float(row_mes['TOTALBDR']) > 0.0 else '') + '</td>' for row_mes in lista_princ_meses])
#             result += '                          </tr>'
#             result += '                          <tr>'
#             result += '                              <td class="xl-khaki font-weight-bold" data-tipo="total">CRIPTOs</td>'
#             result += ''.join(['                     <td data-tipo="total">' + ('R$ ' + decimal_to_str(valor=float(row_mes['TOTALCRIPTO'])) if row_mes['TOTALCRIPTO'] and float(row_mes['TOTALCRIPTO']) > 0.0 else '') + '</td>'for row_mes in lista_princ_meses])
#             result += '                          </tr>'
#             result += '                          <tr>'
#             result += '                              <td class="xl-khaki font-weight-bold" data-tipo="total">PORTFÓLIO</td>'
#             result += ''.join(['                     <td data-tipo="total">' + ('R$ ' + decimal_to_str(valor=float(row_mes['TOTALPORTFOLIO'])) if row_mes['TOTALPORTFOLIO'] and float(row_mes['TOTALPORTFOLIO']) > 0.0 else '') + '</td>' for row_mes in lista_princ_meses])
#             result += '                          </tr>'
#             result += '                          <tr>'
#             result += '                              <th colspan="14" data-tipo="default"></th>'
#             result += '                          </tr>'
#
#             result += '                          </tbody>'
#             result += '                          <tfoot class="table-info">'
#             result += '                          <tr>'
#             result += '                              <th scope="col">ATIVO</th>'
#             result += '                              <th scope="col">TIPO</th>'
#             result += ''.join(['                     <th scope="col">' + buscar_nome_mes_resumido(int(mes)) + '</th>' for mes in range(1, 13)])
#             result += '                          </tr>'
#             result += '                          </tfoot>'
#             result += '                      </table>'
#             result += '                  </div>'
#             result += '                  <!-- Div Table Responsive -->'
#             result += '                  <br/>'
#
#             result += '               </div>'
#             result += '               <!-- Div Card Body -->'
#             result += '             </div>'
#             result += '          </div>'
#             result += '          <!-- Div Card Accordion Ano -->'
#
#         result += '</div>'
#         result += '<!-- Div Row Accordion -->'
#
#         return make_response(result, 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(LogErro.descricao_erro(texto=str(e)), 200)
#
#
# @bp_analise.route('/carregarProjecao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_projecao():
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
#             id_projecao = data.get('IdProjecao')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not id_projecao:
#             return make_response(get_json_retorno_grid(msg='Id. Projeção Inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         projecao = UsuarioCarteiraProjecao.get_by_id_and_usuario(id_usuario=id_usuario, id=int(id_projecao))
#
#         if not projecao:
#             return make_response(get_json_retorno_grid(msg='Projeção não localizada.'), 200)
#
#         itens = UsuarioCarteiraProjecaoItem.buscar_todos(id_usuario=id_usuario, id_projecao=int(id_projecao))
#
#         lista = [
#             {
#                 "NroMes": str(item['NUMERO']),
#                 "AnoAtual": str(item['ANO']),
#                 "MesAtual": str(item['MES']),
#                 "VlrInvestIni": decimal_to_str(valor=float(item['VLRINVESTINI'])),
#                 "VlrInvestMensal": decimal_to_str(valor=float(item['VLRINVESTMES'])),
#                 "VlrInvestFim": decimal_to_str(valor=float(item['VLRINVESTFIM'])),
#                 "TaxaMensal": decimal_to_str(valor=float(item['RENDMENSAL'])),
#                 "Tipo": str(item['TIPO'])
#             }
#             for item in itens
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/salvarProjecao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_projecao():
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
#             descricao = data.get('Descricao')
#             ano_inicio = data.get('AnoInicio')
#             mes_inicio = data.get('MesInicio')
#             qtd_meses = data.get('QtdMeses')
#             vlr_invest_inicio = data.get('VlrInvestInicio')
#             vlr_invest_mensal = data.get('VlrInvestMensal')
#             tx_rend_mensal = data.get('TxRendMensal')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not descricao: return make_response(get_json_retorno_dados(msg='Descrição da Projeção não informada.'), 200)
#         if not ano_inicio: return make_response(get_json_retorno_dados(msg='Ano Início da Projeção não informado.'), 200)
#         if not mes_inicio: return make_response(get_json_retorno_dados(msg='Mês Início da Projeção não informado.'), 200)
#         if not qtd_meses: return make_response(get_json_retorno_dados(msg='Quantidade de Mese da Projeção não informada.'), 200)
#         if not vlr_invest_inicio and not vlr_invest_mensal: return make_response(get_json_retorno_dados(msg='Valor Inicial/Valor Mensal da Projeção não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         if UsuarioCarteiraProjecao.buscar_por_descricao(id_usuario=id_usuario, descricao=descricao):
#             return make_response(get_json_retorno_dados(msg='Descrição da Projeção já Cadastrada.'), 200)
#
#         ano_inicio = int(ano_inicio)
#         mes_inicio = int(mes_inicio)
#         qtd_meses = int(qtd_meses)
#         vlr_invest_inicio = float(vlr_invest_inicio) if vlr_invest_inicio else 0.0
#         vlr_invest_mensal = float(vlr_invest_mensal) if vlr_invest_mensal else 0.0
#         tx_rend_mensal = float(tx_rend_mensal) if tx_rend_mensal else 0.0
#
#         proj = UsuarioCarteiraProjecao()
#         proj.id_usuario = id_usuario
#         proj.descricao = descricao
#         proj.situacao = 'A'  # A-Ativo
#         proj.salvar()
#
#         ano_atual = ano_inicio
#         mes_atual = mes_inicio
#         vlr_invest_final = float(vlr_invest_inicio)
#
#         for numero in range(1, int(qtd_meses) + 1):
#             vlr_invest_final += float(vlr_invest_mensal)
#             if tx_rend_mensal > 0.0: vlr_invest_final += (vlr_invest_final * tx_rend_mensal) / 100
#
#             item = UsuarioCarteiraProjecaoItem()
#             item.id_projecao = int(proj.id)
#             item.numero = int(numero)
#             item.ano = int(ano_atual)
#             item.mes = int(mes_atual)
#             item.vlr_invest_ini = float(vlr_invest_inicio)
#             item.vlr_invest_mes = float(vlr_invest_mensal)
#             item.vlr_invest_fim = float(vlr_invest_final)
#             item.rend_messal = float(tx_rend_mensal)
#             item.tipo = 'C'  # C-Calculado
#             item.situacao = 'A'  # A-Ativo
#             item.salvar()
#
#             mes_atual += 1
#             if mes_atual > 12:
#                 mes_atual = 1
#                 ano_atual += 1
#
#         dados = dict({"Id": str(proj.id)})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/alterarProjecao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def alterar_projecao():
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
#             id_projecao = data.get('IdProjecao')
#             lista = data.to_dict()
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_projecao: return make_response(get_json_retorno_metodo(msg='Id. Projeção Inválido.'), 200)
#         if not lista: return make_response(get_json_retorno_metodo(msg='Lista da Projeção Inválida.'), 200)
#
#         id_usuario = current_user.id
#
#         proj = UsuarioCarteiraProjecao.get_by_id_and_usuario(id_usuario=id_usuario, id=int(id_projecao))
#         if not proj:
#             return make_response(get_json_retorno_metodo(msg='Projeção não localizada.'), 200)
#
#         UsuarioCarteiraProjecaoItem.excluir_carteira_projecao(id_usuario=id_usuario, id_projecao=int(id_projecao))
#
#         idx = -1
#         while True:
#
#             try:
#                 idx += 1
#                 numero = lista['DadosProjecao['+str(idx)+'][NroMes]']
#                 ano = lista['DadosProjecao['+str(idx)+'][AnoAtual]']
#                 mes = lista['DadosProjecao['+str(idx)+'][MesAtual]']
#                 vlr_invest_ini = lista['DadosProjecao['+str(idx)+'][VlrInvestIni]']
#                 vlr_invest_mes = lista['DadosProjecao['+str(idx)+'][VlrInvestMensal]']
#                 vlr_invest_fim = lista['DadosProjecao['+str(idx)+'][VlrInvestFim]']
#                 rend_messal = lista['DadosProjecao['+str(idx)+'][TaxaMensal]']
#                 tipo = lista['DadosProjecao['+str(idx)+'][Tipo]']
#             except:
#                 break
#
#             item = UsuarioCarteiraProjecaoItem()
#             item.id_projecao = int(id_projecao)
#             item.numero = int(numero) if numero else 0
#             item.ano = int(ano) if ano else 0
#             item.mes = int(mes) if mes else 0
#             item.vlr_invest_ini = float(vlr_invest_ini) if vlr_invest_ini else 0.0
#             item.vlr_invest_mes = float(vlr_invest_mes) if vlr_invest_mes else 0.0
#             item.vlr_invest_fim = float(vlr_invest_fim) if vlr_invest_fim else 0.0
#             item.rend_messal = float(rend_messal) if rend_messal else 0.0
#             item.tipo = 'M' if tipo and str(tipo) == 'M' else 'C'  # C-Calculado # M-Modificado
#             item.situacao = 'A'  # A-Ativo
#             item.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_analise.route('/excluirProjecao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir_projecao():
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
#             id_projecao = data.get('IdProjecao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_projecao:
#             return make_response(get_json_retorno_metodo(msg='Id. Projeção Inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         projecao = UsuarioCarteiraProjecao.get_by_id_and_usuario(id_usuario=id_usuario, id=int(id_projecao))
#
#         if not projecao:
#             return make_response(get_json_retorno_metodo(msg='Projeção não localizada.'), 200)
#
#         UsuarioCarteiraProjecaoItem.excluir_carteira_projecao(id_usuario=id_usuario, id_projecao=int(id_projecao))
#         projecao.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
