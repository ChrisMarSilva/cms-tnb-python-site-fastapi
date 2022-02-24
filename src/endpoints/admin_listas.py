# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# from app.optimize import flask_optimize
# from app.models.alerta import Alerta
# from app.models.acao_empresa import ACAOEmpresa
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.acao_empresa_setor import ACAOEmpresaSetor
# from app.models.acao_empresa_subsetor import ACAOEmpresaSubSetor
# from app.models.acao_empresa_segmento import ACAOEmpresaSegmento
# from app.models.fii_fundoimob import FiiFundoImob
# from app.models.fii_fundoimob_tipo import FiiFundoImobTipo
# from app.models.fii_fundoimob_admin import FiiFundoImobAdmin
# from app.models.etf_indice import ETFIndice
# from app.models.bdr_empresa import BDREmpresa
# from app.models.bdr_empresa_setor import BDREmpresaSetor
# from app.models.bdr_empresa_subsetor import BDREmpresaSubSetor
# from app.models.bdr_empresa_segmento import BDREmpresaSegmento
# from app.models.cripto_empresa import CriptoEmpresa
# from app.models.corretora_lista import CorretoraLista
# from app.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamento
# from app.models.usuario_acao_empresa_operacao import UsuarioACAOEmpresaOperacao
# from app.models.usuario_acao_empresa_provento import UsuarioACAOEmpresaProvento
# from app.models.usuario_fii_fundoimob_provento import UsuarioFiiFundoImobProvento
# from app.models.usuario_bdr_empresa_provento import UsuarioBDREmpresaProvento
# from app.models.usuario_corretora import UsuarioCorretora
# from app.models.usuario_carteira import UsuarioCarteira
# from app.models.usuario_carteira_projecao import UsuarioCarteiraProjecao
# from app.models.usuario_radar_grupo import UsuarioRadarGrupo
# from app.models.usuario_radar_acao import UsuarioRadarAcao
# from app.models.usuario_radar_fii import UsuarioRadarFii
# from app.models.usuario_radar_etf import UsuarioRadarEtf
# from app.models.usuario_radar_bdr import UsuarioRadarBdr
# from app.models.usuario_radar_cripto import UsuarioRadarCripto
# from app.models.usuario_alerta_assinatura import UsuarioAlertaAssinatura
# from app.models.usuario_cei_oper import UsuarioCeiOper
# from app.models.usuario_cei_prov import UsuarioCeiProv
# from app.models.log_erro import LogErro
# from app.util.util_datahora import pegar_data_atual
# from app.util.util_json import get_json_retorno_lista
#
#
# bp_admin_listas = Blueprint('admin_listas', __name__, url_prefix='/listas')
#
#
# @bp_admin_listas.route('/lista_codigo_completo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_codigo_completo():
#     try:
#         rows = ACAOEmpresaAtivo.buscar_todos_codigos_com_fiis_etfs_bdrs_criptos()
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['TIPO']), str(row['ID']), str(row['NOME'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_completo_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_codigo_completo_acao():
#     try:
#         rows = ACAOEmpresaAtivo.get_all_codigos()
#         lista = [[str(row.codigo), str(row.codigo)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_completo_fii', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_codigo_completo_fii():
#     try:
#         rows = FiiFundoImob.get_lista_codigos()
#         lista = [[str(row.codigo), str(row.codigo), str(row.id)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_completo_etf', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_codigo_completo_etf():
#     try:
#         rows = ETFIndice.get_lista_codigos()
#         lista = [[str(row.codigo), str(row.codigo), str(row.id)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_completo_cripto', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_codigo_completo_cripto():
#     try:
#         rows = CriptoEmpresa.get_lista_codigos()
#         lista = [[str(row.codigo), str(row.codigo), str(row.id), str(row.nome)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_completo_bdr', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_codigo_completo_bdr():
#     try:
#         rows = BDREmpresa.get_all_codigos()
#         lista = [[str(row.codigo), str(row.codigo)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_comprado', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_comprado():
#     try:
#         id_usuario = current_user.id
#         rows = ACAOEmpresaAtivo.buscar_todos_codigos_comprados_com_fiis_etfs_bdrs_criptos(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID']), str(row['TIPO']), str(row['NOME'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_comprado_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_comprado_acao():
#     try:
#         id_usuario = current_user.id
#         rows = ACAOEmpresaAtivo.buscar_todos_codigos_comprados(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_comprado_fii', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_comprado_fii():
#     try:
#         id_usuario = current_user.id
#         rows = FiiFundoImob.buscar_todos_codigos_comprados(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_comprado_etf', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_comprado_etf():
#     try:
#         id_usuario = current_user.id
#         rows = ETFIndice.buscar_todos_codigos_comprados(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_comprado_bdr', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_comprado_bdr():
#     try:
#         id_usuario = current_user.id
#         rows = BDREmpresa.buscar_todos_codigos_comprados(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_comprado_cripto', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_comprado_cripto():
#     try:
#         id_usuario = current_user.id
#         rows = CriptoEmpresa.buscar_todos_codigos_comprados(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID']), str(row['NOME'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_comprado_para_proventos', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_comprado_para_proventos():
#     try:
#         id_usuario = current_user.id
#         rows = ACAOEmpresaAtivo.buscar_todos_codigos_comprados_com_fiis_bdrs(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID']), str(row['TIPO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_provento', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_provento():
#     try:
#         id_usuario = current_user.id
#         rows = ACAOEmpresaAtivo.buscar_todos_codigos_proventos_com_fiis_bdrs(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID']), str(row['TIPO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_provento_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_provento_acao():
#     try:
#         id_usuario = current_user.id
#         rows = ACAOEmpresaAtivo.buscar_todos_codigos_proventos(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_provento_fii', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_provento_fii():
#     try:
#         id_usuario = current_user.id
#         rows = FiiFundoImob.buscar_todos_codigos_proventos(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_provento_bdr', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_provento_bdr():
#     try:
#         id_usuario = current_user.id
#         rows = BDREmpresa.buscar_todos_codigos_proventos(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['ID'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_aluguel_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_aluguel_acao():
#     try:
#         id_usuario = current_user.id
#         rows = ACAOEmpresaAtivo.buscar_todos_codigos_aluguel(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_radar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_radar():
#     try:
#         lista = []
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_radar_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_radar_acao():
#     try:
#         lista = []
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_radar_fii', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_radar_fii():
#     try:
#         lista = []
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_radar_etf', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_radar_etf():
#     try:
#         lista = []
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_radar_bdr', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_radar_bdr():
#     try:
#         lista = []
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_radar_cripto', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_codigo_user_radar_cripto():
#     try:
#         lista = []
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_setor_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_setor_acao():
#     try:
#         rows = ACAOEmpresaSetor.buscar_lista()  # buscar_lista_cotacao
#         lista = [[str(row['ID']), str(row['DESCRICAO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_subsetor_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_subsetor_acao():
#     try:
#         rows = ACAOEmpresaSubSetor.buscar_lista()  # buscar_lista_cotacao
#         lista = [[str(row['ID']), str(row['DESCRICAO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_segmento_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_segmento_acao():
#     try:
#         rows = ACAOEmpresaSegmento.buscar_lista()  # buscar_lista_cotacao
#         lista = [[str(row['ID']), str(row['DESCRICAO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_setor_bdr', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_setor_bdr():
#     try:
#         rows = BDREmpresaSetor.buscar_lista()  # buscar_lista_cotacao
#         lista = [[str(row['ID']), str(row['DESCRICAO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_subsetor_bdr', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_subsetor_bdr():
#     try:
#         rows = BDREmpresaSubSetor.buscar_lista()  # buscar_lista_cotacao
#         lista = [[str(row['ID']), str(row['DESCRICAO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_segmento_bdr', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_segmento_bdr():
#     try:
#         rows = BDREmpresaSegmento.buscar_lista()  # buscar_lista_cotacao
#         lista = [[str(row['ID']), str(row['DESCRICAO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_corretora_user', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_corretora_user():
#     try:
#         id_usuario = current_user.id
#         rows = UsuarioCorretora.get_nomes(id_usuario=id_usuario)
#         lista = [[str(row.id), str(row.nome)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_corretora_geral', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_corretora_geral():
#     try:
#         rows = CorretoraLista.get_nomes()
#         lista = [[str(row.id), str(row.nome)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_corretora_geral_user_cadastrada', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_corretora_geral_user_cadastrada():
#     try:
#         id_usuario = current_user.id
#         rows = CorretoraLista.buscar_lista_nome_cadastradas(id_usuario=id_usuario)
#         lista = [[str(row['ID']), str(row['NOME'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_corretora_geral_user_nao_cadastrada', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_corretora_geral_user_nao_cadastrada():
#     try:
#         id_usuario = current_user.id
#         rows = CorretoraLista.buscar_lista_nome_nao_cadastradas(id_usuario=id_usuario)
#         lista = [[str(row['ID']), str(row['NOME'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_empresa_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_nomes_empresa_acao():
#     try:
#         rows = ACAOEmpresa.get_lista_razao_social()
#         lista = [[str(row.id), str(row.nome_resumido)] for row in rows]  # razao_social
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_empresa_fii', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_nomes_empresa_fii():
#     try:
#         rows = FiiFundoImob.get_lista_nomes()
#         lista = [[str(row.id), str(row.nome), str(row.nome)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_empresa_etf', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_nomes_empresa_etf():
#     try:
#         rows = ETFIndice.get_lista_nomes()
#         lista = [[str(row.id), str(row.nome), str(row.nome)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_empresa_bdr', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_nomes_empresa_bdr():
#     try:
#         rows = BDREmpresa.get_lista_razao_social()
#         lista = [[str(row.id), str(row.nome)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_empresa_cripto', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_nomes_empresa_cripto():
#     try:
#         rows = CriptoEmpresa.get_lista_nomes()
#         lista = [[str(row.id), str(row.nome)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_carteira_user', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_nomes_carteira_user():
#     try:
#         id_usuario = current_user.id
#         rows = UsuarioCarteira.get_lista_nome(id_usuario=id_usuario)
#         lista = [[str(row.id), str(row.descricao)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_radar_user', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista_nomes_radar_user():
#     try:
#
#         id_usuario = current_user.id
#         rows = UsuarioRadarGrupo.get_descricoes_by_usuario(id_usuario=id_usuario)
#
#         lista = []
#         for row in rows:
#             qtde = 0
#             for result in UsuarioRadarAcao.buscar_quant_grupo(id_grupo=row.id, id_usuario=id_usuario): qtde += int(result['QTDE'])
#             for result in UsuarioRadarFii.buscar_quant_grupo(id_grupo=row.id, id_usuario=id_usuario): qtde += int(result['QTDE'])
#             for result in UsuarioRadarEtf.buscar_quant_grupo(id_grupo=row.id, id_usuario=id_usuario): qtde += int(result['QTDE'])
#             for result in UsuarioRadarBdr.buscar_quant_grupo(id_grupo=row.id, id_usuario=id_usuario): qtde += int(result['QTDE'])
#             for result in UsuarioRadarCripto.buscar_quant_grupo(id_grupo=row.id, id_usuario=id_usuario): qtde += int(result['QTDE'])
#             lista.append([str(row.id), str(row.descricao), str(qtde)])
#
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_projecao_user', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-10')  # 10seg
# def lista_nomes_projecao_user():
#     try:
#         id_usuario = current_user.id
#         rows = UsuarioCarteiraProjecao.get_all_by_usuario(id_usuario=id_usuario)
#         lista = [[str(row.id), str(row.descricao)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_users_com_alerta', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_users_com_alerta():
#     try:
#         rows = Alerta.buscar_lista_user()
#         lista = [[str(row['ID']), str(row['NOME']), str(row['NOME'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_users_com_assinatura_alerta', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_users_com_assinatura_alerta():
#     try:
#         rows = UsuarioAlertaAssinatura.buscar_lista_user()
#         lista = [[str(row['ID']), str(row['NOME']), str(row['NOME'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_operacao_cei', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_codigo_user_operacao_cei():
#     try:
#         id_usuario = current_user.id
#         rows = UsuarioCeiOper.buscar_lista_codigo(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['CODIGO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_codigo_user_provento_cei', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_codigo_user_provento_cei():
#     try:
#         id_usuario = current_user.id
#         rows = UsuarioCeiProv.buscar_lista_codigo(id_usuario=id_usuario)
#         lista = [[str(row['CODIGO']), str(row['CODIGO']), str(row['CODIGO'])] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_tipos_fii', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_nomes_tipos_fii():
#     try:
#         rows = FiiFundoImobTipo.get_lista_nomes()
#         lista = [[str(row.id), str(row.descricao)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_nomes_admins_fii', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-1800')  # 1800seg/30Min
# def lista_nomes_admins_fii():
#     try:
#         rows = FiiFundoImobAdmin.get_lista_nomes()
#         lista = [[str(row.id), str(row.nome)] for row in rows]
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_anos_user_lancamentos_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-10')  # 10seg
# def lista_anos_user_lancamentos_acao():
#     try:
#
#         id_usuario = current_user.id
#         anos = []
#         anos.append(pegar_data_atual(fmt='%Y'))
#         anos.append(UsuarioACAOEmpresaLancamento.get_menor_ano(id_usuario=id_usuario)[0])
#
#         menor = min(int(str(ano)[:4]) for ano in anos if ano is not None and str(ano).strip() != '')
#         maior = max(int(str(ano)[:4]) for ano in anos if ano is not None and str(ano).strip() != '')
#
#         lista = [str(ano) for ano in range(menor, maior + 1)]
#
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_anos_user_operacao_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-10')  # 10seg
# def lista_anos_user_operacao_acao():
#     try:
#
#         id_usuario = current_user.id
#
#         anos = []
#         anos.append(pegar_data_atual(fmt='%Y'))
#         anos.append(UsuarioACAOEmpresaOperacao.get_menor_ano(id_usuario=id_usuario)[0])
#
#         menor = min(int(str(ano)[:4]) for ano in anos if ano is not None and str(ano).strip() != '')
#         maior = max(int(str(ano)[:4]) for ano in anos if ano is not None and str(ano).strip() != '')
#
#         lista = [str(ano) for ano in range(menor, maior + 1)]
#
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_anos_user_provento', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-10')  # 10seg
# def lista_anos_user_provento():
#     try:
#
#         id_usuario = current_user.id
#
#         anos = []
#         anos.append(pegar_data_atual(fmt='%Y'))
#         anos.append(UsuarioACAOEmpresaProvento.get_menor_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioACAOEmpresaProvento.get_maior_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioFiiFundoImobProvento.get_menor_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioFiiFundoImobProvento.get_maior_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioBDREmpresaProvento.get_menor_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioBDREmpresaProvento.get_maior_ano(id_usuario=id_usuario)[0])
#
#         menor = min(int(str(ano)[:4]) for ano in anos if ano is not None and str(ano).strip() != '')
#         maior = max(int(str(ano)[:4]) for ano in anos if ano is not None and str(ano).strip() != '')
#
#         lista = [str(ano) for ano in range(menor, maior + 1)]
#
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_listas.route('/lista_anos_user_provento_acao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json', cache='GET-10')  # 10seg
# def lista_anos_user_provento_acao():
#     try:
#
#         id_usuario = current_user.id
#
#         anos = []
#         anos.append(pegar_data_atual(fmt='%Y'))
#         anos.append(UsuarioACAOEmpresaProvento.get_menor_ano(id_usuario=id_usuario)[0])
#         anos.append(UsuarioACAOEmpresaProvento.get_maior_ano(id_usuario=id_usuario)[0])
#
#         menor = min(int(str(ano)[:4]) for ano in anos if ano is not None and str(ano).strip() != '')
#         maior = max(int(str(ano)[:4]) for ano in anos if ano is not None and str(ano).strip() != '')
#
#         lista = [str(ano) for ano in range(menor, maior + 1)]
#
#         return make_response(get_json_retorno_lista(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
