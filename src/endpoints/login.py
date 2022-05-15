# -*- coding: utf-8 -*-
import sys
import os
import inspect
import fastapi as _fastapi
import sqlalchemy.orm as _orm
import src.database as _database
import src.config.config_trace as _tracer
from src.config.config_login_manager import manager
from src.config.config_templates import templates as _templates
from fastapi.security import OAuth2PasswordRequestForm
from src.services.login import LoginService
from src.schemas.login import LoginIn


router = _fastapi.APIRouter(prefix="/login", tags=['login'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
async def get_index(request: _fastapi.Request):
    # if current_user.is_authenticated:
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="login.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


@router.post(path="/entrar", status_code=_fastapi.status.HTTP_200_OK)  # , response_model=LoginIn
async def entrar(response: _fastapi.Response, request: LoginIn, db: _orm.Session = _fastapi.Depends(_database.base.get_db)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        span.set_attribute("parametro_request", request)
        dados = await LoginService.entrar(db=db, response=response, email=request.txtEmail, senha=request.txtSenha)
        return dados


@router.post(path="/entrar2", status_code=_fastapi.status.HTTP_200_OK)  # , response_model=LoginIn
async def entrar2(response: _fastapi.Response, request: OAuth2PasswordRequestForm = _fastapi.Depends(), db: _orm.Session = _fastapi.Depends(_database.base.get_db)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        span.set_attribute("parametro_request", request)
        dados = await LoginService.entrar(db=db, response=response, email=request.username, senha=request.password)
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


@router.get(path="/sair", status_code=_fastapi.status.HTTP_200_OK)
async def sair(request: _fastapi.Request, current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass
