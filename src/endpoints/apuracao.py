# -*- coding: utf-8 -*-
import sys
import os
import datetime as dt
import time
import asyncio
# from threading import Thread
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.usuario_config import UsuarioConfig
# from app.models.usuario_carteira import UsuarioCarteira
# from app.models.usuario_apuracao import UsuarioApuracao
# from app.models.usuario_apuracao_calculada import UsuarioApuracaoCalculada
# from app.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamento
# from app.models.usuario_fii_fundoimob_lancamento import UsuarioFiiFundoImobLancamento
# from app.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamento
# from app.models.usuario_bdr_empresa_lancamento import UsuarioBDREmpresaLancamento
# from app.models.usuario_acao_empresa_operacao import UsuarioACAOEmpresaOperacao
# from app.models.usuario_etf_indice_operacao import UsuarioETFIndiceOperacao
# from app.models.usuario_bdr_empresa_operacao import UsuarioBDREmpresaOperacao
# from app.models.usuario_cripto_lancamento import UsuarioCriptoLancamento
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid, get_json_retorno_lista
# from app.util.util_formatacao import decimal_to_str, decimal_cripto_to_str, inteiro_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str, pegar_data_atual


router = _fastapi.APIRouter(prefix="/apuracao", tags=['apuracao'])


# @bp_apuracao.route('/')
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
#     return render_template(template_name_or_list="apuracao.html", gerar_portoflio=gerar_portoflio)
#
#
# @bp_apuracao.route('/listaAno', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_ano():
#     try:
#
#         id_usuario = current_user.id
#
#         anos = []
#
#         try:
#
#             anos.append(pegar_data_atual(fmt='%Y')+'0101')
#             anos.append(UsuarioApuracao.get_menor_ano(id_usuario=id_usuario)[0])
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
#         if not menor or not maior:
#             return make_response(get_json_retorno_lista(rslt='OK'), 200)
#
#         lista = [str(ano) for ano in range(menor, maior+1)]
#
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/config', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def config():
#     try:
#
#         id_usuario = current_user.id
#
#         config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo='APURACAO_COMPENSAR_PREJUIZO')
#
#         if not config:
#             config = UsuarioConfig(id_usuario=id_usuario, tipo='APURACAO_COMPENSAR_PREJUIZO', valor='S')  # S - Sim
#             config.salvar()
#             UsuarioApuracaoCalculada.excluir_tudo(id_usuario=id_usuario)
#
#         dados = dict({"Valor": config.valor})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/salvarconfig', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_config():
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
#             calc_vlr_superior = data.get('CalcVlrSuperior')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not calc_vlr_superior: calc_vlr_superior = "S"
#
#         id_usuario = current_user.id
#
#         config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo='APURACAO_COMPENSAR_PREJUIZO')
#         if not config: config = UsuarioConfig()
#
#         config.id_usuario = id_usuario
#         config.tipo = 'APURACAO_COMPENSAR_PREJUIZO'
#         config.valor = calc_vlr_superior
#         config.salvar()
#
#         UsuarioApuracaoCalculada.excluir_tudo(id_usuario=id_usuario)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         data = None
#         tipo_requisicao = ''
#
#         if request.method == 'POST':
#             data = request.form
#             tipo_requisicao = 'WEB'
#             if not data: data = request.get_json(silent=True)
#         elif request.method == 'GET':
#             data = request.args
#             tipo_requisicao = 'APP'
#             if not data: data = request.get_json(silent=True)
#
#         if not data: return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         try:
#             ano_apuracao = data.get('AnoApuracao')
#             tp_apuracao = data.get('TpApuracao')
#             calc_vlr_superior = data.get('CalcVlrSuperior')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not tp_apuracao: return make_response(get_json_retorno_grid(msg='Tipo de Apuração não informado.'), 200)
#
#         tp_apuracao = str(tp_apuracao).upper()
#
#         id_usuario = current_user.id
#
#         UsuarioApuracaoCalculada.gerar(id_usuario=id_usuario, tp_apuracao=tp_apuracao, calc_vlr_superior=calc_vlr_superior)
#
#         ano_mes_ini = str(ano_apuracao) + '01' if ano_apuracao else None
#         ano_mes_fim = str(ano_apuracao) + '12' if ano_apuracao else None
#
#         rows = UsuarioApuracaoCalculada.get_all(id_usuario=id_usuario, categoria=tp_apuracao, ano_mes_ini=ano_mes_ini, ano_mes_fim=ano_mes_fim)
#
#         lista = []
#         if not tipo_requisicao or (tipo_requisicao and str(tipo_requisicao) == 'WEB'):
#             lista = [[row.ano_mes_format(fmt='%m/%Y'), row.vlr_venda_format(), row.vlr_lucro_apurado_format(), row.vlr_prejuizo_compensar_format(), row.vlr_base_calculo_format(), row.vlr_ir_pagar_format(), row.vlr_ir_pago_format(), row.vlr_ir_devido_format()] for row in rows]
#         elif tipo_requisicao and str(tipo_requisicao) == 'APP':
#             lista = [[row.ano_mes_format(fmt='%m/%Y'), row.vlr_venda_format(), row.vlr_lucro_apurado_format(), row.vlr_prejuizo_compensar_format(), row.vlr_base_calculo_format(), row.vlr_ir_devido_format()] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridResumida', methods=['GET', 'POST'])
# @bp_apuracao.route('/gridresumida', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida():
#     try:
#
#         data = None
#         tipo_requisicao = ''
#
#         if request.method == 'POST':
#             tipo_requisicao = 'WEB'
#             data = request.form
#             if not data: data = request.get_json(silent=True)
#         elif request.method == 'GET':
#             tipo_requisicao = 'APP'
#             data = request.args
#             if not data: data = request.get_json(silent=True)
#
#         if not data: return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         try:
#             tp_apuracao = data.get('TpApuracao')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         lista = get_lista_resumida(tp_apuracao=tp_apuracao, tipo_requisicao=tipo_requisicao)
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridresumidaportipo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida_por_tipo():
#     try:
#
#
#         # lista_acao_c = get_lista_resumida(tp_apuracao='C') # C - ACAO Comum
#         # lista_acao_d = get_lista_resumida(tp_apuracao='D')  # D - ACAO DayTrade
#         # lista_fii = get_lista_resumida(tp_apuracao='F')  # F - FII
#         # lista_etf_c = get_lista_resumida(tp_apuracao='E')  # E - ETF Comum
#         # lista_etf_d = get_lista_resumida(tp_apuracao='G')  # G - ETF DayTrade
#         # lista_bdr_c = get_lista_resumida(tp_apuracao='I')  # I - BDR Comum
#         # lista_bdr_d = get_lista_resumida(tp_apuracao='J')  # J - BDR Day Trade
#         # lista_cripto = get_lista_resumida(tp_apuracao='K')  # K - CRIPTO
#
#         loop = asyncio.new_event_loop()  # get_event_loop
#         try:
#             asyncio.set_event_loop(loop)
#
#             tasks = [asyncio.Task(get_lista_resumida_async(tp_apuracao='C')),  # C - ACAO Comum
#                      asyncio.Task(get_lista_resumida_async(tp_apuracao='D')),  # D - ACAO DayTrade
#                      asyncio.Task(get_lista_resumida_async(tp_apuracao='F')),  # F - FII
#                      asyncio.Task(get_lista_resumida_async(tp_apuracao='E')),  # E - ETF Comum
#                      asyncio.Task(get_lista_resumida_async(tp_apuracao='G')),  # G - ETF DayTrade
#                      asyncio.Task(get_lista_resumida_async(tp_apuracao='I')),  # I - BDR Comum
#                      asyncio.Task(get_lista_resumida_async(tp_apuracao='J')),  # J - BDR Day Trade
#                      asyncio.Task(get_lista_resumida_async(tp_apuracao='K')),  # K - CRIPTO
#                      ]
#
#             results = loop.run_until_complete(asyncio.gather(*tasks))
#
#             lista_acao_c = results[0] # tasks[0].result()  # C - ACAO Comum
#             lista_acao_d = results[1] # tasks[1].result()  # D - ACAO DayTrade
#             lista_fii = results[2] # tasks[2].result()  # F - FII
#             lista_etf_c = results[3] # tasks[3].result()  # E - ETF Comum
#             lista_etf_d = results[4] # tasks[4].result()  # G - ETF DayTrade
#             lista_bdr_c = results[5] # tasks[5].result()  # I - BDR Comum
#             lista_bdr_d = results[6] # tasks[6].result()  # J - BDR Day Trade
#             lista_cripto = results[7] # tasks[7].result()  # K - CRIPTO
#
#         finally:
#             try:
#                 loop.close()
#             except:
#                 pass
#
#         dados = dict({"lista_acao_c": lista_acao_c, "lista_acao_d": lista_acao_d, "lista_fii": lista_fii, "lista_etf_c": lista_etf_c, "lista_etf_d": lista_etf_d, "lista_bdr_c": lista_bdr_c, "lista_bdr_d": lista_bdr_d, "lista_cripto": lista_cripto})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridResumidaAcaoComum', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida_acao_comum():
#     try:
#         lista = get_lista_resumida(tp_apuracao='C')  # C - ACAO Comum
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridResumidaAcaoDayTrade', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida_acao_daytrade():
#     try:
#         lista = get_lista_resumida(tp_apuracao='D') # D - ACAO DayTrade
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridResumidaFii', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida_fii():
#     try:
#         lista = get_lista_resumida(tp_apuracao='F') # F - FII
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridResumidaEtfComum', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida_etf_comum():
#     try:
#         lista = get_lista_resumida(tp_apuracao='E') # E - ETF Comum
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridResumidaEtfDayTrade', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida_etf_daytrade():
#     try:
#         lista = get_lista_resumida(tp_apuracao='G') # G - ETF DayTrade
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridResumidaBdrComum', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida_bdr_comum():
#     try:
#         lista = get_lista_resumida(tp_apuracao='I') # I - BDR Comum
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridResumidaBdrDayTrade', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida_bdr_daytrade():
#     try:
#         lista = get_lista_resumida(tp_apuracao='J')  # J - BDR Day Trade
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridResumidaCripto', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_resumida_cripto():
#     try:
#         lista = get_lista_resumida(tp_apuracao='K') # K - CRIPTO
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
# @asyncio.coroutine
# async def get_lista_resumida_async(tp_apuracao: str = None, tipo_requisicao: str = 'WEB') -> []:
#     return get_lista_resumida(tp_apuracao=tp_apuracao, tipo_requisicao=tipo_requisicao)
#
# def get_lista_resumida(tp_apuracao: str = None, tipo_requisicao: str = 'WEB') -> []:
#     try:
#
#         dt_atual = pegar_data_atual(istext=False)
#         ano_atual = converter_datetime_str(data=dt_atual, fmt='%Y')
#         mes_atual = converter_datetime_str(data=dt_atual, fmt='%m')
#         ano_mes_ini = str(ano_atual) + str(int(mes_atual)-1).zfill(2)
#         ano_mes_fim = str(ano_atual) + str(mes_atual).zfill(2)
#         if int(mes_atual) == 1: ano_mes_ini = str(int(ano_atual)-1) + '12'
#
#         retorno_default = [
#             [ano_mes_ini[4:6] + '/' + ano_mes_ini[0:4], "0,00", "0,00", "0,00", "0,00", "0,00", "0,00", "0,00"],
#             [ano_mes_fim[4:6] + '/' + ano_mes_fim[0:4], "0,00", "0,00", "0,00", "0,00", "0,00", "0,00", "0,00"]
#         ]
#
#         if not tp_apuracao:
#             return retorno_default
#
#         id_usuario = current_user.id
#
#         # UsuarioApuracaoCalculada.gerar(id_usuario=id_usuario, tp_apuracao=tp_apuracao)
#
#         if tp_apuracao == "C" and UsuarioACAOEmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, tipo='V') == 0: return retorno_default  # Acao Comum
#         elif tp_apuracao == "D" and UsuarioACAOEmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, tipo='V') == 0: return retorno_default  # Acao DayTrade
#         elif tp_apuracao == "F" and UsuarioFiiFundoImobLancamento.buscar_quant_operacao(id_usuario=id_usuario, tipo='V') == 0: return retorno_default  # FII
#         elif tp_apuracao == "E" and UsuarioETFIndiceLancamento.buscar_quant_operacao(id_usuario=id_usuario, tipo='V') == 0: return retorno_default  # ETF Comum
#         elif tp_apuracao == "G" and UsuarioETFIndiceLancamento.buscar_quant_operacao(id_usuario=id_usuario, tipo='V') == 0: return retorno_default  # ETF DayTrade
#         elif tp_apuracao == "I" and UsuarioBDREmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, tipo='V') == 0: return retorno_default  # BDR Comum
#         elif tp_apuracao == "J" and UsuarioBDREmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, tipo='V') == 0: return retorno_default  # BDR DayTrade
#         elif tp_apuracao == "K" and UsuarioCriptoLancamento.buscar_quant_operacao(id_usuario=id_usuario, tipo='V') == 0: return retorno_default  # Cripto
#
#         rows = UsuarioApuracaoCalculada.get_all(id_usuario=id_usuario, categoria=tp_apuracao, ano_mes_ini=ano_mes_ini, ano_mes_fim=ano_mes_fim)
#         if not rows:
#             time.sleep(1)
#             rows = UsuarioApuracaoCalculada.get_all(id_usuario=id_usuario, categoria=tp_apuracao, ano_mes_ini=ano_mes_ini, ano_mes_fim=ano_mes_fim)
#             if not rows:
#                 time.sleep(2)
#                 rows = UsuarioApuracaoCalculada.get_all(id_usuario=id_usuario, categoria=tp_apuracao, ano_mes_ini=ano_mes_ini, ano_mes_fim=ano_mes_fim)
#                 if not rows:
#                     time.sleep(3)
#                     rows = UsuarioApuracaoCalculada.get_all(id_usuario=id_usuario, categoria=tp_apuracao, ano_mes_ini=ano_mes_ini, ano_mes_fim=ano_mes_fim)
#                     if not rows:
#                         time.sleep(5)
#                         rows = UsuarioApuracaoCalculada.get_all(id_usuario=id_usuario, categoria=tp_apuracao, ano_mes_ini=ano_mes_ini, ano_mes_fim=ano_mes_fim)
#
#         lista = []
#         if not tipo_requisicao or (tipo_requisicao and str(tipo_requisicao) == 'WEB'):
#             lista = [[row.ano_mes_format(fmt='%m/%Y'), row.vlr_venda_format(), row.vlr_lucro_apurado_format(), row.vlr_prejuizo_compensar_format(), row.vlr_base_calculo_format(), row.vlr_ir_pagar_format(), row.vlr_ir_pago_format(), row.vlr_ir_devido_format()] for row in rows]
#         elif tipo_requisicao and str(tipo_requisicao) == 'APP':
#             lista = [[row.ano_mes_format(fmt='%m/%Y'), row.vlr_venda_format(), row.vlr_lucro_apurado_format(), row.vlr_prejuizo_compensar_format(), row.vlr_base_calculo_format(), row.vlr_ir_devido_format()] for row in rows]
#
#         if not lista or len(lista) == 0:
#             lista = retorno_default
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return []
#
#
# @bp_apuracao.route('/carregar', methods=['GET', 'POST'])
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
#             ano = data.get('Ano')
#             categoria = data.get('Categoria')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not ano: return make_response(get_json_retorno_dados(msg='Ano não informado.'), 200)
#         if not categoria: return make_response(get_json_retorno_dados(msg='Tipo não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'01')
#         vlr_jan = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'02')
#         vlr_fev = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'03')
#         vlr_mar = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'04')
#         vlr_abr = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'05')
#         vlr_mai = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'06')
#         vlr_jun = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'07')
#         vlr_jul = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'08')
#         vlr_ago = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'09')
#         vlr_set = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'10')
#         vlr_out = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'11')
#         vlr_nov = apurac[0].valor if apurac else 0.0
#
#         apurac = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'12')
#         vlr_dez = apurac[0].valor if apurac else 0.0
#
#         dados = dict(
#             {
#                 "JAN": decimal_to_str(valor=vlr_jan),
#                 "FEV": decimal_to_str(valor=vlr_fev),
#                 "MAR": decimal_to_str(valor=vlr_mar),
#                 "ABR": decimal_to_str(valor=vlr_abr),
#                 "MAI": decimal_to_str(valor=vlr_mai),
#                 "JUN": decimal_to_str(valor=vlr_jun),
#                 "JUL": decimal_to_str(valor=vlr_jul),
#                 "AGO": decimal_to_str(valor=vlr_ago),
#                 "SET": decimal_to_str(valor=vlr_set),
#                 "OUT": decimal_to_str(valor=vlr_out),
#                 "NOV": decimal_to_str(valor=vlr_nov),
#                 "DEZ": decimal_to_str(valor=vlr_dez),
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
# @bp_apuracao.route('/salvar', methods=['GET', 'POST'])
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
#             ano = data.get('Ano')
#             categoria = data.get('Categoria')
#             vlr_jan = data.get('VlrJAN')
#             vlr_fev = data.get('VlrFEV')
#             vlr_mar = data.get('VlrMAR')
#             vlr_abr = data.get('VlrABR')
#             vlr_mai = data.get('VlrMAI')
#             vlr_jun = data.get('VlrJUN')
#             vlr_jul = data.get('VlrJUL')
#             vlr_ago = data.get('VlrAGO')
#             vlr_set = data.get('VlrSET')
#             vlr_out = data.get('VlrOUT')
#             vlr_nov = data.get('VlrNOV')
#             vlr_dez = data.get('VlrDEZ')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not ano:
#             return make_response(get_json_retorno_metodo(msg='Ano não informado.'), 200)
#
#         if not categoria:
#             return make_response(get_json_retorno_metodo(msg='Tipo não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         UsuarioApuracao.excluir_ano(id_usuario=id_usuario, tipo='M', categoria=categoria, ano=ano)
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'01', valor=vlr_jan if vlr_jan else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'02', valor=vlr_fev if vlr_fev else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'03', valor=vlr_mar if vlr_mar else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'04', valor=vlr_abr if vlr_abr else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'05', valor=vlr_mai if vlr_mai else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'06', valor=vlr_jun if vlr_jun else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'07', valor=vlr_jul if vlr_jul else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'08', valor=vlr_ago if vlr_ago else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'09', valor=vlr_set if vlr_set else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'10', valor=vlr_out if vlr_out else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'11', valor=vlr_nov if vlr_nov else 0.0, situacao='A').salvar()
#         UsuarioApuracao(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano+'12', valor=vlr_dez if vlr_dez else 0.0, situacao='A').salvar()
#
#         UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria=categoria)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_apuracao.route('/gridVendas', methods=['GET', 'POST'])
# @bp_apuracao.route('/gridvendas', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_vendas():
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
#             categoria = data.get('TpApuracao')
#             ano_mes = data.get('AnoMesApuracao')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not categoria: return make_response(get_json_retorno_grid(msg='Tipo de Apuração não informado.'), 200)
#         if not ano_mes: return make_response(get_json_retorno_grid(msg='Ano/Mês da Apuração não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         rows = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=categoria, ano_mes=ano_mes)
#         lista += [[apurac.data_format(), 'AJUSTE', '1.0', apurac.valor_format(), apurac.valor_format(), apurac.valor_format(), apurac.valor_format(), '100.0'] for apurac in rows]
#
#         # ACAO C-Comum e D-DayTrade
#         if categoria == 'C' or categoria == 'D':
#             opers = UsuarioACAOEmpresaOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes + "01", dt_fim=ano_mes + "31", categoria=categoria, tipo="V", troca="N")
#             for oper in opers:
#                 vlr_valorizacao = UsuarioACAOEmpresaOperacao.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                 perc_valorizacao = UsuarioACAOEmpresaOperacao.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 lista.append([
#                          converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'), fmt='%d/%m/%Y'),
#                          oper['CODIGOATIVO'],
#                          inteiro_to_str(valor=oper['QUANT']),
#                          decimal_to_str(valor=oper['VLRCUSTO']),
#                          decimal_to_str(valor=oper['VLRPRECOMEDIO']),
#                          decimal_to_str(valor=oper['TOTVLRCUSTO']),
#                          decimal_to_str(valor=float(vlr_valorizacao)),
#                          decimal_to_str(valor=float(perc_valorizacao))
#                      ])
#
#         # FII
#         if categoria == 'F':
#             opers = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes+"01", dt_fim=ano_mes+"31", tipo="V", troca="N")
#             for oper in opers:
#                 vlr_valorizacao = UsuarioFiiFundoImobLancamento.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                 perc_valorizacao = UsuarioFiiFundoImobLancamento.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 lista.append([
#                          converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'), fmt='%d/%m/%Y'),
#                          oper['CODIGOFUNDO'],
#                          inteiro_to_str(valor=oper['QUANT']),
#                          decimal_to_str(valor=oper['VLRCUSTO']),
#                          decimal_to_str(valor=oper['VLRPRECOMEDIO']),
#                          decimal_to_str(valor=oper['TOTVLRCUSTO']),
#                          decimal_to_str(valor=float(vlr_valorizacao)),
#                          decimal_to_str(valor=float(perc_valorizacao))
#                      ])
#
#         # ETF E-Comum e G-DayTrade
#         if categoria == 'E' or categoria == 'G':
#             if categoria == "E": opers = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes + "01", dt_fim=ano_mes + "31", categoria='C', tipo="V", troca="N")
#             if categoria == "G": opers = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes + "01", dt_fim=ano_mes + "31", categoria='D', tipo="V", troca="N")
#             for oper in opers:
#                 vlr_valorizacao = UsuarioETFIndiceOperacao.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                 perc_valorizacao = UsuarioETFIndiceOperacao.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 lista.append([
#                          converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'), fmt='%d/%m/%Y'),
#                          oper['CODIGOINDICE'],
#                          inteiro_to_str(valor=oper['QUANT']),
#                          decimal_to_str(valor=oper['VLRCUSTO']),
#                          decimal_to_str(valor=oper['VLRPRECOMEDIO']),
#                          decimal_to_str(valor=oper['TOTVLRCUSTO']),
#                          decimal_to_str(valor=float(vlr_valorizacao)),
#                          decimal_to_str(valor=float(perc_valorizacao))
#                      ])
#
#         # BDR I-Comum e J-DayTrade
#         if categoria == 'I' or categoria == 'J':
#             if categoria == "I": opers = UsuarioBDREmpresaOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes + "01", dt_fim=ano_mes + "31", categoria='C', tipo="V", troca="N")
#             if categoria == "J": opers = UsuarioBDREmpresaOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes + "01", dt_fim=ano_mes + "31", categoria='D', tipo="V", troca="N")
#             for oper in opers:
#                 vlr_valorizacao = UsuarioBDREmpresaOperacao.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                 perc_valorizacao = UsuarioBDREmpresaOperacao.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 lista.append([
#                          converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'), fmt='%d/%m/%Y'),
#                          oper['CODIGOBDR'],
#                          inteiro_to_str(valor=oper['QUANT']),
#                          decimal_to_str(valor=oper['VLRCUSTO']),
#                          decimal_to_str(valor=oper['VLRPRECOMEDIO']),
#                          decimal_to_str(valor=oper['TOTVLRCUSTO']),
#                          decimal_to_str(valor=float(vlr_valorizacao)),
#                          decimal_to_str(valor=float(perc_valorizacao))
#                      ])
#
#         # CRIPTO
#         if categoria == 'K':
#             opers = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes+"01", dt_fim=ano_mes+"31", tipo="V")
#             for oper in opers:
#                 vlr_valorizacao = UsuarioCriptoLancamento.calcular_vlr_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_custo=float(oper['TOTVLRCUSTO']))
#                 perc_valorizacao = UsuarioCriptoLancamento.calcular_perc_valorizacao(tipo=oper['TIPO'], quant=float(oper['QUANT']), vlr_preco_medio=float(oper['VLRPRECOMEDIO']), tot_vlr_valorizacao=float(vlr_valorizacao))
#                 lista.append([
#                          converter_datetime_str(data=converter_str_to_datetime(data=oper['DATA'], fmt='%Y%m%d'), fmt='%d/%m/%Y'),
#                          oper['CODIGOCRIPTO'],
#                          decimal_cripto_to_str(valor=float(oper['QUANT'])),
#                          decimal_cripto_to_str(valor=float(oper['VLRCUSTO'])),
#                          decimal_cripto_to_str(valor=float(oper['VLRPRECOMEDIO'])),
#                          decimal_to_str(valor=oper['TOTVLRCUSTO']),
#                          decimal_to_str(valor=float(vlr_valorizacao)),
#                          decimal_to_str(valor=float(perc_valorizacao))
#                      ])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
