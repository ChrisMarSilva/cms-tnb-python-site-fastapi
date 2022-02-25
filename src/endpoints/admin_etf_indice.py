# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro


router = _fastapi.APIRouter(prefix="/admin_etf_indice", tags=['admin_etf_indice'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @login_required
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
async def get_index():
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="admin_etf_indice.html")
    return {"result": "ok"}
