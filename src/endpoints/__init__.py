import fastapi as _fastapi
from src.endpoints import UserEndpoint
from src.endpoints import AuthEndpoint


def init_routers(app: _fastapi.FastAPI):
    app.include_router(AuthEndpoint.router)
    app.include_router(UserEndpoint.router)
