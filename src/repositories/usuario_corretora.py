# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str


# class UsuarioCorretora(db.Model):

#     __tablename__ = "TBCORRETORA"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
#     id_corretora_lista = db.Column('IDCORRETORALISTA', db.Integer, nullable=False)
#     nome = db.Column('NOME', db.String(100), nullable=False)
#     cnpj = db.Column('CNPJ', db.String(14), nullable=False)
#     valor = db.Column('VLRCORRETAGEM', db.Float(17, 2), nullable=False)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_usuario: int = None, id_corretora_lista: int = None, nome: str = None, cnpj: str = None, valor: float = 0.0, situacao: str = None):
#         self.id = id
#         self.id_usuario = id_usuario
#         self.id_corretora_lista = id_corretora_lista
#         self.nome = nome
#         self.cnpj = cnpj
#         self.valor = valor
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_all_by_usuario(cls, id_usuario: int):
#         try:
#             return cls.query.filter_by(id_usuario=id_usuario).order_by(cls.nome).all()
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
#     def get_by_usuario(cls, id: int, id_usuario: int):
#         try:
#             return cls.query.filter_by(id=id, id_usuario=id_usuario).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_cnpj(cls, cnpj: str, id_usuario: int):
#         try:
#             return cls.query.filter_by(cnpj=cnpj, id_usuario=id_usuario).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_nome(cls, nome: str, id_usuario: int):
#         try:
#             return cls.query.filter_by(nome=nome, id_usuario=id_usuario).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_id_corretora_lista(cls, id_corretora_lista: int, id_usuario: int):
#         try:
#             return cls.query.filter_by(id_corretora_lista=id_corretora_lista, id_usuario=id_usuario).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_nomes(cls, id_usuario: int):
#         try:
#             try:
#                 return cls.query.filter_by(situacao='A', id_usuario=id_usuario).order_by(cls.nome).all()
#             except Exception as e:
#                 return cls.query.filter_by(situacao='A', id_usuario=id_usuario).order_by(cls.nome).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls, id_usuario: int):
#         query = """ SELECT C.ID, C.IDUSUARIO, C.NOME, C.CNPJ, C.VLRCORRETAGEM, C.SITUACAO FROM TBCORRETORA C WHERE C.IDUSUARIO = :IDUSUARIO ORDER BY C.NOME """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id_usuario: int, id: int = None):
#         query = """ SELECT C.ID, C.IDUSUARIO, C.NOME, C.CNPJ, C.VLRCORRETAGEM, C.SITUACAO FROM TBCORRETORA C WHERE C.ID = :ID AND C.IDUSUARIO = :IDUSUARIO """
#         params = {'ID': id, 'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_nome(cls, id_usuario: int):
#         query = """ SELECT C.ID, C.IDUSUARIO, C.NOME FROM TBCORRETORA C WHERE C.SITUACAO = 'A' AND C.IDUSUARIO = :IDUSUARIO ORDER BY C.NOME """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBCORRETORA WHERE IDUSUARIO = :IDUSUARIO"
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
#             params = {'IDUSUARIO': self.id_usuario, 'IDCORRETORA': self.id}
#             db.session.execute('UPDATE TBPROVENTO       SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
#             db.session.execute('UPDATE TBOPERACAO       SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
#             db.session.execute('UPDATE TBLANCAMENTO     SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
#             db.session.execute('UPDATE TBFII_PROVENTO   SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
#             db.session.execute('UPDATE TBFII_LANCAMENTO SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
#             db.session.execute('UPDATE TBETF_OPERACAO   SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
#             db.session.execute('UPDATE TBETF_LANCAMENTO SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
#             db.session.delete(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def valor_format(self) -> str:
#         return decimal_to_str(valor=self.valor)

#     def situacao_descr(self) -> str:
#         if self.situacao == 'A':
#             return 'Ativa'
#         elif self.situacao == 'I':
#             return 'Inativa'
#         else:
#             return 'Desconhecida'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<Corretora {str(self.id)} - {self.nome} - {self.cnpj}>'
