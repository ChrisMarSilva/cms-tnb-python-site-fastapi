# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import current_user
# # from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="", tags=['main'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
@router.get(path='/home', response_class=_fastapi.responses.HTMLResponse)
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index1(request: _fastapi.Request):
    # if current_user.is_authenticated:
    #     return redirect(location=url_for('principal.index'))
    # return _templates.TemplateResponse("home.html", {"request": request})
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})
