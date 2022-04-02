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


router = _fastapi.APIRouter(prefix="/admin_investidor_log", tags=['admin_investidor_log'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
async def get_index(request: _fastapi.Request):
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})
    
