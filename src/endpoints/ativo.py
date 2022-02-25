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
# from app.models.usuario_carteira import UsuarioCarteira
# from app.models.usuario_carteira_acao import UsuarioCarteiraAcao
# from app.models.usuario_carteira_fii import UsuarioCarteiraFii
# from app.models.usuario_carteira_etf import UsuarioCarteiraEtf
# from app.models.usuario_carteira_bdr import UsuarioCarteiraBdr
# from app.models.usuario_carteira_cripto import UsuarioCarteiraCripto
# from app.models.usuario_radar_grupo import UsuarioRadarGrupo
# from app.models.usuario_radar_acao import UsuarioRadarAcao
# from app.models.usuario_radar_fii import UsuarioRadarFii
# from app.models.usuario_radar_etf import UsuarioRadarEtf
# from app.models.usuario_radar_bdr import UsuarioRadarBdr
# from app.models.usuario_radar_cripto import UsuarioRadarCripto
# from app.util.util_json import get_json_retorno_grid, get_json_retorno_metodo, get_json_retorno_dados
# from app.util.util_formatacao import decimal_to_str, decimal_cripto_to_str, decimal_prov_to_str


router = _fastapi.APIRouter(prefix="/ativo", tags=['ativo'])


# @bp_ativo.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# # @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     return render_template(template_name_or_list="ativo.html")
#
#
# @bp_ativo.route('/grid', methods=['GET', 'POST'])
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
#             id = data.get('IdGrupo')
#         except:
#             return make_response(get_json_retorno_grid(msg='Dados não informado!'), 200)
#
#         id_usuario = current_user.id
#
#         lista = []
#         if not id:
#
#             rows = UsuarioCarteiraAcao.buscar_dados_grid_radar(id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOATIVO']), str(row['RAZAOSOCIAL']), decimal_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(0), str(0) ] for row in rows]
#
#             rows = UsuarioCarteiraFii.buscar_dados_grid_radar(id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOATIVO']), str(row['RAZAOSOCIAL']), decimal_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(0), str(0) ] for row in rows]
#
#             rows = UsuarioCarteiraEtf.buscar_dados_grid_radar(id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOATIVO']), str(row['RAZAOSOCIAL']), decimal_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(0), str(0) ] for row in rows]
#
#             rows = UsuarioCarteiraBdr.buscar_dados_grid_radar(id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOBDR']), str(row['RAZAOSOCIAL']), decimal_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(0), str(0)] for row in rows]
#
#             rows = UsuarioCarteiraCripto.buscar_dados_grid_radar(id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOATIVO']), str(row['RAZAOSOCIAL']), decimal_cripto_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(0), str(0) ] for row in rows]
#
#         else:
#
#             rows = UsuarioRadarAcao.buscar_dados_grid(id_grupo=id, id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOATIVO']), str(row['RAZAOSOCIAL']), decimal_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(row['IDUSERGRUPO']), str(row['IDUSERATIVO']) ] for row in rows            ]
#
#             rows = UsuarioRadarFii.buscar_dados_grid(id_grupo=id, id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOATIVO']), str(row['RAZAOSOCIAL']), decimal_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(row['IDUSERGRUPO']), str(row['IDUSERATIVO']) ] for row in rows]
#
#             rows = UsuarioRadarEtf.buscar_dados_grid(id_grupo=id, id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOATIVO']), str(row['RAZAOSOCIAL']), decimal_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(row['IDUSERGRUPO']), str(row['IDUSERATIVO']) ] for row in rows]
#
#             rows = UsuarioRadarBdr.buscar_dados_grid(id_grupo=id, id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOBDR']), str(row['RAZAOSOCIAL']), decimal_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(row['IDUSERGRUPO']), str(row['IDUSERATIVO']) ] for row in rows]
#
#             rows = UsuarioRadarCripto.buscar_dados_grid(id_grupo=id, id_usuario=id_usuario)
#             lista += [[str(row['DESCRICAOSETOR']), str(row['DESCRICAOSUBSETOR']), str(row['DESCRICAOSEGMENTO']), str(row['CODIGOCRIPTO']), str(row['RAZAOSOCIAL']), decimal_cripto_to_str(valor=row['PRECO']), decimal_to_str(valor=row['VARIACAO']), str(row['IDUSERGRUPO']), str(row['IDUSERATIVO']) ] for row in rows]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_ativo.route('/carregargrupo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar_grupo():
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
#             id = data.get('IdGrupo')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id:
#             return make_response(get_json_retorno_dados(msg='Id Grupo Radar não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         grupo = UsuarioRadarGrupo.get_by_id_and_id_usuario(id=id, id_usuario=id_usuario)
#         if not grupo:
#             return make_response(get_json_retorno_dados(msg='Grupo de Radar não localizado.'), 200)
#
#         dados = dict({"Id": str(grupo.id), "Nome": grupo.descricao})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_ativo.route('/salvargrupo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_grupo():
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
#             id = data.get('Id')
#             nome = data.get('Nome')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if str(id).strip() == '': id = None
#         if not nome: return make_response(get_json_retorno_metodo(msg='Nome não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         if not id:
#             if UsuarioRadarGrupo.get_by_descricao(id_usuario=id_usuario, descricao=nome):
#                 return make_response(get_json_retorno_metodo(msg='Nome do Grupo já cadastrado.'), 200)
#             grupo = UsuarioRadarGrupo(id_usuario=id_usuario)
#         else:
#             grupo = UsuarioRadarGrupo.get_by_id_and_id_usuario(id=id, id_usuario=id_usuario)
#
#         if not grupo:
#             return make_response(get_json_retorno_metodo(msg='Grupo de Radar não localizado.'), 200)
#
#         grupo.descricao = nome
#         grupo.situacao = 'A'  # A-Ativo
#         grupo.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_ativo.route('/salvarativo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_ativo():
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
#             id = data.get('IdGrupo')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id:
#             return make_response(get_json_retorno_metodo(msg='Id Grupo não informado.'), 200)
#
#         if not codigo:
#             return make_response(get_json_retorno_metodo(msg='Código do Ativo não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         if not UsuarioRadarGrupo.get_by_id_and_id_usuario(id=id, id_usuario=id_usuario):
#             return make_response(get_json_retorno_metodo(msg='Grupo de Radar não localizado.'), 200)
#
#         empresa_ativo = ACAOEmpresaAtivo.get_by_codigo(codigo=codigo)
#         if empresa_ativo:
#             id_ativo = empresa_ativo.id
#             if UsuarioRadarAcao.get_by_ativo(id_grupo=id, id_ativo=id_ativo):
#                 return make_response(get_json_retorno_metodo(msg='Ativo já cadastrado para esse Grupo.'), 200)
#             grupo_item = UsuarioRadarAcao(id_grupo=id, id_ativo=id_ativo, situacao='A')
#             grupo_item.salvar()
#             return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#         fii_fundoimob = FiiFundoImob.get_by_codigo(codigo=codigo)
#         if fii_fundoimob:
#             id_fundo = fii_fundoimob.id
#             if UsuarioRadarFii.get_by_fundo(id_grupo=id, id_fundo=id_fundo):
#                 return make_response(get_json_retorno_metodo(msg='Fundo já cadastrado para esse Grupo.'), 200)
#             grupo_item = UsuarioRadarFii(id_grupo=id, id_fundo=id_fundo, situacao='A')
#             grupo_item.salvar()
#             return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#         etf_indice = ETFIndice.get_by_codigo(codigo=codigo)
#         if etf_indice:
#             id_indice = etf_indice.id
#             if UsuarioRadarEtf.get_by_indice(id_grupo=id, id_indice=id_indice):
#                 return make_response(get_json_retorno_metodo(msg='ETF já cadastrado para esse Grupo.'), 200)
#             grupo_item = UsuarioRadarEtf(id_grupo=id, id_indice=id_indice, situacao='A')
#             grupo_item.salvar()
#             return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#         empresa_bdr = BDREmpresa.get_by_codigo(codigo=codigo)
#         if empresa_bdr:
#             id_bdr = empresa_bdr.id
#             if UsuarioRadarBdr.get_by_ativo(id_grupo=id, id_bdr=id_bdr):
#                 return make_response(get_json_retorno_metodo(msg='Ativo já cadastrado para esse Grupo.'), 200)
#             grupo_item = UsuarioRadarBdr(id_grupo=id, id_bdr=id_bdr, situacao='A')
#             grupo_item.salvar()
#             return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#         cripto = CriptoEmpresa.get_by_codigo(codigo=codigo)
#         if cripto:
#             id_cripto = cripto.id
#             if UsuarioRadarCripto.get_by_cripto(id_grupo=id, id_cripto=id_cripto):
#                 return make_response(get_json_retorno_metodo(msg='Cripto já cadastrada para esse Grupo.'), 200)
#             grupo_item = UsuarioRadarCripto(id_grupo=id, id_cripto=id_cripto, situacao='A')
#             grupo_item.salvar()
#             return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#         return make_response(get_json_retorno_metodo(msg='Código do Ativo não localizado.'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_ativo.route('/excluirgrupo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir_grupo():
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
#             id = data.get('IdGrupo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id:
#             return make_response(get_json_retorno_metodo(msg='Id Grupo Radar não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         grupo = UsuarioRadarGrupo.get_by_id_and_id_usuario(id=id, id_usuario=id_usuario)
#         if not grupo:
#             return make_response(get_json_retorno_metodo(msg='Grupo de Radar não localizado.'), 200)
#
#         grupo.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_ativo.route('/excluirativo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def excluir_ativo():
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
#             id_grupo = data.get('IdUserGrupo')
#             id = data.get('IdUserAtivo')
#             codigo = data.get('CodAtivo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_grupo: return make_response(get_json_retorno_metodo(msg='Id Grupo Radar não informado.'), 200)
#         if not id: return make_response(get_json_retorno_metodo(msg='Id. Ativo não informado.'), 200)
#         if not codigo: return make_response(get_json_retorno_metodo(msg='Código do Ativo não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         grupo = UsuarioRadarGrupo.get_by_id_and_id_usuario(id=id_grupo, id_usuario=id_usuario)
#         if not grupo: return make_response(get_json_retorno_metodo(msg='Grupo de Radar não localizado.'), 200)
#
#         grupo_item = None
#
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=codigo):
#             grupo_item = UsuarioRadarAcao.get_by_id_grupo(id_grupo=id_grupo, id=id)
#
#         elif FiiFundoImob.get_by_codigo(codigo=codigo):
#             grupo_item = UsuarioRadarFii.get_by_id_grupo(id_grupo=id_grupo, id=id)
#
#         elif ETFIndice.get_by_codigo(codigo=codigo):
#             grupo_item = UsuarioRadarEtf.get_by_id_grupo(id_grupo=id_grupo, id=id)
#
#         elif BDREmpresa.get_by_codigo(codigo=codigo):
#             grupo_item = UsuarioRadarBdr.get_by_id_grupo(id_grupo=id_grupo, id=id)
#
#         elif CriptoEmpresa.get_by_codigo(codigo=codigo):
#             grupo_item = UsuarioRadarCripto.get_by_id_grupo(id_grupo=id_grupo, id=id)
#
#         if not grupo_item:
#             return make_response(get_json_retorno_metodo(msg='Código do Ativo não localizado.'), 200)
#
#         grupo_item.excluir()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
