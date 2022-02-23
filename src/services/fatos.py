# # -*- coding: utf-8 -*-
# import sys
# import os
# from math import floor, ceil
# from flask import Blueprint, render_template, request, make_response
# from flask_login import login_required
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.acao_empresa_fato_relevante import ACAOEmpresaFatoRelevante
# from app.models.fii_fundoimob_fato_relevante import FiiFundoImobFatoRelevante
# from app.models.etf_indice_fato_relevante import ETFIndiceFatoRelevante
# from app.models.bdr_empresa_fato_relevante import BDREmpresaFatoRelevante
# from app.util.util_json import get_json_retorno_lista_coment
#
#
# bp_fatos = Blueprint('fatos', __name__, url_prefix='/fatos')
#
#
# @bp_fatos.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# # @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     return render_template(template_name_or_list="fatos.html")
#
#
# @bp_fatos.route('/grid', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid():
#     try:
#
#         qtde_por_pagina = 100  # seta a quantidade de itens por página, neste caso, 2 itens
#         pag_atual = 1
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#             pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         try:
#             tipo_invest = data.get('TipoInvest')
#             id_empresa = data.get('IdEmpresa')
#             if not pag_atual: pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#         except:
#             return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         if not tipo_invest: tipo_invest = 'ACAO'
#         if not pag_atual: pag_atual = 1
#         pag_atual = int(pag_atual)
#
#         tot_registro = 0
#
#         if tipo_invest == 'ACAO': tot_registro = ACAOEmpresaFatoRelevante.get_total(id_empresa=id_empresa)
#         elif tipo_invest == 'FII': tot_registro = FiiFundoImobFatoRelevante.get_total(id_fundo=id_empresa)
#         elif tipo_invest == 'ETF': tot_registro = ETFIndiceFatoRelevante.get_total(id_indice=id_empresa)
#         elif tipo_invest == 'BDR': tot_registro = BDREmpresaFatoRelevante.get_total(id_empresa=id_empresa)
#
#         pag_total = ceil(tot_registro / qtde_por_pagina)  # calcula o número de páginas arredondando o resultado para cima
#         reg_inicio = (qtde_por_pagina * pag_atual) - qtde_por_pagina  # variavel para calcular o início da visualização com base na página atual
#
#         lista = []
#
#         if tipo_invest == 'ACAO':
#             rows = ACAOEmpresaFatoRelevante.get_all(id_empresa=id_empresa, reg_inicio=reg_inicio, qtde_por_pagina=qtde_por_pagina)
#             lista = [[str(fato.id), str(fato.nm_empresa), str(fato.data_env), str(fato.link), str(fato.assunto), str(fato.conteudo), str(fato.protocolo), tipo_invest] for fato in rows]
#
#         elif tipo_invest == 'FII':
#             rows = FiiFundoImobFatoRelevante.get_all(id_fundo=id_empresa, reg_inicio=reg_inicio, qtde_por_pagina=qtde_por_pagina)
#             lista = [[str(fato.id), str(fato.nm_fundo), str(fato.data_env), str(fato.link), str(fato.assunto), str(fato.conteudo), str(fato.protocolo), tipo_invest] for fato in rows]
#
#         elif tipo_invest == 'ETF':
#             rows = ETFIndiceFatoRelevante.get_all(id_indice=id_empresa, reg_inicio=reg_inicio, qtde_por_pagina=qtde_por_pagina)
#             lista = [[str(fato.id), str(fato.nm_indice), str(fato.data_env), str(fato.link), str(fato.assunto), str(fato.conteudo), str(fato.protocolo), tipo_invest] for fato in rows]
#
#         elif tipo_invest == 'BDR':
#             rows = BDREmpresaFatoRelevante.get_all(id_empresa=id_empresa, reg_inicio=reg_inicio, qtde_por_pagina=qtde_por_pagina)
#             lista = [[str(fato.id), str(fato.nm_empresa), str(fato.data_env), str(fato.link), str(fato.assunto), str(fato.conteudo), str(fato.protocolo), tipo_invest] for fato in rows]
#
#         return make_response(get_json_retorno_lista_coment(rslt='OK', pag_atual=str(pag_atual), pag_total=str(pag_total), lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista_coment(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_fatos.route('/gridAcao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_acao():
#     try:
#
#         qtde_por_pagina = 100  # seta a quantidade de itens por página, neste caso, 2 itens
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#             pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         try:
#             id_empresa = data.get('IdEmpresa')
#             pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#         except:
#             return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         if not pag_atual: pag_atual = 1
#         pag_atual = int(pag_atual)
#
#         tot_registro = ACAOEmpresaFatoRelevante.get_total(id_empresa=id_empresa)
#
#         pag_total = ceil(tot_registro / qtde_por_pagina)  # calcula o número de páginas arredondando o resultado para cima
#         reg_inicio = (qtde_por_pagina * pag_atual) - qtde_por_pagina  # variavel para calcular o início da visualização com base na página atual
#
#         rows = ACAOEmpresaFatoRelevante.get_all(id_empresa=id_empresa, reg_inicio=reg_inicio, qtde_por_pagina=qtde_por_pagina)
#         lista = [[str(fato.id), str(fato.nm_empresa), str(fato.data_env), str(fato.link), str(fato.assunto), str(fato.conteudo), str(fato.protocolo), 'ACAO'] for fato in rows]
#
#         return make_response(get_json_retorno_lista_coment(rslt='OK', pag_atual=str(pag_atual), pag_total=str(pag_total), lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista_coment(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_fatos.route('/gridFii', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_fii():
#     try:
#
#         qtde_por_pagina = 100  # seta a quantidade de itens por página, neste caso, 2 itens
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#             pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         try:
#             id_empresa = data.get('IdEmpresa')
#             pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#         except:
#             return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         if not pag_atual: pag_atual = 1
#         pag_atual = int(pag_atual)
#
#         tot_registro = FiiFundoImobFatoRelevante.get_total(id_fundo=id_empresa)
#
#         pag_total = ceil(tot_registro / qtde_por_pagina)  # calcula o número de páginas arredondando o resultado para cima
#         reg_inicio = (qtde_por_pagina * pag_atual) - qtde_por_pagina  # variavel para calcular o início da visualização com base na página atual
#
#         rows = FiiFundoImobFatoRelevante.get_all(id_fundo=id_empresa, reg_inicio=reg_inicio, qtde_por_pagina=qtde_por_pagina)
#         lista = [[str(fato.id), str(fato.nm_fundo), str(fato.data_env), str(fato.link), str(fato.assunto), str(fato.conteudo), str(fato.protocolo), 'FII'] for fato in rows]
#
#         return make_response(get_json_retorno_lista_coment(rslt='OK', pag_atual=str(pag_atual), pag_total=str(pag_total), lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista_coment(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_fatos.route('/gridEtf', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_etf():
#     try:
#
#         qtde_por_pagina = 100  # seta a quantidade de itens por página, neste caso, 2 itens
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#             pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         try:
#             id_empresa = data.get('IdEmpresa')
#             pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#         except:
#             return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         if not pag_atual: pag_atual = 1
#         pag_atual = int(pag_atual)
#
#         tot_registro = ETFIndiceFatoRelevante.get_total(id_indice=id_empresa)
#
#         pag_total = ceil(tot_registro / qtde_por_pagina)  # calcula o número de páginas arredondando o resultado para cima
#         reg_inicio = (qtde_por_pagina * pag_atual) - qtde_por_pagina  # variavel para calcular o início da visualização com base na página atual
#
#         rows = ETFIndiceFatoRelevante.get_all(id_indice=id_empresa, reg_inicio=reg_inicio, qtde_por_pagina=qtde_por_pagina)
#         lista = [[str(fato.id), str(fato.nm_indice), str(fato.data_env), str(fato.link), str(fato.assunto), str(fato.conteudo), str(fato.protocolo), 'ETF'] for fato in rows]
#
#         return make_response(get_json_retorno_lista_coment(rslt='OK', pag_atual=str(pag_atual), pag_total=str(pag_total), lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista_coment(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_fatos.route('/gridBdr', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def grid_bdr():
#     try:
#
#         qtde_por_pagina = 100  # seta a quantidade de itens por página, neste caso, 2 itens
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#             pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         try:
#             id_empresa = data.get('IdEmpresa')
#             pag_atual = data.get('PagAtual')  # verifica a página atual caso seja informada na URL, senão atribui como 1ª página
#         except:
#             return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         if not pag_atual: pag_atual = 1
#         pag_atual = int(pag_atual)
#
#         tot_registro = BDREmpresaFatoRelevante.get_total(id_empresa=id_empresa)
#
#         pag_total = ceil(tot_registro / qtde_por_pagina)  # calcula o número de páginas arredondando o resultado para cima
#         reg_inicio = (qtde_por_pagina * pag_atual) - qtde_por_pagina  # variavel para calcular o início da visualização com base na página atual
#
#         rows = BDREmpresaFatoRelevante.get_all(id_empresa=id_empresa, reg_inicio=reg_inicio, qtde_por_pagina=qtde_por_pagina)
#         lista = [[str(fato.id), str(fato.nm_empresa), str(fato.data_env), str(fato.link), str(fato.assunto), str(fato.conteudo), str(fato.protocolo), 'BDR'] for fato in rows]
#
#         return make_response(get_json_retorno_lista_coment(rslt='OK', pag_atual=str(pag_atual), pag_total=str(pag_total), lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista_coment(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
