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


router = _fastapi.APIRouter(prefix="/usuario", tags=['usuario'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
async def get_index(request: _fastapi.Request):
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


@router.get(path='/criarconta', status_code=_fastapi.status.HTTP_200_OK)
async def criar_conta(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/salvarDadosConta', status_code=_fastapi.status.HTTP_200_OK)
async def salvar_dados_conta(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/ativacao', status_code=_fastapi.status.HTTP_200_OK)
@router.get(path='/ativacao/', status_code=_fastapi.status.HTTP_200_OK)
@router.get(path='/ativacao/:hash', status_code=_fastapi.status.HTTP_200_OK)
async def usuario_ativacao(hash: str = None, db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/sucesso', status_code=_fastapi.status.HTTP_200_OK)
async def usuario_sucesso(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/esqueceusenha', status_code=_fastapi.status.HTTP_200_OK)
async def esqueceu_senha(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/enviarEmailSenha', status_code=_fastapi.status.HTTP_200_OK)
async def enviar_email_senha(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/redefinirsenha', status_code=_fastapi.status.HTTP_200_OK)
@router.get(path='/redefinirsenha/', status_code=_fastapi.status.HTTP_200_OK)
@router.get(path='/redefinirsenha/:hash', status_code=_fastapi.status.HTTP_200_OK)
async def usuario_redefinir_senha(hash: str = None,db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/SalvarNovaSenha', status_code=_fastapi.status.HTTP_200_OK)
@router.get(path='/salvarNovaSenha', status_code=_fastapi.status.HTTP_200_OK)
@router.get(path='/salvarnovasenha', status_code=_fastapi.status.HTTP_200_OK)
async def salvar_nova_senha(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass

@router.get(path='/sucessoredefinirsenha', status_code=_fastapi.status.HTTP_200_OK)
async def sucesso_redefinir_senha(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass
