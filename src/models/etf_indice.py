# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class ETFIndice(db.Model):

#     __tablename__ = "TBETF_INDICE"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True, index=True)
#     razao_social = db.Column('RAZAOSOCIAL', db.String(255), nullable=False, index=True)
#     fundo = db.Column('FUNDO', db.String(100), nullable=False)
#     indice = db.Column('INDICE', db.String(100), nullable=False, index=True)
#     nome = db.Column('NOME', db.String(100), nullable=False, index=True)
#     cnpj = db.Column('CNPJ', db.String(18), nullable=False)
#     codigo = db.Column('CODIGO', db.String(10), nullable=False, index=True)
#     codigo_isin = db.Column('CODISIN', db.String(50), nullable=True, index=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, razao_social: str = None, fundo: str = None, indice: str = None,
#                  nome: str = None, cnpj: str = None, codigo: str = None, codigo_isin: str = None, situacao: str = None):
#         self.id = id
#         self.razao_social = razao_social
#         self.fundo = fundo
#         self.indice = indice
#         self.nome = nome
#         self.cnpj = cnpj
#         self.codigo = codigo
#         self.codigo_isin = codigo_isin
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.filter(cls.situacao.in_(['A', 'E'])).order_by(cls.nome).all()
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
#     def get_by_codigo(cls, codigo: str):
#         try:
#             return cls.query.filter_by(codigo=codigo).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_razao_social(cls, razao_social: str):
#         try:
#             return cls.query.filter_by(razao_social=razao_social).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_fundo(cls, fundo: str):
#         try:
#             return cls.query.filter_by(fundo=fundo).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_indice(cls, indice: str):
#         try:
#             return cls.query.filter_by(indice=indice).first()
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
#     def get_lista_nomes(cls):
#         try:
#             return cls.query.filter(cls.situacao.in_(['A', 'E'])).order_by(cls.nome).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_lista_codigos(cls):
#         try:
#             return cls.query.filter(cls.situacao.in_(['A', 'E'])).order_by(cls.codigo).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls):
#         query = """SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.SITUACAO IN ( 'A' ,'E' ) ORDER BY FI.NOME """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int = None):
#         query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.ID = :ID """
#         params = {'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_codigo(cls, codigo: str = None):
#         query = """SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.CODIGO = :CODIGO """
#         params = {'CODIGO': codigo}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_razao_social(cls, razao_social: str = None):
#         query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.RAZAOSOCIAL = :RAZAOSOCIAL """
#         params = {'RAZAOSOCIAL': razao_social}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_fundo(cls, fundo: str = None):
#         query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.FUNDO = :FUNDO """
#         params = {'FUNDO': fundo}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_indice(cls, indice: str = None):
#         query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.INDICE = :INDICE """
#         params = {'INDICE': indice}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_nome(cls, nome: str = None):
#         query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.NOME = :NOME """
#         params = {'NOME': nome}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_cnpj(cls, cnpj: str = None):
#         query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.CNPJ = :CNPJ """
#         params = {'CNPJ': cnpj}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_nome(cls):
#         query = """ SELECT FI.ID, FI.NOME FROM TBETF_INDICE FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.NOME """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_codigo(cls):
#         query = """ SELECT FI.ID, FI.CODIGO FROM TBETF_INDICE FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.CODIGO """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_pendentes_situacao(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT F.CODIGO, F.ID FROM TBETF_INDICE F WHERE EXISTS( SELECT 1 FROM TBETF_LANCAMENTO FL WHERE FL.IDINDICE = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'P' ) """
#         if codigo: query += " AND F.CODIGO = :CODIGO "
#         query += " ORDER BY F.CODIGO "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         try:
#             return db.session.execute(query, params).fetchall()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_irpf(cls, id_usuario: int = None, dt_fim: str = None):
#         query = """ SELECT F.ID,F.CODIGO, F.CNPJ, F.RAZAOSOCIAL FROM TBETF_INDICE F WHERE F.SITUACAO IN ( 'A' ,'E' ) AND EXISTS( SELECT 1 FROM TBETF_LANCAMENTO FL WHERE FL.IDINDICE = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.DATA <= :DATAFIM ) ORDER BY F.CODIGO """
#         params = {'IDUSUARIO': id_usuario, 'DATAFIM': dt_fim}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_comprados(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT F.ID, F.CODIGO FROM TBETF_INDICE F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBETF_LANCAMENTO FL WHERE FL.IDINDICE = F.ID AND FL.IDUSUARIO = :IDUSUARIO ) """
#         if codigo: query += " AND F.CODIGO = :CODIGO "
#         query += " ORDER BY F.CODIGO "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
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

#     def situacao_descr(self) -> str:
#         return self.descricao_situacao(situacao=self.situacao)

#     @classmethod
#     def descricao_situacao(cls, situacao: str) -> str:
#         if situacao == 'A': return 'Ativo'
#         elif situacao == 'I': return 'Inativo'
#         elif situacao == 'E': return 'Encerrado'
#         else: return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<ETFIndice {str(self.id)} - {self.nome} - {self.razao_social}>'
