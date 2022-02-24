# -*- coding: utf-8 -*-
import sys
import os
import asyncio
import threading
from multiprocessing import Process, Queue
import multiprocessing
import time
import subprocess
from functools import wraps
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from app.models.usuario import Usuario
# from app.models.usuario_log import UsuarioLog
# from app.models.log_erro import LogErro
# from app.util.util_datahora import pegar_data_atual, converter_datetime_str, adicionar_dias, buscar_nome_semana
# from app.util.util_json import get_json_retorno_metodo
#
#
# bp_admin_investidor_log = Blueprint('admin_investidor_log', __name__, url_prefix='/admin_investidor_log')
#
#
# def install_00():
#     try:
#         os.system('pip install --upgrade pip')
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#
#
# def install_01(package):
#     try:
#         os.system('pip install ' + package)
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#
#
# def install_02(package):
#     try:
#         subprocess.call(['pip', 'install', package])
#         subprocess.check_call([sys.executable, "-m", "pip", "install", package])
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#
#
# def install_03(package):
#     try:
#         import pip
#         pip.main(['install', package])
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#
#
# @bp_admin_investidor_log.route('/')
# @login_required
# # @tracing.trace()
# # @cache.cached(timeout=60)
# #@flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
# def index():
#
#     if str(current_user.tipo) != 'A':
#         return redirect(location=url_for('principal.index'))
#
#     lista_datas, lista_grid = get_lista_grid()
#
#     # install_00()
#
#     # install_01('numpy')
#     # install_02('numpy')
#     # install_03('numpy')
#
#     # install_01('pandas')
#     # install_02('pandas')
#     # install_03('pandas')
#
#     # install_01('beautifulsoup4')
#     # install_02('beautifulsoup4')
#     # install_03('beautifulsoup4')
#
#     # install_01('flask')
#     # install_02('flask')
#     # install_03('flask')
#
#     # install_01('mysql-connector-python')
#     # install_02('mysql-connector-python')
#     # install_03('mysql-connector-python')
#
#     # install_01('sqlalchemy')
#     # install_02('sqlalchemy')
#     # install_03('sqlalchemy')
#
#     # install_01('numpy-financial')
#     # install_02('numpy-financial')
#     # install_03('numpy-financial')
#
#     # install_01('pandas-datareader')
#     # install_02('pandas-datareader')
#     # install_03('pandas-datareader')
#
#     # install_01('pip-upgrader')
#     # install_02('pip-upgrader')
#     # install_03('pip-upgrader')
#
#     # install_01('pyfolio')
#     # install_02('pyfolio')
#     # install_03('pyfolio')
#
#     # install_01('pymysql')
#     # install_02('pymysql')
#     # install_03('pymysql')
#
#     # install_01('seaborn')
#     # install_02('seaborn')
#     # install_03('seaborn')
#
#     # install_01('yfinance')
#     # install_02('yfinance')
#     # install_03('yfinance')
#
#     #import sys as s
#     #lista_keys = s.modules.keys()
#
#     # import pkg_resources
#     # # lista_keys = {d.project_name: d.version for d in pkg_resources.working_set}
#     # lista_keys = sorted(["%s==%s" % (i.key, i.version) for i in pkg_resources.working_set])
#
#     lista_keys_1 = []
#     # try:
#     #     tam = len(lista_keys)
#     #     numero_cada = round(tam/3)
#     #     lista_keys_1 = lista_keys[:numero_cada]
#     # except Exception as e:
#     #     pass
#
#     lista_keys_2 = []
#     # try:
#     #     lista_keys_2 = lista_keys[numero_cada:numero_cada*2]
#     # except Exception as e:
#     #     pass
#
#     lista_keys_3 = []
#     # try:
#     #     lista_keys_3 = lista_keys[numero_cada*2:]
#     # except Exception as e:
#     #     pass
#
#     # import asyncio
#     # async def teste1():
#     #     await asyncio.sleep(2)
#     # async def teste2():
#     #     await asyncio.sleep(2)
#     # loop = asyncio.new_event_loop()  # get_event_loop
#     # try:
#     #     asyncio.set_event_loop(loop)
#     #     tasks = [asyncio.Task(teste1()), asyncio.Task(teste2()), ]
#     #     results = loop.run_until_complete(asyncio.gather(*tasks))
#     # finally:
#     #     try:
#     #         loop.close()
#     #     except:
#     #         pass
#
#     return render_template(
#         template_name_or_list="admin_investidor_log.html",
#         lista_datas=lista_datas,
#         lista_grid=lista_grid,
#         lista_keys_1=lista_keys_1,
#         lista_keys_2=lista_keys_2,
#         lista_keys_3=lista_keys_3,
#     )
#
#
# def get_lista_grid():
#     try:
#
#         data_atual = pegar_data_atual(istext=False)
#         data_1_dia = converter_datetime_str(data=data_atual + adicionar_dias(dias=-1), istext=False)
#         data_2_dia = converter_datetime_str(data=data_atual + adicionar_dias(dias=-2), istext=False)
#         data_3_dia = converter_datetime_str(data=data_atual + adicionar_dias(dias=-3), istext=False)
#         data_4_dia = converter_datetime_str(data=data_atual + adicionar_dias(dias=-4), istext=False)
#         data_5_dia = converter_datetime_str(data=data_atual + adicionar_dias(dias=-5), istext=False)
#         data_6_dia = converter_datetime_str(data=data_atual + adicionar_dias(dias=-6), istext=False)
#
#         lista_datas = [
#             [converter_datetime_str(data=data_6_dia, fmt="%d/%m/%Y"), buscar_nome_semana(semana=data_6_dia.weekday())],
#             [converter_datetime_str(data=data_5_dia, fmt="%d/%m/%Y"), buscar_nome_semana(semana=data_5_dia.weekday())],
#             [converter_datetime_str(data=data_4_dia, fmt="%d/%m/%Y"), buscar_nome_semana(semana=data_4_dia.weekday())],
#             [converter_datetime_str(data=data_3_dia, fmt="%d/%m/%Y"), buscar_nome_semana(semana=data_3_dia.weekday())],
#             [converter_datetime_str(data=data_2_dia, fmt="%d/%m/%Y"), buscar_nome_semana(semana=data_2_dia.weekday())],
#             [converter_datetime_str(data=data_1_dia, fmt="%d/%m/%Y"), buscar_nome_semana(semana=data_1_dia.weekday())],
#             [converter_datetime_str(data=data_atual, fmt="%d/%m/%Y"), buscar_nome_semana(semana=data_atual.weekday())]
#         ]
#
#         data_atual = converter_datetime_str(data=data_atual, fmt="%Y%m%d")
#         data_1_dia = converter_datetime_str(data=data_1_dia, fmt="%Y%m%d")
#         data_2_dia = converter_datetime_str(data=data_2_dia, fmt="%Y%m%d")
#         data_3_dia = converter_datetime_str(data=data_3_dia, fmt="%Y%m%d")
#         data_4_dia = converter_datetime_str(data=data_4_dia, fmt="%Y%m%d")
#         data_5_dia = converter_datetime_str(data=data_5_dia, fmt="%Y%m%d")
#         data_6_dia = converter_datetime_str(data=data_6_dia, fmt="%Y%m%d")
#
#         lista_grid = []
#
#         rows = Usuario.buscar_todos(dt_ini=str(data_6_dia)+'000000000', dt_fim=str(data_atual)+'235959000')
#
#         for indx, row in enumerate(rows):
#
#             id_user = int(row['ID'])
#
#             status_site_01 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_6_dia), situacao='L')
#             status_site_02 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_5_dia), situacao='L')
#             status_site_03 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_4_dia), situacao='L')
#             status_site_04 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_3_dia), situacao='L')
#             status_site_05 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_2_dia), situacao='L')
#             status_site_06 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_1_dia), situacao='L')
#             status_site_07 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_atual), situacao='L')
#
#             status_app_01 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_6_dia), situacao='P')
#             status_app_02 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_5_dia), situacao='P')
#             status_app_03 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_4_dia), situacao='P')
#             status_app_04 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_3_dia), situacao='P')
#             status_app_05 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_2_dia), situacao='P')
#             status_app_06 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_1_dia), situacao='P')
#             status_app_07 = UsuarioLog.buscar_teve_acesso(id_usuario=id_user, data=str(data_atual), situacao='P')
#
#             lista_grid.append([
#                 str(int(indx)+1),
#                 str(id_user),
#                 str(row['NOME']),
#                 str(row['EMAIL']),
#                 'SITE' if str(status_site_01) == 'S' else '...',
#                 'APP' if str(status_app_01) == 'S' else '...',
#                 'SITE' if str(status_site_02) == 'S' else '...',
#                 'APP' if str(status_app_02) == 'S' else '...',
#                 'SITE' if str(status_site_03) == 'S' else '...',
#                 'APP' if str(status_app_03) == 'S' else '...',
#                 'SITE' if str(status_site_04) == 'S' else '...',
#                 'APP' if str(status_app_04) == 'S' else '...',
#                 'SITE' if str(status_site_05) == 'S' else '...',
#                 'APP' if str(status_app_05) == 'S' else '...',
#                 'SITE' if str(status_site_06) == 'S' else '...',
#                 'APP' if str(status_app_06) == 'S' else '...',
#                 'SITE' if str(status_site_07) == 'S' else '...',
#                 'APP' if str(status_app_07) == 'S' else '...',
#             ])
#
#         return lista_datas, lista_grid
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return []
#
#
# @bp_admin_investidor_log.route('/testetimenormal', methods=['GET', 'POST'])
# @flask_optimize.optimize('json')
# def teste_time():
#     #start = time.time()
#     #print('ASYNC NORMAL INI')
#
#     get_time()
#     get_time()
#     get_time()
#
#     # queue = Queue()
#     # threads = []
#     # thread = threading.Thread(target=get_time, args=(queue, 1))
#     # # thread = multiprocessing.Process(get_time=calc_square, args=(queue,))
#     # threads.append(thread)
#     # thread.start()
#     # thread = threading.Thread(target=get_time, args=(queue, 2))
#     # # thread = multiprocessing.Process(get_time=calc_square, args=(queue,))
#     # threads.append(thread)
#     # thread.start()
#     # thread = threading.Thread(target=get_time, args=(queue, 3))
#     # # thread = multiprocessing.Process(get_time=calc_square, args=(queue,))
#     # threads.append(thread)
#     # thread.start()
#     # for thread in threads:
#     #     thread.join()
#     #     result = queue.get()
#     #     print(result)
#
#     #diff = int((time.time() - start) * 1000)
#     #print('ASYNC NORMAL FIM', diff)
#     return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
# @bp_admin_investidor_log.route('/testetimeasync', methods=['GET', 'POST'])
# @flask_optimize.optimize('json')
# def teste_time_async():
#     #start = time.time()
#     #print('ASYNC PRINC INI')
#     # asyncio.set_event_loop(asyncio.new_event_loop())
#     # loop = asyncio.get_event_loop()
#     # #result = loop.run_until_complete(get_time())
#     # tasks = [asyncio.Task(get_time_async()), asyncio.Task(get_time_async()), asyncio.Task(get_time_async()), ]
#     # loop.run_until_complete(asyncio.gather(*tasks))
#     loop = asyncio.new_event_loop()
#     try:
#         asyncio.set_event_loop(loop)
#         # loop.run_until_complete(get_time_async())
#         tasks = [asyncio.Task(get_time_async()), asyncio.Task(get_time_async()), asyncio.Task(get_time_async()),]
#         loop.run_until_complete(asyncio.gather(*tasks))
#     finally:
#         loop.close()
#     #diff = int((time.time() - start) * 1000)
#     #print('ASYNC PRINC FIM', diff)
#     return make_response(get_json_retorno_metodo(rslt='OK'), 200)
#
#
# @asyncio.coroutine
# async def get_time_async() -> None:
#     #print(' ==> ASYNC INI')
#     #start = time.time()
#     #await asyncio.sleep(5)
#     get_time()
#     #diff = int((time.time() - start) * 1000)
#     #print(' ==> ASYNC FIM', diff)
#
# def get_time():
#     #print(' ==> NORMAL INI')
#     #start = time.time()
#     time.sleep(5)
#     #diff = int((time.time() - start) * 1000)
#     #print(' ==> NORMAL FIM', diff)