# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class FiiFundoImob(db.Model):

#     __tablename__ = "TBFII_FUNDOIMOB"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True, index=True)
#     id_tipo = db.Column('IDFIITIPO', db.Integer, nullable=True, index=True)
#     id_admin = db.Column('IDFIIADMIN', db.Integer, nullable=True, index=True)
#     nome = db.Column('NOME', db.String(100), nullable=False, index=True)
#     razao_social = db.Column('RAZAOSOCIAL', db.String(255), nullable=False, index=True)
#     cnpj = db.Column('CNPJ', db.String(18), nullable=False)
#     codigo = db.Column('CODIGO', db.String(10), nullable=False, index=True)
#     codigo_isin = db.Column('CODISIN', db.String(50), nullable=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_tipo: int = None, id_admin: int = None, nome: str = None,
#                  razao_social: str = None, cnpj: str = None, codigo: str = None, codigo_isin: str = None,
#                  situacao: str = None):
#         self.id = id
#         self.id_tipo = id_tipo
#         self.id_admin = id_admin
#         self.nome = nome
#         self.razao_social = razao_social
#         self.cnpj = cnpj
#         self.codigo = codigo
#         self.codigo_isin = codigo_isin
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.order_by(cls.nome).all()
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
#         query = """ SELECT FI.ID, 
#                            FI.NOME, 
#                            FI.RAZAOSOCIAL, 
#                            FI.CNPJ, 
#                            FI.CODIGO, 
#                            FI.CODISIN, 
#                            FI.SITUACAO, 
#                            FITP.ID        AS IDFIITIPO, 
#                            FITP.DESCRICAO AS DESCRICAOFIITIPO, 
#                            FITP.SITUACAO  AS SITUACAOFIITIPO, 
#                            FIADM.ID       AS IDFIIADMIN, 
#                            FIADM.NOME     AS NOMEFIIADMIN, 
#                            FIADM.CNPJ     AS CNPJFIIADMIN, 
#                            FIADM.SITUACAO AS SITUACAOFIIADMIN
#                     FROM TBFII_FUNDOIMOB FI
#                       LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
#                       LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
#                     WHERE FI.SITUACAO IN ( 'A' ,'E')
#                     ORDER BY FI.NOME
#                 """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int = None):
#         query = """ SELECT FI.ID, 
#                            FI.NOME, 
#                            FI.RAZAOSOCIAL, 
#                            FI.CNPJ, 
#                            FI.CODIGO, 
#                            FI.CODISIN, 
#                            FI.SITUACAO, 
#                            FITP.ID        AS IDFIITIPO, 
#                            FITP.DESCRICAO AS DESCRICAOFIITIPO, 
#                            FITP.SITUACAO  AS SITUACAOFIITIPO, 
#                            FIADM.ID       AS IDFIIADMIN, 
#                            FIADM.NOME     AS NOMEFIIADMIN, 
#                            FIADM.CNPJ     AS CNPJFIIADMIN, 
#                            FIADM.SITUACAO AS SITUACAOFIIADMIN
#                     FROM TBFII_FUNDOIMOB FI
#                         LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
#                         LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
#                     WHERE FI.ID = :ID 
#                 """
#         params = {'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_codigo(cls, codigo: str = None):
#         query = """ SELECT 	FI.ID, 
#                             FI.NOME, 
#                             FI.RAZAOSOCIAL, 
#                             FI.CNPJ, 
#                             FI.CODIGO, 
#                             FI.CODISIN, 
#                             FI.SITUACAO, 
#                             FITP.ID        AS IDFIITIPO, 
#                             FITP.DESCRICAO AS DESCRICAOFIITIPO, 
#                             FITP.SITUACAO  AS SITUACAOFIITIPO, 
#                             FIADM.ID       AS IDFIIADMIN, 
#                             FIADM.NOME     AS NOMEFIIADMIN, 
#                             FIADM.CNPJ     AS CNPJFIIADMIN, 
#                             FIADM.SITUACAO AS SITUACAOFIIADMIN
#                         FROM TBFII_FUNDOIMOB FI
#                             LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
#                             LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
#                         WHERE FI.CODIGO = :CODIGO 
#                 """
#         params = {'CODIGO': codigo}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_nome(cls, nome: str = None):
#         query = """ SELECT 	FI.ID, 
#                             FI.NOME, 
#                             FI.RAZAOSOCIAL, 
#                             FI.CNPJ, 
#                             FI.CODIGO, 
#                             FI.CODISIN, 
#                             FI.SITUACAO, 
#                             FITP.ID        AS IDFIITIPO, 
#                             FITP.DESCRICAO AS DESCRICAOFIITIPO, 
#                             FITP.SITUACAO  AS SITUACAOFIITIPO, 
#                             FIADM.ID       AS IDFIIADMIN, 
#                             FIADM.NOME     AS NOMEFIIADMIN, 
#                             FIADM.CNPJ     AS CNPJFIIADMIN, 
#                             FIADM.SITUACAO AS SITUACAOFIIADMIN
#                         FROM TBFII_FUNDOIMOB FI
#                             LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
#                             LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
#                         WHERE FI.NOME = :NOME 
#                 """
#         params = {'NOME': nome}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_razao_social(cls, razao_social: str = None):
#         query = """ SELECT 	FI.ID, 
#                             FI.NOME, 
#                             FI.RAZAOSOCIAL, 
#                             FI.CNPJ, 
#                             FI.CODIGO, 
#                             FI.CODISIN, 
#                             FI.SITUACAO, 
#                             FITP.ID        AS IDFIITIPO, 
#                             FITP.DESCRICAO AS DESCRICAOFIITIPO, 
#                             FITP.SITUACAO  AS SITUACAOFIITIPO, 
#                             FIADM.ID       AS IDFIIADMIN, 
#                             FIADM.NOME     AS NOMEFIIADMIN, 
#                             FIADM.CNPJ     AS CNPJFIIADMIN, 
#                             FIADM.SITUACAO AS SITUACAOFIIADMIN
#                         FROM TBFII_FUNDOIMOB FI
#                             LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
#                             LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
#                         WHERE FI.RAZAOSOCIAL = :RAZAOSOCIAL 
#                 """
#         params = {'RAZAOSOCIAL': razao_social}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_cnpj(cls, cnpj: str = None):
#         query = """ SELECT 	FI.ID, 
#                             FI.NOME, 
#                             FI.RAZAOSOCIAL, 
#                             FI.CNPJ, 
#                             FI.CODIGO, 
#                             FI.CODISIN, 
#                             FI.SITUACAO, 
#                             FITP.ID        AS IDFIITIPO, 
#                             FITP.DESCRICAO AS DESCRICAOFIITIPO, 
#                             FITP.SITUACAO  AS SITUACAOFIITIPO, 
#                             FIADM.ID       AS IDFIIADMIN, 
#                             FIADM.NOME     AS NOMEFIIADMIN, 
#                             FIADM.CNPJ     AS CNPJFIIADMIN, 
#                             FIADM.SITUACAO AS SITUACAOFIIADMIN
#                         FROM TBFII_FUNDOIMOB FI
#                             LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
#                             LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
#                         WHERE FI.CNPJ = :CNPJ 
#                 """
#         params = {'CNPJ': cnpj}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_nome(cls):
#         query = """ SSELECT FI.ID, FI.NOME FROM TBFII_FUNDOIMOB FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.NOME """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_codigo(cls):
#         query = """ SELECT FI.ID, FI.CODIGO FROM TBFII_FUNDOIMOB FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.CODIGO """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_proventos(cls, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'FII' AS TIPO		
#                     FROM TBFII_FUNDOIMOB F
#                     WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBFII_PROVENTO P WHERE P.IDFUNDO   = F.ID AND P.IDUSUARIO = :IDUSUARIO
#                 """
#         if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO "
#         if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
#         query += " ) "
#         if codigo: query += " AND F.CODIGO = :CODIGO "
#         query += " ORDER BY F.CODIGO "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         if dt_ini: params['DATAINICIO'] = dt_ini
#         if dt_fim: params['DATAFIM'] = dt_fim

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_pendentes_situacao(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT F.CODIGO, F.ID FROM TBFII_FUNDOIMOB F WHERE EXISTS( SELECT 1 FROM TBFII_LANCAMENTO FL WHERE FL.IDFUNDO = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'P' ) """
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
#         query = """ SELECT F.ID, F.CODIGO, F.CNPJ, F.RAZAOSOCIAL FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBFII_LANCAMENTO FL WHERE FL.IDFUNDO = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.DATA <= :DATAFIM ) ORDER BY F.CODIGO """
#         params = {'IDUSUARIO': id_usuario, 'DATAFIM': dt_fim}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_comprados(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT F.ID, F.CODIGO FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBFII_LANCAMENTO FL WHERE FL.IDFUNDO = F.ID AND FL.IDUSUARIO = :IDUSUARIO ) """
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
#         if situacao == 'A':
#             return 'Ativo'
#         elif situacao == 'I':
#             return 'Inativo'
#         elif situacao == 'E':
#             return 'Encerrado'
#         else:
#             return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<FiiFundoImob {str(self.id)} - {self.nome} - {self.razao_social}>'
