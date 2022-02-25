# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import current_user
# # from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro


router = _fastapi.APIRouter(prefix="/main", tags=['main'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
@router.get(path='/home', status_code=_fastapi.status.HTTP_200_OK)
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index():
    # if current_user.is_authenticated:
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="home.html")
    return {"result": "ok"}
