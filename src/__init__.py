import time
import datetime as dt
import fastapi as _fastapi
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
import src.endpoints as _endpoints
import src.database as _database
import src.config.config_trace as _tracer


def create_app() -> _fastapi.FastAPI:

    _tracer.config_trace_init()

    app = _fastapi.FastAPI(title='TamoNaBolsa', version="2.0.0", openapi_url="/api/v1/openapi.json", debug=True)
    app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.mount("/static", _fastapi.staticfiles.StaticFiles(directory="src/static"), name="static")
    _endpoints.init_routers(app=app)

    @app.middleware("http")
    async def add_process_time_header(request: _fastapi.Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        response.headers["Z-Process-Time"] = str(dt.timedelta(seconds=process_time))
        response.headers["X-Status-Code"] = str(response.status_code)
        return response

    @app.exception_handler(Exception)
    def validation_exception_handler(request, err):
        return _fastapi.responses.JSONResponse(status_code=_fastapi.status.HTTP_400_BAD_REQUEST, content={"message": f"Failed to execute: {request.method}: {request.url}. Detail: {err}"})

    from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
    FastAPIInstrumentor.instrument_app(app, tracer_provider=_tracer.provider)

    from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor
    SQLAlchemyInstrumentor().instrument(engine=_database.session.engine)

    # from fastapi_profiler.profiler_middleware import PyInstrumentProfilerMiddleware
    # app.add_middleware(PyInstrumentProfilerMiddleware)

    return app
