# # -*- coding: utf-8 -*-
# import sys
# import os
# from flask import Blueprint, render_template, redirect, url_for, request, make_response, session
# from flask_login import current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from flask_mail import Message
# from app.mail import mail, email_confirmacao_cadastro, email_redefinir_senha
# from app.models.log_erro import LogErro
# from app.models.alerta import Alerta
# from app.models.usuario import Usuario
# from app.models.usuario_log import UsuarioLog
# from app.models.usuario_hash import UsuarioHash
# from app.util.util_json import get_json_retorno_metodo
# from app.util.util_datahora import pegar_data_atual
#
#
# bp_usuario = Blueprint('usuario', __name__, url_prefix='/usuario')
#
#
# @bp_usuario.route("/criarconta")
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# def criar_conta():
#     if current_user.is_authenticated:
#         return redirect(location=url_for('principal.index'))
#     return render_template(template_name_or_list="usuario_criar_conta.html")
#
#
# @bp_usuario.route('/salvarDadosConta', methods=['GET', 'POST'])
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_dados_conta():
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
#             nome = data.get('txtUserNome')
#             email = data.get('txtUserEmail')
#             senha = data.get('txtUserSenha')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not nome:
#             return make_response(get_json_retorno_metodo(msg='Nome não informado.'), 200)
#
#         if not email:
#             return make_response(get_json_retorno_metodo(msg='Email não informado.'), 200)
#
#         if not senha:
#             return make_response(get_json_retorno_metodo(msg='Senha não informada.'), 200)
#
#         # import re
#         # if re.search("@gm(ia|a|i)l.com$", example):
#         #     return make_response(get_json_retorno_metodo(msg='E-mail inválido.'), 200)
#
#         usuario = Usuario.get_by_email(email=email)
#         if usuario:
#             return make_response(get_json_retorno_metodo(msg='Usuário já cadastrado.'), 200)
#
#         data_registro = pegar_data_atual()
#
#         usuario = Usuario(nome=nome, email=email, data_registro=data_registro, tentatia=0, tipo='I', situacao='B')
#         usuario.senha = usuario.senha_sha256(senha)
#         usuario.salvar()
#
#         hash = usuario.criptografar_hash(email=email)
#
#         hash_mail = UsuarioHash(id_usuario=usuario.id, hash=hash, data_registro=data_registro, situacao='B')
#         hash_mail.salvar()
#
#         subject = 'TnB - Ative sua Conta'
#         html = email_confirmacao_cadastro(hash=hash)
#         sender = "suporte@tamonabolsa.com.br"  # "chris.mar.silva@gmail.com"
#         mail.send(Message(subject=subject, html=html, sender=sender, recipients=[email], charset='UTF-8'))
#
#         msg = "Dados salvo com sucesso. <br/>Enviamos um E-mail para confirmar seu cadastro."
#         return make_response(get_json_retorno_metodo(rslt='OK', msg=msg), 200)
#
#     except Exception as e:
#         #LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_usuario.route("/ativacao", methods=['GET', 'POST'])
# @bp_usuario.route("/ativacao/", methods=['GET', 'POST'])
# @bp_usuario.route("/ativacao/<hash>", methods=['GET', 'POST'])
# # @tracing.trace()
# def usuario_ativacao(hash: str = None):
#     try:
#
#         if not hash:
#             raise Exception('Use o link na mensagem enviada para o seu e-mail para ativar o seu cadastro.')
#
#         email = Usuario().descriptografar_hash(message=hash)
#         if not email:
#             raise Exception('O E-mail para Ativação não foi informado.')
#
#         usuario = Usuario.get_by_email(email=email)
#         if not usuario:
#             raise Exception('O Usuário para Ativação não foi encontrado.')
#
#         if usuario.situacao == "X":  # X - Bloqueado
#             raise Exception('Usuário Bloqueado. Contate o Suporte do Site.')
#
#         # if usuario.situacao != "B":  # B - Aguardando Confirmação de Email
#         #     raise Exception('A Ativação do Usuário já foi confirmada.')
#
#         hash_mail = UsuarioHash.get_by_usuario(id_usuario=usuario.id)
#         if not hash_mail:
#             raise Exception('Hash do Usuário não foi encontrado.')
#
#         if hash_mail.situacao != "B":  # B - Aguardando Confirmação de Email
#            raise Exception('A chave de Ativação do Usuário já foi confirmada.')
#
#         if hash[-1] == '"' and hash_mail.hash[-1] != '"':
#             hash = hash[:-1]
#
#         if hash_mail.hash != hash:
#             raise Exception('A chave de Ativação não está associada ao Usuário de origem.')
#
#         usuario.situacao = 'A'
#         usuario.salvar()
#
#         hash_mail.situacao = 'A'
#         hash_mail.salvar()
#
#         session['tnb-user-cad'] = usuario.nome
#
#         return redirect(location=url_for(endpoint='usuario.usuario_sucesso'))
#
#     except Exception as e:
#         #LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return render_template(template_name_or_list="usuario_ativacao.html", msg=LogErro.descricao_erro(texto=str(e)))
#
#
# @bp_usuario.route("/sucesso", methods=['GET', 'POST'])
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# def usuario_sucesso():
#     try:
#
#         nome = None
#         if 'tnb-user-cad' in session:
#             nome = session['tnb-user-cad']
#             session.pop('tnb-user-cad', None)
#
#         return render_template(template_name_or_list="usuario_sucesso.html", nome=nome)
#
#     except Exception as e:
#         #LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return render_template(template_name_or_list="usuario_ativacao.html", nome=LogErro.descricao_erro(texto=str(e)))
#
#
# @bp_usuario.route("/esqueceusenha", methods=['GET', 'POST'])
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# def esqueceu_senha():
#     if current_user.is_authenticated:
#         return redirect(location=url_for(endpoint='principal.index'))
#     return render_template(template_name_or_list="usuario_esqueceu_senha.html")
#
#
# @bp_usuario.route('/enviarEmailSenha', methods=['GET', 'POST'])
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def enviar_email_senha():
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
#             email = data.get('txtUserEmail')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not email:
#             raise Exception('Email não informado.')
#
#         # import re
#         # if re.search("@gm(ia|a|i)l.com$", example):
#         #     return make_response(get_json_retorno_metodo(msg='E-mail inválido.'), 200)
#
#         usuario = Usuario.get_by_email(email=email)
#         if not usuario:
#             raise Exception('E-mail não cadastrado.')
#
#         if usuario.situacao == "X":  # X - Bloqueado
#             raise Exception('Usuário Bloqueado. <br/>Contate o Suporte do Site.')
#
#         hash_mail = UsuarioHash.get_by_usuario(id_usuario=usuario.id)
#         if not hash_mail:
#             raise Exception('Hash do Usuário não foi encontrado.')
#
#         subject = 'TnB - Redefinir sua Senha'
#         html = email_redefinir_senha(hash=hash_mail.hash)
#         sender = "suporte@tamonabolsa.com.br"
#         mail.send(Message(subject=subject, html=html, sender=sender, recipients=[email], charset='UTF-8'))
#
#         usuario.tentatia = 0
#         usuario.situacao = 'B'  # B - Aguardando Confirmação de Email
#         usuario.salvar()
#
#         hash_mail.situacao = 'B'  # B - Aguardando Confirmação de Email
#         hash_mail.salvar()
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Enviamos um E-mail para redefinir sua Senha.'), 200)
#
#     except Exception as e:
#         #LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_usuario.route("/redefinirsenha", methods=['GET', 'POST'])
# @bp_usuario.route("/redefinirsenha/", methods=['GET', 'POST'])
# @bp_usuario.route("/redefinirsenha/<hash>", methods=['GET', 'POST'])
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# def usuario_redefinir_senha(hash: str = None):
#     try:
#
#         if not hash:
#             raise Exception('Use o link na mensagem enviada para o seu e-mail para redefinir a sua senha.')
#
#         email = Usuario().descriptografar_hash(message=hash)
#
#         if not email:
#             raise Exception('O E-mail para Ativação não foi informado.')
#
#         usuario = Usuario.get_by_email(email=email)
#         if not usuario:
#             raise Exception('O Usuário para Ativação não foi encontrado.')
#
#         if usuario.situacao == "X":  # X - Bloqueado
#             raise Exception('Usuário Bloqueado. Contate o Suporte do Site.')
#
#         if usuario.situacao != "B":  # B - Aguardando Confirmação de Email
#             raise Exception('A Ativação do Usuário já foi confirmada.')
#
#         hash_mail = UsuarioHash.get_by_usuario(id_usuario=usuario.id)
#         if not hash_mail:
#             raise Exception('Hash do Usuário não foi encontrado.')
#
#         #if hash_mail.situacao != "B":  # B - Aguardando Confirmação de Email
#         #    raise Exception('A chave de Ativação do Usuário já foi confirmada.')
#
#         if hash[-1] == '"' and hash_mail.hash[-1] != '"':
#             hash = hash[:-1]
#
#         if hash_mail.hash != hash:
#             raise Exception('A chave de Ativação não está associada ao Usuário de origem.')
#
#         return render_template(template_name_or_list="usuario_redefinir_senha.html", email=email)
#
#     except Exception as e:
#         #LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return render_template(template_name_or_list="usuario_erro_redefinir_senha.html", msg=LogErro.descricao_erro(texto=str(e)))
#
#
# @bp_usuario.route("/SalvarNovaSenha", methods=['GET', 'POST'])
# @bp_usuario.route("/salvarNovaSenha", methods=['GET', 'POST'])
# @bp_usuario.route("/salvarnovasenha", methods=['GET', 'POST'])
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def salvar_nova_senha():
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
#             email = data.get('txtUserEmail')
#             senha = data.get('txtUserSenha')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         if not email:
#             return make_response(get_json_retorno_metodo(msg='Email não informado.'), 200)
#
#         if not senha:
#             return make_response(get_json_retorno_metodo(msg='Senha não informada.'), 200)
#
#         usuario = Usuario.get_by_email(email=email)
#         if not usuario:
#             return make_response(get_json_retorno_metodo(msg='Usuário não encontrado.'), 200)
#
#         if usuario.situacao == "X":  # X - Bloqueado
#             return make_response(get_json_retorno_metodo(msg='Usuário Bloqueado. Contate o Suporte do Site.'), 200)
#
#         if usuario.situacao != "B":  # B - Aguardando Confirmação de Email
#             return make_response(get_json_retorno_metodo(msg='A Ativação do Usuário já foi confirmada.'), 200)
#
#         hash_mail = UsuarioHash.get_by_usuario(id_usuario=usuario.id)
#         if not hash_mail:
#             return make_response(get_json_retorno_metodo(msg='Hash do Usuário não foi encontrado.'), 200)
#
#         #if hash_mail.situacao != "B":  # B - Aguardando Confirmação de Email
#         #    return make_response(get_json_retorno_metodo(msg='A chave de Ativação do Usuário já foi confirmada.'), 200)
#
#         usuario.senha = usuario.senha_sha256(senha)
#         usuario.tentatia = 0
#         usuario.situacao = 'A'
#         usuario.salvar()
#
#         hash_mail.situacao = 'A'
#         hash_mail.salvar()
#
#         UsuarioLog().registrar(id_usuario=usuario.id, situacao='D')  # D-Redefinir Senha
#         Alerta.registrar(id_usuario=usuario.id, tipo='PERFIL-01', mensagem='Sua senha foi alterada. <br>IP: ' + str(request.remote_addr))
#
#         session['tnb-user-sen'] = usuario.nome
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Senha salva com sucesso.'), 200)
#
#     except Exception as e:
#         #LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_usuario.route("/sucessoredefinirsenha")
# # @tracing.trace()
# # @cache.cached(timeout=60)
# @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# def sucesso_redefinir_senha():
#     try:
#
#         nome = None
#         if 'tnb-user-sen' in session:
#             nome = session['tnb-user-sen']
#             session.pop('tnb-user-sen', None)
#
#         return render_template(template_name_or_list="usuario_sucesso_redefinir_senha.html", nome=nome)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return render_template(template_name_or_list="usuario_sucesso_redefinir_senha.html", nome=LogErro.descricao_erro(texto=str(e)))
