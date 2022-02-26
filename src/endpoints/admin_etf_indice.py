# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="/admin_etf_indice", tags=['admin_etf_indice'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
# @login_required
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
async def get_index(request: _fastapi.Request):
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="admin_etf_indice.html")
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})
