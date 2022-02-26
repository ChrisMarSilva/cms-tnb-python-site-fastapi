# -*- coding: utf-8 -*-
import sys
import os
import asyncio
import fastapi as _fastapi
# from flask_login import login_required, current_user
# #from app.tracing import tracing
# from app.optimize import flask_optimize
# from app.cache import cache
# from app.models.log_erro import LogErro
# from app.models.admin_consulta import AdminConsulta
# from app.util.util_json import get_json_retorno_grid
from src.config.config_templates import templates as _templates


router = _fastapi.APIRouter(prefix="/AdminConsulta", tags=['admin_consulta'])


@router.get(path='/', response_class=_fastapi.responses.HTMLResponse)
# @login_required
# @flask_optimize.optimize(cache='GET-84600')  # 84600seg/1410Min/23,5Hr
async def get_index(request: _fastapi.Request):
    # if str(current_user.tipo) != 'A':
    #     return redirect(location=url_for('principal.index'))
    # lista_tabelas = get_lista_tabelas()
    # lista_campos = get_lista_campos()
    # return render_template(template_name_or_list="admin_consulta.html", lista_tabelas=lista_tabelas, lista_campos=lista_campos)
    return _templates.TemplateResponse("index.html", {"request": request, "pagina": "home"})


# @bp_admin_consulta.route('/ComandoSQL', methods=['GET', 'POST'])
# @login_required
# # @tracing.trace()
# @flask_optimize.optimize('text')
# def comando_sql():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return 'Usuário não está Permitido! Somente para Administradores.'
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return 'Dados não informado!'
#
#         try:
#             query = data.get('ComandoSQL')
#         except:
#             return 'Dados não informado!'
#
#         if not query:
#             return '<p>Comando SQL não informado...</p>'
#
#         comando_proibido = 'INSERT INTO'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'INSERT'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'DELETE'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'TRUNCATE TABLE'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         #  comando_proibido = 'TRUNCATE'
#         #  if str(comando).upper().find(comando_proibido) >= 0:
#         #   comando = str(comando).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#         #   return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(comando) + '</p>'
#
#         comando_proibido = 'UPDATE'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'ALTER'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'DROP'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'CREATE'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'COMMIT'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'ROLLBACK'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'EXECUTE'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         comando_proibido = 'GRANT'
#         if str(query).upper().find(comando_proibido) >= 0:
#             query = str(query).replace(comando_proibido, '<b class="text-danger">' + str(comando_proibido) + '</b>')
#             return '<p><b>Erro: </b>Comando <span class="text-danger">"' + str(comando_proibido) + '"</span> não será executado.</p> <p><b>Comando SQL: </b>' + str(query) + '</p>'
#
#         rows = AdminConsulta.buscar_consulta_dinamica(query=query)
#
#         comando_sql_negrito = 'SELECT'
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'COUNT('
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'MAX('
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'MIN('
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'SUM('
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'FROM '
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'INNER JOIN '
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'LEFT JOIN '
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'WHERE '
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'NOT IN '
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'NOT EXISTS('
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'ORDER BY '
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'GROPU BY '
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#         comando_sql_negrito = 'HAVING '
#         query = str(query).replace(comando_sql_negrito, '<br/><b class="text-primary">' + str(comando_sql_negrito) + '</b>')
#
#         result = ''
#
#         result += '<div class="row clearfix">'
#         result += '  <span class="col-xl-12 col-lg-12 col-md-12 col-sm-12"> <b>Comando SQL: </b> ' + str(query) + ' </div> '
#         result += '</div> '
#
#         result += '<br/> '
#
#         result += '<div class="row clearfix">'
#         result += '  <span class="col-xl-12 col-lg-12 col-md-12 col-sm-12"> <b>Qtde Registros: </b> ' + str(rows.rowcount) + ' </div> '
#         result += '</div> '
#
#         result += '<br/> '
#
#         result += '<div class="table-responsive">'
#         result += '<table border="1" width="100%" class="table table-sm table-striped table-bordered table-hover">'
#
#         result += '<thead class="thead-dark">'
#         result += '<tr>'
#         for col in rows.keys():
#             result += '<th scope="col">' + str(col) + '</th>'
#         result += '</tr>'
#         result += '</thead>'
#
#         result += '<tbody>'
#         for row in rows:
#             result += '<tr>'
#             indx_col = 0
#             for col in rows.keys():
#                 if indx_col == 0: result += '<th scope="row">' + str(row[str(col)]) +'</th>'
#                 if indx_col != 0: result += '<td>' + str(row[str(col)]) +'</td>'
#                 indx_col += 1
#             result += '</tr>'
#         result += '</tbody>'
#
#         if int(rows.rowcount) > 10:
#             result += '<tfoot>'
#             result += '<tr class="bg-dark text-white">'
#             for col in rows.keys():
#                 result += '<td>' + str(col) + '</td>'
#             result += '</tr>'
#             result += '</tfoot>'
#
#         result += '</table>'
#         result += '</div>'
#
#         return result
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return LogErro.descricao_erro(texto=str(e))
#
#
# def get_lista_tabelas():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return []
#
#         rows = AdminConsulta.buscar_tabelas()
#
#         lista = [str(row['TABLE_NAME']).upper() for row in rows]
#
#         return lista
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return []
#
#
# def get_lista_campos():
#     try:
#
#         if str(current_user.tipo) != 'A':
#             return get_json_retorno_grid(msg='Usuário não está Permitido! Somente para Administradores.')
#
#         rows = AdminConsulta.buscar_campos()
#
#         lista = [[str(row['TABLE_NAME']).upper(), str(row['COLUMN_NAME']).upper(), str(row['COLUMN_KEY']).upper()] for row in rows]
#
#         return get_json_retorno_grid(rslt='OK', lista=lista)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return get_json_retorno_grid(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e)))
#
