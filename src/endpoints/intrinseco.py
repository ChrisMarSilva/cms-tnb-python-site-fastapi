# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro


router = _fastapi.APIRouter(prefix="/intrinseco", tags=['intrinseco'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @login_required
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index():
    # return render_template(template_name_or_list="intrinseco.html")
    return {"result": "ok"}
