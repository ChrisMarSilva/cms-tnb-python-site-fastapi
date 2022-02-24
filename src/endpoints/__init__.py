import fastapi as _fastapi
from src.endpoints import AAUserEndpoint
from src.endpoints import AAuthEndpoint


def init_routers(app: _fastapi.FastAPI):
    app.include_router(AAuthEndpoint.router)
    app.include_router(AAUserEndpoint.router)
