# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.alerta import Alerta
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.acao_empresa_ativo_cotacao import ACAOEmpresaAtivoCotacao
# from app.models.fii_fundoimob import FiiFundoImob
# from app.models.fii_fundoimob_cotacao import FiiFundoImobCotacao
# from app.models.etf_indice import ETFIndice
# from app.models.etf_indice_cotacao import ETFIndiceCotacao
# from app.models.bdr_empresa import BDREmpresa
# from app.models.bdr_empresa_cotacao import BDREmpresaCotacao
# from app.models.cripto_empresa import CriptoEmpresa
# from app.models.corretora_lista import CorretoraLista
# from app.models.usuario_apuracao_calculada import UsuarioApuracaoCalculada
# from app.models.usuario_corretora import UsuarioCorretora
# from app.models.usuario_carteira import UsuarioCarteira
# from app.models.usuario_carteira_acao import UsuarioCarteiraAcao
# from app.models.usuario_carteira_fii import UsuarioCarteiraFii
# from app.models.usuario_carteira_etf import UsuarioCarteiraEtf
# from app.models.usuario_carteira_bdr import UsuarioCarteiraBdr
# from app.models.usuario_carteira_cripto import UsuarioCarteiraCripto
# from app.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamento
# from app.models.usuario_acao_empresa_operacao import UsuarioACAOEmpresaOperacao
# from app.models.usuario_fii_fundoimob_lancamento import UsuarioFiiFundoImobLancamento
# from app.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamento
# from app.models.usuario_etf_indice_operacao import UsuarioETFIndiceOperacao
# from app.models.usuario_bdr_empresa_lancamento import UsuarioBDREmpresaLancamento
# from app.models.usuario_bdr_empresa_operacao import UsuarioBDREmpresaOperacao
# from app.models.usuario_cripto_lancamento import UsuarioCriptoLancamento
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_formatacao import decimal_to_str, decimal_prov_to_str, decimal_cripto_to_str, decimal_cripto_curto_to_str
# from app.util.util_datahora import converter_datetime_str, converter_str_to_datetime, pegar_data_hora_atual
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="/operacoes", tags=['operacoes'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
# @login_required
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index(request: _fastapi.Request):
    # return render_template(template_name_or_list="operacoes.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


# @bp_operacoes.route('/grid', methods=['GET', 'POST'])
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
#             codigo = data.get('CodAtivo')
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#             id_corretora = data.get('Corretora')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if dt_ini: dt_ini = str(dt_ini).replace('-', '')
#         if dt_fim: dt_fim = str(dt_fim).replace('-', '')
#
#         tipo_invest = ''
#         if codigo and str(codigo) == 'ACAO': tipo_invest = 'ACAO'
#         if codigo and str(codigo) == 'FII': tipo_invest = 'FII'
#         if codigo and str(codigo) == 'ETF': tipo_invest = 'ETF'
#         if codigo and str(codigo) == 'BDR': tipo_invest = 'BDR'
#         if codigo and str(codigo) == 'CRIPTO': tipo_invest = 'CRIPTO'
#         if tipo_invest: codigo = ''
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             rows = UsuarioACAOEmpresaLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#             lista += [[str(row['DATA']), UsuarioACAOEmpresaLancamento.descricao_tipo(tipo=str(row['TIPO']), troca=str(row['TROCA'])), str(row['CODIGOATIVO']), int(row['QUANT']), decimal_to_str(valor=float(row['VLRPRECO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', decimal_to_str(valor=float(row['VLRTXCORRETAGEM'])), decimal_to_str(valor=float(row['TOTVLRTX'])), decimal_to_str(valor=float(row['TOTVLR'])), decimal_to_str(valor=float(row['VLRCUSTO'])), str(row['ID']), 'ACAO'] for row in rows]
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             rows = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#             lista += [[str(row['DATA']), UsuarioFiiFundoImobLancamento.descricao_tipo(tipo=str(row['TIPO']), troca=str(row['TROCA'])), str(row['CODIGOFUNDO']), int(row['QUANT']), decimal_to_str(valor=float(row['VLRPRECO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', decimal_to_str(valor=float(row['VLRTXCORRETAGEM'])), decimal_to_str(valor=float(row['TOTVLRTX'])), decimal_to_str(valor=float(row['TOTVLR'])), decimal_to_str(valor=float(row['VLRCUSTO'])), str(row['ID']), 'FII'] for row in rows]
#
#         if not tipo_invest or str(tipo_invest) == 'ETF':
#             rows = UsuarioETFIndiceLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#             lista += [[str(row['DATA']), UsuarioETFIndiceLancamento.descricao_tipo(tipo=str(row['TIPO']), troca=str(row['TROCA'])), str(row['CODIGOINDICE']), int(row['QUANT']), decimal_to_str(valor=float(row['VLRPRECO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', decimal_to_str(valor=float(row['VLRTXCORRETAGEM'])), decimal_to_str(valor=float(row['TOTVLRTX'])), decimal_to_str(valor=float(row['TOTVLR'])), decimal_to_str(valor=float(row['VLRCUSTO'])), str(row['ID']), 'ETF'] for row in rows]
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             rows = UsuarioBDREmpresaLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#             lista += [[str(row['DATA']), UsuarioBDREmpresaLancamento.descricao_tipo(tipo=str(row['TIPO']), troca=str(row['TROCA'])), str(row['CODIGOBDR']), int(row['QUANT']), decimal_to_str(valor=float(row['VLRPRECO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', decimal_to_str(valor=float(row['VLRTXCORRETAGEM'])), decimal_to_str(valor=float(row['TOTVLRTX'])), decimal_to_str(valor=float(row['TOTVLR'])), decimal_to_str(valor=float(row['VLRCUSTO'])), str(row['ID']), 'BDR'] for row in rows]
#
#         if not tipo_invest or str(tipo_invest) == 'CRIPTO':
#             rows = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, codigo=codigo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#             lista += [[str(row['DATA']), UsuarioCriptoLancamento.descricao_tipo(tipo=str(row['TIPO'])), str(row['CODIGOCRIPTO']), float(row['QUANT']), decimal_cripto_to_str(valor=float(row['VLRPRECO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', decimal_to_str(valor=float(row['VLRTAXA'])), decimal_to_str(valor=float(row['VLRTAXA'])), decimal_to_str(valor=float(row['TOTVLR'])), decimal_cripto_to_str(valor=float(row['VLRCUSTO'])), str(row['ID']), 'CRIPTO'] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/salvar', methods=['GET', 'POST'])
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
#             id_lancamento = data.get('Id')
#             id_corretora = data.get('Corretora')
#             codigo = data.get('Ativo')
#             tipo = data.get('Tipo')
#             dt_lanc = data.get('Data')
#             quant = data.get('Quant')
#             vlr_preco = data.get('Preco')
#             vlr_corretagem = data.get('TxCorret')
#             vlr_liquidacao = data.get('TxLiquid')
#             vlr_emolumentos = data.get('TxEmol')
#             vlr_iss = data.get('TxISS')
#             vlr_irpf = data.get('TxIRRF')
#             vlr_outras = data.get('TxOutros')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Código não informado.'), 200)
#         if not tipo: return make_response(get_json_retorno_metodo(msg='Tipo não informado.'), 200)
#         if not dt_lanc: return make_response(get_json_retorno_metodo(msg='Data não informada.'), 200)
#         if not quant: return make_response(get_json_retorno_metodo(msg='Quant. não informada.'), 200)
#
#         if dt_lanc: dt_lanc = str(dt_lanc).replace('-', '')
#         if id_lancamento and int(id_lancamento) <= 0: id_lancamento = None
#
#         quant = float(str(quant).replace('.', '').replace(',', '.')) if quant else 0.0
#         vlr_preco = float(str(vlr_preco).replace('.', '').replace(',', '.')) if vlr_preco else 0.0
#         vlr_corretagem = float(str(vlr_corretagem).replace('.', '').replace(',', '.')) if vlr_corretagem else 0.0
#         vlr_liquidacao = float(str(vlr_liquidacao).replace('.', '').replace(',', '.')) if vlr_liquidacao else 0.0
#         vlr_emolumentos = float(str(vlr_emolumentos).replace('.', '').replace(',', '.')) if vlr_emolumentos else 0.0
#         vlr_iss = float(str(vlr_iss).replace('.', '').replace(',', '.')) if vlr_iss else 0.0
#         vlr_irpf = float(str(vlr_irpf).replace('.', '').replace(',', '.')) if vlr_irpf else 0.0
#         vlr_outras = float(str(vlr_outras).replace('.', '').replace(',', '.')) if vlr_outras else 0.0
#
#         if str(tipo) != "A" and str(tipo) != "C" and str(tipo) != "V" and str(tipo) != "B" and str(tipo) != "D" and str(tipo) != "G":
#             return make_response(get_json_retorno_metodo(msg='Tipo Inválido.'), 200)
#
#         if (str(tipo) == "A" or str(tipo) == "C" or str(tipo) == "V" or str(tipo) == "B") and (not vlr_preco or float(vlr_preco) <= 0.0):
#             return make_response(get_json_retorno_metodo(msg='Preço não informado.'), 200)
#
#         tipo_invest = ''
#         id_ativo = None
#
#         if not tipo_invest:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'ACAO'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'FII'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = ETFIndice.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'ETF'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'BDR'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = CriptoEmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'CRIPTO'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest or not id_ativo:
#             return make_response(get_json_retorno_metodo(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         if id_corretora:
#             if not UsuarioCorretora.get_by_usuario(id_usuario=id_usuario, id=int(id_corretora)):
#                 return make_response(get_json_retorno_metodo(msg='Corretora não localizada.'), 200)
#
#         if str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'ETF' or str(tipo_invest) == 'BDR' or str(tipo_invest) == 'CRIPTO':
#             if str(tipo) == 'A': return make_response(get_json_retorno_metodo(msg='Tipo inválido para o Ativo.'), 200)
#
#         if str(tipo) == 'V':
#             UsuarioCarteira.gerar(id_usuario=id_usuario, codigo=str(codigo))
#             qtd_tot_compra = 0
#             qtd_tot_bonus = 0
#             qtd_tot_venda = 0
#             if str(tipo_invest) == 'ACAO':
#                 qtd_tot_compra = float(UsuarioACAOEmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_ativo=int(id_ativo)))
#                 qtd_tot_bonus = float(UsuarioACAOEmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_ativo=int(id_ativo)))
#                 qtd_tot_venda = float(UsuarioACAOEmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_ativo=int(id_ativo), id_lanc=id_lancamento))
#                 qtd_tot_venda = (qtd_tot_venda - float(quant)) if id_lancamento else (qtd_tot_venda + float(quant))
#             elif str(tipo_invest) == 'FII':
#                 qtd_tot_compra = float(UsuarioFiiFundoImobLancamento.buscar_total_compra(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#                 qtd_tot_bonus = float(UsuarioFiiFundoImobLancamento.buscar_total_bonus(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#                 qtd_tot_venda = float(UsuarioFiiFundoImobLancamento.buscar_total_venda(id_usuario=id_usuario, id_fundo=int(id_ativo), id_lanc=id_lancamento))
#             elif str(tipo_invest) == 'ETF':
#                 qtd_tot_compra = float(UsuarioETFIndiceOperacao.buscar_total_compra(id_usuario=id_usuario, id_indice=int(id_ativo)))
#                 qtd_tot_bonus = float(UsuarioETFIndiceOperacao.buscar_total_bonus(id_usuario=id_usuario, id_indice=int(id_ativo)))
#                 qtd_tot_venda = float(UsuarioETFIndiceOperacao.buscar_total_venda(id_usuario=id_usuario, id_indice=int(id_ativo), id_lanc=id_lancamento))
#                 qtd_tot_venda = (qtd_tot_venda - float(quant)) if id_lancamento else (qtd_tot_venda + float(quant))
#             elif str(tipo_invest) == 'BDR':
#                 qtd_tot_compra = float(UsuarioBDREmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_bdr=int(id_ativo)))
#                 qtd_tot_bonus = float(UsuarioBDREmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_bdr=int(id_ativo)))
#                 qtd_tot_venda = float(UsuarioBDREmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_bdr=int(id_ativo), id_lanc=id_lancamento))
#                 qtd_tot_venda = (qtd_tot_venda - float(quant)) if id_lancamento else (qtd_tot_venda + float(quant))
#             elif str(tipo_invest) == 'CRIPTO':
#                 qtd_tot_compra = float(UsuarioCriptoLancamento.buscar_total_compra(id_usuario=id_usuario, id_cripto=int(id_ativo)))
#                 qtd_tot_venda = float(UsuarioCriptoLancamento.buscar_total_venda(id_usuario=id_usuario, id_cripto=int(id_ativo), id_lanc=id_lancamento))
#             if float(qtd_tot_venda) < 0.0 or float(qtd_tot_venda) > float(qtd_tot_compra) + float(qtd_tot_bonus):
#                 return make_response(get_json_retorno_metodo(msg='Venda Superior('+decimal_to_str(valor=float(qtd_tot_venda))+') a quant. Comprada('+decimal_to_str(valor=float(qtd_tot_compra)+float(qtd_tot_bonus))+').'), 200)
#
#         lanc = None
#
#         if str(tipo_invest) == 'ACAO':
#             if id_lancamento:
#                 lanc = UsuarioACAOEmpresaLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#                 if lanc and int(lanc.id_ativo) != int(id_ativo):
#                     UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(lanc.id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                     UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(lanc.id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                     UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(lanc.id_ativo))  # Excluir Todas as Operações do Ativo
#                     lanc.id_ativo = int(id_ativo)
#             else:
#                 lanc = UsuarioACAOEmpresaLancamento(id_ativo=int(id_ativo))
#
#         elif str(tipo_invest) == 'FII':
#             if id_lancamento:
#                 lanc = UsuarioFiiFundoImobLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#                 if lanc and int(lanc.id_fundo) != int(id_ativo):
#                     UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(lanc.id_fundo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                     UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(lanc.id_fundo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                     lanc.id_fundo = int(id_ativo)
#             else:
#                 lanc = UsuarioFiiFundoImobLancamento(id_fundo=int(id_ativo))
#
#         elif str(tipo_invest) == 'ETF':
#             if id_lancamento:
#                 lanc = UsuarioETFIndiceLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#                 if lanc and int(lanc.id_indice) != int(id_ativo):
#                     UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(lanc.id_indice))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                     UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(lanc.id_indice))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                     UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(lanc.id_indice))   # Excluir Todas as Operações do Ativo
#                     lanc.id_indice = int(id_ativo)
#             else:
#                 lanc = UsuarioETFIndiceLancamento(id_indice=int(id_ativo))
#
#         elif str(tipo_invest) == 'BDR':
#             if id_lancamento:
#                 lanc = UsuarioBDREmpresaLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#                 if lanc and int(lanc.id_bdr) != int(id_ativo):
#                     UsuarioCarteiraBdr.resetar_indices(id_usuario=id_usuario, id_bdr=int(lanc.id_bdr))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                     UsuarioBDREmpresaLancamento.resetar_indices(id_usuario=id_usuario, id_bdr=int(lanc.id_bdr))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                     UsuarioBDREmpresaOperacao.resetar_indices(id_usuario=id_usuario, id_bdr=int(lanc.id_bdr))   # Excluir Todas as Operações do Ativo
#                     lanc.id_bdr = int(id_ativo)
#             else:
#                 lanc = UsuarioBDREmpresaLancamento(id_bdr=int(id_ativo))
#
#         elif str(tipo_invest) == 'CRIPTO':
#             if id_lancamento:
#                 lanc = UsuarioCriptoLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#                 if lanc and int(lanc.id_cripto) != int(id_ativo):
#                     UsuarioCarteiraCripto.resetar_ativos(id_usuario=id_usuario, id_cripto=int(lanc.id_cripto))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                     UsuarioCriptoLancamento.resetar_ativos(id_usuario=id_usuario, id_cripto=int(lanc.id_cripto))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                     lanc.id_cripto = int(id_ativo)
#             else:
#                 lanc = UsuarioCriptoLancamento(id_cripto=int(id_ativo))
#
#         if not lanc:
#             return make_response(get_json_retorno_metodo(msg='Lançamento não Localizado.'), 200)
#
#         lanc.id_usuario = id_usuario
#         lanc.tipo = str(tipo)
#         lanc.data = str(dt_lanc)
#         lanc.quant = float(quant) if quant and float(quant) > 0 else 0
#
#         if str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'ETF' or str(tipo_invest) == 'BDR':
#             lanc.quant_pend = float(quant) if quant and float(quant) > 0 else 0
#         elif str(tipo_invest) == 'FII' or str(tipo_invest) == 'CRIPTO':
#             lanc.quant_orig = float(quant) if quant and float(quant) > 0 else 0
#
#         lanc.vlr_preco = 0.0
#         if str(tipo) == 'A' or str(tipo) == 'C' or str(tipo) == 'B' or str(tipo) == 'V':
#             lanc.vlr_preco = float(vlr_preco) if vlr_preco and float(vlr_preco) > 0.0 else 0.0
#             lanc.id_corretora = int(id_corretora) if id_corretora else None
#
#         lanc.vlr_corretagem = 0.0
#         lanc.vlr_liquidacao = 0.0
#         lanc.vlr_emolumentos = 0.0
#         lanc.vlr_iss = 0.0
#         lanc.vlr_irpf = 0.0
#         lanc.vlr_outras = 0.0
#         if str(tipo) == 'C' or str(tipo) == 'V':
#             lanc.vlr_corretagem = float(vlr_corretagem) if vlr_corretagem and float(vlr_corretagem) > 0.0 else 0.0
#             lanc.vlr_liquidacao = float(vlr_liquidacao) if vlr_liquidacao and float(vlr_liquidacao) > 0.0 else 0.0
#             lanc.vlr_emolumentos = float(vlr_emolumentos) if vlr_emolumentos and float(vlr_emolumentos) > 0.0 else 0.0
#             lanc.vlr_iss = float(vlr_iss) if vlr_iss and float(vlr_iss) > 0.0 else 0.0
#             lanc.vlr_irpf = float(vlr_irpf) if vlr_irpf and float(vlr_irpf) > 0.0 else 0.0
#             lanc.vlr_outras = float(vlr_outras) if vlr_outras and float(vlr_outras) > 0.0 else 0.0
#
#         if str(tipo_invest) == 'FII' or str(tipo_invest) == 'CRIPTO':
#             lanc.vlr_preco_medio = 0.0
#             lanc.tot_vlr_valorizacao = 0.0
#             lanc.perc_valorizacao = 0.0
#
#         lanc.calc_tot_preco()
#         lanc.calc_tot_taxa()
#         lanc.calc_total()
#         lanc.calc_custo()
#
#         lanc.situacao = 'A' if (str(tipo) == 'D' or str(tipo) == 'G') and not vlr_preco else 'P'  # A-Ativo # P-PendenteDefinicaoSituacao
#         lanc.salvar()
#
#         if str(tipo_invest) == 'ACAO':
#             UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Excluir Todas as Operações do Ativo
#             if str(tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='C')  # C - AÇÂO-Comum
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='D')  # D - AÇÂO-Day-Trade
#
#         elif str(tipo_invest) == 'FII':
#             UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             if str(tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='F')  # F - FII
#
#         elif str(tipo_invest) == 'ETF':
#             UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Excluir Todas as Operações do Ativo
#             if str(tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='E')  # E - ETF-Comum
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='G')  # G - ETF-Day-Trade
#
#         elif str(tipo_invest) == 'BDR':
#             UsuarioCarteiraBdr.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioBDREmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioBDREmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Excluir Todas as Operações do Ativo
#             if str(tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='I')  # I - BDR-Comum
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='J')  # J - BDR-Day-Trade
#
#         elif str(tipo_invest) == 'CRIPTO':
#             UsuarioCarteiraCripto.resetar_ativos(id_usuario=id_usuario, id_cripto=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioCriptoLancamento.resetar_ativos(id_usuario=id_usuario, id_cripto=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             if str(tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='K')  # K - CRIPTO
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Dados salvo com sucesso.'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/salvarincorporacao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_incorporacao():
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
#             dt_lanc = data.get('Data')
#             fator = data.get('Fator')
#             id_corretora = data.get('Corretora')
#             codigo_atual = data.get('CodAtivoAtual')
#             quant_atual = data.get('QuantAtual')
#             preco_medio_atual = data.get('PrecoMedioAtual')
#             codigo_novo = data.get('CodAtivoNovo')
#             quant_novo = data.get('QuantNovo')
#             preco_medio_novo = data.get('PrecoMedioNovo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not dt_lanc: return make_response(get_json_retorno_metodo(msg='Data não informada.'), 200)
#         if not fator: return make_response(get_json_retorno_metodo(msg='Fator não informado.'), 200)
#
#         if not codigo_atual: return make_response(get_json_retorno_metodo(msg='Código Atual não informado.'), 200)
#         if not quant_atual: return make_response(get_json_retorno_metodo(msg='Quant. Atual não informada.'), 200)
#         if not preco_medio_atual: return make_response(get_json_retorno_metodo(msg='Preço Médio Atual não informado.'), 200)
#
#         if not codigo_novo: return make_response(get_json_retorno_metodo(msg='Código Novo não informado.'), 200)
#         if not quant_novo: return make_response(get_json_retorno_metodo(msg='Quant. Novo não informada.'), 200)
#         if not preco_medio_novo: return make_response(get_json_retorno_metodo(msg='Preço Médio Novo não informado.'), 200)
#
#         if dt_lanc: dt_lanc = str(dt_lanc).replace('-', '')
#         preco_medio_atual = float(str(preco_medio_atual).replace('.', '').replace(',', '.')) if preco_medio_atual else 0.0
#         preco_medio_novo = float(str(preco_medio_novo).replace('.', '').replace(',', '.')) if preco_medio_novo else 0.0
#
#         if preco_medio_atual <= 0.0: return make_response(get_json_retorno_metodo(msg='Preço Médio Atual não informado.'), 200)
#         if preco_medio_novo <= 0.0: return make_response(get_json_retorno_metodo(msg='Preço Médio Novo não informado.'), 200)
#
#         tipo_invest_atual = ''
#         id_ativo_atual = None
#
#         if not tipo_invest_atual:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo_atual))
#             if row:
#                 tipo_invest_atual = 'ACAO'
#                 id_ativo_atual = int(row.id)
#
#         if not tipo_invest_atual:
#             row = FiiFundoImob.get_by_codigo(codigo=str(codigo_atual))
#             if row:
#                 tipo_invest_atual = 'FII'
#                 id_ativo_atual = int(row.id)
#
#         if not tipo_invest_atual:
#             row = ETFIndice.get_by_codigo(codigo=str(codigo_atual))
#             if row:
#                 tipo_invest_atual = 'ETF'
#                 id_ativo_atual = int(row.id)
#
#         if not tipo_invest_atual:
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo_atual))
#             if row:
#                 tipo_invest_atual = 'BDR'
#                 id_ativo_atual = int(row.id)
#
#         if not tipo_invest_atual or not id_ativo_atual:
#             return make_response(get_json_retorno_metodo(msg='Código do Ativo Atual não localizado.'), 200)
#
#         tipo_invest_novo = ''
#         id_ativo_novo = None
#
#         if not tipo_invest_novo:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo_novo))
#             if row:
#                 tipo_invest_novo = 'ACAO'
#                 id_ativo_novo = int(row.id)
#
#         if not tipo_invest_novo:
#             row = FiiFundoImob.get_by_codigo(codigo=str(codigo_novo))
#             if row:
#                 tipo_invest_novo = 'FII'
#                 id_ativo_novo = int(row.id)
#
#         if not tipo_invest_novo:
#             row = ETFIndice.get_by_codigo(codigo=str(codigo_novo))
#             if row:
#                 tipo_invest_novo = 'ETF'
#                 id_ativo_novo = int(row.id)
#
#         if not tipo_invest_novo:
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo_novo))
#             if row:
#                 tipo_invest_novo = 'BDR'
#                 id_ativo_novo = int(row.id)
#
#         if not tipo_invest_novo or not id_ativo_novo:
#             return make_response(get_json_retorno_metodo(msg='Código do Ativo Novo não localizado.'), 200)
#
#         if tipo_invest_atual != tipo_invest_novo:
#             return make_response(get_json_retorno_metodo(msg='Tipo do Ativo Atual('+tipo_invest_atual+') diferente do Tipo de Ativo Novo('+tipo_invest_novo+').'), 200)
#
#         if int(id_ativo_atual) == int(id_ativo_novo):
#             return make_response(get_json_retorno_metodo(msg='Ativo Atual igual ao Ativo Novo.'), 200)
#
#         id_usuario = current_user.id
#
#         if id_corretora:
#             if not UsuarioCorretora.get_by_usuario(id_usuario=id_usuario, id=int(id_corretora)):
#                 return make_response(get_json_retorno_metodo(msg='Corretora não localizada.'), 200)
#
#         lancVenda = None
#         if str(tipo_invest_atual) == 'ACAO': lancVenda = UsuarioACAOEmpresaLancamento(id_ativo=int(id_ativo_atual), id_usuario=int(id_usuario))
#         elif str(tipo_invest_atual) == 'FII': lancVenda = UsuarioFiiFundoImobLancamento(id_fundo=int(id_ativo_atual), id_usuario=int(id_usuario))
#         elif str(tipo_invest_atual) == 'ETF': lancVenda = UsuarioETFIndiceLancamento(id_indice=int(id_ativo_atual), id_usuario=int(id_usuario))
#         elif str(tipo_invest_atual) == 'BDR': lancVenda = UsuarioBDREmpresaLancamento(id_bdr=int(id_ativo_atual), id_usuario=int(id_usuario))
#         if not lancVenda: return make_response(get_json_retorno_metodo(msg='Lançamento de Venda não Localizado.'), 200)
#
#         lancVenda.tipo = 'V'  # V-Venda
#         lancVenda.data = str(dt_lanc)
#         lancVenda.quant = int(quant_atual) if quant_atual and int(quant_atual) > 0 else 0
#         if str(tipo_invest_atual) == 'ACAO' or str(tipo_invest_atual) == 'ETF' or str(tipo_invest_atual) == 'BDR':
#             lancVenda.quant_pend = int(quant_atual) if quant_atual and int(quant_atual) > 0 else 0
#         elif str(tipo_invest_atual) == 'FII':
#             lancVenda.quant_orig = int(quant_atual) if quant_atual and int(quant_atual) > 0 else 0
#         lancVenda.vlr_preco = float(preco_medio_atual) if preco_medio_atual and float(preco_medio_atual) > 0.0 else 0.0
#         lancVenda.id_corretora = int(id_corretora) if id_corretora else None
#         lancVenda.troca = 'S' # S-Sim
#         lancVenda.situacao = 'P' # P-PendenteDefinicaoSituacao
#         lancVenda.calc_tot_preco()
#         lancVenda.calc_tot_taxa()
#         lancVenda.calc_total()
#         lancVenda.calc_custo()
#         lancVenda.salvar()
#
#         if str(tipo_invest_atual) == 'ACAO':
#             UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_atual))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_atual))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_atual))  # Excluir Todas as Operações do Ativo
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='C')  # C - AÇÂO-Comum
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='D')  # D - AÇÂO-Day-Trade
#         elif str(tipo_invest_atual) == 'FII':
#             UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo_atual))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo_atual))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='F')  # F - FII
#         elif str(tipo_invest_atual) == 'ETF':
#             UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_atual))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_atual))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_atual))  # Excluir Todas as Operações do Ativo
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='E')  # E - ETF-Comum
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='G')  # G - ETF-Day-Trade
#         elif str(tipo_invest_atual) == 'BDR':
#             UsuarioCarteiraBdr.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_atual))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioBDREmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_atual))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioBDREmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_atual))  # Excluir Todas as Operações do Ativo
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='I')  # I - BDR-Comum
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='J')  # J - BDR-Day-Trade
#
#         lancCompra = None
#         if str(tipo_invest_novo) == 'ACAO': lancCompra = UsuarioACAOEmpresaLancamento(id_ativo=int(id_ativo_novo), id_usuario=int(id_usuario))
#         elif str(tipo_invest_novo) == 'FII': lancCompra = UsuarioFiiFundoImobLancamento(id_fundo=int(id_ativo_novo), id_usuario=int(id_usuario))
#         elif str(tipo_invest_novo) == 'ETF': lancCompra = UsuarioETFIndiceLancamento(id_indice=int(id_ativo_novo), id_usuario=int(id_usuario))
#         elif str(tipo_invest_novo) == 'BDR': lancCompra = UsuarioBDREmpresaLancamento(id_bdr=int(id_ativo_novo), id_usuario=int(id_usuario))
#         if not lancCompra: return make_response(get_json_retorno_metodo(msg='Lançamento de Compra não Localizado.'), 200)
#
#         lancCompra.tipo = 'C'  # C-Compra
#         lancCompra.data = str(dt_lanc)
#         lancCompra.quant = int(quant_novo) if quant_novo and int(quant_novo) > 0 else 0
#         if str(tipo_invest_novo) == 'ACAO' or str(tipo_invest_novo) == 'ETF' or str(tipo_invest_novo) == 'BDR':
#             lancCompra.quant_pend = int(quant_novo) if quant_novo and int(quant_novo) > 0 else 0
#         elif str(tipo_invest_novo) == 'FII':
#             lancCompra.quant_orig = int(quant_novo) if quant_novo and int(quant_novo) > 0 else 0
#         lancCompra.vlr_preco = float(preco_medio_novo) if preco_medio_novo and float(preco_medio_novo) > 0.0 else 0.0
#         lancCompra.id_corretora = int(id_corretora) if id_corretora else None
#         lancCompra.troca = 'S' # S-Sim
#         lancCompra.situacao = 'P'  # P-PendenteDefinicaoSituacao
#         lancCompra.calc_tot_preco()
#         lancCompra.calc_tot_taxa()
#         lancCompra.calc_total()
#         lancCompra.calc_custo()
#         lancCompra.salvar()
#
#         if str(tipo_invest_novo) == 'ACAO':
#             UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_novo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_novo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_novo))  # Excluir Todas as Operações do Ativo
#         elif str(tipo_invest_novo) == 'FII':
#             UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo_novo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo_novo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#         elif str(tipo_invest_novo) == 'ETF':
#             UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_novo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_novo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_novo))  # Excluir Todas as Operações do Ativo
#         elif str(tipo_invest_novo) == 'BDR':
#             UsuarioCarteiraBdr.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_novo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioBDREmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_novo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioBDREmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_novo))  # Excluir Todas as Operações do Ativo
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Dados salvo com sucesso.'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/salvartroca', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_troca():
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
#             codigo_atual = data.get('CodAtivoAtual')
#             codigo_novo = data.get('CodAtivoNovo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not codigo_atual: return make_response(get_json_retorno_metodo(msg='Código Atual não informado.'), 200)
#         if not codigo_novo: return make_response(get_json_retorno_metodo(msg='Código Novo não informado.'), 200)
#
#         tipo_invest_atual = ''
#         id_ativo_atual = None
#
#         if not tipo_invest_atual:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo_atual))
#             if row:
#                 tipo_invest_atual = 'ACAO'
#                 id_ativo_atual = int(row.id)
#
#         if not tipo_invest_atual:
#             row = FiiFundoImob.get_by_codigo(codigo=str(codigo_atual))
#             if row:
#                 tipo_invest_atual = 'FII'
#                 id_ativo_atual = int(row.id)
#
#         if not tipo_invest_atual:
#             row = ETFIndice.get_by_codigo(codigo=str(codigo_atual))
#             if row:
#                 tipo_invest_atual = 'ETF'
#                 id_ativo_atual = int(row.id)
#
#         if not tipo_invest_atual:
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo_atual))
#             if row:
#                 tipo_invest_atual = 'BDR'
#                 id_ativo_atual = int(row.id)
#
#         if not tipo_invest_atual or not id_ativo_atual:
#             return make_response(get_json_retorno_metodo(msg='Código do Ativo Atual não localizado.'), 200)
#
#         tipo_invest_novo = ''
#         id_ativo_novo = None
#
#         if not tipo_invest_novo:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo_novo))
#             if row:
#                 tipo_invest_novo = 'ACAO'
#                 id_ativo_novo = int(row.id)
#
#         if not tipo_invest_novo:
#             row = FiiFundoImob.get_by_codigo(codigo=str(codigo_novo))
#             if row:
#                 tipo_invest_novo = 'FII'
#                 id_ativo_novo = int(row.id)
#
#         if not tipo_invest_novo:
#             row = ETFIndice.get_by_codigo(codigo=str(codigo_novo))
#             if row:
#                 tipo_invest_novo = 'ETF'
#                 id_ativo_novo = int(row.id)
#
#         if not tipo_invest_novo:
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo_novo))
#             if row:
#                 tipo_invest_novo = 'BDR'
#                 id_ativo_novo = int(row.id)
#
#         if not tipo_invest_novo or not id_ativo_novo:
#             return make_response(get_json_retorno_metodo(msg='Código do Ativo Novo não localizado.'), 200)
#
#         if tipo_invest_atual != tipo_invest_novo:
#             return make_response(get_json_retorno_metodo(msg='Tipo do Ativo Atual('+tipo_invest_atual+') diferente do Tipo de Ativo Novo('+tipo_invest_novo+').'), 200)
#
#         if int(id_ativo_atual) == int(id_ativo_novo):
#             return make_response(get_json_retorno_metodo(msg='Ativo Atual igual ao Ativo Novo.'), 200)
#
#         id_usuario = current_user.id
#
#         if str(tipo_invest_atual) == 'ACAO':
#             # Antigo
#             UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_atual))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_atual))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_atual))  # Excluir Todas as Operações do Ativo
#             # Novo
#             UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_novo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_novo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo_novo))  # Excluir Todas as Operações do Ativo
#             # Troca
#             UsuarioCarteiraAcao.trocar_ativos(id_usuario=id_usuario, id_ativo_atual=int(id_ativo_atual), id_ativo_novo=int(id_ativo_novo))
#             # Apuracao
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='C')  # C - AÇÂO-Comum
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='D')  # D - AÇÂO-Day-Trade
#
#         elif str(tipo_invest_atual) == 'FII':
#             # Antigo
#             UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo_atual))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo_atual))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             # Novo
#             UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo_novo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo_novo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             # Troca
#             UsuarioCarteiraFii.trocar_ativos(id_usuario=id_usuario, id_fundo_atual=int(id_ativo_atual), id_fundo_novo=int(id_ativo_novo))
#             # Apuracao
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='F')  # F - FII
#
#         elif str(tipo_invest_atual) == 'ETF':
#             # Antigo
#             UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_atual))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_atual))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_atual))  # Excluir Todas as Operações do Ativo
#             # Novo
#             UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_novo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_novo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo_novo))  # Excluir Todas as Operações do Ativo
#             # Troca
#             UsuarioCarteiraEtf.trocar_ativos(id_usuario=id_usuario, id_indice_atual=int(id_ativo_atual), id_indice_novo=int(id_ativo_novo))
#             # Apuracao
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='E')  # E - ETF-Comum
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='G')  # G - ETF-Day-Trade
#
#         elif str(tipo_invest_atual) == 'BDR':
#             # Antigo
#             UsuarioCarteiraBdr.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_atual))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioBDREmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_atual))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioBDREmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_atual))  # Excluir Todas as Operações do Ativo
#             # Novo
#             UsuarioCarteiraBdr.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_novo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioBDREmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_novo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             UsuarioBDREmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo_novo))  # Excluir Todas as Operações do Ativo
#             # Troca
#             UsuarioCarteiraBdr.trocar_ativos(id_usuario=id_usuario, id_bdr_atual=int(id_ativo_atual), id_bdr_novo=int(id_ativo_novo))
#             # Apuracao
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='I')  # I - BDR-Comum
#             UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='J')  # J - BDR-Day-Trade
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Dados salvo com sucesso.'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/importarcsv', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def importar_csv():
#     try:
#
#         if 'arquivo' not in request.files:
#             return make_response(get_json_retorno_grid(msg='Nenhuma Arquivo informado.'), 200)
#
#         file = request.files['arquivo']
#
#         if file.filename == '':
#             return make_response(get_json_retorno_grid(msg='Nenhuma Arquivo informado.'), 200)
#
#         id_usuario = current_user.id
#
#         ext = file.filename.rsplit(".", 1)[1]
#         if ext.lower() != 'csv' and ext.lower() != '.csv':
#             return make_response(get_json_retorno_grid(msg="Arquivo não é uma extensão válida - " + file.filename), 200)
#
#         # array('application/vnd.ms-excel','application/vnd.msexcel','text/plain','text/csv','text/tsv', 'application/txt','application/octet-stream','text/anytext','application/csv','text/comma-separated-values','application/excel');
#         # $fileSize <= 0 # $msg = "Arquivo vazio - " . $fileName;
#         # $fileSize > 10485760 ){  // 10,485,760 # $msg = "Arquivo deve ser de no máximo 10MB - " .$fileName;
#
#         filename = 'user_'+str(id_usuario)+'_' + pegar_data_hora_atual() + '.' + ext.lower()
#
#         path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../' + current_app.config['CSV_OPER_UPLOADS'])
#         file.save(os.path.join(path, filename))
#
#         # import pandas as pd
#         # df = pd.read_csv(filepath_or_buffer=os.path.join(path, filename), sep=';', decimal=',', encoding='UTF-8')  # ISO-8859-1 # UTF-8
#         # print(df)
#
#         lista_import = []
#
#         import csv
#         with open(os.path.join(path, filename), mode='r', encoding='utf-8') as csvfile:
#
#             rows = csv.reader(csvfile, delimiter=';')
#             # rows = csv.DictReader(csvfile)
#
#             indx = -1
#             for row in rows:
#
#                 if not row: continue
#
#                 dt_lanc = str(row[0]).strip() if row[0] else ''
#                 tipo = str(row[1]).strip()[0:1] if row[1] else ''
#                 codigo = str(row[2]).strip().upper() if row[2] else ''
#                 quant = str(row[3]).strip() if row[3] else ''
#                 vlr_preco = str(row[4]).strip() if row[4] else ''
#
#                 try:
#                     vlr_corretagem = str(row[5]).strip() if row[5] else ''
#                 except:
#                     vlr_corretagem = '0,00'
#
#                 try:
#                     vlr_liquidacao = str(row[6]).strip() if row[6] else ''
#                 except:
#                     vlr_liquidacao = '0,00'
#
#                 try:
#                     vlr_emolumentos = str(row[7]).strip() if row[7] else ''
#                 except:
#                     vlr_emolumentos = '0,00'
#
#                 try:
#                     vlr_iss = str(row[8]).strip() if row[8] else ''
#                 except:
#                     vlr_iss = '0,00'
#
#                 try:
#                     vlr_irpf = str(row[9]).strip() if row[9] else ''
#                 except:
#                     vlr_irpf = '0,00'
#
#                 try:
#                     vlr_outras = str(row[10]).strip() if row[10] else ''
#                 except:
#                     vlr_outras = '0,00'
#
#                 try:
#                     id_corretora  = None
#                     nome_corretora = str(row[11]).strip().replace('"', '').replace("'", "") if row[11] else ''
#                 except:
#                     nome_corretora = ''
#
#                 if not dt_lanc or not tipo or not codigo or not quantidade: continue
#                 if str(dt_lanc)[0:1] == 'D': continue
#
#                 dt_lanc = str(dt_lanc).replace('/', '').replace('-', '').ljust(8,'0')
#                 dt_lanc = dt_lanc[4:8] + dt_lanc[2:4] + dt_lanc[0:2]
#                 # if str(tipo) == 'A': tipo = 'G'
#
#                 indx += 1
#                 lista_import.append({'INDEX': str(int(indx)+1), 'ID': '', 'DATA': str(dt_lanc), 'TIPO': str(tipo), 'CODIGO': str(codigo), 'QUANT': str(quant), 'VLRPRECO': str(vlr_preco), 'VLRTXCORRETAGEM': str(vlr_corretagem), 'VLRTXLIQUIDACAO': str(vlr_liquidacao), 'VLRTXEMOLUMENTOS': str(vlr_emolumentos), 'VLRTXISS': str(vlr_iss), 'VLRTXIRRF': str(vlr_irpf), 'VLRTXOUTRAS': str(vlr_outras), 'SITUACAO': 'Não Importado', 'TIPO_INVEST': '', 'CORRETORA': str(nome_corretora)})
#
#                 if not vlr_preco or str(vlr_preco) == '' or str(vlr_preco) == ',' or str(vlr_preco) == ',0' or str(vlr_preco) == ',00' or str(vlr_preco) == '0,00':
#                     vlr_preco = '0,00'
#
#                 try:
#                     quant = float(str(quant).replace('.', '').replace(',', '.')) if quant else 0.0
#                     lista_import[indx]['QUANT'] = str(quant)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Quantidade não informado ou inválido.'
#                     continue
#
#                 try:
#                     vlr_preco = float(str(vlr_preco).replace('.', '').replace(',', '.')) if vlr_preco else 0.0
#                     lista_import[indx]['VLRPRECO'] = str(vlr_preco)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Preço não informado ou inválido.'
#                     continue
#
#                 try:
#                     vlr_corretagem = float(str(vlr_corretagem).replace('.', '').replace(',', '.')) if vlr_corretagem else 0.0
#                     lista_import[indx]['VLRTXCORRETAGEM'] = str(vlr_corretagem)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'corretagem não informado ou inválido.'
#                     continue
#
#                 try:
#                     vlr_liquidacao = float(str(vlr_liquidacao).replace('.', '').replace(',', '.')) if vlr_liquidacao else 0.0
#                     lista_import[indx]['VLRTXLIQUIDACAO'] = str(vlr_liquidacao)
#                 except:
#                     lista_import[indx]['SITUACAO'] = ' liquidação não informado ou inválido.'
#                     continue
#
#                 try:
#                     vlr_emolumentos = float(str(vlr_emolumentos).replace('.', '').replace(',', '.')) if vlr_emolumentos else 0.0
#                     lista_import[indx]['VLRTXEMOLUMENTOS'] = str(vlr_emolumentos)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'emolumentos não informado ou inválido.'
#                     continue
#
#                 try:
#                     vlr_iss = float(str(vlr_iss).replace('.', '').replace(',', '.')) if vlr_iss else 0.0
#                     lista_import[indx]['VLRTXISS'] = str(vlr_iss)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'iss não informado ou inválido.'
#                     continue
#
#                 try:
#                     vlr_irpf = float(str(vlr_irpf).replace('.', '').replace(',', '.')) if vlr_irpf else 0.0
#                     lista_import[indx]['VLRTXIRRF'] = str(vlr_irpf)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'irpf não informado ou inválido.'
#                     continue
#
#                 try:
#                     vlr_outras = float(str(vlr_outras).replace('.', '').replace(',', '.')) if vlr_outras else 0.0
#                     lista_import[indx]['VLRTXOUTRAS'] = str(vlr_outras)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'vlr. outros não informado ou inválido.'
#                     continue
#
#                 if str(tipo) != "A" and str(tipo) != "C" and str(tipo) != "V" and str(tipo) != "B" and str(tipo) != "D" and str(tipo) != "G":
#                     lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                     continue
#
#                 if (str(tipo) == "A" or str(tipo) == "C" or str(tipo) == "V" or str(tipo) == "B") and vlr_preco <= 0.0:
#                     lista_import[indx]['SITUACAO'] = 'Preço não informada.'
#                     continue
#
#                 tipo_invest = ''
#                 id_ativo = None
#
#                 if not tipo_invest:
#                     row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#                     if row:
#                         tipo_invest = 'ACAO'
#                         id_ativo = int(row.id)
#
#                 if not tipo_invest:
#                     row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#                     if row:
#                         tipo_invest = 'FII'
#                         id_ativo = int(row.id)
#
#                 if not tipo_invest:
#                     row = ETFIndice.get_by_codigo(codigo=str(codigo))
#                     if row:
#                         tipo_invest = 'ETF'
#                         id_ativo = int(row.id)
#
#                 if not tipo_invest:
#                     row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#                     if row:
#                         tipo_invest = 'BDR'
#                         id_ativo = int(row.id)
#
#                 if not tipo_invest:
#                     row = CriptoEmpresa.get_by_codigo(codigo=str(codigo))
#                     if row:
#                         tipo_invest = 'CRIPTO'
#                         id_ativo = int(row.id)
#
#                 if not tipo_invest or not id_ativo:
#                     lista_import[indx]['SITUACAO'] = 'Código não localizado.'
#                     continue
#
#                 lista_import[indx]['TIPO_INVEST'] = tipo_invest
#
#                 if nome_corretora:
#                     corretora = UsuarioCorretora.get_by_nome(id_usuario=id_usuario, nome=nome_corretora)
#                     if corretora: id_corretora = corretora.id
#
#                 # if str(tipo) == 'V':
#                 #     if str(tipo_invest) == 'ACAO':
#                 #         qtd_tot_compra = int(UsuarioEmpresaLancamento.buscar_total_compra(id_usuario=id_usuario, id_ativo=int(id_ativo)))
#                 #         qtd_tot_venda = int(UsuarioEmpresaLancamento.buscar_total_venda(id_usuario=id_usuario, id_ativo=int(id_ativo)))
#                 #         qtd_tot_venda = qtd_tot_venda + int(quant)
#                 #         if int(qtd_tot_venda) > int(qtd_tot_compra):
#                 #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(qtd_tot_compra) + ').'
#                 #             continue
#                 #     elif str(tipo_invest) == 'FII':
#                 #         qtd_tot_compra = int(UsuarioFiiFundoImobLancamento.buscar_total_compra(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#                 #         qtd_tot_bonus = int(UsuarioFiiFundoImobLancamento.buscar_total_bonus(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#                 #         qtd_tot_venda = int(UsuarioFiiFundoImobLancamento.buscar_total_venda(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#                 #         qtd_tot_venda = qtd_tot_venda + int(quant)
#                 #         if int(qtd_tot_venda) > (int(qtd_tot_compra)+int(qtd_tot_bonus)):
#                 #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(int(qtd_tot_compra)+int(qtd_tot_bonus)) + ').'
#                 #             continue
#                 #     elif str(tipo_invest) == 'ETF':
#                 #         qtd_tot_compra = int(UsuarioETFIndiceLancamento.buscar_total_compra(id_usuario=id_usuario, id_indice=int(id_ativo)))
#                 #         qtd_tot_venda = int(UsuarioETFIndiceLancamento.buscar_total_venda(id_usuario=id_usuario, id_indice=int(id_ativo)))
#                 #         qtd_tot_venda = qtd_tot_venda + int(quant)
#                 #         if int(qtd_tot_venda) > int(qtd_tot_compra):
#                 #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(qtd_tot_compra) + ').'
#                 #             continue
#                 #     elif str(tipo_invest) == 'BDR':
#                 #         qtd_tot_compra = int(UsuarioBDREmpresaLancamento.buscar_total_compra(id_usuario=id_usuario, id_bdr=int(id_ativo)))
#                 #         qtd_tot_venda = int(UsuarioBDREmpresaLancamento.buscar_total_venda(id_usuario=id_usuario, id_bdr=int(id_ativo)))
#                 #         qtd_tot_venda = qtd_tot_venda + int(quant)
#                 #         if int(qtd_tot_venda) > int(qtd_tot_compra):
#                 #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(qtd_tot_compra) + ').'
#                 #             continue
#
#                 if str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'ETF' or str(tipo_invest) == 'BDR':
#                     if str(tipo) == 'A':
#                         lista_import[indx]['SITUACAO'] = 'Tipo inválido para o Ativo.'
#                         continue
#
#                 lanc = None
#
#                 if str(tipo_invest) == 'ACAO':
#                     lanc = UsuarioACAOEmpresaLancamento(id_ativo=int(id_ativo), id_usuario=id_usuario)
#                     lanc.quant_pend = float(quant)
#
#                 elif str(tipo_invest) == 'FII':
#                     lanc = UsuarioFiiFundoImobLancamento(id_fundo=int(id_ativo), id_usuario=id_usuario)
#                     lanc.quant_orig = float(quant)
#
#                 elif str(tipo_invest) == 'ETF':
#                     lanc = UsuarioETFIndiceLancamento(id_indice=int(id_ativo), id_usuario=id_usuario)
#                     lanc.quant_pend = float(quant)
#
#                 elif str(tipo_invest) == 'BDR':
#                     lanc = UsuarioBDREmpresaLancamento(id_bdr=int(id_ativo), id_usuario=id_usuario)
#                     lanc.quant_pend = float(quant)
#
#                 elif str(tipo_invest) == 'CRIPTO':
#                     lanc = UsuarioCriptoLancamento(id_cripto=int(id_ativo), id_usuario=id_usuario)
#                     lanc.quant_orig = float(quant)
#
#                 lanc.id_corretora = int(id_corretora) if id_corretora else None
#                 lanc.tipo = str(tipo)
#                 lanc.data = str(dt_lanc)
#                 lanc.quant = float(quant)
#                 lanc.vlr_preco = float(vlr_preco) if str(tipo) == 'A' or str(tipo) == 'C' or str(tipo) == 'B' or str(tipo) == 'V' else 0.0
#                 lanc.vlr_corretagem = 0.0
#                 lanc.vlr_liquidacao = 0.0
#                 lanc.vlr_emolumentos = 0.0
#                 lanc.vlr_iss = 0.0
#                 lanc.vlr_irpf = 0.0
#                 lanc.vlr_outras = 0.0
#
#                 if str(tipo) == 'C' or str(tipo) == 'V':
#                     lanc.vlr_corretagem = float(vlr_corretagem)
#                     lanc.vlr_liquidacao = float(vlr_liquidacao)
#                     lanc.vlr_emolumentos = float(vlr_emolumentos)
#                     lanc.vlr_iss = float(vlr_iss)
#                     lanc.vlr_irpf = float(vlr_irpf)
#                     lanc.vlr_outras = float(vlr_outras)
#
#                 if str(tipo_invest) == 'FII' or str(tipo_invest) == 'CRIPTO':
#                     lanc.vlr_preco_medio = 0.0
#                     lanc.tot_vlr_valorizacao = 0.0
#                     lanc.perc_valorizacao = 0.0
#
#                 lanc.calc_tot_preco()
#                 lanc.calc_tot_taxa()
#                 lanc.calc_total()
#                 lanc.calc_custo()
#                 lanc.situacao = 'A' if (str(tipo) == 'D' or str(tipo) == 'G') and not vlr_preco else 'P'  # A-Ativo # P-PendenteDefinicaoSituacao
#
#                 try:
#                     lanc.salvar()
#                     lista_import[indx]['ID'] = str(lanc.id)
#                     lista_import[indx]['TIPO'] = lanc.tipo_descr()
#                     lista_import[indx]['SITUACAO'] = 'Importado'
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Falha ao inserir.'
#                     continue
#
#                 try:
#
#                     if str(tipo_invest) == 'ACAO':
#                         UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                         UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                         UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Excluir Todas as Operações do Ativo
#
#                     elif str(tipo_invest) == 'FII':
#                         UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                         UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#
#                     elif str(tipo_invest) == 'ETF':
#                         UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                         UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                         UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Excluir Todas as Operações do Ativo
#
#                     elif str(tipo_invest) == 'BDR':
#                         UsuarioCarteiraBdr.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                         UsuarioBDREmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                         UsuarioBDREmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Excluir Todas as Operações do Ativo
#
#                     elif str(tipo_invest) == 'CRIPTO':
#                         UsuarioCarteiraCripto.resetar_ativos(id_usuario=id_usuario, id_cripto=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                         UsuarioCriptoLancamento.resetar_ativos(id_usuario=id_usuario, id_cripto=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Falha ao Resetar Ativos.'
#                     continue
#
#         if not lista_import:
#             return make_response(get_json_retorno_grid(msg='Nenhum Operação Importada.'), 200)
#
#         UsuarioApuracaoCalculada.excluir_tudo(id_usuario=id_usuario)
#
#         lista = [
#             [
#                 str(row['DATA']),
#                 str(row['TIPO']),
#                 str(row['CODIGO']),
#                 decimal_cripto_to_str(valor=float(row['QUANT'])) if str(row['TIPO_INVEST']) == 'CRIPTO' else decimal_to_str(valor=float(row['QUANT'])).replace(',00', ''),
#                 decimal_cripto_to_str(valor=float(row['VLRPRECO'])) if str(row['TIPO_INVEST']) == 'CRIPTO' else decimal_to_str(valor=float(row['VLRPRECO'])),
#                 decimal_to_str(valor=float(row['VLRTXCORRETAGEM'])),
#                 decimal_to_str(valor=float(row['VLRTXLIQUIDACAO'])),
#                 decimal_to_str(valor=float(row['VLRTXEMOLUMENTOS'])),
#                 decimal_to_str(valor=float(row['VLRTXISS'])),
#                 decimal_to_str(valor=float(row['VLRTXIRRF'])),
#                 decimal_to_str(valor=float(row['VLRTXOUTRAS'])),
#                 str(row['SITUACAO']),
#                 str(row['ID']),
#                 str(row['INDEX']),
#                 str(row['TIPO_INVEST'])
#             ] for row in lista_import
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', msg='Arquivo CSV importado com sucesso!', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/importarcei', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def importar_cei():
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
#             dados_cei = data.get('DadosCEI')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not dados_cei:
#             return make_response(get_json_retorno_grid(msg='Dados da CEI não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         lista_import = []
#
#         # import re
#         # rows = re.split(r'/$\R?^/m', dados_cei)
#         rows = str(dados_cei).splitlines()
#
#         # from __future__ import division
#
#         indx = -1
#         for linha in rows:
#             if not linha: continue
#
#             # import re
#             # r = re.split(r'\t+', str(linha))
#             # r = re.split(r'\t+', str(linha).rstrip('\t'))
#             # r = re.compile("[^\t]+")
#             # r = re.compile(r'([^\t]*)\t*')
#             # ista_campos = r.findall(str(linha))[:-1]
#
#             row = str(linha).split('\t')
#             if not row: continue
#
#             dt_lanc = str(row[0]).strip() if row[0] else ''
#             tipo = str(row[1]).strip()[0:1] if row[1] else ''
#             codigo = str(row[4]).strip().upper() if row[4] else ''
#             quant = str(row[6]).strip().replace('.','') if row[6] else ''
#             vlr_preco = str(row[7]).strip() if row[7] else ''
#             vlr_corretagem = 0.0
#             vlr_liquidacao = 0.0
#             vlr_emolumentos = 0.0
#             vlr_iss = 0.0
#             vlr_irpf = 0.0
#             vlr_outras = 0.0
#
#             if not dt_lanc or not tipo or not codigo or not quantidade: continue
#             if str(dt_lanc)[0:1] == 'D': continue
#
#             dt_lanc = str(dt_lanc).replace('/', '').replace('-', '').ljust(8,'0')
#             dt_lanc = dt_lanc[4:8] + dt_lanc[2:4] + dt_lanc[0:2]
#             # if str(tipo) == 'A': tipo = 'G'
#
#             indx += 1
#             lista_import.append({'INDEX': str(int(indx)+1), 'ID': '', 'DATA': str(dt_lanc), 'TIPO': str(tipo), 'CODIGO': str(codigo), 'QUANT': str(quant), 'VLRPRECO': str(vlr_preco), 'VLRTXCORRETAGEM': str(vlr_corretagem), 'VLRTXLIQUIDACAO': str(vlr_liquidacao), 'VLRTXEMOLUMENTOS': str(vlr_emolumentos), 'VLRTXISS': str(vlr_iss), 'VLRTXIRRF': str(vlr_irpf), 'VLRTXOUTRAS': str(vlr_outras), 'SITUACAO': 'Não Importado'})
#
#             if not vlr_preco or str(vlr_preco) == '' or str(vlr_preco) == ',' or str(vlr_preco) == ',0' or str(vlr_preco) == ',00' or str(vlr_preco) == '0,00':
#                 vlr_preco = '0,00'
#
#             try:
#                 quant = int(float(str(quant).replace('.', '').replace(',', '.'))) if quant else 0
#                 lista_import[indx]['QUANT'] = str(quant)
#             except:
#                 lista_import[indx]['SITUACAO'] = 'Quantidade não informado ou inválido.'
#                 continue
#
#             try:
#                 vlr_preco = float(str(vlr_preco).replace('.', '').replace(',', '.')) if vlr_preco else 0.0
#                 lista_import[indx]['VLRPRECO'] = str(vlr_preco)
#             except:
#                 lista_import[indx]['SITUACAO'] = 'Preço não informado ou inválido.'
#                 continue
#
#             if str(tipo) != "A" and str(tipo) != "C" and str(tipo) != "V" and str(tipo) != "B" and str(tipo) != "D" and str(tipo) != "G":
#                 lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                 continue
#
#             if (str(tipo) == "A" or str(tipo) == "C" or str(tipo) == "V" or str(tipo) == "B") and vlr_preco <= 0.0:
#                 lista_import[indx]['SITUACAO'] = 'Preço não informada.'
#                 continue
#
#             tipo_invest = ''
#             id_ativo = None
#
#             if not tipo_invest:
#                 row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     tipo_invest = 'ACAO'
#                     id_ativo = int(row.id)
#
#             if not tipo_invest:
#                 row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     tipo_invest = 'FII'
#                     id_ativo = int(row.id)
#
#             if not tipo_invest:
#                 row = ETFIndice.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     tipo_invest = 'ETF'
#                     id_ativo = int(row.id)
#
#             if not tipo_invest:
#                 row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     tipo_invest = 'BDR'
#                     id_ativo = int(row.id)
#
#             if not tipo_invest or not id_ativo:
#                 lista_import[indx]['SITUACAO'] = 'Código não localizado.'
#                 continue
#
#             # if str(tipo) == 'V':
#             #     if str(tipo_invest) == 'ACAO':
#             #         qtd_tot_compra = int(UsuarioEmpresaLancamento.buscar_total_compra(id_usuario=id_usuario, id_ativo=int(id_ativo)))
#             #         qtd_tot_venda = int(UsuarioEmpresaLancamento.buscar_total_venda(id_usuario=id_usuario, id_ativo=int(id_ativo)))
#             #         qtd_tot_venda = qtd_tot_venda + int(quant)
#             #         if int(qtd_tot_venda) > int(qtd_tot_compra):
#             #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(qtd_tot_compra) + ').'
#             #             continue
#             #     elif str(tipo_invest) == 'FII':
#             #         qtd_tot_compra = int(UsuarioFiiFundoImobLancamento.buscar_total_compra(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#             #         qtd_tot_bonus = int(UsuarioFiiFundoImobLancamento.buscar_total_bonus(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#             #         qtd_tot_venda = int(UsuarioFiiFundoImobLancamento.buscar_total_venda(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#             #         qtd_tot_venda = qtd_tot_venda + int(quant)
#             #         if int(qtd_tot_venda) > (int(qtd_tot_compra)+int(qtd_tot_bonus)):
#             #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(int(qtd_tot_compra)+int(qtd_tot_bonus)) + ').'
#             #             continue
#             #     elif str(tipo_invest) == 'ETF':
#             #         qtd_tot_compra = int(UsuarioETFIndiceLancamento.buscar_total_compra(id_usuario=id_usuario, id_indice=int(id_ativo)))
#             #         qtd_tot_venda = int(UsuarioETFIndiceLancamento.buscar_total_venda(id_usuario=id_usuario, id_indice=int(id_ativo)))
#             #         qtd_tot_venda = qtd_tot_venda + int(quant)
#             #         if int(qtd_tot_venda) > int(qtd_tot_compra):
#             #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(qtd_tot_compra) + ').'
#             #             continue
#             #     elif str(tipo_invest) == 'BDR':
#             #         qtd_tot_compra = int(UsuarioBDREmpresaLancamento.buscar_total_compra(id_usuario=id_usuario, id_bdr=int(id_ativo)))
#             #         qtd_tot_venda = int(UsuarioBDREmpresaLancamento.buscar_total_venda(id_usuario=id_usuario, id_bdr=int(id_ativo)))
#             #         qtd_tot_venda = qtd_tot_venda + int(quant)
#             #         if int(qtd_tot_venda) > int(qtd_tot_compra):
#             #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(qtd_tot_compra) + ').'
#             #             continue
#
#             if str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'ETF':
#                 if str(tipo) == 'A':
#                     lista_import[indx]['SITUACAO'] = 'Tipo inválido para o Ativo.'
#                     continue
#
#             lanc = None
#
#             if str(tipo_invest) == 'ACAO':
#                 lanc = UsuarioACAOEmpresaLancamento(id_ativo=int(id_ativo), id_usuario=id_usuario)
#                 lanc.quant_pend = int(quant)
#
#             elif str(tipo_invest) == 'FII':
#                 lanc = UsuarioFiiFundoImobLancamento(id_fundo=int(id_ativo), id_usuario=id_usuario)
#                 lanc.quant_orig = int(quant)
#
#             elif str(tipo_invest) == 'ETF':
#                 lanc = UsuarioETFIndiceLancamento(id_indice=int(id_ativo), id_usuario=id_usuario)
#                 lanc.quant_pend = int(quant)
#
#             elif str(tipo_invest) == 'BDR':
#                 lanc = UsuarioBDREmpresaLancamento(id_bdr=int(id_ativo), id_usuario=id_usuario)
#                 lanc.quant_pend = int(quant)
#
#             lanc.tipo = str(tipo)
#             lanc.data = str(dt_lanc)
#             lanc.quant = int(quant)
#             lanc.vlr_preco = float(vlr_preco) if str(tipo) == 'A' or str(tipo) == 'C' or str(tipo) == 'B' or str(tipo) == 'V' else 0.0
#             lanc.vlr_corretagem = 0.0
#             lanc.vlr_liquidacao = 0.0
#             lanc.vlr_emolumentos = 0.0
#             lanc.vlr_iss = 0.0
#             lanc.vlr_irpf = 0.0
#             lanc.vlr_outras = 0.0
#
#             if str(tipo_invest) == 'FII':
#                 lanc.vlr_preco_medio = 0.0
#                 lanc.tot_vlr_valorizacao = 0.0
#                 lanc.perc_valorizacao = 0.0
#
#             lanc.calc_tot_preco()
#             lanc.calc_tot_taxa()
#             lanc.calc_total()
#             lanc.calc_custo()
#             lanc.situacao = 'A' if (str(tipo) == 'D' or str(tipo) == 'G') and not vlr_preco else 'P'  # A-Ativo # P-PendenteDefinicaoSituacao
#
#             try:
#                 lanc.salvar()
#                 lista_import[indx]['ID'] = str(lanc.id)
#                 lista_import[indx]['TIPO'] = lanc.tipo_descr()
#                 lista_import[indx]['SITUACAO'] = 'Importado'
#             except:
#                 lista_import[indx]['SITUACAO'] = 'Falha ao inserir.'
#                 continue
#
#             try:
#
#                 if str(tipo_invest) == 'ACAO':
#                     UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                     UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                     UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Excluir Todas as Operações do Ativo
#
#                 elif str(tipo_invest) == 'FII':
#                     UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                     UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#
#                 elif str(tipo_invest) == 'ETF':
#                     UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                     UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                     UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Excluir Todas as Operações do Ativo
#
#                 elif str(tipo_invest) == 'ETF':
#                     UsuarioCarteiraBdr.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                     UsuarioBDREmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                     UsuarioBDREmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Excluir Todas as Operações do Ativo
#
#             except:
#                 lista_import[indx]['SITUACAO'] = 'Falha ao Resetar Ativos.'
#                 continue
#
#         if not lista_import:
#             return make_response(get_json_retorno_grid(msg='Nenhum Operação Importada.'), 200)
#
#         UsuarioApuracaoCalculada.excluir_tudo(id_usuario=id_usuario)
#
#         lista = [[str(row['DATA']), str(row['TIPO']), str(row['CODIGO']), str(row['QUANT']).replace('.',''), decimal_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['VLRTXCORRETAGEM'])), decimal_to_str(valor=float(row['VLRTXLIQUIDACAO'])), decimal_to_str(valor=float(row['VLRTXEMOLUMENTOS'])), decimal_to_str(valor=float(row['VLRTXISS'])), decimal_to_str(valor=float(row['VLRTXIRRF'])), decimal_to_str(valor=float(row['VLRTXOUTRAS'])), str(row['SITUACAO']), str(row['ID']), str(row['INDEX'])] for row in lista_import]
#
#         return make_response(get_json_retorno_grid(rslt='OK', msg='Dados do CEI importado com sucesso!', lista=lista),200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# def remover_decimal(valor: float = 0.0) -> float:
#     valor = str(valor) + '00'
#     valor = valor[0:valor.find('.')+3] if valor.find('.') >= 0 else valor
#     valor = float(valor)
#     return valor
#
#
# def converter_valor(valor: str = '') -> float:
#     try:
#         valor = valor.encode('ascii', 'ignore').decode("utf-8").replace('D', '').replace('C', '').replace('R$', '').strip()
#         if valor.find(',') >= 0: valor = valor.replace('.', '').replace(',', '.').strip()
#         valor = float(valor.strip())
#         valor = float("%0.2f" % valor)
#         return valor
#     except Exception as e:
#       print('ERRO', valor, e)
#       return 0
#
#
# def get_lista_oper_nota_modalmais(texto: str = ''):
#     try:
#
#         data = {}
#         etapa = '01-PEGAR-NRO-PAGINA'
#         nro = 0
#
#         for index, linha in enumerate(texto.splitlines()):
#
#             linha = linha.strip()
#             if linha == '':
#                 continue
#
#             if etapa == '01-PEGAR-NRO-PAGINA' and 'Nr. Nota' in linha:
#                 oper_data = ''
#                 etapa = '02-PEGAR-DATA'
#
#             elif etapa == '02-PEGAR-DATA':
#                 oper_data = linha[-10:].strip()
#                 data[oper_data] = {'VLR_LIQ_OPER': 0.0, 'VLR_TX_LIQ': 0.0, 'VLR_TX_EMOL': 0.0, 'VLR_TX_CORRET': 0.0, 'VLR_TX_ISS': 0.0, 'VLR_TX_IRRF': 0.0, 'VLR_TX_OUTRAS': 0.0, 'VLR_TOTAL': 0.0, 'OPERACOES': []}
#                 etapa = '03-PEGAR-DESCRICAO-VALOR'
#
#             elif etapa == '03-PEGAR-DESCRICAO-VALOR' and linha == 'Valor':
#                 etapa = '04-PEGAR-VALOR-PAGINA'
#
#             elif etapa == '04-PEGAR-VALOR-PAGINA':
#                 # page_vlr = float(linha.replace('.', '').replace(',', '.').strip())
#                 etapa = '05-PEGAR-DESCRICAO-OPERACOES'
#
#             elif etapa == '05-PEGAR-DESCRICAO-OPERACOES' and 'D/C' in linha:
#                 etapa = '06-PEGAR-OPERACOES'
#
#             elif etapa == '06-PEGAR-OPERACOES' and 'Resumo Financeiro' in linha:
#                 etapa = '07-PEGAR-VALOR-OPERACAO'
#
#             elif etapa == '06-PEGAR-OPERACOES':
#                 nro += 1
#                 operacao = linha.replace(' - ', '-').strip().split()
#                 oper_tipo = operacao[2].upper()
#                 oper_codigo = operacao[4].strip().upper()
#                 oper_codigo = oper_codigo[:oper_codigo.find('-')].replace(',', '.').strip() if oper_codigo.find('-') >= 0 else oper_codigo.replace(',', '.').strip()
#                 oper_quant = float(operacao[-4].replace('.', '').replace(',', '.').strip())
#                 oper_preco = float(operacao[-3].replace('.', '').replace(',', '.').strip())
#                 oper_total_preco = float(operacao[-2].replace('.', '').replace(',', '.').strip())
#                 data[oper_data]['OPERACOES'] += [{'TIPO': oper_tipo, 'CODIGO': oper_codigo, 'QUANT': oper_quant, 'PRECO': oper_preco,'TOTAL_PRECO': oper_total_preco}]
#                 etapa = '06-PEGAR-OPERACOES'
#                 # print(f'#{str(nro)}', oper_data, 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#
#             elif etapa == '07-PEGAR-VALOR-OPERACAO' and 'Operações' in linha:  # 'Valor Líquido das Operações'
#                 data[oper_data]['VLR_LIQ_OPER'] = converter_valor(valor=linha.replace('Valor', '').replace('Líquido', '').replace('das', '').replace('Operações','').strip())
#                 etapa = '08-PEGAR-VALOR-LIQUIDACAO'
#
#             elif etapa == '08-PEGAR-VALOR-LIQUIDACAO' and 'Liquidação' in linha:  # 'Taxa de Liquidação'
#                 data[oper_data]['VLR_TX_LIQ'] = converter_valor(valor=linha.replace('Taxa', '').replace('de', '').replace('Liquidação', '').strip())
#                 etapa = '09-PEGAR-VALOR-EMOLUMENTOS'
#
#             elif etapa == '09-PEGAR-VALOR-EMOLUMENTOS' and 'Emolumentos' in linha:
#                 data[oper_data]['VLR_TX_EMOL'] = converter_valor(valor=linha.replace('Emolumentos', '').strip())
#                 etapa = '10-PEGAR-VALOR-CORRETAGEM'
#
#             elif etapa == '10-PEGAR-VALOR-CORRETAGEM' and 'Corretagem' in linha and 'Despesas' not in linha:
#                 data[oper_data]['VLR_TX_CORRET'] = converter_valor(valor=linha.replace('Corretagem', '').strip())
#                 etapa = '11-PEGAR-VALOR-ISS'
#
#             elif etapa == '11-PEGAR-VALOR-ISS' and 'ISS' in linha:
#                 data[oper_data]['VLR_TX_ISS'] = converter_valor(valor=linha.replace('ISS', '').replace('(', '').replace('SÃO', '').replace('PAULO', '').replace(')','').replace('*', '').strip())
#                 etapa = '12-PEGAR-VALOR-IRRF'
#
#             elif etapa == '12-PEGAR-VALOR-IRRF' and 'I.R.R.F' in linha:
#                 data[oper_data]['VLR_TX_IRRF'] = converter_valor(valor=linha.replace('I.R.R.F', '').replace('s/', '').replace('operações,', '').replace('base','').replace('0,00', '').strip())
#                 etapa = '13-PEGAR-VALOR-OUTRAS'
#
#             elif etapa == '13-PEGAR-VALOR-OUTRAS' and 'Despesas/Outras' in linha:
#                 data[oper_data]['VLR_TX_OUTRAS'] = converter_valor(valor=linha.replace('Despesas', '').replace('/', '').replace('Outras', '').strip())
#                 etapa = '14-PEGAR-VALOR-TOTAL'
#
#             elif etapa == '14-PEGAR-VALOR-TOTAL' and 'Líquido' in linha:
#                 data[oper_data]['VLR_TOTAL'] = converter_valor(valor=linha[linha.find('/') + 8:].strip())
#                 etapa = '01-PEGAR-NRO-PAGINA'
#
#         return data
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         raise
#
#
# def get_lista_oper_nota_clear(texto: str = ''):
#     try:
#
#         data = {}
#         etapa = '01-PEGAR-DESCRICAO-OPERACOES'
#         nro = 0
#
#         for index, linha in enumerate(texto.splitlines()):
#
#             linha = linha.strip()
#             if linha == '':
#                 continue
#
#             #print(linha)
#
#             if etapa == '01-PEGAR-DESCRICAO-OPERACOES' and 'D/C' in linha:
#                 oper_data = ''
#                 oper_itens =  []
#                 etapa = '02-PEGAR-OPERACOES'
#
#             elif etapa ==  '02-PEGAR-OPERACOES' and ('NOTA' in linha or 'nota' in linha):
#                 etapa = '03-PEGAR-DESCRICAO-DATA'
#
#             elif etapa ==  '02-PEGAR-OPERACOES':
#                 nro += 1
#                 operacao = linha.replace(' - ', '-').strip().split()
#                 oper_tipo = operacao[1].upper()
#                 oper_codigo = operacao[3].strip().upper()
#                 oper_codigo = oper_codigo[:oper_codigo.find('-')].replace(',', '.').strip() if oper_codigo.find('-') >= 0 else oper_codigo.replace(',', '.').strip()
#                 oper_quant = float(operacao[-4].replace('.', '').replace(',', '.').strip())
#                 oper_preco = float(operacao[-3].replace('.', '').replace(',', '.').strip())
#                 oper_total_preco = float(operacao[-2].replace('.', '').replace(',', '.').strip())
#                 oper_itens += [{'TIPO': oper_tipo, 'CODIGO': oper_codigo, 'QUANT': oper_quant, 'PRECO': oper_preco, 'TOTAL_PRECO': oper_total_preco}]
#                 etapa = '02-PEGAR-OPERACOES'
#                 #print(f'#{str(nro)}',  'Tp:', oper_tipo, 'Cod:', oper_codigo, 'Qtd:', oper_quant,  'Prç:', oper_preco,  'Tot:', oper_total_preco,  '****', operacao)
#
#             elif etapa ==  '03-PEGAR-DESCRICAO-DATA' and 'pregão' in linha:
#                 etapa = '04-PEGAR-DATA'
#
#             elif etapa ==  '04-PEGAR-DATA':
#                 oper_data = linha[-10:].strip()
#                 data[oper_data] = { 'VLR_LIQ_OPER': 0.0, 'VLR_TX_LIQ': 0.0, 'VLR_TX_EMOL': 0.0, 'VLR_TX_CORRET': 0.0, 'VLR_TX_ISS': 0.0, 'VLR_TX_IRRF': 0.0, 'VLR_TX_OUTRAS': 0.0, 'VLR_TOTAL': 0.0, 'OPERACOES': oper_itens }
#                 oper_itens =  []
#                 etapa = '05-PEGAR-VALOR-OPERACAO'
#
#             elif etapa == '05-PEGAR-VALOR-OPERACAO' and 'operações' in linha and 'líquido' in linha:  # 'Valor líquido das operações'
#                 data[oper_data]['VLR_LIQ_OPER'] = converter_valor(valor=linha.replace('Valor', '').replace('líquido', '').replace('das', '').replace('operações', '').strip())
#                 etapa = '06-PEGAR-VALOR-LIQUIDACAO'
#
#             elif etapa == '06-PEGAR-VALOR-LIQUIDACAO' and 'liquidação' in linha:  # 'Taxa deliquidação'
#                 data[oper_data]['VLR_TX_LIQ'] = converter_valor(valor=linha.replace('Taxa', '').replace('de', '').replace('liquidação', '').replace('deliquidação', '').strip())
#                 etapa = '07-PEGAR-VALOR-EMOLUMENTOS'
#
#             elif etapa == '07-PEGAR-VALOR-EMOLUMENTOS' and 'Emolumentos' in linha:
#                 data[oper_data]['VLR_TX_EMOL'] = converter_valor(valor=linha.replace('Emolumentos', '').strip())
#                 etapa = '08-PEGAR-VALOR-CORRETAGEM'
#
#             elif etapa == '08-PEGAR-VALOR-CORRETAGEM' and 'Despesas' in linha:
#                 data[oper_data]['VLR_TX_CORRET'] = 0.0  # converter_valor(valor=linha.replace('Total', '').replace('Custos', '').replace('/', '').replace('Despesas', '').strip())
#                 etapa = '09-PEGAR-VALOR-ISS'
#
#             elif etapa == '09-PEGAR-VALOR-ISS':
#                 data[oper_data]['VLR_TX_ISS'] = 0.0  # converter_valor(valor=linha.replace('ISS', '').replace('(', '').replace('SÃO', '').replace('PAULO', '').replace(')', '').replace('*', '').strip())
#                 etapa = '10-PEGAR-VALOR-IRRF'
#
#             elif etapa == '10-PEGAR-VALOR-IRRF' and 'I.R.R.F' in linha:
#                 data[oper_data]['VLR_TX_IRRF'] = converter_valor(valor=linha.replace('I.R.R.F', '').replace('s/', '').replace('operações,', '').replace('base', '').replace('0,00.', '').replace('R$', '').strip())
#                 etapa = '11-PEGAR-VALOR-OUTRAS'
#
#             elif etapa == '11-PEGAR-VALOR-OUTRAS' and 'Outros' in linha:
#                 data[oper_data]['VLR_TX_OUTRAS'] = converter_valor(valor=linha.replace('Outros', '').strip())
#                 etapa = '12-PEGAR-VALOR-TOTAL'
#
#             elif etapa == '12-PEGAR-VALOR-TOTAL' and 'Líquido' in linha:
#                 data[oper_data]['VLR_TOTAL'] =  converter_valor(valor=linha[:linha.find('/')-2].replace('Líquido ', '').replace('para', '').strip())
#                 etapa = '01-PEGAR-DESCRICAO-OPERACOES'
#
#         return data
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         raise
#
#
# def get_lista_oper_nota_rico(texto: str = ''):
#     try:
#
#         data = {}
#         etapa = '01-PEGAR-DESCRICAO-OPERACOES'
#         nro = 0
#
#         for index, linha in enumerate(texto.splitlines()):
#
#             linha = linha.strip()
#             if linha == '':
#                 continue
#
#             # print(linha)
#
#             if etapa == '01-PEGAR-DESCRICAO-OPERACOES' and 'D/C' in linha:
#                 oper_data = ''
#                 oper_itens =  []
#                 etapa = '02-PEGAR-OPERACOES'
#
#             elif etapa ==  '02-PEGAR-OPERACOES' and ('NOTA' in linha or 'nota' in linha):
#                 etapa = '03-PEGAR-DESCRICAO-DATA'
#
#             elif etapa ==  '02-PEGAR-OPERACOES':
#                 nro += 1
#                 operacao = linha.replace(' - ', '-').strip().split()
#                 oper_tipo = operacao[1].upper()
#                 oper_codigo = operacao[-7].strip().upper()
#                 oper_codigo = oper_codigo[:oper_codigo.find('-')].replace(',', '.').strip() if oper_codigo.find('-') >= 0 else oper_codigo.replace(',', '.').strip()
#                 oper_quant = float(operacao[-4].replace('.', '').replace(',', '.').strip())
#                 oper_preco = float(operacao[-3].replace('.', '').replace(',', '.').strip())
#                 oper_total_preco = float(operacao[-2].replace('.', '').replace(',', '.').strip())
#                 oper_itens += [{'TIPO': oper_tipo, 'CODIGO': oper_codigo, 'QUANT': oper_quant, 'PRECO': oper_preco, 'TOTAL_PRECO': oper_total_preco}]
#                 etapa = '02-PEGAR-OPERACOES'
#                 # print(f'#{str(nro)}',  'Tp:', oper_tipo, 'Cod:', oper_codigo, 'Qtd:', oper_quant,  'Prç:', oper_preco,  'Tot:', oper_total_preco,  '***', operacao )
#
#             elif etapa ==  '03-PEGAR-DESCRICAO-DATA' and 'pregão' in linha:
#                 etapa = '04-PEGAR-DATA'
#
#             elif etapa ==  '04-PEGAR-DATA':
#                 oper_data = linha[-10:].strip()
#                 data[oper_data] = { 'VLR_LIQ_OPER': 0.0, 'VLR_TX_LIQ': 0.0, 'VLR_TX_EMOL': 0.0, 'VLR_TX_CORRET': 0.0, 'VLR_TX_ISS': 0.0, 'VLR_TX_IRRF': 0.0, 'VLR_TX_OUTRAS': 0.0, 'VLR_TOTAL': 0.0, 'OPERACOES': oper_itens }
#                 oper_itens =  []
#                 etapa = '05-PEGAR-VALOR-OPERACAO'
#
#             elif etapa == '05-PEGAR-VALOR-OPERACAO' and 'operações' in linha and 'líquido' in linha:  # 'Valor líquido das operações'
#                 data[oper_data]['VLR_LIQ_OPER'] = converter_valor(valor=linha.replace('Valor', '').replace('líquido', '').replace('das', '').replace('operações', '').strip())
#                 etapa = '06-PEGAR-VALOR-LIQUIDACAO'
#
#             elif etapa == '06-PEGAR-VALOR-LIQUIDACAO' and 'liquidação' in linha:  # 'Taxa deliquidação'
#                 data[oper_data]['VLR_TX_LIQ'] = converter_valor(valor=linha.replace('Taxa', '').replace('de', '').replace('liquidação', '').replace('deliquidação', '').strip())
#                 etapa = '07-PEGAR-VALOR-EMOLUMENTOS'
#
#             elif etapa == '07-PEGAR-VALOR-EMOLUMENTOS' and 'Emolumentos' in linha:
#                 data[oper_data]['VLR_TX_EMOL'] = converter_valor(valor=linha.replace('Emolumentos', '').strip())
#                 etapa = '08-PEGAR-VALOR-CORRETAGEM'
#
#             elif etapa == '08-PEGAR-VALOR-CORRETAGEM' and 'Operacional' in linha:
#                 data[oper_data]['VLR_TX_CORRET'] = converter_valor(valor=linha.replace('Taxa', '').replace('Operacional', '').strip())
#                 etapa = '09-PEGAR-VALOR-ISS'
#
#             elif etapa == '09-PEGAR-VALOR-ISS':
#                 data[oper_data]['VLR_TX_ISS'] = 0.0  # converter_valor(valor=linha.replace('ISS', '').replace('(', '').replace('SÃO', '').replace('PAULO', '').replace(')', '').replace('*', '').strip())
#                 etapa = '10-PEGAR-VALOR-IRRF'
#
#             elif etapa == '10-PEGAR-VALOR-IRRF' and 'I.R.R.F' in linha:
#                 data[oper_data]['VLR_TX_IRRF'] = converter_valor(valor=linha.replace('I.R.R.F', '').replace('s/', '').replace('operações,', '').replace('base', '').replace('0,00.', '').replace('R$', '').strip())
#                 etapa = '11-PEGAR-VALOR-OUTRAS'
#
#             elif etapa == '11-PEGAR-VALOR-OUTRAS' and 'Outros' in linha:
#                 data[oper_data]['VLR_TX_OUTRAS'] = converter_valor(valor=linha.replace('Outros', '').strip())
#                 etapa = '12-PEGAR-VALOR-TOTAL'
#
#             elif etapa == '12-PEGAR-VALOR-TOTAL' and 'Líquido' in linha:
#                 data[oper_data]['VLR_TOTAL'] = converter_valor(valor=linha[:linha.find('/')-2].replace('Líquido ', '').replace('para', '').strip())
#                 etapa = '01-PEGAR-DESCRICAO-OPERACOES'
#
#         return data
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         raise
#
#
# def get_lista_oper_nota_mirae(texto: str = ''):
#     try:
#
#         data = {}
#         etapa = '01-PEGAR-DATA'
#         nro = 0
#         oper_data = ""
#
#         for index, linha in enumerate(texto.splitlines()):
#
#             linha = linha.strip()
#             if linha == '':
#                 continue
#
#             if etapa == '01-PEGAR-DATA' and 'Data pregão' in linha:
#                 if linha[0:25].strip().replace('Data pregão:', '').strip() != oper_data:
#                     oper_data = linha[0:25].strip().replace('Data pregão:', '').strip()
#                     data[oper_data] = { 'VLR_LIQ_OPER': 0.0, 'VLR_TX_LIQ': 0.0, 'VLR_TX_EMOL': 0.0, 'VLR_TX_CORRET': 0.0, 'VLR_TX_ISS': 0.0, 'VLR_TX_IRRF': 0.0, 'VLR_TX_OUTRAS': 0.0, 'VLR_TOTAL': 0.0, 'OPERACOES': [] }
#                 etapa = '02-PEGAR-DESCRICAO-OPERACOES'
#
#             elif etapa ==  '02-PEGAR-DESCRICAO-OPERACOES' and 'D/C' in linha:
#                 etapa = '03-PEGAR-OPERACOES'
#
#             elif etapa ==  '03-PEGAR-OPERACOES' and ('Resumo dos Negócios' in linha or 'SubTotal' in linha):
#                 etapa = '05-PEGAR-VALOR-OPERACAO'
#
#             elif etapa ==  '03-PEGAR-OPERACOES':
#                 nro += 1
#                 operacao = linha.replace(' - ', '-').strip().split()
#                 oper_tipo = operacao[1].upper()
#                 oper_codigo = operacao[3].strip().upper()
#                 oper_codigo = oper_codigo[:oper_codigo.find('-')].replace(',', '.').strip() if oper_codigo.find('-') >= 0 else oper_codigo.replace(',', '.').strip()
#                 oper_quant = float(operacao[-4].replace('.', '').replace(',', '.').strip())
#                 oper_preco = float(operacao[-3].replace('.', '').replace(',', '.').strip())
#                 oper_total_preco = float(operacao[-2].replace('.', '').replace(',', '.').strip())
#                 data[oper_data]['OPERACOES'] += [{'TIPO': oper_tipo, 'CODIGO': oper_codigo, 'QUANT': oper_quant, 'PRECO': oper_preco, 'TOTAL_PRECO': oper_total_preco}]
#                 etapa = '03-PEGAR-OPERACOES'
#                 # print(f'#{str(nro)}',  'Tp:', oper_tipo, 'Cod:', oper_codigo, 'Qtd:', oper_quant,  'Prç:', oper_preco,  'Tot:', oper_total_preco,  '***', operacao )
#
#             elif etapa == '05-PEGAR-VALOR-OPERACAO' and 'Valor Líquido' in linha:
#                 valor = converter_valor(valor=linha.replace('Valor', '').replace('Líquido', '').replace('das', '').replace('Operações', '').replace('(1)', '').replace('D', '').strip())
#                 data[oper_data]['VLR_LIQ_OPER'] += float(valor) if float(valor) > 0.0 else float(valor) * -1
#                 etapa = '06-PEGAR-VALOR-LIQUIDACAO'
#
#             elif etapa == '06-PEGAR-VALOR-LIQUIDACAO' and 'Taxa de Liquidação' in linha:
#                 valor =  converter_valor(valor=linha.replace('Taxa', '').replace('de', '').replace('Liquidação', '').replace('(2)', '').replace('D', '').strip())
#                 data[oper_data]['VLR_TX_LIQ'] += float(valor) if float(valor) > 0.0 else float(valor) * -1
#                 etapa = '07-PEGAR-VALOR-EMOLUMENTOS'
#
#             elif etapa == '07-PEGAR-VALOR-EMOLUMENTOS' and 'Emolumentos' in linha:
#                 valor = converter_valor(valor=linha.replace('Emolumentos', '').replace('D', '').strip())
#                 data[oper_data]['VLR_TX_EMOL'] += float(valor) if float(valor) > 0.0 else float(valor) * -1
#                 etapa = '08-PEGAR-VALOR-CORRETAGEM'
#
#             elif etapa == '08-PEGAR-VALOR-CORRETAGEM' and 'Corretagem' in linha:
#                 valor = converter_valor(valor=linha.replace('Corretagem', '').replace('D', '').strip())
#                 data[oper_data]['VLR_TX_CORRET'] += float(valor) if float(valor) > 0.0 else float(valor) * -1
#                 etapa = '09-PEGAR-VALOR-ISS'
#
#             elif etapa == '09-PEGAR-VALOR-ISS':
#                 valor =  converter_valor(valor=linha.replace('ISS', '').replace('(', '').replace('SÃO', '').replace('PAULO', '').replace(')', '').replace('*', '').replace('D', '').strip())
#                 data[oper_data]['VLR_TX_ISS'] += float(valor) if float(valor) > 0.0 else float(valor) * -1
#                 etapa = '10-PEGAR-VALOR-IRRF'
#
#             elif etapa == '10-PEGAR-VALOR-IRRF' and 'I.R.R.F' in linha:
#                 valor =  converter_valor(valor=linha.replace('I.R.R.F.', '').replace('I.R.R.F', '').replace('s/', '').replace('operações,', '').replace('base 0,00', '0').replace('base', '').replace('0,00', '').replace('D', '').strip())
#                 data[oper_data]['VLR_TX_IRRF'] += float(valor) if float(valor) > 0.0 else float(valor) * -1
#                 etapa = '11-PEGAR-VALOR-OUTRAS'
#
#             elif etapa == '11-PEGAR-VALOR-OUTRAS' and 'Outras' in linha:
#                 valor = converter_valor(valor=linha.replace('Outras', '').replace('D', '').strip())
#                 data[oper_data]['VLR_TX_OUTRAS'] += float(valor) if float(valor) > 0.0 else float(valor) * -1
#                 etapa = '12-PEGAR-VALOR-TOTAL'
#
#             elif etapa == '12-PEGAR-VALOR-TOTAL' and 'Liquido' in linha:
#                 valor = converter_valor(valor=linha[linha.find('/')+8:].strip())
#                 data[oper_data]['VLR_TOTAL'] += float(valor) if float(valor) > 0.0 else float(valor) * -1
#                 etapa = '01-PEGAR-DATA'
#
#         return data
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         raise
#
#
# def get_lista_oper_nota_ajustado(data: dict = {}):
#     try:
#
#         data_orig = {}
#
#         for dt, row in data.items():
#
#             data_orig[dt] = {
#                 'VLR_LIQ_OPER': row['VLR_LIQ_OPER'],
#                 'VLR_TX_LIQ': row['VLR_TX_LIQ'],
#                 'VLR_TX_EMOL': row['VLR_TX_EMOL'],
#                 'VLR_TX_CORRET': row['VLR_TX_CORRET'],
#                 'VLR_TX_ISS': row['VLR_TX_ISS'],
#                 'VLR_TX_IRRF': row['VLR_TX_IRRF'],
#                 'VLR_TX_OUTRAS': row['VLR_TX_OUTRAS'],
#                 'VLR_TOTAL': row['VLR_TOTAL'],
#                 'OPERACOES': []
#             }
#
#             ult_tipo = ''
#             ult_codigo = ''
#             ult_quant = 0.0
#             ult_preco = 0.0
#             ult_total_preco =  0.0
#
#             oper_tipo = ''
#             oper_codigo = ''
#             oper_quant = 0.0
#             oper_preco = 0.0
#             oper_total_preco = 0.0
#
#             print()
#
#             for index, oper in enumerate(row['OPERACOES']):
#
#                 oper_tipo = oper['TIPO']
#                 oper_codigo = oper['CODIGO']
#                 oper_quant = oper['QUANT']
#                 oper_preco = oper['PRECO']
#                 oper_total_preco = oper['TOTAL_PRECO']
#                 # print(f'#{str(index)}', '00', dt, 'ULTIM', 'Tp:', ult_tipo,  'Cod:', ult_codigo, 'Qtd:', ult_quant, 'Prç:',  ult_preco, 'Tot:', ult_total_preco)
#                 # print(f'#{str(index)}', '00', dt, 'ATUAL', 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#
#                 if ult_tipo == '' and ult_codigo == '' and ult_preco == 0.0:
#                     ult_tipo = oper_tipo
#                     ult_codigo = oper_codigo
#                     ult_quant = oper_quant
#                     ult_preco = oper_preco
#                     ult_total_preco = oper_total_preco
#                     # print(f'#{str(index)}', '01', dt, 'ULTIM', 'Tp:', ult_tipo,  'Cod:', ult_codigo, 'Qtd:', ult_quant, 'Prç:',  ult_preco, 'Tot:', ult_total_preco)
#                     # print(f'#{str(index)}', '01', dt, 'ATUAL', 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#
#                 elif ult_tipo == oper_tipo and ult_codigo == oper_codigo and ult_preco == oper_preco:
#                     ult_tipo = oper_tipo
#                     # ult_codigo = oper_codigo
#                     ult_quant += oper_quant
#                     # ult_preco = oper_preco
#                     ult_total_preco += oper_total_preco
#                     # print(f'#{str(index)}', '02', dt, 'ULTIM', 'Tp:', ult_tipo,  'Cod:', ult_codigo, 'Qtd:', ult_quant, 'Prç:',  ult_preco, 'Tot:', ult_total_preco)
#                     # print(f'#{str(index)}', '02', dt, 'ATUAL', 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#
#                 # print(f'#{str(index)}', '03', ult_tipo == oper_tipo, ult_codigo == oper_codigo, ult_preco == oper_preco)
#                 if ult_tipo != oper_tipo or ult_codigo != oper_codigo or ult_preco != oper_preco:
#
#                     # print(f'#{str(index)}', '03', dt, 'ULTIM', 'Tp:', ult_tipo,  'Cod:', ult_codigo, 'Qtd:', ult_quant, 'Prç:',  ult_preco, 'Tot:', ult_total_preco)
#                     # print(f'#{str(index)}', '03', dt, 'ATUAL', 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#
#                     ult_liquid = ((ult_total_preco * 0.0275) / 100)
#                     # ult_liquid = float("%0.2f" % ult_liquid)
#                     ult_emol = ((ult_total_preco * 0.003125) / 100) # if dt >= '22/04/2020' else ((ult_total_preco * 0.00366) / 100)
#                     # ult_emol = float("%0.2f" % ult_emol)
#                     ult_corret = 0.0 # 1.49
#                     ult_iss = ((ult_corret / 100) * 9.65) # if dt >= '01/02/2020' else ((ult_corret / 100) * 5)
#                     # ult_iss = float("%0.2f" % ult_iss)
#                     ult_irrp = 0.0
#                     ult_outras = 0.00
#                     ult_total = 0.00
#                     if ult_tipo == 'C':
#                         ult_total = ult_total_preco + ult_liquid + ult_emol + ult_corret + ult_iss + ult_irrp + ult_outras
#                     elif ult_tipo == 'V':
#                         ult_irrp = ((ult_total_preco * 0.0050) / 100)
#                         # ult_irrp = float("%0.2f" % ult_irrp)
#                         if ult_irrp <= 1.0: ult_irrp = 0.0
#                         ult_total = ult_total_preco - ult_liquid - ult_emol - ult_corret - ult_iss - ult_irrp - ult_outras
#                     # ult_total = float("%0.2f" % ult_total)
#                     ult_total = remover_decimal(valor=ult_total)
#                     data_orig[dt]['OPERACOES'] += [{'TIPO': ult_tipo, 'CODIGO': ult_codigo, 'QUANT': ult_quant, 'PRECO': ult_preco, 'TOTAL_PRECO': ult_total_preco, 'VLR_TX_LIQ': ult_liquid, 'VLR_TX_EMOL': ult_emol, 'VLR_TX_CORRET': ult_corret,  'VLR_TX_ISS': ult_iss,  'VLR_TX_IRRF': ult_irrp, 'VLR_TX_OUTRAS': ult_outras, 'VLR_TOTAL': ult_total}]
#
#                     ult_tipo = oper_tipo
#                     ult_codigo = oper_codigo
#                     ult_quant = oper_quant
#                     ult_preco = oper_preco
#                     ult_total_preco = oper_total_preco
#
#                     # print(f'#{str(index)}', '04', dt, 'ULTIM', 'Tp:', ult_tipo,  'Cod:', ult_codigo, 'Qtd:', ult_quant, 'Prç:',  ult_preco, 'Tot:', ult_total_preco)
#                     # print(f'#{str(index)}', '04', dt, 'ATUAL', 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#
#             # print(f'#{str(index)}', '05', dt, 'ULTIM', 'Tp:', ult_tipo,  'Cod:', ult_codigo, 'Qtd:', ult_quant, 'Prç:',  ult_preco, 'Tot:', ult_total_preco)
#             # print(f'#{str(index)}', '05', dt, 'ATUAL', 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#
#             # if ult_tipo == oper_tipo and ult_codigo == oper_codigo and ult_preco == oper_preco:
#             #     ult_quant += oper_quant
#             #     ult_total_preco += oper_total_preco
#             #     #print('06', dt, 'ULTIM', 'Tp:', ult_tipo,  'Cod:', ult_codigo, 'Qtd:', ult_quant, 'Prç:',  ult_preco, 'Tot:', ult_total_preco)
#             #     print('06', dt, 'ATUAL', 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#
#             if ult_tipo != oper_tipo or ult_codigo != oper_codigo or ult_preco != oper_preco:
#                 ult_tipo = oper_tipo
#                 ult_codigo = oper_codigo
#                 ult_quant = oper_quant
#                 ult_preco = oper_preco
#                 ult_total_preco = oper_total_preco
#                 # print(f'#{str(index)}', '07', dt, 'ULTIM', 'Tp:', ult_tipo,  'Cod:', ult_codigo, 'Qtd:', ult_quant, 'Prç:',  ult_preco, 'Tot:', ult_total_preco)
#                 # print(f'#{str(index)}', '07', dt, 'ATUAL', 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#
#             # print(f'#{str(index)}', '08', dt, 'ULTIM', 'Tp:', ult_tipo,  'Cod:', ult_codigo, 'Qtd:', ult_quant, 'Prç:',  ult_preco, 'Tot:', ult_total_preco)
#             # print(f'#{str(index)}', '08', dt, 'ATUAL', 'Tp:', oper_tipo,  'Cod:', oper_codigo, 'Qtd:', oper_quant, 'Prç:', oper_preco, 'Tot:', oper_total_preco)
#             ult_liquid = ((ult_total_preco * 0.0275) / 100)
#             # ult_liquid = float("%0.2f" % ult_liquid)
#             ult_emol = ((ult_total_preco * 0.003125) / 100) # if dt >= '22/04/2020' else ((ult_total_preco * 0.00366) / 100)
#             # ult_emol = float("%0.2f" % ult_emol)
#             ult_corret = 0.0 # 1.49
#             ult_iss = ((ult_corret / 100) * 9.65) # if dt >= '01/02/2020' else ((ult_corret / 100) * 5)
#             # ult_iss = float("%0.2f" % ult_iss)
#             ult_irrp = 0.0
#             ult_outras = 0.00
#             ult_total = 0.00
#             if ult_tipo == 'C':
#                 ult_total = ult_total_preco + ult_liquid + ult_emol + ult_corret + ult_iss + ult_irrp + ult_outras
#             elif ult_tipo == 'V':
#                 ult_irrp = ((ult_total_preco * 0.0050) / 100)
#                 # ult_irrp = float("%0.2f" % ult_irrp)
#                 if ult_irrp <= 1.0: ult_irrp = 0.0
#                 ult_total = ult_total_preco - ult_liquid - ult_emol - ult_corret - ult_iss - ult_irrp - ult_outras
#             # ult_total = float("%0.2f" % ult_total)
#             ult_total = remover_decimal(valor=ult_total)
#             data_orig[dt]['OPERACOES'] += [{'TIPO': ult_tipo, 'CODIGO': ult_codigo, 'QUANT': ult_quant, 'PRECO': ult_preco, 'TOTAL_PRECO': ult_total_preco, 'VLR_TX_LIQ': ult_liquid, 'VLR_TX_EMOL': ult_emol, 'VLR_TX_CORRET': ult_corret,  'VLR_TX_ISS': ult_iss,  'VLR_TX_IRRF': ult_irrp, 'VLR_TX_OUTRAS': ult_outras, 'VLR_TOTAL': ult_total}]
#
#         return data_orig
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         raise
#
#
# def get_lista_oper_nota_rateio_taxas(data: dict = {}):
#     try:
#
#         for dt, row in data.items():
#
#             tot_liq_oper = float(row['VLR_LIQ_OPER']) if row['VLR_LIQ_OPER'] else 0.0
#             tot_tx_liq = float(row['VLR_TX_LIQ']) if row['VLR_TX_LIQ'] else 0.0
#             tot_tx_emol = float(row['VLR_TX_EMOL']) if row['VLR_TX_EMOL'] else 0.0
#             tot_tx_corret = float(row['VLR_TX_CORRET']) if row['VLR_TX_CORRET'] else 0.0
#             tot_tx_iss = float(row['VLR_TX_ISS']) if row['VLR_TX_ISS'] else 0.0
#             qtd_operac = float(len(row['OPERACOES'])) if row['OPERACOES'] else 0.0
#
#             tx_liq_calc = float(tot_tx_liq / tot_liq_oper) if tot_tx_liq > 0.0 and tot_liq_oper > 0.0 else 0.0
#             tx_emol_calc = float(tot_tx_emol / tot_liq_oper) if tot_tx_emol > 0.0 and tot_liq_oper > 0.0 else 0.0
#             tx_corret_calc = float(tot_tx_corret / qtd_operac) if tot_tx_corret > 0.0 and qtd_operac > 0.0 else 0.0
#             tx_iss_calc = float(tot_tx_iss / qtd_operac) if tot_tx_iss > 0.0 and qtd_operac > 0.0 else 0.0
#
#             # tx_corret_calc = remover_decimal(valor=tx_corret_calc)
#             # tx_iss_calc = remover_decimal(valor=tx_iss_calc)
#             tx_corret_calc = float("%0.2f" % tx_corret_calc)
#             tx_iss_calc = float("%0.2f" % tx_iss_calc)
#
#             for index, oper in enumerate(row['OPERACOES']):
#                 tot_preco = float(oper['TOTAL_PRECO'])
#                 tx_iss_liq = float(tot_preco) * float(tx_liq_calc) if tot_preco > 0.0 and tx_liq_calc > 0.0 else 0.0
#                 tx_iss_emol = float(tot_preco) * float(tx_emol_calc) if tot_preco > 0.0 and tx_emol_calc > 0.0 else 0.0
#                 tx_iss_irrf = float(oper['VLR_TX_IRRF'])
#                 tx_iss_outras = float(oper['VLR_TX_OUTRAS'])
#
#                 # tx_iss_liq = remover_decimal(valor=tx_iss_liq)
#                 # tx_iss_emol = remover_decimal(valor=tx_iss_emol)
#                 tx_iss_liq = float("%0.2f" % tx_iss_liq)
#                 tx_iss_emol = float("%0.2f" % tx_iss_emol)
#
#                 vlr_total = float(oper['VLR_TOTAL'])
#                 if oper['TIPO'] == 'C':  vlr_total = float(tot_preco) + float(tx_iss_liq) + float(tx_iss_emol) + float(tx_corret_calc) + float(tx_iss_calc) + float(tx_iss_irrf) + float(tx_iss_outras)
#                 if oper['TIPO'] == 'V':  vlr_total = float(tot_preco) - float(tx_iss_liq) - float(tx_iss_emol) - float(tx_corret_calc) - float(tx_iss_calc) - float(tx_iss_irrf) - float(tx_iss_outras)
#
#                 # vlr_total = remover_decimal(valor=vlr_total)
#                 vlr_total = float("%0.2f" % vlr_total)
#
#                 oper['VLR_TX_LIQ'] = float(tx_iss_liq)
#                 oper['VLR_TX_EMOL'] = float(tx_iss_emol)
#                 oper['VLR_TX_CORRET'] = float(tx_corret_calc)
#                 oper['VLR_TX_ISS'] = float(tx_iss_calc)
#                 oper['VLR_TX_IRRF'] = float(tx_iss_irrf)
#                 oper['VLR_TX_OUTRAS'] = float(tx_iss_outras)
#                 oper['VLR_TOTAL'] = float(vlr_total)
#
#         return data
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         raise
#
#
# @bp_operacoes.route('/importarnotacorretagem', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def importar_nota_corretagem():
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
#             id_corretora = data.get('corretora')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         if not id_corretora:
#             return make_response(get_json_retorno_grid(msg='Corretora não informada.'), 200)
#
#         id_usuario = current_user.id
#
#         corretora = UsuarioCorretora.get_by_usuario(id=int(id_corretora), id_usuario=id_usuario)
#         if not corretora:
#             return make_response(get_json_retorno_grid(msg='Corretora não localizada.'), 200)
#
#         corretora_lista = CorretoraLista.get_by_id(id=int(corretora.id_corretora_lista))
#         if not corretora_lista:
#             return make_response(get_json_retorno_grid(msg='Corretora não localizada.'), 200)
#
#         if str(corretora_lista.importar_nota) != 'S':
#             return make_response(get_json_retorno_dados(msg='Corretora não habilidata para importação. Entre em Contato com o Admin do Site.'), 200)
#
#         if 'arquivo' not in request.files:
#             return make_response(get_json_retorno_grid(msg='Nenhuma Arquivo informado.'), 200)
#
#         file = request.files['arquivo']
#
#         if file.filename == '':
#             return make_response(get_json_retorno_grid(msg='Nenhuma Arquivo informado.'), 200)
#
#         ext = file.filename.rsplit(".", 1)[1]
#         if ext.lower() != 'pdf' and ext.lower() != '.pdf':
#             return make_response(get_json_retorno_grid(msg="Arquivo não é uma extensão válida - " + file.filename), 200)
#
#         # array('application/vnd.ms-excel','application/vnd.msexcel','text/plain','text/csv','text/tsv', 'application/txt','application/octet-stream','text/anytext','application/csv','text/comma-separated-values','application/excel');
#         # $fileSize <= 0 # $msg = "Arquivo vazio - " . $fileName;
#         # $fileSize > 10485760 ){  // 10,485,760 # $msg = "Arquivo deve ser de no máximo 10MB - " .$fileName;
#
#         filename = 'user_'+str(id_usuario)+'_' + pegar_data_hora_atual() + '.' + ext.lower()
#         path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../' + current_app.config['PDF_NOTA_UPLOADS'])
#         file.save(os.path.join(path, filename))
#
#         import warnings
#         warnings.filterwarnings('ignore')
#
#         # try:
#         #     # os.environ['CLASSPATH'] = "/path/to/tika-app.jar"
#         #     os.environ['TIKA_SERVER_JAR'] = 'https://repo1.maven.org/maven2/org/apache/tika/tika-server/1.19/tika-server-1.19.jar'
#         # except:
#         #     pass
#
#         try:
#
#             # import textract
#             # texto = textract.process(filename=os.path.join(path, filename), method='pdfminer')
#
#             # import pdfplumber
#             # import pdfplumber.utils
#             # from pdfplumber.pdf import PDF
#             # import pdfminer
#             # import pdfminer.pdftypes
#             # texto = ""
#             # with PDF.open(os.path.join(path, filename)) as pdf:
#             #     pages = pdf.pages
#             #     for i, pg in enumerate(pages):
#             #         texto += pdf.pages[i].extract_text()
#
#             # import tika
#             # from tika import parser
#             # tika.initVM() # Start running the tika service
#             # tika.TikaClientOnly = True
#             # raw = parser.from_file(filename=os.path.join(path, filename))
#             # texto = raw['content']
#
#             def convert_pdf_to_txt(path):
#                 from io import StringIO, BytesIO
#                 #     from pdfminer.converter import TextConverter
#                 #     from pdfminer.layout import LAParams
#                 #     from pdfminer.pdfdocument import PDFDocument
#                 #     from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#                 #     from pdfminer.pdfpage import PDFPage
#                 #     from pdfminer.pdfparser import PDFParser
#                 #     rsrcmgr = PDFResourceManager()
#                 #     codec = 'utf-8'  # 'ignore' #  'ascii' # 'utf-8' # 'ISO-8859-1'
#                 #     laparams = LAParams(all_texts=True)
#                 #     with BytesIO() as retstr:  # StringIO() # BytesIO()
#                 #         with TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams) as device:
#                 #             with open(file=path, mode='rb') as fp:
#                 #                 interpreter = PDFPageInterpreter(rsrcmgr, device)
#                 #                 for page in PDFPage.get_pages(fp, set(), maxpages=0, password="", caching=True, check_extractable=True):
#                 #                     interpreter.process_page(page)
#                 #                 return retstr.getvalue()  # .decode('utf-8') #.replace(chr(272)," ")
#
#             texto = convert_pdf_to_txt(path=os.path.join(path, filename))
#
#         except Exception as e:
#             # return make_response(get_json_retorno_grid(msg='Não foi possível ler o PDF.'), 200)
#             return make_response(get_json_retorno_grid(msg=str(e)), 200)
#
#         lista_nota = {}
#
#         if int(corretora_lista.id) == 244: lista_nota = get_lista_oper_nota_modalmais(texto=str(texto))
#         if int(corretora_lista.id) == 214: lista_nota = get_lista_oper_nota_clear(texto=str(texto))
#         if int(corretora_lista.id) == 256: lista_nota = get_lista_oper_nota_rico(texto=str(texto))
#         if int(corretora_lista.id) == 243: lista_nota = get_lista_oper_nota_mirae(texto=str(texto))
#
#         if not lista_nota:
#             return make_response(get_json_retorno_grid(msg='Nenhum Operação Importada.'), 200)
#
#         lista_nota = get_lista_oper_nota_ajustado(data=lista_nota)  # fazer grupamento das operações
#
#         lista_nota = get_lista_oper_nota_rateio_taxas(data=lista_nota)  # caclular taxas das operações
#
#         lista_import = []
#         lista_import_geral = []
#         indx = -1
#
#         for dt, row in lista_nota.items():
#
#             dt_lanc = str(dt).replace('/', '').replace('-', '').ljust(8, '0')
#             dt_lanc = dt_lanc[4:8] + dt_lanc[2:4] + dt_lanc[0:2]
#
#             lista_import_geral.append([
#                 str(dt_lanc),
#                 float(row['VLR_LIQ_OPER']),
#                 float(row['VLR_TX_LIQ']),
#                 float(row['VLR_TX_EMOL']),
#                 float(row['VLR_TX_CORRET']),
#                 float(row['VLR_TX_ISS']),
#                 float(row['VLR_TX_IRRF']),
#                 float(row['VLR_TX_OUTRAS']),
#                 float(row['VLR_TOTAL']),
#             ])
#
#             for oper in row['OPERACOES']:
#
#                 tipo = str(oper['TIPO'])
#                 codigo = str(oper['CODIGO'])
#                 quant = int(oper['QUANT'])
#                 vlr_preco = float(oper['PRECO'])
#                 vlr_corretagem = float(oper['VLR_TX_CORRET'])
#                 vlr_liquidacao = float(oper['VLR_TX_LIQ'])
#                 vlr_emolumentos = float(oper['VLR_TX_EMOL'])
#                 vlr_iss = float(oper['VLR_TX_ISS'])
#                 vlr_irpf = float(oper['VLR_TX_IRRF'])
#                 vlr_outras = float(oper['VLR_TX_OUTRAS'])
#                 vlr_total = float(oper['VLR_TOTAL'])
#                 # if str(tipo) == 'A': tipo = 'G'
#
#                 indx += 1
#                 lista_import.append({'INDEX': str(int(indx)+1), 'ID': '', 'DATA': str(dt_lanc), 'TIPO': str(tipo), 'CODIGO': str(codigo), 'QUANT': str(quant), 'VLRPRECO': str(vlr_preco), 'VLRTXCORRETAGEM': str(vlr_corretagem), 'VLRTXLIQUIDACAO': str(vlr_liquidacao), 'VLRTXEMOLUMENTOS': str(vlr_emolumentos), 'VLRTXISS': str(vlr_iss), 'VLRTXIRRF': str(vlr_irpf), 'VLRTXOUTRAS': str(vlr_outras), 'SITUACAO': 'Não Importado'})
#
#                 if (str(tipo) == "A" or str(tipo) == "C" or str(tipo) == "V" or str(tipo) == "B") and vlr_preco <= 0.0:
#                     lista_import[indx]['SITUACAO'] = 'Preço não informada.'
#                     continue
#
#                 tipo_invest = ''
#                 id_ativo = None
#
#                 if not tipo_invest:
#                     obj = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#                     if obj:
#                         tipo_invest = 'ACAO'
#                         id_ativo = int(obj.id)
#
#                 if not tipo_invest:
#                     obj = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#                     if obj:
#                         tipo_invest = 'FII'
#                         id_ativo = int(obj.id)
#
#                 if not tipo_invest:
#                     obj = ETFIndice.get_by_codigo(codigo=str(codigo))
#                     if obj:
#                         tipo_invest = 'ETF'
#                         id_ativo = int(obj.id)
#
#                 if not tipo_invest:
#                     obj = BDREmpresa.get_by_codigo(codigo=str(codigo))
#                     if obj:
#                         tipo_invest = 'BDR'
#                         id_ativo = int(obj.id)
#
#                 if not tipo_invest or not id_ativo:
#                     lista_import[indx]['SITUACAO'] = 'Código não localizado.'
#                     continue
#
#                 # if str(tipo) == 'V':
#                 #     if str(tipo_invest) == 'ACAO':
#                 #         qtd_tot_compra = int(UsuarioEmpresaLancamento.buscar_total_compra(id_usuario=id_usuario, id_ativo=int(id_ativo)))
#                 #         qtd_tot_venda = int(UsuarioEmpresaLancamento.buscar_total_venda(id_usuario=id_usuario, id_ativo=int(id_ativo)))
#                 #         qtd_tot_venda = qtd_tot_venda + int(quant)
#                 #         if int(qtd_tot_venda) > int(qtd_tot_compra):
#                 #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(qtd_tot_compra) + ').'
#                 #             continue
#                 #     elif str(tipo_invest) == 'FII':
#                 #         qtd_tot_compra = int(UsuarioFiiFundoImobLancamento.buscar_total_compra(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#                 #         qtd_tot_bonus = int(UsuarioFiiFundoImobLancamento.buscar_total_bonus(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#                 #         qtd_tot_venda = int(UsuarioFiiFundoImobLancamento.buscar_total_venda(id_usuario=id_usuario, id_fundo=int(id_ativo)))
#                 #         qtd_tot_venda = qtd_tot_venda + int(quant)
#                 #         if int(qtd_tot_venda) > (int(qtd_tot_compra)+int(qtd_tot_bonus)):
#                 #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(int(qtd_tot_compra)+int(qtd_tot_bonus)) + ').'
#                 #             continue
#                 #     elif str(tipo_invest) == 'ETF':
#                 #         qtd_tot_compra = int(UsuarioETFIndiceLancamento.buscar_total_compra(id_usuario=id_usuario, id_indice=int(id_ativo)))
#                 #         qtd_tot_venda = int(UsuarioETFIndiceLancamento.buscar_total_venda(id_usuario=id_usuario, id_indice=int(id_ativo)))
#                 #         qtd_tot_venda = qtd_tot_venda + int(quant)
#                 #         if int(qtd_tot_venda) > int(qtd_tot_compra):
#                 #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(qtd_tot_compra) + ').'
#                 #             continue
#                 #     elif str(tipo_invest) == 'BDR':
#                 #         qtd_tot_compra = int(UsuarioBDREmpresaLancamento.buscar_total_compra(id_usuario=id_usuario, id_bdr=int(id_ativo)))
#                 #         qtd_tot_venda = int(UsuarioBDREmpresaLancamento.buscar_total_venda(id_usuario=id_usuario, id_bdr=int(id_ativo)))
#                 #         qtd_tot_venda = qtd_tot_venda + int(quant)
#                 #         if int(qtd_tot_venda) > int(qtd_tot_compra):
#                 #             lista_import[indx]['SITUACAO'] = 'Venda Superior a Quant. Comprado(' + str(qtd_tot_compra) + ').'
#                 #             continue
#
#                 if str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'ETF' or str(tipo_invest) == 'BDR':
#                     if str(tipo) == 'A':
#                         lista_import[indx]['SITUACAO'] = 'Tipo inválido para o Ativo.'
#                         continue
#
#                 lanc = None
#
#                 if str(tipo_invest) == 'ACAO':
#                     lanc = UsuarioACAOEmpresaLancamento(id_ativo=int(id_ativo), id_usuario=id_usuario, quant_pend=int(quant))
#
#                 elif str(tipo_invest) == 'FII':
#                     lanc = UsuarioFiiFundoImobLancamento(id_fundo=int(id_ativo), id_usuario=id_usuario, quant_orig=int(quant))
#
#                 elif str(tipo_invest) == 'ETF':
#                     lanc = UsuarioETFIndiceLancamento(id_indice=int(id_ativo), id_usuario=id_usuario, quant_pend=int(quant))
#
#                 elif str(tipo_invest) == 'BDR':
#                     lanc = UsuarioBDREmpresaLancamento(id_bdr=int(id_ativo), id_usuario=id_usuario, quant_pend=int(quant))
#
#                 lanc.id_corretora = int(id_corretora)
#                 lanc.tipo = str(tipo)
#                 lanc.data = str(dt_lanc)
#                 lanc.quant = int(quant)
#                 lanc.vlr_preco = float(vlr_preco) if str(tipo) == 'A' or str(tipo) == 'C' or str(tipo) == 'B' or str(tipo) == 'V' else 0.0
#                 lanc.vlr_corretagem = 0.0
#                 lanc.vlr_liquidacao = 0.0
#                 lanc.vlr_emolumentos = 0.0
#                 lanc.vlr_iss = 0.0
#                 lanc.vlr_irpf = 0.0
#                 lanc.vlr_outras = 0.0
#
#                 if str(tipo) == 'C' or str(tipo) == 'V':
#                     lanc.vlr_corretagem = float(vlr_corretagem)
#                     lanc.vlr_liquidacao = float(vlr_liquidacao)
#                     lanc.vlr_emolumentos = float(vlr_emolumentos)
#                     lanc.vlr_iss = float(vlr_iss)
#                     lanc.vlr_irpf = float(vlr_irpf)
#                     lanc.vlr_outras = float(vlr_outras)
#
#                 if str(tipo_invest) == 'FII':
#                     lanc.vlr_preco_medio = 0.0
#                     lanc.tot_vlr_valorizacao = 0.0
#                     lanc.perc_valorizacao = 0.0
#
#                 lanc.calc_tot_preco()
#                 lanc.calc_tot_taxa()
#                 lanc.calc_total()
#                 lanc.calc_custo()
#                 lanc.situacao = 'A' if (str(tipo) == 'D' or str(tipo) == 'G') and not vlr_preco else 'P'  # A-Ativo # P-PendenteDefinicaoSituacao
#
#                 try:
#                     lanc.salvar()
#                     lista_import[indx]['ID'] = str(lanc.id)
#                     lista_import[indx]['TIPO'] = lanc.tipo_descr()
#                     lista_import[indx]['SITUACAO'] = 'Importado'
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Falha ao inserir.'
#                     continue
#
#                 try:
#                     if str(tipo_invest) == 'ACAO':
#                         UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                         UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                         UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(id_ativo))  # Excluir Todas as Operações do Ativo
#                     elif str(tipo_invest) == 'FII':
#                         UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                         UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                     elif str(tipo_invest) == 'ETF':
#                         UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                         UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                         UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(id_ativo))  # Excluir Todas as Operações do Ativo
#                     elif str(tipo_invest) == 'BDR':
#                         UsuarioCarteiraBdr.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Alterar Ativo para F-Finalizado e Quant para Zero
#                         UsuarioBDREmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#                         UsuarioBDREmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_bdr=int(id_ativo))  # Excluir Todas as Operações do Ativo
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Falha ao Resetar Ativos.'
#                     continue
#
#         if not lista_import:
#             return make_response(get_json_retorno_grid(msg='Nenhum Operação Importada.'), 200)
#
#         UsuarioApuracaoCalculada.excluir_tudo(id_usuario=id_usuario)
#
#         lista = []
#
#         lista += [
#             [
#                 'CALC',
#                 str(row[0]), # dt_lanc
#                 decimal_to_str(valor=float(row[1])), # VLR_LIQ_OPER
#                 decimal_to_str(valor=float(row[2])), # VLR_TX_LIQ
#                 decimal_to_str(valor=float(row[3])), # VLR_TX_EMOL
#                 decimal_to_str(valor=float(row[4])), # VLR_TX_CORRET
#                 decimal_to_str(valor=float(row[5])), # VLR_TX_ISS
#                 decimal_to_str(valor=float(row[6])), # VLR_TX_IRRF
#                 decimal_to_str(valor=float(row[7])), # VLR_TX_OUTRAS
#                 decimal_to_str(valor=float(row[8])), # VLR_TOTAL
#             ] for row in lista_import_geral
#         ]
#
#         lista += [
#             [
#                 str(row['DATA']),
#                 str(row['TIPO']),
#                 str(row['CODIGO']),
#                 str(row['QUANT']).replace('.',''),
#                 decimal_to_str(valor=float(row['VLRPRECO'])),
#                 decimal_to_str(valor=float(row['VLRTXCORRETAGEM'])),
#                 decimal_to_str(valor=float(row['VLRTXLIQUIDACAO'])),
#                 decimal_to_str(valor=float(row['VLRTXEMOLUMENTOS'])),
#                 decimal_to_str(valor=float(row['VLRTXISS'])),
#                 decimal_to_str(valor=float(row['VLRTXIRRF'])),
#                 decimal_to_str(valor=float(row['VLRTXOUTRAS'])),
#                 str(row['SITUACAO']),
#                 str(row['ID']),
#                 str(row['INDEX'])
#             ] for row in lista_import
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', msg='Arquivo CSV importado com sucesso!', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/carregar', methods=['GET', 'POST'])
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
#             id_lancamento = data.get('IdOper')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_lancamento: return make_response(get_json_retorno_dados(msg='Id. Operação não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_dados(msg='Código não informado.'), 200)
#
#         tipo_invest = ''
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'ACAO'
#         elif FiiFundoImob.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'FII'
#         elif ETFIndice.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'ETF'
#         elif BDREmpresa.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'BDR'
#         elif CriptoEmpresa.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'CRIPTO'
#
#         if not tipo_invest:
#             return make_response(get_json_retorno_dados(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         oper = None
#         if str(tipo_invest) == 'ACAO':
#             oper = UsuarioACAOEmpresaLancamento.buscar_por_id(id_usuario=id_usuario, id=int(id_lancamento))
#         elif str(tipo_invest) == 'FII':
#             oper = UsuarioFiiFundoImobLancamento.buscar_por_id(id_usuario=id_usuario, id=int(id_lancamento))
#         elif str(tipo_invest) == 'ETF':
#             oper = UsuarioETFIndiceLancamento.buscar_por_id(id_usuario=id_usuario, id=int(id_lancamento))
#         elif str(tipo_invest) == 'BDR':
#             oper = UsuarioBDREmpresaLancamento.buscar_por_id(id_usuario=id_usuario, id=int(id_lancamento))
#         elif str(tipo_invest) == 'CRIPTO':
#             oper = UsuarioCriptoLancamento.buscar_por_id(id_usuario=id_usuario, id=int(id_lancamento))
#
#         if not oper:
#             return make_response(get_json_retorno_dados(msg='Operação não localizada.'), 200)
#
#         dados = dict({})
#
#         if str(tipo_invest) == 'ACAO':
#             dados = dict({
#                 "IdOper": str(oper['ID']),
#                 "CodAtivo": str(oper['CODIGOATIVO']),
#                 "Tipo": str(oper['TIPO']),
#                 "Data": converter_datetime_str(data=converter_str_to_datetime(data=str(oper['DATA']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "Quant": int(oper['QUANT']),
#                 "Preco": decimal_to_str(valor=oper['VLRPRECO']),
#                 "Corretora": str(oper['IDCORRETORA']) if oper['IDCORRETORA'] else '',
#                 "TxCorret": decimal_to_str(valor=oper['VLRTXCORRETAGEM']),
#                 "TxLiquid": decimal_to_str(valor=oper['VLRTXLIQUIDACAO']),
#                 "TxEmol": decimal_to_str(valor=oper['VLRTXEMOLUMENTOS']),
#                 "TxISS": decimal_to_str(valor=oper['VLRTXISS']),
#                 "TxIRRF": decimal_to_str(valor=oper['VLRTXIRRF']),
#                 "TxOutras": decimal_to_str(valor=oper['VLRTXOUTRAS'])
#             })
#
#         elif str(tipo_invest) == 'FII':
#             dados = dict({
#                 "IdOper": str(oper['ID']),
#                 "CodAtivo": str(oper['CODIGOFUNDO']),
#                 "Tipo": str(oper['TIPO']),
#                 "Data": converter_datetime_str(data=converter_str_to_datetime(data=str(oper['DATA']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "Quant": int(oper['QUANT']),
#                 "Preco": decimal_to_str(valor=oper['VLRPRECO']),
#                 "Corretora": str(oper['IDCORRETORA']) if oper['IDCORRETORA'] else '',
#                 "TxCorret": decimal_to_str(valor=oper['VLRTXCORRETAGEM']),
#                 "TxLiquid": decimal_to_str(valor=oper['VLRTXLIQUIDACAO']),
#                 "TxEmol": decimal_to_str(valor=oper['VLRTXEMOLUMENTOS']),
#                 "TxISS": decimal_to_str(valor=oper['VLRTXISS']),
#                 "TxIRRF": decimal_to_str(valor=oper['VLRTXIRRF']),
#                 "TxOutras": decimal_to_str(valor=oper['VLRTXOUTRAS'])
#             })
#
#         elif str(tipo_invest) == 'ETF':
#             dados = dict({
#                 "IdOper": str(oper['ID']),
#                 "CodAtivo": str(oper['CODIGOINDICE']),
#                 "Tipo": str(oper['TIPO']),
#                 "Data": converter_datetime_str(data=converter_str_to_datetime(data=str(oper['DATA']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "Quant": int(oper['QUANT']),
#                 "Preco": decimal_to_str(valor=oper['VLRPRECO']),
#                 "Corretora": str(oper['IDCORRETORA']) if oper['IDCORRETORA'] else '',
#                 "TxCorret": decimal_to_str(valor=oper['VLRTXCORRETAGEM']),
#                 "TxLiquid": decimal_to_str(valor=oper['VLRTXLIQUIDACAO']),
#                 "TxEmol": decimal_to_str(valor=oper['VLRTXEMOLUMENTOS']),
#                 "TxISS": decimal_to_str(valor=oper['VLRTXISS']),
#                 "TxIRRF": decimal_to_str(valor=oper['VLRTXIRRF']),
#                 "TxOutras": decimal_to_str(valor=oper['VLRTXOUTRAS'])
#             })
#
#         elif str(tipo_invest) == 'BDR':
#             dados = dict({
#                 "IdOper": str(oper['ID']),
#                 "CodAtivo": str(oper['CODIGOBDR']),
#                 "Tipo": str(oper['TIPO']),
#                 "Data": converter_datetime_str(data=converter_str_to_datetime(data=str(oper['DATA']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "Quant": int(oper['QUANT']),
#                 "Preco": decimal_to_str(valor=oper['VLRPRECO']),
#                 "Corretora": str(oper['IDCORRETORA']) if oper['IDCORRETORA'] else '',
#                 "TxCorret": decimal_to_str(valor=oper['VLRTXCORRETAGEM']),
#                 "TxLiquid": decimal_to_str(valor=oper['VLRTXLIQUIDACAO']),
#                 "TxEmol": decimal_to_str(valor=oper['VLRTXEMOLUMENTOS']),
#                 "TxISS": decimal_to_str(valor=oper['VLRTXISS']),
#                 "TxIRRF": decimal_to_str(valor=oper['VLRTXIRRF']),
#                 "TxOutras": decimal_to_str(valor=oper['VLRTXOUTRAS'])
#             })
#
#         elif str(tipo_invest) == 'CRIPTO':
#             dados = dict({
#                 "IdOper": str(oper['ID']),
#                 "CodAtivo": str(oper['CODIGOCRIPTO']),
#                 "Tipo": str(oper['TIPO']),
#                 "Data": converter_datetime_str(data=converter_str_to_datetime(data=str(oper['DATA']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "Quant": decimal_prov_to_str(valor=float(oper['QUANT'])),
#                 "Preco": decimal_prov_to_str(valor=float(oper['VLRPRECO'])),  # .rstrip('0')
#                 "Corretora": str(oper['IDCORRETORA']) if oper['IDCORRETORA'] else '',
#                 "TxCorret": decimal_to_str(valor=float(oper['VLRTAXA'])),
#                 "TxLiquid": decimal_to_str(valor=0.0),
#                 "TxEmol": decimal_to_str(valor=0.0),
#                 "TxISS": decimal_to_str(valor=0.0),
#                 "TxIRRF": decimal_to_str(valor=0.0),
#                 "TxOutras": decimal_to_str(valor=0.0)
#             })
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/precoatual', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def preco_atual():
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
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_dados(msg='Código não informado.'), 200)
#
#         tipo_invest = ''
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'ACAO'
#         elif FiiFundoImob.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'FII'
#         elif ETFIndice.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'ETF'
#         elif BDREmpresa.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'BDR'
#         elif CriptoEmpresa.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'CRIPTO'
#
#         if not tipo_invest:
#             return make_response(get_json_retorno_dados(msg='Código não localizado.'), 200)
#
#         cotacao = None
#         if str(tipo_invest) == 'ACAO':
#             cotacao = ACAOEmpresaAtivoCotacao.buscar_por_codigo(codigo=str(codigo))
#         elif str(tipo_invest) == 'FII':
#             cotacao = FiiFundoImobCotacao.buscar_por_codigo(codigo=str(codigo))
#         elif str(tipo_invest) == 'ETF':
#             cotacao = ETFIndiceCotacao.buscar_por_codigo(codigo=str(codigo))
#         elif str(tipo_invest) == 'BDR':
#             cotacao = BDREmpresaCotacao.buscar_por_codigo(codigo=str(codigo))
#         elif str(tipo_invest) == 'CRIPTO':
#             cotacao = CriptoEmpresa.buscar_por_codigo(codigo=str(codigo))
#
#         vlr_preco_atual = float(cotacao['VLRPRECOFECHAMENTO']) if cotacao and cotacao['VLRPRECOFECHAMENTO'] and float(cotacao['VLRPRECOFECHAMENTO']) > 0.0 else 0.0
#
#         dados = dict({"PrecoAtual": decimal_to_str(valor=float(vlr_preco_atual))})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/precomedio', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def preco_medio():
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
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_dados(msg='Código não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         tipo_invest = ''
#         id_ativo = None
#
#         if not tipo_invest:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'ACAO'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'FII'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = ETFIndice.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'ETF'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'BDR'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = CriptoEmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'CRIPTO'
#                 id_ativo = int(row.id)
#
#         # if not tipo_invest or not id_ativo:
#         #     return make_response(get_json_retorno_metodo(msg='Código não localizado.'), 200)
#
#         ativo = None
#         if str(tipo_invest) == 'ACAO': ativo = UsuarioCarteiraAcao.buscar_por_ativo(id_usuario=id_usuario, id_ativo=int(id_ativo))
#         elif str(tipo_invest) == 'FII': ativo = UsuarioCarteiraFii.buscar_por_ativo(id_usuario=id_usuario, id_fundo=int(id_ativo))
#         elif str(tipo_invest) == 'ETF': ativo = UsuarioCarteiraEtf.buscar_por_ativo(id_usuario=id_usuario, id_indice=int(id_ativo))
#         elif str(tipo_invest) == 'BDR': ativo = UsuarioCarteiraBdr.buscar_por_ativo(id_usuario=id_usuario, id_bdr=int(id_ativo))
#         elif str(tipo_invest) == 'CRIPTO': ativo = UsuarioCarteiraCripto.buscar_por_ativo(id_usuario=id_usuario, id_cripto=int(id_ativo))
#
#         preco_medio = float(ativo['VLRPRECOMEDIO']) if ativo and ativo['VLRPRECOMEDIO'] and float(ativo['VLRPRECOMEDIO']) > 0.0 else 0.0
#
#         dados = dict({"PrecoMedio": decimal_to_str(valor=float(preco_medio))})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/quantidade', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def quantidade():
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
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_dados(msg='Código não informado.'), 200)
#
#         tipo_invest = ''
#         id_ativo = None
#
#         if not tipo_invest:
#             row = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'ACAO'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = FiiFundoImob.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'FII'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = ETFIndice.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'ETF'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'BDR'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest:
#             row = CriptoEmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'CRIPTO'
#                 id_ativo = int(row.id)
#
#         if not tipo_invest or not id_ativo:
#             return make_response(get_json_retorno_dados(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         quant_atual = 0.0
#
#         if str(tipo_invest) == 'ACAO':
#             quant_compra = UsuarioACAOEmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_ativo=int(id_ativo))
#             quant_bonus = UsuarioACAOEmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_ativo=int(id_ativo))
#             quant_venda = UsuarioACAOEmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_ativo=int(id_ativo))
#             quant_atual = (float(quant_compra) + float(quant_bonus)) - float(quant_venda)
#             if float(quant_atual) <= 0:
#                 quant_compra = UsuarioACAOEmpresaLancamento.buscar_total_compra(id_usuario=id_usuario, id_ativo=int(id_ativo))
#                 quant_venda = UsuarioACAOEmpresaLancamento.buscar_total_venda(id_usuario=id_usuario, id_ativo=int(id_ativo))
#                 quant_atual = float(quant_compra) + - float(quant_venda)
#
#         elif str(tipo_invest) == 'FII':
#             quant_compra = UsuarioFiiFundoImobLancamento.buscar_total_compra(id_usuario=id_usuario, id_fundo=int(id_ativo))
#             quant_bonus = UsuarioFiiFundoImobLancamento.buscar_total_bonus(id_usuario=id_usuario, id_fundo=int(id_ativo))
#             quant_venda = UsuarioFiiFundoImobLancamento.buscar_total_venda(id_usuario=id_usuario, id_fundo=int(id_ativo))
#             quant_atual = (float(quant_compra) + float(quant_bonus)) - float(quant_venda)
#
#         elif str(tipo_invest) == 'ETF':
#             quant_compra = UsuarioETFIndiceOperacao.buscar_total_compra(id_usuario=id_usuario, id_indice=int(id_ativo))
#             quant_bonus = UsuarioETFIndiceOperacao.buscar_total_bonus(id_usuario=id_usuario, id_indice=int(id_ativo))
#             quant_venda = UsuarioETFIndiceOperacao.buscar_total_venda(id_usuario=id_usuario, id_indice=int(id_ativo))
#             quant_atual = (float(quant_compra) + float(quant_bonus)) - float(quant_venda)
#             if float(quant_atual) <= 0:
#                 quant_compra = UsuarioETFIndiceLancamento.buscar_total_compra(id_usuario=id_usuario, id_indice=int(id_ativo))
#                 quant_venda = UsuarioETFIndiceLancamento.buscar_total_venda(id_usuario=id_usuario, id_indice=int(id_ativo))
#                 quant_atual = float(quant_compra) + - float(quant_venda)
#
#         elif str(tipo_invest) == 'BDR':
#             quant_compra = UsuarioBDREmpresaOperacao.buscar_total_compra(id_usuario=id_usuario, id_bdr=int(id_ativo))
#             quant_bonus = UsuarioBDREmpresaOperacao.buscar_total_bonus(id_usuario=id_usuario, id_bdr=int(id_ativo))
#             quant_venda = UsuarioBDREmpresaOperacao.buscar_total_venda(id_usuario=id_usuario, id_bdr=int(id_ativo))
#             quant_atual = (float(quant_compra) + float(quant_bonus)) - float(quant_venda)
#             if float(quant_atual) <= 0:
#                 quant_compra = UsuarioBDREmpresaLancamento.buscar_total_compra(id_usuario=id_usuario, id_bdr=int(id_ativo))
#                 quant_venda = UsuarioBDREmpresaLancamento.buscar_total_venda(id_usuario=id_usuario, id_bdr=int(id_ativo))
#                 quant_atual = float(quant_compra) + - float(quant_venda)
#
#         elif str(tipo_invest) == 'CRIPTO':
#             quant_compra = UsuarioCriptoLancamento.buscar_total_compra(id_usuario=id_usuario, id_cripto=int(id_ativo))
#             quant_venda = UsuarioCriptoLancamento.buscar_total_venda(id_usuario=id_usuario, id_cripto=int(id_ativo))
#             quant_atual = float(quant_compra) - float(quant_venda)
#
#         dados = dict({"QuantAtual": float(quant_atual)})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/excluir', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir():
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
#             id_lancamento = data.get('IdOper')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_lancamento: return make_response(get_json_retorno_metodo(msg='Id. Operação não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Código não informado.'), 200)
#
#         tipo_invest = ''
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'ACAO'
#         elif FiiFundoImob.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'FII'
#         elif ETFIndice.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'ETF'
#         elif BDREmpresa.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'BDR'
#         elif CriptoEmpresa.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'CRIPTO'
#
#         if not tipo_invest: return make_response(get_json_retorno_metodo(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         lanc = None
#         if str(tipo_invest) == 'ACAO':
#             lanc = UsuarioACAOEmpresaLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#         elif str(tipo_invest) == 'FII':
#             lanc = UsuarioFiiFundoImobLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#         elif str(tipo_invest) == 'ETF':
#             lanc = UsuarioETFIndiceLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#         elif str(tipo_invest) == 'BDR':
#             lanc = UsuarioBDREmpresaLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#         elif str(tipo_invest) == 'CRIPTO':
#             lanc = UsuarioCriptoLancamento.get_by_usuario(id_usuario=id_usuario, id=int(id_lancamento))
#
#         if not lanc:
#             return make_response(get_json_retorno_metodo(msg='Operação não localizada.'), 200)
#
#         if str(tipo_invest) == 'ACAO':
#             UsuarioCarteiraAcao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(lanc.id_ativo))
#             UsuarioACAOEmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_ativo=int(lanc.id_ativo))
#             UsuarioACAOEmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_ativo=int(lanc.id_ativo))
#             if str(lanc.tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='C')  # C - AÇÂO-Comum
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='D')  # D - AÇÂO-Day-Trade
#
#         elif str(tipo_invest) == 'FII':
#             UsuarioCarteiraFii.resetar_ativos(id_usuario=id_usuario, id_fundo=int(lanc.id_fundo))
#             UsuarioFiiFundoImobLancamento.resetar_ativos(id_usuario=id_usuario, id_fundo=int(lanc.id_fundo))
#             if str(lanc.tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='F')  # F - FII
#
#         elif str(tipo_invest) == 'ETF':
#             UsuarioCarteiraEtf.resetar_ativos(id_usuario=id_usuario, id_indice=int(lanc.id_indice))
#             UsuarioETFIndiceOperacao.resetar_ativos(id_usuario=id_usuario, id_indice=int(lanc.id_indice))
#             UsuarioETFIndiceLancamento.resetar_ativos(id_usuario=id_usuario, id_indice=int(lanc.id_indice))
#             if str(lanc.tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='E')  # E - ETF-Comum
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='G')  # G - ETF-Day-Trade
#
#         elif str(tipo_invest) == 'BDR':
#             UsuarioCarteiraBdr.resetar_ativos(id_usuario=id_usuario, id_bdr=int(lanc.id_bdr))
#             UsuarioBDREmpresaOperacao.resetar_ativos(id_usuario=id_usuario, id_bdr=int(lanc.id_bdr))
#             UsuarioBDREmpresaLancamento.resetar_ativos(id_usuario=id_usuario, id_bdr=int(lanc.id_bdr))
#             if str(lanc.tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='I')  # I - BDR-Comum
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='J')  # J - BDR-Day-Trade
#
#         elif str(tipo_invest) == 'CRIPTO':
#             UsuarioCarteiraCripto.resetar_ativos(id_usuario=id_usuario, id_cripto=int(lanc.id_cripto))  # Alterar Ativo para F-Finalizado e Quant para Zero
#             UsuarioCriptoLancamento.resetar_ativos(id_usuario=id_usuario, id_cripto=int(lanc.id_cripto))  # Alterar para Pendente Processamento todos os Lançamentos do Ativo
#             if str(lanc.tipo) == 'V':
#                 UsuarioApuracaoCalculada.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria='K')  # K - CRIPTO
#
#         lanc.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Operação Excluída!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_operacoes.route('/excluirtudo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir_tudo():
#     try:
#
#         id_usuario = current_user.id
#
#         UsuarioApuracaoCalculada.excluir_tudo(id_usuario=id_usuario)
#
#         UsuarioCarteiraCripto.excluir_tudo(id_usuario=id_usuario)
#         UsuarioCriptoLancamento.excluir_tudo(id_usuario=id_usuario)
#
#         UsuarioCarteiraBdr.excluir_tudo(id_usuario=id_usuario)
#         UsuarioBDREmpresaOperacao.excluir_tudo(id_usuario=id_usuario)
#         UsuarioBDREmpresaLancamento.excluir_tudo(id_usuario=id_usuario)
#
#         UsuarioCarteiraEtf.excluir_tudo(id_usuario=id_usuario)
#         UsuarioETFIndiceOperacao.excluir_tudo(id_usuario=id_usuario)
#         UsuarioETFIndiceLancamento.excluir_tudo(id_usuario=id_usuario)
#
#         UsuarioCarteiraFii.excluir_tudo(id_usuario=id_usuario)
#         UsuarioFiiFundoImobLancamento.excluir_tudo(id_usuario=id_usuario)
#
#         UsuarioCarteiraAcao.excluir_tudo(id_usuario=id_usuario)
#         UsuarioACAOEmpresaOperacao.excluir_tudo(id_usuario=id_usuario)
#         UsuarioACAOEmpresaLancamento.excluir_tudo(id_usuario=id_usuario)
#
#         Alerta.registrar(id_usuario=id_usuario, tipo='PERFIL-03', mensagem='Todas as suas operações foram apagadas. <br>IP: ' + str(request.remote_addr))
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Todas as operações foram excluídas!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
