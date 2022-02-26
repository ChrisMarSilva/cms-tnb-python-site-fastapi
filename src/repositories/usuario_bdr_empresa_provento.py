# # -*- coding: utf-8 -*-
# import sys
# import os
# import asyncio
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str, inteiro_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class UsuarioBDREmpresaProvento(db.Model):

#     __tablename__ = "TBBDR_PROVENTO"
#     # __table_args__ = {'extend_existing': True}

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
#     id_bdr = db.Column('IDBDR', db.Integer, db.ForeignKey('TBBDR_EMPRESA.ID'), nullable=False, index=True)
#     id_corretora = db.Column('IDCORRETORA', db.Integer, db.ForeignKey('TBCORRETORA.ID'), nullable=True)
#     tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
#     data_ex = db.Column('DATAEX', db.String(8), nullable=False)
#     data_pagto = db.Column('DATAPAGTO', db.String(8), nullable=False, index=True)
#     calc_vlr_liquido = db.Column('CALCVLRLIQUIDO', db.String(1), nullable=True)
#     quantidade = db.Column('QUANTIDADE', db.Float(20, 10), nullable=False)
#     vlr_preco = db.Column('VLRPRECO', db.Float(20, 10), nullable=False)
#     tot_vlr = db.Column('TOTVLR', db.Float(17, 2), nullable=False)
#     vlr_preco_bruto = db.Column('VLRPRECOBRUTO', db.Float(20, 10), nullable=True)
#     tot_vlr_bruto = db.Column('TOTVLRBRUTO', db.Float(17, 2), nullable=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_usuario: int = None, id_bdr: int = None, id_corretora: int = None,
#                  tipo: str = None, data_ex: str = None, data_pagto: str = None,
#                  calc_vlr_liquido: str = None, quantidade: float = 0.0, vlr_preco: float = 0.0,
#                  tot_vlr: float = 0.0, vlr_preco_bruto: float = 0.0, tot_vlr_bruto: float = 0.0,
#                  situacao: str = None):
#         self.id = id
#         self.id_usuario = id_usuario
#         self.id_bdr = id_bdr
#         self.id_corretora = id_corretora
#         self.tipo = tipo
#         self.data_ex = data_ex
#         self.data_pagto = data_pagto
#         self.calc_vlr_liquido = calc_vlr_liquido
#         self.quantidade = quantidade
#         self.vlr_preco = vlr_preco
#         self.tot_vlr = tot_vlr
#         self.vlr_preco_bruto = vlr_preco_bruto
#         self.tot_vlr_bruto = tot_vlr_bruto
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
#             return cls.query.filter_by(id_usuario=id_usuario).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_all_by_ativo(cls, id_bdr: int):
#         try:
#             return cls.query.filter_by(id_bdr=id_bdr).all()
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
#     def get_menor_ano(cls, id_usuario: int = None, id_bdr: int = None):
#         try:
#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_bdr: filters.append(cls.id_bdr == id_bdr)
#             return db.session.query(db.func.min(cls.data_pagto)).filter(*filters).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_menor_ano_ex(cls, id_usuario: int = None, id_bdr: int = None):
#         try:
#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_bdr: filters.append(cls.id_bdr == id_bdr)
#             return db.session.query(db.func.min(cls.data_ex)).filter(*filters).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_maior_ano(cls, id_usuario: int = None, id_bdr: int = None):
#         try:
#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_bdr: filters.append(cls.id_bdr == id_bdr)
#             return db.session.query(db.func.max(cls.data_pagto)).filter(*filters).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_maior_ano_ex(cls, id_usuario: int = None, id_bdr: int = None):
#         try:
#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_bdr: filters.append(cls.id_bdr == id_bdr)
#             return db.session.query(db.func.max(cls.data_ex)).filter(*filters).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls, id_usuario: int = None, codigo: str = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None, id_corretora: str = None, situacao: str = None):

#         query = """ SELECT P.ID, 
#                            P.IDUSUARIO, 
#                            P.IDBDR      AS IDBDR, 
#                            E.CODIGO       AS CODIGOBDR, 
#                            E.SITUACAO     AS SITUACAOBDR,
#                            P.IDCORRETORA  AS IDCORRETORA, 
#                            C.NOME         AS NOMECORRETORA, 
#                            P.TIPO,  
#                            P.DATAEX,  
#                            P.DATAPAGTO, 
#                            P.QUANTIDADE, 
#                            P.CALCVLRLIQUIDO, 
#                            P.VLRPRECOBRUTO, 
#                            P.VLRPRECO, 
#                            P.TOTVLRBRUTO, 
#                            P.TOTVLR, 
#                            P.SITUACAO 
#                     FROM TBBDR_PROVENTO P
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = P.IDBDR     )
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = P.IDCORRETORA )
#                     WHERE P.IDUSUARIO = :IDUSUARIO
#                 """

#         if codigo: query += " AND E.CODIGO = :CODIGO "
#         if tipo: query += " AND P.TIPO =  :TIPO "
#         if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO "
#         if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
#         if id_corretora: query += " AND P.IDCORRETORA = :IDCORRETORA "
#         if situacao: query += " AND P.SITUACAO = :SITUACAO "
#         query += " ORDER BY P.DATAPAGTO, P.TIPO "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         if tipo: params['TIPO'] = tipo
#         if dt_ini: params['DATAINICIO'] = dt_ini
#         if dt_fim: params['DATAFIM'] = dt_fim
#         if id_corretora: params['IDCORRETORA'] = id_corretora
#         if situacao: params['SITUACAO'] = situacao
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id_usuario: int = None, id: int = None):
#         query = """ SELECT P.ID, 
#                            P.IDUSUARIO, 
#                            P.IDBDR      AS IDBDR, 
#                            E.CODIGO       AS CODIGOBDR, 
#                            E.SITUACAO     AS SITUACAOBDR,
#                            P.IDCORRETORA  AS IDCORRETORA, 
#                            C.NOME         AS NOMECORRETORA, 
#                            P.TIPO,  
#                            P.DATAEX,  
#                            P.DATAPAGTO, 
#                            P.QUANTIDADE, 
#                            P.CALCVLRLIQUIDO, 
#                            P.VLRPRECOBRUTO, 
#                            P.VLRPRECO, 
#                            P.TOTVLRBRUTO, 
#                            P.TOTVLR, 
#                            P.SITUACAO 
#                     FROM TBBDR_PROVENTO P
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = P.IDBDR     )
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = P.IDCORRETORA )
#                     WHERE P.ID        = :ID
#                       AND P.IDUSUARIO = :IDUSUARIO
#                 """
#         params = {'ID': id, 'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_codigo(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT P.ID, 
#                            P.IDUSUARIO, 
#                            P.IDBDR      AS IDBDR, 
#                            E.CODIGO       AS CODIGOBDR, 
#                            E.SITUACAO     AS SITUACAOBDR,
#                            P.IDCORRETORA  AS IDCORRETORA, 
#                            C.NOME         AS NOMECORRETORA, 
#                            P.TIPO,  
#                            P.DATAEX,  
#                            P.DATAPAGTO, 
#                            P.QUANTIDADE, 
#                            P.CALCVLRLIQUIDO, 
#                            P.VLRPRECOBRUTO, 
#                            P.VLRPRECO, 
#                            P.TOTVLRBRUTO, 
#                            P.TOTVLR, 
#                            P.SITUACAO 
#                     FROM TBBDR_PROVENTO P
#                       INNER JOIN TBBDR_EMPRESA A ON ( E.ID = P.IDBDR     )
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = P.IDCORRETORA )
#                     WHERE E.CODIGO    = :CODIGO
#                       AND P.IDUSUARIO = :IDUSUARIO
#                 """
#         params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_dados_grid_irpf(cls, id_usuario: int = None, tipo: str = None, dt_pagto_ini: str = None, dt_pagto_fim: str = None, dt_ex_ini: str = None, dt_ex_fim: str = None):
#         query = """ SELECT MAX(E.CODIGO) AS CODIGO, MAX(E.CNPJ) AS CNPJ, MAX(E.RAZAOSOCIAL) AS RAZAOSOCIAL, SUM(P.TOTVLR) AS TOTVLR
#                     FROM TBBDR_PROVENTO P 
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = P.IDBDR ) 
#                     WHERE P.IDUSUARIO = :IDUSUARIO AND P.TIPO = :TIPO AND P.DATAPAGTO >= :DATAINICIO AND P.DATAPAGTO <= :DATAFIM
#                 """
#         if dt_ex_ini: query += " AND P.DATAEX >= :DATAEXINI "
#         if dt_ex_fim: query += " AND P.DATAEX <= :DATAEXFIM "
#         query += " GROUP BY P.IDBDR "
#         query += " ORDER BY E.RAZAOSOCIAL "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['TIPO'] = tipo
#         params['DATAINICIO'] = dt_pagto_ini
#         params['DATAFIM'] = dt_pagto_fim
#         if dt_ex_ini: params['DATAEXINI'] = dt_ex_ini
#         if dt_ex_fim: params['DATAEXFIM'] = dt_ex_fim
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_vlr_total(cls, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
#         query = """ SELECT IFNULL(SUM(P.TOTVLR), 0.00 ) AS TOTAL FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO AND P.IDBDR = :IDBDR AND P.SITUACAO = 'A' """
#         if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDBDR'] = id_bdr
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_vlr_total_periodo(cls, id_usuario: int = None, id_bdr: int = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT IFNULL(SUM(P.TOTVLR), 0.00 ) AS TOTAL FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
#         if id_bdr: query += " AND P.IDBDR = :IDBDR "
#         if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO "
#         if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDBDR'] = id_bdr
#         if dt_ini: params['DATAINICIO'] = dt_ini
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_vlr_total_periodo_ex(cls, id_usuario: int = None, id_bdr: int = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT IFNULL(SUM(P.TOTVLR), 0.00 ) AS TOTAL FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO AND P.IDBDR = :IDBDR AND P.DATAEX >= :DATAINICIO AND P.DATAEX <= :DATAFIM """
#         params = {'IDUSUARIO': id_usuario, 'IDBDR': id_bdr, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_vlr_preco(cls, id_usuario: int = None, id_bdr: int = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT IFNULL(SUM(P.VLRPRECO), 0.00 ) AS VALOR FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO AND P.IDBDR = :IDBDR AND P.DATAPAGTO >= :DATAINICIO AND P.DATAPAGTO <= :DATAFIM """
#         params = {'IDUSUARIO': id_usuario, 'IDBDR': id_bdr, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_vlr_preco_ex(cls, id_usuario: int = None, id_bdr: int = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT IFNULL(SUM(P.VLRPRECO), 0.00 ) AS VALOR FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO AND P.IDBDR = :IDBDR AND P.DATAEX >= :DATAINICIO AND P.DATAEX <= :DATAFIM """
#         params = {'IDUSUARIO': id_usuario, 'IDBDR': id_bdr, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     @asyncio.coroutine
#     async def buscar_qtde_total_base(cls, id_usuario: int = None, tipo: str = None):
#         query = """ SELECT COUNT(1) AS QTDE FROM TBBDR_PROVENTO P WHERE 1 = 1 """
#         if tipo: query += " AND P.TIPO = :TIPO "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if tipo: params['TIPO'] = tipo
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] and rows[0] > 0 else 0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_qtd_operacao_usuario(cls, id_usuario: int = None):
#         query = """ SELECT COUNT(1) AS QTDE FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO"""
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] and rows[0] > 0 else 0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_menor_ano(cls, id_usuario: int = None, id_bdr: int = None):
#         query = """ SELECT SUBSTRING(MIN(P.DATAPAGTO), 1, 4) AS MENORANO FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
#         if id_bdr: query += " AND P.IDBDR = :IDBDR "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_bdr: params['IDBDR'] = id_bdr
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] else ''
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_menor_ano_ex(cls, id_usuario: int = None, id_bdr: int = None):
#         query = """ SELECT SUBSTRING(MIN(P.DATAEX), 1, 4) AS MENORANO FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
#         if id_bdr: query += " AND P.IDBDR = :IDBDR "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_bdr: params['IDBDR'] = id_bdr
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] else ''
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_maior_ano(cls, id_usuario: int = None, id_bdr: int = None):
#         query = """ SELECT SUBSTRING(MAX(P.DATAPAGTO), 1, 4) AS MAIORANO FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
#         if id_bdr: query += " AND P.IDBDR = :IDBDR "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_bdr: params['IDBDR'] = id_bdr
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] else ''
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_maior_ano_ex(cls, id_usuario: int = None, id_bdr: int = None):
#         query = """ SELECT SUBSTRING(MAX(P.DATAEX), 1, 4) AS MAIORANO FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
#         if id_bdr: query += " AND P.IDBDR = :IDBDR "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_bdr: params['IDBDR'] = id_bdr
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] else ''
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_maior_data(cls, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
#         query = """ SELECT MAX(P.DATAPAGTO) AS MAIORDATA FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
#         if id_bdr: query += " AND P.IDBDR = :IDBDR "
#         if dt_fim: query += " AND P.DATAEX <= :DATAFIM  "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_bdr: params['IDBDR'] = id_bdr
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] else ''
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_maior_data_ex(cls, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
#         query = """ SELECT MAX(P.DATAEX) AS MAIORDATA FROM TBBDR_PROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
#         if id_bdr: query += " AND P.IDBDR = :IDBDR "
#         if dt_fim: query += " AND P.DATAEX <= :DATAFIM  "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_bdr: params['IDBDR'] = id_bdr
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] else ''
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBBDR_PROVENTO WHERE IDUSUARIO = :IDUSUARIO"
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
#             db.session.delete(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def calc_total_bruto(self) -> float:
#         return self.calcular_total_bruto(quantidade=self.quantidade, vlr_preco_bruto=self.vlr_preco_bruto)

#     def calc_total(self) -> float:
#         return self.calcular_total(quantidade=self.quantidade, vlr_preco=self.vlr_preco)

#     def data_ex_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_pagto_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_ex_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def data_pagto_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def quantidade_format(self) -> str:
#         return inteiro_to_str(valor=self.quantidade)

#     def vlr_preco_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco)

#     def tot_vlr_format(self) -> str:
#         return decimal_to_str(valor=self.tot_vlr)

#     def vlr_preco_bruto_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_bruto)

#     def tot_vlr_bruto_format(self) -> str:
#         return decimal_to_str(valor=self.tot_vlr_bruto)

#     def calc_vlr_liquido_descr(self) -> str:
#         return self.descricao_calc_vlr_liquido(calc_vlr_liquido=self.calc_vlr_liquido)

#     def tipo_descr(self) -> str:
#         return self.descricao_tipo(tipo=self.tipo)

#     def situacao_descr(self) -> str:
#         return self.descricao_situacao(situacao=self.situacao)

#     @classmethod
#     def calcular_total_bruto(cls, quantidade: float, vlr_preco_bruto: float) -> float:
#         return float(quantidade) * float(vlr_preco_bruto) if quantidade > 0.0 and vlr_preco_bruto > 0.0 else 0.0

#     @classmethod
#     def calcular_total(cls, quantidade: float, vlr_preco: float) -> float:
#         return float(quantidade) * float(vlr_preco) if quantidade > 0.0 and vlr_preco > 0.0 else 0.0

#     @classmethod
#     def descricao_calc_vlr_liquido(cls, calc_vlr_liquido: str) -> str:
#         if calc_vlr_liquido == 'S': return 'Sim'
#         elif calc_vlr_liquido == 'N': return 'Não'
#         else: return 'Desconhecida'

#     @classmethod
#     def descricao_tipo(cls, tipo: str) -> str:
#         if tipo == 'D': return 'DIVIDENDOS'
#         elif tipo == 'J': return 'JRS CAP PRÓPRIO'
#         elif tipo == 'R': return 'REST CAP DIN'
#         else: return 'Desconhecido'

#     @classmethod
#     def descricao_situacao(cls, situacao: str) -> str:
#         if situacao == 'A': return 'Ativo'
#         elif situacao == 'B': return 'Pendente Aprovação/Confirmação'
#         elif situacao == 'I': return 'Inativo'
#         else: return 'Desconhecida'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioEmpresaProvento {str(self.id)}>'
