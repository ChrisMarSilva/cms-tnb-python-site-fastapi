# # -*- coding: utf-8 -*-
# import sys
# import os
# from flask import Blueprint, render_template, make_response, request
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.alerta import Alerta
# from app.models.usuario import Usuario
# from app.models.usuario_cei import UsuarioCei
# from app.models.usuario_cei_oper import UsuarioCeiOper
# from app.models.usuario_cei_prov import UsuarioCeiProv
# from app.util.util_json import get_json_retorno_dados, get_json_retorno_metodo, get_json_retorno_grid
# from app.util.util_datahora import pegar_data_hora_atual
# from app.util.util_formatacao import decimal_to_str, inteiro_to_str
#
#
# bp_cei = Blueprint('cei', __name__, url_prefix='/cei')
#
#
# @bp_cei.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# # @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     user_cpf = ''
#     user_dthr = ''
#     user_sit = 'I'
#     title_cor = 'text-danger'
#     id_usuario = current_user.id
#     usuario_cei = UsuarioCei.get_by_usuario(id_usuario=id_usuario)
#     if usuario_cei:
#         user_cpf = usuario_cei.cpf
#         user_dthr = usuario_cei.dthr_alteracao_format()
#         user_sit = usuario_cei.situacao
#         if user_dthr != '':
#             title_cor = 'text-success'
#     return render_template(template_name_or_list="cei.html", user_cpf=user_cpf, user_dthr=user_dthr, user_sit=user_sit, title_cor=title_cor)
#
#
# @bp_cei.route('/salvar', methods=['GET', 'POST'])
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
#         if not data: return make_response(get_json_retorno_dados(msg='Dados n??o informado!'), 200)
#
#         try:
#             cpf = data.get('txtCPF')
#             senha = data.get('txtSenha')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados n??o informado!'), 200)
#
#         if cpf is None:
#             cpf = ''
#
#         if senha is None:
#             senha = ''
#
#         id_usuario = current_user.id
#
#         usuario = Usuario.get_by_id(id=id_usuario)
#         if not usuario:
#             return make_response(get_json_retorno_dados(msg='Usu??rio n??o encontrado!.'), 200)
#
#         usuario_cei = UsuarioCei.get_by_usuario(id_usuario=id_usuario)
#         if not usuario_cei:
#             usuario_cei = UsuarioCei(id_usuario=id_usuario, dthr_registro=pegar_data_hora_atual(fmt='%Y%m%d%H%M%S'), tipo='C')  # C- Carregar/SomenteImportar
#
#         usuario_cei.cpf = cpf
#         usuario_cei.senha = senha
#         usuario_cei.situacao = 'A'  # A-Ativo
#         if cpf == '' or senha == '':
#             usuario_cei.cpf = ''
#             usuario_cei.senha = ''
#             usuario_cei.situacao = 'I'  # I-Inativo
#         usuario_cei.salvar()
#
#         if usuario_cei.situacao == 'A': Alerta.registrar(id_usuario=id_usuario, tipo='CEI-01', mensagem='Sua integra????o foi ativada. <br>IP: ' + str(request.remote_addr))
#         if usuario_cei.situacao == 'I': Alerta.registrar(id_usuario=id_usuario, tipo='CEI-01', mensagem='Sua integra????o foi inativada. <br>IP: ' + str(request.remote_addr))
#
#         dados = dict({"Cpf": str(usuario_cei.cpf), "Sit": str(usuario_cei.situacao)})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_cei.route('/grid', methods=['GET', 'POST'])
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
#         if not data: return make_response(get_json_retorno_grid(msg='Dados n??o informado!'), 200)
#
#         try:
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#             cod_ativo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados n??o informado!'), 200)
#
#         if dt_ini: dt_ini = str(dt_ini).replace('-', '')
#         if dt_fim: dt_fim = str(dt_fim).replace('-', '')
#
#         categoria = ''
#         if cod_ativo and cod_ativo == 'ACAO': categoria = 'A'
#         if cod_ativo and cod_ativo == 'FII': categoria = 'F'
#         if cod_ativo and cod_ativo == 'ETF': categoria = 'E"'
#         if categoria: cod_ativo = '"'
#
#         id_usuario = current_user.id
#
#         rows = UsuarioCeiOper.buscar_todos(id_usuario=id_usuario, dt_ini=dt_ini, dt_fim=dt_fim, codigo=cod_ativo, categoria=categoria)
#
#         lista = [
#             [
#                 '',
#                 str(row['DATA']),
#                 UsuarioCeiOper.descricao_tipo(tipo=row['TIPO']),
#                 str(row['CODIGO']),
#                 inteiro_to_str(valor=row['QUANT']).replace(',00', '').replace('.', ''),
#                 decimal_to_str(valor=row['PRECO']),
#                 decimal_to_str(valor=row['TOTAL']),
#                 str(row['CORRET_NOME']),
#                 UsuarioCeiOper.descricao_situacao(situacao=row['SITUACAO']),
#                 str(row['ID']),
#                 str(row['SITUACAO'])
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
# @bp_cei.route('/alterarsituacao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def alterar_situacao():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         try:
#             id_oper = data.get('IdOper')
#             id_sit = data.get('IdSit')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         if not id_oper:
#             return make_response(get_json_retorno_metodo(msg='Id Oper. n??o informado!'), 200)
#
#         if not id_sit:
#             return make_response(get_json_retorno_metodo(msg='Situa????o n??o informada!'), 200)
#
#         id_usuario = current_user.id
#
#         row = UsuarioCeiOper.buscar_por_id_oper(id_usuario=id_usuario, id=id_oper)
#         if not row:
#             return make_response(get_json_retorno_metodo(msg='"Opera????o n??o localizada!'), 200)
#
#         UsuarioCeiOper.atualizar_situacao(id_usuario=id_usuario, id=id_oper, situacao=id_sit)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_cei.route('/alterarlistasituacao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def alterar_lista_situacao():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         try:
#             id_sit = data.get('IdSit')
#             lista_id_oper = data.getlist('LstIdOper[]')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         if not lista_id_oper:
#             return make_response(get_json_retorno_metodo(msg='Id Oper. n??o informado!'), 200)
#
#         if not id_sit:
#             return make_response(get_json_retorno_metodo(msg='Situa????o n??o informada!'), 200)
#
#         id_usuario = current_user.id
#
#         for id_oper in lista_id_oper:
#             row = UsuarioCeiOper.buscar_por_id_oper(id_usuario=id_usuario, id=id_oper)
#             if not row:
#                 return make_response(get_json_retorno_metodo(msg='"Opera????o n??o localizada!'), 200)
#             UsuarioCeiOper.atualizar_situacao(id_usuario=id_usuario, id=id_oper, situacao=id_sit)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_cei.route('/gridprov', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
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
#         if not data: return make_response(get_json_retorno_grid(msg='Dados n??o informado!'), 200)
#
#         try:
#             dt_ini = data.get('DataIni')
#             dt_fim = data.get('DataFim')
#             cod_ativo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados n??o informado!'), 200)
#
#         if dt_ini: dt_ini = str(dt_ini).replace('-', '')
#         if dt_fim: dt_fim = str(dt_fim).replace('-', '')
#
#         categoria = ''
#         if cod_ativo and cod_ativo == 'ACAO': categoria = 'A'
#         if cod_ativo and cod_ativo == 'FII': categoria = 'F'
#         if cod_ativo and cod_ativo == 'ETF': categoria = 'E"'
#         if categoria: cod_ativo = ''
#
#         id_usuario = current_user.id
#
#         rows = UsuarioCeiProv.buscar_todos(id_usuario=id_usuario, dt_ini=dt_ini, dt_fim=dt_fim, codigo=cod_ativo, categoria=categoria)
#
#         lista = [
#             [
#                 '',
#                 str(row['DATA_PAGTO']),
#                 UsuarioCeiProv.descricao_tipo(tipo=row['TIPO']),
#                 str(row['CODIGO']),
#                 inteiro_to_str(valor=row['QUANT']).replace(',00', '').replace('.', ''),
#                 decimal_to_str(valor=row['TOTAL_BRUTO']),
#                 decimal_to_str(valor=row['TOTAL_LIQUIDO']),
#                 str(row['CORRET_NOME']),
#                 UsuarioCeiProv.descricao_situacao(situacao=row['SITUACAO']),
#                 str(row['ID']),
#                 str(row['SITUACAO'])
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
# @bp_cei.route('/alterarsituacaoprov', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def alterar_situacao_prov():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         try:
#             id_prov = data.get('IdProv')
#             id_sit = data.get('IdSit')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         if not id_prov:
#             return make_response(get_json_retorno_metodo(msg='Id Prov. n??o informado!'), 200)
#
#         if not id_sit:
#             return make_response(get_json_retorno_metodo(msg='Situa????o n??o informada!'), 200)
#
#         id_usuario = current_user.id
#
#         row = UsuarioCeiProv.buscar_por_id_prov(id_usuario=id_usuario, id=id_prov)
#         if not row:
#             return make_response(get_json_retorno_metodo(msg='"Provento n??o localizado!'), 200)
#
#         UsuarioCeiProv.atualizar_situacao(id_usuario=id_usuario, id=id_prov, situacao=id_sit)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_cei.route('/alterarlistasituacaoprov', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def alterar_lista_situacao_prov():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         try:
#             id_sit = data.get('IdSit')
#             lista_id_prov = data.getlist('LstIdProv[]')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados n??o informado!'), 200)
#
#         if not lista_id_prov:
#             return make_response(get_json_retorno_metodo(msg='Id Prov. n??o informado!'), 200)
#
#         if not id_sit:
#             return make_response(get_json_retorno_metodo(msg='Situa????o n??o informada!'), 200)
#
#         id_usuario = current_user.id
#
#         for id_prov in lista_id_prov:
#             row = UsuarioCeiProv.buscar_por_id_prov(id_usuario=id_usuario, id=id_prov)
#             if not row:
#                 return make_response(get_json_retorno_metodo(msg='"Provento n??o localizado!'), 200)
#             UsuarioCeiProv.atualizar_situacao(id_usuario=id_usuario, id=id_prov, situacao=id_sit)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
