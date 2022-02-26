# -*- coding: utf-8 -*-
import sys
import os
from math import floor, ceil
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.usuario_comentario import UsuarioComentario
# from app.models.usuario_comentario_alerta import UsuarioComentarioAlerta
# from app.models.usuario_comentario_reacao import UsuarioComentarioReacao
# from app.models.usuario_comentario_denuncia import UsuarioComentarioDenuncia
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str, pegar_data_hora_atual
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_lista_erro, get_json_retorno_lista_coment, get_json_retorno_dados
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="/comentarios", tags=['comentarios'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
# @login_required
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index(request: _fastapi.Request):
    # return render_template(template_name_or_list="comentarios.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


# @bp_comentarios.route('/montarMenu', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def montar_menu():
#     try:
#
#         path_img = current_app.config['IMAGE_UPLOADS']
#         id_usuario = current_user.id
#         rows = UsuarioComentarioAlerta.buscar_todos(id_usuario=id_usuario, situacao='P')  # P-Pendente
#
#         lista = [
#             [
#                 'Novo Comentário' if alerta['TIPOALERTA'] == 'C' else 'Nova Resposta' if alerta['TIPOALERTA'] == 'R' else 'Nova Denúncia' if alerta['TIPOALERTA'] == 'D' else alerta['TIPOALERTA'],
#                 alerta['DTHRALERTA'],
#                 'de ' + alerta['NMUSUARIOORIGEM'],  # 'Comentário do ' + alerta['NMUSUARIOORIGEM'] if alerta['TIPOALERTA'] == 'C' else 'Resposta do ' + alerta['NMUSUARIOORIGEM'] if alerta['TIPOALERTA'] == 'R' else 'Denúncia do ' + alerta['NMUSUARIOORIGEM'] if alerta['TIPOALERTA'] == 'D' else '',
#                 path_img + '/' + alerta['FTUSUARIOORIGEM'] if alerta['FTUSUARIOORIGEM'] and alerta['FTUSUARIOORIGEM'] != '' else ''
#             ]
#             for alerta in rows
#         ]
#
#         existe = 'SIM' if rows else 'NAO'
#
#         return make_response(get_json_retorno_lista_erro(rslt='OK', existe=existe, lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista_erro(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_comentarios.route('/marcarTodosPend', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def marcar_todos_pend():
#     try:
#
#         id_usuario = current_user.id
#
#         UsuarioComentarioAlerta.marcar_todos_pendentes(id_usuario=id_usuario)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_comentarios.route('/lista', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def lista():
#     try:
#
#         data = None
#         pag_atual = None
#
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#             pag_atual = int(data.get('PagAtual'))
#
#         try:
#             if not pag_atual:
#                 if not data: data = request.get_json(silent=True)
#                 if not data: return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#                 pag_atual = int(data.get('PagAtual'))
#         except:
#             return make_response(get_json_retorno_lista_coment(msg='Dados não informado!'), 200)
#
#         if not pag_atual:
#             pag_atual = 1
#
#         tot_registro = UsuarioComentario.get_qtde_total_coment_princ()
#         qtde_por_pagina = 10
#         pag_total = ceil(tot_registro / qtde_por_pagina)  # calcula o número de páginas arredondando o resultado para cima
#         reg_inicio = (qtde_por_pagina * pag_atual) - qtde_por_pagina  # variavel para calcular o início da visualização com base na página atual
#         id_usuario = current_user.id
#         tipo_usuario = current_user.tipo
#         path_img = str(current_app.config['IMAGE_UPLOADS'])[1:]
#         print(path_img)
#
#         exibir_dados_admin = 'S' if str(tipo_usuario) == 'A' else 'N'
#
#         comentarios = UsuarioComentario.buscar_coment_grid_princ(reg_inicio=reg_inicio, qtde_pagina=qtde_por_pagina)
#
#         lista = []
#         for coment in comentarios:
#
#             qtd_coment = 0
#             lista_resp = []
#
#             respostas = UsuarioComentario.buscar_coment_grid_resp(id_comentario=int(coment["IDCOMENTARIO"]))
#             for resp in respostas:
#                 qtd_coment += 1
#                 lista_resp.append({
#                     "Id": str(resp['IDCOMENTARIO']),
#                     "Nome": str(resp['NOMEUSUARIO']),
#                     "Foto": path_img + '/' + str(resp['FOTOUSUARIO']) if resp['FOTOUSUARIO'] and resp['FOTOUSUARIO'] != '' else '',
#                     "DtHr": converter_datetime_str(data=converter_str_to_datetime(data=str(resp['DTHRCOMENTARIO']), fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S'),
#                     "Texto": str(resp['TXTCOMENTARIO']).replace('\n', '<br>'),
#                     "ExibeBtnDenu": 'N' if str(id_usuario) == str(resp['IDUSUARIO']) else 'S',
#                     "ExibeBtnEdit": 'S' if str(id_usuario) == str(resp['IDUSUARIO']) else 'N',
#                     "ExibeBtnExcl": 'S' if str(id_usuario) == str(resp['IDUSUARIO']) else 'N',
#                     "ExibirDadosAdmin": str(exibir_dados_admin),
#                     "MarcarGostei": str(UsuarioComentarioReacao.buscar_verifica(id_usuario=id_usuario, id_comentario=int(resp["IDCOMENTARIO"]), tipo="A")),  # A-Gostei
#                     "QtdeGostei": str(UsuarioComentarioReacao.buscar_qtde_total(id_comentario=int(resp["IDCOMENTARIO"]), tipo="A")),  # A-Gostei
#                     "MarcarNaoGostei": str(UsuarioComentarioReacao.buscar_verifica(id_usuario=id_usuario, id_comentario=int(resp["IDCOMENTARIO"]), tipo="B")),  # B-NAO Gostei
#                     "QtdeNaoGostei": str(UsuarioComentarioReacao.buscar_qtde_total(id_comentario=int(resp["IDCOMENTARIO"]), tipo="B"))  # B-NAO Gostei
#                 })
#
#             lista.append({
#                 "Id": str(coment['IDCOMENTARIO']),
#                 "Nome": str(coment['NOMEUSUARIO']),
#                 "Foto": path_img + '/' + str(coment['FOTOUSUARIO']) if coment['FOTOUSUARIO'] and coment['FOTOUSUARIO'] != '' else '',
#                 "DtHr": converter_datetime_str(data=converter_str_to_datetime(data=str(coment['DTHRCOMENTARIO']), fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S'),
#                 "Texto": str(coment['TXTCOMENTARIO']).replace('\n', '<br>'),
#                 "ExibeBtnDenu": 'N' if str(id_usuario) == str(coment['IDUSUARIO']) else 'S',
#                 "ExibeBtnEdit": 'S' if str(id_usuario) == str(coment['IDUSUARIO']) else 'N',
#                 "ExibeBtnExcl": 'S' if str(id_usuario) == str(coment['IDUSUARIO']) else 'N',
#                 "MarcarGostei": str(UsuarioComentarioReacao.buscar_verifica(id_usuario=id_usuario, id_comentario=int(coment["IDCOMENTARIO"]), tipo="A")),  # A-Gostei
#                 "QtdeGostei": str(UsuarioComentarioReacao.buscar_qtde_total(id_comentario=int(coment["IDCOMENTARIO"]), tipo="A")),  # A-Gostei
#                 "MarcarNaoGostei": str(UsuarioComentarioReacao.buscar_verifica(id_usuario=id_usuario, id_comentario=int(coment["IDCOMENTARIO"]), tipo="B")),  # B-NAO Gostei
#                 "QtdeNaoGostei": str(UsuarioComentarioReacao.buscar_qtde_total(id_comentario=int(coment["IDCOMENTARIO"]), tipo="B")),  # B-NAO Gostei
#                 "QtdeComent": str(qtd_coment),
#                 "ExibirDadosAdmin": str(exibir_dados_admin),
#                 "ListaResp": lista_resp
#             })
#
#         return make_response(get_json_retorno_lista_coment(rslt='OK', pag_atual=str(pag_atual), pag_total=str(pag_total), lista=lista), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_lista_coment(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_comentarios.route('/salvarComentario', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_comentario():
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
#             texto = data.get('Texto')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if str(id).strip() == '':
#             id = None
#
#         if not texto:
#             return make_response(get_json_retorno_metodo(msg='Texto Comentário não informado.'), 200)
#
#         id_usuario = current_user.id
#         tipo_usuario = current_user.tipo
#
#         if not id:
#             coment = UsuarioComentario(id_usuario=id_usuario)
#         else:
#             coment = UsuarioComentario.get_by_id_and_id_usuario(id=id, id_usuario=id_usuario)
#
#         if not coment:
#             return make_response(get_json_retorno_metodo(msg='Comentário não localizado.'), 200)
#
#         coment.tipo = 'A'  # A-Comentario Princ
#         coment.texto = texto
#         coment.data_hora = pegar_data_hora_atual()
#         coment.situacao = 'A'  # A-Ativo
#         coment.salvar()
#
#         if not id:
#             tipo_usuario = 'A' if str(tipo_usuario) == 'I' else 'I'  # I-Investidor  # A-Administrador
#             UsuarioComentarioAlerta().salvar_todos(id_usuario=id_usuario, id_comentario=coment.id, tipo_alerta='C', tipo_usuario=tipo_usuario) # C-Comentario
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_comentarios.route('/salvarResposta', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_resposta():
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
#             id_comentario = data.get('IdComent')
#             texto = data.get('Texto')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if str(id).strip() == '':
#             id = None
#
#         if not id_comentario:
#             return make_response(get_json_retorno_metodo(msg='Id. Comentário não informado.'), 200)
#
#         if not texto:
#             return make_response(get_json_retorno_metodo(msg='Texto Comentário não informado.'), 200)
#
#         id_usuario = current_user.id
#
#         if not id:
#             coment = UsuarioComentario(id_usuario=id_usuario)
#         else:
#             coment = UsuarioComentario.get_by_id_and_id_usuario(id=id, id_usuario=id_usuario)
#
#         if not coment:
#             return make_response(get_json_retorno_metodo(msg='Comentário não localizado.'), 200)
#
#         coment.id_pai = id_comentario
#         coment.tipo = 'B'  # B-Resposta
#         coment.texto = texto
#         coment.data_hora = pegar_data_hora_atual()
#         coment.situacao = 'A'  # A-Ativo
#         coment.salvar()
#
#         if not id:
#             UsuarioComentarioAlerta().salvar_todas_resp(id_usuario=id_usuario, id_comentario=id_comentario)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_comentarios.route('/salvarReacao', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_reacao():
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
#             id_comentario = data.get('IdComent')
#             tipo = data.get('Tipo')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_comentario:
#             return make_response(get_json_retorno_dados(msg='Id. Comentário não informado.'), 200)
#
#         if not tipo:
#             return make_response(get_json_retorno_dados(msg='Tipo Comentário não informado.'), 200)
#
#         id_usuario = current_user.id
#         # existe_reacao = UsuarioComentarioReacao.buscar_verifica(id_usuario=id_usuario, id_comentario=id_comentario, tipo=tipo)
#
#         coment_reacao = UsuarioComentarioReacao.get_by_id_comentario(id_comentario=int(id_comentario), id_usuario=id_usuario)
#         if coment_reacao:
#             coment_reacao.excluir()
#
#         coment_reacao = UsuarioComentarioReacao()
#         coment_reacao.id_usuario = id_usuario
#         coment_reacao.id_comentario = int(id_comentario)
#         coment_reacao.tipo = tipo
#         coment_reacao.salvar()
#
#         dados = dict(
#             {
#                 "QtdeGostei": str(UsuarioComentarioReacao.buscar_qtde_total(id_comentario=int(id_comentario), tipo="A")),  # A-Gostei
#                 "QtdeNaoGostei": str(UsuarioComentarioReacao.buscar_qtde_total(id_comentario=int(id_comentario), tipo="B"))  # B-NAO Gostei
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
# @bp_comentarios.route('/denunciar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def denunciar():
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
#             id_comentario = data.get('IdComent')
#             tipo = data.get('Tipo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_comentario:
#             return make_response(get_json_retorno_metodo(msg='Id. Comentário não informado.'), 200)
#
#         if not tipo:
#             return make_response(get_json_retorno_metodo(msg='Tipo Comentário não informado.'), 200)
#
#         coment = UsuarioComentario.get_by_id(id=id_comentario)
#
#         if not coment:
#             return make_response(get_json_retorno_metodo(msg='Comentário não localizado.'), 200)
#
#         coment.situacao = 'D'  # D-Denunciado
#         coment.salvar()
#
#         id_usuario = current_user.id
#
#         coment_denuncia = UsuarioComentarioDenuncia()
#         coment_denuncia.id_usuario = id_usuario
#         coment_denuncia.id_comentario = int(id_comentario)
#         coment_denuncia.tipo = tipo
#         coment_denuncia.situacao = 'A'  # A-Em Avaliação pelo ADM
#         coment_denuncia.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_comentarios.route('/excluir', methods=['GET', 'POST'])
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
#             id_comentario = data.get('IdComent')
#             tipo = data.get('Tipo')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not id_comentario:
#             return make_response(get_json_retorno_metodo(msg='Id. Comentário não informado.'), 200)
#
#         if not tipo:
#             return make_response(get_json_retorno_metodo(msg='Tipo Comentário não informado.'), 200)
#
#         coment = UsuarioComentario.get_by_id(id=id_comentario)
#
#         if not coment:
#             return make_response(get_json_retorno_metodo(msg='Comentário não localizado.'), 200)
#
#         if tipo == 'A':  # A-Comentario
#             UsuarioComentarioAlerta.excluir_resposta(id_comentario=int(id_comentario))
#             UsuarioComentarioDenuncia.excluir_respostas(id_comentario=int(id_comentario))
#             UsuarioComentarioReacao.excluir_respostas(id_comentario=int(id_comentario))
#             UsuarioComentario.excluir_respostas(id_comentario=int(id_comentario))
#
#         UsuarioComentarioAlerta.excluir_comentario(id_comentario=int(id_comentario))
#         UsuarioComentarioDenuncia.excluir_comentario(id_comentario=int(id_comentario))
#         UsuarioComentarioReacao.excluir_comentario(id_comentario=int(id_comentario))
#         UsuarioComentario.excluir_comentario(id_comentario=int(id_comentario))
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_comentarios.route('/visualizar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def visualizar():
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
#             id_comentario = data.get('IdComent')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not id_comentario:
#             return make_response(get_json_retorno_dados(msg='Id. Comentário não informado.'), 200)
#
#         coment = UsuarioComentario.get_by_id(id=int(id_comentario))
#
#         if not coment:
#             return make_response(get_json_retorno_dados(msg='Comentário não localizado.'), 200)
#
#         lista_visualizou = ''
#         lista_gostei = ''
#         lista_nao_gostei = ''
#
#         rows = UsuarioComentario.buscar_lista_user_alerta(id_comentario=int(id_comentario))
#         for row in rows:
#             lista_visualizou += "<br>" if lista_visualizou != '' else '' + str(row['IDUSUARIO']) + ' - ' + str(row['NOMEUSUARIO']) + '( ' + str(row['EMAILUSUARIO']) + ' )'
#
#         rows = UsuarioComentario.buscar_lista_user_reacao(id_comentario=int(id_comentario), tipo='A')  # A-Gostei
#         for row in rows:
#             lista_gostei += "<br>" if lista_gostei != '' else '' + str(row['IDUSUARIO']) + ' - ' + str(row['NOMEUSUARIO']) + '( ' + str(row['EMAILUSUARIO']) + ' )'
#
#         rows = UsuarioComentario.buscar_lista_user_reacao(id_comentario=int(id_comentario), tipo='B')  # B-NAO Gostei
#         for row in rows:
#             lista_nao_gostei += "<br>" if lista_nao_gostei != '' else '' + str(row['IDUSUARIO']) + ' - ' + str(row['NOMEUSUARIO']) + '( ' + str(row['EMAILUSUARIO']) + ' )'
#
#         dados = dict(
#             {
#                 "ListaVisualizou": lista_visualizou,
#                 "ListaGostei": lista_gostei,
#                 "ListaNaoGostei": lista_nao_gostei
#             }
#         )
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
