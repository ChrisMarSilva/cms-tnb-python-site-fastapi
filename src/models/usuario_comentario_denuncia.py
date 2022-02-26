# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class UsuarioComentarioDenuncia(db.Model):

#     __tablename__ = "TBCOMENTARIO_DENUNCIA"

#     id_comentario = db.Column('IDCOMENTARIO', db.Integer, db.ForeignKey('TBCOMENTARIO.ID'), primary_key=True, nullable=False, index=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)
#     tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id_comentario: int = None, id_usuario: int = None, tipo: str = None, situacao: str = None):
#         self.id_comentario = id_comentario
#         self.id_usuario = id_usuario
#         self.tipo = tipo
#         self.situacao = situacao

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBCOMENTARIO_DENUNCIA WHERE IDUSUARIO = :IDUSUARIO"
#             params = {'IDUSUARIO': id_usuario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_respostas(cls, id_comentario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBCOMENTARIO_DENUNCIA WHERE IDCOMENTARIO IN ( SELECT C.ID FROM TBCOMENTARIO C WHERE C.IDPAI = :IDPAI AND C.TIPO = 'B' )"
#             params = {'IDPAI': id_comentario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_comentario(cls, id_comentario: int, commit: bool = True):
#         try:
#             query = """DELETE FROM TBCOMENTARIO_DENUNCIA WHERE IDCOMENTARIO = :IDCOMENTARIO """
#             params = {'IDCOMENTARIO': id_comentario}
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

#     def tipo_descr(self) -> str:
#         if self.tipo == 'A':
#             return 'Conteúdo Impróprio com Apelo Sexual'
#         elif self.tipo == 'B':
#             return 'Conteúdo Violento, Repulsivo, Ofensivo ou Proibido'
#         elif self.tipo == 'C':
#             return 'Conteúdo Enganaso ou é uma Fraude'
#         elif self.tipo == 'D':
#             return 'Não Concordo com isso'
#         elif self.tipo == 'E':
#             return 'Conteúdo de Incitação de Ódio ou Abusivo'
#         elif self.tipo == 'F':
#             return 'Spam'
#         elif self.tipo == 'Z':
#             return 'Outra coisa'
#         else:
#             return 'Desconhecido'

#     def situacao_descr(self) -> str:
#         if self.situacao == 'A':
#             return 'Em Avaliação pelo ADM'
#         elif self.situacao == 'B':
#             return 'Avaliado Pelo ADM'
#         elif self.situacao == 'C':
#             return 'Ignorado pelo ADM'
#         elif self.situacao == 'D':
#             return 'Cancelado pelo Usuário'
#         else:
#             return 'Desconhecida'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioComentarioDenuncia - {str(self.id_comentario)} - {str(self.id_usuario)}>'
