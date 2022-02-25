# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required
# from app.optimize import flask_optimize


router = _fastapi.APIRouter(prefix="/radar", tags=['radar'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @login_required
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index():
    # return render_template(template_name_or_list="radar.html")
    return {"result": "ok"}
