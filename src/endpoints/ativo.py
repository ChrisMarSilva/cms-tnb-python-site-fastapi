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


router = _fastapi.APIRouter(prefix="/ativo", tags=['ativo'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
async def get_index(request: _fastapi.Request):
    # return render_template(template_name_or_list="ativo.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


@router.get(path='/grid', status_code=_fastapi.status.HTTP_200_OK)
async def grid(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/carregargrupo', status_code=_fastapi.status.HTTP_200_OK)
async def carregar_grupo(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/salvargrupo', status_code=_fastapi.status.HTTP_200_OK)
async def salvar_grupo(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/salvarativo', status_code=_fastapi.status.HTTP_200_OK)
async def salvar_ativo(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/excluirgrupo', status_code=_fastapi.status.HTTP_200_OK)
async def excluir_grupo(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/excluirativo', status_code=_fastapi.status.HTTP_200_OK)
async def excluir_ativo(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass
