# -*- coding: utf-8 -*-
import sys
import os
import time
import asyncio
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.alerta_noticia import AlertaNoticia
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.fii_fundoimob import FiiFundoImob
# from app.models.etf_indice import ETFIndice
# from app.models.bdr_empresa import BDREmpresa
# from app.models.cripto_empresa import CriptoEmpresa
# from app.models.acao_empresa_fato_relevante import ACAOEmpresaFatoRelevante
# from app.models.fii_fundoimob_fato_relevante import FiiFundoImobFatoRelevante
# from app.models.etf_indice_fato_relevante import ETFIndiceFatoRelevante
# from app.models.bdr_empresa_fato_relevante import BDREmpresaFatoRelevante
# from app.models.acao_empresa_provento import ACAOEmpresaProvento
# from app.models.acao_empresa_financeiro_agenda import ACAOEmpresaFinanceiroAgenda
# from app.models.fii_fundoimob_provento import FiiFundoImobProvento
# from app.models.bdr_empresa_provento import BDREmpresaProvento
# from app.models.usuario import Usuario
# from app.models.usuario_apuracao_calculada import UsuarioApuracaoCalculada
# from app.models.usuario_carteira import UsuarioCarteira
# from app.models.usuario_carteira_acao import UsuarioCarteiraAcao
# from app.models.usuario_carteira_fii import UsuarioCarteiraFii
# from app.models.usuario_carteira_etf import UsuarioCarteiraEtf
# from app.models.usuario_carteira_bdr import UsuarioCarteiraBdr
# from app.models.usuario_carteira_cripto import UsuarioCarteiraCripto
# from app.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamento
# from app.models.usuario_fii_fundoimob_lancamento import UsuarioFiiFundoImobLancamento
# from app.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamento
# from app.models.usuario_bdr_empresa_lancamento import UsuarioBDREmpresaLancamento
# from app.models.usuario_cripto_lancamento import UsuarioCriptoLancamento
# from app.models.usuario_acao_empresa_provento import UsuarioACAOEmpresaProvento
# from app.models.usuario_fii_fundoimob_provento import UsuarioFiiFundoImobProvento
# from app.models.usuario_bdr_empresa_provento import UsuarioBDREmpresaProvento
# from app.models.usuario_acao_empresa_provento_ativo import UsuarioACAOEmpresaProventoAtivo
# from app.models.usuario_fii_fundoimob_provento_ativo import UsuarioFiiFundoImobProventoAtivo
# from app.models.usuario_bdr_empresa_provento_ativo import UsuarioBDREmpresaProventoAtivo
# from app.models.usuario_acao_empresa_fato_relevante_ativo import UsuarioACAOEmpresaFatoRelevanteAtivo
# from app.models.usuario_fii_fundoimob_fato_relevante_ativo import UsuarioFiiFundoImobFatoRelevanteAtivo
# from app.models.usuario_etf_indice_fato_relevante_ativo import UsuarioETFIndiceFatoRelevanteAtivo
# from app.models.usuario_bdr_empresa_fato_relevante_ativo import UsuarioBDREmpresaFatoRelevanteAtivo
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_formatacao import decimal_to_str, decimal_prov_to_str, decimal_cripto_curto_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str, pegar_data_atual, adicionar_dias, adicionar_meses


router = _fastapi.APIRouter(prefix="/principal", tags=['principal'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @login_required
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index():
    # id_usuario = current_user.id
    # gerar_portoflio = False
    # if not gerar_portoflio and UsuarioACAOEmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioFiiFundoImobLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioETFIndiceLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioBDREmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioCriptoLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # UsuarioApuracaoCalculada.gerar_todos(id_usuario=id_usuario)
    # return render_template(template_name_or_list="principal.html", gerar_portoflio=gerar_portoflio)
    return {"result": "ok"}


# @bp_principal.route('/inicial')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# def inicial():
#     return render_template(template_name_or_list="principal.html")
#
#
# @bp_principal.route('/gerarportifolio', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def gerar_portifolio():
#     try:
#
#         id_usuario = current_user.id
#         UsuarioCarteira.gerar(id_usuario=id_usuario)
#         UsuarioApuracaoCalculada.excluir_tudo(id_usuario=id_usuario)
#         UsuarioApuracaoCalculada.gerar_todos(id_usuario=id_usuario)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar():
#     try:
#
#         # print(' ==> CARREGAR INI')
#         # start = time.time()
#
#         data_atual = pegar_data_atual()
#
#         QtdeInvest = 0
#         QtdeInvestAtivo = 0
#         QtdeInvestAguarde = 0
#         QtdeInvestCriado = 0
#         QtdeUserLogSite = 0
#         QtdeUserLogApp = 0
#         QtdeACAOOper = 0
#         QtdeFIIOper = 0
#         QtdeETFOper = 0
#         QtdeBDROper = 0
#         QtdeCRIPTOOper = 0
#         QtdeACAOProv = 0
#         QtdeFIIProv = 0
#         QtdeBDRProv = 0
#
#         @asyncio.coroutine
#         async def usuario_buscar_total_base(msg: None, situacao: str = ""):
#             result = await Usuario.buscar_total_base(situacao=situacao)
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_buscar_total_base_criado(msg: None, data_registro: str = ""):
#             result = await Usuario.buscar_total_base_criado(data_registro=data_registro)
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_buscar_total_base_logado(msg: None, data: str = "", situacao: str = ""):
#             result = await Usuario.buscar_total_base_logado(data=data, situacao=situacao)
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_acao_lanc_buscar_qtde_total_base(msg: None):
#             result = await UsuarioACAOEmpresaLancamento.buscar_qtde_total_base()
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_fii_lanc_buscar_qtde_total_base(msg: None):
#             result = await UsuarioFiiFundoImobLancamento.buscar_qtde_total_base()
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_etf_lanc_buscar_qtde_total_base(msg: None):
#             result = await UsuarioETFIndiceLancamento.buscar_qtde_total_base()
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_bdr_lanc_buscar_qtde_total_base(msg: None):
#             result = await UsuarioBDREmpresaLancamento.buscar_qtde_total_base()
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_cripto_lanc_buscar_qtde_total_base(msg: None):
#             result = await UsuarioCriptoLancamento.buscar_qtde_total_base()
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_acao_prov_buscar_qtde_total_base(msg: None):
#             result = await UsuarioACAOEmpresaProvento.buscar_qtde_total_base()
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_fii_prov_buscar_qtde_total_base(msg: None):
#             result = await UsuarioFiiFundoImobProvento.buscar_qtde_total_base()
#             if msg: msg.put(result)
#             return result
#
#         @asyncio.coroutine
#         async def usuario_bdr_prov_buscar_qtde_total_base(msg: None):
#             result = await UsuarioBDREmpresaProvento.buscar_qtde_total_base()
#             if msg: msg.put(result)
#             return result
#
#         # from queue import Queue
#         #from multiprocessing import Queue
#         #messages = Queue()
#         messages = None
#
#         loop = asyncio.new_event_loop()
#         try:
#             asyncio.set_event_loop(loop)
#             tasks = [asyncio.Task(usuario_buscar_total_base(messages, situacao="")),
#                      asyncio.Task(usuario_buscar_total_base(messages, situacao="A")),
#                      asyncio.Task(usuario_buscar_total_base(messages, situacao="B")),
#                      asyncio.Task(usuario_buscar_total_base_criado(messages, data_registro=str(data_atual))),
#                      asyncio.Task(usuario_buscar_total_base_logado(messages, data=str(data_atual), situacao='L')),
#                      asyncio.Task(usuario_buscar_total_base_logado(messages, data=str(data_atual), situacao='P')),
#                      asyncio.Task(usuario_acao_lanc_buscar_qtde_total_base(messages)),
#                      asyncio.Task(usuario_fii_lanc_buscar_qtde_total_base(messages)),
#                      asyncio.Task(usuario_etf_lanc_buscar_qtde_total_base(messages)),
#                      asyncio.Task(usuario_bdr_lanc_buscar_qtde_total_base(messages)),
#                      asyncio.Task(usuario_cripto_lanc_buscar_qtde_total_base(messages)),
#                      asyncio.Task(usuario_acao_prov_buscar_qtde_total_base(messages)),
#                      asyncio.Task(usuario_fii_prov_buscar_qtde_total_base(messages)),
#                      asyncio.Task(usuario_bdr_prov_buscar_qtde_total_base(messages)),
#                      ]
#             results = loop.run_until_complete(asyncio.gather(*tasks))
#         finally:
#             loop.close()
#
#         # import multiprocessing
#         #
#         # q = multiprocessing.Queue()
#         #
#         # threads = []
#         #
#         # thread = multiprocessing.Process(target=usuario_buscar_total_base, args=(q, ''))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # for thread in threads:
#         #     thread.join()
#         #
#         # while q.empty() is False:
#         #     print('messages', q.get())
#
#         # import threading
#         #
#         # threads = []
#         #
#         # thread = threading.Thread(target=usuario_buscar_total_base, args=(messages, ''))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_buscar_total_base, args=(messages, 'A'))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_buscar_total_base, args=(messages, 'B'))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_buscar_total_base_criado, args=(messages, data_atual))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_buscar_total_base_logado, args=(messages, data_atual, 'L'))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_buscar_total_base_logado, args=(messages, data_atual, 'P'))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_acao_lanc_buscar_qtde_total_base, args=(messages))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_fii_lanc_buscar_qtde_total_base, args=(messages))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_etf_lanc_buscar_qtde_total_base, args=(messages))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_bdr_lanc_buscar_qtde_total_base, args=(messages))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_cripto_lanc_buscar_qtde_total_base, args=(messages))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_acao_prov_buscar_qtde_total_base, args=(messages))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_fii_prov_buscar_qtde_total_base, args=(messages))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # thread = threading.Thread(target=usuario_bdr_prov_buscar_qtde_total_base, args=(messages))
#         # threads.append(thread)
#         # thread.start()
#         #
#         # results = []
#         # for thread in threads:
#         #     thread.join()
#         #     #results.append(messages.get())
#         #
#         # messages.task_done()
#         # while not messages.empty():
#         #     results.append(messages.get())
#
#         QtdeInvest = results[0]
#         QtdeInvestAtivo = results[1]
#         QtdeInvestAguarde = results[2]
#         QtdeInvestCriado = results[3]
#         QtdeUserLogSite = results[4]
#         QtdeUserLogApp = results[5]
#         QtdeACAOOper = results[6]
#         QtdeFIIOper = results[7]
#         QtdeETFOper = results[8]
#         QtdeBDROper = results[9]
#         QtdeCRIPTOOper = results[10]
#         QtdeACAOProv = results[11]
#         QtdeFIIProv = results[12]
#         QtdeBDRProv = results[13]
#
#         #  ==> CARREGAR FIM 595
#
#         dados = dict(
#             {
#                 "QtdeInvest": str(QtdeInvest),
#                 "QtdeInvestAtivo": str(QtdeInvestAtivo),
#                 "QtdeInvestAguarde": str(QtdeInvestAguarde),
#                 "QtdeInvestCriado": str(QtdeInvestCriado),
#                 "QtdeUserLogSite": str(QtdeUserLogSite),
#                 "QtdeUserLogApp": str(QtdeUserLogApp),
#                 "QtdeACAOOper": str(QtdeACAOOper),
#                 "QtdeFIIOper": str(QtdeFIIOper),
#                 "QtdeETFOper": str(QtdeETFOper),
#                 "QtdeBDROper": str(QtdeBDROper),
#                 "QtdeCRIPTOOper": str(QtdeCRIPTOOper),
#                 "QtdeACAOProv": str(QtdeACAOProv),
#                 "QtdeFIIProv": str(QtdeFIIProv),
#                 "QtdeBDRProv": str(QtdeBDRProv),
#             }
#         )
#
#         # diff = int((time.time() - start) * 1000)
#         # print(' ==> CARREGAR FIM', diff)
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarCarteira', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_carteira():
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
#             tipo_invest = data.get('TipoInvest')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         id_usuario = current_user.id
#
#         data_atual = pegar_data_atual()
#         tot_investido = 0.0
#         tot_atual = 0.0
#         vlr_proventos = 0.0
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             rows = UsuarioCarteiraAcao.buscar_todos_simples(id_usuario=id_usuario, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_investido += (float(quant_tot) * float(preco_medio)) if quant > 0.0 and preco_medio > 0.0 else 0.0
#                 tot_atual += (quant_tot * vlr_preco_atual) if quant_tot > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_proventos += UsuarioACAOEmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_ativo=int(row['IDATIVO']), dt_fim=str(data_atual))
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             rows = UsuarioCarteiraFii.buscar_todos_simples(id_usuario=id_usuario, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 tot_investido += (float(quant_tot) * float(preco_medio)) if quant > 0.0 and preco_medio > 0.0 else 0.0
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_atual += (quant_tot * vlr_preco_atual) if quant_tot > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_proventos += UsuarioFiiFundoImobProvento.buscar_vlr_total(id_usuario=id_usuario, id_fundo=int(row['IDFUNDO']), dt_fim=str(data_atual))
#
#         if not tipo_invest or str(tipo_invest) == 'ETF':
#             rows = UsuarioCarteiraEtf.buscar_todos_simples(id_usuario=id_usuario, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 tot_investido += (float(quant_tot) * float(preco_medio)) if quant > 0.0 and preco_medio > 0.0 else 0.0
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_atual += (quant_tot * vlr_preco_atual) if quant_tot > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_proventos += 0.0
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             rows = UsuarioCarteiraBdr.buscar_todos_simples(id_usuario=id_usuario, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_investido += (float(quant_tot) * float(preco_medio)) if quant > 0.0 and preco_medio > 0.0 else 0.0
#                 tot_atual += (quant_tot * vlr_preco_atual) if quant_tot > 0.0 and vlr_preco_atual > 0.0 else 0.0
#                 vlr_proventos += UsuarioBDREmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_bdr=int(row['IDBDR']), dt_fim=str(data_atual))
#
#         if not tipo_invest or str(tipo_invest) == 'CRIPTO':
#             rows = UsuarioCarteiraCripto.buscar_todos_simples(id_usuario=id_usuario, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_tot = float(quant)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 tot_investido += (float(quant_tot) * float(preco_medio)) if quant > 0.0 and preco_medio > 0.0 else 0.0
#                 vlr_preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_atual += (quant_tot * vlr_preco_atual) if quant_tot > 0.0 and vlr_preco_atual > 0.0 else 0.0
#
#         tot_valorizacao = float(tot_atual) - float(tot_investido)
#         perc_valorizacao = 0.0
#         if tot_valorizacao != 0.0 and tot_investido > 0.00: perc_valorizacao = (float(tot_valorizacao) / float(tot_investido)) * 100
#         if tot_valorizacao != 0.0 and tot_investido == 0.00: perc_valorizacao = 100.0
#
#         dados = dict(
#             {
#                 "TotInvest": decimal_to_str(valor=float(tot_investido)),
#                 "TotAtual": decimal_to_str(valor=float(tot_atual)),
#                 "TotValoriz": decimal_to_str(valor=float(tot_valorizacao)),
#                 "PercValoriz": decimal_to_str(valor=float(perc_valorizacao)),
#                 "TotProv": decimal_to_str(valor=float(vlr_proventos))
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
# @bp_principal.route('/carregarOperacoes', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_operacoes():
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
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         lista = []
#         if not tipo_invest or str(tipo_invest) == 'ACAO': lista += get_lista_operacoes(tipo_invest='ACAO')
#         if not tipo_invest or str(tipo_invest) == 'FII': lista += get_lista_operacoes(tipo_invest='FII')
#         if not tipo_invest or str(tipo_invest) == 'ETF': lista += get_lista_operacoes(tipo_invest='ETF')
#         if not tipo_invest or str(tipo_invest) == 'BDR': lista += get_lista_operacoes(tipo_invest='BDR')
#         if not tipo_invest or str(tipo_invest) == 'CRIPTO': lista += get_lista_operacoes(tipo_invest='CRIPTO')
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregaroperacoesportipos', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_operacoes_por_tipo():
#     try:
#
#         loop = asyncio.new_event_loop()  # get_event_loop
#         try:
#             asyncio.set_event_loop(loop)
#
#             tasks = [asyncio.Task(get_lista_operacoes_async(tipo_invest='ACAO')),
#                      asyncio.Task(get_lista_operacoes_async(tipo_invest='FII')),
#                      asyncio.Task(get_lista_operacoes_async(tipo_invest='ETF')),
#                      asyncio.Task(get_lista_operacoes_async(tipo_invest='BDR')),
#                      asyncio.Task(get_lista_operacoes_async(tipo_invest='CRIPTO')),
#                     ]
#
#             results = loop.run_until_complete(asyncio.gather(*tasks))
#
#             lista_acao = results[0]
#             lista_fii = results[1]
#             lista_etf = results[2]
#             lista_bdr = results[3]
#             lista_cripto = results[4]
#
#         finally:
#             try:
#                 loop.close()
#             except:
#                 pass
#
#         dados = dict({"lista_acao": lista_acao, "lista_fii": lista_fii, "lista_etf": lista_etf, "lista_bdr": lista_bdr, "lista_cripto": lista_cripto})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarOperacoesAcoes', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_operacoes_acoes():
#     try:
#         lista = get_lista_operacoes(tipo_invest='ACAO')
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarOperacoesFiis', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_operacoes_fiis():
#     try:
#         lista = get_lista_operacoes(tipo_invest='FII')
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarOperacoesEtfs', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_operacoes_etfs():
#     try:
#         lista = get_lista_operacoes(tipo_invest='ETF')
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarOperacoesBdrs', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_operacoes_bdrs():
#     try:
#         lista = get_lista_operacoes(tipo_invest='BDR')
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarOperacoesCriptos', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_operacoes_criptos():
#     try:
#         lista = get_lista_operacoes(tipo_invest='CRIPTO')
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @asyncio.coroutine
# async def get_lista_operacoes_async(id_usuario: int = None, tipo_invest: str = None) -> []:
#     return get_lista_operacoes(id_usuario=id_usuario, tipo_invest=tipo_invest)
#
#
# def get_lista_operacoes(id_usuario: int = None, tipo_invest: str = None) -> []:
#     try:
#
#         if not id_usuario: id_usuario = current_user.id
#
#         lista = []
#         dt_ini = pegar_data_atual(fmt='%Y%m') + '01'
#
#         if str(tipo_invest) == 'ACAO':
#             rows = UsuarioACAOEmpresaLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=str(dt_ini))
#             lista = [[str(row["DATA"]), str(row["TIPO"]), str(row["CODIGOATIVO"]), float(row["QUANT"]), decimal_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         elif str(tipo_invest) == 'FII':
#             rows = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=str(dt_ini))
#             lista = [[str(row["DATA"]), str(row["TIPO"]), str(row["CODIGOFUNDO"]), float(row["QUANT"]), decimal_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         elif str(tipo_invest) == 'ETF':
#             rows = UsuarioETFIndiceLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=str(dt_ini))
#             lista = [[str(row["DATA"]), str(row["TIPO"]), str(row["CODIGOINDICE"]), float(row["QUANT"]), decimal_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         elif str(tipo_invest) == 'BDR':
#             rows = UsuarioBDREmpresaLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=str(dt_ini))
#             lista = [[str(row["DATA"]), str(row["TIPO"]), str(row["CODIGOBDR"]), float(row["QUANT"]), decimal_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         elif str(tipo_invest) == 'CRIPTO':
#             rows = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=str(dt_ini))
#             lista = [[str(row["DATA"]), str(row["TIPO"]), str(row["CODIGOCRIPTO"]), float(row["QUANT"]), decimal_cripto_curto_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return []
#
#
# @bp_principal.route('/carregarProventos', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_proventos():
#     try:
#
#         loop = asyncio.new_event_loop()  # get_event_loop
#         try:
#             asyncio.set_event_loop(loop)
#
#             tasks = [asyncio.Task(get_json_carregar_proventos_async(tipo_invest='ACAO-1')),
#                      asyncio.Task(get_json_carregar_proventos_async(tipo_invest='ACAO-2')),
#                      asyncio.Task(get_json_carregar_proventos_async(tipo_invest='FII-1')),
#                      asyncio.Task(get_json_carregar_proventos_async(tipo_invest='FII-2')),
#                      asyncio.Task(get_json_carregar_proventos_async(tipo_invest='BDR-1')),
#                      asyncio.Task(get_json_carregar_proventos_async(tipo_invest='BDR-2')),
#                     ]
#
#             results = loop.run_until_complete(asyncio.gather(*tasks))
#
#             lista = []
#             lista += results[0]
#             lista += results[1]
#             lista += results[2]
#             lista += results[3]
#             lista += results[4]
#             lista += results[5]
#
#         finally:
#             try:
#                 loop.close()
#             except:
#                 pass
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @asyncio.coroutine
# async def get_json_carregar_proventos_async(tipo_invest: str = None) -> []:
#     return get_json_carregar_proventos(tipo_invest=tipo_invest)
#
#
# def get_json_carregar_proventos(tipo_invest: str = None):
#     try:
#
#         lista = []
#         id_usuario = current_user.id
#
#         # ACAO - proventos recebidos nao aprovados
#         if not tipo_invest or str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'ACAO-1':
#             dt_fim = converter_datetime_str(data=pegar_data_atual(istext=False) + adicionar_dias(dias=-1), fmt="%Y%m%d")  # DIA ANTERIOR
#             rows = UsuarioACAOEmpresaProvento.buscar_todos(id_usuario=id_usuario, dt_fim=str(dt_fim), situacao='B')
#             lista += [[str(row['DATAPAGTO']), str(row['TIPO']), str(row['CODIGOATIVO']), int(row['QUANTIDADE']), decimal_prov_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['TOTVLR'])), str(row['SITUACAO']), str(row['ID']), str(row['DATAEX']), UsuarioACAOEmpresaProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', 'ACAO'] for row in rows]
#
#         # ACAO - proventos a receber no mes
#         if not tipo_invest or str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'ACAO-2':
#             dt_ini = pegar_data_atual()
#             rows = UsuarioACAOEmpresaProvento.buscar_todos(id_usuario=id_usuario, dt_ini=str(dt_ini))
#             lista += [[str(row['DATAPAGTO']), str(row['TIPO']), str(row['CODIGOATIVO']), int(row['QUANTIDADE']), decimal_prov_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['TOTVLR'])), str(row['SITUACAO']), str(row['ID']), str(row['DATAEX']), UsuarioACAOEmpresaProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', 'ACAO'] for row in rows]
#
#         # FII - proventos recebidos nao aprovados
#         if not tipo_invest or str(tipo_invest) == 'FII' or str(tipo_invest) == 'FII-1':
#             dt_fim = converter_datetime_str(data=pegar_data_atual(istext=False) + adicionar_meses(meses=-1), fmt="%Y%m") + '31'  # ULTIMO DIA DO MES ANTERIOR
#             rows = UsuarioFiiFundoImobProvento.buscar_todos(id_usuario=id_usuario, dt_fim=str(dt_fim), situacao='B')
#             lista += [[str(row['DATAPAGTO']), str(row['TIPO']), str(row['CODIGOFUNDO']), int(row['QUANTIDADE']), decimal_prov_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['TOTVLR'])), str(row['SITUACAO']), str(row['ID']), str(row['DATAEX']), UsuarioFiiFundoImobProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', 'FII'] for row in rows]
#
#         # FII - proventos a receber no mes
#         if not tipo_invest or str(tipo_invest) == 'FII' or str(tipo_invest) == 'FII-2':
#             dt_ini = pegar_data_atual(fmt='%Y%m')+'01'
#             rows = UsuarioFiiFundoImobProvento.buscar_todos(id_usuario=id_usuario, dt_ini=str(dt_ini))
#             lista += [[str(row['DATAPAGTO']), 'F'+str(row['TIPO']), str(row['CODIGOFUNDO']), int(row['QUANTIDADE']), decimal_prov_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['TOTVLR'])), str(row['SITUACAO']), str(row['ID']), str(row['DATAEX']), UsuarioFiiFundoImobProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', 'FII'] for row in rows]
#
#         # BDR - proventos recebidos nao aprovados
#         if not tipo_invest or str(tipo_invest) == 'BDR' or str(tipo_invest) == 'BDR-1':
#             dt_fim = converter_datetime_str(data=pegar_data_atual(istext=False) + adicionar_dias(dias=-1), fmt="%Y%m%d")  # DIA ANTERIOR
#             rows = UsuarioBDREmpresaProvento.buscar_todos(id_usuario=id_usuario, dt_fim=str(dt_fim), situacao='B')
#             lista += [[str(row['DATAPAGTO']), str(row['TIPO']), str(row['CODIGOBDR']), int(row['QUANTIDADE']), decimal_prov_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['TOTVLR'])), str(row['SITUACAO']), str(row['ID']), str(row['DATAEX']), UsuarioBDREmpresaProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', 'BDR'] for row in rows]
#
#         # BDR - proventos a receber no mes
#         if not tipo_invest or str(tipo_invest) == 'BDR' or str(tipo_invest) == 'BDR-2':
#             dt_ini = pegar_data_atual()
#             rows = UsuarioBDREmpresaProvento.buscar_todos(id_usuario=id_usuario, dt_ini=str(dt_ini))
#             lista += [[str(row['DATAPAGTO']), str(row['TIPO']), str(row['CODIGOBDR']), int(row['QUANTIDADE']), decimal_prov_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['TOTVLR'])), str(row['SITUACAO']), str(row['ID']), str(row['DATAEX']), UsuarioBDREmpresaProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', 'BDR'] for row in rows]
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return []
#
#
# @bp_principal.route('/carregarFatos', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_fatos():
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
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         lista = []
#         if not tipo_invest or str(tipo_invest) == 'ACAO': lista += get_lista_fatos(tipo_invest='ACAO')
#         if not tipo_invest or str(tipo_invest) == 'FII': lista += get_lista_fatos(tipo_invest='FII')
#         if not tipo_invest or str(tipo_invest) == 'ETF': lista += get_lista_fatos(tipo_invest='ETF')
#         if not tipo_invest or str(tipo_invest) == 'BDR': lista += get_lista_fatos(tipo_invest='BDR')
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarfatosportipos', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_fatos_por_tipo():
#     try:
#
#         loop = asyncio.new_event_loop()  # get_event_loop
#         try:
#             asyncio.set_event_loop(loop)
#
#             tasks = [asyncio.Task(get_lista_fatos_async(tipo_invest='ACAO')),
#                      asyncio.Task(get_lista_fatos_async(tipo_invest='FII')),
#                      asyncio.Task(get_lista_fatos_async(tipo_invest='ETF')),
#                      asyncio.Task(get_lista_fatos_async(tipo_invest='BDR')),
#                     ]
#
#             results = loop.run_until_complete(asyncio.gather(*tasks))
#
#             lista_acao = results[0]
#             lista_fii = results[1]
#             lista_etf = results[2]
#             lista_bdr = results[3]
#
#         finally:
#             try:
#                 loop.close()
#             except:
#                 pass
#
#         dados = dict({"lista_acao": lista_acao, "lista_fii": lista_fii, "lista_etf": lista_etf, "lista_bdr": lista_bdr})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarFatosAcoes', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_fatos_acoes():
#     try:
#         lista = get_lista_fatos(tipo_invest='ACAO')
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarFatosFiis', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_fatos_fiis():
#     try:
#         lista = get_lista_fatos(tipo_invest='FII')
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarFatosEtfs', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_fatos_etfs():
#     try:
#         lista = get_lista_fatos(tipo_invest='ETF')
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarFatosBdrs', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_fatos_bdrs():
#     try:
#         lista = get_lista_fatos(tipo_invest='BDR')
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @asyncio.coroutine
# async def get_lista_fatos_async(id_usuario: int = None, tipo_invest: str = None) -> []:
#     return get_lista_fatos(id_usuario=id_usuario, tipo_invest=tipo_invest)
#
#
# def get_lista_fatos(id_usuario: int = None, tipo_invest: str = None) -> []:
#     try:
#
#         if not id_usuario: id_usuario = current_user.id
#
#         lista = []
#         dt_env = pegar_data_atual(fmt='%Y%m') + '01'
#
#         if str(tipo_invest) == 'ACAO':
#             rows = ACAOEmpresaFatoRelevante.buscar_por_ano_mes(id_usuario=id_usuario, dt_env=str(dt_env))
#             lista += [[str(row['ID']), str(row['NMEMPRESA']), str(row['DATA_ENV']), str(row['LINK']), str(row['ASSUNTO']), str(row['PROTOCOLO']), 'ACAO'] for row in rows]
#
#         elif str(tipo_invest) == 'FII':
#             rows = FiiFundoImobFatoRelevante.buscar_por_ano_mes(id_usuario=id_usuario, dt_env=str(dt_env))
#             lista += [[str(row['ID']), str(row['NMFUNDO']), str(row['DATA_ENV']), str(row['LINK']), str(row['ASSUNTO']), str(row['PROTOCOLO']), 'FII'] for row in rows]
#
#         elif str(tipo_invest) == 'ETF':
#             rows = ETFIndiceFatoRelevante.buscar_por_ano_mes(id_usuario=id_usuario, dt_env=str(dt_env))
#             lista += [[str(row['ID']), str(row['NMINDICE']), str(row['DATA_ENV']), str(row['LINK']), str(row['ASSUNTO']), str(row['PROTOCOLO']), 'ETF'] for row in rows]
#
#         elif str(tipo_invest) == 'BDR':
#             rows = BDREmpresaFatoRelevante.buscar_por_ano_mes(id_usuario=id_usuario, dt_env=str(dt_env))
#             lista += [[str(row['ID']), str(row['NMEMPRESA']), str(row['DATA_ENV']), str(row['LINK']), str(row['ASSUNTO']), str(row['PROTOCOLO']), 'BDR'] for row in rows]
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return []
#
#
# @bp_principal.route('/carregarNoticias', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_noticias():
#     try:
#
#         dt_hr_ini = pegar_data_atual()+'000000'
#         dt_hr_fim = pegar_data_atual()+'235959'
#
#         rows = AlertaNoticia.buscar_todos(dt_hr_ini=str(dt_hr_ini), dt_hr_fim=str(dt_hr_fim))
#         lista = [[str(row['ID']), str(row['SITE']), str(row['DTHRREGISTRO']), str(row['TIPO']), str(row['TITULO']), str(row['LINK'])] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/carregarCalendario', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_calendario(tipo_invest: str = None):
#     try:
#
#         loop = asyncio.new_event_loop()  # get_event_loop
#         try:
#             asyncio.set_event_loop(loop)
#
#             tasks = [asyncio.Task(get_json_carregar_calendario_async(tipo_invest='ACAO')),
#                      asyncio.Task(get_json_carregar_calendario_async(tipo_invest='FII')),
#                      asyncio.Task(get_json_carregar_calendario_async(tipo_invest='BDR')),
#                     ]
#
#             results = loop.run_until_complete(asyncio.gather(*tasks))
#
#             lista = []
#             lista += results[0]
#             lista += results[1]
#             lista += results[2]
#
#         finally:
#             try:
#                 loop.close()
#             except:
#                 pass
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @asyncio.coroutine
# async def get_json_carregar_calendario_async(tipo_invest: str = None) -> []:
#     return get_json_carregar_calendario(tipo_invest=tipo_invest)
#
#
# def get_json_carregar_calendario(tipo_invest: str = None):
#     try:
#
#         lista = []
#         id_usuario = current_user.id
#         dt_ini = pegar_data_atual(fmt='%Y%m')+'01'
#         dt_ex = dt_ini
#         dt_pagto = dt_ini
#
#         # ACAO - PROVENTOS CALENDARIO
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             rows = ACAOEmpresaProvento.buscar_por_usuario(id_usuario=id_usuario, dt_ex=str(dt_ex), dt_pagto=str(dt_pagto))
#             lista += [[str(row['ID']), str(row['CODATIVO']), str(row['TIPO']), converter_datetime_str(data=converter_str_to_datetime(data=str(row['DATAEX']), fmt='%Y%m%d'), fmt='%Y-%m-%d'), converter_datetime_str(data=converter_str_to_datetime(data=str(row['DATAPAGTO']), fmt='%Y%m%d'), fmt='%Y-%m-%d'), str(row['VLRPRECO']), "ACAO"] for row in rows]
#
#         # FII - PROVENTOS CALENDARIO
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             rows = FiiFundoImobProvento.buscar_por_usuario(id_usuario=id_usuario, dt_ex=str(dt_ex), dt_pagto=str(dt_pagto))
#             lista += [[str(row['ID']), str(row['CODIGOFUNDO']), 'F'+str(row['TIPO']), converter_datetime_str(data=converter_str_to_datetime(data=str(row['DATAEX']), fmt='%Y%m%d'), fmt='%Y-%m-%d'), converter_datetime_str(data=converter_str_to_datetime(data=str(row['DATAPAGTO']), fmt='%Y%m%d'), fmt='%Y-%m-%d'), str(row['VLRPRECO']), "FII"] for row in rows]
#
#         # BDR - PROVENTOS CALENDARIO
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             rows = BDREmpresaProvento.buscar_por_usuario(id_usuario=id_usuario, dt_ex=str(dt_ex), dt_pagto=str(dt_pagto))
#             lista += [[str(row['ID']), str(row['CODIGOBDR']), str(row['TIPO']), converter_datetime_str(data=converter_str_to_datetime(data=str(row['DATAEX']), fmt='%Y%m%d'), fmt='%Y-%m-%d'), converter_datetime_str(data=converter_str_to_datetime(data=str(row['DATAPAGTO']), fmt='%Y%m%d'), fmt='%Y-%m-%d'), str(row['VLRPRECO']), "BDR"] for row in rows]
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return []
#
#
# @bp_principal.route('/removerProvDivulgado', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def remover_prov_divulgado():
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
#             id_provento = data.get('IdEmprProv')
#             codigo = data.get('CodAtivo')
#             tipo = data.get('Tipo')
#             data_ex = data.get('DataEx')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_provento: return make_response(get_json_retorno_metodo(msg='Id. Provento Inválido.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Código não informado.'), 200)
#         if not tipo: return make_response(get_json_retorno_metodo(msg='Tipo Provento Inválido.'), 200)
#         if not data_ex: return make_response(get_json_retorno_metodo(msg='Data Ex Provento Inválido.'), 200)
#
#         tipo_invest = ''
#         id_ativo = None
#
#         if not tipo_invest:
#             ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#             if ativo:
#                 tipo_invest = 'ACAO'
#                 id_ativo = int(ativo.id)
#
#         if not tipo_invest:
#             ativo = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#             if ativo:
#                 tipo_invest = 'FII'
#                 id_ativo = int(ativo.id)
#
#         if not tipo_invest:
#             ativo = BDREmpresa.get_by_codigo(codigo=str(codigo))
#             if ativo:
#                 tipo_invest = 'BDR'
#                 id_ativo = int(ativo.id)
#
#         if not tipo_invest:
#             return make_response(get_json_retorno_metodo(msg='Tipo Invest. não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         prov = None
#
#         if tipo_invest and str(tipo_invest) == 'ACAO':
#             prov = UsuarioACAOEmpresaProventoAtivo()
#             prov.id_ativo = int(id_ativo)
#             prov.tipo = str(tipo)
#
#         elif tipo_invest and str(tipo_invest) == 'FII':
#             prov = UsuarioFiiFundoImobProventoAtivo()
#             prov.id_fundo = int(id_ativo)
#             prov.tipo = "R" if str(tipo) == 'FR' else str(tipo)  # FR - FII RENDIMENTO
#
#         elif tipo_invest and str(tipo_invest) == 'BDR':
#             prov = UsuarioBDREmpresaProventoAtivo()
#             prov.id_bdr = int(id_ativo)
#             prov.tipo = str(tipo)
#
#         if not prov:
#             return make_response(get_json_retorno_metodo(msg='Tipo Provento não informado.'), 200)
#
#         prov.id_usuario = id_usuario
#         prov.id_provento = int(id_provento)
#         prov.data_ex = str(data_ex)
#         prov.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Provento Removido!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/removerFatoRelevante', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def remover_fato_relevante():
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
#             id_fato = data.get('IdFato')
#             tipo_invest = data.get('TipoInvest')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_fato: return make_response(get_json_retorno_metodo(msg='Id. Fato Inválido.'), 200)
#         if not tipo_invest: return make_response(get_json_retorno_metodo(msg='Tipo Fato Inválido.'), 200)
#
#         fato = None
#         if tipo_invest and str(tipo_invest) == 'ACAO':
#             fato = UsuarioACAOEmpresaFatoRelevanteAtivo()
#         elif tipo_invest and str(tipo_invest) == 'FII':
#             fato = UsuarioFiiFundoImobFatoRelevanteAtivo()
#         elif tipo_invest and str(tipo_invest) == 'ETF':
#             fato = UsuarioETFIndiceFatoRelevanteAtivo()
#         elif tipo_invest and str(tipo_invest) == 'BDR':
#             fato = UsuarioBDREmpresaFatoRelevanteAtivo()
#
#         if not fato:
#             return make_response(get_json_retorno_metodo(msg='Tipo Fato não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         fato.id_usuario = id_usuario
#         fato.id_fato = id_fato
#         fato.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Fato Removido!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_principal.route('/agendatrimestre', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def agenda_trimestre():
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
#             tipo = data.get('Tipo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not tipo: return make_response(get_json_retorno_metodo(msg='Tipo Inválido.'), 200)
#
#         id_usuario = current_user.id
#         data_atual = pegar_data_atual()
#
#         rows = ACAOEmpresaFinanceiroAgenda.buscar_todos(id_usuario=id_usuario, divulgacao=str(data_atual), tipo=str(tipo))
#         lista = [[str(row['NOME']), str(row['CODIGO']), str(row['DIVULGACAO']), str(row['HORARIO'])] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)