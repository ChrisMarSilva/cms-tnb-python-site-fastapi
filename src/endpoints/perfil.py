# # -*- coding: utf-8 -*-
# import sys
# import os
# from flask import Blueprint, render_template, make_response, request, current_app
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache, del_cache_user
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.usuario_config import UsuarioConfig
# from app.models.alerta import Alerta
# from app.models.usuario import Usuario
# from app.models.usuario_log import UsuarioLog
# from app.models.usuario_cei import UsuarioCei
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados
# from app.util.util_datahora import pegar_data_hora_atual
#
#
# bp_perfil = Blueprint('perfil', __name__, url_prefix='/perfil')
#
#
# @bp_perfil.route('/')
# @login_required
# # @tracing.trace()
# #@cache.cached(timeout=60)
# # @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     return render_template(template_name_or_list="perfil.html")
#
#
# @bp_perfil.route('/carregar', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def carregar():
#     try:
#
#         id_usuario = current_user.id
#
#         usuario = Usuario.get_by_id(id=id_usuario)
#         if not usuario:
#             return make_response(get_json_retorno_dados(msg='Usuário não encontrado!.'), 200)
#
#         cei_cpf = ""
#         cei_status = "I"
#         usuario_cei = UsuarioCei.get_by_usuario(id_usuario=id_usuario)
#         if usuario_cei:
#             cei_cpf = usuario_cei.cpf
#             cei_status = usuario_cei.situacao
#
#         foto = usuario.foto
#         if foto:
#             foto = current_app.config['IMAGE_UPLOADS'] + '/' + foto
#             foto = foto[1:]
#
#         dados = dict(
#             {
#                 "Nome": str(usuario.nome),
#                 "Email": str(usuario.email),
#                 "ChaId": str(usuario.chat_id) if usuario.chat_id else '',
#                 "Foto": str(foto) if foto else '',
#                 "Cpf": str(cei_cpf) if cei_cpf else '',
#                 "Status": str(cei_status) if cei_status else ''
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
# @bp_perfil.route('/salvarDados', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_dados():
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
#             nome = data.get('txtNome')
#             chat_id = data.get('txtChatId')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         id_usuario = current_user.id
#
#         usuario = Usuario.get_by_id(id=id_usuario)
#         if not usuario: return make_response(get_json_retorno_metodo(msg='Usuário não encontrado!.'), 200)
#
#         usuario.nome = nome
#         usuario.chat_id = chat_id
#         usuario.salvar()
#
#         del_cache_user(id_usuario)
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_perfil.route('/salvarSenha', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_senha():
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
#             senha_atual = data.get('txtSenhaAtual')
#             senha_nova = data.get('txtNovaSenha')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not senha_atual: return make_response(get_json_retorno_metodo(msg='Senha Atual não informada.'), 200)
#         if not senha_nova: return make_response(get_json_retorno_metodo(msg='Senha Nova não informada.'), 200)
#
#         id_usuario = current_user.id
#
#         usuario = Usuario.get_by_id(id=id_usuario)
#         if not usuario: return make_response(get_json_retorno_metodo(msg='Usuário não encontrado!.'), 200)
#
#         senha_atual = usuario.senha_sha256(senha_atual)
#         senha_nova = usuario.senha_sha256(senha_nova)
#         if senha_atual != usuario.senha:return make_response(get_json_retorno_metodo(msg='Senha Atual Inválida!'), 200)
#
#         usuario.senha = senha_nova
#         usuario.salvar()
#
#         del_cache_user(id_usuario)
#
#         Alerta.registrar(id_usuario=id_usuario, tipo='PERFIL-01', mensagem='Sua senha foi alterada. <br>IP: ' + str(request.remote_addr))
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_perfil.route('/resetarOperac', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def resetar_operacao():
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
#             senha = data.get('SenhaResetar')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not senha:
#             return make_response(get_json_retorno_dados(msg='Senha não informada.'), 200)
#
#         id_usuario = current_user.id
#
#         usuario = Usuario.get_by_id(id=id_usuario)
#         if not usuario: return make_response(get_json_retorno_metodo(msg='Usuário não encontrado!.'), 200)
#
#         senha = usuario.senha_sha256(senha)
#         if senha != usuario.senha:return make_response(get_json_retorno_dados(msg='Senha Atual Inválida!'), 200)
#
#         usuario.resetar_dados()
#
#         UsuarioLog().registrar(id_usuario=id_usuario, situacao='R') # R-Resetar Operações
#
#         Alerta.registrar(id_usuario=id_usuario, tipo='PERFIL-02', mensagem='Todos os seus dados foram apagado. <br>IP: ' + str(request.remote_addr))
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# def allowed_file(filename):
#     if not "." in filename:
#         return False
#     ext = filename.rsplit(".", 1)[1]
#     if ext.upper() in current_app.config.get('ALLOWED_IMAGE_EXTENSIONS'):
#         return True
#     else:
#         return False
#
#
# def allowed_image_filesize(filesize):
#     if int(filesize) <= current_app.config.get('MAX_IMAGE_FILESIZE'):
#         return True
#     else:
#         return False
#
#
# @bp_perfil.route('/importarfoto', methods=['POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def importar_foto():
#     try:
#
#         if 'arquivo' not in request.files:
#             return make_response(get_json_retorno_metodo(msg='Nenhuma Imagem informada.'), 200)
#
#         file = request.files['arquivo']
#
#         if file.filename == '':
#             return make_response(get_json_retorno_metodo(msg='Nenhuma Imagem informada.'), 200)
#
#         if not allowed_file(file.filename):
#             return make_response(get_json_retorno_metodo(msg="Arquivo não é uma imagem - " + file.filename), 200)
#
#         # if not allowed_image_filesize(request.cookies["filesize"]):
#         #     return make_response(get_json_retorno_metodo(msg='Arquivo deve ser de no máximo 10MB - ' + file.filename), 200)
#
#         id_usuario = current_user.id
#
#         ext = file.filename.rsplit(".", 1)[1]
#
#         filename = 'user_'+str(id_usuario)+'_' + pegar_data_hora_atual() +'.' + ext.lower()
#
#         import os
#         path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../' + current_app.config['IMAGE_UPLOADS'])
#         file.save(os.path.join(path, filename))
#
#         try:
#             from PIL import Image
#             size = 150, 100  # Largura # Altura
#             im = Image.open(os.path.join(path, filename))
#             im.thumbnail(size, Image.ANTIALIAS)
#             im.save(os.path.join(path, filename))
#         except:
#             pass
#
#         usuario = Usuario.get_by_id(id=id_usuario)
#         if not usuario:
#             return make_response(get_json_retorno_dados(msg='Usuário não encontrado!.'), 200)
#
#         if usuario.foto != '':
#             try:
#                 os.remove(os.path.join(path, usuario.foto))
#             except:
#                 pass
#
#         # usuario.foto = current_app.config['IMAGE_UPLOADS'] + '/' + filename
#         usuario.foto = filename
#         usuario.salvar()
#
#         del_cache_user(id_usuario)
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Imagem salva com sucesso!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_perfil.route('/config', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def config():
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
#             tipo = data.get('tipo')
#             valor = data.get('valor')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not tipo: return make_response(get_json_retorno_metodo(msg='Tipo Inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo=tipo)
#         if not config:
#             config = UsuarioConfig(id_usuario=id_usuario, tipo=tipo, valor=valor)
#             config.salvar()
#
#         dados = dict({"Valor": config.valor})
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_dados(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_perfil.route('/salvarconfig', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_config():
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
#             tipo = data.get('tipo')
#             valor = data.get('valor')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not tipo: return make_response(get_json_retorno_metodo(msg='Tipo Inválido.'), 200)
#         if not valor: return make_response(get_json_retorno_metodo(msg='Valor Inválido.'), 200)
#
#         id_usuario = current_user.id
#
#         config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo=tipo)
#         if not config:  config = UsuarioConfig(id_usuario=id_usuario, tipo=tipo, valor=valor)
#         config.valor = valor
#         config.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
