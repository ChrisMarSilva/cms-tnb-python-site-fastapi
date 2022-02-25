# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.acao_empresa import ACAOEmpresa
# from app.models.acao_empresa_ativo import ACAOEmpresaAtivo
# from app.models.acao_empresa_ativo_cotacao import ACAOEmpresaAtivoCotacao
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados, get_json_retorno_grid
# from app.util.util_datahora import pegar_data_atual, pegar_data_hora_atual


router = _fastapi.APIRouter(prefix="/empresa", tags=['admin_empresa'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @login_required
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
async def get_index():
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="admin_empresa.html")
    return {"result": "ok"}


# @bp_admin_empresa.route('/grid', methods=['GET', 'POST'])
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
#         rows = ACAOEmpresa.buscar_todos_completo(id_usuario=id_usuario, setor=setor, subsetor=subsetor, segmento=segmento, codigo=codigo, tipo=tipo)
#
#         lista = [
#             [
#                 str(row['CODIGOATIVO']) if row['CODIGOATIVO'] else '',
#                 str(row['NOME']),
#                 str(row['RAZAOSOCIAL']),
#                 str(row['DESCRICAOSETOR'])[0:20] if row['DESCRICAOSETOR'] else '',
#                 str(row['DESCRICAOSUBSETOR'])[0:20] if row['DESCRICAOSUBSETOR'] else '',
#                 str(row['DESCRICAOSEGMENTO'])[0:20] if row['DESCRICAOSEGMENTO'] else '',
#                 str(row['SITUACAO']),
#                 str(row['ID'])
#             ] for row in rows
#         ]
#
#         return make_response(get_json_retorno_grid(rslt='OK', lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_empresa.route('/salvar', methods=['GET', 'POST'])
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
#             id_empresa = data.get('EmprId')
#             id_setor = data.get('EmprSetor')
#             id_subsetor = data.get('EmprSubSetor')
#             id_segmento = data.get('EmprSegmento')
#             nome = data.get('EmprNome')
#             razao_social = data.get('EmprRazao')
#             cnpj = data.get('EmprCNPJ')
#             atividade = data.get('EmprAtividade')
#             cod_cvm = data.get('EmprCodCVM')
#             sit_cvm = data.get('EmprSitCVM')
#             situacao = data.get('EmprSituacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         empresa = ACAOEmpresa()
#         if id_empresa:
#             empresa = ACAOEmpresa.get_by_id(id=int(id_empresa))
#             if not empresa: return make_response(get_json_retorno_metodo(msg='Empresa não localizada.'), 200)
#
#         empresa.id_setor = id_setor
#         empresa.id_subsetor = id_subsetor
#         empresa.id_segmento = id_segmento
#         empresa.nome = str(nome).strip() if nome else None
#         empresa.nome_resumido = str(nome).strip() if nome else None
#         empresa.razao_social = str(razao_social).strip() if razao_social else None
#         empresa.cnpj = str(cnpj).strip() if cnpj else None
#         empresa.atividade = str(atividade).strip() if atividade else None
#         empresa.cod_cvm = str(cod_cvm).strip() if cod_cvm else None
#         empresa.sit_cvm = str(sit_cvm).strip() if sit_cvm else None
#         empresa.situacao = str(situacao).strip() if situacao else None
#         empresa.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_empresa.route('/salvarEmpresa', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_empresa():
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
#             id_setor = data.get('EmprSetor')
#             id_subsetor = data.get('EmprSubSetor')
#             id_segmento = data.get('EmprSegmento')
#             nome = data.get('EmprNome')
#             razao_social = data.get('EmprRazao')
#             cnpj = data.get('EmprCNPJ')
#             atividade = data.get('EmprAtividade')
#             cod_cvm = data.get('EmprCodCVM')
#             sit_cvm = data.get('EmprSitCVM')
#             situacao = data.get('EmprSituacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if ACAOEmpresa.buscar_por_nome(nome=str(nome)):
#             return make_response(get_json_retorno_metodo(msg='Nome da Empresa já cadastro.'), 200)
#
#         if ACAOEmpresa.buscar_por_razao_social(razao_social=str(razao_social)):
#             return make_response(get_json_retorno_metodo(msg='Razão Social da Empresa já cadastra.'), 200)
#
#         if ACAOEmpresa.buscar_por_cnpj(cnpj=str(cnpj)):
#             return make_response(get_json_retorno_metodo(msg='CNPJ da Empresa já cadastro.'), 200)
#
#         empresa = ACAOEmpresa()
#         empresa.id_setor = id_setor
#         empresa.id_subsetor = id_subsetor
#         empresa.id_segmento = id_segmento
#         empresa.nome = str(nome).strip() if nome else None
#         empresa.nome_resumido = str(nome).strip() if nome else None
#         empresa.razao_social = str(razao_social).strip() if razao_social else None
#         empresa.cnpj = str(cnpj).strip() if cnpj else None
#         empresa.atividade = str(atividade).strip() if atividade else None
#         empresa.cod_cvm = str(cod_cvm).strip() if cod_cvm else None
#         empresa.sit_cvm = str(sit_cvm).strip() if sit_cvm else None
#         empresa.situacao = str(situacao).strip() if situacao else None
#         empresa.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_admin_empresa.route('/salvarAtivo', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_ativo():
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
#             id_empresa = data.get('AtvEmpresa')
#             codigo = data.get('AtvCodigo')
#             codigo_isin = data.get('AtvCodIsin')
#             tipo = data.get('AtvTipo')
#             situacao = data.get('AtvSituacao')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         empresa = ACAOEmpresa.get_by_id(id=int(id_empresa))
#         if not empresa:
#             return make_response(get_json_retorno_metodo(msg='Empresa nao localizada.'), 200)
#
#         if ACAOEmpresaAtivo.get_by_codigo(codigo=str(codigo)):
#             return make_response(get_json_retorno_metodo(msg='Ativo já cadastrado.'), 200)
#
#         ativo = ACAOEmpresaAtivo()
#         ativo.id_empresa = int(id_empresa)
#         ativo.codigo = str(codigo).strip() if codigo else None
#         ativo.tipo = str(tipo).strip() if tipo else None
#         ativo.codigo_isin = str(codigo_isin).strip() if codigo_isin else None
#         ativo.situacao = str(situacao).strip() if situacao else None
#         ativo.salvar()
#
#         cotacao = ACAOEmpresaAtivoCotacao()
#         cotacao.id_ativo = int(ativo.id)
#         cotacao.data = pegar_data_atual()
#         cotacao.vlr_preco_abertura = 0.0
#         cotacao.vlr_preco_fechamento = 0.0
#         cotacao.vlr_preco_maximo = 0.0
#         cotacao.vlr_preco_minimo = 0.0
#         cotacao.vlr_preco_anterior = 0.0
#         cotacao.vlr_variacao = 0.0
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
# @bp_admin_empresa.route('/carregar', methods=['GET', 'POST'])
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
#             id_empresa = data.get('IdEmpresa')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_empresa:
#             return make_response(get_json_retorno_dados(msg='Id. Empresa não informado.'), 200)
#
#         empresa = ACAOEmpresa.buscar_por_id(id=int(id_empresa))
#         if not empresa:
#             return make_response(get_json_retorno_dados(msg='Empresa Provento não localizada!'), 200)
#
#         dados = dict(
#             {
#                 "Id": str(empresa['ID']),
#                 "Nome": str(empresa['NOME']) if empresa['NOME'] else '',
#                 "RazaoSocial": str(empresa['RAZAOSOCIAL']) if empresa['RAZAOSOCIAL'] else '',
#                 "CNPJ": str(empresa['CNPJ']) if empresa['CNPJ'] else '',
#                 "Atividade": str(empresa['ATIVIDADE']) if empresa['ATIVIDADE'] else '',
#                 "CodCVM": str(empresa['CODCVM']) if empresa['CODCVM'] else '',
#                 "SitCVM": str(empresa['SITCVM']) if empresa['SITCVM'] else '',
#                 "Situacao": str(empresa['SITUACAO']) if empresa['SITUACAO'] else '',
#                 "SetorId": str(empresa['IDSETOR']) if empresa['IDSETOR'] else '',
#                 "SubSetorId": str(empresa['IDSUBSETOR']) if empresa['IDSUBSETOR'] else '',
#                 "SegmentoId": str(empresa['IDSEGMENTO']) if empresa['IDSEGMENTO'] else '',
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
