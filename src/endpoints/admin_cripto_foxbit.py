# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
#
# bp_admin_cripto_foxbit = Blueprint('admin_cripto_foxbit', __name__, url_prefix='/criptofoxbit')
#
#
# @bp_admin_cripto_foxbit.route('/')
# @login_required
# @flask_optimize.optimize(cache='GET-1')
# def index():
#     if str(current_user.tipo) != 'A':
#         return redirect(location=url_for('principal.index'))
#     return render_template(template_name_or_list="admin_cripto_foxbit.html")
#
#
# @bp_admin_cripto_foxbit.route('/processar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
# def processar():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return 'Usuário não está Permitido! Somente para Administradores.'
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return 'Dados não informado!'
#
#         try:
#             htmlTrades = data.get('trades')
#         except:
#             return 'Dados não informado!'
#
#         if not htmlTrades:
#             return '<p>Trades não informado...</p>'
#
#         lstTrades = htmlTrades.split('\n')  # criar lista por quebra de linha
#         lstTrades = [row for row in lstTrades if str(row).strip() != '']  # remover linhas em branco
#         lstTrades = [row.split('\t') for row in lstTrades]  # criar colunas, por tab = \t
#         lstTrades = [[row.strip() for row in trade if str(row).strip() != ''] for trade in lstTrades]  # remover colunas em branco
#
#         data = lstTrades[1:]  # os registros são do indice 1 até o penultimo indice
#         columns = lstTrades[:1][0]  # o indice 1 é as colunas
#
#         import pandas as pd
#         import numpy as np
#
#         df = pd.DataFrame(data=data, columns=columns)
#
#         # df.columns = ['CONTA', 'TRADE', 'PAR',      'TIPO', 'QUANTIDADE', 'PRECO', 'TOTAL', 'TAXA', 'DATA']
#         df.columns = ['CONTA', 'TRADE', 'MOEDA', 'TIPO', 'QUANTIDADE', 'PRECO', 'TOTAL', 'TAXA', 'DATA']
#
#         df.drop(df.loc[df['CONTA'] == 'CONTA'].index, inplace=True)
#         df.sort_index(ascending=False, inplace=True)
#         df.reset_index(inplace=True)
#
#         df['CONTA'] = df['CONTA'].apply(pd.to_numeric, errors='ignore')  # df['CONTA'] = pd.to_numeric(df['CONTA'])
#         df['TRADE'] = df['TRADE'].apply(pd.to_numeric, errors='ignore')
#         df['QUANTIDADE'] = df['QUANTIDADE'].map(lambda x: ''.join([i for i in x if i.isdigit() or i == '.' or i == ',']).replace('.', '').replace(',', '.')).astype(np.float64)
#         df['PRECO'] = df['PRECO'].map(lambda x: ''.join([i for i in x if i.isdigit() or i == '.' or i == ',']).replace('.', '').replace(',', '.')).astype(np.float64)
#         df['TOTAL'] = df['TOTAL'].map(lambda x: ''.join([i for i in x if i.isdigit() or i == '.' or i == ',']).replace('.', '').replace(',', '.')).astype(np.float64)
#         df['TAXA'] = df['TAXA'].map(lambda x: ''.join([i for i in x if i.isdigit() or i == '.' or i == ',']).replace('.', '').replace(',', '.')).astype(np.float64)
#         df['DATA'] = pd.to_datetime(df['DATA'], errors='ignore', format="%d-%m-%Y %H:%M")
#
#         # df['QUANTIDADE'] = df.apply(lambda x: x.QUANTIDADE * -1 if x.TIPO == 'Venda' else x.QUANTIDADE, axis=1)
#         # df['TOTAL'] = df.apply(lambda x: x.TOTAL * -1 if x.TIPO == 'Venda' else x.TOTAL, axis=1)
#         # df['TAXA'] = df.apply(lambda x: x.TAXA * -1 if x.TIPO == 'Venda' else x.TAXA, axis=1)
#         # df['CUSTO'] = df['QUANTIDADE'] / df['TOTAL']
#         df = df[['DATA', 'MOEDA', 'TIPO', 'QUANTIDADE', 'PRECO', 'TOTAL', 'TAXA']]
#
#         # Compra == TAXA ==  XRP 1,863241 /  CHZ 4,84833870 / LINK 0,07562770 / Ł 0,01801139 / Ξ 0,00155816	 # LTC = Ł # ETH = Ξ
#         # Venda    == TAXA ==  R$ 0,306
#
#         pd.set_option('precision', 10)  # tamanho da casas decimasi
#
#         df_new = df.copy()
#         df_new['IDX'] = df_new.index.map(lambda x: int(x))
#         df_new['TOTAL'] = df_new.apply(lambda x: x.TOTAL * -1 if x.TIPO == 'Venda' else x.TOTAL, axis=1)
#
#         df_new['QTDE_AJUSTADA'] = df_new.apply(lambda x: float(float(x.QUANTIDADE) * -1) if x.TIPO == 'Venda' else float(x.QUANTIDADE) - float(x.TAXA), axis=1, )
#         df_new['TAXA_AJUSTADA'] = df_new.apply(lambda x: float(x.TAXA) if x.TIPO == 'Venda' else float(x.PRECO) * float(x.TAXA), axis=1, )
#         df_new['QTDE_CUSTODIA'] = 0.0
#         df_new['QTDE_CUSTODIA_ANT'] = 0.0
#         df_new['PRECO_MEDIO'] = 0.0
#         df_new['PRECO_ATUAL'] = 0.0
#         df_new['VALRZ_ATUAL'] = 0.0
#
#         for moeda in df['MOEDA'].unique():
#
#             df_new['QTDE_CUSTODIA'].loc[df_new['MOEDA'] == moeda] = df_new['QTDE_AJUSTADA'].loc[df_new['MOEDA'] == moeda].cumsum()
#             df_new['QTDE_CUSTODIA'].loc[df_new['MOEDA'] == moeda] = df_new['QTDE_CUSTODIA'].apply(lambda x: float(x) if round(float(x), 5) > 0.0 else 0.0)
#             df_new['QTDE_CUSTODIA_ANT'].loc[df_new['MOEDA'] == moeda] = df_new['QTDE_CUSTODIA'].loc[df_new['MOEDA'] == moeda].shift(1, fill_value=0)
#
#             preco_atual, valoriz_atual = 0.0, 0.0  # get_price(moeda=moeda)
#             df_new['PRECO_ATUAL'].loc[df_new['MOEDA'] == moeda] = float(preco_atual)
#             df_new['VALRZ_ATUAL'].loc[df_new['MOEDA'] == moeda] = float(valoriz_atual)
#
#             df_new_ativo = df_new.loc[df_new['MOEDA'] == moeda].copy()
#             df_new_ativo.reset_index(drop=True, inplace=True)
#             df_new_ativo.fillna(0, inplace=True)
#             df_new.fillna(0, inplace=True)
#
#             for idx, row in df_new_ativo.iterrows():
#                 if row['QTDE_AJUSTADA'] > 0:
#                     preco_medio_atual = df_new_ativo['PRECO_MEDIO'].shift(1, fill_value=df_new_ativo['PRECO'].iloc[0])[idx]
#                     qtd_custodia_anterior = df_new_ativo['QTDE_CUSTODIA_ANT'][idx]
#                     valor_da_compra_atual = row['TOTAL']
#                     preco_medio = (valor_da_compra_atual + (preco_medio_atual * qtd_custodia_anterior)) / df_new_ativo['QTDE_CUSTODIA'][idx]
#                     df_new_ativo.loc[idx, 'PRECO_MEDIO'] = preco_medio  # df_new_ativo.iloc[idx, df_new_ativo.columns == 'PRECO_MEDIO'] = preco_medio
#                     df_new['PRECO_MEDIO'].loc[(df_new['MOEDA'] == moeda) & (df_new['IDX'] == row['IDX'])] = preco_medio
#                 else:
#                     pass
#                     try:
#                         preco_medio_atual = df_new_ativo['PRECO_MEDIO'][idx - 1]
#                         df_new_ativo.loc[idx, 'PRECO_MEDIO'] = preco_medio_atual
#                         df_new['PRECO_MEDIO'].loc[(df_new['MOEDA'] == moeda) & (df_new['IDX'] == row['IDX'])] = preco_medio_atual
#                     except:
#                         pass
#
#         df_new.fillna(0, inplace=True)
#
#         df_new['DATA'] = df_new['DATA'].dt.strftime('%Y-%m-%d')  # df_new['DATA'].dt.strftime('%d/%m/%Y')
#         df_new['QUANTIDADE'] = df_new['QUANTIDADE'].astype(str)
#         df_new['QUANTIDADE'] = df_new['QUANTIDADE'].str.replace('.', ',')
#         df_new['PRECO'] = df_new['PRECO'].astype(str)
#         df_new['QTDE_AJUSTADA'] = df_new['QTDE_AJUSTADA'].astype(str)
#         df_new['QTDE_AJUSTADA'] = df_new['QTDE_AJUSTADA'].str.replace('.', ',').str.replace('-', '')
#         df_new['PRECO'] = df_new['PRECO'].astype(str)
#         df_new['PRECO'] = df_new['PRECO'].str.replace('.', ',')
#         # df_new['CUSTO'] = df_new['CUSTO'].astype(str)
#         # df_new['CUSTO'] = df_new['CUSTO'].str.replace('.',',')
#         df_new['TAXA'] = df_new['TAXA'].astype(str)
#         df_new['TAXA'] = df_new['TAXA'].str.replace('.', ',')
#         df_new['TAXA_AJUSTADA'] = df_new['TAXA_AJUSTADA'].astype(str)
#         df_new['TAXA_AJUSTADA'] = df_new['TAXA_AJUSTADA'].str.replace('.', ',')
#         # df_new[['DATA', 'TIPO', 'MOEDA', 'QTDE_AJUSTADA', 'PRECO', 'TAXA_AJUSTADA']].head(3)
#
#         # df_new[['DATA', 'TIPO', 'MOEDA', 'QTDE_AJUSTADA', 'PRECO', 'TAXA_AJUSTADA']].to_csv(path_or_buf="/content/cms.cripto.foxbit.csv", index=False, sep=";", )
#
#         result = ''
#         result += '<br/> '
#         result += '<div class="table-responsive">'
#         result += '<table id="Grid" border="1" width="100%" class="table table-sm table-striped table-bordered table-hover">'
#         result += '<thead class="thead-dark">'
#         result += '<tr>'
#         result += '<th scope="col">Data</th>'
#         result += '<th scope="col">Tipo</th>'
#         result += '<th scope="col">Código</th>'
#         result += '<th scope="col">Quant.</th>'
#         result += '<th scope="col">Preço</th>'
#         result += '<th scope="col">Taxas</th>'
#         result += '<th scope="col">Total</th>'
#         result += '<th scope="col">Ação</th>'
#         result += '</tr>'
#         result += '</thead>'
#         result += '<tbody>'
#
#         for idx, row in df_new.iterrows():
#             result += '<tr id="GridTr-'+str(idx)+'">'
#             result += '<td>' + str(row['DATA']) +'</td>'
#             result += '<td>' + str(row['TIPO']) +'</td>'
#             result += '<td>' + str(row['MOEDA']) +'</td>'
#             result += '<td>' + str(row['QTDE_AJUSTADA']) +'</td>'
#             result += '<td>' + str(row['PRECO']) +'</td>'
#             result += '<td>' + str(row['TAXA_AJUSTADA']) +'</td>'
#             result += '<td>' + str(row['TOTAL']) +'</td>'
#             result += '<td class="text-center"> <div class="btn-group btn-group-sm" role="group">'
#             result += '<a id="GridSalvar-'+str(idx)+'" class="btn btn-sm btn-success btn-icon btn-icon-mini btn-round btn-simple" style="font-size:0.5rem;" href="javascript:void(0);" onclick="fSalvar( '+str(idx)+', \''+str(row['TIPO'])[:1]+'\', \''+str(row['MOEDA'])+'\', \''+str(row['DATA'])+'\', \''+str(row['QTDE_AJUSTADA'])+'\', \''+str(row['PRECO'])+'\', \''+str(row['TAXA_AJUSTADA'])+'\' );"> <i class="fa fa-plus-square text-success fa-lg" aria-hidden="true"></i> </a>'
#             result += '</div> </td> '
#             result += '</tr>'
#
#         result += '</tbody>'
#         result += '</table>'
#         result += '</div>'
#
#         return result
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return LogErro.descricao_erro(texto=str(e))
