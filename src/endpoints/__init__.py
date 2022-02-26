import fastapi as _fastapi
from src.endpoints import AAUserEndpoint
from src.endpoints import admin_alerta
from src.endpoints import admin_bdr
from src.endpoints import admin_consulta
from src.endpoints import admin_cripto
from src.endpoints import admin_cripto_foxbit
from src.endpoints import admin_empresa
from src.endpoints import admin_empresa_cotacao
from src.endpoints import admin_empresa_proventos
from src.endpoints import admin_etf
from src.endpoints import admin_etf_indice
from src.endpoints import admin_etf_indice_cotacao
from src.endpoints import admin_fundoimob
from src.endpoints import admin_fundoimob_cotacao
from src.endpoints import admin_fundoimob_proventos
from src.endpoints import admin_investidor
from src.endpoints import admin_investidor_log
from src.endpoints import admin_listas
from src.endpoints import admin_log_erros
from src.endpoints import admin_testes
from src.endpoints import aluguel
from src.endpoints import analise
from src.endpoints import apuracao
from src.endpoints import ativo
from src.endpoints import calendario
from src.endpoints import cei
from src.endpoints import comentarios
from src.endpoints import contato
from src.endpoints import corretora
from src.endpoints import fatos
from src.endpoints import finan_acoes
from src.endpoints import intrinseco
from src.endpoints import irpf
from src.endpoints import login
from src.endpoints import main
from src.endpoints import operacoes
from src.endpoints import perfil
from src.endpoints import portfolio
from src.endpoints import principal
from src.endpoints import proventos
from src.endpoints import radar
from src.endpoints import usuario
from src.endpoints import valorizacao
from src.endpoints import valuation


def init_routers(app: _fastapi.FastAPI):
    app.include_router(AAUserEndpoint.router)
    # app.include_router(admin_alerta.router)
    # app.include_router(admin_bdr.router)
    # app.include_router(admin_consulta.router)
    # app.include_router(admin_cripto.router)
    # app.include_router(admin_cripto_foxbit.router)
    # app.include_router(admin_empresa.router)
    # app.include_router(admin_empresa_cotacao.router)
    # app.include_router(admin_empresa_proventos.router)
    # app.include_router(admin_etf.router)
    # app.include_router(admin_etf_indice.router)
    # app.include_router(admin_etf_indice_cotacao.router)
    # app.include_router(admin_fundoimob.router)
    # app.include_router(admin_fundoimob_cotacao.router)
    # app.include_router(admin_fundoimob_proventos.router)
    # app.include_router(admin_investidor.router)
    # app.include_router(admin_investidor_log.router)
    # app.include_router(admin_listas.router)
    # app.include_router(admin_log_erros.router)
    # app.include_router(admin_testes.router)
    # app.include_router(aluguel.router)
    # app.include_router(analise.router)
    # app.include_router(apuracao.router)
    # app.include_router(ativo.router)
    # app.include_router(calendario.router)
    # app.include_router(cei.router)
    # app.include_router(comentarios.router)
    # app.include_router(contato.router)
    # app.include_router(corretora.router)
    # app.include_router(fatos.router)
    # app.include_router(finan_acoes.router)
    # app.include_router(intrinseco.router)
    # app.include_router(irpf.router)
    app.include_router(login.router)
    app.include_router(main.router)
    # app.include_router(operacoes.router)
    # app.include_router(perfil.router)
    # app.include_router(portfolio.router)
    # app.include_router(principal.router)
    # app.include_router(proventos.router)
    # app.include_router(radar.router)
    # app.include_router(usuario.router)
    # app.include_router(valorizacao.router)
    # app.include_router(valuation.router)
