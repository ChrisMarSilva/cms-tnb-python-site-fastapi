# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class FiiFundoImobTipo(db.Model):

#     __tablename__ = "TBFII_FUNDOIMOB_TIPO"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     descricao = db.Column('DESCRICAO', db.String(250), nullable=False)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, descricao: str = None, situacao: str = None):
#         self.id = id
#         self.descricao = descricao
#         self.situacao = situacao

#     @classmethod
#     def find_by_id(cls, id: int):
#         try:
#             return cls.query.filter_by(id=id).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_lista_nomes(cls):
#         try:
#             return cls.query.order_by(cls.descricao).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_nome_tipo(cls):
#         query = """ SELECT ID, DESCRICAO FROM TBFII_FUNDOIMOB_TIPO ORDER BY DESCRICAO """
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
#         return '<FiiFundoImobTipo {str(self.id)} - {self.cpf}>'
