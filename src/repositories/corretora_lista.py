# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class CorretoraLista(db.Model):

#     __tablename__ = "TBCORRETORA_LISTA"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     nome = db.Column('NOME', db.String(100), nullable=False, index=True)
#     cnpj = db.Column('CNPJ', db.String(14), nullable=False, index=True)
#     importar_nota = db.Column('IMPORTAR_NOTA', db.String(1), nullable=False)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, nome: str = None, cnpj: str = None, importar_nota: str = None, situacao: str = None):
#         self.id = id
#         self.nome = nome
#         self.cnpj = cnpj
#         self.importar_nota = importar_nota
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.all()
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
#     def get_by_nome(cls, nome: str):
#         try:
#             return cls.query.filter_by(nome=nome).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_cnpj(cls, cnpj: str):
#         try:
#             return cls.query.filter_by(cnpj=cnpj).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_nomes(cls):
#         try:
#             try:
#                 return cls.query.filter_by(situacao='A').order_by(cls.nome).all()
#             except Exception as e:
#                 return cls.query.filter_by(situacao='A').order_by(cls.nome).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls):
#         query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L ORDER BY L.NOME """
#         params = {}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int = None):
#         query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.ID = :ID """
#         params = {'ID': id}
#         try:
#             try:
#                 return db.session.execute(query, params).first()
#             except Exception as e:
#                 return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_nome(cls, nome: str = None):
#         query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.NOME = :NOME """
#         params = {'NOME': nome}
#         try:
#             try:
#                 return db.session.execute(query, params).first()
#             except Exception as e:
#                 return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_cnpj(cls, cnpj: str = None):
#         query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.CNPJ = :CNPJ """
#         params = {'CNPJ': cnpj}
#         try:
#             try:
#                 return db.session.execute(query, params).first()
#             except Exception as e:
#                 return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_nome(cls):
#         try:
#             query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.SITUACAO = 'A' ORDER BY L.NOME """
#             params = {}
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_nome_cadastradas(cls, id_usuario: int):
#         try:
#             query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBCORRETORA C WHERE C.IDCORRETORALISTA = L.ID AND C.IDUSUARIO = :IDUSUARIO ) ORDER BY L.NOME """
#             params = {'IDUSUARIO': id_usuario}
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_nome_nao_cadastradas(cls, id_usuario: int):
#         try:
#             query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.SITUACAO = 'A' AND NOT EXISTS( SELECT 1 FROM TBCORRETORA C WHERE C.IDCORRETORALISTA = L.ID AND C.IDUSUARIO = :IDUSUARIO ) ORDER BY L.NOME """
#             params = {'IDUSUARIO': id_usuario}
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id: int, commit: bool = True):
#         try:

#             query = "UPDATE TBCORRETORA SET IDCORRETORALISTA = NULL WHERE IDCORRETORALISTA = :IDCORRETORALISTA"
#             params = {'IDCORRETORALISTA': id}
#             db.session.execute(query, params)

#             query = "DELETE FROM TBCORRETORA_LISTA WHERE ID = :ID"
#             params = {'ID': id}
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
#             params = {'IDCORRETORALISTA': self.id}
#             db.session.execute('UPDATE TBCORRETORA SET IDCORRETORALISTA = NULL WHERE IDCORRETORALISTA = :IDCORRETORALISTA', params)
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
#         return '<Corretora {str(self.id)} - {self.nome} - {self.cnpj}>'
