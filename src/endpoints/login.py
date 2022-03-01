# -*- coding: utf-8 -*-
# import sys
import os
import inspect
# from datetime import timedelta
import fastapi as _fastapi
from fastapi.security import OAuth2PasswordRequestForm
import sqlalchemy.orm as _orm
# from flask_login import login_user, logout_user, current_user, login_required
# from app.cache import cache, del_cache_all
# # from app.tracing import tracing
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
# from app.models.alerta import Alerta
# from app.models.usuario import Usuario
# from app.models.usuario_log import UsuarioLog
# from src.util.util_json import get_json_retorno_dados  # get_json_retorno_metodo
from src.config.config_templates import templates as _templates
from src.services.login import LoginService
from src.schemas.login import LoginIn
import src.database as _database
import src.config.config_trace as _tracer
# from src.schemas.login import LoginOut
from src.config.config_login_manager import manager


router = _fastapi.APIRouter(prefix="/login", tags=['login'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
# @flask_optimize.optimize(cache='GET-10')  # 10seg
async def get_index(request: _fastapi.Request):
    # if current_user.is_authenticated:
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="login.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


@router.post(path="/entrar", status_code=_fastapi.status.HTTP_200_OK)  # , response_model=LoginIn
# @flask_optimize.optimize('json')
async def entrar(response: _fastapi.Response, request: LoginIn, db: _orm.Session = _fastapi.Depends(_database.base.get_db)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        span.set_attribute("parametro_request", request)
        dados = await LoginService.entrar(db=db, response=response, email=request.txtEmail, senha=request.txtSenha)
        return dados


@router.post(path="/entrar2", status_code=_fastapi.status.HTTP_200_OK)  # , response_model=LoginIn
# @flask_optimize.optimize('json')
async def entrar2(response: _fastapi.Response, request: OAuth2PasswordRequestForm = _fastapi.Depends(), db: _orm.Session = _fastapi.Depends(_database.base.get_db)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        span.set_attribute("parametro_request", request)
        # dados = await LoginService.entrar(db=db, response=response, email=request.username, senha=request.password)
        dados = await LoginService.entrar(db=db, response=response, email="chris.mar.silva@gmail.com", senha="#Chrs2387")
        return dados

'''

async def get_current_user(request: Request): 
    try:
        cookie_authorization: str = request.cookies.get("Authorization")
        # some logic with cookie_authorization
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication"
        )
'''


@router.get(path="/logado", status_code=_fastapi.status.HTTP_200_OK)
async def logado(request: _fastapi.Request, current_user=_fastapi.Depends(manager)):
    try:
        # cookie_session_id: str = request.cookies.get("session_id")
        return {"logado": current_user, "access-token": request.cookies.get("access-token")}
        #return {"logado": current_user, "manager": manager}
    except Exception as e:
        raise _fastapi.HTTPException(status_code=_fastapi.status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


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
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
