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
# from app.models.fii_fundoimob import FiiFundoImob
# from app.models.bdr_empresa import BDREmpresa
# from app.models.usuario_corretora import UsuarioCorretora
# from app.models.usuario_acao_empresa_provento import UsuarioACAOEmpresaProvento
# from app.models.usuario_fii_fundoimob_provento import UsuarioFiiFundoImobProvento
# from app.models.usuario_bdr_empresa_provento import UsuarioBDREmpresaProvento
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_formatacao import decimal_to_str, decimal_prov_to_str
# from app.util.util_datahora import converter_datetime_str, converter_str_to_datetime, pegar_data_hora_atual
#
#
# bp_proventos = Blueprint('proventos', __name__, url_prefix='/proventos')
#
#
# @bp_proventos.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# # @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     return render_template(template_name_or_list="proventos.html")
#
#
# @bp_proventos.route('/grid', methods=['GET', 'POST'])
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
#             tipo = data.get('TipoRend')
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
#         if codigo and str(codigo) == 'BDR': tipo_invest = 'BDR'
#         if tipo_invest: codigo = ''
#
#         id_usuario = current_user.id
#
#         lista = []
#
#         if not tipo_invest or str(tipo_invest) == 'ACAO':
#             if not tipo or str(tipo) == 'D' or str(tipo) == 'J' or str(tipo) == 'R':
#                 rows = UsuarioACAOEmpresaProvento.buscar_todos(id_usuario=id_usuario, codigo=codigo, tipo=tipo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#                 lista += [[str(row['DATAEX']), str(row['DATAPAGTO']), str(row['CODIGOATIVO']), UsuarioACAOEmpresaProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', int(row['QUANTIDADE']), decimal_prov_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['TOTVLR'])), str(row['ID']), str(row['SITUACAO']), 'ACAO'] for row in rows]
#
#         if not tipo_invest or str(tipo_invest) == 'FII':
#             if not tipo or str(tipo) == 'FR':
#                 tipo = 'R' if str(tipo) == 'FR' else tipo # FR - FII RENDIMENTO
#                 rows = UsuarioFiiFundoImobProvento.buscar_todos(id_usuario=id_usuario, codigo=codigo, tipo=tipo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#                 lista += [[str(row['DATAEX']), str(row['DATAPAGTO']), str(row['CODIGOFUNDO']), UsuarioFiiFundoImobProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', int(row['QUANTIDADE']), decimal_prov_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['TOTVLR'])), str(row['ID']), str(row['SITUACAO']), 'FII'] for row in rows]
#
#         if not tipo_invest or str(tipo_invest) == 'BDR':
#             if not tipo or str(tipo) == 'D' or str(tipo) == 'J' or str(tipo) == 'R':
#                 rows = UsuarioBDREmpresaProvento.buscar_todos(id_usuario=id_usuario, codigo=codigo, tipo=tipo, dt_ini=dt_ini, dt_fim=dt_fim, id_corretora=id_corretora)
#                 lista += [[str(row['DATAEX']), str(row['DATAPAGTO']), str(row['CODIGOBDR']), UsuarioBDREmpresaProvento.descricao_tipo(tipo=str(row['TIPO'])), str(row['NOMECORRETORA']) if row['NOMECORRETORA'] else '', int(row['QUANTIDADE']), decimal_prov_to_str(valor=float(row['VLRPRECO'])), decimal_to_str(valor=float(row['TOTVLR'])), str(row['ID']), str(row['SITUACAO']), 'BDR'] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_proventos.route('/salvar', methods=['GET', 'POST'])
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
#             id_provento = data.get('Id')
#             id_corretora = data.get('Corretora')
#             codigo = data.get('Ativo')
#             tipo = data.get('Tipo')
#             data_ex = data.get('DataEx')
#             data_pagto = data.get('DataPagto')
#             quantidade = data.get('Quant')
#             calc_vlr_liquido = data.get('CalcVlrLiq')
#             vlr_preco_bruto = data.get('PrecoBruto')
#             vlr_preco = data.get('Preco')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Código não informado.'), 200)
#         if not tipo: return make_response(get_json_retorno_metodo(msg='Tipo não informado.'), 200)
#
#         vlr_preco_bruto = float(str(vlr_preco_bruto).replace('.', '').replace(',', '.')) if vlr_preco_bruto else 0.0
#         vlr_preco = float(str(vlr_preco).replace('.', '').replace(',', '.')) if vlr_preco else 0.0
#         if data_ex: data_ex = str(data_ex).replace('-', '')
#         if data_pagto: data_pagto = str(data_pagto).replace('-', '')
#         if tipo and (str(tipo) == 'D' or str(tipo) == 'R'or str(tipo) == 'FR'): calc_vlr_liquido = 'N'
#         if calc_vlr_liquido and str(calc_vlr_liquido) == 'N': vlr_preco_bruto = vlr_preco
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
#             row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#             if row:
#                 tipo_invest = 'BDR'
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
#         if str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'BDR':
#             if str(tipo) != 'D' and str(tipo) != 'J' and str(tipo) != 'R':
#                 return make_response(get_json_retorno_metodo(msg='Tipo Provento Inválido.'), 200)
#
#         elif str(tipo_invest) == 'FII':
#             if str(tipo) != 'FR':
#                 return make_response(get_json_retorno_metodo(msg='Tipo Provento Inválido.'), 200)
#             tipo = "R" if str(tipo) == 'FR' else str(tipo)
#
#         prov = None
#
#         if str(tipo_invest) == 'ACAO':
#
#             if id_provento:
#                 prov = UsuarioACAOEmpresaProvento.get_by_usuario(id_usuario=id_usuario, id=int(id_provento))
#
#             else:
#                 prov = UsuarioACAOEmpresaProvento()
#                 prov.id_ativo = id_ativo
#                 prov.calc_vlr_liquido = calc_vlr_liquido
#                 prov.vlr_preco_bruto = float(vlr_preco_bruto) if vlr_preco_bruto and float(vlr_preco_bruto) > 0.0 else 0.0
#                 prov.situacao = "B" if int(id_usuario) == 7 else 'A' # A-Ativo # B - Pendente Aprovação/Confirmação
#
#         elif str(tipo_invest) == 'FII':
#
#             if id_provento:
#                 prov = UsuarioFiiFundoImobProvento.get_by_usuario(id_usuario=id_usuario, id=int(id_provento))
#
#             else:
#                 prov = UsuarioFiiFundoImobProvento()
#                 prov.id_fundo = id_ativo
#                 prov.situacao = "B" if int(id_usuario) == 7 else 'A' # A-Ativo # B - Pendente Aprovação/Confirmação
#
#         elif str(tipo_invest) == 'BDR':
#
#             if id_provento:
#                 prov = UsuarioBDREmpresaProvento.get_by_usuario(id_usuario=id_usuario, id=int(id_provento))
#
#             else:
#                 prov = UsuarioBDREmpresaProvento()
#                 prov.id_bdr = id_ativo
#                 prov.calc_vlr_liquido = calc_vlr_liquido
#                 prov.vlr_preco_bruto = float(vlr_preco_bruto) if vlr_preco_bruto and float(vlr_preco_bruto) > 0.0 else 0.0
#                 prov.situacao = "B" if int(id_usuario) == 7 else 'A' # A-Ativo # B - Pendente Aprovação/Confirmação
#
#         if not prov:
#             return make_response(get_json_retorno_metodo(msg='Provento não Localizado.'), 200)
#
#         prov.id_usuario = id_usuario
#         prov.id_corretora = int(id_corretora) if id_corretora else None
#         prov.tipo = str(tipo)
#         prov.data_ex = data_ex
#         prov.data_pagto = data_pagto
#         prov.quantidade = int(quantidade) if quantidade and int(quantidade) > 0 else 0
#         prov.vlr_preco =  float(vlr_preco) if vlr_preco and float(vlr_preco) > 0.0 else 0.0
#
#         prov.tot_vlr = prov.calc_total()
#         if str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'BDR':
#             prov.tot_vlr_bruto = prov.calc_total_bruto()
#
#         prov.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_proventos.route('/aprovar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def aprovar():
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
#             id_provento = data.get('Id')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_provento: return make_response(get_json_retorno_metodo(msg='Id Provento não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Código não informado.'), 200)
#
#         tipo_invest = ''
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'ACAO'
#         elif FiiFundoImob.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'FII'
#         elif BDREmpresa.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'BDR'
#
#         if not tipo_invest:
#             return make_response(get_json_retorno_metodo(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         prov = None
#
#         if str(tipo_invest) == 'ACAO':
#             prov = UsuarioACAOEmpresaProvento.get_by_usuario(id_usuario=id_usuario, id=int(id_provento))
#         elif str(tipo_invest) == 'FII':
#             prov = UsuarioFiiFundoImobProvento.get_by_usuario(id_usuario=id_usuario, id=int(id_provento))
#         elif str(tipo_invest) == 'BDR':
#             prov = UsuarioBDREmpresaProvento.get_by_usuario(id_usuario=id_usuario, id=int(id_provento))
#
#         if not prov:
#             return make_response(get_json_retorno_metodo(msg='Provento não localizado.'), 200)
#
#         if str(prov.situacao) == 'A':
#             return make_response(get_json_retorno_metodo(msg='Provento já Aprovado.'), 200)  # A-Ativo
#
#         if str(prov.situacao) != 'B':
#             return make_response(get_json_retorno_metodo(msg='Provento não está Pendente Aprovação.'), 200)  # B - Pendente Aprovação/Confirmação
#
#         prov.situacao = 'A'
#         prov.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_proventos.route('/importarcsv', methods=['GET', 'POST'])
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
#         path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../' + current_app.config['CSV_PROV_UPLOADS'])
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
#                 data_ex = str(row[0]).strip() if row[0] else ''
#                 data_pagto = str(row[1]).strip() if row[1] else ''
#                 tipo = str(row[2]).strip()[0:1] if row[2] else ''
#                 codigo = str(row[3]).strip().upper() if row[3] else ''
#                 quantidade = str(row[4]).strip().replace('.','') if row[4] else ''
#                 vlr_preco_bruto = str(row[5]).strip() if row[5] else ''
#                 vlr_preco = str(row[6]).strip() if row[6] else ''
#
#                 if not data_ex or not data_pagto or not tipo or not codigo or not quantidade: continue
#                 if str(data_ex)[0:1] == 'D': continue
#                 if str(data_pagto)[0:1] == 'D': continue
#
#                 data_ex = str(data_ex).replace('/', '').replace('-', '').ljust(8,'0')
#                 data_pagto = str(data_pagto).replace('/', '').replace('-', '').ljust(8,'0')
#
#                 data_ex = data_ex[4:8] + data_ex[2:4] + data_ex[0:2]
#                 data_pagto = data_pagto[4:8] + data_pagto[2:4] + data_pagto[0:2]
#
#                 indx += 1
#                 lista_import.append({'INDEX': str(int(indx)+1), 'ID': '', 'DATAEX': str(data_ex), 'DATAPAGTO': str(data_pagto), 'TIPO': str(tipo), 'CODIGO': str(codigo), 'QUANTIDADE': str(quantidade), 'VLRPRECOBRUTO': str(vlr_preco_bruto), 'VLRPRECO': str(vlr_preco), 'SITUACAO': 'Não Importado'})
#
#                 if str(tipo) != "D" and str(tipo) != "R" and str(tipo) != "J" and str(tipo) != "FR":
#                     lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                     continue
#
#                 if not vlr_preco_bruto and vlr_preco: vlr_preco_bruto = vlr_preco
#                 if not vlr_preco and vlr_preco_bruto: vlr_preco = vlr_preco_bruto
#
#                 if not vlr_preco_bruto or str(vlr_preco_bruto) == '' or str(vlr_preco_bruto) == ',' or str(vlr_preco_bruto) == ',0' or str(vlr_preco_bruto) == ',00' or str(vlr_preco_bruto) == '0,00': vlr_preco_bruto = '0,00'
#                 if not vlr_preco or str(vlr_preco) == '' or str(vlr_preco) == ',' or str(vlr_preco) == ',0' or str(vlr_preco) == ',00' or str(vlr_preco) == '0,00': vlr_preco = '0,00'
#
#                 try:
#                     quantidade = int(str(quantidade).replace('.', '').replace(',', '.'))
#                     lista_import[indx]['QUANTIDADE'] = str(quantidade)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Quantidade não informado ou inválido.'
#                     continue
#
#                 try:
#                     vlr_preco_bruto = float(str(vlr_preco_bruto).replace('.', '').replace(',', '.'))
#                     lista_import[indx]['VLRPRECOBRUTO'] = str(vlr_preco_bruto)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Preço Bruto não informado ou inválido.'
#                     continue
#
#                 try:
#                     vlr_preco = float(str(vlr_preco).replace('.', '').replace(',', '.'))
#                     lista_import[indx]['VLRPRECO'] = str(vlr_preco)
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Preço Liquido não informado ou inválido.'
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
#                     row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#                     if row:
#                         tipo_invest = 'BDR'
#                         id_ativo = int(row.id)
#
#                 if not tipo_invest or not id_ativo:
#                     lista_import[indx]['SITUACAO'] = 'Código não localizado.'
#                     continue
#
#                 prov = None
#
#                 if str(tipo_invest) == 'ACAO':
#                     if str(tipo) != 'D' and str(tipo) != 'J' and str(tipo) != 'R':
#                         lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                         continue
#                     prov = UsuarioACAOEmpresaProvento()
#                     prov.id_ativo = int(id_ativo)
#                     prov.vlr_preco_bruto = float(vlr_preco_bruto)
#
#                 elif str(tipo_invest) == 'FII':
#                     if str(tipo) != 'R' and str(tipo) != 'FR':
#                         lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                         continue
#                     tipo = "R" if str(tipo) == 'FR' else str(tipo)
#                     prov = UsuarioFiiFundoImobProvento()
#                     prov.id_fundo = int(id_ativo)
#
#                 elif str(tipo_invest) == 'BDR':
#                     if str(tipo) != 'D' and str(tipo) != 'J' and str(tipo) != 'R':
#                         lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                         continue
#                     prov = UsuarioBDREmpresaProvento()
#                     prov.id_bdr = int(id_ativo)
#                     prov.vlr_preco_bruto = float(vlr_preco_bruto)
#
#                 prov.id_usuario = id_usuario
#                 prov.tipo = str(tipo)
#                 prov.data_ex = str(data_ex)
#                 prov.data_pagto = str(data_pagto)
#                 prov.quantidade = int(quantidade)
#                 prov.vlr_preco =  float(vlr_preco)
#                 prov.tot_vlr = prov.calc_total()
#                 if str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'BDR':
#                     prov.tot_vlr_bruto = prov.calc_total_bruto()
#                 prov.situacao = 'A'
#
#                 try:
#                     prov.salvar()
#                     lista_import[indx]['ID'] = str(prov.id)
#                     lista_import[indx]['TIPO'] = prov.tipo_descr()
#                     lista_import[indx]['SITUACAO'] = 'Importado'
#                 except:
#                     lista_import[indx]['SITUACAO'] = 'Falha ao inserir.'
#                     continue
#
#         if not lista_import:
#             return make_response(get_json_retorno_metodo(msg='Nenhum Provento Importado.'), 200)
#
#         lista = [[str(row['DATAEX']), str(row['DATAPAGTO']), str(row['TIPO']), str(row['CODIGO']), str(row['QUANTIDADE']).replace('.',''), decimal_prov_to_str(valor=float(row['VLRPRECOBRUTO'])),  decimal_prov_to_str(valor=float(row['VLRPRECO'])), str(row['SITUACAO']), str(row['ID']), str(row['INDEX'])] for row in lista_import]
#
#         return make_response(get_json_retorno_grid(rslt='OK', msg='Arquivo CSV importado com sucesso!', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_proventos.route('/importarcei', methods=['GET', 'POST'])
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
#             codigo = str(row[2]).strip().upper() if row[2] else ''
#             data_ex = str(row[3]).strip() if row[3] else ''
#             data_pagto = str(row[3]).strip() if row[3] else ''
#             tipo = str(row[4]).strip()[0:1] if row[4] else ''
#             quantidade = str(row[5]).strip().replace('.','') if row[5] else ''
#             vlr_preco_bruto = str(row[7]).strip() if row[7] else ''
#             vlr_preco = str(row[8]).strip() if row[8] else ''
#
#             if not data_ex or not data_pagto or not tipo or not codigo or not quantidade: continue
#             if str(data_ex)[0:1] == 'D': continue
#             if str(data_pagto)[0:1] == 'D': continue
#
#             data_ex = str(data_ex).replace('/', '').replace('-', '').ljust(8,'0')
#             data_pagto = str(data_pagto).replace('/', '').replace('-', '').ljust(8,'0')
#
#             data_ex = data_ex[4:8] + data_ex[2:4] + data_ex[0:2]
#             data_pagto = data_pagto[4:8] + data_pagto[2:4] + data_pagto[0:2]
#
#             if str(data_ex) == '00010101': data_ex = '99991231'
#             if str(data_pagto) == '00010101': data_pagto = '99991231'
#
#             indx += 1
#             lista_import.append({'INDEX': str(int(indx)+1), 'ID': '', 'DATAEX': str(data_ex), 'DATAPAGTO': str(data_pagto), 'TIPO': str(tipo), 'CODIGO': str(codigo), 'QUANTIDADE': str(quantidade), 'VLRPRECOBRUTO': str(vlr_preco_bruto), 'VLRPRECO': str(vlr_preco), 'SITUACAO': 'Não Importado'})
#
#             if str(tipo) != "D" and str(tipo) != "R" and str(tipo) != "J" and str(tipo) != "FR":
#                 lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                 continue
#
#             if not vlr_preco_bruto and vlr_preco: vlr_preco_bruto = vlr_preco
#             if not vlr_preco and vlr_preco_bruto: vlr_preco = vlr_preco_bruto
#
#             if not vlr_preco_bruto or str(vlr_preco_bruto) == '' or str(vlr_preco_bruto) == ',' or str(vlr_preco_bruto) == ',0' or str(vlr_preco_bruto) == ',00' or str(vlr_preco_bruto) == '0,00': vlr_preco_bruto = '0,00'
#             if not vlr_preco or str(vlr_preco) == '' or str(vlr_preco) == ',' or str(vlr_preco) == ',0' or str(vlr_preco) == ',00' or str(vlr_preco) == '0,00': vlr_preco = '0,00'
#
#             try:
#                 quantidade = int(float(str(quantidade).replace('.', '').replace(',', '.')))
#                 lista_import[indx]['QUANTIDADE'] = str(quantidade)
#             except:
#                 lista_import[indx]['SITUACAO'] = 'Quantidade não informado ou inválido.'
#                 continue
#
#             try:
#                 vlr_preco_bruto = float(str(vlr_preco_bruto).replace('.', '').replace(',', '.'))
#                 if vlr_preco_bruto > 0.0 and quantidade > 0: vlr_preco_bruto = float(vlr_preco_bruto) / int(quantidade)
#                 vlr_preco_bruto = float(vlr_preco_bruto)
#                 lista_import[indx]['VLRPRECOBRUTO'] = str(vlr_preco_bruto)
#             except:
#                 lista_import[indx]['SITUACAO'] = 'Preço Bruto não informado ou inválido.'
#                 continue
#
#             try:
#                 vlr_preco = float(str(vlr_preco).replace('.', '').replace(',', '.'))
#                 if vlr_preco > 0.0 and quantidade > 0: vlr_preco = float(vlr_preco) / int(quantidade)
#                 vlr_preco = float(vlr_preco)
#                 lista_import[indx]['VLRPRECO'] = str(vlr_preco)
#             except:
#                 lista_import[indx]['SITUACAO'] = 'Preço Liquido não informado ou inválido.'
#                 continue
#
#             if vlr_preco_bruto == 0.0:
#                 lista_import[indx]['SITUACAO'] = 'Preço Bruto não informado.'
#                 continue
#
#             if vlr_preco == 0.0:
#                 lista_import[indx]['SITUACAO'] = 'Preço Liquido não informado..'
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
#                 row = BDREmpresa.get_by_codigo(codigo=str(codigo))
#                 if row:
#                     tipo_invest = 'BDR'
#                     id_ativo = int(row.id)
#
#             if not tipo_invest or not id_ativo:
#                 lista_import[indx]['SITUACAO'] = 'Código não localizado.'
#                 continue
#
#             prov = None
#
#             if str(tipo_invest) == 'ACAO':
#                 if str(tipo) != 'D' and str(tipo) != 'J' and str(tipo) != 'R':
#                     lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                     continue
#                 prov = UsuarioACAOEmpresaProvento()
#                 prov.id_ativo = int(id_ativo)
#                 prov.vlr_preco_bruto = float(vlr_preco_bruto)
#
#             elif str(tipo_invest) == 'FII':
#                 if str(tipo) != 'R' and str(tipo) != 'FR':
#                     lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                     continue
#                 tipo = "R" if str(tipo) == 'FR' else str(tipo)
#                 prov = UsuarioFiiFundoImobProvento()
#                 prov.id_fundo = int(id_ativo)
#
#             elif str(tipo_invest) == 'BDR':
#                 if str(tipo) != 'D' and str(tipo) != 'J' and str(tipo) != 'R':
#                     lista_import[indx]['SITUACAO'] = 'Tipo Inválido.'
#                     continue
#                 prov = UsuarioBDREmpresaProvento()
#                 prov.id_bdr = int(id_ativo)
#                 prov.vlr_preco_bruto = float(vlr_preco_bruto)
#
#             prov.id_usuario = id_usuario
#             prov.tipo = str(tipo)
#             prov.data_ex = str(data_ex)
#             prov.data_pagto = str(data_pagto)
#             prov.quantidade = int(quantidade)
#             prov.vlr_preco =  float(vlr_preco)
#             prov.tot_vlr = prov.calc_total()
#             if str(tipo_invest) == 'ACAO' or str(tipo_invest) == 'BDR':
#                 prov.tot_vlr_bruto = prov.calc_total_bruto()
#             prov.situacao = 'A'
#
#             try:
#                 prov.salvar()
#                 lista_import[indx]['ID'] = str(prov.id)
#                 lista_import[indx]['TIPO'] = prov.tipo_descr()
#                 lista_import[indx]['SITUACAO'] = 'Importado'
#             except:
#                 lista_import[indx]['SITUACAO'] = 'Falha ao inserir.'
#                 continue
#
#         if not lista_import:
#             return make_response(get_json_retorno_grid(msg='Nenhum Provento Importado.'), 200)
#
#         lista = [[str(row['DATAEX']), str(row['DATAPAGTO']), str(row['TIPO']), str(row['CODIGO']), str(row['QUANTIDADE']).replace('.',''), decimal_prov_to_str(valor=float(row['VLRPRECOBRUTO'])),  decimal_prov_to_str(valor=float(row['VLRPRECO'])), str(row['SITUACAO']), str(row['ID']), str(row['INDEX'])] for row in lista_import]
#
#         return make_response(get_json_retorno_grid(rslt='OK', msg='Dados do CEI importado com sucesso!', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_proventos.route('/carregar', methods=['GET', 'POST'])
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
#             id_provento = data.get('IdRent')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_provento: return make_response(get_json_retorno_dados(msg='Id. Provento não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_dados(msg='Código não informado.'), 200)
#
#         tipo_invest = ''
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'ACAO'
#         elif FiiFundoImob.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'FII'
#         elif BDREmpresa.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'BDR'
#
#         if not tipo_invest:
#             return make_response(get_json_retorno_dados(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         prov = None
#
#         if str(tipo_invest) == 'ACAO':
#             prov = UsuarioACAOEmpresaProvento.buscar_por_id(id_usuario=id_usuario, id=int(id_provento))
#         elif str(tipo_invest) == 'FII':
#             prov = UsuarioFiiFundoImobProvento.buscar_por_id(id_usuario=id_usuario, id=int(id_provento))
#         elif str(tipo_invest) == 'BDR':
#             prov = UsuarioBDREmpresaProvento.buscar_por_id(id_usuario=id_usuario, id=int(id_provento))
#
#         if not prov:
#             return make_response(get_json_retorno_dados(msg='Provento não localizado.'), 200)
#
#         dados = dict({})
#
#         if str(tipo_invest) == 'ACAO':
#             dados = dict({
#                 "IdRent": str(prov['ID']),
#                 "Descricao": '',
#                 "Tipo": str(prov['TIPO']),
#                 "Corretora": str(prov['IDCORRETORA']),
#                 "CodAtivo": str(prov['CODIGOATIVO']),
#                 "DataEx": converter_datetime_str(data=converter_str_to_datetime(data=str(prov['DATAEX']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "DataPagto": converter_datetime_str(data=converter_str_to_datetime(data=str(prov['DATAPAGTO']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "Quant": int(prov['QUANTIDADE']),
#                 "CalcVlrLiq": str(prov['CALCVLRLIQUIDO']),
#                 "PrecoBruto": decimal_prov_to_str(valor=prov['VLRPRECOBRUTO']),
#                 "Preco": decimal_prov_to_str(valor=prov['VLRPRECO'])
#             })
#
#         elif str(tipo_invest) == 'FII':
#             dados = dict({
#                 "IdRent": str(prov['ID']),
#                 "Descricao": '',
#                 "Tipo": str(prov['TIPO']),
#                 "Corretora": str(prov['IDCORRETORA']),
#                 "CodAtivo": str(prov['CODIGOFUNDO']),
#                 "DataEx": converter_datetime_str(data=converter_str_to_datetime(data=str(prov['DATAEX']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "DataPagto": converter_datetime_str(data=converter_str_to_datetime(data=str(prov['DATAPAGTO']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "Quant": int(prov['QUANTIDADE']),
#                 "CalcVlrLiq": 'N',
#                 "PrecoBruto": decimal_prov_to_str(valor=prov['VLRPRECO']),
#                 "Preco": decimal_prov_to_str(valor=prov['VLRPRECO'])
#             })
#
#         elif str(tipo_invest) == 'BDR':
#             dados = dict({
#                 "IdRent": str(prov['ID']),
#                 "Descricao": '',
#                 "Tipo": str(prov['TIPO']),
#                 "Corretora": str(prov['IDCORRETORA']),
#                 "CodAtivo": str(prov['CODIGOBDR']),
#                 "DataEx": converter_datetime_str(data=converter_str_to_datetime(data=str(prov['DATAEX']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "DataPagto": converter_datetime_str(data=converter_str_to_datetime(data=str(prov['DATAPAGTO']), fmt='%Y%m%d'),fmt='%Y-%m-%d'),
#                 "Quant": int(prov['QUANTIDADE']),
#                 "CalcVlrLiq": 'N',
#                 "PrecoBruto": decimal_prov_to_str(valor=prov['VLRPRECO']),
#                 "Preco": decimal_prov_to_str(valor=prov['VLRPRECO'])
#             })
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_proventos.route('/excluir', methods=['GET', 'POST'])
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
#             id_provento = data.get('IdRend')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_provento: return make_response(get_json_retorno_metodo(msg='Id. Provento não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Código não informado.'), 200)
#
#         tipo_invest = ''
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'ACAO'
#         elif FiiFundoImob.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'FII'
#         elif BDREmpresa.get_by_codigo(codigo=str(codigo)):
#             tipo_invest = 'BDR'
#
#         if not tipo_invest:
#             return make_response(get_json_retorno_metodo(msg='Código não localizado.'), 200)
#
#         id_usuario = current_user.id
#
#         prov = None
#
#         if str(tipo_invest) == 'ACAO':
#             prov = UsuarioACAOEmpresaProvento.get_by_usuario(id_usuario=id_usuario, id=int(id_provento))
#         elif str(tipo_invest) == 'FII':
#             prov = UsuarioFiiFundoImobProvento.get_by_usuario(id_usuario=id_usuario, id=int(id_provento))
#         elif str(tipo_invest) == 'BDR':
#             prov = UsuarioBDREmpresaProvento.get_by_usuario(id_usuario=id_usuario, id=int(id_provento))
#
#         if not prov: return make_response(get_json_retorno_metodo(msg='Provento não localizado.'), 200)
#
#         prov.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Provento Excluído!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_proventos.route('/excluirtudo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir_tudo():
#     try:
#
#         id_usuario = current_user.id
#
#         UsuarioACAOEmpresaProvento.excluir_tudo(id_usuario=id_usuario)
#         UsuarioFiiFundoImobProvento.excluir_tudo(id_usuario=id_usuario)
#         UsuarioBDREmpresaProvento.excluir_tudo(id_usuario=id_usuario)
#
#         Alerta.registrar(id_usuario=id_usuario, tipo='PERFIL-04', mensagem='Todos os seus proventos foram apagados. <br>IP: ' + str(request.remote_addr))
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Todos os Proventos foram Excluída!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
