# # -*- coding: utf-8 -*-
# import sys
# import os
# from flask_login import current_user
# from app.banco import db
# from app.util.util_datahora import pegar_data_hora_atual, converter_str_to_datetime, converter_datetime_str


# class LogErro(db.Model):

#     __tablename__ = "TBLOGERRO"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True, nullable=False)
#     data_hora = db.Column('DATAHORA', db.String(20), nullable=False, index=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=True)
#     arquivo = db.Column('ARQUIVO', db.String(250), nullable=True)
#     linha = db.Column('LINHA', db.Integer, nullable=True)
#     codigo = db.Column('CODIGO', db.Integer, nullable=True)
#     texto = db.Column('TEXTO', db.Text(), nullable=False)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, data_hora: str = None, id_usuario: int = None, arquivo: str = None,
#                  linha: int = None, codigo: int = None, texto: str = None, situacao: str = None):
#         self.id = id
#         self.data_hora = data_hora
#         self.id_usuario = id_usuario
#         self.arquivo = arquivo
#         self.linha = linha
#         self.codigo = codigo
#         self.texto = texto
#         self.situacao = situacao

#     @classmethod
#     def find_all(cls):
#         try:
#             return cls.query.order_by(cls.data_hora, cls.id).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def find_by_id(cls, id: int):
#         try:
#             return cls.query.filter_by(id=id).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls, situacao : str = None):
#         query = """ SELECT E.ID, E.DATAHORA, E.IDUSUARIO, U.NOME AS NOMEUSUARIO, E.ARQUIVO, E.LINHA, E.CODIGO, E.TEXTO, E.SITUACAO 
#                     FROM TBLOGERRO E LEFT JOIN TBUSUARIO U ON ( U.ID = E.IDUSUARIO ) 
#                     WHERE 1 = 1
#                 """
#         if situacao: query += """ AND E.SITUACAO = :SITUACAO  """
#         query += """ ORDER BY E.DATAHORA, E.ID  """

#         params = {}
#         if situacao: params['SITUACAO'] = situacao

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int = None):
#         query = """ SELECT E.ID, E.DATAHORA, E.IDUSUARIO, U.NOME AS NOMEUSUARIO, E.ARQUIVO, E.LINHA, E.CODIGO, E.TEXTO, E.SITUACAO FROM TBLOGERRO E LEFT JOIN TBUSUARIO U ON ( U.ID = E.IDUSUARIO ) WHERE E.ID = :ID """
#         params = {'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def marcar_tudo(cls, commit: bool = True):
#         try:
#             query = "UPDATE TBLOGERRO SET SITUACAO = 'L' " # L - LIDO
#             params = {}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, commit: bool = True):
#         try:
#             query = "DELETE FROM TBLOGERRO "
#             params = {}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def salvar(self, commit: bool = True):
#         try:
#             db.session.add(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def excluir(self, commit: bool = True):
#         try:
#             db.session.delete(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @staticmethod
#     def descricao_erro(texto: str = None) -> str:
#         try:
#             if str(current_user.tipo) == 'A': return str(texto)
#             return "Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!"
#         except:
#             return "Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!"

#     @staticmethod
#     def registrar(id_usuario: int = None, arqv: str = None, linha: int = None, texto: str = None) -> bool:
#         try:

#             try:
#                 db.session.rollback()
#             except:
#                 pass

#             if texto.strip() == '': return False

#             try:
#                 if not id_usuario: id_usuario = current_user.id
#                 if id_usuario is not None and str(id_usuario).strip() == '': id_usuario = None
#             except:
#                 id_usuario = None

#             try:
#                 if arqv is not None and arqv.strip() == '': arqv = None
#             except:
#                 arqv = None

#             try:
#                 if linha is not None and str(linha).strip() == '': linha = None
#             except:
#                 linha = None

#             try:
#                 (dt, micro) = pegar_data_hora_atual(fmt='%Y%m%d%H%M%S.%f').split('.')
#                 data_hora = "%s%03d" % (dt, int(micro) / 1000)
#             except Exception as e:
#                 data_hora = pegar_data_hora_atual()

#             log_erro = LogErro()
#             log_erro.data_hora = data_hora
#             log_erro.id_usuario = id_usuario
#             log_erro.arquivo = arqv
#             log_erro.linha = linha
#             log_erro.texto = texto
#             log_erro.situacao = 'N'

#             db.session.add(log_erro)
#             db.session.commit()

#             return True

#         except Exception as e:
#             pass

#     def data_hora_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

#     def situacao_descr(self) -> str:
#         if self.situacao == 'L':
#             return 'Lido'
#         elif self.situacao == 'N':
#             return 'Não Lido'
#         else:
#             return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<LogErro - IdUser: {str(self.id_usuario)}>'
