# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import current_user
# # from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.log_erro import LogErro
#
#
# bp_main = Blueprint("main", __name__)
#
#
# @bp_main.route('/')
# @bp_main.route('/home')
# # @tracing.trace()
# # @cache.cached(timeout=60)
# # @flask_optimize.optimize(cache='GET-600')  # 600seg/10Min
# @flask_optimize.optimize(cache='GET-1')  # 1seg
# def home():
#     if current_user.is_authenticated:
#         return redirect(location=url_for('principal.index'))
#     return render_template(template_name_or_list="home.html")
