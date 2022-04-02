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


router = _fastapi.APIRouter(prefix="/cei", tags=['cei'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
async def get_index(request: _fastapi.Request):
    # user_cpf = ''
    # user_dthr = ''
    # user_sit = 'I'
    # title_cor = 'text-danger'
    # id_usuario = current_user.id
    # usuario_cei = UsuarioCei.get_by_usuario(id_usuario=id_usuario)
    # if usuario_cei:
    #     user_cpf = usuario_cei.cpf
    #     user_dthr = usuario_cei.dthr_alteracao_format()
    #     user_sit = usuario_cei.situacao
    #     if user_dthr != '':
    #         title_cor = 'text-success'
    # return render_template(template_name_or_list="cei.html", user_cpf=user_cpf, user_dthr=user_dthr, user_sit=user_sit, title_cor=title_cor)
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


@router.get(path='/salvar', status_code=_fastapi.status.HTTP_200_OK)
async def salvar(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/grid', status_code=_fastapi.status.HTTP_200_OK)
async def grid(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/alterarsituacao', status_code=_fastapi.status.HTTP_200_OK)
async def alterar_situacao(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/alterarlistasituacao', status_code=_fastapi.status.HTTP_200_OK)
async def alterar_lista_situacao(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridprov', status_code=_fastapi.status.HTTP_200_OK)
async def grid_prov(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/alterarsituacaoprov', status_code=_fastapi.status.HTTP_200_OK)
async def alterar_situacao_prov(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/alterarlistasituacaoprov', status_code=_fastapi.status.HTTP_200_OK)
async def alterar_lista_situacao_prov(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass
