# -*- coding: utf-8 -*-
import sys
import os
import requests
from lxml import html
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.acao_empresa_ativo_cotacao import ACAOEmpresaAtivoCotacao
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_formatacao import decimal_to_str
# from app.util.util_datahora import pegar_data_atual, pegar_data_hora_atual, converter_str_to_datetime, converter_datetime_str


router = _fastapi.APIRouter(prefix="/cotacao", tags=['admin_empresa_cotacao'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @login_required
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
async def get_index():
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="admin_empresa_cotacao.html")
    return {"result": "ok"}


# @bp_admin_empresa_cotacao.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_grid(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
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
#             setor = data.get('Setor')
#             subsetor = data.get('SubSetor')
#             segmento = data.get('Segmento')
#             codigo = data.get('CodAtivo')
#             tipo = data.get('Tipo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         id_usuario = current_user.id
#
#         rows = ACAOEmpresaAtivoCotacao.buscar_todos_completo(id_usuario=id_usuario, setor=setor, subsetor=subsetor, segmento=segmento, codigo=codigo, tipo=tipo)
#
#         lista = [
#             [
#                 str(row['CODIGOATIVO']),
#                 decimal_to_str(valor=float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] else 0.0),
#                 decimal_to_str(valor=float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] else 0.0),
#                 decimal_to_str(valor=((float(row['VLRPRECOANTERIOR']) if row['VLRPRECOANTERIOR'] else 0.0) - (float(row['VLRPRECOFECHAMENTO']) if row['VLRPRECOFECHAMENTO'] else 0.0))),
#                 decimal_to_str(valor=float(row['VLRVARIACAO']) if row['VLRVARIACAO'] else 0.0),
#                 str(row['DATAHORAALTERACO'])
#             ]
#             for row in rows
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_empresa_cotacao.route('/salvar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_metodo(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
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
#             vlr_preco_fechamento = data.get('VlrFechamento')
#             vlr_preco_anterior = data.get('VlrAnterior')
#             vlr_variacao = data.get('Variacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Ativo não informado.'), 200)
#
#         ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#
#         if not ativo:
#             return make_response(get_json_retorno_metodo(msg='Ativo não localizado.'), 200)
#
#         cotacao = ACAOEmpresaAtivoCotacao.get_by_ativo(id_ativo=int(ativo.id))
#
#         if not cotacao:
#             cotacao = ACAOEmpresaAtivoCotacao(id_ativo=int(ativo.id))
#
#         vlr_preco_fechamento = float(str(vlr_preco_fechamento).replace('.', '').replace(',', '.')) if vlr_preco_fechamento else 0.0
#         vlr_preco_anterior = float(str(vlr_preco_anterior).replace('.', '').replace(',', '.')) if vlr_preco_anterior else 0.0
#         vlr_variacao = float(str(vlr_variacao).replace('.', '').replace(',', '.')) if vlr_variacao else 0.0
#
#         cotacao.data = pegar_data_atual()
#         cotacao.vlr_preco_abertura = 0.0
#         cotacao.vlr_preco_fechamento = float(vlr_preco_fechamento)
#         cotacao.vlr_preco_maximo = 0.0
#         cotacao.vlr_preco_minimo = 0.0
#         cotacao.vlr_preco_anterior = float(vlr_preco_anterior)
#         cotacao.vlr_variacao = float(vlr_variacao)
#         cotacao.data_hora_alteracao = pegar_data_hora_atual()
#         cotacao.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_empresa_cotacao.route('/carregar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_dados(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
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
#         if not codigo: return make_response(get_json_retorno_dados(msg='Ativo não informado.'), 200)
#
#         cotacao = ACAOEmpresaAtivoCotacao.buscar_por_codigo(codigo=str(codigo))
#
#         if not cotacao:
#             return make_response(get_json_retorno_dados(msg='Cotação não localizada!'), 200)
#
#         dados = dict(
#             {
#                 "Data": converter_datetime_str(data=converter_str_to_datetime(data=cotacao['DATA'], fmt='%Y%m%d'), fmt='%Y-%m-%d'),
#                 "Ativo": cotacao['CODIGOATIVO'],
#                 "Abertura": decimal_to_str(valor=float(cotacao['VLRPRECOABERTURA']) if cotacao['VLRPRECOABERTURA'] else 0.0),
#                 "Fechamento": decimal_to_str(valor=float(cotacao['VLRPRECOFECHAMENTO']) if cotacao['VLRPRECOFECHAMENTO'] else 0.0),
#                 "Maximo": decimal_to_str(valor=float(cotacao['VLRPRECOMAXIMO']) if cotacao['VLRPRECOMAXIMO'] else 0.0),
#                 "Minimo": decimal_to_str(valor=float(cotacao['VLRPRECOMINIMO']) if cotacao['VLRPRECOMINIMO'] else 0.0),
#                 "VlrAnterior": decimal_to_str(valor=float(cotacao['VLRPRECOANTERIOR']) if cotacao['VLRPRECOANTERIOR'] else 0.0),
#                 "Variacao": decimal_to_str(valor=float(cotacao['VLRVARIACAO']) if cotacao['VLRVARIACAO'] else 0.0)
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
# @bp_admin_empresa_cotacao.route('/AtualizaCotacao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def atualiza_ctacao():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return make_response(get_json_retorno_dados(msg='Usuário não está Permitido! Somente para Administradores.'), 200)
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
#         if not codigo: return make_response(get_json_retorno_dados(msg='Cod. Ativo não informado.'), 200)
#
#         ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo))
#         if not ativo:
#             return make_response(get_json_retorno_dados(msg='Ativo não localizado.'), 200)
#
#         try:
#             url = 'https://br.financas.yahoo.com/quote/%5EBVSP/' if str(codigo) == 'IBOV' else 'https://br.financas.yahoo.com/quote/'+codigo+'.SA/'
#             response = requests.get(url, verify=True, timeout=30, headers={'User-Agent': 'Mozilla/5.0'})
#         except Exception as e:
#             response = None
#
#         if not response or response.status_code != 200:
#             return make_response(get_json_retorno_dados(msg='Cotação do Ativo: '+codigo+' - Sem conteudo'), 200)
#
#         # soup = BeautifulSoup(response.content, 'lxml')  # lxml # html.parser
#         tree = html.fromstring(response.content)
#
#         try:
#             vlr_preco_fechamento = tree.xpath('//*[@id="quote-header-info"]/div[3]/div/span[1]/text()')[0].strip()
#             perc_variacao = tree.xpath('//*[@id="quote-header-info"]/div[3]/div/div/span[1]/text()')[0].strip()
#         except:
#             vlr_preco_fechamento = tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[1]/text()')[0].strip()
#             perc_variacao = tree.xpath('//*[@id="quote-header-info"]/div[3]/div[1]/div/span[2]/text()')[0].strip()
#
#         vlr_preco_anterior = tree.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]/span/text()')[0].strip()
#
#         vlr_preco_fechamento = vlr_preco_fechamento.replace('.', '').replace(',', '.')
#         perc_variacao = perc_variacao.replace('.', '').replace(',', '.')
#         vlr_preco_anterior = vlr_preco_anterior.replace('.', '').replace(',', '.')
#
#         perc_variacao = perc_variacao[perc_variacao.find('(') + 1:perc_variacao.find('%')].strip()
#
#         vlr_preco_fechamento = float(vlr_preco_fechamento)
#         perc_variacao = float(perc_variacao)
#         vlr_preco_anterior = float(vlr_preco_anterior)
#
#         if vlr_preco_fechamento <= 0.0 or vlr_preco_anterior <= 0.0:
#             return make_response(get_json_retorno_metodo(msg='Cotação do Ativo: '+codigo+' - Sem Valoes'), 200)
#
#         cotacao = ACAOEmpresaAtivoCotacao.get_by_ativo(id_ativo=int(ativo.id))
#         if not cotacao:
#             cotacao = ACAOEmpresaAtivoCotacao(id_ativo=int(ativo.id))
#
#         cotacao.data = pegar_data_atual()
#         cotacao.vlr_preco_abertura = 0.0
#         cotacao.vlr_preco_fechamento = float(vlr_preco_fechamento)
#         cotacao.vlr_preco_maximo = 0.0
#         cotacao.vlr_preco_minimo = 0.0
#         cotacao.vlr_preco_anterior = float(vlr_preco_anterior)
#         cotacao.vlr_variacao = float(vlr_preco_anterior) - float(vlr_preco_fechamento)
#         cotacao.data_hora_alteracao = pegar_data_hora_atual()
#         cotacao.salvar()
#
#         dados = dict(
#             {
#                 "Ativo": str(codigo),
#                 "Fechamento": decimal_to_str(valor=float(cotacao.vlr_preco_fechamento)),
#                 "VlrAnterior": decimal_to_str(valor=float(cotacao.vlr_preco_anterior)),
#                 "VlrVariacao": decimal_to_str(valor=float(cotacao.vlr_variacao)),
#                 "PercVariacao": decimal_to_str(valor=float(perc_variacao)),
#                 "DtHrAtualizacao": str(cotacao.data_hora_alteracao)
#             }
#         )
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
