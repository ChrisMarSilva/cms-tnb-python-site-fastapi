# -*- coding: utf-8 -*-
import sys
import os
import fastapi as _fastapi
# from flask_login import current_user
# #from app.tracing import tracing
# from app.cache import cache
# from app.optimize import flask_optimize
# from flask_mail import Message
# from app.models.log_erro import LogErro
# from app.mail import mail
# from app.util.util_json import get_json_retorno_metodo


router = _fastapi.APIRouter(prefix="/contato", tags=['contato'])


@router.get(path='/', status_code=_fastapi.status.HTTP_200_OK)
# @flask_optimize.optimize(cache='GET-1')  # 1seg
async def get_index():
    # if current_user.is_authenticated:
    #     return redirect(location=url_for('principal.index'))
    # return render_template(template_name_or_list="contato.html")
    return {"result": "ok"}


# @bp_contato.route('/enviarMensagem', methods=['GET', 'POST'])
# # @tracing.trace()
# @flask_optimize.optimize('json')
# def enviar_mensagem():
#     try:
#
#         data = None
#         if request.method == 'POST':
#             data = request.form
#         elif request.method == 'GET':
#             data = request.args
#
#         if not data: data = request.get_json(silent=True)
#         if not data: return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         try:
#             nome = data.get('txtContatoNome')
#             email = data.get('txtContatoEmail')
#             assunto = data.get('txtContatoAssunto')
#         except:
#             return make_response(get_json_retorno_metodo(msg='Dados não informado!'), 200)
#
#         mensagem = data.get('txtContatoMensagem')
#
#         if not nome: return make_response(get_json_retorno_metodo(msg='Nome não informado.'), 200)
#         if not email: return make_response(get_json_retorno_metodo(msg='Email não informado.'), 200)
#         if not assunto: return make_response(get_json_retorno_metodo(msg='Assunto não informado.'), 200)
#         if not mensagem: return make_response(get_json_retorno_metodo(msg='Mensagem não informada.'), 200)
#
#         # import re
#         # if re.search("@gm(ia|a|i)l.com$", example):
#         #     return make_response(get_json_retorno_metodo(msg='E-mail inválido.'), 200)
#
#         html = ''
#         html += "<strong>Nome</strong>: "+nome+"<br/>"
#         html += "<strong>Email</strong>: "+email+"<br/>"
#         html += "<strong>Assunto</strong>: "+assunto+"<br/>"
#         html += "<strong>Mensagem</strong>: "+mensagem+"<br/>"
#
#         sender = "suporte@tamonabolsa.com.br" # "chris.mar.silva@gmail.com"
#         mail.send(Message(subject='TnB - Contato', html=html, sender=sender, recipients=[sender], charset='UTF-8'))
#
#         return make_response(get_json_retorno_metodo(rslt='OK', msg='Mensagem enviada com sucesso!'), 200)
#
#     except Exception as e:
#         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '')), linha=int(sys.exc_info()[-1].tb_lineno))
#         return make_response(get_json_retorno_metodo(rslt='FALHA', msg=LogErro.descricao_erro(texto=str(e))), 200)
