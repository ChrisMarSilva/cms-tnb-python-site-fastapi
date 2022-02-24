# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import login_required
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
#
#
# bp_intrinseco = Blueprint('intrinseco', __name__, url_prefix='/intrinseco')
#
#
# @bp_intrinseco.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# #@flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def index():
#     return render_template(template_name_or_list="intrinseco.html")
