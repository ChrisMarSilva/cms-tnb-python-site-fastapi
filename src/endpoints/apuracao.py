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


router = _fastapi.APIRouter(prefix="/apuracao", tags=['apuracao'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
async def get_index(request: _fastapi.Request):
    # id_usuario = current_user.id
    # gerar_portoflio = False
    # if not gerar_portoflio and UsuarioACAOEmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioFiiFundoImobLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioETFIndiceLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioBDREmpresaLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # if not gerar_portoflio and UsuarioCriptoLancamento.buscar_quant_operacao(id_usuario=id_usuario, situacao='P') > 0: gerar_portoflio = True
    # return render_template(template_name_or_list="apuracao.html", gerar_portoflio=gerar_portoflio)
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


@router.get(path='/listaAno', status_code=_fastapi.status.HTTP_200_OK)
async def lista_ano(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/config', status_code=_fastapi.status.HTTP_200_OK)
async def config(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/salvarconfig', status_code=_fastapi.status.HTTP_200_OK)
async def salvar_config(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
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


@router.get(path='/gridResumida', status_code=_fastapi.status.HTTP_200_OK)
@router.get(path='/gridresumida', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridresumidaportipo', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida_por_tipo(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridResumidaAcaoComum', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida_acao_comum(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridResumidaAcaoDayTrade', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida_acao_daytrade(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridResumidaFii', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida_fii(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridResumidaEtfComum', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida_etf_comum(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridResumidaEtfDayTrade', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida_etf_daytrade(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridResumidaBdrComum', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida_bdr_comum(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridResumidaBdrDayTrade', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida_bdr_daytrade(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridResumidaCripto', status_code=_fastapi.status.HTTP_200_OK)
async def grid_resumida_cripto(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/carregar', status_code=_fastapi.status.HTTP_200_OK)
async def carregar(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/salvar', status_code=_fastapi.status.HTTP_200_OK)
async def salvar(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass


@router.get(path='/gridVendas', status_code=_fastapi.status.HTTP_200_OK)
@router.get(path='/gridvendas', status_code=_fastapi.status.HTTP_200_OK)
async def grid_vendas(db: _orm.Session = _fastapi.Depends(_database.base.get_db), current_user=_fastapi.Depends(manager)):
    with _tracer.tracer.start_as_current_span(f"{str(os.path.basename(__file__).replace('.py', ''))}.{inspect.stack()[0][3]}") as span:
        # dados = await xxxxService.xxxxxxx(db=db)
        # return dados
        pass
