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


router = _fastapi.APIRouter(prefix="/IRPF", tags=['irpf'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
async def get_index(request: _fastapi.Request):
    # id_usuario = current_user.id
    # gerar_portoflio = False
    # if not gerar_portoflio and UsuarioACAOEmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioFiiFundoImobLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioETFIndiceLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioBDREmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and  UsuarioCriptoLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # return render_template(template_name_or_list="irpf.html", gerar_portoflio=gerar_portoflio)
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


@router.get(path='/listaAno', status_code=_fastapi.status.HTTP_200_OK)
async def lista_ano(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridIsentos', status_code=_fastapi.status.HTTP_200_OK)
async def grid_isentos(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridIsentosDetalhe', status_code=_fastapi.status.HTTP_200_OK)
async def grid_isentos_detalhe(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridTributaveis', status_code=_fastapi.status.HTTP_200_OK)
async def grid_tributaveis(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridTributaveisDetalhe', status_code=_fastapi.status.HTTP_200_OK)
async def grid_tributaveis_detalhe(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridBensEDiretos', status_code=_fastapi.status.HTTP_200_OK)
async def grid_bens_e_diretos(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridBensEDiretosDetalhe', status_code=_fastapi.status.HTTP_200_OK)
async def ggrid_bens_e_diretos_detalhe(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridRendaVariavel', status_code=_fastapi.status.HTTP_200_OK)
async def grid_renda_variavel(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridRendaVariavelFII', status_code=_fastapi.status.HTTP_200_OK)
async def grid_renda_variavel_fii(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass
