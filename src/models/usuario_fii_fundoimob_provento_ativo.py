# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class UsuarioFiiFundoImobProventoAtivo(db.Model):

#     __tablename__ = "TBFII_FUNDOIMOB_PROVENTO_ATIVO"

#     id_provento = db.Column('IDEMPRPROV', db.Integer, db.ForeignKey('TBFII_FUNDOIMOB_PROVENTO.ID'), primary_key=True, nullable=False, index=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)
#     id_fundo = db.Column('IDFUNDO', db.Integer, db.ForeignKey('TBFII_FUNDOIMOB.ID'), nullable=False, index=True)
#     tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
#     data_ex = db.Column('DATAEX', db.String(1), nullable=False, index=True)

#     def __init__(self, id_provento: int = None, id_usuario: int = None, id_fundo: int = None, tipo: str = None,
#                  data_ex: str = None):
#         self.id_provento = id_provento
#         self.id_usuario = id_usuario
#         self.id_fundo = id_fundo
#         self.tipo = tipo
#         self.data_ex = data_ex

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_provento_and_usuario(cls, id_usuario: int, id_provento: int):
#         try:
#             return cls.query.filter_by(id_usuario=id_usuario, id_provento=id_provento).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBFII_FUNDOIMOB_PROVENTO_ATIVO WHERE IDUSUARIO = :IDUSUARIO"
#             params = {'IDUSUARIO': id_usuario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def salvar(self, commit: bool = True):
#         try:
#             if self.get_by_provento_and_usuario(id_provento=self.id_provento, id_usuario=self.id_usuario): return False
#             db.session.add(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             #raise

#     def excluir(self, commit: bool = True):
#         try:
#             db.session.delete(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioFiiFundoImobProventoAtivo - {str(self.id_fato)} -  {str(self.id_usuario)}>'
