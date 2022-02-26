# -*- coding: utf-8 -*-
import sys
import os
from time import perf_counter
import pandas as pd
import fastapi as _fastapi
# from flask_login import login_required, current_user
# from app.banco import db
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.util.util_json import get_json_retorno_grid
# from app.util.util_datahora import pegar_data_atual
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="/admin/testes", tags=['admim_testes'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
# @login_required
# @flask_optimize.optimize(cache='GET-1')  # 84600seg/1410Min/23,5Hr
async def get_index(request: _fastapi.Request):
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


#     if str(current_user.tipo) != 'A':
#         return redirect(location=url_for('principal.index'))
#
#     lista = []
#
#     id_usuario = current_user.id
#
#     # PASSO 01: BUSCAR TODOS OS LANÇAMENTOS
#
#     query = " SELECT O.DATA, A.CODIGO, O.TIPO, O.QUANT AS QTD, O.VLRCUSTO AS PRECO FROM TBLANCAMENTO O JOIN TBEMPRESA_ATIVO A ON ( A.ID = O.IDATIVO ) WHERE O.IDUSUARIO = " + str(id_usuario) + " ORDER BY O.DATA, O.TIPO, O.ID "
#     trades = pd.read_sql(query, db.engine.connect().connection)
#     trades.sort_values(by=['CODIGO', 'DATA'], inplace=True, kind='quicksort')
#     trades['QTD'] = trades.apply(lambda x: float(x.QTD) * -1 if str(x.TIPO) == 'V' else float(x.QTD), axis=1)
#     trades.drop(['TIPO'], axis=1, inplace=True)
#
#     # ######################################################
#     # ######################################################
#     # SOMENTE PARA TESTE
#     trades = trades.loc[trades['CODIGO'] == 'ITSA4']
#     # ######################################################
#     # ######################################################
#
#     # PASSO 02: BUSCAR TODAS os CODIGOS
#
#     codigos = trades[['CODIGO']].drop_duplicates()
#
#     # PASSO 03: BUSCAR TODAS AS COTAÇOES
#
#     precos = pd.DataFrame()
#     for row in codigos.itertuples():
#         codigo = row.CODIGO
#
#         trade = trades.loc[trades['CODIGO'] == codigo]
#         dt_ini = trade['DATA'].min()
#         dt_fim = pegar_data_atual(fmt="%Y%m%d")
#
#         query = " SELECT C.DATA, '" + codigo + "' AS CODIGO, C.COTACAO, C.VARIACAO FROM TBEMPRESA_ATIVOCOTACAO_" + codigo + " C WHERE C.DATA >= " + dt_ini + " AND C.DATA <= " + dt_fim + " ORDER BY C.DATA "
#         preco = pd.read_sql(query, db.engine.connect().connection)
#         precos = precos.append(preco)
#
#         del preco
#         del trade
#
#     # PASSO 04: CRIAR A LISTA DE DATAS - MENOR DATA ATE DATA ATUAL
#
#     start = trades['DATA'].min()
#     end = pegar_data_atual(fmt="%Y%m%d")
#     dates = pd.date_range(start=dt_ini, end=dt_fim)
#
#     # PASSO 05: CRIAR A CARTERIA
#
#     carteiras = pd.DataFrame()
#
#     for row in codigos.itertuples():
#         codigo = row.CODIGO
#
#         # PASSO 06: BUSCAR AS COTACOES SOMENTE DE UM DETERMINADO ATIVO
#
#         preco = precos.loc[precos['CODIGO'] == codigo].copy()
#         preco.drop(['CODIGO'], axis=1, inplace=True)
#         preco.set_index('DATA', inplace=True)
#
#         # PASSO 07: BUSCAR AS LANCAMENTOS SOMENTE DE UM DETERMINADO ATIVO
#
#         trade = trades.loc[trades['CODIGO'] == codigo].copy()
#         trade.set_index('DATA', inplace=True)
#         # trade = trade.join(preco, how='outer')
#
#         # PASSO 08: CRIAR A CARTEIRA SOMENTE DE UM DETERMINADO ATIVO
#
#         carteira = pd.DataFrame(index=dates)
#         carteira['DATA'] = carteira.index.map(lambda x: str(x.strftime("%Y%m%d")))
#         carteira.set_index('DATA', inplace=True)
#         carteira = carteira.join(trade, how='outer')
#         carteira = carteira.join(preco, how='outer')
#         carteira.dropna(axis=0, how='all', inplace=True)
#         carteira["QTD"].fillna(0.0, inplace=True)
#         carteira['QTD_ACUM'] = carteira['QTD'].cumsum()
#         carteira["PRECO"].fillna(0.0, inplace=True)
#         carteira['CODIGO'] = codigo
#         carteira['VLR_INVEST'] = carteira['QTD'] * carteira['PRECO']
#         carteira['INVESTIMENTO'] = carteira['VLR_INVEST'].cumsum()
#         carteira['PATRIMONIO'] = carteira['QTD_ACUM'] * carteira['COTACAO']
#         # carteira['QTD_COTA_ATUAL'] = 0.0
#         # carteira['VLR_COTA_ATUAL'] = 0.0
#         # carteira['PERC_COTA_ATUAL'] = 0.0
#         carteira.reset_index(drop=False, inplace=True)
#
#         # qtd_cota_atual = 0.0
#         # vlr_cota_atual = 0.0
#         # vlr_cota_anterior = 0.0
#         # perc_cota_atual = 0.0
#         #
#         # for indx, row in enumerate(carteira.itertuples()):  # for indx, row in carteira.iterrows():
#         #
#         #     qtd_acumulada = float(row.QTD_ACUM) if row.QTD_ACUM else 0.0
#         #     vlr_cotacao = float(row.COTACAO) if row.COTACAO else 0.0
#         #     vlr_invest = float(row.VLR_INVEST)  # VALOR INVESTIDO NO MES
#         #     vlr_tot_atual = (qtd_acumulada * vlr_cotacao) if qtd_acumulada != 0.0 and vlr_cotacao > 0.0 else 0.00  # TOAL ATUAL
#
#         '''
#
#                     trades_qtd = pd.pivot_table(arqv, values='quantidade', index=['data'], columns=arqv['ativo'].str.upper(), aggfunc=np.sum, fill_value=0)
#                     trades_precos = pd.pivot_table(arqv, values='preço',  index=['data'], columns=arqv['ativo'].str.upper(), fill_value=0.0)
#                     aportes = (trades * trades_precos).sum(axis=1)
#                     posicao = trades.cumsum()
#                     carteira = posicao *  precos
#                     carteira['saldo'] = carteira.sum(axis=1)
#
#                     for i, data in enumerate(aportes.index): loop por data
#                       if i == 0:
#                           carteira.at[data, 'vlr_cota'] = 1
#                           carteira.at[data, 'qtd_cotas'] = carteira.loc[data]['saldo'].copy()
#                       else:
#                           if aportes[data] != 0.0:
#                               carteira.at[data, 'qtd_cotas'] = carteira.iloc[i-1]['qtd_cotas'] + (aportes[data] / carteira.iloc[i-1]['vlr_cota'])
#                           else:
#                               carteira.at[data, 'qtd_cotas'] = carteira.iloc[i-1]['qtd_cotas']
#                           carteira.at[data, 'vlr_cota'] = carteira.iloc[i]['saldo'] / carteira.at[data, 'qtd_cotas']
#
#                           carteira.at[data, 'retorno'] = (carteira.iloc[i]['vlr_cota'] / carteira.iloc[i-1]['vlr_cota']) -1
#
#                     Data
#                     VlrInvest
#                     VlrCarteira
#                     VlrCota -  Valor da carteira divididos pelo número de cotas do dia anterior
#                     PctCota - valor da cota atual ÷ valor da cota do fim do ultim perido (ano anterior,mes anterior, dia anterior)
#                     QtdCota - número de cotas, valor da operação dividido pelo valor da cota anterior
#                     PctCotaMes
#                     PctCotaAno
#                     PctCotaAcum
#
#                 # Como calcular os retornos cumulativos do portfólio em Python
#                 tickers = ['BND', 'VB', 'VEA', 'VOO', 'VWO']
#                 wts = [0.1, 0.2, 0.25, 0.25, 0.2]
#                 price_data = web.get_data_yahoo(tickers, start='2013-01-01', end='2018-03-01')
#                 price_data = price_data['Adj Close']
#                 weighted_returns = (wts * ret_data)  # calcularemos a média ponderada dos retornos de nossos ativos.
#                 port_ret = weighted_returns.sum(axis=1)  # Finalmente, os retornos da carteira são a soma dos retornos ponderados.
#                 cumulative_ret = (port_ret + 1).cumprod()  # Para calcular os retornos cumulativos, precisamos usar a cumprod()função.
#                 fig = plt.figure()
#                 ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#                 ax1.plot(cumulative_ret)
#                 ax1.set_xlabel('Date')
#                 ax1.set_ylabel("Cumulative Returns")
#                 ax1.set_title("Portfolio Cumulative Returns")
#                 plt.show()
#
#                 # Como calcular o retorno do portfólio em Python - https://www.codingfinance.com/post/2018-04-05-portfolio-returns-py/
#                 # Títulos agregados ETF (BND) 10%
#                 # Small Cap ETF (VB) 20%
#                 # Mercados desenvolvidos ETF (VEA) 25%
#                 # S&P 500 ETF (VOO) 25%
#                 # Emerging Markets ETF (VWO) 20%
#                 symbols = ['VOO', 'VEA', 'VB', 'VWO', 'BND']
#                 price_data = web.get_data_yahoo(symbols, start='2010-01-01', end='2020-08-01')
#                 price_data = price_data['Adj Close']
#                 w = [0.1, 0.2, 0.25, 0.25, 0.2]
#                 ret_data = price_data.pct_change()[1:]
#                 weighted_returns = (w * ret_data)
#                 port_ret = weighted_returns.sum(axis=1)
#                 fig = plt.figure()
#                 ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#                 ax1.hist(port_ret, bins=60)
#                 ax1.set_xlabel('Portfolio returns')
#                 ax1.set_ylabel("Freq")
#                 ax1.set_title("Portfolio Returns calculated manually")
#                 plt.show()
#                 wts_table = pd.DataFrame({'symbol': symbols, 'wts': [0.25, 0.25, 0.2, 0.2, 0.1]})
#                 ret_data_tidy = pd.melt(ret_data.reset_index(), id_vars='Date', var_name='symbol', value_name='ret')
#                 ret_data_tidy_wts = pd.merge(ret_data_tidy, wts_table, on="symbol")
#                 ret_data_tidy_wts['wt_returns'] = ret_data_tidy_wts['ret'] * ret_data_tidy_wts['wts']
#                 port_ret_tidy = ret_data_tidy_wts.groupby("Date").sum()['wt_returns']
#                 diff = port_ret - port_ret_tidy
#                 fig = plt.figure()
#                 ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#                 ax1.hist(port_ret, bins=60)  # manually calculated returns
#                 ax1.set_xlabel('Portfolio returns')
#                 ax1.set_ylabel("Freq")
#                 ax1.set_title("Portfolio Returns calculated manually")
#                 plt.show()
#                 fig = plt.figure()
#                 ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#                 ax1.hist(port_ret_tidy, bins=60)  # Tidy returns
#                 ax1.set_xlabel('Portfolio returns')
#                 ax1.set_ylabel("Freq")
#                 ax1.set_title("Portfolio Returns calculated in Tidy format")
#                 plt.show()
#                 mean_ret = port_ret.mean()
#                 std_returns = port_ret.std()
#                 print(std_returns)
#
#         '''
#         #
#         #     if indx == 0 or qtd_acumulada == 0.0:
#         #         qtd_cota_atual = float(vlr_invest)  # valor investido no mes
#         #         vlr_cota_atual = float(1.0)
#         #     else:
#         #         if vlr_invest != 0.0:
#         #             qtd_cota_atual += float(vlr_invest) / float(vlr_cota_atual)  # qtd cota atual + ( total investido / valor da cota autal)
#         #         vlr_cota_atual = float(vlr_tot_atual) / float(qtd_cota_atual) if vlr_tot_atual > 0.0 else 0.0  # total atual / dividio pela qtd cota taul
#         #         perc_cota_atual = (float(vlr_cota_atual) / float(vlr_cota_anterior)) - 1 if vlr_cota_atual > 0.0 and vlr_cota_anterior > 0.0 else 0.0
#         #
#         #     carteira.at[indx, 'QTD_COTA_ATUAL'] = float('%.4f' % float(qtd_cota_atual))
#         #     carteira.at[indx, 'VLR_COTA_ATUAL'] = float('%.4f' % float(vlr_cota_atual))
#         #     carteira.at[indx, 'PERC_COTA_ATUAL'] = float('%.2f' % float(perc_cota_atual))
#         #
#         #     vlr_cota_anterior = float(vlr_cota_atual)
#         #
#         # try:
#         #     import os
#         #     path = 'carteira.xlsx'
#         #     if os.path.exists(path=path): os.remove(path)
#         #     carteira.to_excel(excel_writer=path, index=True)
#         # except:
#         #     pass
#
#         carteiras = carteiras.append(carteira)
#         del preco
#         del trade
#         del carteira
#
#     lista = [
#         {"data": str(row.DATA),
#          "codigo": str(row.CODIGO),
#          "quant": int(row.QTD),
#          "preco":  float('%.2f' % float(row.PRECO)),
#          "investido":  float('%.2f' % float(row.VLR_INVEST)),
#          "acum": int(row.QTD_ACUM),
#          "cotacao":  float('%.2f' % float(row.COTACAO)),
#          "investimento":  float('%.2f' % float(row.INVESTIMENTO)),
#          "patrimonio":  float('%.2f' % float(row.PATRIMONIO)),
#          }
#         for row in carteiras.itertuples()
#     ]
#
#     cart = carteiras.loc[carteiras['CODIGO'] == 'ITSA4']
#     cart['DATA'] = cart['DATA'].apply(lambda x: str(x)[:6])
#     cart['ANO'] = cart['DATA'].apply(lambda x: str(x)[:4])
#     cart.drop_duplicates(subset=['DATA'], keep="last", inplace=True)
#     cart.drop(['QTD', 'PRECO', 'COTACAO', 'QTD_ACUM', 'VLR_INVEST'], axis=1, inplace=True)
#
#     mensal = [
#         {
#             "data": str(row.DATA),
#             "codigo": str(row.CODIGO),
#             "investimento":  float('%.2f' % float(row.INVESTIMENTO)),
#             "patrimonio":  float('%.2f' % float(row.PATRIMONIO)),
#          }
#         for row in cart.itertuples()
#     ]
#
#     cart.set_index('DATA', inplace=True)
#     anos = cart['ANO'].unique()
#
#     anual = [
#         {
#             'ano': str(ano),
#             'jan': ('%.2f' % float(cart.at[str(ano)+'01', 'PATRIMONIO'])) if str(ano)+'01' in cart.index else ('%.2f' % float(0.0)),
#             'fev': ('%.2f' % float(cart.at[str(ano)+'02', 'PATRIMONIO'])) if str(ano)+'02' in cart.index else ('%.2f' % float(0.0)),
#             'mar': ('%.2f' % float(cart.at[str(ano)+'03', 'PATRIMONIO'])) if str(ano)+'03' in cart.index else ('%.2f' % float(0.0)),
#             'abr': ('%.2f' % float(cart.at[str(ano)+'04', 'PATRIMONIO'])) if str(ano)+'04' in cart.index else ('%.2f' % float(0.0)),
#             'mai': ('%.2f' % float(cart.at[str(ano)+'05', 'PATRIMONIO'])) if str(ano)+'05' in cart.index else ('%.2f' % float(0.0)),
#             'jun': ('%.2f' % float(cart.at[str(ano)+'06', 'PATRIMONIO'])) if str(ano)+'06' in cart.index else ('%.2f' % float(0.0)),
#             'jul': ('%.2f' % float(cart.at[str(ano)+'07', 'PATRIMONIO'])) if str(ano)+'07' in cart.index else ('%.2f' % float(0.0)),
#             'ago': ('%.2f' % float(cart.at[str(ano)+'08', 'PATRIMONIO'])) if str(ano)+'07' in cart.index else ('%.2f' % float(0.0)),
#             'set': ('%.2f' % float(cart.at[str(ano)+'09', 'PATRIMONIO'])) if str(ano)+'09' in cart.index else ('%.2f' % float(0.0)),
#             'out': ('%.2f' % float(cart.at[str(ano)+'10', 'PATRIMONIO'])) if str(ano)+'10' in cart.index else ('%.2f' % float(0.0)),
#             'nov': ('%.2f' % float(cart.at[str(ano)+'11', 'PATRIMONIO'])) if str(ano)+'11' in cart.index else ('%.2f' % float(0.0)),
#             'dez': ('%.2f' % float(cart.at[str(ano)+'12', 'PATRIMONIO'])) if str(ano)+'12' in cart.index else ('%.2f' % float(0.0)),
#             'anual': 0.0,
#             'acum': 0.0,
#          }
#         for ano in anos
#     ]
#
#     return render_template(template_name_or_list="admin_testes.html", lista=lista, mensal=mensal, anual=anual)