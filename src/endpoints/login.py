# -*- coding: utf-8 -*-
import sys
import os
from datetime import timedelta
import fastapi as _fastapi
# from flask_login import login_user, logout_user, current_user, login_required
# from app.cache import cache, del_cache_all
# # from app.tracing import tracing
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.alerta import Alerta
# from app.models.usuario import Usuario
# from app.models.usuario_log import UsuarioLog
# from app.util.util_json import get_json_retorno_metodo, get_json_retorno_dados


router = _fastapi.APIRouter(prefix="/login", tags=['login'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @flask_optimize.optimize(cache='GET-10')  # 10seg
async def get_index():
    # if current_user.is_authenticated:
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="login.html")
    return {"result": "ok"}


# @bp_login.route("/entrar", methods=['GET', 'POST'])
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def entrar():
#     try:
#
#         data = None
#         origem = ''
#
#         if request.method == 'POST':
#             data = request.form
#             origem = 'L'  # Login Site
#         elif request.method == 'GET':
#             data = request.args
#             origem = 'P'  # Login App
#
#         if not data:
#             origem = 'P'  # Login App
#             data = request.get_json(silent=True)
#
#         if not data: return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         try:
#             email = data.get('txtEmail')
#             senha = data.get('txtSenha')
#         except:
#             return make_response(get_json_retorno_dados(msg='Dados não informado!'), 200)
#
#         if not email: return make_response(get_json_retorno_dados(msg='E-mail não informado!'), 200)
#         if not senha: return make_response(get_json_retorno_dados(msg='Senha não informada!'), 200)
#
#         usuario = Usuario.get_by_email_full(email=email)
#         if not usuario: return make_response(get_json_retorno_dados(msg='Usuário/Senha Inválido.'), 200)
#
#         # usuario = Usuario.get_by_email(email=email)
#         # if not usuario:
#         #     usuario = Usuario.get_by_email_parcial(email=email)
#         #     if not usuario:
#         #         return make_response(get_json_retorno_dados(msg='Usuário/Senha Inválido.'), 200)
#
#         if usuario.situacao == 'X':  # X-Bloqueado
#             Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-02', mensagem='Usuário Bloqueado. <br>IP: ' + str(request.remote_addr))
#             return make_response(get_json_retorno_dados(msg='Usuário Bloqueado. <br/>Contate o Suporte do Site.'), 200)
#
#         if usuario.situacao != 'A':  # A-Ativo
#             Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-02', mensagem='Usuário não está Ativo. <br>IP: ' + str(request.remote_addr))
#             return make_response(get_json_retorno_dados(msg='Usuário não está Ativo.'), 200)
#
#         if not usuario.validar_senha(senha=senha):
#
#             UsuarioLog().registrar(id_usuario=usuario.id, situacao='I')   # I-Senha Invalida
#             usuario.tentatia += 1
#             Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-02', mensagem='Tentativa de login ' + str(usuario.tentatia) + '/3. <br>IP: ' + str(request.remote_addr))
#
#             if usuario.tentatia >= 3:
#                 UsuarioLog().registrar(id_usuario=usuario.id, situacao='B')  # B-Inativar Usuario
#                 usuario.situacao = 'I'  # I-Inativo
#                 usuario.salvar()
#                 Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-03', mensagem='Usuário inativado por tentativas de login. <br>IP: ' + str(request.remote_addr))
#                 return make_response(get_json_retorno_dados(msg='Usuário Inativo por Tentativas de Login com senha Inválida.'), 200)
#
#             usuario.salvar()
#             return make_response(get_json_retorno_dados(msg='Usuário/Senha Inválido.'), 200)
#
#         if usuario.tentatia > 0 or usuario.situacao != 'A':  # A-Ativo
#             usuario.tentatia = 0
#             usuario.situacao = 'A'  # A-Ativo
#             usuario.salvar()
#
#         try:
#             cache.clear()
#         except Exception as e:
#             pass
#
#         try:
#             del_cache_all(current_user.id)
#         except Exception as e:
#             pass
#
#         try:
#             logout_user()
#         except Exception as e:
#             pass
#
#         login_user(user=usuario, remember=True, duration=timedelta(hours=1))
#         UsuarioLog().registrar(id_usuario=usuario.id, situacao=origem)
#
#         foto = usuario.foto
#         if foto:
#             foto = current_app.config['IMAGE_UPLOADS'] + '/' + foto
#             foto = foto[1:]
#
#         dados = dict({
#             "Id": str(usuario.id),
#             "Tipo": str(usuario.tipo),
#             "Nome": str(usuario.nome),
#             "Foto": str(foto) if foto else '',
#             "Email": str(usuario.email),
#         })
#
#         return make_response(get_json_retorno_dados(rslt='OK', dados=dados), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
#
#
# @bp_login.route("/sair", methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def sair():
#     try:
#
#         try:
#             cache.clear()
#         except Exception as e:
#             pass
#
#         try:
#             del_cache_all(current_user.id)
#         except Exception as e:
#             pass
#
#         try:
#             logout_user()
#         except Exception as e:
#             pass
#
#         return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(
#             __file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
