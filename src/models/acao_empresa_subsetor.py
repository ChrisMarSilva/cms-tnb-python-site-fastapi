# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class ACAOEmpresaSubSetor(db.Model):

#     __tablename__ = "TBEMPRESA_SUBSETOR"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     descricao = db.Column('DESCRICAO', db.String(255), nullable=False, index=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, descricao: str = None, situacao: str = None):
#         self.id = id
#         self.descricao = descricao
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.filter_by(situacao='A').order_by(cls.descricao).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_id(cls, id: int):
#         try:
#             return cls.query.filter_by(id=id, situacao='A').first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_descricao(cls, descricao: str):
#         try:
#             return cls.query.filter_by(descricao=descricao, situacao='A').first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls):
#         query = """ SELECT S.ID, S.DESCRICAO, S.SITUACAO FROM TBEMPRESA_SUBSETOR S WHERE S.SITUACAO = 'A' ORDER BY S.DESCRICAO """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int):
#         query = """ SELECT S.ID, S.DESCRICAO, S.SITUACAO FROM TBEMPRESA_SUBSETOR S WHERE S.SITUACAO = 'A' AND S.ID = :ID """
#         params = {'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_descricao(cls, descricao: str):
#         query = """ SELECT S.ID, S.DESCRICAO, S.SITUACAO FROM TBEMPRESA_SUBSETOR S WHERE S.SITUACAO = 'A' AND S.DESCRICAO = :DESCRICAO """
#         params = {'DESCRICAO': descricao}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista(cls):
#         query = """ SELECT S.ID, S.DESCRICAO FROM TBEMPRESA_SUBSETOR S WHERE S.SITUACAO = 'A' ORDER BY S.DESCRICAO """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_cotacao(cls):
#         query = """ SELECT S.ID, S.DESCRICAO
#                     FROM TBEMPRESA_SUBSETOR S
#                     WHERE S.SITUACAO = 'A'
#                       AND EXISTS( SELECT 1
#                                   FROM TBEMPRESA E
#                                   WHERE E.IDSETOR = S.ID
#                                     AND EXISTS( SELECT 1
#                                                 FROM TBEMPRESA_ATIVO A
#                                                 WHERE A.IDEMPRESA = E.ID
#                                                    AND EXISTS( SELECT 1 FROM TBEMPRESA_ATIVOCOTACAO C WHERE C.IDATIVO = A.ID )
#                                               )
#                                 )
#                     ORDER BY S.DESCRICAO
#                 """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def situacao_descr(self) -> str:
#         if self.situacao == 'A':
#             return 'Ativo'
#         elif self.situacao == 'I':
#             return 'Inativo'
#         else:
#             return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<EmpresaSubSetor {str(self.id)} - {self.cpf}>'
