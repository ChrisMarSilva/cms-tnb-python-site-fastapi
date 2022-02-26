# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class UsuarioRadarGrupo(db.Model):

#     __tablename__ = "TBUSUARIO_ACOMP_GRUPO"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
#     descricao = db.Column('DESCRICAO', db.String(255), nullable=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_usuario: int = None, descricao: str = None, situacao: str = None):
#         self.id = id
#         self.id_usuario = id_usuario
#         self.descricao = descricao
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.order_by(cls.id).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_all_by_usuario(cls, id_usuario: int):
#         try:
#             return cls.query.filter_by(id_usuario=id_usuario).order_by(cls.id_usuario, cls.descricao).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_id(cls, id: int):
#         try:
#             return cls.query.filter_by(id=id).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_id_and_id_usuario(cls, id: int, id_usuario: int):
#         try:
#             return cls.query.filter_by(id=id, id_usuario=id_usuario).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_descricao(cls, id_usuario: int, descricao: str):
#         try:
#             return cls.query.filter_by(id_usuario=id_usuario, descricao=descricao).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_descricoes_by_usuario(cls, id_usuario: int):
#         try:
#             return cls.query.filter_by(id_usuario=id_usuario, situacao='A', ).order_by(cls.descricao).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls, id_usuario: int):
#         query = """ SELECT G.ID, G.DESCRICAO, G.SITUACAO FROM TBUSUARIO_ACOMP_GRUPO G WHERE G.IDUSUARIO = :IDUSUARIO ORDER BY G.DESCRICAO """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id_usuario: int, id: int):
#         query = """ SELECT G.ID, G.DESCRICAO, G.SITUACAO FROM TBUSUARIO_ACOMP_GRUPO G WHERE G.ID = :ID AND G.IDUSUARIO = :IDUSUARIO """
#         params = {'IDUSUARIO': id_usuario, 'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_nome(cls, id_usuario: int, nome: str):
#         query = """ SELECT G.ID, G.DESCRICAO, G.SITUACAO FROM TBUSUARIO_ACOMP_GRUPO G WHERE G.DESCRICAO = :DESCRICAO AND G.IDUSUARIO = :IDUSUARIO """
#         params = {'IDUSUARIO': id_usuario, 'DESCRICAO': nome}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_nome(cls, id_usuario: int):
#         query = """ SELECT G.ID, G.DESCRICAO FROM TBUSUARIO_ACOMP_GRUPO G WHERE G.SITUACAO = 'A' AND G.IDUSUARIO = :IDUSUARIO ORDER BY G.DESCRICAO """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO"
#             params = {'IDUSUARIO': id_usuario}
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
#             params = {'IDGRUPO': self.id}
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_CRIPTO WHERE IDGRUPO = :IDGRUPO", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_INDICE WHERE IDGRUPO = :IDGRUPO", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_FUNDO  WHERE IDGRUPO = :IDGRUPO", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_ATIVO  WHERE IDGRUPO = :IDGRUPO", params)
#             db.session.delete(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
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
#         return '<UsuarioRadarGrupo {str(self.id)}>'
