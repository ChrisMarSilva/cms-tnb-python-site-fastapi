# import uvicorn
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve
from src import create_app

app = create_app()


if __name__ == "__main__":
    # uvicorn.run("main:app", port=5001, reload=True, workers=1)
    # uvicorn.run("src.app:app", host="127.0.0.1", port=8001, log_level="info", reload=True, debug=True)
    config = Config()
    config.bind = ["127.0.0.1:5001"]
    # config.debug = True
    config.use_reloader = True
    asyncio.run(serve(app, config))

# TnB FastAPI
# 	separar os endpoints
# 	separar as paginas
# 	separar os models
# 	separar os repositories

# python3 -m venv venv
# source venv/Scripts/activate
# cd venv\Scripts
# activate

# pip install --upgrade pip
# pip install fastapi[all] -U
# pip install "uvicorn[standard]" -U
# pip install "hypercorn[trio]" -U
# pip install jinja2 -U
# pip install dependency-injector -U
# pip install sqlalchemy -U
# pip install pytest -U
# pip install pytest-cov -U
# pip install opentelemetry-api -U
# pip install opentelemetry-sdk -U
# pip install opentelemetry-launcher -U
# pip install opentelemetry-instrumentation -U
# pip install opentelemetry-instrumentation-fastapi -U
# pip install opentelemetry-instrumentation-sqlalchemy -U
# pip install opentelemetry-distro -U
# pip install opentelemetry-exporter-jaeger -U
# pip install opentelemetry-exporter-otlp -U
# pip install opentelemetry-instrumentation-logging -U
# pip install "python-jose[cryptography]" -U
# pip install "passlib[bcrypt]" -U
# pip install python-multipart -U
# pip install PyJWT -U
# pip install databases -U
# pip install aiosqlite -U
# pip install fastapi_profiler -U
# pip install requests -U
# pip install bs4 --upgrade
# pip install html5lib --upgrade
# pip install lxml --upgrade
# pip install numpy --upgrade
# pip install pandas --upgrade
# pip install pytz --upgrade
# pip install validate-docbr --upgrade
# pip install Pillow --upgrade
# pip install mysql-connector-python --upgrade
# pip install pymysql --upgrade
# pip install aiomysql --upgrade
# pip install sqltap
# pip install fastapi-login
# pip install 'fastapi-users[sqlalchemy2]'

# uvicorn main:app --reload
# hypercorn main:app --worker-class trio

# pip freeze > requirements.txt
# pip install -r requirements.txt
