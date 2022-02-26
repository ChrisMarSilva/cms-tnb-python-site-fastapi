# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="/valuation", tags=['valuation'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
# @login_required
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index(request: _fastapi.Request):
    # return render_template(template_name_or_list="valuation.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})
