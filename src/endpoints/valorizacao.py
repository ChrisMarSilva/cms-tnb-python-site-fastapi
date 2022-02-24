# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.acao_empresa_ativo_cotacao_hist import ACAOEmpresaAtivoCotacaoHist
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
# from app.util.util_json import get_json_retorno_grid
# from app.util.util_datahora import converter_datetime_str, pegar_data_atual, adicionar_dias, adicionar_meses
#
#
# bp_valorizacao = Blueprint('valorizacao', __name__, url_prefix='/valorizacao')
#
#
# @bp_valorizacao.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# # @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     return render_template(template_name_or_list="valorizacao.html")
#
#
# @bp_valorizacao.route('/grid', methods=['GET', 'POST'])
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
#             categ = data.get('Categ')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not categ: return make_response(get_json_retorno_grid(msg='Categoria não informada.'), 200)
#
#         id_usuario = current_user.id
#         id_portfolio = None
#
#         # data_atual = pegar_data_atual(istext=False)
#         # dias_weekday = data_atual.isoweekday() % 7
#         # dias_weekday = dias_weekday if dias_weekday != 0 else 6
#         # data_ini_semana = converter_datetime_str(data=data_atual - adicionar_dias(dias=dias_weekday))
#         # data_ini_mes = converter_datetime_str(data=data_atual, fmt='%Y%m') + '01'
#         # data_ini_ano = converter_datetime_str(data=data_atual, fmt='%Y') + '0101'
#         # data_ini_12m = converter_datetime_str(data=data_atual - adicionar_meses(meses=12))
#         # data_atual = converter_datetime_str(data=data_atual)
#
#         data_atual = pegar_data_atual(istext=False)
#
#         dias_weekday = data_atual.isoweekday() % 7
#         dias_weekday = dias_weekday if dias_weekday != 0 else 6
#         data_ini_semana = converter_datetime_str(data=data_atual - adicionar_meses(meses=1))
#         data_fim_semana = converter_datetime_str(data=data_atual - adicionar_dias(dias=dias_weekday))
#
#         data_ano_mes_ant = converter_datetime_str(data=data_atual - adicionar_meses(meses=1), fmt='%Y%m')
#         data_ini_mes = str(data_ano_mes_ant) + '01'
#         data_fim_mes = str(data_ano_mes_ant) + '31'
#
#         data_ano_ant = int(converter_datetime_str(data=data_atual, fmt='%Y')) - 1
#         data_ini_ano = str(data_ano_ant) + '1201'
#         data_fim_ano = str(data_ano_ant) + '1231'
#
#         data_ini_12m = converter_datetime_str(data=data_atual - adicionar_meses(meses=13))
#         data_fim_12m = converter_datetime_str(data=data_atual - adicionar_meses(meses=12) - adicionar_dias(dias=1))
#
#         # if categ == 'ACAO':
#         #     # DATA ATUAL = QUARTA FEIRA 2021-05-05
#         #     print('data_ini_semana', data_ini_semana, 'data_fim_semana', data_fim_semana) # 2021-04-05 # 2021-05-02
#         #     print('data_ini_mes', data_ini_mes, 'data_fim_mes', data_fim_mes)   # 2021-04-01 # 2021-04-31
#         #     print('data_ini_ano', data_ini_ano, 'data_fim_ano', data_fim_ano)   # 2020-12-01 # 2020-12-31
#         #     print('data_ini_12m', data_ini_12m, 'data_fim_12m', data_fim_12m)   # 2020-04-05 # 2020-05-04
#
#         lista = []
#
#         def pegar_percentual(atv_tipo: str, atv_codigo: str, atv_vlr_cotacao: float, dt_ini: str, dt_fim: str):
#             atv_vlr_consulta = ACAOEmpresaAtivoCotacaoHist.buscar_valor_data_max(categoria=atv_tipo, codigo=atv_codigo, dt_ini=dt_ini, dt_fim=dt_fim)
#             atv_vlr_dif = atv_vlr_cotacao - atv_vlr_consulta
#             atv_vlr_pct = (float(atv_vlr_dif) / float(atv_vlr_consulta)) * 100 if atv_vlr_dif != 0.0 and atv_vlr_cotacao > 0.0 and atv_vlr_consulta > 0.0 else 0.0
#             return atv_vlr_pct
#
#         def pegar_dados(atv_tipo: str, atv_codigo: str, atv_nome: str, atv_vlr_cotacao: float, atv_vlr_variacao: float):
#             atv_vlr_pct_semana = pegar_percentual(atv_tipo=atv_tipo, atv_codigo=atv_codigo, atv_vlr_cotacao=atv_vlr_cotacao, dt_ini=data_ini_semana, dt_fim=data_fim_semana)
#             atv_vlr_pct_mes = pegar_percentual(atv_tipo=atv_tipo, atv_codigo=atv_codigo, atv_vlr_cotacao=atv_vlr_cotacao, dt_ini=data_ini_mes, dt_fim=data_fim_mes)
#             atv_vlr_pct_ano = pegar_percentual(atv_tipo=atv_tipo, atv_codigo=atv_codigo, atv_vlr_cotacao=atv_vlr_cotacao, dt_ini=data_ini_ano, dt_fim=data_fim_ano)
#             atv_vlr_pct_12m = pegar_percentual(atv_tipo=atv_tipo, atv_codigo=atv_codigo, atv_vlr_cotacao=atv_vlr_cotacao, dt_ini=data_ini_12m, dt_fim=data_fim_12m)
#             return [atv_codigo, atv_nome, atv_vlr_cotacao, atv_vlr_variacao, atv_vlr_pct_semana, atv_vlr_pct_mes, atv_vlr_pct_ano, atv_vlr_pct_12m]
#
#         if categ == 'ACAO':
#             rows = UsuarioCarteiraAcao.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A', ordem='CODIGO')
#             lista += [pegar_dados(atv_tipo='ACAO', atv_codigo=str(row['CODIGOATIVO']), atv_nome=str(row['NOMRESUMIDOEMPRESA']) if row['NOMRESUMIDOEMPRESA'] else str(row['NOMEEMPRESA']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']), atv_vlr_variacao=float(row['VLRVARIACAO'])) for row in rows]
#
#         if categ == 'FII':
#             rows = UsuarioCarteiraFii.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#             lista += [pegar_dados(atv_tipo='FII', atv_codigo=str(row['CODIGOFUNDO']), atv_nome=str(row['NOMEFUNDO']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']), atv_vlr_variacao=float(row['VLRVARIACAO'])) for row in rows]
#
#         if categ == 'ETF':
#             rows = UsuarioCarteiraEtf.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#             lista += [pegar_dados(atv_tipo='ETF', atv_codigo=str(row['CODIGOINDICE']), atv_nome=str(row['NOMEINDICE']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']), atv_vlr_variacao=float(row['VLRVARIACAO'])) for row in rows]
#
#         if categ == 'BDR':
#             rows = UsuarioCarteiraBdr.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A', ordem='CODIGO')
#             lista += [pegar_dados(atv_tipo='BDR', atv_codigo=str(row['CODIGOBDR']), atv_nome=str(row['NOMEBDR']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']), atv_vlr_variacao=float(row['VLRVARIACAO'])) for row in rows]
#
#         if categ == 'CRIPTO':
#             rows = UsuarioCarteiraCripto.buscar_todos(id_usuario=id_usuario, id_carteira=id_portfolio, situacao='A')
#             lista += [pegar_dados(atv_tipo='CRIPTO', atv_codigo=str(row['CODIGOCRIPTO']), atv_nome=str(row['NOMECRIPTO']), atv_vlr_cotacao=float(row['VLRPRECOFECHAMENTO']), atv_vlr_variacao=float(row['VLRVARIACAO'])) for row in rows]
#
#         if categ == 'RADAR':
#
#             rows = UsuarioRadarAcao.buscar_dados_grid_port(id_usuario=id_usuario)
#             lista += [pegar_dados(atv_tipo='ACAO', atv_codigo=str(row['CODIGOATIVO']), atv_nome=str(row['NOMRESUMIDOEMPRESA']) if row['NOMRESUMIDOEMPRESA'] else str(row['NOMEEMPRESA']), atv_vlr_cotacao=float(row['PRECO']), atv_vlr_variacao=float(row['VARIACAO'])) for row in rows]
#
#             rows = UsuarioRadarFii.buscar_dados_grid_port(id_usuario=id_usuario)
#             lista += [pegar_dados(atv_tipo='FII', atv_codigo=str(row['CODIGOATIVO']), atv_nome=str(row['NOMEFUNDO']), atv_vlr_cotacao=float(row['PRECO']), atv_vlr_variacao=float(row['VARIACAO'])) for row in rows]
#
#             rows = UsuarioRadarEtf.buscar_dados_grid_port(id_usuario=id_usuario)
#             lista += [pegar_dados(atv_tipo='ETF', atv_codigo=str(row['CODIGOATIVO']), atv_nome=str(row['NOMEINDICE']), atv_vlr_cotacao=float(row['PRECO']), atv_vlr_variacao=float(row['VARIACAO'])) for row in rows]
#
#             rows = UsuarioRadarBdr.buscar_dados_grid_port(id_usuario=id_usuario)
#             lista += [pegar_dados(atv_tipo='BDR', atv_codigo=str(row['CODIGOBDR']), atv_nome=str(row['NOMEBDR']), atv_vlr_cotacao=float(row['PRECO']), atv_vlr_variacao=float(row['VARIACAO'])) for row in rows]
#
#             rows = UsuarioRadarCripto.buscar_dados_grid_port(id_usuario=id_usuario)
#             lista += [pegar_dados(atv_tipo='CRIPTO', atv_codigo=str(row['CODIGOATIVO']), atv_nome=str(row['NOMECRIPTO']), atv_vlr_cotacao=float(row['PRECO']), atv_vlr_variacao=float(row['VARIACAO'])) for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
