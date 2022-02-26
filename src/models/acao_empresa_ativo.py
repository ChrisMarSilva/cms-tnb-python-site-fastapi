# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class ACAOEmpresaAtivo(db.Model):

#     __tablename__ = "TBEMPRESA_ATIVO"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_empresa = db.Column('IDEMPRESA', db.Integer, db.ForeignKey('TBEMPRESA.ID'), nullable=False, index=True)
#     codigo = db.Column('CODIGO', db.String(10), nullable=False, index=True)
#     tipo = db.Column('TIPO', db.String(100), nullable=True)
#     codigo_isin = db.Column('CODISIN', db.String(50), nullable=True, index=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_empresa: int = None, codigo: str = None, tipo: str = None, codigo_isin: str = None, situacao: str = None):
#         self.id = id
#         self.id_empresa = id_empresa
#         self.codigo = codigo
#         self.tipo = tipo
#         self.codigo_isin = codigo_isin
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_all_by_empresa(cls, id_empresa: int):
#         try:
#             return cls.query.filter_by(id_empresa=id_empresa, situacao='A').order_by(cls.codigo).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_all_codigos(cls):
#         try:
#             return cls.query.filter(cls.situacao == 'A').order_by(cls.codigo).all()
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
#     def buscar_todos(cls):
#         query = """ SELECT A.ID, A.IDEMPRESA, E.NOME, E.RAZAOSOCIAL, E.CNPJ, E.ATIVIDADE, E.SITUACAO AS SITUACAOEMPRESA, A.CODIGO, A.CODISIN, A.TIPO, A.SITUACAO 
#                     FROM TBEMPRESA_ATIVO A
#                       INNER JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA )
#                     WHERE A.SITUACAO = 'A'
#                       AND E.SITUACAO = 'A'
#                     ORDER BY A.CODIGO
#                 """
#         params = {}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int = None):
#         query = """ SELECT A.ID, A.IDEMPRESA, E.NOME, E.RAZAOSOCIAL, E.CNPJ, E.ATIVIDADE, E.SITUACAO AS SITUACAOEMPRESA, A.CODIGO, A.CODISIN, A.TIPO, A.SITUACAO 
#                     FROM TBEMPRESA_ATIVO A
#                       INNER JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA )
#                     WHERE A.ID = :ID 
#                 """
#         params = {'ID': id}
#         try:
#             try:
#                 return db.session.execute(query, params).first()
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_codigo(cls, codigo: str = None):
#         query = """ SELECT A.ID, A.IDEMPRESA, E.NOME, E.RAZAOSOCIAL, E.CNPJ, E.ATIVIDADE, E.SITUACAO AS SITUACAOEMPRESA, A.CODIGO, A.CODISIN, A.TIPO, A.SITUACAO 
#                     FROM TBEMPRESA_ATIVO A
#                       INNER JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA )
#                     WHERE A.CODIGO = :CODIGO 
#                 """
#         params = {'CODIGO': codigo}

#         try:
#             try:
#                 return db.session.execute(query, params).first()
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos(cls):
#         query = """ SELECT A.CODIGO FROM TBEMPRESA_ATIVO A WHERE A.SITUACAO = 'A' ORDER BY A.CODIGO  """
#         params = {}

#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_com_fiis_etfs_bdrs(cls):
#         query = """ SELECT A.CODIGO AS CODIGO, 'ACAO' AS TIPO, A.ID AS ID, IFNULL(E.NOMRESUMIDO, E.NOME) AS NOME FROM TBEMPRESA_ATIVO A JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA ) WHERE A.SITUACAO = 'A'
#                     UNION
#                     SELECT F.CODIGO AS CODIGO, 'FII' AS TIPO, F.ID AS ID, F.NOME AS NOME FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ('A','E')
#                     UNION
#                     SELECT F.CODIGO AS CODIGO, 'ETF' AS TIPO, F.ID AS ID, F.NOME AS NOME FROM TBETF_INDICE F WHERE F.SITUACAO IN ('A','E')
#                     UNION
#                     SELECT F.CODIGO AS CODIGO, 'BDR' AS TIPO, F.ID AS ID, F.NOME AS NOME FROM TBBDR_EMPRESA F WHERE F.SITUACAO IN ('A','E')
#                     ORDER BY CODIGO
#                 """
#         params = {}

#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_com_fiis_etfs_bdrs_criptos(cls):
#         query = """ SELECT A.CODIGO AS CODIGO, 'ACAO' AS TIPO, A.ID AS ID, IFNULL(E.NOMRESUMIDO, E.NOME) AS NOME FROM TBEMPRESA_ATIVO A JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA ) WHERE A.SITUACAO = 'A'
#                     UNION
#                     SELECT F.CODIGO AS CODIGO, 'FII' AS TIPO, F.ID AS ID, F.NOME AS NOME FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ('A','E')
#                     UNION
#                     SELECT F.CODIGO AS CODIGO, 'ETF' AS TIPO, F.ID AS ID, F.NOME AS NOME FROM TBETF_INDICE F WHERE F.SITUACAO IN ('A','E')
#                     UNION
#                     SELECT F.CODIGO AS CODIGO, 'BDR' AS TIPO, F.ID AS ID, F.NOME AS NOME FROM TBBDR_EMPRESA F WHERE F.SITUACAO IN ('A','E')
#                     UNION
#                     SELECT F.CODIGO AS CODIGO, 'CRIPTO' AS TIPO, F.ID AS ID, F.NOME AS NOME FROM TBCRIPTO_EMPRESA F WHERE F.SITUACAO IN ('A','E')
#                     ORDER BY CODIGO
#                 """
#         params = {}

#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_com_nome(cls, codigo: str = None):
#         query = """ SELECT A.CODIGO, E.RAZAOSOCIAL FROM TBEMPRESA_ATIVO A JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA ) WHERE A.SITUACAO = 'A' """
#         if codigo: query += " AND A.CODIGO = :CODIGO "
#         query += " ORDER BY A.CODIGO "

#         params = {}
#         if codigo: params['CODIGO'] = codigo
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_comprados(cls, id_usuario: int, codigo: str = None):
#         query = """ SELECT A.ID, A.CODIGO FROM TBEMPRESA_ATIVO A WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBLANCAMENTO O WHERE O.IDATIVO = A.ID AND O.IDUSUARIO = :IDUSUARIO ) """
#         if codigo: query += " AND A.CODIGO = :CODIGO "
#         query += " ORDER BY A.CODIGO "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo

#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_comprados_com_fiis_bdrs(cls, id_usuario: int):
#         query = """ SELECT A.ID AS ID, A.CODIGO AS CODIGO, 'ACAO' AS TIPO FROM TBEMPRESA_ATIVO A WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBLANCAMENTO O WHERE O.IDATIVO = A.ID AND O.IDUSUARIO = :IDUSUARIO1 )
#                     UNION 
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'FII' AS TIPO FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBFII_LANCAMENTO O WHERE O.IDFUNDO = F.ID AND O.IDUSUARIO = :IDUSUARIO2 )
#                     UNION 
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'BDR' AS TIPO FROM TBBDR_EMPRESA F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO O WHERE O.IDBDR = F.ID AND O.IDUSUARIO = :IDUSUARIO3 )
#                     ORDER BY CODIGO
#                 """
#         params = {'IDUSUARIO1': id_usuario, 'IDUSUARIO2': id_usuario, 'IDUSUARIO3': id_usuario}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_comprados_com_fiis_bdrs_criptos(cls, id_usuario: int):
#         query = """ SELECT A.ID AS ID, A.CODIGO AS CODIGO, 'ACAO' AS TIPO FROM TBEMPRESA_ATIVO A WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBLANCAMENTO O WHERE O.IDATIVO = A.ID AND O.IDUSUARIO = :IDUSUARIO1 )
#                     UNION 
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'FII' AS TIPO FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBFII_LANCAMENTO O WHERE O.IDFUNDO = F.ID AND O.IDUSUARIO = :IDUSUARIO2 )
#                     UNION 
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'BDR' AS TIPO FROM TBBDR_EMPRESA F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO O WHERE O.IDBDR = F.ID AND O.IDUSUARIO = :IDUSUARIO3 )
#                     UNION 
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'CRIPTO' AS TIPO FROM TBCRIPTO_EMPRESA F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBCRIPTO_LANCAMENTO O WHERE O.IDCRIPTO = F.ID AND O.IDUSUARIO = :IDUSUARIO4 )
#                     ORDER BY CODIGO
#                 """
#         params = {'IDUSUARIO1': id_usuario, 'IDUSUARIO2': id_usuario, 'IDUSUARIO3': id_usuario, 'IDUSUARIO4': id_usuario}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_comprados_com_fiis_etfs_bdrs(cls, id_usuario: int):
#         query = """ SELECT A.ID AS ID, A.CODIGO AS CODIGO, 'ACAO' AS TIPO, IFNULL(E.NOMRESUMIDO, E.NOME) AS NOME FROM TBEMPRESA_ATIVO A JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA ) WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBLANCAMENTO O WHERE O.IDATIVO = A.ID AND O.IDUSUARIO = :IDUSUARIO1 )
#                     UNION
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'FII' AS TIPO, F.NOME AS NOME FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBFII_LANCAMENTO O WHERE O.IDFUNDO = F.ID AND O.IDUSUARIO = :IDUSUARIO2 )
#                     UNION
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'ETF' AS TIPO, F.FUNDO AS NOME FROM TBETF_INDICE F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBETF_LANCAMENTO O WHERE O.IDINDICE = F.ID AND O.IDUSUARIO = :IDUSUARIO3 )
#                     UNION 
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'BDR' AS TIPO, F.NOME AS NOME FROM TBBDR_EMPRESA F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO O WHERE O.IDBDR = F.ID AND O.IDUSUARIO = :IDUSUARIO4 )
#                     ORDER BY CODIGO
#                 """
#         params = {'IDUSUARIO1': id_usuario, 'IDUSUARIO2': id_usuario, 'IDUSUARIO3': id_usuario, 'IDUSUARIO4': id_usuario}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_comprados_com_fiis_etfs_bdrs_criptos(cls, id_usuario: int):
#         query = """  SELECT A.ID AS ID, A.CODIGO AS CODIGO, 'ACAO' AS TIPO, IFNULL(E.NOMRESUMIDO, E.NOME) AS NOME FROM TBEMPRESA_ATIVO A JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA ) WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBLANCAMENTO O WHERE O.IDATIVO = A.ID AND O.IDUSUARIO = :IDUSUARIO1 )
#                     UNION
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'FII' AS TIPO, F.NOME AS NOME FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBFII_LANCAMENTO O WHERE O.IDFUNDO = F.ID AND O.IDUSUARIO = :IDUSUARIO2 )
#                     UNION
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'ETF' AS TIPO, F.FUNDO AS NOME FROM TBETF_INDICE F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBETF_LANCAMENTO O WHERE O.IDINDICE = F.ID AND O.IDUSUARIO = :IDUSUARIO3 )
#                     UNION 
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'BDR' AS TIPO, F.NOME AS NOME FROM TBBDR_EMPRESA F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO O WHERE O.IDBDR = F.ID AND O.IDUSUARIO = :IDUSUARIO4 )
#                     UNION 
#                     SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'CRIPTO' AS TIPO, F.NOME AS NOME FROM TBCRIPTO_EMPRESA F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBCRIPTO_LANCAMENTO O WHERE O.IDCRIPTO = F.ID AND O.IDUSUARIO = :IDUSUARIO5 )
#                     ORDER BY CODIGO
#                 """
#         params = {'IDUSUARIO1': id_usuario, 'IDUSUARIO2': id_usuario, 'IDUSUARIO3': id_usuario, 'IDUSUARIO4': id_usuario, 'IDUSUARIO5': id_usuario}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_proventos(cls, id_usuario: int, codigo: str = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT A.ID AS ID, A.CODIGO AS CODIGO FROM TBEMPRESA_ATIVO A WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBPROVENTO P WHERE P.IDATIVO   = A.ID AND P.IDUSUARIO = :IDUSUARIO """
#         if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO "
#         if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
#         query += " ) "
#         if codigo: query += " AND A.CODIGO = :CODIGO "
#         query += " ORDER BY A.CODIGO "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if dt_ini: params['DATAINICIO'] = dt_ini
#         if dt_fim: params['DATAFIM'] = dt_fim
#         if codigo:params['CODIGO'] = codigo

#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_proventos_com_fiis_bdrs(cls, id_usuario: int, codigo: str = None, dt_ini: str = None, dt_fim: str = None):

#         query = """ SELECT A.ID AS ID, A.CODIGO AS CODIGO, 'ACAO' AS TIPO FROM TBEMPRESA_ATIVO A WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBPROVENTO P WHERE P.IDATIVO = A.ID AND P.IDUSUARIO = :IDUSUARIO1 """
#         if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO1 "
#         if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM1 "
#         query += " ) "
#         if codigo: query += " AND A.CODIGO = :CODIGO1 "

#         query += " UNION "

#         query += """ SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'FII' AS TIPO FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBFII_PROVENTO P WHERE P.IDFUNDO = F.ID AND P.IDUSUARIO = :IDUSUARIO2 """
#         if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO2 "
#         if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM2 "
#         query += " ) "
#         if codigo: query += " AND F.CODIGO = :CODIGO2 "

#         query += " UNION "

#         query += """ SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'BDR' AS TIPO FROM TBBDR_EMPRESA F WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBBDR_PROVENTO P WHERE P.IDBDR = F.ID AND P.IDUSUARIO = :IDUSUARIO3 """
#         if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO3 "
#         if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM3 "
#         query += " ) "
#         if codigo: query += " AND F.CODIGO = :CODIGO3 "

#         query += " ORDER BY CODIGO "

#         params = {}
#         params['IDUSUARIO1'] = id_usuario
#         params['IDUSUARIO2'] = id_usuario
#         params['IDUSUARIO3'] = id_usuario
#         if dt_ini:
#             params['DATAINICIO1'] = dt_ini
#             params['DATAINICIO2'] = dt_ini
#             params['DATAINICIO3'] = dt_ini
#         if dt_fim:
#             params['DATAFIM1'] = dt_fim
#             params['DATAFIM2'] = dt_fim
#             params['DATAFIM3'] = dt_fim
#         if codigo:
#             params['CODIGO1'] = codigo
#             params['CODIGO2'] = codigo
#             params['CODIGO3'] = codigo

#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_proventos_com_fiis_bdrs_calendario(cls, id_usuario: int, dt_ini: str = None, dt_fim: str = None):

#         query = """ 
        
#             SELECT P.IDATIVO AS ID, MAX(A.CODIGO) AS CODIGO, SUBSTR(P.DATAPAGTO, 1, 6) AS DATAPAGTO, IFNULL(SUM(P.TOTVLR), 0.00 ) AS TOTVLR, 'ACAO' AS TIPO
#             FROM TBPROVENTO P
#               JOIN TBEMPRESA_ATIVO A ON ( A.ID = P.IDATIVO )
#             WHERE P.IDUSUARIO  = :IDUSUARIO1 
#               AND P.DATAPAGTO >= :DATAINICIO1
#               AND P.DATAPAGTO <= :DATAFIM1
#               AND A.SITUACAO   = 'A'
#             GROUP BY P.IDATIVO, SUBSTR(P.DATAPAGTO, 1, 6)
            
#             UNION ALL
            
#             SELECT P.IDFUNDO AS ID, MAX(A.CODIGO) AS CODIGO, SUBSTR(P.DATAPAGTO, 1, 6) AS DATAPAGTO, IFNULL(SUM(P.TOTVLR), 0.00 ) AS TOTVLR, 'FII' AS TIPO
#             FROM TBFII_PROVENTO P
#               JOIN TBFII_FUNDOIMOB A ON ( A.ID = P.IDFUNDO )
#             WHERE P.IDUSUARIO  = :IDUSUARIO2 
#               AND P.DATAPAGTO >= :DATAINICIO2
#               AND P.DATAPAGTO <= :DATAFIM2
#               AND A.SITUACAO   IN ('A','E')
#             GROUP BY P.IDFUNDO, SUBSTR(P.DATAPAGTO, 1, 6)
            
#             UNION ALL
            
#             SELECT P.IDBDR AS ID, MAX(A.CODIGO) AS CODIGO, SUBSTR(P.DATAPAGTO, 1, 6) AS DATAPAGTO, IFNULL(SUM(P.TOTVLR), 0.00 ) AS TOTVLR, 'BDR' AS TIPO
#             FROM TBBDR_PROVENTO P
#               JOIN TBBDR_EMPRESA A ON ( A.ID = P.IDBDR )
#             WHERE P.IDUSUARIO = :IDUSUARIO3 
#               AND P.DATAPAGTO >= :DATAINICIO3
#               AND P.DATAPAGTO <= :DATAFIM3
#               AND A.SITUACAO   IN ('A','E')
#             GROUP BY P.IDBDR, SUBSTR(P.DATAPAGTO, 1, 6)
            
#             ORDER BY CODIGO
            
#         """

#         params = {}
#         params['IDUSUARIO1'] = id_usuario
#         params['IDUSUARIO2'] = id_usuario
#         params['IDUSUARIO3'] = id_usuario
#         params['DATAINICIO1'] = dt_ini
#         params['DATAINICIO2'] = dt_ini
#         params['DATAINICIO3'] = dt_ini
#         params['DATAFIM1'] = dt_fim
#         params['DATAFIM2'] = dt_fim
#         params['DATAFIM3'] = dt_fim

#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_aluguel(cls, id_usuario: int):
#         query = """ SELECT A.CODIGO FROM TBEMPRESA_ATIVO A WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBALUGUEL_ATIVO AL WHERE AL.IDATIVO = A.ID AND AL.IDUSUARIO = :IDUSUARIO ) ORDER BY A.CODIGO """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_pendentes_situacao(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT A.CODIGO, A.ID FROM TBEMPRESA_ATIVO A WHERE EXISTS( SELECT 1 FROM TBLANCAMENTO O WHERE O.IDATIVO = A.ID AND O.IDUSUARIO = :IDUSUARIO AND O.SITUACAO = 'P' ) """
#         if codigo:query += " AND A.CODIGO = :CODIGO "
#         query += " ORDER BY A.CODIGO "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo:params['CODIGO'] = codigo

#         try:
#             try:
#                 return db.session.execute(query, params).fetchall()
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params).fetchall()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_irpf(cls, id_usuario: int = None, dt_fim: str = None):
#         query = """ SELECT A.ID, A.CODIGO, E.CNPJ, E.RAZAOSOCIAL FROM TBEMPRESA_ATIVO A JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA ) WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBOPERACAO O WHERE O.IDATIVO   = A.ID AND O.IDUSUARIO = :IDUSUARIO AND O.DATA <= :DATAFIM ) ORDER BY A.CODIGO """
#         params = {'IDUSUARIO': id_usuario, 'DATAFIM': dt_fim}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
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
#         if self.situacao == 'A': return 'Ativo'
#         elif self.situacao == 'I': return 'Inativo'
#         else: return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<EmpresaAtivo {str(self.id)} - {self.nome} - {self.cnpj}>'
