# -*- coding: utf-8 -*-
import sys
import os
import datetime as dt
import time
import asyncio
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache, set_cache_portf, get_cache_portf
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.acao_empresa_ativo_cotacao import ACAOEmpresaAtivoCotacao
# from app.models.fii_fundoimob import FiiFundoImob
# from app.models.etf_indice import ETFIndice
# from app.models.bdr_empresa import BDREmpresa
# from app.models.cripto_empresa import CriptoEmpresa
# from app.models.usuario_carteira import UsuarioCarteira
# from app.models.usuario_carteira_acao import UsuarioCarteiraAcao
# from app.models.usuario_carteira_fii import UsuarioCarteiraFii
# from app.models.usuario_carteira_etf import UsuarioCarteiraEtf
# from app.models.usuario_carteira_bdr import UsuarioCarteiraBdr
# from app.models.usuario_carteira_cripto import UsuarioCarteiraCripto
# from app.models.usuario_radar_acao import UsuarioRadarAcao
# from app.models.usuario_radar_fii import UsuarioRadarFii
# from app.models.usuario_radar_etf import UsuarioRadarEtf
# from app.models.usuario_radar_bdr import UsuarioRadarBdr
# from app.models.usuario_radar_cripto import UsuarioRadarCripto
# from app.models.usuario_acao_empresa_aluguel import UsuarioACAOEmpresaAluguel
# from app.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamento
# from app.models.usuario_acao_empresa_operacao import UsuarioACAOEmpresaOperacao
# from app.models.usuario_acao_empresa_provento import UsuarioACAOEmpresaProvento
# from app.models.usuario_fii_fundoimob_lancamento import UsuarioFiiFundoImobLancamento
# from app.models.usuario_fii_fundoimob_provento import UsuarioFiiFundoImobProvento
# from app.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamento
# from app.models.usuario_etf_indice_operacao import UsuarioETFIndiceOperacao
# from app.models.usuario_bdr_empresa_lancamento import UsuarioBDREmpresaLancamento
# from app.models.usuario_bdr_empresa_operacao import UsuarioBDREmpresaOperacao
# from app.models.usuario_bdr_empresa_provento import UsuarioBDREmpresaProvento
# from app.models.usuario_cripto_lancamento import UsuarioCriptoLancamento
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_formatacao import decimal_to_str, decimal_prov_to_str, decimal_cripto_curto_to_str, inteiro_to_str
# from app.util.util_datahora import pegar_data_atual
# #import memory_profiler as mp
#
#
# bp_portfolio = Blueprint('portfolio', __name__, url_prefix='/portfolio')
#
#
# @bp_portfolio.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#
#     id_usuario = current_user.id
#
#     # qtd_ativos = 0
#     # if qtd_ativos == 0 and UsuarioACAOEmpresaOperacao.buscar_quant_ativo(id_usuario=id_usuario) > 0: qtd_ativos = 1
#     # if qtd_ativos == 0 and UsuarioFiiFundoImobLancamento.buscar_quant_ativo(id_usuario=id_usuario) > 0: qtd_ativos = 1
#     # if qtd_ativos == 0 and UsuarioETFIndiceOperacao.buscar_quant_ativo(id_usuario=id_usuario) > 0: qtd_ativos = 1
#     # if qtd_ativos == 0 and UsuarioBDREmpresaOperacao.buscar_quant_ativo(id_usuario=id_usuario) > 0: qtd_ativos = 1
#     # if qtd_ativos == 0 and UsuarioCriptoLancamento.buscar_quant_ativo(id_usuario=id_usuario) > 0: qtd_ativos = 1
#     # if qtd_ativos == 0.0: return render_template(template_name_or_list="portfolio_sem_ativo.html")
#
#     lista_nomes = get_lista_nome_portfolio()
#     if lista_nomes: lista_nomes.sort(reverse=True)
#     # lista_nomes = sorted(lista_nomes, reverse=True, key=lambda k: k[0])
#
#     # lista_data_set_pagina = get_json_data_set_pagina()
#     # lista_data_set_radar = get_json_ativos_no_radar()
#
#     gerar_portoflio = False
#     if not gerar_portoflio and UsuarioACAOEmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#     if not gerar_portoflio and UsuarioFiiFundoImobLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#     if not gerar_portoflio and UsuarioETFIndiceLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#     if not gerar_portoflio and UsuarioBDREmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#     if not gerar_portoflio and UsuarioCriptoLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#
#     return render_template(
#         template_name_or_list="portfolio.html",
#         gerar_portoflio=gerar_portoflio,
#         lista_nomes=lista_nomes
#         # lista_data_set_pagina=lista_data_set_pagina
#         # lista_data_set_radar=lista_data_set_radar
#     )
#
# @bp_portfolio.route('/grid', methods=['GET', 'POST'])
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
#             id_portfolio = data.get('IdPortfolio')
#             tipo_invest = data.get('TipoInvest')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         id_usuario = current_user.id
#
#         lista = []
#         data_atual = pegar_data_atual()
#         ano_atual = pegar_data_atual(fmt='%Y')
#         data_inicio = str(int(ano_atual)- 1) + pegar_data_atual(fmt='%m%d')
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             rows = UsuarioCarteiraAcao.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#             for row in rows:
#                 id_ativo = int(row['IDATIVO'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#                 tot_invest = (int(quant_tot) * float(preco_medio)) if int(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual = (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_valorz = float(tot_atual) - float(tot_invest)
#                 perc_valorz = 0.0
#                 if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#                 if float(tot_valorz) != 0.00 and float(tot_invest) == 0.0 and int(quant_bonus) > 0 and float(preco_medio) > 0.0: perc_valorz = (float(tot_valorz) / (int(quant_bonus) * float(preco_medio))) * 100
#                 tot_alug = UsuarioACAOEmpresaAluguel.buscar_vlr_total(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(ano_atual) + '1231')
#                 tot_prov = UsuarioACAOEmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(data_atual))
#                 dt_fim = UsuarioACAOEmpresaProvento.buscar_maior_data_ex(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(data_atual))
#                 prec_prov = UsuarioACAOEmpresaProvento.buscar_vlr_preco_ex(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_ini=str(data_inicio), dt_fim=str(dt_fim))
#                 preco_medio_yoc = UsuarioACAOEmpresaOperacao.buscar_preco_medio_antes(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(dt_fim))
#                 yield_on_cost = ((float(prec_prov) / float(preco_medio_yoc)) * 100) if float(preco_medio_yoc) > 0.0 and float(prec_prov) > 0.0 else 0.0
#                 lista.append([str(row['CODIGOATIVO']), inteiro_to_str(valor=float(quant_tot)), decimal_to_str(valor=float(preco_medio)), decimal_to_str(valor=float(preco_atual)), decimal_to_str(valor=float(preco_teto)), decimal_to_str(valor=float(tot_invest)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(tot_valorz)), decimal_to_str(valor=float(perc_valorz)), decimal_to_str(valor=float(tot_prov)), decimal_to_str(valor=float(yield_on_cost)), decimal_to_str(valor=float(tot_alug)), str(id_ativo), 'ACAO'])
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             rows = UsuarioCarteiraFii.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#             for row in rows:
#                 id_fundo = int(row['IDFUNDO'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#                 tot_invest = (int(quant_tot) * float(preco_medio)) if int(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual = (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_valorz = float(tot_atual) - float(tot_invest)
#                 perc_valorz = 0.0
#                 if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#                 if float(tot_valorz) != 0.00 and float(tot_invest) == 0.0 and int(quant_bonus) > 0 and float(preco_medio) > 0.0: perc_valorz = (float(tot_valorz) / (int(quant_bonus) * float(preco_medio))) * 100
#                 tot_alug = 0.0
#                 tot_prov = UsuarioFiiFundoImobProvento.buscar_vlr_total(id_usuario=id_usuario, id_fundo=int(id_fundo), dt_fim=str(data_atual))
#                 dt_fim = UsuarioFiiFundoImobProvento.buscar_maior_data_ex(id_usuario=id_usuario, id_fundo=int(id_fundo), dt_fim=str(data_atual))
#                 prec_prov = UsuarioFiiFundoImobProvento.buscar_vlr_preco_ex(id_usuario=id_usuario, id_fundo=int(id_fundo), dt_ini=str(data_inicio), dt_fim=str(dt_fim))
#                 preco_medio_yoc = UsuarioFiiFundoImobLancamento.buscar_preco_medio_antes(id_usuario=id_usuario, id_fundo=int(id_fundo), dt_fim=str(dt_fim))
#                 yield_on_cost = ((float(prec_prov) / float(preco_medio_yoc)) * 100) if float(preco_medio_yoc) > 0.0 and float(prec_prov) > 0.0 else 0.0
#                 lista.append([str(row['CODIGOFUNDO']), inteiro_to_str(valor=float(quant_tot)), decimal_to_str(valor=float(preco_medio)), decimal_to_str(valor=float(preco_atual)), decimal_to_str(valor=float(preco_teto)), decimal_to_str(valor=float(tot_invest)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(tot_valorz)), decimal_to_str(valor=float(perc_valorz)), decimal_to_str(valor=float(tot_prov)), decimal_to_str(valor=float(yield_on_cost)), decimal_to_str(valor=float(tot_alug)), str(id_fundo), 'FII'])
#
#         if not tipo_invest or str(tipo_invest) == 'ETF':
#             rows = UsuarioCarteiraEtf.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#             for row in rows:
#                 id_indice = int(row['IDINDICE'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#                 tot_invest = (int(quant_tot) * float(preco_medio)) if int(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual = (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_valorz = float(tot_atual) - float(tot_invest)
#                 perc_valorz = 0.0
#                 if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#                 if float(tot_valorz) != 0.00 and float(tot_invest) == 0.0 and int(quant_bonus) > 0 and float(preco_medio) > 0.0: perc_valorz = (float(tot_valorz) / (int(quant_bonus) * float(preco_medio))) * 100
#                 tot_alug = 0.0
#                 tot_prov = 0.0
#                 yield_on_cost = 0.0
#                 lista.append([str(row['CODIGOINDICE']), inteiro_to_str(valor=float(quant_tot)), decimal_to_str(valor=float(preco_medio)), decimal_to_str(valor=float(preco_atual)), decimal_to_str(valor=float(preco_teto)), decimal_to_str(valor=float(tot_invest)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(tot_valorz)), decimal_to_str(valor=float(perc_valorz)), decimal_to_str(valor=float(tot_prov)), decimal_to_str(valor=float(yield_on_cost)), decimal_to_str(valor=float(tot_alug)), str(id_indice), 'ETF'])
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             rows = UsuarioCarteiraBdr.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#             for row in rows:
#                 id_ativo = int(row['IDBDR'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#                 tot_invest = (int(quant_tot) * float(preco_medio)) if int(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual = (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_valorz = float(tot_atual) - float(tot_invest)
#                 perc_valorz = 0.0
#                 if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#                 if float(tot_valorz) != 0.00 and float(tot_invest) == 0.0 and int(quant_bonus) > 0 and float(preco_medio) > 0.0: perc_valorz = (float(tot_valorz) / (int(quant_bonus) * float(preco_medio))) * 100
#                 tot_alug = 0.0
#                 tot_prov = UsuarioBDREmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_bdr=int(id_ativo), dt_fim=str(data_atual))
#                 dt_fim = UsuarioBDREmpresaProvento.buscar_maior_data_ex(id_usuario=id_usuario, id_bdr=int(id_ativo), dt_fim=str(data_atual))
#                 prec_prov = UsuarioBDREmpresaProvento.buscar_vlr_preco_ex(id_usuario=id_usuario, id_bdr=int(id_ativo), dt_ini=str(data_inicio), dt_fim=str(dt_fim))
#                 preco_medio_yoc = UsuarioBDREmpresaOperacao.buscar_preco_medio_antes(id_usuario=id_usuario, id_bdr=int(id_ativo), dt_fim=str(dt_fim))
#                 yield_on_cost = ((float(prec_prov) / float(preco_medio_yoc)) * 100) if float(preco_medio_yoc) > 0.0 and float(prec_prov) > 0.0 else 0.0
#                 lista.append([str(row['CODIGOBDR']), inteiro_to_str(valor=float(quant_tot)), decimal_to_str(valor=float(preco_medio)), decimal_to_str(valor=float(preco_atual)), decimal_to_str(valor=float(preco_teto)), decimal_to_str(valor=float(tot_invest)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(tot_valorz)), decimal_to_str(valor=float(perc_valorz)), decimal_to_str(valor=float(tot_prov)), decimal_to_str(valor=float(yield_on_cost)), decimal_to_str(valor=float(tot_alug)), str(id_ativo), 'BDR'])
#
#         if not tipo_invest or str(tipo_invest) == 'CRIPTO':
#             rows = UsuarioCarteiraCripto.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#             for row in rows:
#                 id_cripto = int(row['IDCRIPTO'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_tot = float(quant)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#                 tot_invest = (int(quant_tot) * float(preco_medio)) if int(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual = (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_valorz = float(tot_atual) - float(tot_invest)
#                 perc_valorz = 0.0
#                 if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#                 tot_alug = 0.0
#                 tot_prov = 0.0
#                 yield_on_cost = 0.0
#                 lista.append([str(row['CODIGOCRIPTO']), decimal_prov_to_str(valor=float(quant_tot)), decimal_prov_to_str(valor=float(preco_medio)), decimal_prov_to_str(valor=float(preco_atual)), decimal_prov_to_str(valor=float(preco_teto)), decimal_to_str(valor=float(tot_invest)), decimal_to_str(valor=float(tot_atual)), decimal_to_str(valor=float(tot_valorz)), decimal_to_str(valor=float(perc_valorz)), decimal_to_str(valor=float(tot_prov)), decimal_to_str(valor=float(yield_on_cost)), decimal_to_str(valor=float(tot_alug)), str(id_cripto), 'CRIPTO'])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/gridcompleta', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_completa():
#     try:
#
#         id_usuario = current_user.id
#
#         data_atual = pegar_data_atual()
#         ano_atual = pegar_data_atual(fmt='%Y')
#         lista = []
#
#         carteiras = UsuarioCarteira.buscar_todos(id_usuario=id_usuario)
#
#         for carteira in carteiras:
#
#             id_portforio = int(carteira['ID']) if str(carteira['TIPO']) == 'P' else None
#             tot_invest = 0.0
#             tot_atual = 0.0
#             tot_prov = 0.0
#             tot_alug = 0.0
#
#             rows = UsuarioCarteiraAcao.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portforio, situacao='A')
#             for row in rows:
#                 id_ativo = int(row['IDATIVO'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_invest += (int(quant_tot) * float(preco_medio)) if int(quant_tot) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_prov += UsuarioACAOEmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(data_atual))
#                 tot_alug += UsuarioACAOEmpresaAluguel.buscar_vlr_total(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(ano_atual) + '1231')
#
#             rows = UsuarioCarteiraFii.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portforio, situacao='A')
#             for row in rows:
#                 id_fundo = int(row['IDFUNDO'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_invest += (int(quant_tot) * float(preco_medio)) if int(quant_tot) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_prov += UsuarioFiiFundoImobProvento.buscar_vlr_total(id_usuario=id_usuario, id_fundo=int(id_fundo), dt_fim=str(data_atual))
#                 tot_alug += 0.0
#
#             rows = UsuarioCarteiraEtf.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portforio, situacao='A')
#             for row in rows:
#                 id_indice = int(row['IDINDICE'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_invest += (int(quant_tot) * float(preco_medio)) if int(quant_tot) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_prov += 0.0
#                 tot_alug += 0.0
#
#             rows = UsuarioCarteiraBdr.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portforio, situacao='A')
#             for row in rows:
#                 id_ativo = int(row['IDBDR'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_invest += (int(quant_tot) * float(preco_medio)) if int(quant_tot) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_prov += UsuarioBDREmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_bdr=int(id_ativo), dt_fim=str(data_atual))
#                 tot_alug += 0.0
#
#             rows = UsuarioCarteiraCripto.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portforio, situacao='A')
#             for row in rows:
#                 id_cripto = int(row['IDCRIPTO'])
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_tot = float(quant)
#                 preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#                 preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 tot_invest += (int(quant_tot) * float(preco_medio)) if int(quant_tot) > 0 and float(preco_medio) > 0.00 else 0.0
#                 tot_atual += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#                 tot_prov += 0.0
#                 tot_alug += 0.0
#
#             tot_valorz = float(tot_atual) - float(tot_invest)
#             perc_valorz = 0.0
#             if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#             if float(tot_valorz) != 0.00 and float(tot_invest) == 0.0: perc_valorz = 100.0
#             tot_ganho = float(tot_valorz) + float(tot_prov) + float(tot_alug)
#             perc_ganho = ((float(tot_ganho) / float(tot_invest)) * 100) if float(tot_ganho) != 0.0 and float(tot_invest) > 0.0 else 0.0
#
#             lista.append({
#                 "id": str(id_portforio),
#                 "descr": str(carteira['DESCRICAO']),
#                 "totInvest": decimal_to_str(valor=float(tot_invest)),
#                 "totAtual": decimal_to_str(valor=float(tot_atual)),
#                 "totValorz": decimal_to_str(valor=float(tot_valorz)),
#                 "percValorz": decimal_to_str(valor=float(perc_valorz)),
#                 "totProv": decimal_to_str(valor=float(tot_prov)),
#                 "totAlug": decimal_to_str(valor=float(tot_alug)),
#                 "totGanho": decimal_to_str(valor=float(tot_ganho)),
#                 "percGanho": decimal_to_str(valor=float(perc_ganho))
#             })
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/valorizacaoDia', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def valorizacaoDia():
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
#             tipo_invest = data.get('TipoInvest')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             rows = UsuarioCarteiraAcao.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 vlr_fechamento = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 vlr_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#                 perc_valorizacao = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#                 tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#                 lista.append([str(row['CODIGOATIVO']), inteiro_to_str(valor=float(quant_tot)), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             rows = UsuarioCarteiraFii.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 vlr_fechamento = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 vlr_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#                 perc_valorizacao = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#                 tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#                 lista.append([str(row['CODIGOFUNDO']), inteiro_to_str(valor=float(quant_tot)), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         if not tipo_invest or str(tipo_invest) == 'ETF':
#             rows = UsuarioCarteiraEtf.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 vlr_fechamento = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 vlr_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#                 perc_valorizacao = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#                 tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#                 lista.append([str(row['CODIGOINDICE']), inteiro_to_str(valor=float(quant_tot)), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             rows = UsuarioCarteiraBdr.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                 quant_tot = float(quant) + float(quant_bonus)
#                 vlr_fechamento = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 vlr_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#                 perc_valorizacao = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#                 tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#                 lista.append([str(row['CODIGOBDR']), inteiro_to_str(valor=float(quant_tot)), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         if not tipo_invest or str(tipo_invest) == 'CRIPTO':
#             rows = UsuarioCarteiraCripto.buscar_todos_simples(id_usuario=id_usuario, id_carteira=id_portfolio, situacao="A")
#             for row in rows:
#                 quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                 quant_tot = float(quant)
#                 vlr_fechamento = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                 vlr_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#                 perc_valorizacao = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#                 tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#                 lista.append([str(row['CODIGOCRIPTO']), decimal_prov_to_str(valor=float(quant_tot)), decimal_prov_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/ativosNoRadar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def ativos_no_radar():
#     try:
#
#         return make_response(get_json_ativos_no_radar(), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# def get_json_ativos_no_radar():
#     try:
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         codigo = 'IBOV'
#         row = ACAOEmpresaAtivoCotacao.buscar_por_codigo(codigo=str(codigo))
#         vlr_fechamento = float(row['VLRPRECOFECHAMENTO']) if row and row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#         vlr_anterior = float(row['VLRPRECOANTERIOR']) if row and row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#         perc_valorizacao = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#         tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#         lista.append([str(codigo), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         codigo = 'IDIV'
#         row = ACAOEmpresaAtivoCotacao.buscar_por_codigo(codigo=str(codigo))
#         vlr_fechamento = float(row['VLRPRECOFECHAMENTO']) if row and row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#         vlr_anterior = float(row['VLRPRECOANTERIOR']) if row and row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#         perc_valorizacao = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#         tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#         lista.append([str(codigo), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         codigo = 'IBXX'
#         row = ACAOEmpresaAtivoCotacao.buscar_por_codigo(codigo=str(codigo))
#         vlr_fechamento = float(row['VLRPRECOFECHAMENTO']) if row and row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#         vlr_anterior = float(row['VLRPRECOANTERIOR']) if row and row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#         perc_valorizacao = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#         tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#         lista.append([str(codigo), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         codigo = 'SMLL'
#         row = ACAOEmpresaAtivoCotacao.buscar_por_codigo(codigo=str(codigo))
#         vlr_fechamento = float(row['VLRPRECOFECHAMENTO']) if row and row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#         vlr_anterior = float(row['VLRPRECOANTERIOR']) if row and row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#         perc_valorizacao = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#         tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#         lista.append([str(codigo), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         rows = UsuarioRadarAcao.buscar_dados_grid_port(id_usuario=id_usuario)
#         for row in rows:
#             vlr_fechamento = float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0
#             vlr_anterior = float(row['ANTERIOR']) if row['ANTERIOR'] and float(row['ANTERIOR']) > 0.0 else 0.0
#             perc_valorizacao = float(row['VARIACAO']) if row['VARIACAO'] and float(row['VARIACAO']) != 0.0 else 0.0
#             tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#             lista.append([str(row['CODIGOATIVO']), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         rows = UsuarioRadarFii.buscar_dados_grid_port(id_usuario=id_usuario)
#         for row in rows:
#             vlr_fechamento = float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0
#             vlr_anterior = float(row['ANTERIOR']) if row['ANTERIOR'] and float(row['ANTERIOR']) > 0.0 else 0.0
#             perc_valorizacao = float(row['VARIACAO']) if row['VARIACAO'] and float(row['VARIACAO']) != 0.0 else 0.0
#             tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#             lista.append([str(row['CODIGOATIVO']), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         rows = UsuarioRadarEtf.buscar_dados_grid_port(id_usuario=id_usuario)
#         for row in rows:
#             vlr_fechamento = float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0
#             vlr_anterior = float(row['ANTERIOR']) if row['ANTERIOR'] and float(row['ANTERIOR']) > 0.0 else 0.0
#             perc_valorizacao = float(row['VARIACAO']) if row['VARIACAO'] and float(row['VARIACAO']) != 0.0 else 0.0
#             tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#             lista.append([str(row['CODIGOATIVO']), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         rows = UsuarioRadarBdr.buscar_dados_grid_port(id_usuario=id_usuario)
#         for row in rows:
#             vlr_fechamento = float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0
#             vlr_anterior = float(row['ANTERIOR']) if row['ANTERIOR'] and float(row['ANTERIOR']) > 0.0 else 0.0
#             perc_valorizacao = float(row['VARIACAO']) if row['VARIACAO'] and float(row['VARIACAO']) != 0.0 else 0.0
#             tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#             lista.append([str(row['CODIGOBDR']), decimal_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         rows = UsuarioRadarCripto.buscar_dados_grid_port(id_usuario=id_usuario)
#         for row in rows:
#             vlr_fechamento = float(row['PRECO']) if row['PRECO'] and float(row['PRECO']) > 0.0 else 0.0
#             vlr_anterior = float(row['ANTERIOR']) if row['ANTERIOR'] and float(row['ANTERIOR']) > 0.0 else 0.0
#             perc_valorizacao = float(row['VARIACAO']) if row['VARIACAO'] and float(row['VARIACAO']) != 0.0 else 0.0
#             tot_valorizacao = float(vlr_fechamento) - float(vlr_anterior)
#             lista.append([str(row['CODIGOATIVO']), decimal_prov_to_str(valor=float(vlr_fechamento)), decimal_to_str(valor=float(tot_valorizacao)), decimal_to_str(valor=abs(float(perc_valorizacao)))])
#
#         return get_json_retorno_grid(rslt='OK', lista=lista)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/salvarPortfolio', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_portfolio():
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
#             id_portfolio = data.get('Id')
#             nome_portfolio = data.get('Nome')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not nome_portfolio: return make_response(get_json_retorno_metodo(msg='Nome não informado.'), 200)
#
#         if str(id_portfolio).strip() == '': id_portfolio = None
#
#         id_usuario = current_user.id
#
#         if not id_portfolio:
#             if UsuarioCarteira.get_by_descricao(id_usuario=id_usuario, descricao=str(nome_portfolio)):
#                 return make_response(get_json_retorno_metodo(msg='Nome do Portfólio já cadastrado.'), 200)
#             carteira = UsuarioCarteira()
#         else:
#             carteira = UsuarioCarteira.get_by_usuario(id_usuario=id_usuario, id=int(id_portfolio))
#
#         if not carteira:
#             return make_response(get_json_retorno_metodo(msg='Portfólio não localizado.'), 200)
#
#         carteira.id_usuario = id_usuario
#         carteira.descricao = str(nome_portfolio)
#         carteira.tipo = 'P'  # P-Personalizada
#         carteira.situacao = 'A'  # A-Ativo
#         carteira.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/excluirPortfolio', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir_portfolio():
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
#             id_portfolio = data.get('IdPortfolio')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_portfolio: return make_response(get_json_retorno_metodo(msg='Id. Portfólio Inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         carteira_excl = UsuarioCarteira.get_by_usuario(id_usuario=id_usuario, id=int(id_portfolio))
#         if not carteira_excl: return make_response(get_json_retorno_metodo(msg='Portfólio não localizado.'), 200)
#
#         carteira_default = UsuarioCarteira.buscar_por_tipo_default(id_usuario=id_usuario)
#         if not carteira_default: return make_response(get_json_retorno_metodo(msg='Portfólio Principal não localizado.'), 200)
#
#         # UsuarioEmailInfo.excluir_carteira(id_usuario=id_usuario, id_portfolio=int(id_portfolio))
#         UsuarioCarteiraAcao.atualizar_novo_id_carteira(id_usuario=id_usuario, id_portfolio_old=int(id_portfolio), id_portfolio_new=int(carteira_default['ID']))
#         UsuarioCarteiraFii.atualizar_novo_id_carteira(id_usuario=id_usuario, id_portfolio_old=int(id_portfolio), id_portfolio_new=int(carteira_default['ID']))
#         UsuarioCarteiraEtf.atualizar_novo_id_carteira(id_usuario=id_usuario, id_portfolio_old=int(id_portfolio), id_portfolio_new=int(carteira_default['ID']))
#         UsuarioCarteiraBdr.atualizar_novo_id_carteira(id_usuario=id_usuario, id_portfolio_old=int(id_portfolio), id_portfolio_new=int(carteira_default['ID']))
#         UsuarioCarteiraCripto.atualizar_novo_id_carteira(id_usuario=id_usuario, id_portfolio_old=int(id_portfolio), id_portfolio_new=int(carteira_default['ID']))
#         UsuarioCarteira.excluir_por_id(id_usuario=id_usuario, id_portfolio=int(id_portfolio))
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/salvarAtivo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_ativo():
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
#             id_portfolio = data.get('IdPortfolio')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_portfolio: return make_response(get_json_retorno_metodo(msg='Id. Portfólio Inválido.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Cód. Ativo não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         carteira = UsuarioCarteira.get_by_usuario(id_usuario=id_usuario, id=int(id_portfolio))
#
#         if not carteira:
#             return make_response(get_json_retorno_metodo(msg='Portfólio não localizado.'), 200)
#
#         id_ativo = None
#         tipo_invest = ''
#
#         row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#         if row:
#             id_ativo = int(row.id)
#             tipo_invest = 'ACAO'
#
#         if not id_ativo:
#             row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'FII'
#
#         if not id_ativo:
#             row = ETFIndice.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'ETF'
#
#         if not id_ativo:
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'BDR'
#
#         if not id_ativo:
#             row = CriptoEmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'CRIPTO'
#
#         if not id_ativo:
#             return make_response(get_json_retorno_metodo(msg='Código não localizado.'), 200)
#
#         if str(tipo_invest) == 'ACAO':
#             row = UsuarioCarteiraAcao.buscar_por_ativo(id_usuario=id_usuario, id_ativo=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='Ação não localizada no Portfólio.'), 200)
#             if int(carteira.id) == int(row['IDCARTEIRA']): return make_response(get_json_retorno_metodo(msg='Ação já cadastrada para esse Portfólio.'), 200)
#             UsuarioCarteiraAcao.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(id_portfolio))
#
#         elif str(tipo_invest) == 'FII':
#             row = UsuarioCarteiraFii.buscar_por_ativo(id_usuario=id_usuario, id_fundo=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='FII não localizado no Portfólio.'), 200)
#             if int(carteira.id) == int(row['IDCARTEIRA']): return make_response(get_json_retorno_metodo(msg='FII já cadastrado para esse Portfólio.'), 200)
#             UsuarioCarteiraFii.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(id_portfolio))
#
#         elif str(tipo_invest) == 'ETF':
#             row = UsuarioCarteiraEtf.buscar_por_ativo(id_usuario=id_usuario, id_indice=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='ETF não localizado no Portfólio.'), 200)
#             if int(carteira.id) == int(row['IDCARTEIRA']): return make_response(get_json_retorno_metodo(msg='ETF já cadastrado para esse Portfólio.'), 200)
#             UsuarioCarteiraEtf.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(id_portfolio))
#
#         elif str(tipo_invest) == 'BDR':
#             row = UsuarioCarteiraBdr.buscar_por_ativo(id_usuario=id_usuario, id_bdr=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='BDR não localizada no Portfólio.'), 200)
#             if int(carteira.id) == int(row['IDCARTEIRA']): return make_response(get_json_retorno_metodo(msg='BDR já cadastrada para esse Portfólio.'), 200)
#             UsuarioCarteiraBdr.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(id_portfolio))
#
#         elif str(tipo_invest) == 'CRIPTO':
#             row = UsuarioCarteiraCripto.buscar_por_ativo(id_usuario=id_usuario, id_cripto=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='CRIPTO não localizada no Portfólio.'), 200)
#             if int(carteira.id) == int(row['IDCARTEIRA']): return make_response(get_json_retorno_metodo(msg='CRIPTO já cadastrada para esse Portfólio.'), 200)
#             UsuarioCarteiraCripto.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(id_portfolio))
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/salvarAtivoPrecoTeto', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_ativo_preco_teto():
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
#             codigo = data.get('CodAtivo')
#             preco_teto = data.get('Preco')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Id. Portfólio Inválido.'), 200)
#
#         id_ativo = None
#         tipo_invest = ''
#
#         row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#         if row:
#             id_ativo = int(row.id)
#             tipo_invest = 'ACAO'
#
#         if not id_ativo:
#             row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'FII'
#
#         if not id_ativo:
#             row = ETFIndice.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'ETF'
#
#         if not id_ativo:
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'BDR'
#
#         if not id_ativo:
#             row = CriptoEmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 id_ativo = int(row.id)
#                 tipo_invest = 'CRIPTO'
#
#         if not id_ativo:
#             return make_response(get_json_retorno_metodo(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         preco_teto = float(str(preco_teto).replace('.', '').replace(',', '.')) if preco_teto else 0.0
#
#         if tipo_invest == 'ACAO':
#             row = UsuarioCarteiraAcao.buscar_por_ativo(id_usuario=id_usuario, id_ativo=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='Açao não localizada no Portfólio.'), 200)
#             UsuarioCarteiraAcao.atualizar_preco_teto(id=int(row['ID']), preco_teto=float(preco_teto))
#
#         elif tipo_invest == 'FII':
#             row = UsuarioCarteiraFii.buscar_por_ativo(id_usuario=id_usuario, id_fundo=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='FII não localizado no Portfólio.'), 200)
#             UsuarioCarteiraFii.atualizar_preco_teto(id=int(row['ID']), preco_teto=float(preco_teto))
#
#         elif tipo_invest == 'ETF':
#             row = UsuarioCarteiraEtf.buscar_por_ativo(id_usuario=id_usuario, id_indice=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='ETF não localizado no Portfólio.'), 200)
#             UsuarioCarteiraEtf.atualizar_preco_teto(id=int(row['ID']), preco_teto=float(preco_teto))
#
#         elif tipo_invest == 'BDR':
#             row = UsuarioCarteiraBdr.buscar_por_ativo(id_usuario=id_usuario, id_bdr=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='BDR não localizada no Portfólio.'), 200)
#             UsuarioCarteiraBdr.atualizar_preco_teto(id=int(row['ID']), preco_teto=float(preco_teto))
#
#         elif tipo_invest == 'CRIPTO':
#             row = UsuarioCarteiraCripto.buscar_por_ativo(id_usuario=id_usuario, id_cripto=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='CRIPTO não localizado no Portfólio.'), 200)
#             UsuarioCarteiraCripto.atualizar_preco_teto(id=int(row['ID']), preco_teto=float(preco_teto))
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/excluirAtivo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir_ativo():
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
#             id_portfolio = data.get('IdPortfolio')
#             id_ativo = data.get('IdAtivo')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_portfolio: return make_response(get_json_retorno_metodo(msg='Id. Portfólio Inválido.'), 200)
#         if not id_ativo: return make_response(get_json_retorno_metodo(msg='Id. Ativo Inválido.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Cód. Ativo não informado.'), 200)
#
#         tipo_invest = ''
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo)): tipo_invest = 'ACAO'
#         if not tipo_invest:
#             if FiiFundoImob.get_by_codigo(codigo=str(codigo)): tipo_invest = 'FII'
#         if not tipo_invest:
#             if ETFIndice.get_by_codigo(codigo=str(codigo)): tipo_invest = 'ETF'
#         if not tipo_invest:
#             if BDREmpresa.get_by_codigo(codigo=str(codigo)): tipo_invest = 'BDR'
#         if not tipo_invest:
#             if CriptoEmpresa.get_by_codigo(codigo=str(codigo)): tipo_invest = 'CRIPTO'
#         if not tipo_invest:
#             return make_response(get_json_retorno_metodo(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         carteira_atual = UsuarioCarteira.get_by_usuario(id_usuario=id_usuario, id=int(id_portfolio))
#         if not carteira_atual:
#             return make_response(get_json_retorno_metodo(msg='Portfólio não localizado.'), 200)
#
#         carteira_default = UsuarioCarteira.buscar_por_tipo_default(id_usuario=id_usuario)
#         if not carteira_default:
#             return make_response(get_json_retorno_metodo(msg='Portfólio Principal não localizado.'), 200)
#
#         if tipo_invest == 'ACAO':
#             if not ACAOEmpresaAtivo.get_by_id(id=int(id_ativo)): return make_response(get_json_retorno_metodo(msg='Ação não localizada.'), 200)
#             row = UsuarioCarteiraAcao.buscar_por_ativo(id_usuario=id_usuario, id_ativo=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='Ação não localizada no Portfólio.'), 200)
#             UsuarioCarteiraAcao.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(carteira_default['ID']))
#
#         elif tipo_invest == 'FII':
#             if not FiiFundoImob.get_by_id(id=int(id_ativo)): return make_response(get_json_retorno_metodo(msg='FII não localizado.'), 200)
#             row = UsuarioCarteiraFii.buscar_por_ativo(id_usuario=id_usuario, id_fundo=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='FII não localizado no Portfólio.'), 200)
#             UsuarioCarteiraFii.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(carteira_default['ID']))
#
#         elif tipo_invest == 'ETF':
#             if not ETFIndice.get_by_id(id=int(id_ativo)): return make_response(get_json_retorno_metodo(msg='ETF não localizado.'), 200)
#             row = UsuarioCarteiraEtf.buscar_por_ativo(id_usuario=id_usuario, id_indice=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='ETF não localizado no Portfólio.'), 200)
#             UsuarioCarteiraEtf.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(carteira_default['ID']))
#
#         elif tipo_invest == 'BDR':
#             if not BDREmpresa.get_by_id(id=int(id_ativo)): return make_response(get_json_retorno_metodo(msg='BDR não localizada.'), 200)
#             row = UsuarioCarteiraBdr.buscar_por_ativo(id_usuario=id_usuario, id_bdr=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='BDR não localizada no Portfólio.'), 200)
#             UsuarioCarteiraBdr.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(carteira_default['ID']))
#
#         elif tipo_invest == 'CRIPTO':
#             if not CriptoEmpresa.get_by_id(id=int(id_ativo)): return make_response(get_json_retorno_metodo(msg='CRIPTO não localizada.'), 200)
#             row = UsuarioCarteiraCripto.buscar_por_ativo(id_usuario=id_usuario, id_cripto=int(id_ativo))
#             if not row: return make_response(get_json_retorno_metodo(msg='CRIPTO não localizada no Portfólio.'), 200)
#             UsuarioCarteiraCripto.atualizar_id_carteira(id_usuario=id_usuario, id=int(row['ID']), id_portfolio=int(carteira_default['ID']))
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/carregarEmailInfo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_email_info():
#     try:
#         dados = dict({})
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/salvarEmailInfo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_email_info():
#     try:
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/gridsetores', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_setores():
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
#             id_portfolio = data.get('IdPortfolio')
#             tipo_invest = data.get('TipoInvest')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         id_usuario = current_user.id
#
#         lista_setor = []
#         lista_sub_setor = []
#         lista_segmento = []
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#
#             tipo = 'ST' # ST-Setor
#             setores = UsuarioCarteiraAcao.buscar_lista_setores(id_usuario=id_usuario, id_carteira=id_portfolio, tipo=tipo)
#             for setor in setores:
#                 tot_investido = 0.0
#                 rows = UsuarioCarteiraAcao.buscar_lista_ativos_setores(id_usuario=id_usuario, id_carteira=id_portfolio, id_setor=int(setor['ID']), tipo=tipo)
#                 for row in rows:
#                     quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                     quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                     quant_tot = float(quant) + float(quant_bonus)
#                     preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                     tot_investido += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.00 else 0.0
#                 lista_setor.append([str(setor['DESCRICAO']), decimal_to_str(valor=float(tot_investido))])
#
#             tipo = 'SS' # SS-SubSetor
#             setores = UsuarioCarteiraAcao.buscar_lista_setores(id_usuario=id_usuario, id_carteira=id_portfolio, tipo=tipo)
#             for setor in setores:
#                 tot_investido = 0.0
#                 rows = UsuarioCarteiraAcao.buscar_lista_ativos_setores(id_usuario=id_usuario, id_carteira=id_portfolio, id_setor=int(setor['ID']), tipo=tipo)
#                 for row in rows:
#                     quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                     quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                     quant_tot = float(quant) + float(quant_bonus)
#                     preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                     tot_investido += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.00 else 0.0
#                 lista_sub_setor.append([str(setor['DESCRICAO']), decimal_to_str(valor=float(tot_investido))])
#
#             tipo = 'SG' # SG-Segmento
#             setores = UsuarioCarteiraAcao.buscar_lista_setores(id_usuario=id_usuario, id_carteira=id_portfolio, tipo=tipo)
#             for setor in setores:
#                 tot_investido = 0.0
#                 rows = UsuarioCarteiraAcao.buscar_lista_ativos_setores(id_usuario=id_usuario, id_carteira=id_portfolio, id_setor=int(setor['ID']), tipo=tipo)
#                 for row in rows:
#                     quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#                     quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#                     quant_tot = float(quant) + float(quant_bonus)
#                     preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#                     tot_investido += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.00 else 0.0
#                 lista_segmento.append([str(setor['DESCRICAO']), decimal_to_str(valor=float(tot_investido))])
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             pass
#
#         if not tipo_invest or str(tipo_invest) == 'ETF':
#             pass
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             pass
#
#             # tipo = 'ST' # ST-Setor
#             # setores = UsuarioCarteiraBdr.buscar_lista_setores(id_usuario=id_usuario, id_carteira=id_portfolio, tipo=tipo)
#             # for setor in setores:
#             #     tot_investido = 0.0
#             #     rows = UsuarioCarteiraBdr.buscar_lista_ativos_setores(id_usuario=id_usuario, id_carteira=id_portfolio, id_setor=int(setor['ID']), tipo=tipo)
#             #     for row in rows:
#             #         quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#             #         quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#             #         quant_tot = float(quant) + float(quant_bonus)
#             #         preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#             #         tot_investido += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.00 else 0.0
#             #     lista_setor.append([str(setor['DESCRICAO']), decimal_to_str(valor=float(tot_investido))])
#             #
#             # tipo = 'SS' # SS-SubSetor
#             # setores = UsuarioCarteiraBdr.buscar_lista_setores(id_usuario=id_usuario, id_carteira=id_portfolio, tipo=tipo)
#             # for setor in setores:
#             #     tot_investido = 0.0
#             #     rows = UsuarioCarteiraBdr.buscar_lista_ativos_setores(id_usuario=id_usuario, id_carteira=id_portfolio, id_setor=int(setor['ID']), tipo=tipo)
#             #     for row in rows:
#             #         quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#             #         quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#             #         quant_tot = float(quant) + float(quant_bonus)
#             #         preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#             #         tot_investido += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.00 else 0.0
#             #     lista_sub_setor.append([str(setor['DESCRICAO']), decimal_to_str(valor=float(tot_investido))])
#             #
#             # tipo = 'SG' # SG-Segmento
#             # setores = UsuarioCarteiraBdr.buscar_lista_setores(id_usuario=id_usuario, id_carteira=id_portfolio, tipo=tipo)
#             # for setor in setores:
#             #     tot_investido = 0.0
#             #     rows = UsuarioCarteiraBdr.buscar_lista_ativos_setores(id_usuario=id_usuario, id_carteira=id_portfolio, id_setor=int(setor['ID']), tipo=tipo)
#             #     for row in rows:
#             #         quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#             #         quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#             #         quant_tot = float(quant) + float(quant_bonus)
#             #         preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#             #         tot_investido += (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.00 else 0.0
#             #     lista_segmento.append([str(setor['DESCRICAO']), decimal_to_str(valor=float(tot_investido))])
#
#         dados = dict({"Setor": lista_setor, "SubSetor": lista_sub_setor, "Segmento": lista_segmento})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/gridPorcentagem', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_porcentagem():
#     try:
#
#         lista = []
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_portfolio.route('/ListaNomePortfolio', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_nome_portfolio():
#     try:
#
#         lista = get_lista_nome_portfolio()
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# def get_lista_nome_portfolio():
#     try:
#
#         id_usuario = current_user.id
#
#         rows = UsuarioCarteira.buscar_lista_nome(id_usuario=id_usuario)
#
#         lista = [[str(row['ID']), str(row['DESCRICAO'])] for row in rows]
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return []
#
#
# @login_required
# @flask_optimize.optimize('json')
# # @tracing.trace()
# # @mp.profile
# @bp_portfolio.route('/DataSetPagina', methods=['GET', 'POST'])
# def data_set_pagina():
#     try:
#
#         # try:
#         #     id_usuario = current_user.id
#         # except Exception as e:
#         #     id_usuario = 2
#         #
#         # data = get_cache_portf(id_usuario=id_usuario)
#         # if not data:
#         #     data = get_json_data_set_pagina(id_usuario=id_usuario)
#         #     set_cache_portf(id_usuario=id_usuario, data=data)
#         # return make_response(data, 200)
#
#         return make_response(get_json_data_set_pagina(), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# def get_json_data_set_pagina(id_usuario: int = None, id_portfolio: str = None, tipo_invest: str = None):
#     try:
#
#         if not id_usuario: id_usuario = current_user.id
#
#         lista = []
#
#         # if not tipo_invest or str(tipo_invest) == 'ACAO':
#         #     rows = get_json_data_set_pagina_acao(id_usuario=id_usuario, id_portfolio=id_portfolio)
#         #     if rows: lista += rows
#         # if not tipo_invest or str(tipo_invest) == 'FII':
#         #     rows = get_json_data_set_pagina_fii(id_usuario=id_usuario, id_portfolio=id_portfolio)
#         #     if rows: lista += rows
#         # if not tipo_invest or str(tipo_invest) == 'ETF':
#         #     rows = get_json_data_set_pagina_eft(id_usuario=id_usuario, id_portfolio=id_portfolio)
#         #     if rows: lista += rows
#         # if not tipo_invest or str(tipo_invest) == 'BDR':
#         #     rows = get_json_data_set_pagina_bdr(id_usuario=id_usuario, id_portfolio=id_portfolio)
#         #     if rows: lista += rows
#         # if not tipo_invest or str(tipo_invest) == 'CRIPTO':
#         #     rows = get_json_data_set_pagina_cripto(id_usuario=id_usuario, id_portfolio=id_portfolio)
#         #     if rows: lista += rows
#
#         loop = asyncio.new_event_loop()  # get_event_loop
#         try:
#             asyncio.set_event_loop(loop)
#             tasks = [asyncio.Task(get_json_data_set_pagina_acao_async(id_usuario=id_usuario, id_portfolio=id_portfolio)),
#                      asyncio.Task(get_json_data_set_pagina_fii_async(id_usuario=id_usuario, id_portfolio=id_portfolio)),
#                      asyncio.Task(get_json_data_set_pagina_eft_async(id_usuario=id_usuario, id_portfolio=id_portfolio)),
#                      asyncio.Task(get_json_data_set_pagina_bdr_async(id_usuario=id_usuario, id_portfolio=id_portfolio)),
#                      asyncio.Task(get_json_data_set_pagina_cripto_async(id_usuario=id_usuario, id_portfolio=id_portfolio)),
#                      ]
#             results = loop.run_until_complete(asyncio.gather(*tasks))
#         finally:
#             try:
#                 loop.close()
#             except:
#                 pass
#
#         if results[0]: lista += results[0] # acao
#         if results[1]: lista += results[1] # fii
#         if results[2]: lista += results[2] # eft
#         if results[3]: lista += results[3] # bdr
#         if results[4]: lista += results[4] # cripto
#
#         return get_json_retorno_grid(rslt='OK', lista=lista)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e)))
#
# @asyncio.coroutine
# async def get_json_data_set_pagina_acao_async(id_usuario: int = None, id_portfolio: str = None) -> []:
#     return get_json_data_set_pagina_acao(id_usuario=id_usuario, id_portfolio=id_portfolio)
#
# def get_json_data_set_pagina_acao(id_usuario: int = None, id_portfolio: str = None) -> []:
#     try:
#
#         lista = []
#         data_atual = pegar_data_atual()
#         ano_atual = pegar_data_atual(fmt='%Y')
#         data_inicio = str(int(ano_atual)- 1) + pegar_data_atual(fmt='%m%d')
#
#         # print(dt.datetime.now(), 'ACAO - QUERY - INICIO')
#         # start = time.time()
#
#         rows = UsuarioCarteiraAcao.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'ACAO - QUERY - FIM', diff)
#         #
#         # print(dt.datetime.now(), 'ACAO - LOOP - INICIO')
#         # start = time.time()
#
#         for row in rows:
#             id_ativo = int(row['IDATIVO'])
#             quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#             quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#             quant_tot = float(quant) + float(quant_bonus)
#             preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#             preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#             preco_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#             perc_valorz_dia = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#             preco_valorz_dia = float(preco_atual) - float(preco_anterior)
#             preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#             tot_invest = (int(quant_tot) * float(preco_medio)) if int(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#             tot_atual = (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#             tot_valorz = float(tot_atual) - float(tot_invest)
#             perc_valorz = 0.0
#             if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#             if float(tot_valorz) != 0.00 and float(tot_invest) == 0.0 and int(quant_bonus) > 0 and float(preco_medio) > 0.0: perc_valorz = (float(tot_valorz) / (int(quant_bonus) * float(preco_medio))) * 100
#             tot_alug = UsuarioACAOEmpresaAluguel.buscar_vlr_total(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(ano_atual) + '1231')
#             tot_prov = UsuarioACAOEmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(data_atual))
#             dt_fim = UsuarioACAOEmpresaProvento.buscar_maior_data_ex(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(data_atual))
#             prec_prov = UsuarioACAOEmpresaProvento.buscar_vlr_preco_ex(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_ini=str(data_inicio), dt_fim=str(dt_fim))
#             preco_medio_yoc = UsuarioACAOEmpresaOperacao.buscar_preco_medio_antes(id_usuario=id_usuario, id_ativo=int(id_ativo), dt_fim=str(dt_fim))
#             yield_on_cost = ((float(prec_prov) / float(preco_medio_yoc)) * 100) if float(preco_medio_yoc) > 0.0 and float(prec_prov) > 0.0 else 0.0
#             lista.append({
#                 "CartId": str(row['IDCARTEIRA']),
#                 "CartNome": str(row['DESCRICAOCARTEIRA']),
#                 "SetorId": str(row['IDSETOR']),
#                 "SetorNome": str(row['DESCRICAOSETOR']),
#                 "SubSetorId": str(row['IDSUBSETOR']),
#                 "SubSetorNome": str(row['DESCRICAOSUBSETOR']),
#                 "SegmentoId": str(row['IDSEGMENTO']),
#                 "SegmentoNome": str(row['DESCRICAOSEGMENTO']),
#                 "AtvId": str(id_ativo),
#                 "AtvTipoInvest": 'ACAO',
#                 "AtvCodigo": str(row['CODIGOATIVO']),
#                 "AtvQtde": inteiro_to_str(valor=float(quant_tot)),
#                 "AtvPrecoMedio": decimal_to_str(valor=float(preco_medio)),
#                 "AtvPrecoAtual": decimal_to_str(valor=float(preco_atual)),
#                 "AtvPrecoTeto": decimal_to_str(valor=float(preco_teto)),
#                 "AtvVlrValorizDia": decimal_to_str(valor=float(preco_valorz_dia)),
#                 "AtvPercValorizDia": decimal_to_str(valor=abs(float(perc_valorz_dia))),
#                 "AtvTotInvest": decimal_to_str(valor=float(tot_invest)),
#                 "AtvTotAtual": decimal_to_str(valor=float(tot_atual)),
#                 "AtvTotValoriz": decimal_to_str(valor=float(tot_valorz)),
#                 "AtvPercValoriz": decimal_to_str(valor=float(perc_valorz)),
#                 "AtvTotProv": decimal_to_str(valor=float(tot_prov)),
#                 "AtvTotAlug": decimal_to_str(valor=float(tot_alug)),
#                 "AtvYieldOnCost": decimal_to_str(valor=float(yield_on_cost))
#             })
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'ACAO - LOOP - FIM', diff)
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e)))
#
# @asyncio.coroutine
# async def get_json_data_set_pagina_fii_async(id_usuario: int = None, id_portfolio: str = None) -> []:
#     return get_json_data_set_pagina_fii(id_usuario=id_usuario, id_portfolio=id_portfolio)
#
# def get_json_data_set_pagina_fii(id_usuario: int = None, id_portfolio: str = None) -> []:
#     try:
#
#         lista = []
#         data_atual = pegar_data_atual()
#         ano_atual = pegar_data_atual(fmt='%Y')
#         data_inicio = str(int(ano_atual)- 1) + pegar_data_atual(fmt='%m%d')
#
#         # print(dt.datetime.now(), 'FII - QUERY - INICIO')
#         # start = time.time()
#
#         rows = UsuarioCarteiraFii.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'FII - QUERY - FIM', diff)
#         #
#         # print(dt.datetime.now(), 'FII - LOOP - INICIO')
#         # start = time.time()
#
#         for row in rows:
#             id_fundo = int(row['IDFUNDO'])
#             quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#             quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#             quant_tot = float(quant) + float(quant_bonus)
#             preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#             preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#             preco_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#             perc_valorz_dia = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#             preco_valorz_dia = float(preco_atual) - float(preco_anterior)
#             preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#             tot_invest = (int(quant_tot) * float(preco_medio)) if int(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#             tot_atual = (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#             tot_valorz = float(tot_atual) - float(tot_invest)
#             perc_valorz = 0.0
#             if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#             if float(tot_valorz) != 0.00 and float(tot_invest) == 0.0 and int(quant_bonus) > 0 and float(preco_medio) > 0.0: perc_valorz = (float(tot_valorz) / (int(quant_bonus) * float(preco_medio))) * 100
#             tot_alug = 0.0
#             tot_prov = UsuarioFiiFundoImobProvento.buscar_vlr_total(id_usuario=id_usuario, id_fundo=int(id_fundo), dt_fim=str(data_atual))
#             dt_fim = UsuarioFiiFundoImobProvento.buscar_maior_data_ex(id_usuario=id_usuario, id_fundo=int(id_fundo), dt_fim=str(data_atual))
#             prec_prov = UsuarioFiiFundoImobProvento.buscar_vlr_preco_ex(id_usuario=id_usuario, id_fundo=int(id_fundo), dt_ini=str(data_inicio), dt_fim=str(dt_fim))
#             preco_medio_yoc = UsuarioFiiFundoImobLancamento.buscar_preco_medio_antes(id_usuario=id_usuario, id_fundo=int(id_fundo), dt_fim=str(dt_fim))
#             yield_on_cost = ((float(prec_prov) / float(preco_medio_yoc)) * 100) if float(preco_medio_yoc) > 0.0 and float(prec_prov) > 0.0 else 0.0
#             lista.append({
#                 "CartId": str(row['IDCARTEIRA']),
#                 "CartNome": str(row['DESCRICAOCARTEIRA']),
#                 "SetorId": '1',
#                 "SetorNome": 'FII',
#                 "SubSetorId": '1',
#                 "SubSetorNome": 'FII',
#                 "SegmentoId": '1',
#                 "SegmentoNome": 'FII',
#                 "AtvId": str(id_fundo),
#                 "AtvTipoInvest": 'FII',
#                 "AtvCodigo": str(row['CODIGOFUNDO']),
#                 "AtvQtde": inteiro_to_str(valor=float(quant_tot)),
#                 "AtvPrecoMedio": decimal_to_str(valor=float(preco_medio)),
#                 "AtvPrecoAtual": decimal_to_str(valor=float(preco_atual)),
#                 "AtvPrecoTeto": decimal_to_str(valor=float(preco_teto)),
#                 "AtvVlrValorizDia": decimal_to_str(valor=float(preco_valorz_dia)),
#                 "AtvPercValorizDia": decimal_to_str(valor=abs(float(perc_valorz_dia))),
#                 "AtvTotInvest": decimal_to_str(valor=float(tot_invest)),
#                 "AtvTotAtual": decimal_to_str(valor=float(tot_atual)),
#                 "AtvTotValoriz": decimal_to_str(valor=float(tot_valorz)),
#                 "AtvPercValoriz": decimal_to_str(valor=float(perc_valorz)),
#                 "AtvTotProv": decimal_to_str(valor=float(tot_prov)),
#                 "AtvTotAlug": decimal_to_str(valor=float(tot_alug)),
#                 "AtvYieldOnCost": decimal_to_str(valor=float(yield_on_cost))
#             })
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'FII - LOOP - FIM', diff)
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e)))
#
# @asyncio.coroutine
# async def get_json_data_set_pagina_eft_async(id_usuario: int = None, id_portfolio: str = None) -> []:
#     return get_json_data_set_pagina_eft(id_usuario=id_usuario, id_portfolio=id_portfolio)
#
# def get_json_data_set_pagina_eft(id_usuario: int = None, id_portfolio: str = None) -> []:
#     try:
#
#         lista = []
#         data_atual = pegar_data_atual()
#         ano_atual = pegar_data_atual(fmt='%Y')
#         data_inicio = str(int(ano_atual)- 1) + pegar_data_atual(fmt='%m%d')
#
#         # print(dt.datetime.now(), 'ETF - QUERY - INICIO')
#         # start = time.time()
#
#         rows = UsuarioCarteiraEtf.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'ETF - QUERY - FIM', diff)
#         #
#         # print(dt.datetime.now(), 'ETF - LOOP - INICIO')
#         # start = time.time()
#
#         for row in rows:
#             id_indice = int(row['IDINDICE'])
#             quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#             quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#             quant_tot = float(quant) + float(quant_bonus)
#             preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#             preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#             preco_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#             perc_valorz_dia = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#             preco_valorz_dia = float(preco_atual) - float(preco_anterior)
#             preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#             tot_invest = (int(quant_tot) * float(preco_medio)) if int(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#             tot_atual = (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#             tot_valorz = float(tot_atual) - float(tot_invest)
#             perc_valorz = 0.0
#             if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#             if float(tot_valorz) != 0.00 and float(tot_invest) == 0.0 and int(quant_bonus) > 0 and float(preco_medio) > 0.0: perc_valorz = (float(tot_valorz) / (int(quant_bonus) * float(preco_medio))) * 100
#             tot_alug = 0.0
#             tot_prov = 0.0
#             yield_on_cost = 0.0
#             lista.append({
#                 "CartId": str(row['IDCARTEIRA']),
#                 "CartNome": str(row['DESCRICAOCARTEIRA']),
#                 "SetorId": '1',
#                 "SetorNome": 'ETF',
#                 "SubSetorId": '1',
#                 "SubSetorNome": 'ETF',
#                 "SegmentoId": '1',
#                 "SegmentoNome": 'ETF',
#                 "AtvId": str(id_indice),
#                 "AtvTipoInvest": 'ETF',
#                 "AtvCodigo": str(row['CODIGOINDICE']),
#                 "AtvQtde": inteiro_to_str(valor=float(quant_tot)),
#                 "AtvPrecoMedio": decimal_to_str(valor=float(preco_medio)),
#                 "AtvPrecoAtual": decimal_to_str(valor=float(preco_atual)),
#                 "AtvPrecoTeto": decimal_to_str(valor=float(preco_teto)),
#                 "AtvVlrValorizDia": decimal_to_str(valor=float(preco_valorz_dia)),
#                 "AtvPercValorizDia": decimal_to_str(valor=abs(float(perc_valorz_dia))),
#                 "AtvTotInvest": decimal_to_str(valor=float(tot_invest)),
#                 "AtvTotAtual": decimal_to_str(valor=float(tot_atual)),
#                 "AtvTotValoriz": decimal_to_str(valor=float(tot_valorz)),
#                 "AtvPercValoriz": decimal_to_str(valor=float(perc_valorz)),
#                 "AtvTotProv": decimal_to_str(valor=float(tot_prov)),
#                 "AtvTotAlug": decimal_to_str(valor=float(tot_alug)),
#                 "AtvYieldOnCost": decimal_to_str(valor=float(yield_on_cost)),
#             })
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'ETF - LOOP - FIM', diff)
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e)))
#
# @asyncio.coroutine
# async def get_json_data_set_pagina_bdr_async(id_usuario: int = None, id_portfolio: str = None) -> []:
#     return get_json_data_set_pagina_bdr(id_usuario=id_usuario, id_portfolio=id_portfolio)
#
# def get_json_data_set_pagina_bdr(id_usuario: int = None, id_portfolio: str = None) -> []:
#     try:
#
#         lista = []
#         data_atual = pegar_data_atual()
#         ano_atual = pegar_data_atual(fmt='%Y')
#         data_inicio = str(int(ano_atual)- 1) + pegar_data_atual(fmt='%m%d')
#
#         # print(dt.datetime.now(), 'BDR - QUERY - INICIO')
#         # start = time.time()
#
#         rows = UsuarioCarteiraBdr.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'BDR - QUERY - FIM', diff)
#         #
#         # print(dt.datetime.now(), 'BDR - LOOP - INICIO')
#         # start = time.time()
#
#         for row in rows:
#             id_ativo = int(row['IDBDR'])
#             quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#             quant_bonus = float(row['QUANTBONUS']) if row['QUANTBONUS'] and float(row['QUANTBONUS']) > 0.0 else 0.0
#             quant_tot = float(quant) + float(quant_bonus)
#             preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#             preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#             preco_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#             perc_valorz_dia = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#             preco_valorz_dia = float(preco_atual) - float(preco_anterior)
#             preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#             tot_invest = (int(quant_tot) * float(preco_medio)) if int(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#             tot_atual = (int(quant_tot) * float(preco_atual)) if int(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#             tot_valorz = float(tot_atual) - float(tot_invest)
#             perc_valorz = 0.0
#             if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#             if float(tot_valorz) != 0.00 and float(tot_invest) == 0.0 and int(quant_bonus) > 0 and float(preco_medio) > 0.0: perc_valorz = (float(tot_valorz) / (int(quant_bonus) * float(preco_medio))) * 100
#             tot_alug = 0.0
#             tot_prov = UsuarioBDREmpresaProvento.buscar_vlr_total(id_usuario=id_usuario, id_bdr=int(id_ativo), dt_fim=str(data_atual))
#             dt_fim = UsuarioBDREmpresaProvento.buscar_maior_data_ex(id_usuario=id_usuario, id_bdr=int(id_ativo), dt_fim=str(data_atual))
#             prec_prov = UsuarioBDREmpresaProvento.buscar_vlr_preco_ex(id_usuario=id_usuario, id_bdr=int(id_ativo), dt_ini=str(data_inicio), dt_fim=str(dt_fim))
#             preco_medio_yoc = UsuarioBDREmpresaOperacao.buscar_preco_medio_antes(id_usuario=id_usuario, id_bdr=int(id_ativo), dt_fim=str(dt_fim))
#             yield_on_cost = ((float(prec_prov) / float(preco_medio_yoc)) * 100) if float(preco_medio_yoc) > 0.0 and float(prec_prov) > 0.0 else 0.0
#             lista.append({
#                 "CartId": str(row['IDCARTEIRA']),
#                 "CartNome": str(row['DESCRICAOCARTEIRA']),
#                 "SetorId": str(row['IDSETOR']),
#                 "SetorNome": str(row['DESCRICAOSETOR']),
#                 "SubSetorId": str(row['IDSUBSETOR']),
#                 "SubSetorNome": str(row['DESCRICAOSUBSETOR']),
#                 "SegmentoId": str(row['IDSEGMENTO']),
#                 "SegmentoNome": str(row['DESCRICAOSEGMENTO']),
#                 "AtvId": str(id_ativo),
#                 "AtvTipoInvest": 'BDR',
#                 "AtvCodigo": str(row['CODIGOBDR']),
#                 "AtvQtde": inteiro_to_str(valor=float(quant_tot)),
#                 "AtvPrecoMedio": decimal_to_str(valor=float(preco_medio)),
#                 "AtvPrecoAtual": decimal_to_str(valor=float(preco_atual)),
#                 "AtvPrecoTeto": decimal_to_str(valor=float(preco_teto)),
#                 "AtvVlrValorizDia": decimal_to_str(valor=float(preco_valorz_dia)),
#                 "AtvPercValorizDia": decimal_to_str(valor=abs(float(perc_valorz_dia))),
#                 "AtvTotInvest": decimal_to_str(valor=float(tot_invest)),
#                 "AtvTotAtual": decimal_to_str(valor=float(tot_atual)),
#                 "AtvTotValoriz": decimal_to_str(valor=float(tot_valorz)),
#                 "AtvPercValoriz": decimal_to_str(valor=float(perc_valorz)),
#                 "AtvTotProv": decimal_to_str(valor=float(tot_prov)),
#                 "AtvTotAlug": decimal_to_str(valor=float(tot_alug)),
#                 "AtvYieldOnCost": decimal_to_str(valor=float(yield_on_cost))
#             })
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'BDR - LOOP - FIM', diff)
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e)))
#
# @asyncio.coroutine
# async def get_json_data_set_pagina_cripto_async(id_usuario: int = None, id_portfolio: str = None) -> []:
#     return get_json_data_set_pagina_cripto(id_usuario=id_usuario, id_portfolio=id_portfolio)
#
# def get_json_data_set_pagina_cripto(id_usuario: int = None, id_portfolio: str = None) -> []:
#     try:
#
#         lista = []
#         data_atual = pegar_data_atual()
#         ano_atual = pegar_data_atual(fmt='%Y')
#         data_inicio = str(int(ano_atual)- 1) + pegar_data_atual(fmt='%m%d')
#
#         # print(dt.datetime.now(), 'CRIPTO - QUERY - INICIO')
#         # start = time.time()
#
#         rows = UsuarioCarteiraCripto.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'CRIPTO - QUERY - FIM', diff)
#         #
#         # print(dt.datetime.now(), 'CRIPTO - LOOP - INICIO')
#         # start = time.time()
#
#         for row in rows:
#             id_cripto = int(row['IDCRIPTO'])
#             quant = float(row['QUANT']) if row['QUANT'] and float(row['QUANT']) > 0.0 else 0.0
#             quant_tot = float(quant)
#             preco_medio = float(row['VLRPRECOMEDIO']) if row['VLRPRECOMEDIO'] and float(row['VLRPRECOMEDIO']) > 0.0 else 0.0
#             preco_atual = float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#             preco_anterior = float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] and float(row['VLRPRECOANTERIOR']) > 0.0 else 0.0
#             perc_valorz_dia = float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0
#             preco_valorz_dia = float(preco_atual) - float(preco_anterior)
#             preco_teto = float(row['VLRPRECOTETO']) if row['VLRPRECOTETO'] and float(row['VLRPRECOTETO']) > 0.0 else 0.0
#             tot_invest = (float(quant_tot) * float(preco_medio)) if float(quant) > 0 and float(preco_medio) > 0.00 else 0.0
#             tot_atual = (float(quant_tot) * float(preco_atual)) if float(quant_tot) > 0 and float(preco_atual) > 0.0 else 0.0
#             tot_valorz = float(tot_atual) - float(tot_invest)
#             perc_valorz = 0.0
#             if float(tot_valorz) != 0.00 and float(tot_invest) > 0.0: perc_valorz = (float(tot_valorz) / float(tot_invest)) * 100
#             tot_alug = 0.0
#             tot_prov = 0.0
#             yield_on_cost = 0.0
#             lista.append({
#                 "CartId": str(row['IDCARTEIRA']),
#                 "CartNome": str(row['DESCRICAOCARTEIRA']),
#                 "SetorId": '1',
#                 "SetorNome": 'CRIPTO',
#                 "SubSetorId": '1',
#                 "SubSetorNome": 'CRIPTO',
#                 "SegmentoId": '1',
#                 "SegmentoNome": 'CRIPTO',
#                 "AtvId": str(id_cripto),
#                 "AtvTipoInvest": 'CRIPTO',
#                 "AtvCodigo": str(row['CODIGOCRIPTO']),
#                 "AtvQtde": decimal_cripto_curto_to_str(valor=float(quant_tot)),
#                 "AtvPrecoMedio": decimal_cripto_curto_to_str(valor=float(preco_medio)),
#                 "AtvPrecoAtual": decimal_cripto_curto_to_str(valor=float(preco_atual)),
#                 "AtvPrecoTeto": decimal_cripto_curto_to_str(valor=float(preco_teto)),
#                 "AtvVlrValorizDia": decimal_to_str(valor=float(preco_valorz_dia)),
#                 "AtvPercValorizDia": decimal_to_str(valor=abs(float(perc_valorz_dia))),
#                 "AtvTotInvest": decimal_to_str(valor=float(tot_invest)),
#                 "AtvTotAtual": decimal_to_str(valor=float(tot_atual)),
#                 "AtvTotValoriz": decimal_to_str(valor=float(tot_valorz)),
#                 "AtvPercValoriz": decimal_to_str(valor=float(perc_valorz)),
#                 "AtvTotProv": decimal_to_str(valor=float(tot_prov)),
#                 "AtvTotAlug": decimal_to_str(valor=float(tot_alug)),
#                 "AtvYieldOnCost": decimal_to_str(valor=float(yield_on_cost))
#             })
#
#         # diff = int((time.time() - start) * 1000)
#         # print(dt.datetime.now(), 'CRIPTO - LOOP - FIM', diff)
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e)))