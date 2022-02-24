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
# from app.models.fii_fundoimob import FiiFundoImob
# from app.models.etf_indice import ETFIndice
# from app.models.bdr_empresa import BDREmpresa
# from app.models.cripto_empresa import CriptoEmpresa
# from app.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamento
# from app.models.usuario_acao_empresa_operacao import UsuarioACAOEmpresaOperacao
# from app.models.usuario_acao_empresa_provento import UsuarioACAOEmpresaProvento
# from app.models.usuario_acao_empresa_aluguel import UsuarioACAOEmpresaAluguel
# from app.models.usuario_fii_fundoimob_lancamento import UsuarioFiiFundoImobLancamento
# from app.models.usuario_fii_fundoimob_provento import UsuarioFiiFundoImobProvento
# from app.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamento
# from app.models.usuario_etf_indice_operacao import UsuarioETFIndiceOperacao
# from app.models.usuario_bdr_empresa_lancamento import UsuarioBDREmpresaLancamento
# from app.models.usuario_bdr_empresa_operacao import UsuarioBDREmpresaOperacao
# from app.models.usuario_bdr_empresa_provento import UsuarioBDREmpresaProvento
# from app.models.usuario_cripto_lancamento import UsuarioCriptoLancamento
# from app.models.usuario_config import UsuarioConfig
# from app.models.usuario_apuracao import UsuarioApuracao
# from app.models.usuario_carteira import UsuarioCarteira
# from app.util.util_json import get_json_retorno_dados, get_json_retorno_grid, get_json_retorno_lista
# from app.util.util_formatacao import decimal_to_str, inteiro_to_str, decimal_prov_to_str, decimal_cripto_to_str
# from app.util.util_datahora import pegar_data_atual, buscar_nome_mes_resumido
#
#
# bp_irpf = Blueprint('irpf', __name__, url_prefix='/IRPF')
#
#
# @bp_irpf.route('/')
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
#     if not gerar_portoflio and  UsuarioCriptoLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
#
#     return render_template(template_name_or_list="irpf.html", gerar_portoflio=gerar_portoflio)
#
#
# @bp_irpf.route('/listaAno', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_ano():
#     try:
#
#         id_usuario = current_user.id
#
#         try:
#
#             anos = []
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
#         if not menor or not maior: return make_response(get_json_retorno_lista(rslt='OK'), 200)
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
# @bp_irpf.route('/gridIsentos', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_isentos():
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
#             ano = data.get('AnoDeclaracao')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not ano: return make_response(get_json_retorno_grid(msg='Ano Declaracao não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         lista = []
#         dt_ini = str(ano)+'0101'
#         dt_fim = str(ano)+'1231'
#         dt_ini_pos = str(int(ano)+1) + '0101'
#         dt_fim_pos = str(int(ano)+1) + '1231'
#         ano_atual = pegar_data_atual(fmt='%Y')
#         mes_atual = pegar_data_atual(fmt='%m')
#
#         # ACAO - SOMENTE DIVIDENDOOS RECEBIDOS NO MESMO ANO
#         rows = UsuarioACAOEmpresaProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='D', dt_pagto_ini=str(dt_ini), dt_pagto_fim=str(dt_fim))
#         lista += [['09 - Lucros e dividendos recebidos (Pagos no mesmo Ano)', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'D'] for row in rows]
#
#         # ACAO - SOMENTE DIVIDENDOOS RECEBIDOS NO PROXIMO ANO
#         rows = UsuarioACAOEmpresaProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='D', dt_ex_ini=str(dt_ini), dt_ex_fim=str(dt_fim), dt_pagto_ini=str(dt_ini_pos), dt_pagto_fim=str(dt_fim_pos))
#         lista += [['09 - Lucros e dividendos recebidos (Pagos no próximo Ano)', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'D'] for row in rows]
#
#         # ACAO - SOMENTE BONUS RECEBIDOS NO ANO
#         rows = UsuarioACAOEmpresaLancamento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='B', dt_ini=str(dt_ini), dt_fim=str(dt_fim))
#         lista += [['18 - Incorporação de reservas ao capital / Bonificações em ações', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'B'] for row in rows]
#
#         # ACAO - LUCRO ISENTO COM VENDA INFERIOR A 20MIL
#         vlr_total_ano = 0.0
#         for mes in range(1, 13):
#             if int(ano) == int(ano_atual) and int(mes) > int(mes_atual): break
#             ano_mes = str(ano) + str(mes).zfill(2)
#             vlr_apurado = 0.0
#             vlr_venda = 0.0
#             rows = UsuarioACAOEmpresaOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=str(ano_mes) + "01", dt_fim=str(ano_mes) + "31", categoria="C", tipo="V", troca="N")  # C - Comun  # V - Venda
#             for row in rows:
#                 vlr_valorizacao = UsuarioACAOEmpresaOperacao.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO']))
#                 vlr_apurado += float(vlr_valorizacao)
#                 vlr_venda += float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0
#             if vlr_venda <= 20000.00 and vlr_apurado > 0.0: vlr_total_ano += vlr_apurado
#         if vlr_total_ano > 0.0:
#             lista += [['20 - Ganhos líquidos em operações no mercado à vista de ações <br>negociadas em bolsas de valores nas alienações realizadas até R$ 20.000,00 em cada mês, <br>para o conjunto de ações', '', '', decimal_to_str(valor=float(vlr_total_ano)), '', '']]
#
#         # ACAO - SOMENTE RESTITUICAO DE CAPITAL SOCIAL EM DINHEIRO RECEBIDOS NO ANO
#         rows = UsuarioACAOEmpresaProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='R', dt_pagto_ini=str(dt_ini), dt_pagto_fim=str(dt_fim))
#         lista += [['26 - Outros <br/> Descrição: Restituição de Capital Social em Dinheiro', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'R'] for row in rows]
#
#         # FII - SOMENTE RENDIMENTOS RECEBIDOS NO ANO
#         rows = UsuarioFiiFundoImobProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='R', dt_pagto_ini=str(dt_ini), dt_pagto_fim=str(dt_fim))
#         lista += [['26 - Outros (FIIs/Rendimentos)', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'F'] for row in rows]
#
#         # BDR - SOMENTE DIVIDENDOOS RECEBIDOS NO ANO
#         rows = UsuarioBDREmpresaProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='D', dt_pagto_ini=str(dt_ini), dt_pagto_fim=str(dt_fim))
#         lista += [['09 - Lucros e dividendos recebidos', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'D'] for row in rows]
#
#         # CRIPTO - LUCRO ISENTO COM VENDA INFERIOR A 35MIL
#         vlr_total_ano = 0.0
#         for mes in range(1, 13):
#             if int(ano) == int(ano_atual) and int(mes) > int(mes_atual): break
#             ano_mes = str(ano) + str(mes).zfill(2)
#             vlr_apurado = 0.0
#             vlr_venda = 0.0
#             rows = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=str(ano_mes) + "01", dt_fim=str(ano_mes) + "31", tipo="V")  # V - Venda
#             for row in rows:
#                 vlr_valorizacao = UsuarioCriptoLancamento.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO']))
#                 vlr_apurado += float(vlr_valorizacao)
#                 vlr_venda += float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0
#             if vlr_venda <= 35000.00 and vlr_apurado > 0.0: vlr_total_ano += vlr_apurado
#         if vlr_total_ano > 0.0:
#             lista += [['05 - Ganho de capital na alienação de bem, <br>direito ou conjunto de bens ou direitos da mesma natureza, alienados em um mesmo mês, <br>de valor total de alienação até R$ 20.000,00, <br>para ações alienadas no mercado de balcão, e R$ 35.000,00, nos demais casos', '', '', decimal_to_str(valor=float(vlr_total_ano)), '', '']]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_irpf.route('/gridIsentosDetalhe', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_isentos_detalhe():
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
#             ano = data.get('AnoDeclaracao')
#             tipo = data.get('TpRendIsento')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not ano: return make_response(get_json_retorno_grid(msg='Ano Declaracao não informado.'), 200)
#         if not tipo: return make_response(get_json_retorno_grid(msg='Tipo de Rendimento não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_grid(msg='Cod. Ativo não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         lista = []
#         dt_ini = str(ano)+'0101'
#         dt_fim = str(ano)+'1231'
#
#         if str(tipo) == 'D' or str(tipo) == 'R':
#
#             # ACAO - SOMENTE DIVIDENDOOS RECEBIDOS NO ANO
#             # ACAO - SOMENTE RESTITUICAO DE CAPITAL SOCIAL EM DINHEIRO RECEBIDOS NO ANO
#             rows = UsuarioACAOEmpresaProvento.buscar_todos(id_usuario=id_usuario, codigo=str(codigo), tipo=str(tipo), dt_ini=str(dt_ini), dt_fim=str(dt_fim))
#             lista += [[str(row["DATAEX"]), str(row["DATAPAGTO"]), str(row["CODIGOATIVO"]), UsuarioACAOEmpresaProvento.descricao_tipo(tipo=row["TIPO"]), float(row["QUANTIDADE"]), decimal_prov_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#             # BDR - SOMENTE DIVIDENDOOS RECEBIDOS NO ANO
#             rows = UsuarioBDREmpresaProvento.buscar_todos(id_usuario=id_usuario, codigo=str(codigo), tipo=str(tipo), dt_ini=str(dt_ini), dt_fim=str(dt_fim))
#             lista += [[str(row["DATAEX"]), str(row["DATAPAGTO"]), str(row["CODIGOBDR"]), UsuarioBDREmpresaProvento.descricao_tipo(tipo=row["TIPO"]), float(row["QUANTIDADE"]), decimal_prov_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         elif str(tipo) == 'B':
#             # ACAO - SOMENTE BONUS RECEBIDOS NO ANO
#             rows = UsuarioACAOEmpresaLancamento.buscar_todos(id_usuario=id_usuario, codigo=str(codigo), dt_ini=str(dt_ini), dt_fim=str(dt_fim), tipo=str(tipo))
#             lista += [[str(row["DATA"]), str(row["DATA"]), str(row["CODIGOATIVO"]), UsuarioACAOEmpresaLancamento.descricao_tipo(tipo=row["TIPO"]), float(row["QUANT"]), decimal_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         elif str(tipo) == 'F':
#             # FII - SOMENTE RENDIMENTOS RECEBIDOS NO ANO
#             tipo = "R"  # R-Rendimento
#             rows = UsuarioFiiFundoImobProvento.buscar_todos(id_usuario=id_usuario, codigo=str(codigo), tipo=str(tipo), dt_ini=str(dt_ini), dt_fim=str(dt_fim))
#             lista += [[str(row["DATAEX"]), str(row["DATAPAGTO"]), str(row["CODIGOFUNDO"]), UsuarioFiiFundoImobProvento.descricao_tipo(tipo=row["TIPO"]), float(row["QUANTIDADE"]), decimal_prov_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         # elif str(tipo) == 'k':
#         #     # CRIPTOS - SOMENTE VENDAS NO ANO
#         #     rows = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, codigo=str(codigo), tipo=str(tipo), dt_ini=str(dt_ini), dt_fim=str(dt_fim))
#         #     lista += [[str(row["DATAEX"]), str(row["DATAPAGTO"]), str(row["CODIGOFUNDO"]), UsuarioCriptoLancamento.descricao_tipo(tipo=row["TIPO"]), float(row["QUANTIDADE"]), decimal_prov_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_irpf.route('/gridTributaveis', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_tributaveis():
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
#             ano = data.get('AnoDeclaracao')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not ano: return make_response(get_json_retorno_grid(msg='Ano Declaracao não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         lista = []
#         dt_ini = str(ano)+'0101'
#         dt_fim = str(ano)+'1231'
#         dt_ini_pos = str(int(ano)+1) + '0101'
#         dt_fim_pos = str(int(ano)+1) + '1231'
#         ano_atual = pegar_data_atual(fmt='%Y')
#         mes_atual = pegar_data_atual(fmt='%m')
#
#         # ACAO - SOMENTE JUROS SOBRE CAPITAL PRORIO RECEBIDOS NO MESMO ANO
#         rows = UsuarioACAOEmpresaProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='J', dt_pagto_ini=str(dt_ini), dt_pagto_fim=str(dt_fim))
#         lista += [['10 - Juros sobre capital prórpio (Pagos no mesmo Ano)', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'J'] for row in rows]
#
#         # ACAO - SOMENTE JUROS SOBRE CAPITAL PRORIO RECEBIDOS NO PROXIMO ANO
#         rows = UsuarioACAOEmpresaProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='J', dt_ex_ini=str(dt_ini), dt_ex_fim=str(dt_fim), dt_pagto_ini=str(dt_ini_pos), dt_pagto_fim=str(dt_fim_pos))
#         lista += [['10 - Juros sobre capital prórpio (Pagos no próximo Ano)', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'J'] for row in rows]
#
#         # ACAO - SOMENTE ALUGUEIS DE ATIVOS NO ANO
#         rows = UsuarioACAOEmpresaAluguel.buscar_dados_grid_irpf(id_usuario=id_usuario, dt_ini=str(dt_ini), dt_fim=str(dt_fim))
#         lista += [['06 - Rendimentos de Aplicações Financeiras <br/> Aluguel de Ativos', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'A'] for row in rows]
#
#         # FII - SOMENTE AMORTIZACOES NO ANO
#         rows = UsuarioFiiFundoImobLancamento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='A', dt_ini=str(dt_ini), dt_fim=str(dt_fim))
#         lista += [['06 - Rendimentos de aplicações financeiras (FIIs/Amortização)', str(row["CNPJ"]), str(row["RAZAOSOCIAL"]), decimal_to_str(valor=float(row["TOTVLR"]) if row["TOTVLR"] else 0.0), str(row["CODIGO"]), 'F'] for row in rows]
#
#         # CRIPTO - LUCRO ISENTO COM VENDA INFERIOR A 35MIL
#         vlr_total_ano = 0.0
#         for mes in range(1, 13):
#             if int(ano) == int(ano_atual) and int(mes) > int(mes_atual): break
#             ano_mes = str(ano) + str(mes).zfill(2)
#             vlr_apurado = 0.0
#             vlr_venda = 0.0
#             rows = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=str(ano_mes) + "01", dt_fim=str(ano_mes) + "31", tipo="V")  # V - Venda
#             for row in rows:
#                 vlr_valorizacao = UsuarioCriptoLancamento.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO']))
#                 vlr_apurado += float(vlr_valorizacao)
#                 vlr_venda += float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0
#             if vlr_venda > 35000.00 and vlr_apurado > 0.0: vlr_total_ano += vlr_apurado
#         if vlr_total_ano > 0.0:
#             lista += [['06 - Rendimentos de aplicações financeiras (Criptos)', '00.000.000/0000-00', 'Criptosmoedas<br>Pegar o CNPJ e o Nome da Exchange/Corretora', decimal_to_str(valor=float(vlr_total_ano)), 'CRIPTO', 'K']]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_irpf.route('/gridTributaveisDetalhe', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_tributaveis_detalhe():
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
#             ano = data.get('AnoDeclaracao')
#             tipo = data.get('TpRendTributavel')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not ano: return make_response(get_json_retorno_grid(msg='Ano Declaracao não informado.'), 200)
#         if not tipo: return make_response(get_json_retorno_grid(msg='Tipo de Rendimento não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_grid(msg='Cod. Ativo não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         lista = []
#         dt_ini = str(ano)+'0101'
#         dt_fim = str(ano)+'1231'
#         ano_atual = pegar_data_atual(fmt='%Y')
#         mes_atual = pegar_data_atual(fmt='%m')
#
#         if str(tipo) == 'J':
#             # ACAO - SOMENTE JUROS SOBRE CAPITAL PRORIO RECEBIDOS NO ANO
#             rows = UsuarioACAOEmpresaProvento.buscar_todos(id_usuario=id_usuario, codigo=str(codigo), tipo=str(tipo), dt_ini=str(dt_ini), dt_fim=str(dt_fim))
#             lista = [[str(row["DATAEX"]), str(row["DATAPAGTO"]), str(row["CODIGOATIVO"]), UsuarioACAOEmpresaProvento.descricao_tipo(tipo=str(row["TIPO"])), str(row["QUANTIDADE"]), decimal_prov_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         elif str(tipo) == 'A':
#             # ACAO - SOMENTE ALUGUEIS DE ATIVOS NO ANO
#             rows = UsuarioACAOEmpresaAluguel.buscar_todos(id_usuario=id_usuario, codigo=str(codigo), dt_ini=str(dt_ini), dt_fim=str(dt_fim))
#             lista = [[str(row["DATA"]), str(row["DATA"]), str(row["CODIGOATIVO"]), 'Aluguel', 1, decimal_to_str(valor=float(row["VLRLIQUIDO"])), decimal_to_str(valor=float(row["VLRLIQUIDO"]))] for row in rows]
#
#         elif str(tipo) == 'F':
#             #  FII - SOMENTE AMORTIZACOES NO ANO
#             tipo = "A"  # A-Amortização
#             rows = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, codigo=str(codigo), dt_ini=str(dt_ini), dt_fim=str(dt_fim), tipo=str(tipo))
#             lista = [[str(row["DATA"]), str(row["DATA"]), str(row["CODIGOFUNDO"]), UsuarioFiiFundoImobLancamento.descricao_tipo(tipo=row["TIPO"]), str(row["QUANT"]), decimal_prov_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))] for row in rows]
#
#         # elif str(tipo) == 'K':
#         #     # CRIPTO - LUCRO ISENTO COM VENDA INFERIOR A 35MIL
#         #     for mes in range(1, 13):
#         #         if int(ano) == int(ano_atual) and int(mes) > int(mes_atual): break
#         #         ano_mes = str(ano) + str(mes).zfill(2)
#         #         vlr_apurado = 0.0
#         #         vlr_venda = 0.0
#         #         rows = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=str(ano_mes) + "01", dt_fim=str(ano_mes) + "31", tipo="V")  # V - Venda
#         #         for row in rows:
#         #             vlr_valorizacao = UsuarioCriptoLancamento.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO']))
#         #             vlr_apurado += float(vlr_valorizacao)
#         #             vlr_venda += float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0
#         #         if vlr_venda > 35000.00 and vlr_apurado > 0.0:
#         #             lista += [[str(row["DATA"]), str(row["DATA"]), str(row["CODIGOCRIPTO"]), UsuarioCriptoLancamento.descricao_tipo(tipo=row["TIPO"]), str(row["QUANT"]), decimal_prov_to_str(valor=float(row["VLRPRECO"])), decimal_to_str(valor=float(row["TOTVLR"]))]]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_irpf.route('/gridBensEDiretos', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_bens_e_diretos():
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
#             ano = data.get('AnoDeclaracao')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not ano: return make_response(get_json_retorno_grid(msg='Ano Declaracao não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         try:
#
#             anos = []
#             anos.append(str(ano) + '0101')
#             anos.append(UsuarioACAOEmpresaLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#             anos.append(UsuarioFiiFundoImobLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#             anos.append(UsuarioETFIndiceLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#             anos.append(UsuarioBDREmpresaLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#             anos.append(UsuarioCriptoLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#
#             menor = min(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#
#         except:
#             menor = None
#
#         if not menor: return make_response(get_json_retorno_lista(rslt='OK'), 200)
#
#         lista = []
#         dt_ini = str(ano) + '0101'
#         dt_fim = str(ano) + '1231'
#         dt_fim_ant = str(int(ano)-1) + '1231'
#         dt_ini_pos = str(int(ano)+1) + '0101'
#         dt_fim_pos = '99999999'  # str(int(ano)+1) + '1231'
#
#         # ACAO - TODAS AS ACOES QUE VOCE TEM ATE O ANO DE DECLARACAO
#         rows = ACAOEmpresaAtivo.buscar_lista_irpf(id_usuario=id_usuario, dt_fim=dt_fim)
#         for row in rows:
#             qtde_tot_compra = UsuarioACAOEmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_ativo=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_bonus = UsuarioACAOEmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_ativo=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_venda = UsuarioACAOEmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_ativo=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_atual = (float(qtde_tot_compra) + float(qtde_tot_bonus)) - float(qtde_tot_venda)
#             if qtde_tot_atual > 0.0:
#                 preco_medio = UsuarioACAOEmpresaOperacao.buscar_preco_medio(id_usuario=id_usuario, id_ativo=int(row['ID']), dt_fim=dt_fim)
#                 vlr_tot_atual = (preco_medio * qtde_tot_atual) if preco_medio > 0.0 else 0.0
#                 vlr_tot_ant = 0.0
#                 if int(ano) > int(menor):
#                     qtde_tot_compra_ant = UsuarioACAOEmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_ativo=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_bonus_ant = UsuarioACAOEmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_ativo=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_venda_ant = UsuarioACAOEmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_ativo=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_ant = (float(qtde_tot_compra_ant) + float(qtde_tot_bonus_ant)) - float(qtde_tot_venda_ant)
#                     if qtde_tot_ant > 0.0:
#                         preco_medio_ant = UsuarioACAOEmpresaOperacao.buscar_preco_medio(id_usuario=id_usuario, id_ativo=int(row['ID']), dt_fim=dt_fim_ant)
#                         vlr_tot_ant = (preco_medio_ant * qtde_tot_ant) if preco_medio_ant > 0.0 else 0.0
#                 lista.append(['31 - Ações', str(row["CNPJ"]), 'Papel: ' + str(row["CODIGO"]) + ' - ' + str(row["RAZAOSOCIAL"]) + '<br/>' + 'Quantidade: ' + inteiro_to_str(valor=float(qtde_tot_atual)) + '<br/>Preço Médio de Compra: '+ decimal_to_str(valor=float(preco_medio)), decimal_to_str(valor=float(vlr_tot_ant)), decimal_to_str(valor=float(vlr_tot_atual)), str(row["CODIGO"]), 'ACAO'])
#
#         # ACAO - SOMENTE DIVIDENDOOS A RECEBER
#         rows = UsuarioACAOEmpresaProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='D', dt_pagto_ini=str(dt_ini_pos), dt_pagto_fim=str(dt_fim_pos), dt_ex_ini=str(dt_ini), dt_ex_fim=str(dt_fim))
#         lista += [['99 - Outros bens e direitos', str(row["CNPJ"]), 'Dividendos a Receber<br/>Empresa : ' + str(row["RAZAOSOCIAL"]) + '<br/> declarados em ' + str(ano) + ' e que serão pagos em ' + str(int(ano)+1), decimal_to_str(valor=0.0), decimal_to_str(valor=float(row["TOTVLR"])), str(row["CODIGO"]), 'DIV'] for row in rows]
#
#         # ACAO - SOMENTE JUROS SOBRE CAPITAL PROPRIO A RECEBER
#         rows = UsuarioACAOEmpresaProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='J', dt_pagto_ini=str(dt_ini_pos), dt_pagto_fim=str(dt_fim_pos), dt_ex_ini=str(dt_ini), dt_ex_fim=str(dt_fim))
#         lista += [['99 - Outros bens e direitos', str(row["CNPJ"]), 'Juros sobre Capital Próprio a Receber <br/> Empresa : ' + str(row["RAZAOSOCIAL"]) + '<br/> declarados em ' + str(ano) + ' e que serão pagos em ' + str(int(ano)+1), decimal_to_str(valor=0.0), decimal_to_str(valor=float(row["TOTVLR"])), str(row["CODIGO"]), 'JSCP'] for row in rows]
#
#         # FII - TODOS OS FIIs QUE VOCE TEM ATE O ANO DE DECLARACAO
#         rows = FiiFundoImob.buscar_lista_irpf(id_usuario=id_usuario, dt_fim=dt_fim)
#         for row in rows:
#             qtde_tot_compra = UsuarioFiiFundoImobLancamento.buscar_total_compra(id_usuario=id_usuario, id_fundo=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_bonus = UsuarioFiiFundoImobLancamento.buscar_total_bonus(id_usuario=id_usuario, id_fundo=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_venda = UsuarioFiiFundoImobLancamento.buscar_total_venda(id_usuario=id_usuario, id_fundo=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_atual = (float(qtde_tot_compra) + float(qtde_tot_bonus)) - float(qtde_tot_venda)
#             if qtde_tot_atual > 0.0:
#                 preco_medio = UsuarioFiiFundoImobLancamento.buscar_preco_medio(id_usuario=id_usuario, id_fundo=int(row['ID']), dt_fim=dt_fim)
#                 vlr_tot_atual = (preco_medio * qtde_tot_atual) if preco_medio > 0.0 else 0.0
#                 vlr_tot_ant = 0.0
#                 if int(ano) > int(menor):
#                     qtde_tot_compra_ant = UsuarioFiiFundoImobLancamento.buscar_total_compra(id_usuario=id_usuario, id_fundo=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_bonus_ant = UsuarioFiiFundoImobLancamento.buscar_total_bonus(id_usuario=id_usuario, id_fundo=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_venda_ant = UsuarioFiiFundoImobLancamento.buscar_total_venda(id_usuario=id_usuario, id_fundo=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_ant = (float(qtde_tot_compra_ant) + float(qtde_tot_bonus_ant)) - float(qtde_tot_venda_ant)
#                     if qtde_tot_ant > 0.0:
#                         preco_medio_ant = UsuarioFiiFundoImobLancamento.buscar_preco_medio(id_usuario=id_usuario, id_fundo=int(row['ID']), dt_fim=dt_fim_ant)
#                         vlr_tot_ant = (preco_medio_ant * qtde_tot_ant) if preco_medio_ant > 0.0 else 0.0
#                 # Número de Cotas, Nome do Fundo, CNPJ do Fundo, nome da Corretora de Valores custodiante e valor total da posição.
#                 # Cotas do FII "NOMEFII", CNPJ "CNPJFII", Qtde e Preço Medio
#                 lista.append(['73 - Fundo de Investimento Imobiliário', str(row["CNPJ"]), 'Fundo: ' + str(row["CODIGO"]) + ' - ' + str(row["RAZAOSOCIAL"]) + '<br/>' + 'Quantidade: ' + inteiro_to_str(valor=float(qtde_tot_atual)) + '<br/>Preço Médio de Compra: '+ decimal_to_str(valor=float(preco_medio)), decimal_to_str(valor=float(vlr_tot_ant)), decimal_to_str(valor=float(vlr_tot_atual)), str(row["CODIGO"]), 'FII'])
#
#         # ETF - TODOS OS ETFs QUE VOCE TEM ATE O ANO DE DECLARACAO
#         rows = ETFIndice.buscar_lista_irpf(id_usuario=id_usuario, dt_fim=dt_fim)
#         for row in rows:
#             qtde_tot_compra = UsuarioETFIndiceOperacao.buscar_total_compra(id_usuario=id_usuario, id_indice=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_bonus = UsuarioETFIndiceOperacao.buscar_total_bonus(id_usuario=id_usuario, id_indice=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_venda = UsuarioETFIndiceOperacao.buscar_total_venda(id_usuario=id_usuario, id_indice=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_atual = (float(qtde_tot_compra) + float(qtde_tot_bonus)) - float(qtde_tot_venda)
#             if qtde_tot_atual > 0.0:
#                 preco_medio = UsuarioETFIndiceOperacao.buscar_preco_medio(id_usuario=id_usuario, id_indice=int(row['ID']), dt_fim=dt_fim)
#                 vlr_tot_atual = (preco_medio * qtde_tot_atual) if preco_medio > 0.0 else 0.0
#                 vlr_tot_ant = 0.0
#                 if int(ano) > int(menor):
#                     qtde_tot_compra_ant = UsuarioETFIndiceOperacao.buscar_total_compra(id_usuario=id_usuario, id_indice=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_bonus_ant = UsuarioETFIndiceOperacao.buscar_total_bonus(id_usuario=id_usuario, id_indice=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_venda_ant = UsuarioETFIndiceOperacao.buscar_total_venda(id_usuario=id_usuario, id_indice=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_ant = (float(qtde_tot_compra_ant) + float(qtde_tot_bonus_ant)) - float(qtde_tot_venda_ant)
#                     if qtde_tot_ant > 0.0:
#                         preco_medio_ant = UsuarioETFIndiceOperacao.buscar_preco_medio(id_usuario=id_usuario, id_indice=int(row['ID']), dt_fim=dt_fim_ant)
#                         vlr_tot_ant = (preco_medio_ant * qtde_tot_ant) if preco_medio_ant > 0.0 else 0.0
#                 # Número de Cotas, Nome do Indice, CNPJ do Indice, nome da Corretora de Valores custodiante e valor total da posição.
#                 # Cotas do ETF "NOME-ETF", CNPJ "CNPJ-ETF", Qtde e Preço Medio
#                 lista.append(['74 - Fundo de ações, Fundos Mútuos de Privatização, <br/>Fundos de Investimento em Empresas Emergentes, <br/>Fundos de Investimento em Participação e Fundos de Investimentos de Índice de Mercado', str(row["CNPJ"]), 'Cotas do Fundo de Índice (ETF) - ' + str(row["CODIGO"]) + ' <br/> ' + str(row["RAZAOSOCIAL"]) + '<br/>' + 'Quantidade: ' + inteiro_to_str(valor=float(qtde_tot_atual)) + '<br/>Preço Médio de Compra: '+ decimal_to_str(valor=float(preco_medio)), decimal_to_str(valor=float(vlr_tot_ant)), decimal_to_str(valor=float(vlr_tot_atual)), str(row["CODIGO"]), 'ETF'])
#
#         # BDR - TODAS AS ACOES QUE VOCE TEM ATE O ANO DE DECLARACAO
#         rows = BDREmpresa.buscar_lista_irpf(id_usuario=id_usuario, dt_fim=dt_fim)
#         for row in rows:
#             qtde_tot_compra = UsuarioBDREmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_bdr=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_bonus = UsuarioBDREmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_bdr=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_venda = UsuarioBDREmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_bdr=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_atual = (float(qtde_tot_compra) + float(qtde_tot_bonus)) - float(qtde_tot_venda)
#             if qtde_tot_atual > 0.0:
#                 preco_medio = UsuarioBDREmpresaOperacao.buscar_preco_medio(id_usuario=id_usuario, id_bdr=int(row['ID']), dt_fim=dt_fim)
#                 vlr_tot_atual = (preco_medio * qtde_tot_atual) if preco_medio > 0.0 else 0.0
#                 vlr_tot_ant = 0.0
#                 if int(ano) > int(menor):
#                     qtde_tot_compra_ant = UsuarioBDREmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_bdr=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_bonus_ant = UsuarioBDREmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_bdr=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_venda_ant = UsuarioBDREmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_bdr=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_ant = (float(qtde_tot_compra_ant) + float(qtde_tot_bonus_ant)) - float(qtde_tot_venda_ant)
#                     if qtde_tot_ant > 0.0:
#                         preco_medio_ant = UsuarioBDREmpresaOperacao.buscar_preco_medio(id_usuario=id_usuario, id_bdr=int(row['ID']), dt_fim=dt_fim_ant)
#                         vlr_tot_ant = (preco_medio_ant * qtde_tot_ant) if preco_medio_ant > 0.0 else 0.0
#                 lista.append(['31 - Ações', str(row["CNPJ"]), 'Papel: ' + str(row["CODIGO"]) + ' - ' + str(row["RAZAOSOCIAL"]) + '<br/>' + 'Quantidade: ' + inteiro_to_str(valor=float(qtde_tot_atual)) + '<br/>Preço Médio de Compra: ' + decimal_to_str(valor=float(preco_medio)), decimal_to_str(valor=float(vlr_tot_ant)), decimal_to_str(valor=float(vlr_tot_atual)), str(row["CODIGO"]), 'BDR'])
#
#         # BDR - SOMENTE DIVIDENDOOS A RECEBER
#         rows = UsuarioBDREmpresaProvento.buscar_dados_grid_irpf(id_usuario=id_usuario, tipo='D', dt_pagto_ini=str(dt_ini_pos), dt_pagto_fim=str(dt_fim_pos), dt_ex_ini=str(dt_ini), dt_ex_fim=str(dt_fim))
#         lista += [['99 - Outros bens e direitos', str(row["CNPJ"]), 'Dividendos a Receber<br/>Empresa : ' + str(row["RAZAOSOCIAL"]) + '<br/> declarados em ' + str(ano) + ' e que serão pagos em ' + str(int(ano)+1), decimal_to_str(valor=0.0), decimal_to_str(valor=float(row["TOTVLR"])), str(row["CODIGO"]), 'DIV'] for row in rows]
#
#         # CRIPTO - TODOS OS CRIPTOs QUE VOCE TEM ATE O ANO DE DECLARACAO
#         rows = CriptoEmpresa.buscar_lista_irpf(id_usuario=id_usuario, dt_fim=dt_fim)
#         for row in rows:
#             codigo = str(row["CODIGO"])
#             qtde_tot_compra = UsuarioCriptoLancamento.buscar_total_compra(id_usuario=id_usuario, id_cripto=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_venda = UsuarioCriptoLancamento.buscar_total_venda(id_usuario=id_usuario, id_cripto=int(row['ID']), dt_fim=dt_fim)
#             qtde_tot_atual = float(qtde_tot_compra) - float(qtde_tot_venda)
#             if qtde_tot_atual > 0.0:
#                 preco_medio = UsuarioCriptoLancamento.buscar_preco_medio(id_usuario=id_usuario, id_cripto=int(row['ID']), dt_fim=dt_fim)
#                 vlr_tot_atual = (preco_medio * qtde_tot_atual) if preco_medio > 0.0 else 0.0
#                 vlr_tot_ant = 0.0
#                 if int(ano) > int(menor):
#                     qtde_tot_compra_ant = UsuarioCriptoLancamento.buscar_total_compra(id_usuario=id_usuario, id_cripto=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_venda_ant = UsuarioCriptoLancamento.buscar_total_venda(id_usuario=id_usuario, id_cripto=int(row['ID']), dt_fim=dt_fim_ant)
#                     qtde_tot_ant = float(qtde_tot_compra_ant) - float(qtde_tot_venda_ant)
#                     if qtde_tot_ant > 0.0:
#                         preco_medio_ant = UsuarioCriptoLancamento.buscar_preco_medio(id_usuario=id_usuario, id_cripto=int(row['ID']), dt_fim=dt_fim_ant)
#                         vlr_tot_ant = (preco_medio_ant * qtde_tot_ant) if preco_medio_ant > 0.0 else 0.0
#                 if codigo[:3] == 'BTC':
#                     lista.append(['81 - Criptoativo bitcoin (BTC)', '00.000.000/0000-00', 'Cripto: ' + codigo + ' - ' + str(row["NOME"]) + '<br/>' + 'Quantidade: ' + decimal_prov_to_str(valor=float(qtde_tot_atual)) + '<br/>Preço Médio de Compra: '+ decimal_prov_to_str(valor=float(preco_medio)) + ' <br/> Pegar o CNPJ e o Nome da Exchange/Corretora', decimal_to_str(valor=float(vlr_tot_ant)), decimal_to_str(valor=float(vlr_tot_atual)), codigo, 'CRIPTO'])
#                 elif codigo[:3] == 'ETH' or codigo[:3] == 'XRP' or codigo[:3] == 'LTC' or codigo[:3] == 'BCH' or codigo[:4] == 'USDT' or codigo[:4] == 'LINK':
#                     lista.append(['82 - Outras moedas digitais, conhecidas como “altcoins”, entre elas: <br>criptomoedas, como ether (ETH), XRP (ripple), litecoin (LTC) e bitcoin cash (BCH); <br>stable coins, como tether (USDT); e o chainlink (LINK)', '00.000.000/0000-00', 'Cripto: ' + codigo + ' - ' + str(row["NOME"]) + '<br/>' + 'Quantidade: ' + decimal_prov_to_str(valor=float(qtde_tot_atual)) + '<br/>Preço Médio de Compra: ' + decimal_prov_to_str(valor=float(preco_medio)) + ' <br/> Pegar o CNPJ e o Nome da Exchange/Corretora', decimal_to_str(valor=float(vlr_tot_ant)), decimal_to_str(valor=float(vlr_tot_atual)), codigo, 'CRIPTO'])
#                 else:
#                     lista.append(['89 - Demais criptoativos, para ativos digitais que não são criptomoedas, mas tokens utilitários ou de segurança', '00.000.000/0000-00', 'Cripto: ' + codigo + ' - ' + str(row["NOME"]) + '<br/>' + 'Quantidade: ' + decimal_prov_to_str(valor=float(qtde_tot_atual)) + '<br/>Preço Médio de Compra: ' + decimal_prov_to_str(valor=float(preco_medio)) + ' <br/> Pegar o CNPJ e o Nome da Exchange/Corretora', decimal_to_str(valor=float(vlr_tot_ant)), decimal_to_str(valor=float(vlr_tot_atual)), codigo, 'CRIPTO'])
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_irpf.route('/gridBensEDiretosDetalhe', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def ggrid_bens_e_diretos_detalhe():
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
# @bp_irpf.route('/gridRendaVariavel', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_renda_variavel():
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
#             ano_declaracao = data.get('AnoDeclaracao')
#             calc_vlr_superior = data.get('CalcVlrSuperior')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not ano_declaracao: return make_response(get_json_retorno_dados(msg='Ano Declaracao não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         if not calc_vlr_superior:
#             config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo='APURACAO_COMPENSAR_PREJUIZO')
#             calc_vlr_superior = config.valor if config else 'S'
#
#         if not calc_vlr_superior: calc_vlr_superior = 'N'
#
#         anos = []
#         anos.append(str(ano_declaracao)+'0101')
#         anos.append(UsuarioApuracao.get_menor_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioACAOEmpresaLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioETFIndiceLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioBDREmpresaLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#
#         try:
#             menor = min(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#         except:
#             menor = None
#
#         if not menor: return make_response(get_json_retorno_dados(rslt='OK'), 200)
#
#         merc_avst_comun, merc_avst_trade = 0.0, 0.0
#         result_liq_comum, result_liq_trade = 0.0, 0.0
#         result_neg_comum, result_neg_trade = 0.0, 0.0
#         result_base_comum, result_base_trade = 0.0, 0.0
#         result_prej_comum, result_prej_trade = 0.0, 0.0
#         result_dev_comum, result_dev_trade = 0.0, 0.0
#         result_prej_comum_anterior, result_prej_trade_anterior = 0.0, 0.0
#         consold_devido = 0.0
#         consold_trade_mes_atual, consold_trade_mes_ant = 0.0, 0.0
#         consold_trade_compensar, consold_comun_compensar = 0.0, 0.0
#         consold_comun_mes_atual, consold_comun_mes_ant = 0.0, 0.0
#         consold_pagar = 0.0
#         vlr_saldo_comun, etf_vlr_saldo_comun, vlr_saldo_trade = 0.0, 0.0, 0.0
#
#         ano_atual = pegar_data_atual(fmt='%Y')
#         mes_atual = pegar_data_atual(fmt='%m')
#         dados = dict({})
#
#         for ano in range(menor, int(ano_declaracao) + 1):
#             for mes in range(1, 13):
#
#                 if int(ano) == int(ano_atual) and int(mes) > int(mes_atual): break
#
#                 ano_mes = str(ano) + str(mes).zfill(2)
#                 vlr_apurado_comun, vlr_venda_comun, vlr_a_compensar_comun, vlr_resultado_comun, vlr_imposto_devido_comun, vlr_imposto_pago_comun, vlr_imposto_a_pagar_comun = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#                 etf_vlr_apurado_comun, etf_vlr_imposto_pago_comun, etf_vlr_a_compensar_comun, etf_vlr_resultado_comun, etf_vlr_imposto_devido_comun, etf_vlr_imposto_a_pagar_comun = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#                 vlr_apurado_trade, vlr_a_compensar_trade, vlr_resultado_trade, vlr_imposto_devido_trade, vlr_imposto_pago_trade, vlr_imposto_a_pagar_trade = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
#
#                 # ==================================================================================================================
#
#                 # ACAO - COMUM
#
#                 rows = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria="C", ano_mes=ano_mes)  # M-Manual # C-ACAO-Comum
#                 for row in rows:
#                     vlr_apurado_comun += float(row.valor) if row.valor else 0.0
#                     vlr_venda_comun += float(row.valor) if row.valor else 0.0
#
#                 rows = UsuarioACAOEmpresaOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes + "01", dt_fim=ano_mes + "31", categoria="C", tipo="V", troca="N")  # C-Comum # V-Vendas
#                 for row in rows:
#                     vlr_valorizacao = UsuarioACAOEmpresaOperacao.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO']))
#                     vlr_apurado_comun += float(vlr_valorizacao)
#                     vlr_venda_comun += float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0
#                     lanc = UsuarioACAOEmpresaLancamento.buscar_por_id(id_usuario=id_usuario, id=int(row['IDLANC']))
#                     if lanc: vlr_imposto_pago_comun += float(lanc['VLRTXIRRF']) if lanc['VLRTXIRRF'] else 0.0
#
#                 # ==================================================================================================================
#
#                 # ETF - COMUM
#
#                 rows = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria="E", ano_mes=ano_mes)  # M-Manual # E-ETF-Comum
#                 for row in rows:
#                     etf_vlr_apurado_comun += float(row.valor) if row.valor else 0.0
#
#                 rows = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes+"01", dt_fim=ano_mes+"31", categoria='C', tipo="V", troca="N") # C-Comum // V-Vendas
#                 for row in rows:
#                     vlr_valorizacao = UsuarioETFIndiceOperacao.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO']))
#                     etf_vlr_apurado_comun += float(vlr_valorizacao)
#                     lanc = UsuarioETFIndiceLancamento.buscar_por_id(id_usuario=id_usuario, id=int(row['IDLANC']))
#                     if lanc: etf_vlr_imposto_pago_comun += float(lanc['VLRTXIRRF']) if lanc['VLRTXIRRF'] else 0.0
#
#                 # ==================================================================================================================
#
#                 if float(vlr_apurado_comun) <= 0.0:
#                     vlr_saldo_comun += float(vlr_apurado_comun)
#                 elif float(vlr_apurado_comun) > 0.0:
#                     if calc_vlr_superior == "N":
#                         vlr_saldo_comun += float(vlr_apurado_comun)
#                     elif calc_vlr_superior == "S" and float(vlr_venda_comun) > 20000.0:
#                         vlr_saldo_comun += float(vlr_apurado_comun)
#
#                 if float(vlr_saldo_comun) < 0.0: vlr_a_compensar_comun = float(vlr_saldo_comun)
#                 if float(vlr_saldo_comun) > 0.0: vlr_resultado_comun = float(vlr_saldo_comun)
#                 if float(vlr_venda_comun) > 20000.0 and vlr_resultado_comun > 0.0: vlr_imposto_devido_comun = (float(vlr_resultado_comun) * 15) / 100
#                 if float(vlr_imposto_devido_comun) > 0.0: vlr_imposto_a_pagar_comun = float(vlr_imposto_devido_comun) - float(vlr_imposto_pago_comun)
#
#                 etf_vlr_saldo_comun += float(etf_vlr_apurado_comun)
#
#                 if float(etf_vlr_saldo_comun) < 0.0: etf_vlr_a_compensar_comun = float(etf_vlr_saldo_comun)
#                 if float(etf_vlr_saldo_comun) > 0.0: etf_vlr_resultado_comun = float(etf_vlr_saldo_comun)
#                 if float(etf_vlr_resultado_comun) > 0.0: etf_vlr_imposto_devido_comun = (float(etf_vlr_resultado_comun) * 15) / 100
#                 if float(etf_vlr_imposto_devido_comun) > 0.0: etf_vlr_imposto_a_pagar_comun = float(etf_vlr_imposto_devido_comun) - float(etf_vlr_imposto_pago_comun)
#
#                 merc_avst_comun = float(etf_vlr_apurado_comun)
#                 result_liq_comum = float(etf_vlr_apurado_comun)
#                 if float(vlr_venda_comun) > 20000.0 or float(vlr_apurado_comun) < 0.0:
#                     merc_avst_comun  = float(vlr_apurado_comun) + float(etf_vlr_apurado_comun)
#                     result_liq_comum = float(vlr_apurado_comun) + float(etf_vlr_apurado_comun)
#
#                 result_neg_comum = float(result_prej_comum_anterior)
#                 result_base_comum = (float(vlr_saldo_comun) + float(etf_vlr_saldo_comun)) if float(vlr_saldo_comun) + float(etf_vlr_saldo_comun) > 0.0 else 0.0
#                 result_prej_comum = ((float(vlr_saldo_comun) + float(etf_vlr_saldo_comun)) * -1) if float(vlr_saldo_comun) + float(etf_vlr_saldo_comun) < 0.0 else 0.0
#                 result_dev_comum = float(vlr_imposto_devido_comun) + float(etf_vlr_imposto_devido_comun)
#
#                 result_prej_comum_anterior = (float(result_prej_comum) * -1) if (float(result_prej_comum) < 0.0) else float(result_prej_comum)
#
#                 # ==================================================================================================================
#
#                 # ACAO - DAY TRADE
#
#                 rows = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria="D", ano_mes=ano_mes)  # M-Manual # D-ACAO-DayTrade
#                 for row in rows:
#                     vlr_apurado_trade += float(row.valor) if row.valor else 0.0
#
#                 rows = UsuarioACAOEmpresaOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes + "01", dt_fim=ano_mes + "31", categoria="D", tipo="V", troca="N")  # D-DayTrade # V-Vendas
#                 for row in rows:
#                     vlr_valorizacao = UsuarioACAOEmpresaOperacao.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO']))
#                     vlr_apurado_trade += float(vlr_valorizacao)
#                     lanc = UsuarioACAOEmpresaLancamento.buscar_por_id(id_usuario=id_usuario, id=int(row['IDLANC']))
#                     if lanc: vlr_imposto_pago_trade += float(lanc['VLRTXIRRF']) if lanc['VLRTXIRRF'] else 0.0
#
#                 # ==================================================================================================================
#
#                 # ETF - DAY TRADE
#
#                 rows = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria="G", ano_mes=ano_mes)  # M-Manual # G-ETF-DayTrade
#                 for row in rows:
#                     vlr_apurado_trade += float(row.valor) if row.valor else 0.0
#
#                 rows = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, dt_ini=ano_mes+"01", dt_fim=ano_mes+"31", categoria='D', tipo="V", troca="N") # D-DayTrade // V-Vendas
#                 for row in rows:
#                     vlr_valorizacao = UsuarioETFIndiceOperacao.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO']))
#                     vlr_apurado_trade += float(vlr_valorizacao)
#                     lanc = UsuarioETFIndiceLancamento.buscar_por_id(id_usuario=id_usuario, id=int(row['IDLANC']))
#                     if lanc: vlr_imposto_pago_trade += float(lanc['VLRTXIRRF']) if lanc['VLRTXIRRF'] else 0.0
#
#                 # ==================================================================================================================
#
#                 vlr_saldo_trade += float(vlr_apurado_trade)
#                 if float(vlr_saldo_trade) < 0.0: vlr_a_compensar_trade = float(vlr_saldo_trade)
#                 if float(vlr_saldo_trade) > 0.0: vlr_resultado_trade = float(vlr_saldo_trade)
#                 if float(vlr_resultado_trade) > 0.0: vlr_imposto_devido_trade = (float(vlr_resultado_trade) * 20) / 100
#
#                 if float(vlr_imposto_devido_trade) > 0.0: vlr_imposto_a_pagar_trade = float(vlr_imposto_devido_trade) - float(vlr_imposto_pago_trade)
#
#                 merc_avst_trade = float(vlr_apurado_trade)
#                 result_liq_trade = float(vlr_apurado_trade)
#                 result_neg_trade = float(result_prej_trade_anterior)
#                 result_base_trade = float(vlr_saldo_trade) if float(vlr_saldo_trade) > 0.0 else 0.0
#                 result_prej_trade = float(vlr_saldo_trade) * -1 if float(vlr_saldo_trade) < 0.0 else 0.0
#                 result_dev_trade = float(vlr_imposto_devido_trade)
#                 result_prej_trade_anterior = float(result_prej_trade) * -1 if float(result_prej_trade) < 0.0 else float(result_prej_trade)
#
#                 consold_devido  = float(vlr_imposto_devido_comun) + float(etf_vlr_imposto_devido_comun) + float(vlr_imposto_devido_trade)
#
#                 consold_trade_mes_atual = float(vlr_imposto_pago_trade)
#                 consold_trade_mes_ant = 0.0
#                 consold_trade_compensar = 0.0
#
#                 consold_comun_mes_atual = float(vlr_imposto_pago_comun) + float(etf_vlr_imposto_pago_comun)
#                 consold_comun_mes_ant = 0.0
#                 consold_comun_compensar = 0.0
#
#                 consold_pagar = float(vlr_imposto_a_pagar_comun) + float(etf_vlr_imposto_a_pagar_comun) + float(vlr_imposto_a_pagar_trade)
#
#                 if str(ano) == str(ano_declaracao):
#                     dados[str(buscar_nome_mes_resumido(int(mes)))] = {
#                         "MercAvst": [decimal_to_str(valor=float(merc_avst_comun)), decimal_to_str(valor=float(merc_avst_trade))],
#                         "ResultLiq": [decimal_to_str(valor=float(result_liq_comum)), decimal_to_str(valor=float(result_liq_trade)), decimal_to_str(valor=float(result_neg_comum)), decimal_to_str(valor=float(result_neg_trade)), decimal_to_str(valor=float(result_base_comum)), decimal_to_str(valor=float(result_base_trade)), decimal_to_str(valor=float(result_prej_comum)), decimal_to_str(valor=float(result_prej_trade)), decimal_to_str(valor=float(result_dev_comum)), decimal_to_str(valor=float(result_dev_trade))],
#                         "Consolid": [decimal_to_str(valor=float(consold_devido)), decimal_to_str(valor=float(consold_trade_mes_atual)), decimal_to_str(valor=float(consold_trade_mes_ant)), decimal_to_str(valor=float(consold_trade_compensar)), decimal_to_str(valor=float(consold_comun_mes_atual)), decimal_to_str(valor=float(consold_comun_mes_ant)), decimal_to_str(valor=float(consold_comun_compensar)), decimal_to_str(valor=float(consold_pagar))]
#                     }
#
#                 if float(vlr_saldo_comun) > 0.0: vlr_saldo_comun = 0.0
#                 if float(etf_vlr_saldo_comun) > 0.0: etf_vlr_saldo_comun = 0.0
#                 if float(vlr_saldo_trade) > 0.0: vlr_saldo_trade = 0.0
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_irpf.route('/gridRendaVariavelFII', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_renda_variavel_fii():
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
#             ano_declaracao = data.get('AnoDeclaracao')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not ano_declaracao: return make_response(get_json_retorno_dados(msg='Ano Declaracao não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         anos = []
#         anos.append(str(ano_declaracao)+'0101')
#         anos.append(UsuarioApuracao.get_menor_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioFiiFundoImobLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#
#         try:
#             menor = min(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
#         except:
#             menor = None
#
#         if not menor: return make_response(get_json_retorno_dados(rslt='OK'), 200)
#
#         aliquota_ir = 20.0
#         result_neg_mes_ant = 0.0
#         preju_a_comp = 0.0
#         ano_atual = pegar_data_atual(fmt='%Y')
#         mes_atual = pegar_data_atual(fmt='%m')
#         dados = dict({})
#
#         for ano in range(menor, int(ano_declaracao) + 1):
#             for mes in range(1, 13):
#                 if int(ano) == int(ano_atual) and int(mes) > int(mes_atual): break
#                 ano_mes = str(ano) + str(mes).zfill(2)
#                 result_liq_mes = 0.0
#                 ir_devido = 0.0
#                 vlr_ir_pag = 0.0
#                 rows = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, dt_ini=str(ano_mes)+"01", dt_fim=str(ano_mes)+"31", tipo="V", troca="N")
#                 for row in rows:
#                     vlr_valorizacao = UsuarioFiiFundoImobLancamento.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO']))
#                     result_liq_mes += float(vlr_valorizacao)
#                     vlr_ir_pag += float(row['VLRTXIRRF']) if row['VLRTXIRRF'] else 0.0
#                 rows = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria="F", ano_mes=str(ano_mes))
#                 for row in rows:
#                     result_liq_mes += float(row.valor) if row.valor else 0.0
#                 base_cacl_ir = result_liq_mes - result_neg_mes_ant
#                 if base_cacl_ir < 0.0: preju_a_comp = (base_cacl_ir * -1)
#                 if base_cacl_ir > 0.0: preju_a_comp = 0.0
#                 if preju_a_comp < 0.0: preju_a_comp= 0.0
#                 if base_cacl_ir > 0.0: ir_devido = (base_cacl_ir * 20) / 100
#                 if base_cacl_ir <= 0.0: base_cacl_ir= 0.0
#                 if ir_devido > 0.0: ir_devido -= vlr_ir_pag
#                 if str(ano) == str(ano_declaracao):
#                     dados[str(buscar_nome_mes_resumido(int(mes)))] = {"ResultLiqMes": decimal_to_str(valor=float(result_liq_mes)), "ResultNegMesAnt": decimal_to_str(valor=float(result_neg_mes_ant)), "BaseCaclIR": decimal_to_str(valor=float(base_cacl_ir)), "PrejuAComp": decimal_to_str(valor=float(preju_a_comp)), "AliquotaIR": decimal_to_str(valor=float(aliquota_ir)), "IRDevido": decimal_to_str(valor=float(ir_devido))}
#                 result_neg_mes_ant = preju_a_comp
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
