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


router = _fastapi.APIRouter(prefix="/comentarios", tags=['comentarios'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
async def get_index(request: _fastapi.Request):
    # return render_template(template_name_or_list="comentarios.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


@router.get(path='/montarMenu', status_code=_fastapi.status.HTTP_200_OK)
async def montar_menu(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/marcarTodosPend', status_code=_fastapi.status.HTTP_200_OK)
async def marcar_todos_pend(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/lista', status_code=_fastapi.status.HTTP_200_OK)
async def lista(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/salvarComentario', status_code=_fastapi.status.HTTP_200_OK)
async def salvar_comentario(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/salvarResposta', status_code=_fastapi.status.HTTP_200_OK)
async def salvar_resposta(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/salvarReacao', status_code=_fastapi.status.HTTP_200_OK)
async def salvar_reacao(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/denunciar', status_code=_fastapi.status.HTTP_200_OK)
async def denunciar(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/excluir', status_code=_fastapi.status.HTTP_200_OK)
async def excluir(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/visualizar', status_code=_fastapi.status.HTTP_200_OK)
async def visualizar(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass
