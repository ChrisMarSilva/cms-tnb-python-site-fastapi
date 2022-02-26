# # -*- coding: utf-8 -*-
# import sys
# import os
from datetime import timedelta
# from app.cache import cache, del_cache_all
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.alerta import Alerta
# from app.models.usuario import Usuario
# from app.models.usuario_log import UsuarioLog
from src.util.util_json import get_json_retorno_metodo, get_json_retorno_dados
import inspect
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import src.services as _services
from src.schemas.login import LoginIn, LoginOut
from src.repositories.usuario import UsuarioRepository
import src.config.config_trace as _tracer
# import src.config.config_token as _token
from src.config.config_login_manager import manager


class LoginService(_services.BaseService):

    def __init__(self) -> None:
        super().__init__()

    @classmethod
    async def entrar(cls, response: _fastapi.Response, db: _orm.Session, email: str, senha: str) -> [dict | None]:
        with _tracer.tracer.start_as_current_span(f"{cls.__name__}.{inspect.stack()[0][3]}") as span:
            span.set_attribute("parametro_email", email)
            span.set_attribute("parametro_senha", senha)
            try:

                # email = request.txtEmail
                # if not email:
                #     email = request.username
                #
                # senha = request.txtSenha
                # if not senha:
                #     senha = request.password

                if not email:
                    raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_400_BAD_REQUEST, detail='E-mail não informado!')

                if not senha:
                    raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_400_BAD_REQUEST, detail='Senha não informada!')

                usuario = await UsuarioRepository.get_by_email_full(db=db, email=email)
                if not usuario:
                    raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_404_NOT_FOUND, detail='Usuário/Senha Inválido.')

                if usuario.situacao == 'X':  # X-Bloqueado
                    # Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-02', mensagem='Usuário Bloqueado. <br>IP: ' + str(request.remote_addr))
                    raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_400_BAD_REQUEST, detail='Usuário Bloqueado. <br/>Contate o Suporte do Site.')

                if usuario.situacao != 'A':  # A-Ativo
                    # Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-02', mensagem='Usuário não está Ativo. <br>IP: ' + str(request.remote_addr))
                    raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_400_BAD_REQUEST, detail='Usuário não está Ativo.')

                if not usuario.validar_senha(senha=senha):
                    #UsuarioLog().registrar(id_usuario=usuario.id, situacao='I')   # I-Senha Invalida
                    usuario.tentatia += 1
                    #Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-02', mensagem='Tentativa de login ' + str(usuario.tentatia) + '/3. <br>IP: ' + str(request.remote_addr))
                    if usuario.tentatia >= 3:
                        #UsuarioLog().registrar(id_usuario=usuario.id, situacao='B')  # B-Inativar Usuario
                        usuario.situacao = 'I'  # I-Inativo
                        usuario.salvar()
                        #Alerta.registrar(id_usuario=usuario.id, tipo='LOGIN-03', mensagem='Usuário inativado por tentativas de login. <br>IP: ' + str(request.remote_addr))
                        raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_400_BAD_REQUEST, detail='Usuário Inativo por Tentativas de Login com senha Inválida.')
                    usuario.salvar()
                    raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_400_BAD_REQUEST, detail='Usuário/Senha Inválido.')

                if usuario.tentatia > 0 or usuario.situacao != 'A':  # A-Ativo
                    usuario.tentatia = 0
                    usuario.situacao = 'A'  # A-Ativo
                    usuario.salvar()

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

                # login_user(user=usuario, remember=True, duration=timedelta(hours=1))
                # UsuarioLog().registrar(id_usuario=usuario.id, situacao=origem)

                foto = usuario.foto

                # if foto:
                #     foto = current_app.config['IMAGE_UPLOADS'] + '/' + foto
                #     foto = foto[1:]

                #access_token = _token.create_access_token(data={"sub": usuario.email, "id": usuario.id})
                #print("access_token_1", access_token)

                access_token = manager.create_access_token(data=dict(sub=email, id=usuario.id), expires=timedelta(hours=12))
                manager.set_cookie(response=response, token=access_token)
                # response.set_cookie(key='session_id', value=session['session_id'], httponly=True)

                dados = dict({
                    "token_type": "bearer",
                    "access_token": access_token,
                    "Id": str(usuario.id),
                    "Tipo": str(usuario.tipo),
                    "Nome": str(usuario.nome),
                    "Foto": str(foto) if foto else '',
                    "Email": str(usuario.email),
                })

                # return get_json_retorno_dados(rslt='OK', dados=dados)
                # return {"access_token": access_token, "token_type": "bearer"}
                # return {"data": {"Resultado": "OK", "Mensagem": "", "Dados": dados}}
                return dados

            except Exception as e:
                span.record_exception(e)
                #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
                # raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
                return {"data": {"Resultado": "FALHA", "Mensagem": str(e.detail) if e.detail else str(e), "Dados": {}}}



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
