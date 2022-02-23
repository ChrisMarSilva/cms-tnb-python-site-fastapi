# # -*- coding: utf-8 -*-
# import sys
# import os
# from math import floor, ceil
# from flask import Blueprint, render_template, make_response, request
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.acao_empresa import ACAOEmpresa
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.acao_empresa_ativo_cotacao_hist import ACAOEmpresaAtivoCotacaoHist
# from app.models.acao_empresa_provento import ACAOEmpresaProvento
# from app.models.acao_empresa_fato_relevante import ACAOEmpresaFatoRelevante
# from app.models.acao_empresa_financeiro import ACAOEmpresaFinanceiro
# from app.models.acao_empresa_financeiro_bpa_anual import ACAOEmpresaFinanceiroBPAAnual
# from app.models.acao_empresa_financeiro_bpa_trimestral import ACAOEmpresaFinanceiroBPATrimestral
# from app.models.acao_empresa_financeiro_bpp_anual import ACAOEmpresaFinanceiroBPPAnual
# from app.models.acao_empresa_financeiro_bpp_trimestral import ACAOEmpresaFinanceiroBPPTrimestral
# from app.models.acao_empresa_financeiro_dre_anual import ACAOEmpresaFinanceiroDREAnual
# from app.models.acao_empresa_financeiro_dre_trimestral import ACAOEmpresaFinanceiroDRETrimestral
# from app.models.acao_empresa_financeiro_dfc_anual import ACAOEmpresaFinanceiroDFCAnual
# from app.models.acao_empresa_financeiro_dfc_trimestral import ACAOEmpresaFinanceiroDFCTrimestral
# from app.models.usuario_carteira_acao import UsuarioCarteiraAcao
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str, decimal_resumido, decimal_prov_to_str
# from app.util.util_json import get_json_retorno_grid, get_json_retorno_dados
# from app.util.util_datahora import  converter_datetime_str, pegar_data_atual, adicionar_meses
#
#
# bp_finan_acoes = Blueprint('finan_acoes', __name__, url_prefix='/finan/acoes')
#
#
# @bp_finan_acoes.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     return render_template(template_name_or_list="finan_acoes.html")
#
#
# @bp_finan_acoes.route("/<codigo>", methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index_codigo(codigo: str = None):
#     return render_template(template_name_or_list="finan_acoes_codigo.html", codigo=str(codigo).strip().upper())
#
#
# @bp_finan_acoes.route('/filtros')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def filtros():
#     return render_template(template_name_or_list="finan_acoes_filtros.html")
#
#
# @bp_finan_acoes.route('/grid', methods=['GET', 'POST'])
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
#             filtro_tipo = data.get('FiltroTipo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         lista = []
#
#         if filtro_tipo == "M":  # M-MeusAtivos
#             id_usuario = current_user.id
#             rows = UsuarioCarteiraAcao.buscar_todos(id_usuario=id_usuario, id_carteira=None, situacao='A')
#             lista = [
#                 {
#                     "nome": str(row['NOMRESUMIDOEMPRESA']),
#                     "codigos": [str(row['CODIGOATIVO'])],
#                     "logo": '/static/pages/ativos/' + str(row['CODIGOATIVO'])[0:4] + '.gif' if row['CODIGOATIVO'] else '',
#                     "cotacao": float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] and float(row['VLRPRECOFECHAMENTO']) > 0.0 else 0.0,
#                     "variacao_percent": float(row['VLRVARIACAO']) if row['VLRVARIACAO'] and float(row['VLRVARIACAO']) != 0.0 else 0.0,
#                     "variacao_valor": (float(row['VLRPRECOFECHAMENTO']) - float(row['VLRPRECOANTERIOR'])) if row['VLRPRECOFECHAMENTO'] and row['VLRPRECOANTERIOR'] else 0.0,
#                 }
#                 for row in rows
#             ]
#         else:
#
#             rows = ACAOEmpresaAtivo.get_all()
#             lista_codigos = [
#                 {
#                     "id": int(row.id),
#                     "idEmpresa": int(row.id_empresa) if row.id_empresa else 0,
#                     "codigo": str(row.codigo) if row.codigo else '',
#                 }
#                 for row in rows if row.codigo and row.situacao == "A"
#             ]
#
#             rows = ACAOEmpresa.buscar_todos()
#             for row in rows:
#                 id_empresa = int(row['ID'])
#                 nome = str(row['NOME']) if row['NOME'] else ''
#                 nome_resumo = str(row['NOMRESUMIDO']) if row['NOMRESUMIDO'] else ''
#                 setor = str(row['DESCRICAOSETOR']) if row['DESCRICAOSETOR'] else 'Não Classificado'
#                 subsetor = str(row['DESCRICAOSUBSETOR']) if row['DESCRICAOSUBSETOR'] else 'Não Classificado'
#                 segmento = str(row['DESCRICAOSEGMENTO']) if row['DESCRICAOSEGMENTO'] else 'Não Classificado'
#                 if nome in ['Ibovespa', 'Índice Brasil 100', 'Índice Dividendos', 'Índice Small Cap']: continue  # ['IBOV', 'IBXX', 'IDIV', 'SMLL']
#                 codigos = [ativo['codigo'] for ativo in lista_codigos if int(ativo['idEmpresa']) == int(id_empresa)]
#                 logo = '/static/pages/ativos/' + codigos[0][0:4] + '.gif' if codigos else ''
#                 lista.append({"nome": nome_resumo if nome_resumo else nome, "codigos": codigos, "logo": logo, "setor": setor, "subsetor": subsetor, "segmento": segmento})
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_finan_acoes.route('/carregar', methods=['GET', 'POST'])
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
#         if not data: return make_response('Dados não informado!', 200)
#
#         try:
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response('Dados não informado!', 200)
#
#         if not codigo:
#             return make_response('Ativo não informado!', 200)
#
#         codigo = str(codigo).strip().upper()
#
#         empresa = ACAOEmpresa.buscar_por_codigo(codigo=codigo)
#         if not empresa:
#             return make_response('Empresa não localizada!', 200)
#
#         id_empresa = int(empresa['ID'])
#         cod_cvm = str(empresa['CODCVM'])
#
#         rows = ACAOEmpresaAtivo.get_all_by_empresa(id_empresa=id_empresa)
#         lista_codigos = [
#             str(row.codigo)
#             for row in rows
#             if row.codigo and row.situacao == "A"
#         ]
#
#         ult_balanco = ''
#         row = ACAOEmpresaFinanceiro.get_by_cod_cvmd(cod_cvm=cod_cvm)
#         if row: ult_balanco = row.ult_tri_refer if row.ult_tri_refer else row.ult_ano_refer
#
#         dados = dict({
#             "nome": str(empresa['NOMRESUMIDO']) if empresa['NOMRESUMIDO'] else empresa['NOME'],
#             "nomeRazaoSocial": str(empresa['RAZAOSOCIAL']) if empresa['RAZAOSOCIAL'] else '',
#             "cnpj": str(empresa['CNPJ']) if empresa['CNPJ'] else '',
#             "setor": str(empresa['DESCRICAOSETOR']) if empresa['DESCRICAOSETOR'] else '',
#             "subsetor": str(empresa['DESCRICAOSUBSETOR']) if empresa['DESCRICAOSUBSETOR'] else '',
#             "segmeto": str(empresa['DESCRICAOSEGMENTO']) if empresa['DESCRICAOSEGMENTO'] else '',
#             "codigos": lista_codigos,
#             "siteRI": str(empresa['SITE']) if empresa['SITE'] else '',
#             "governanca": str(empresa['TIPO_MERCADO']).replace('NM - ', '').replace('N1 - ', '').replace('N2 - ', '').replace('MA - ', '').replace('DR3 - ', '') if empresa['TIPO_MERCADO'] else '',
#             "ultBalanco": ult_balanco if ult_balanco else '',
#         })
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_finan_acoes.route('/grid_demonst_result', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
# def grid_demonst_result():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response('Dados não informado!', 200)
#
#         try:
#             codigo = data.get('CodAtivo')
#             tipo_finan = data.get('TipoFinan')
#         except:
#             return make_response('Dados não informado!', 200)
#
#         if not codigo: return make_response('Ativo não informado!', 200)
#
#         codigo = str(codigo).strip().upper()
#         empresa = ACAOEmpresa.buscar_por_codigo(codigo=codigo)
#         if not empresa:
#             return make_response('Empresa não localizada!', 200)
#
#         cod_cvm = str(empresa['CODCVM'])
#
#         rows = None
#         if tipo_finan == "A":  # A-Anual
#             rows = ACAOEmpresaFinanceiroDREAnual.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         elif tipo_finan == "T":  # T-Trimestral
#             rows = ACAOEmpresaFinanceiroDRETrimestral.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         if not rows:
#             return make_response('NENHUM RESULTADO ENCONTRADO', 200)
#
#         lista = [
#             {
#                 "ANO_REFER": str(row.ano_refer),
#                 "TRI_REFER": str(row.ano_refer) if tipo_finan == "A" else str(row.tri_refer),
#                 "VLR_RECEITA_LIQ": float(row.vlr_receita_liq),
#                 "VLR_CUSTO": float(row.vlr_custo),
#                 "VLR_LUCRO_BRUTO": float(row.vlr_lucro_bruto),
#                 "VLR_MARGEM_BRUTA": float(row.vlr_margem_bruta) if row.vlr_margem_bruta else 0.0,
#                 "VLR_DESPESA_OPERAC": float(row.vlr_despesa_operac),
#                 "VLR_RESULTADO_OPERAC": float(row.vlr_resultado_operac),
#                 "VLR_MARGEM_OPERAC": float(row.vlr_margem_operac) if row.vlr_margem_operac else 0.0,
#                 "VLR_RESULTADO_FINAN": float(row.vlr_resultado_finan),
#                 "VLR_RESULTADO_ANTES_IR": float(row.vlr_resultado_antes_ir),
#                 "VLR_IMPOSTO": float(row.vlr_imposto),
#                 "VLR_OPERAC_CONT": float(row.vlr_operac_cont),
#                 "VLR_OPERAC_DESCONT": float(row.vlr_operac_descont),
#                 "VLR_LUCRO_LIQUIDO": float(row.vlr_lucro_liquido),
#                 "VLR_MARGEM_LIQUIDA": float(row.vlr_margem_liquida) if row.vlr_margem_liquida else 0.0,
#             }
#             for row in rows
#         ]
#
#         linha_titulo             = '</th> <th width="40px">Descrição</th>'
#         linha_receita_liq        = '<td class="text-left"> &emsp; Receita Líquida</td>'
#         linha_custo              = '<td class="text-left"> &emsp; &emsp; &emsp; Custos</td>'
#         linha_lucro_bruto        = '<td class="text-left"> &emsp; Lucro Bruto</td>'
#         linha_despesa_operac     = '<td class="text-left"> &emsp; &emsp; &emsp; Despesas/Receitas Operacionais</td>'
#         linha_resultado_operac   = '<td class="text-left"> &emsp; Resultado Operacional</td>'
#         linha_resultado_finan    = '<td class="text-left"> &emsp; &emsp; &emsp; Resultado Financeiro</td>'
#         linha_resultado_antes_ir = '<td class="text-left"> &emsp; Resultado Antes dos Tributos</td>'
#         linha_imposto            = '<td class="text-left"> &emsp; &emsp; &emsp; Impostos</td>'
#         linha_operac_cont        = '<td class="text-left"> &emsp; Operações Continuadas</td>'
#         linha_operac_descont     = '<td class="text-left"> &emsp; &emsp; &emsp; Operações Descontinuadas</td>'
#         linha_lucro_liquido      = '<td class="text-left"> &emsp; Lucro Líquido</td>'
#         linha_margem_bruta       = '<td class="text-left"> &emsp; &emsp; &emsp; Margem Bruta</td>'
#         linha_margem_operac      = '<td class="text-left"> &emsp; &emsp; &emsp; Margem Operacional</td>'
#         linha_margem_liquida     = '<td class="text-left"> &emsp; &emsp; &emsp; Margem Líquida</td>'
#
#         fator = 0.0
#
#         lista = sorted(lista, reverse=True, key=lambda k: (k['ANO_REFER'], k['TRI_REFER']))
#
#         for indx, row in enumerate(lista):
#             if fator == 0.0: fator = 1000000 if float(row['VLR_RECEITA_LIQ']) >= 1000000000 else 1000
#             if tipo_finan == "T" and indx > 7: break  # somente os ultimos 8
#             linha_titulo             += '<th class="text-right" width="40px">' + row['TRI_REFER'] + '</th>'
#             linha_receita_liq        += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_RECEITA_LIQ']) + '</td>'
#             linha_custo              += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CUSTO']) + '</td>'
#             linha_lucro_bruto        += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_LUCRO_BRUTO']) + '</td>'
#             linha_despesa_operac     += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_DESPESA_OPERAC']) + '</td>'
#             linha_resultado_operac   += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_RESULTADO_OPERAC']) + '</td>'
#             linha_resultado_finan    += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_RESULTADO_FINAN']) + '</td>'
#             linha_resultado_antes_ir += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_RESULTADO_ANTES_IR']) + '</td>'
#             linha_imposto            += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_IMPOSTO']) + '</td>'
#             linha_operac_cont        += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_OPERAC_CONT']) + '</td>'
#             linha_operac_descont     += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_OPERAC_DESCONT']) + '</td>'
#             linha_lucro_liquido      += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_LUCRO_LIQUIDO']) + '</td>'  # font-weight-bold
#             linha_margem_bruta       += '<td class="text-right text-muted" style="font-size: 11px;">' + decimal_to_str(valor=float(row['VLR_MARGEM_BRUTA'])) + '%</td>'
#             linha_margem_operac      += '<td class="text-right text-muted" style="font-size: 11px;">' + decimal_to_str(valor=float(row['VLR_MARGEM_OPERAC'])) + '%</td>'
#             linha_margem_liquida     += '<td class="text-right text-muted" style="font-size: 11px;">' + decimal_to_str(valor=float(row['VLR_MARGEM_LIQUIDA'])) + '%</td>'
#
#         result = ''
#         result += '<div class="table-responsive">'
#         result += '<table style="font-size: 12px" class="table table-sm table-hover table-condensed nowrap" cellspacing="0" width="100%">'
#         result += '<thead>'
#         result += '<tr style="font-size: 14px" class="thead-dark font-weight-bold">' + linha_titulo + '</tr>'
#         result += '</thead>'
#         result += '<tbody>'
#         result += '<tr>' + linha_receita_liq + '</tr>'
#         result += '<tr>' + linha_custo + '</tr>'
#         result += '<tr>' + linha_lucro_bruto + '</tr>'
#         result += '<tr>' + linha_despesa_operac + '</tr>'
#         result += '<tr>' + linha_resultado_operac + '</tr>'
#         result += '<tr>' + linha_resultado_finan + '</tr>'
#         result += '<tr>' + linha_resultado_antes_ir + '</tr>'
#         result += '<tr>' + linha_imposto + '</tr>'
#         result += '<tr>' + linha_operac_cont + '</tr>'
#         result += '<tr>' + linha_operac_descont + '</tr>'
#         result += '<tr>' + linha_lucro_liquido + '</tr>'
#         result += '<tr>' + linha_margem_bruta + '</tr>'
#         result += '<tr>' + linha_margem_operac + '</tr>'
#         result += '<tr>' + linha_margem_liquida + '</tr>'
#         result += '</tbody>'
#         result += '</table>'
#         result += '</div>'
#
#         return make_response(result, 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(LogErro.descricao_erro(texto=str(e)), 200)
#
#
# @bp_finan_acoes.route('/grid_fluxo_caixa', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
# def grid_fluxo_caixa():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response('Dados não informado!', 200)
#
#         try:
#             codigo = data.get('CodAtivo')
#             tipo_finan = data.get('TipoFinan')
#         except:
#             return make_response('Dados não informado!', 200)
#
#         if not codigo: return make_response('Ativo não informado!', 200)
#
#         codigo = str(codigo).strip().upper()
#         empresa = ACAOEmpresa.buscar_por_codigo(codigo=codigo)
#         if not empresa:
#             return make_response('Empresa não localizada!', 200)
#
#         cod_cvm = str(empresa['CODCVM'])
#
#         rows = None
#         if tipo_finan == "A":  # A-Anual
#             rows = ACAOEmpresaFinanceiroDFCAnual.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         elif tipo_finan == "T":  # T-Trimestral
#             rows = ACAOEmpresaFinanceiroDFCTrimestral.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         if not rows:
#             return make_response('NENHUM RESULTADO ENCONTRADO', 200)
#
#         lista = [
#             {
#                 "ANO_REFER": str(row.ano_refer),
#                 "TRI_REFER": str(row.ano_refer) if tipo_finan == "A" else str(row.tri_refer),
#                 "VLR_CAIXA_LIQUIDO_OPERAC": float(row.vlr_caixa_liquido_operac),
#                 "VLR_CAIXA_LIQUIDO_OPERAC_CAIXA_GERADO": float(row.vlr_caixa_liquido_operac_gerado),
#                 "VLR_CAIXA_LIQUIDO_OPERAC_VARIACOES": float(row.vlr_caixa_liquido_operac_variacoes),
#                 "VLR_CAIXA_LIQUIDO_OPERAC_OUTROS": float(row.vlr_caixa_liquido_operac_outros),
#                 "VLR_CAIXA_LIQUIDO_OPERAC_DEPRECIACAO_AMORTIZACAO": float(row.vlr_caixa_liquido_operac_depre_amort),
#                 "VLR_CAIXA_LIQUIDO_INVEST": float(row.vlr_caixa_liquido_invest),
#                 "VLR_CAIXA_LIQUIDO_FINAN": float(row.vlr_caixa_liquido_finan),
#                 "VLR_VARIACOES_CAMBIAL": float(row.vlr_variacao_cambial),
#                 "VLR_CAIXA_EQUIVALENTE": float(row.vlr_caixa_equivalente),
#                 "VLR_CAIXA_EQUIVALENTE_SALDO_INICIA": float(row.vlr_caixa_equivalente_saldo_ini),
#                 "VLR_CAIXA_EQUIVALENTE_SALDO_FINAL": float(row.vlr_caixa_equivalente_saldo_fim),
#                 "VLR_CAIXA_TOTAL": float(row.vlr_caixa_total),
#                 "VLR_CAIXA_LIVRE": float(row.vlr_caixa_livre),
#             }
#             for row in rows
#         ]
#
#         linha_titulo                           = '</th> <th width="40px">Descrição</th>'
#         linha_caixa_liquido_operac             = '<td class="text-left"> &emsp; Caixa Líquido Atividades Operacionais</td>'
#         linha_caixa_liquido_operac_gerado      = '<td class="text-left"> &emsp; &emsp; &emsp; Caixa Gerado nas Operações</td>'
#         linha_caixa_liquido_operac_variacoes   = '<td class="text-left"> &emsp; &emsp; &emsp; Variações nos Ativos e Passivos</td>'
#         linha_caixa_liquido_operac_outros      = '<td class="text-left"> &emsp; &emsp; &emsp; Outros</td>'
#         linha_caixa_liquido_operac_depre_amort = '<td class="text-left"> &emsp; &emsp; &emsp; Depreciação e Amortização</td>'
#         linha_caixa_liquido_invest             = '<td class="text-left"> &emsp; Caixa Líquido Atividades de Investimento</td>'
#         linha_caixa_liquido_finan              = '<td class="text-left"> &emsp; Caixa Líquido Atividades de Financiamento</td>'
#         linha_variacao_cambial                 = '<td class="text-left"> &emsp; Variação Cambial s/ Caixa e Equivalentes</td>'
#         linha_caixa_equivalente                = '<td class="text-left"> &emsp; Aumento (Redução) de Caixa e Equivalentes</td>'
#         linha_caixa_equivalente_saldo_ini      = '<td class="text-left"> &emsp; &emsp; &emsp; Saldo Inicial de Caixa e Equivalentes</td>'
#         linha_caixa_equivalente_saldo_fim      = '<td class="text-left"> &emsp; &emsp; &emsp; Saldo Final de Caixa e Equivalentes</td>'
#         linha_caixa_total                      = '<td class="text-left"> &emsp; Fluxo de Caixa Total</td>'
#         linha_caixa_livre                      = '<td class="text-left"> &emsp; Fluxo de Caixa Livre</td>'
#
#         fator = 0.0
#
#         lista = sorted(lista, reverse=True, key=lambda k: (k['ANO_REFER'], k['TRI_REFER']))
#         for indx, row in enumerate(lista):
#             if fator == 0.0: fator = 1000000 if float(row['VLR_CAIXA_LIQUIDO_OPERAC']) >= 1000000000 else 1000
#             if tipo_finan == "T" and indx > 7: break  # somente os ultimos 8
#             linha_titulo                           += '<th class="text-right" width="40px">' + row['TRI_REFER'] + '</th>'
#             linha_caixa_liquido_operac             += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_LIQUIDO_OPERAC']) + '</td>'
#             linha_caixa_liquido_operac_gerado      += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_LIQUIDO_OPERAC_CAIXA_GERADO']) + '</td>'
#             linha_caixa_liquido_operac_variacoes   += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_LIQUIDO_OPERAC_VARIACOES']) + '</td>'
#             linha_caixa_liquido_operac_outros      += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_LIQUIDO_OPERAC_OUTROS']) + '</td>'
#             linha_caixa_liquido_operac_depre_amort += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_LIQUIDO_OPERAC_DEPRECIACAO_AMORTIZACAO']) + '</td>'
#             linha_caixa_liquido_invest             += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_LIQUIDO_INVEST']) + '</td>'
#             linha_caixa_liquido_finan              += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_LIQUIDO_FINAN']) + '</td>'
#             linha_variacao_cambial                 += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_VARIACOES_CAMBIAL']) + '</td>'
#             linha_caixa_equivalente                += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_EQUIVALENTE']) + '</td>'
#             linha_caixa_equivalente_saldo_ini      += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_EQUIVALENTE_SALDO_INICIA']) + '</td>'
#             linha_caixa_equivalente_saldo_fim      += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_EQUIVALENTE_SALDO_FINAL']) + '</td>'
#             linha_caixa_total                      += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_TOTAL']) + '</td>'
#             linha_caixa_livre                      += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_CAIXA_LIVRE']) + '</td>'
#
#         result = ''
#         result += '<div class="table-responsive">'
#         result += '<table style="font-size: 12px" class="table table-sm table-hover table-condensed nowrap" cellspacing="0" width="100%">'
#         result += '<thead>'
#         result += '<tr style="font-size: 14px" class="thead-dark font-weight-bold">' + linha_titulo + '</tr>'
#         result += '</thead>'
#         result += '<tbody>'
#         result += '<tr>' + linha_caixa_liquido_operac + '</tr>'
#         result += '<tr>' + linha_caixa_liquido_operac_gerado + '</tr>'
#         result += '<tr>' + linha_caixa_liquido_operac_variacoes + '</tr>'
#         # result += '<tr>' + linha_caixa_liquido_operac_outros + '</tr>'
#         # result += '<tr>' + linha_caixa_liquido_operac_depre_amort + '</tr>'
#         result += '<tr>' + linha_caixa_liquido_invest + '</tr>'
#         result += '<tr>' + linha_caixa_liquido_finan + '</tr>'
#         result += '<tr>' + linha_variacao_cambial + '</tr>'
#         result += '<tr>' + linha_caixa_equivalente + '</tr>'
#         result += '<tr>' + linha_caixa_equivalente_saldo_ini + '</tr>'
#         result += '<tr>' + linha_caixa_equivalente_saldo_fim + '</tr>'
#         result += '<tr>' + linha_caixa_total + '</tr>'
#         result += '<tr>' + linha_caixa_livre + '</tr>'
#         result += '</tbody>'
#         result += '</table>'
#         result += '</div>'
#
#         return make_response(result, 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(LogErro.descricao_erro(texto=str(e)), 200)
#
#
# @bp_finan_acoes.route('/grid_balanc_patrimol', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
# def grid_balanc_patrimol():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response('Dados não informado!', 200)
#
#         try:
#             codigo = data.get('CodAtivo')
#             tipo_finan = data.get('TipoFinan')
#         except:
#             return make_response('Dados não informado!', 200)
#
#         if not codigo: return make_response('Ativo não informado!', 200)
#
#         codigo = str(codigo).strip().upper()
#         empresa = ACAOEmpresa.buscar_por_codigo(codigo=codigo)
#         if not empresa:
#             return make_response('Empresa não localizada!', 200)
#
#         cod_cvm = str(empresa['CODCVM'])
#
#         rows = None
#         if tipo_finan == "A":  # A-Anual
#             rows = ACAOEmpresaFinanceiroBPAAnual.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         elif tipo_finan == "T":  # T-Trimestral
#             rows = ACAOEmpresaFinanceiroBPATrimestral.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#
#         lista_ativos = [
#             {
#                 "ANO_REFER": str(row.ano_refer),
#                 "TRI_REFER": str(row.ano_refer) if tipo_finan == "A" else str(row.tri_refer),
#                 "VLR_ATIVO_TOTAL": float(row.vlr_ativo_total),
#                 "VLR_ATIVO_CIRCULANTE": float(row.vlr_circulante),
#                 "VLR_ATIVO_CIRCULANTE_CAIXA": float(row.vlr_circulante_caixa),
#                 "VLR_ATIVO_CIRCULANTE_APLIC_FINAN": float(row.vlr_circulante_aplic_finan),
#                 "VLR_ATIVO_CIRCULANTE_CONTAS_REC": float(row.vlr_circulante_contas_rec),
#                 "VLR_ATIVO_CIRCULANTE_ESTOQUE": float(row.vlr_circulante_estoque),
#                 "VLR_ATIVO_CIRCULANTE_OUTROS": float(row.vlr_circulante_outros),
#                 "VLR_ATIVO_NAO_CIRCULANTE": float(row.vlr_nao_circulante),
#                 "VLR_ATIVO_NAO_CIRCULANTE_LONGO_PRAZO": float(row.vlr_nao_circulante_longo_prazo),
#                 "VLR_ATIVO_NAO_CIRCULANTE_INVESTIMENTOS": float(row.vlr_nao_circulante_investimentos),
#                 "VLR_ATIVO_NAO_CIRCULANTE_IMOBILIZADO": float(row.vlr_nao_circulante_imobilizado),
#                 "VLR_ATIVO_NAO_CIRCULANTE_INTANGIVEL": float(row.vlr_nao_circulante_intangivel),
#                 "VLR_ATIVO_NAO_CIRCULANTE_OUTROS": float(row.vlr_nao_circulante_outros),
#             }
#             for row in rows
#         ]
#
#         rows = None
#         if tipo_finan == "A":  # A-Anual
#             rows = ACAOEmpresaFinanceiroBPPAnual.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         elif tipo_finan == "T":  # T-Trimestral
#             rows = ACAOEmpresaFinanceiroBPPTrimestral.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#
#         lista_passivos = [
#             {
#                 "ANO_REFER": str(row.ano_refer),
#                 "TRI_REFER": str(row.ano_refer) if tipo_finan == "A" else str(row.tri_refer),
#                 "VLR_PASSIVO_TOTAL": float(row.vlr_passivo_total),
#                 "VLR_PASSIVO_CIRCULANTE": float(row.vlr_circulante),
#                 "VLR_PASSIVO_CIRCULANTE_SALARIOS": float(row.vlr_circulante_salarios),
#                 "VLR_PASSIVO_CIRCULANTE_FORNECEDORES": float(row.vlr_circulante_fornecedores),
#                 "VLR_PASSIVO_CIRCULANTE_EMPRESTIMOSS": float(row.vlr_circulante_emprestimos),
#                 "VLR_PASSIVO_CIRCULANTE_OUTROS": float(row.vlr_circulante_outros),
#                 "VLR_PASSIVO_NAO_CIRCULANTE": float(row.vlr_nao_circulante),
#                 "VLR_PASSIVO_NAO_CIRCULANTE_EMPRESTIMOSS": float(row.vlr_nao_circulante_emprestimos),
#                 "VLR_PASSIVO_NAO_CIRCULANTE_OUTROS": float(row.vlr_nao_circulante_outros),
#                 "VLR_PASSIVO_PATRIMONIO_LIQUIDO_CONSOLIDADO": float(row.vlr_patrimonio_liquido_consolidado),
#                 "VLR_PASSIVO_PATRIMONIO_CAPITAL_SOCIAL_REALIZADO": float(row.vlr_patrimonio_capital_social_realizado),
#                 "VLR_PASSIVO_PATRIMONIO_LUCRO_PREJUIZO_ACUMULADO": float(row.vlr_patrimonio_lucro_prejuizo_acumulado),
#                 "VLR_PASSIVO_PATRIMONIO_RESERVA_CAPITAL": float(row.vlr_patrimonio_reserva_capital),
#                 "VLR_PASSIVO_PATRIMONIO_RESERVA_LUCROS": float(row.vlr_patrimonio_reserva_lucros),
#                 "VLR_PASSIVO_PATRIMONIO_PARTICIPACAO_NAO_CONTROLADORES": float(row.vlr_patrimonio_participacoes),
#                 "VLR_PASSIVO_PATRIMONIO_OUTROS": float(row.vlr_patrimonio_outros),
#             }
#             for row in rows
#         ]
#
#         if not lista_ativos and not lista_passivos:
#             return make_response('NENHUM RESULTADO ENCONTRADO', 200)
#
#         linha_titulo                                      = '</th> <th width="40px">Descrição</th>'
#         linha_ativo_total                                 = '<td class="text-left"> &emsp; Ativo Total</td>'
#         linha_ativo_circulante                            = '<td class="text-left"> &emsp; &emsp; Ativo Circulante</td>'
#         linha_ativo_circulante_caixa                      = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Caixa e Equivalentes de Caixa </td>'
#         linha_ativo_circulante_aplic_finan                = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Aplicações Financeiras</td>'
#         linha_ativo_circulante_contas_rec                 = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Contas a Receber</td>'
#         linha_ativo_circulante_estoque                    = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Estoque </td>'
#         linha_ativo_circulante_outros                     = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Outros</td>'
#         linha_ativo_nao_circulante                        = '<td class="text-left"> &emsp; &emsp; Ativo Não Circulante</td>'
#         linha_ativo_nao_circulante_longo_prazo            = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Ativo Realizável a Longo Prazo </td>'
#         linha_ativo_nao_circulante_investimentos          = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Investimentos </td>'
#         linha_ativo_nao_circulante_imobilizado            = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Imobilizado </td>'
#         linha_ativo_nao_circulante_intangivel             = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Intangível </td>'
#         linha_ativo_nao_circulante_outros                 = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Outros</td>'
#         linha_passivo_total                               = '<td class="text-left"> &emsp; Passivo Total</td>'
#         linha_passivo_circulante                          = '<td class="text-left"> &emsp; &emsp; Passivo Circulante </td>'
#         linha_passivo_circulante_salarios                 = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Salários, férias e encargos sociais </td>'
#         linha_passivo_circulante_fornecedores             = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Fornecedores </td>'
#         linha_passivo_circulante_emprestimos              = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Empréstimos e Financiamentos </td>'
#         linha_passivo_circulante_outros                   = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Outros </td>'
#         linha_passivo_nao_circulante                      = '<td class="text-left"> &emsp; &emsp; Passivo Não Circulante</td>'
#         linha_passivo_nao_circulante_emprestimos          = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Empréstimos e Financiamentos </td>'
#         linha_passivo_nao_circulante_outros               = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Outros </td>'
#         linha_passivo_patrimonio_liquido_consolidado      = '<td class="text-left"> &emsp; &emsp; Patrimônio Líquido Consolidado</td>'
#         linha_passivo_patrimonio_capital_social_realizado = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Capital Social Realizado </td>'
#         linha_passivo_patrimonio_lucro_prejuizo_acumulado = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Reserva de Lucro/Prejuizo Acumulado </td>'
#         linha_passivo_patrimonio_reserva_capital          = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Reserva Capital </td>'
#         linha_passivo_patrimonio_reserva_lucros           = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Reserva Lucros  </td>'
#         linha_passivo_patrimonio_participacoes            = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Participação dos Não Controladores </td>'
#         linha_passivo_patrimonio_outros                   = '<td class="text-left"> &emsp; &emsp; &emsp; &emsp; Outros </td>'
#
#         fator = 0.0
#
#         lista_ativos = sorted(lista_ativos, reverse=True, key=lambda k: (k['ANO_REFER'], k['TRI_REFER']))
#         for indx, row in enumerate(lista_ativos):
#             if fator == 0.0: fator = 1000000 if float(row['VLR_ATIVO_TOTAL']) >= 1000000000 else 1000
#             if tipo_finan == "T" and indx > 7: break  # somente os ultimos 8
#             linha_titulo                             += '<th class="text-right" width="40px">' + row['TRI_REFER'] + '</th>'
#             linha_ativo_total                        += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_TOTAL']) + '</td>'
#             linha_ativo_circulante                   += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_CIRCULANTE']) + '</td>'
#             linha_ativo_circulante_caixa             += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_CIRCULANTE_CAIXA']) + '</td>'
#             linha_ativo_circulante_aplic_finan       += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_CIRCULANTE_APLIC_FINAN']) + '</td>'
#             linha_ativo_circulante_contas_rec        += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_CIRCULANTE_CONTAS_REC']) + '</td>'
#             linha_ativo_circulante_estoque           += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_CIRCULANTE_ESTOQUE']) + '</td>'
#             linha_ativo_circulante_outros            += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_CIRCULANTE_OUTROS']) + '</td>'
#             linha_ativo_nao_circulante               += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_NAO_CIRCULANTE']) + '</td>'
#             linha_ativo_nao_circulante_longo_prazo   += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_NAO_CIRCULANTE_LONGO_PRAZO']) + '</td>'
#             linha_ativo_nao_circulante_investimentos += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_NAO_CIRCULANTE_INVESTIMENTOS']) + '</td>'
#             linha_ativo_nao_circulante_imobilizado   += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_NAO_CIRCULANTE_IMOBILIZADO']) + '</td>'
#             linha_ativo_nao_circulante_intangivel    += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_NAO_CIRCULANTE_INTANGIVEL']) + '</td>'
#             linha_ativo_nao_circulante_outros        += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_ATIVO_NAO_CIRCULANTE_OUTROS']) + '</td>'
#
#         lista_passivos = sorted(lista_passivos, reverse=True, key=lambda k: (k['ANO_REFER'], k['TRI_REFER']))
#         for indx, row in enumerate(lista_passivos):
#             if tipo_finan == "T" and indx > 7: break  # somente os ultimos 8
#             linha_passivo_total                               += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_TOTAL']) + '</td>'
#             linha_passivo_circulante                          += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_CIRCULANTE']) + '</td>'
#             linha_passivo_circulante_salarios                 += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_CIRCULANTE_SALARIOS']) + '</td>'
#             linha_passivo_circulante_fornecedores             += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_CIRCULANTE_FORNECEDORES']) + '</td>'
#             linha_passivo_circulante_emprestimos              += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_CIRCULANTE_EMPRESTIMOSS']) + '</td>'
#             linha_passivo_circulante_outros                   += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_CIRCULANTE_OUTROS']) + '</td>'
#             linha_passivo_nao_circulante                      += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_NAO_CIRCULANTE']) + '</td>'
#             linha_passivo_nao_circulante_emprestimos          += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_NAO_CIRCULANTE_EMPRESTIMOSS']) + '</td>'
#             linha_passivo_nao_circulante_outros               += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_NAO_CIRCULANTE_OUTROS']) + '</td>'
#             linha_passivo_patrimonio_liquido_consolidado      += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_PATRIMONIO_LIQUIDO_CONSOLIDADO']) + '</td>'
#             linha_passivo_patrimonio_capital_social_realizado += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_PATRIMONIO_CAPITAL_SOCIAL_REALIZADO']) + '</td>'
#             linha_passivo_patrimonio_lucro_prejuizo_acumulado += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_PATRIMONIO_LUCRO_PREJUIZO_ACUMULADO']) + '</td>'
#             linha_passivo_patrimonio_reserva_capital          += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_PATRIMONIO_RESERVA_CAPITAL']) + '</td>'
#             linha_passivo_patrimonio_reserva_lucros           += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_PATRIMONIO_RESERVA_LUCROS']) + '</td>'
#             linha_passivo_patrimonio_participacoes            += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_PATRIMONIO_PARTICIPACAO_NAO_CONTROLADORES']) + '</td>'
#             linha_passivo_patrimonio_outros                   += '<td class="text-right">' + decimal_resumido(fator=fator, valor=row['VLR_PASSIVO_PATRIMONIO_OUTROS']) + '</td>'
#
#         result = ''
#         result += '<div class="table-responsive">'
#         result += '<table style="font-size: 12px" class="table table-sm table-hover table-condensed nowrap" cellspacing="0" width="100%">'
#         result += '<thead>'
#         result += '<tr style="font-size: 14px" class="thead-dark font-weight-bold">' + linha_titulo + '</tr>'
#         result += '</thead>'
#         result += '<tbody>'
#         result += '<tr>' + linha_ativo_total + '</tr>'
#         result += '<tr>' + linha_ativo_circulante + '</tr>'
#         result += '<tr>' + linha_ativo_circulante_caixa + '</tr>'
#         result += '<tr>' + linha_ativo_circulante_aplic_finan + '</tr>'
#         result += '<tr>' + linha_ativo_circulante_contas_rec + '</tr>'
#         result += '<tr>' + linha_ativo_circulante_estoque + '</tr>'
#         result += '<tr>' + linha_ativo_circulante_outros + '</tr>'
#         result += '<tr>' + linha_ativo_nao_circulante + '</tr>'
#         result += '<tr>' + linha_ativo_nao_circulante_longo_prazo + '</tr>'
#         result += '<tr>' + linha_ativo_nao_circulante_investimentos + '</tr>'
#         result += '<tr>' + linha_ativo_nao_circulante_imobilizado + '</tr>'
#         result += '<tr>' + linha_ativo_nao_circulante_intangivel + '</tr>'
#         result += '<tr>' + linha_ativo_nao_circulante_outros + '</tr>'
#         result += '<tr>' + linha_passivo_total + '</tr>'
#         result += '<tr>' + linha_passivo_circulante + '</tr>'
#         result += '<tr>' + linha_passivo_circulante_salarios + '</tr>'
#         result += '<tr>' + linha_passivo_circulante_fornecedores + '</tr>'
#         result += '<tr>' + linha_passivo_circulante_emprestimos + '</tr>'
#         result += '<tr>' + linha_passivo_circulante_outros + '</tr>'
#         result += '<tr>' + linha_passivo_nao_circulante + '</tr>'
#         result += '<tr>' + linha_passivo_nao_circulante_emprestimos + '</tr>'
#         result += '<tr>' + linha_passivo_nao_circulante_outros + '</tr>'
#         result += '<tr>' + linha_passivo_patrimonio_liquido_consolidado + '</tr>'
#         result += '<tr>' + linha_passivo_patrimonio_capital_social_realizado + '</tr>'
#         result += '<tr>' + linha_passivo_patrimonio_lucro_prejuizo_acumulado + '</tr>'
#         result += '<tr>' + linha_passivo_patrimonio_reserva_capital + '</tr>'
#         result += '<tr>' + linha_passivo_patrimonio_reserva_lucros + '</tr>'
#         result += '<tr>' + linha_passivo_patrimonio_participacoes + '</tr>'
#         result += '<tr>' + linha_passivo_patrimonio_outros + '</tr>'
#         result += '</tbody>'
#         result += '</table>'
#         result += '</div>'
#
#         return make_response(result, 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(LogErro.descricao_erro(texto=str(e)), 200)
#
#
# @bp_finan_acoes.route('/grid_prov', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
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
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_grid(msg='Ativo não informado!'), 200)
#
#         codigo = str(codigo).strip().upper()
#
#         empresa = ACAOEmpresa.buscar_por_codigo(codigo=codigo)
#         if not empresa:
#             return make_response(get_json_retorno_grid(msg='Empresa não localizada!'), 200)
#
#         codigo_isin = str(empresa['CODISINATIVO']) if empresa['CODISINATIVO'] else ''
#         if not codigo_isin:
#             return make_response(get_json_retorno_grid(rslt='OK', msg='NENHUM RESULTADO ENCONTRADO'), 200)
#
#         rows = ACAOEmpresaProvento.get_all_by_codigo_isin(codigo_isin=codigo_isin)
#         if not rows:
#             return make_response(get_json_retorno_grid(rslt='OK', msg='NENHUM RESULTADO ENCONTRADO'), 200)
#
#         lista = [
#             {
#                 "tipo": str(row.tipo),
#                 "tipoFormat": str(row.tipo_descr()),
#                 "dataAprov": str(row.data_aprov),
#                 "dataAprovFormat": str(row.data_aprov_format()),
#                 "dataEx": str(row.data_ex),
#                 "dataExFormat": str(row.data_ex_format()),
#                 "dataPagto": str(row.data_pagto),
#                 "dataPagtoFormat": str(row.data_pagto_format()),
#                 "vlrPreco": float(row.vlr_preco),
#                 "vlrPrecoFormat": row.vlr_preco_format_2(),
#             }
#             for row in rows if row.situacao == 'A' and row.tipo in ['D', 'J', 'R']
#         ]
#
#         # lista = sorted(lista, reverse=True, key=lambda k: (k['dataAprov'], k['dataEx']))
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_finan_acoes.route('/grid_prov_tab', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
# def grid_prov_tab():
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
#             tipo = data.get('TipoTabela')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_grid(msg='Ativo não informado!'), 200)
#         if not tipo: return make_response(get_json_retorno_grid(msg='Tipo não informado!'), 200)
#
#         codigo = str(codigo).strip().upper()
#         tipo = str(tipo).strip().upper()
#
#         ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=codigo)
#         if not ativo: return make_response(get_json_retorno_grid(msg='Empresa não localizada!'), 200)
#         if not ativo.codigo_isin: return make_response(get_json_retorno_grid(rslt='OK', msg='NENHUM RESULTADO ENCONTRADO'), 200)
#
#         is_data_pagto = tipo == 'P' # E-Ex // # P-Pagt
#         rows = ACAOEmpresaProvento.buscar__dados_tab_finan(id_empresa=int(ativo.id_empresa), codigo_isin=str(ativo.codigo_isin), is_data_pagto=is_data_pagto)
#         if not rows: return make_response(get_json_retorno_grid(rslt='OK', msg='NENHUM RESULTADO ENCONTRADO'), 200)
#
#         import pandas as pd
#
#         df = pd.DataFrame(rows)
#         df.columns = ['DATA', 'VALOR']
#         df['DATA'].fillna('99991231', inplace=True)
#         df['DATA'] = df['DATA'].map(lambda x: str(x).strip() if x and str(x).strip() != "" else '99991231')
#         df['DATA'] = df['DATA'].astype('int32')
#         df['ANO'] = df['DATA'].apply(lambda x: int(str(x)[:4])).astype('int')
#         df['MES'] = df['DATA'].apply(lambda x: int(str(x)[4:6])).astype('int')
#         df = pd.pivot_table(df, values='VALOR', index='ANO', columns='MES', aggfunc='first')
#         df.fillna('', inplace=True)
#         for idx in range(1, 13):
#             if idx not in df: df[idx] = ''
#         df.rename(columns={1: "JAN", 2: "FEV", 3: "MAR", 4: "ABR", 5: "MAI", 6: "JUN", 7: "JUL", 8: "AGO", 9: "SET", 10: "OUT", 11: "NOV", 12: "DEZ"}, inplace=True)
#         df = df[['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']]
#         df.reset_index(inplace=True)
#         df.sort_values(by='ANO', ascending=False, inplace=True)
#
#         lista = [
#             {
#                 "ano": row.ANO,
#                 "jan": float(row.JAN) if row.JAN else 0.0,
#                 "fev": float(row.FEV) if row.FEV else 0.0,
#                 "mar": float(row.MAR) if row.MAR else 0.0,
#                 "abr": float(row.ABR) if row.ABR else 0.0,
#                 "mai": float(row.MAI) if row.MAI else 0.0,
#                 "jun": float(row.JUN) if row.JUN else 0.0,
#                 "jul": float(row.JUL) if row.JUL else 0.0,
#                 "ago": float(row.AGO) if row.AGO else 0.0,
#                 "set": float(row.SET) if row.SET else 0.0,
#                 "out": float(row.OUT) if row.OUT else 0.0,
#                 "nov": float(row.NOV) if row.NOV else 0.0,
#                 "dez": float(row.DEZ) if row.DEZ else 0.0,
#             }
#             for idx, row in df.iterrows()
#         ]
#
#         lista = lista[:10]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
#
# @bp_finan_acoes.route('/grid_cot', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
# def grid_cot():
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
#         if not codigo: return make_response(get_json_retorno_grid(msg='Ativo não informado!'), 200)
#
#         codigo = str(codigo).strip().upper()
#
#         ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=codigo)
#         if not ativo: return make_response(get_json_retorno_grid(msg='Empresa não localizada!'), 200)
#
#         data_atual = pegar_data_atual(istext=False)
#         data_ano = int(converter_datetime_str(data=data_atual, fmt='%Y')) - 11
#         data_ini = str(data_ano) + '1201'
#
#         rows = ACAOEmpresaAtivoCotacaoHist.buscar_todos(categoria='ACAO', codigo=codigo, dt_ini=data_ini)
#         if not rows: return make_response(get_json_retorno_grid(rslt='OK', msg='NENHUM RESULTADO ENCONTRADO'), 200)
#
#         import pandas as pd
#         import numpy as np
#
#         df = pd.DataFrame(rows)
#         df.columns = ['Date', 'Adj Close', 'Retorno']
#         df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
#         df['Adj Close'] = df['Adj Close'].astype('float64')
#         df.drop(columns=['Retorno'], axis=1, inplace=True)
#         df.set_index('Date', inplace=True)
#
#         retorno_anual = df['Adj Close'].resample('A', kind='period').last()
#         retorno_anual = retorno_anual.pct_change()
#         # retorno_anual = retorno_anual.dropna()
#         # retorno_anual = retorno_anual.fillna(0)
#         retorno_anual = retorno_anual.to_frame()
#         retorno_anual.columns = ['retono']
#         print('retorno_anual', len(retorno_anual.index))
#
#         retorno_anual_medio = df['Adj Close'].resample('A', kind='period').last()
#         retorno_anual_medio = retorno_anual_medio.to_frame()
#         retorno_anual_medio = retorno_anual_medio.dropna()
#         retorno_anual_medio = np.log(retorno_anual_medio / retorno_anual_medio.shift(1))  # Taxa média de crescimento
#         retorno_anual_medio.columns = ['retono']
#         # retorno_anual_medio = retorno_anual_medio.fillna(0)
#         # retorno_anual_medio = retorno_anual_medio.dropna()
#         print('retorno_anual_medio', len(retorno_anual_medio.index))
#
#         retorno_mensal = df['Adj Close'].resample('M', kind='period').last()
#         retorno_mensal = retorno_mensal.pct_change()
#         retorno_mensal = retorno_mensal.dropna()
#         retorno_mensal = retorno_mensal.to_frame()
#         retorno_mensal.columns = ['retono']
#         retorno_mensal['ano'] = retorno_mensal.index.year
#         retorno_mensal['mes'] = retorno_mensal.index.month
#
#         tab_retorno_mensal = retorno_mensal.pivot(index='ano', columns='mes', values='retono')
#         # tab_retorno_mensal = retorno_mensal.pivot_table(index='ano', columns='mes', values='retono', fill_value=0.0)
#         tab_retorno_mensal = tab_retorno_mensal.fillna(0)
#         for idx in range(1, 13):
#             if idx not in tab_retorno_mensal.columns: tab_retorno_mensal.loc[:, idx] = 0.0
#         tab_retorno_mensal.rename(columns={1: "JAN", 2: "FEV", 3: "MAR", 4: "ABR", 5: "MAI", 6: "JUN", 7: "JUL", 8: "AGO", 9: "SET", 10: "OUT", 11: "NOV", 12: "DEZ"}, inplace=True)
#         tab_retorno_mensal = tab_retorno_mensal[['JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ']]
#
#         if len(retorno_anual.index) != len(tab_retorno_mensal.index):
#             retorno_anual = retorno_anual.dropna()
#         retorno_anual = retorno_anual.fillna(0)
#         tab_retorno_mensal['ANO'] = retorno_anual.values
#
#         if len(retorno_anual_medio.index) != len(tab_retorno_mensal.index):
#             retorno_anual_medio = retorno_anual_medio.dropna()
#         retorno_anual_medio = retorno_anual_medio.fillna(0)
#         tab_retorno_mensal['ANO_MEDIO'] = retorno_anual_medio.values
#
#         tab_retorno_mensal = round(tab_retorno_mensal * 100, 2)
#         tab_retorno_mensal.index.name = ""
#         tab_retorno_mensal.columns.name = ""
#         tab_retorno_mensal.sort_index(ascending=False, inplace=True)
#
#         lista = [
#             {
#                 "ano": int(idx),
#                 "jan": float(row.JAN) if row.JAN else 0.0,
#                 "fev": float(row.FEV) if row.FEV else 0.0,
#                 "mar": float(row.MAR) if row.MAR else 0.0,
#                 "abr": float(row.ABR) if row.ABR else 0.0,
#                 "mai": float(row.MAI) if row.MAI else 0.0,
#                 "jun": float(row.JUN) if row.JUN else 0.0,
#                 "jul": float(row.JUL) if row.JUL else 0.0,
#                 "ago": float(row.AGO) if row.AGO else 0.0,
#                 "set": float(row.SET) if row.SET else 0.0,
#                 "out": float(row.OUT) if row.OUT else 0.0,
#                 "nov": float(row.NOV) if row.NOV else 0.0,
#                 "dez": float(row.DEZ) if row.DEZ else 0.0,
#                 "anual": float(row.ANO) if row.ANO else 0.0,
#                 "medio": float(row.ANO_MEDIO) if row.ANO_MEDIO else 0.0,
#             }
#             for idx, row in tab_retorno_mensal.iterrows()
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_finan_acoes.route('/grid_dre', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_dre():
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
#             codigo = data.get('CodAtivo')
#             tipo_finan = data.get('TipoFinan')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         codigo = str(codigo).strip().upper()
#         empresa = ACAOEmpresa.buscar_por_codigo(codigo=codigo)
#         if not empresa:
#             return make_response(get_json_retorno_dados(msg='Empresa não localizada!'), 200)
#
#         cod_cvm = str(empresa['CODCVM'])
#
#         rows = None
#         if tipo_finan == "A":  # A-Anual
#             rows = ACAOEmpresaFinanceiroDREAnual.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         elif tipo_finan == "T":  # T-Trimestral
#             rows = ACAOEmpresaFinanceiroDRETrimestral.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         if not rows:
#             return make_response(get_json_retorno_dados(msg='NENHUM RESULTADO ENCONTRADO'), 200)
#
#         lista = [
#             {
#                 "ANO_REFER": str(row.ano_refer),
#                 "TRI_REFER": str(row.ano_refer) if tipo_finan == "A" else str(row.tri_refer),
#                 "VLR_RECEITA_LIQ": float(row.vlr_receita_liq),
#                 "VLR_CUSTO": float(row.vlr_custo),
#                 "VLR_LUCRO_BRUTO": float(row.vlr_lucro_bruto),
#                 "VLR_MARGEM_BRUTA": float(row.vlr_margem_bruta) if row.vlr_margem_bruta else 0.0,
#                 "VLR_DESPESA_OPERAC": float(row.vlr_despesa_operac),
#                 "VLR_RESULTADO_OPERAC": float(row.vlr_resultado_operac),
#                 "VLR_MARGEM_OPERAC": float(row.vlr_margem_operac) if row.vlr_margem_operac else 0.0,
#                 "VLR_RESULTADO_FINAN": float(row.vlr_resultado_finan),
#                 "VLR_RESULTADO_ANTES_IR": float(row.vlr_resultado_antes_ir),
#                 "VLR_IMPOSTO": float(row.vlr_imposto),
#                 "VLR_OPERAC_CONT": float(row.vlr_operac_cont),
#                 "VLR_OPERAC_DESCONT": float(row.vlr_operac_descont),
#                 "VLR_LUCRO_LIQUIDO": float(row.vlr_lucro_liquido),
#                 "VLR_MARGEM_LIQUIDA": float(row.vlr_margem_liquida) if row.vlr_margem_liquida else 0.0,
#             }
#             for row in rows
#         ]
#
#         lista_titulo = []
#         lista_receita_liq = []
#         lista_custo = []
#         lista_lucro_bruto = []
#         lista_despesa_operac = []
#         lista_resultado_operac = []
#         lista_resultado_finan = []
#         lista_resultado_antes_ir = []
#         lista_imposto = []
#         lista_operac_cont = []
#         lista_operac_descont = []
#         lista_lucro_liquido = []
#         lista_margem_bruta = []
#         lista_margem_operac = []
#         lista_margem_liquida = []
#
#         for indx, row in enumerate(lista):
#             lista_titulo.append(row['TRI_REFER'])
#             lista_receita_liq.append(float(row['VLR_RECEITA_LIQ'])) # lista_receita_liq.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_RECEITA_LIQ']))
#             lista_custo.append(float(row['VLR_CUSTO'])) # lista_custo.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_CUSTO']))
#             lista_lucro_bruto.append(float(row['VLR_LUCRO_BRUTO'])) # lista_lucro_bruto.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_LUCRO_BRUTO']))
#             #lista_despesa_operac.append(float(row['VLR_DESPESA_OPERAC'])) # lista_despesa_operac.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_DESPESA_OPERAC']))
#             lista_resultado_operac.append(float(row['VLR_RESULTADO_OPERAC'])) # lista_resultado_operac.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_RESULTADO_OPERAC']))
#             #lista_resultado_finan.append(float(row['VLR_RESULTADO_FINAN'])) # lista_resultado_finan.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_RESULTADO_FINAN']))
#             #lista_resultado_antes_ir.append(float(row['VLR_RESULTADO_ANTES_IR'])) # lista_resultado_antes_ir.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_RESULTADO_ANTES_IR']))
#             #lista_imposto.append(float(row['VLR_IMPOSTO'])) # lista_imposto.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_IMPOSTO']))
#             #lista_operac_cont.append(float(row['VLR_OPERAC_CONT'])) # lista_operac_cont.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_OPERAC_CONT']))
#             #lista_operac_descont.append(float(row['VLR_OPERAC_DESCONT'])) # lista_operac_descont.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_OPERAC_DESCONT']))
#             lista_lucro_liquido.append(float(row['VLR_LUCRO_LIQUIDO'])) # lista_lucro_liquido.append(decimal_resumido(fator=fator, convertStr=False, valor=row['VLR_LUCRO_LIQUIDO']))
#             lista_margem_bruta.append(float(row['VLR_MARGEM_BRUTA']))
#             lista_margem_operac.append(float(row['VLR_MARGEM_OPERAC']))
#             lista_margem_liquida.append(float(row['VLR_MARGEM_LIQUIDA']))
#
#         dados = dict({
#             "listaTitulo": lista_titulo,
#             "listaReceitaLiq": lista_receita_liq,
#             "listaCusto": lista_custo,
#             "listaLucroBruto": lista_lucro_bruto,
#             "listaDespesaOperac": lista_despesa_operac,
#             "listaResultadoOperac": lista_resultado_operac,
#             "listaResultadoFinan": lista_resultado_finan,
#             "listaResultadoAntesIR": lista_resultado_antes_ir,
#             "listaImposto": lista_imposto,
#             "listaOperacCont": lista_operac_cont,
#             "listaOperacDescont": lista_operac_descont,
#             "listaLucroLiquido": lista_lucro_liquido,
#             "listaMargemBruta": lista_margem_bruta,
#             "listaMargemOperac": lista_margem_operac,
#             "listaMargemLiquida": lista_margem_liquida,
#         })
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_finan_acoes.route('/grid_dfc', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_dfc():
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
#             codigo = data.get('CodAtivo')
#             tipo_finan = data.get('TipoFinan')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         codigo = str(codigo).strip().upper()
#         empresa = ACAOEmpresa.buscar_por_codigo(codigo=codigo)
#         if not empresa:
#             return make_response(get_json_retorno_dados(msg='Empresa não localizada!'), 200)
#
#         cod_cvm = str(empresa['CODCVM'])
#
#         rows = None
#         if tipo_finan == "A":  # A-Anual
#             rows = ACAOEmpresaFinanceiroDFCAnual.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         elif tipo_finan == "T":  # T-Trimestral
#             rows = ACAOEmpresaFinanceiroDFCTrimestral.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         if not rows:
#             return make_response(get_json_retorno_dados(msg='NENHUM RESULTADO ENCONTRADO'), 200)
#
#         lista = [
#             {
#                 "ANO_REFER": str(row.ano_refer),
#                 "TRI_REFER": str(row.ano_refer) if tipo_finan == "A" else str(row.tri_refer),
#                 "VLR_CAIXA_LIQUIDO_OPERAC": float(row.vlr_caixa_liquido_operac),
#                 "VLR_CAIXA_LIQUIDO_OPERAC_CAIXA_GERADO": float(row.vlr_caixa_liquido_operac_gerado),
#                 "VLR_CAIXA_LIQUIDO_OPERAC_VARIACOES": float(row.vlr_caixa_liquido_operac_variacoes),
#                 "VLR_CAIXA_LIQUIDO_OPERAC_OUTROS": float(row.vlr_caixa_liquido_operac_outros),
#                 "VLR_CAIXA_LIQUIDO_OPERAC_DEPRECIACAO_AMORTIZACAO": float(row.vlr_caixa_liquido_operac_depre_amort),
#                 "VLR_CAIXA_LIQUIDO_INVEST": float(row.vlr_caixa_liquido_invest),
#                 "VLR_CAIXA_LIQUIDO_FINAN": float(row.vlr_caixa_liquido_finan),
#                 "VLR_VARIACOES_CAMBIAL": float(row.vlr_variacao_cambial),
#                 "VLR_CAIXA_EQUIVALENTE": float(row.vlr_caixa_equivalente),
#                 "VLR_CAIXA_EQUIVALENTE_SALDO_INICIA": float(row.vlr_caixa_equivalente_saldo_ini),
#                 "VLR_CAIXA_EQUIVALENTE_SALDO_FINAL": float(row.vlr_caixa_equivalente_saldo_fim),
#                 "VLR_CAIXA_TOTAL": float(row.vlr_caixa_total),
#                 "VLR_CAIXA_LIVRE": float(row.vlr_caixa_livre),
#             }
#             for row in rows
#         ]
#
#         lista_titulo = []
#         lista_caixa_liquido_operac = []
#         lista_caixa_liquido_operac_gerado = []
#         lista_caixa_liquido_operac_variacoes = []
#         lista_caixa_liquido_operac_outros = []
#         lista_caixa_liquido_operac_depre_amort = []
#         lista_caixa_liquido_invest = []
#         lista_caixa_liquido_finan = []
#         lista_variacao_cambial = []
#         lista_caixa_equivalente = []
#         lista_caixa_equivalente_saldo_ini = []
#         lista_caixa_equivalente_saldo_fim = []
#         lista_caixa_total = []
#         lista_caixa_livre = []
#
#         for indx, row in enumerate(lista):
#             lista_titulo.append(row['TRI_REFER'])
#             lista_caixa_liquido_operac.append(float(row['VLR_CAIXA_LIQUIDO_OPERAC']))
#             #lista_caixa_liquido_operac_gerado.append(float(row['VLR_CAIXA_LIQUIDO_OPERAC_CAIXA_GERADO']))
#             #lista_caixa_liquido_operac_variacoes.append(float(row['VLR_CAIXA_LIQUIDO_OPERAC_VARIACOES']))
#             #lista_caixa_liquido_operac_outros.append(float(row['VLR_CAIXA_LIQUIDO_OPERAC_OUTROS']))
#             #lista_caixa_liquido_operac_depre_amort.append(float(row['VLR_CAIXA_LIQUIDO_OPERAC_DEPRECIACAO_AMORTIZACAO']))
#             lista_caixa_liquido_invest.append(float(row['VLR_CAIXA_LIQUIDO_INVEST']))
#             lista_caixa_liquido_finan.append(float(row['VLR_CAIXA_LIQUIDO_FINAN']))
#             #lista_variacao_cambial.append(float(row['VLR_VARIACOES_CAMBIAL']))
#             #lista_caixa_equivalente.append(float(row['VLR_CAIXA_EQUIVALENTE']))
#             #lista_caixa_equivalente_saldo_ini.append(float(row['VLR_CAIXA_EQUIVALENTE_SALDO_INICIA']))
#             #lista_caixa_equivalente_saldo_fim.append(float(row['VLR_CAIXA_EQUIVALENTE_SALDO_FINAL']))
#             lista_caixa_total.append(float(row['VLR_CAIXA_TOTAL']))
#             lista_caixa_livre.append(float(row['VLR_CAIXA_LIVRE']))
#
#         dados = dict({
#             "listaTitulo": lista_titulo,
#             "listaCaixaLiquidoOperac": lista_caixa_liquido_operac,
#             "listaCaixaLiquidoOperacGerado": lista_caixa_liquido_operac_gerado,
#             "listaCaixaLiquidoOperacVariacoes": lista_caixa_liquido_operac_variacoes,
#             "listaCaixaLiquidoOperacOutros": lista_caixa_liquido_operac_outros,
#             "listaCaixaLiquidoOperacDepreAmort": lista_caixa_liquido_operac_depre_amort,
#             "listaCaixaLiquidoInvest": lista_caixa_liquido_invest,
#             "listaCaixaLiquidoFinan": lista_caixa_liquido_finan,
#             "listaVariacaoCambial": lista_variacao_cambial,
#             "listaCaixaEquivalente": lista_caixa_equivalente,
#             "listaCaixaEquivalenteSaldoIni": lista_caixa_equivalente_saldo_ini,
#             "listaCaixaEquivalentesaldoFim": lista_caixa_equivalente_saldo_fim,
#             "listaCaixaTotal": lista_caixa_total,
#             "listaCaixaLivre": lista_caixa_livre,
#         })
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_finan_acoes.route('/grid_bp', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_bp():
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
#             codigo = data.get('CodAtivo')
#             tipo_finan = data.get('TipoFinan')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         codigo = str(codigo).strip().upper()
#         empresa = ACAOEmpresa.buscar_por_codigo(codigo=codigo)
#         if not empresa:
#             return make_response(get_json_retorno_dados(msg='Empresa não localizada!'), 200)
#
#         cod_cvm = str(empresa['CODCVM'])
#
#         rows = None
#         if tipo_finan == "A":  # A-Anual
#             rows = ACAOEmpresaFinanceiroBPAAnual.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         elif tipo_finan == "T":  # T-Trimestral
#             rows = ACAOEmpresaFinanceiroBPATrimestral.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#
#         lista_ativos = [
#             {
#                 "ANO_REFER": str(row.ano_refer),
#                 "TRI_REFER": str(row.ano_refer) if tipo_finan == "A" else str(row.tri_refer),
#                 "VLR_ATIVO_TOTAL": float(row.vlr_ativo_total),
#                 "VLR_ATIVO_CIRCULANTE": float(row.vlr_circulante),
#                 "VLR_ATIVO_CIRCULANTE_CAIXA": float(row.vlr_circulante_caixa),
#                 "VLR_ATIVO_CIRCULANTE_APLIC_FINAN": float(row.vlr_circulante_aplic_finan),
#                 "VLR_ATIVO_CIRCULANTE_CONTAS_REC": float(row.vlr_circulante_contas_rec),
#                 "VLR_ATIVO_CIRCULANTE_ESTOQUE": float(row.vlr_circulante_estoque),
#                 "VLR_ATIVO_CIRCULANTE_OUTROS": float(row.vlr_circulante_outros),
#                 "VLR_ATIVO_NAO_CIRCULANTE": float(row.vlr_nao_circulante),
#                 "VLR_ATIVO_NAO_CIRCULANTE_LONGO_PRAZO": float(row.vlr_nao_circulante_longo_prazo),
#                 "VLR_ATIVO_NAO_CIRCULANTE_INVESTIMENTOS": float(row.vlr_nao_circulante_investimentos),
#                 "VLR_ATIVO_NAO_CIRCULANTE_IMOBILIZADO": float(row.vlr_nao_circulante_imobilizado),
#                 "VLR_ATIVO_NAO_CIRCULANTE_INTANGIVEL": float(row.vlr_nao_circulante_intangivel),
#                 "VLR_ATIVO_NAO_CIRCULANTE_OUTROS": float(row.vlr_nao_circulante_outros),
#             }
#             for row in rows
#         ]
#
#         rows = None
#         if tipo_finan == "A":  # A-Anual
#             rows = ACAOEmpresaFinanceiroBPPAnual.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#         elif tipo_finan == "T":  # T-Trimestral
#             rows = ACAOEmpresaFinanceiroBPPTrimestral.get_all_by_cod_cvm(cod_cvm=cod_cvm)
#
#         lista_passivos = [
#             {
#                 "ANO_REFER": str(row.ano_refer),
#                 "TRI_REFER": str(row.ano_refer) if tipo_finan == "A" else str(row.tri_refer),
#                 "VLR_PASSIVO_TOTAL": float(row.vlr_passivo_total),
#                 "VLR_PASSIVO_CIRCULANTE": float(row.vlr_circulante),
#                 "VLR_PASSIVO_CIRCULANTE_SALARIOS": float(row.vlr_circulante_salarios),
#                 "VLR_PASSIVO_CIRCULANTE_FORNECEDORES": float(row.vlr_circulante_fornecedores),
#                 "VLR_PASSIVO_CIRCULANTE_EMPRESTIMOSS": float(row.vlr_circulante_emprestimos),
#                 "VLR_PASSIVO_CIRCULANTE_OUTROS": float(row.vlr_circulante_outros),
#                 "VLR_PASSIVO_NAO_CIRCULANTE": float(row.vlr_nao_circulante),
#                 "VLR_PASSIVO_NAO_CIRCULANTE_EMPRESTIMOSS": float(row.vlr_nao_circulante_emprestimos),
#                 "VLR_PASSIVO_NAO_CIRCULANTE_OUTROS": float(row.vlr_nao_circulante_outros),
#                 "VLR_PASSIVO_PATRIMONIO_LIQUIDO_CONSOLIDADO": float(row.vlr_patrimonio_liquido_consolidado),
#                 "VLR_PASSIVO_PATRIMONIO_CAPITAL_SOCIAL_REALIZADO": float(row.vlr_patrimonio_capital_social_realizado),
#                 "VLR_PASSIVO_PATRIMONIO_LUCRO_PREJUIZO_ACUMULADO": float(row.vlr_patrimonio_lucro_prejuizo_acumulado),
#                 "VLR_PASSIVO_PATRIMONIO_RESERVA_CAPITAL": float(row.vlr_patrimonio_reserva_capital),
#                 "VLR_PASSIVO_PATRIMONIO_RESERVA_LUCROS": float(row.vlr_patrimonio_reserva_lucros),
#                 "VLR_PASSIVO_PATRIMONIO_PARTICIPACAO_NAO_CONTROLADORES": float(row.vlr_patrimonio_participacoes),
#                 "VLR_PASSIVO_PATRIMONIO_OUTROS": float(row.vlr_patrimonio_outros),
#             }
#             for row in rows
#         ]
#
#         if not lista_ativos and not lista_passivos:
#             return make_response(get_json_retorno_dados(msg='NENHUM RESULTADO ENCONTRADO'), 200)
#
#         lista_titulo = []
#         lista_ativo_total = []
#         lista_ativo_circulante = []
#         lista_ativo_circulante_caixa = []
#         lista_ativo_circulante_aplic_finan = []
#         lista_ativo_circulante_contas_rec = []
#         lista_ativo_circulante_estoque = []
#         lista_ativo_circulante_outros = []
#         lista_ativo_nao_circulante = []
#         lista_ativo_nao_circulante_longo_prazo = []
#         lista_ativo_nao_circulante_investimentos = []
#         lista_ativo_nao_circulante_imobilizado = []
#         lista_ativo_nao_circulante_intangivel = []
#         lista_ativo_nao_circulante_outros = []
#         lista_passivo_total = []
#         lista_passivo_circulante = []
#         lista_passivo_circulante_salarios = []
#         lista_passivo_circulante_fornecedores = []
#         lista_passivo_circulante_emprestimos = []
#         lista_passivo_circulante_outros = []
#         lista_passivo_nao_circulante = []
#         lista_passivo_nao_circulante_emprestimos = []
#         lista_passivo_nao_circulante_outros = []
#         lista_passivo_patrimonio_liquido_consolidado = []
#         lista_passivo_patrimonio_capital_social_realizado = []
#         lista_passivo_patrimonio_lucro_prejuizo_acumulado = []
#         lista_passivo_patrimonio_reserva_capital = []
#         lista_passivo_patrimonio_reserva_lucros = []
#         lista_passivo_patrimonio_participacoes = []
#         lista_passivo_patrimonio_outros = []
#
#         for indx, row in enumerate(lista_ativos):
#             lista_titulo.append(row['TRI_REFER'])
#             lista_ativo_total.append(float(row['VLR_ATIVO_TOTAL']))
#             lista_ativo_circulante.append(float(row['VLR_ATIVO_CIRCULANTE']))
#             #lista_ativo_circulante_caixa.append(float(row['VLR_ATIVO_CIRCULANTE_CAIXA']))
#             #lista_ativo_circulante_aplic_finan.append(float(row['VLR_ATIVO_CIRCULANTE_APLIC_FINAN']))
#             #lista_ativo_circulante_contas_rec.append(float(row['VLR_ATIVO_CIRCULANTE_CONTAS_REC']))
#             #lista_ativo_circulante_estoque.append(float(row['VLR_ATIVO_CIRCULANTE_ESTOQUE']))
#             #lista_ativo_circulante_outros.append(float(row['VLR_ATIVO_CIRCULANTE_OUTROS']))
#             lista_ativo_nao_circulante.append(float(row['VLR_ATIVO_NAO_CIRCULANTE']))
#             #lista_ativo_nao_circulante_longo_prazo.append(float(row['VLR_ATIVO_NAO_CIRCULANTE_LONGO_PRAZO']))
#             #lista_ativo_nao_circulante_investimentos.append(float(row['VLR_ATIVO_NAO_CIRCULANTE_INVESTIMENTOS']))
#             #lista_ativo_nao_circulante_imobilizado.append(float(row['VLR_ATIVO_NAO_CIRCULANTE_IMOBILIZADO']))
#             #lista_ativo_nao_circulante_intangivel.append(float(row['VLR_ATIVO_NAO_CIRCULANTE_INTANGIVEL']))
#             #lista_ativo_nao_circulante_outros.append(float(row['VLR_ATIVO_NAO_CIRCULANTE_OUTROS']))
#
#         for indx, row in enumerate(lista_passivos):
#             lista_passivo_total.append(float(row['VLR_PASSIVO_TOTAL']))
#             lista_passivo_circulante.append(float(row['VLR_PASSIVO_CIRCULANTE']))
#             #lista_passivo_circulante_salarios.append(float(row['VLR_PASSIVO_CIRCULANTE_SALARIOS']))
#             #lista_passivo_circulante_fornecedores.append(float(row['VLR_PASSIVO_CIRCULANTE_FORNECEDORES']))
#             #lista_passivo_circulante_emprestimos.append(float(row['VLR_PASSIVO_CIRCULANTE_EMPRESTIMOSS']))
#             #lista_passivo_circulante_outros.append(float(row['VLR_PASSIVO_CIRCULANTE_OUTROS']))
#             lista_passivo_nao_circulante.append(float(row['VLR_PASSIVO_NAO_CIRCULANTE']))
#             #lista_passivo_nao_circulante_emprestimos.append(float(row['VLR_PASSIVO_NAO_CIRCULANTE_EMPRESTIMOSS']))
#             #lista_passivo_nao_circulante_outros.append(float(row['VLR_PASSIVO_NAO_CIRCULANTE_OUTROS']))
#             lista_passivo_patrimonio_liquido_consolidado.append(float(row['VLR_PASSIVO_PATRIMONIO_LIQUIDO_CONSOLIDADO']))
#             #lista_passivo_patrimonio_capital_social_realizado.append(float(row['VLR_PASSIVO_PATRIMONIO_CAPITAL_SOCIAL_REALIZADO']))
#             #lista_passivo_patrimonio_lucro_prejuizo_acumulado.append(float(row['VLR_PASSIVO_PATRIMONIO_LUCRO_PREJUIZO_ACUMULADO']))
#             #lista_passivo_patrimonio_reserva_capital.append(float(row['VLR_PASSIVO_PATRIMONIO_RESERVA_CAPITAL']))
#             #lista_passivo_patrimonio_reserva_lucros.append(float(row['VLR_PASSIVO_PATRIMONIO_RESERVA_LUCROS']))
#             #lista_passivo_patrimonio_participacoes.append(float(row['VLR_PASSIVO_PATRIMONIO_PARTICIPACAO_NAO_CONTROLADORES']))
#             #lista_passivo_patrimonio_outros.append(float(row['VLR_PASSIVO_PATRIMONIO_OUTROS']))
#
#         dados = dict({
#             "listaTitulo": lista_titulo,
#             "listaAtivoTotal": lista_ativo_total,
#             "listaAtivoCirculante": lista_ativo_circulante,
#             "listaAtivoCirculanteCaixa": lista_ativo_circulante_caixa,
#             "listaAtivoCirculanteAplicFinan": lista_ativo_circulante_aplic_finan,
#             "listaAtivoCirculanteContas_rec": lista_ativo_circulante_contas_rec,
#             "listaAtivoCirculanteEstoque": lista_ativo_circulante_estoque,
#             "listaAtivoCirculanteOutros": lista_ativo_circulante_outros,
#             "listaAtivoNaoCirculante": lista_ativo_nao_circulante,
#             "listaAtivoNaoCirculanteLongo_prazo": lista_ativo_nao_circulante_longo_prazo,
#             "listaAtivoNaoCirculanteInvestimentos": lista_ativo_nao_circulante_investimentos,
#             "listaAtivoNaoCirculanteImobilizado": lista_ativo_nao_circulante_imobilizado,
#             "listaAtivoNaoCirculanteIntangivel": lista_ativo_nao_circulante_intangivel,
#             "listaAtivoNaoCirculanteOutros": lista_ativo_nao_circulante_outros,
#             "listaPassivoTotal": lista_passivo_total,
#             "listaPassivoCirculante": lista_passivo_circulante,
#             "listaPassivoCirculanteSalarios": lista_passivo_circulante_salarios,
#             "listaPassivoCirculanteFornecedores": lista_passivo_circulante_fornecedores,
#             "listaPassivoCirculanteEmprestimos": lista_passivo_circulante_emprestimos,
#             "listaPassivoCirculanteOutros": lista_passivo_circulante_outros,
#             "listaPassivoNaoCirculante": lista_passivo_nao_circulante,
#             "listaPassivoNaoCirculanteEmprestimos": lista_passivo_nao_circulante_emprestimos,
#             "listaPassivoNaoCirculanteOutros": lista_passivo_nao_circulante_outros,
#             "listaPassivoPatrimonioLiquidoConsolidado": lista_passivo_patrimonio_liquido_consolidado,
#             "listaPassivoPatrimonioCapitalSocialRealizado": lista_passivo_patrimonio_capital_social_realizado,
#             "listaPassivoPatrimonioLucroPrejuizoAcumulado": lista_passivo_patrimonio_lucro_prejuizo_acumulado,
#             "listaPassivoPatrimonioReservaCapital": lista_passivo_patrimonio_reserva_capital,
#             "listaPassivoPatrimonioReservaLucros": lista_passivo_patrimonio_reserva_lucros,
#             "listaPassivoPatrimonioParticipacoes": lista_passivo_patrimonio_participacoes,
#             "listaPassivoPatrimonioOutros": lista_passivo_patrimonio_outros,
#         })
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_finan_acoes.route('/grid_fatos', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
# def grid_fatos():
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
#             return make_response(get_json_retorno_grid(msg='Ativo não informado!'), 200)
#
#         codigo = str(codigo).strip().upper()
#
#         empresa = ACAOEmpresa.buscar_por_codigo(codigo=codigo)
#         if not empresa:
#             return make_response(get_json_retorno_grid(msg='Empresa não localizada!'), 200)
#
#         id_empresa = int(empresa['ID'])
#
#         dt_env_ini = converter_datetime_str(data=pegar_data_atual(istext=False) + adicionar_meses(meses=-12), fmt="%Y%m%d") + '000000'
#
#         rows = ACAOEmpresaFatoRelevante.get_all(id_empresa=id_empresa, dt_env_ini=dt_env_ini, reg_inicio=1, qtde_por_pagina=10000)
#         if not rows:
#             return make_response(get_json_retorno_grid(rslt='OK', msg='NENHUM RESULTADO ENCONTRADO'), 200)
#
#         lista = [
#             {
#                 "id": str(fato.id),
#                 "empresa": str(fato.nm_empresa),
#                 "data": str(fato.data_env),
#                 "dataFormat": str(fato.data_env_format()),
#                 "link": str(fato.link),
#                 "assunto": str(fato.assunto),
#                 "conteudo": str(fato.conteudo),
#                 "protocolo": str(fato.protocolo)
#             }
#             for fato in rows
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
