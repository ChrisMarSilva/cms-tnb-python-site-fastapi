# # -*- coding: utf-8 -*-
# import sys
# import os
# import asyncio
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str, inteiro_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class UsuarioBDREmpresaLancamento(db.Model):

#     __tablename__ = "TBBDR_LANCAMENTO"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
#     id_bdr = db.Column('IDBDR', db.Integer, db.ForeignKey('TBBDR_EMPRESA.ID'), nullable=False, index=True)
#     id_corretora = db.Column('IDCORRETORA', db.Integer, db.ForeignKey('TBCORRETORA.ID'), nullable=True)
#     tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
#     data = db.Column('DATA', db.String(8), nullable=False, index=True)
#     quant = db.Column('QUANT', db.Float(20, 10), nullable=False)
#     quant_pend = db.Column('QUANTPEND', db.Float(20, 10), nullable=True, index=True)
#     vlr_preco = db.Column('VLRPRECO', db.Float(17, 2), nullable=True)
#     tot_vlr_preco = db.Column('TOTVLRPRECO', db.Float(17, 2), nullable=True)
#     vlr_liquidacao = db.Column('VLRTXLIQUIDACAO', db.Float(17, 2), nullable=True)
#     vlr_emolumentos = db.Column('VLRTXEMOLUMENTOS', db.Float(17, 2), nullable=True)
#     vlr_corretagem = db.Column('VLRTXCORRETAGEM', db.Float(17, 2), nullable=True)
#     vlr_irpf = db.Column('VLRTXIRRF', db.Float(17, 2), nullable=True)
#     vlr_iss = db.Column('VLRTXISS', db.Float(17, 2), nullable=True)
#     vlr_outras = db.Column('VLRTXOUTRAS', db.Float(17, 2), nullable=True)
#     tot_vlr_taxa = db.Column('TOTVLRTX', db.Float(17, 2), nullable=True)
#     tot_vlr = db.Column('TOTVLR', db.Float(17, 2), nullable=True)
#     vlr_custo = db.Column('VLRCUSTO', db.Float(20, 10), nullable=True)
#     troca = db.Column('TROCA', db.String(1), nullable=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_usuario: int = None, id_bdr: int = None, id_corretora: int = None,
#                  tipo: str = None, data: str = None, quant: float = 0.0, quant_pend: float = 0.0,
#                  vlr_preco: float = 0.0, tot_vlr_preco: float = 0.0, vlr_liquidacao: float = 0.0,
#                  vlr_emolumentos: float = 0.0, vlr_corretagem: float = 0.0, vlr_irpf: float = 0.0,
#                  vlr_iss: float = 0.0, vlr_outras: float = 0.0, tot_vlr_taxa: float = 0.0, tot_vlr: float = 0.0,
#                  vlr_custo: float = 0.0, troca: str = 'N', situacao: str = None):
#         self.id = id
#         self.id_usuario = id_usuario
#         self.id_bdr = id_bdr
#         self.id_corretora = id_corretora
#         self.tipo = tipo
#         self.data = data
#         self.quant = quant
#         self.quant_pend = quant_pend
#         self.vlr_preco = vlr_preco
#         self.tot_vlr_preco = tot_vlr_preco
#         self.vlr_liquidacao = vlr_liquidacao
#         self.vlr_emolumentos = vlr_emolumentos
#         self.vlr_corretagem = vlr_corretagem
#         self.vlr_irpf = vlr_irpf
#         self.vlr_iss = vlr_iss
#         self.vlr_outras = vlr_outras
#         self.tot_vlr_taxa = tot_vlr_taxa
#         self.tot_vlr = tot_vlr
#         self.vlr_custo = vlr_custo
#         self.troca = troca
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         return cls.query.all()

#     @classmethod
#     def get_all_by_usuario(cls, id_usuario: int):
#         return cls.query.filter_by(id_usuario=id_usuario).all()

#     @classmethod
#     def get_all_by_ativo(cls, id_bdr: int):
#         return cls.query.filter_by(id_bdr=id_bdr).all()

#     @classmethod
#     def get_by_id(cls, id: int):
#         return cls.query.filter_by(id=id).first()

#     @classmethod
#     def get_by_usuario(cls, id: int, id_usuario: int):
#         return cls.query.filter_by(id=id, id_usuario=id_usuario).first()

#     @classmethod
#     def get_menor_ano(cls, id_usuario: int = None, id_bdr: int = None):
#         filters = []
#         if id_usuario: filters.append(cls.id_usuario == id_usuario)
#         if id_bdr: filters.append(cls.id_bdr == id_bdr)
#         return db.session.query(db.func.min(cls.data)).filter(*filters).first()

#     @classmethod
#     def get_maior_ano(cls, id_usuario: int = None, id_bdr: int = None):
#         filters = []
#         if id_usuario: filters.append(cls.id_usuario == id_usuario)
#         if id_bdr: filters.append(cls.id_bdr == id_bdr)
#         return db.session.query(db.func.max(cls.data)).filter(*filters).first()

#     @classmethod
#     def buscar_todos(cls, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None, ordem: str = None, id_corretora: str = None, troca: str = None):
#         try:

#             query = """ SELECT O.ID, O.IDUSUARIO, O.IDBDR AS IDBDR, E.CODIGO AS CODIGOBDR, E.SITUACAO AS SITUACAOBDR, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
#                                O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
#                                O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, O.TROCA, O.SITUACAO,
#                                ( SELECT MAX(OP.VLRPRECOMEDIO)     FROM TBBDR_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDBDR = O.IDBDR AND OP.IDLANC = O.ID ) AS VLRPRECOMEDIO, 
#                                ( SELECT SUM(OP.TOTVLRVALORIZACAO) FROM TBBDR_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDBDR = O.IDBDR AND OP.IDLANC = O.ID ) AS TOTVLRVALORIZACAO, 
#                                ( SELECT SUM(OP.PERCVALORIZACAO)   FROM TBBDR_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDBDR = O.IDBDR AND OP.IDLANC = O.ID ) AS PERCVALORIZACAO
#                         FROM TBBDR_LANCAMENTO O
#                           INNER JOIN TBBDR_EMPRESA E ON ( E.ID = O.IDBDR )
#                           LEFT  JOIN TBCORRETORA C ON ( C.ID = O.IDCORRETORA )
#                         WHERE O.IDUSUARIO = :IDUSUARIO
#                     """

#             if codigo: query += " AND E.CODIGO = :CODIGO "
#             if dt_ini: query += " AND O.DATA >= :DATAINICIO "
#             if dt_fim: query += " AND O.DATA <= :DATAFIM "
#             if tipo: query += " AND O.TIPO = :TIPO "
#             if id_corretora: query += " AND O.IDCORRETORA = :IDCORRETORA "
#             if troca: query += " AND IFNULL(O.TROCA, 'N') = :TROCA "

#             if ordem: query += " ORDER BY O.DATA DESC, O.TIPO, O.ID "
#             else: query += "  ORDER BY O.DATA, O.TIPO, O.ID "

#             params = {}
#             params['IDUSUARIO'] = id_usuario
#             if codigo: params['CODIGO'] = codigo
#             if dt_ini: params['DATAINICIO'] = dt_ini
#             if dt_fim: params['DATAFIM'] = dt_fim
#             if tipo: params['TIPO'] = tipo
#             if id_corretora: params['IDCORRETORA'] = id_corretora
#             if troca: params['TROCA'] = troca

#             return db.session.execute(query, params)

#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_data(cls, id_usuario: int = None, codigo: str = None, data: str = None, tipo: str = None):
#         query = """ SELECT O.ID, O.IDUSUARIO, O.IDBDR AS IDBDR, E.CODIGO AS CODIGOBDR, E.SITUACAO AS SITUACAOBDR, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
#                            O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
#                            O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, O.TROCA, O.SITUACAO,
#                            ( SELECT MAX(OP.VLRPRECOMEDIO)     FROM TBBDR_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDBDR = O.IDBDR AND OP.IDLANC = O.ID ) AS VLRPRECOMEDIO, 
#                            ( SELECT SUM(OP.TOTVLRVALORIZACAO) FROM TBBDR_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDBDR = O.IDBDR AND OP.IDLANC = O.ID ) AS TOTVLRVALORIZACAO, 
#                            ( SELECT SUM(OP.PERCVALORIZACAO)   FROM TBBDR_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDBDR = O.IDBDR AND OP.IDLANC = O.ID ) AS PERCVALORIZACAO
#                     FROM TBBDR_LANCAMENTO O
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = O.IDBDR )
#                       LEFT  JOIN TBCORRETORA C ON ( C.ID = O.IDCORRETORA )
#                     WHERE O.IDUSUARIO = :IDUSUARIO AND O.QUANTPEND > 0
#                 """

#         if codigo: query += " AND E.CODIGO = :CODIGO "
#         if data: query += " AND O.DATA = :DATA"
#         if tipo: query += " AND O.TIPO = :TIPO "

#         query += " ORDER BY O.ID "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         if data: params['DATA'] = data
#         if tipo: params['TIPO'] = tipo

#         return db.session.execute(query, params).fetchall()

#     @classmethod
#     def buscar_por_id(cls, id_usuario: int = None, id: int = None):
#         query = """ SELECT O.ID, O.IDUSUARIO, O.IDBDR AS IDBDR, E.CODIGO AS CODIGOBDR, E.SITUACAO AS SITUACAOBDR, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
#                            O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
#                            O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, O.TROCA, O.SITUACAO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO
#                     FROM TBBDR_LANCAMENTO O
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = O.IDBDR )
#                       LEFT JOIN TBCORRETORA C ON ( C.ID = O.IDCORRETORA )
#                     WHERE O.ID = :ID AND O.IDUSUARIO = :IDUSUARIO
#                 """
#         params = {'ID': id, 'IDUSUARIO': id_usuario}
#         return db.session.execute(query, params).first()

#     @classmethod
#     def buscar_por_codigo(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT O.ID, O.IDUSUARIO, O.IDBDR AS IDBDR, E.CODIGO AS CODIGOBDR, E.SITUACAO AS SITUACAOBDR, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
#                            O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
#                            O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, O.TROCA, O.SITUACAO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO
#                     FROM TBBDR_LANCAMENTO O
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = O.IDBDR     )
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
#                     WHERE O.IDUSUARIO = :IDUSUARIO AND E.CODIGO = :CODIGO
#                     ORDER BY O.DATA, O.ID, O.TIPO 
#                 """
#         params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
#         return db.session.execute(query, params)

#     @classmethod
#     def buscar_por_day_trade(cls, id_usuario: int = None, codigo: str = None, tipo: str = None):
#         query = ''
#         if tipo == 'C' or tipo == 'B':
#             query = """ SELECT OC.ID, OC.IDUSUARIO, OC.IDBDR AS IDBDR, AC.CODIGO AS CODIGOBDR, AC.SITUACAO AS SITUACAOBDR, OC.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
#                                OC.TIPO, OC.DATA, OC.QUANT, OC.QUANTPEND, OC.VLRPRECO, OC.TOTVLRPRECO, OC.VLRTXLIQUIDACAO, OC.VLRTXEMOLUMENTOS, OC.VLRTXCORRETAGEM, OC.VLRTXISS, OC.VLRTXIRRF, 
#                                OC.VLRTXOUTRAS, OC.TOTVLRTX, OC.TOTVLR, OC.VLRCUSTO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO, OC.TROCA, OC.SITUACAO 
#                         FROM TBBDR_LANCAMENTO OC
#                           INNER JOIN TBBDR_EMPRESA AC ON ( AC.ID = OC.IDBDR ) 
#                           LEFT  JOIN TBCORRETORA C ON ( C.ID = OC.IDCORRETORA )
#                         WHERE OC.IDUSUARIO = :IDUSUARIO AND AC.CODIGO = :CODIGO AND OC.TIPO IN ('C', 'B')
#                           AND EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO OV WHERE OV.IDUSUARIO = OC.IDUSUARIO AND OV.IDBDR = OC.IDBDR AND OV.TIPO = 'V' AND OV.DATA = OC.DATA ) 
#                         ORDER BY OC.DATA, OC.ID
#                     """
#         if tipo == 'V':
#             query = """ SELECT OV.ID, OV.IDUSUARIO, OV.IDBDR AS IDBDR, AV.CODIGO AS CODIGOBDR, AV.SITUACAO AS SITUACAOBDR, OV.IDCORRETORA AS IDCORRETORA, 
#                                C.NOME AS NOMECORRETORA, OV.TIPO, OV.DATA, OV.QUANT, OV.QUANTPEND, OV.VLRPRECO, OV.TOTVLRPRECO, OV.VLRTXLIQUIDACAO, OV.VLRTXEMOLUMENTOS, 
#                                OV.VLRTXCORRETAGEM, OV.VLRTXISS, OV.VLRTXIRRF, OV.VLRTXOUTRAS, OV.TOTVLRTX, OV.TOTVLR, OV.VLRCUSTO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 
#                                0.00 AS PERCVALORIZACAO, OV.TROCA, OV.SITUACAO 
#                         FROM TBBDR_LANCAMENTO OV
#                           INNER JOIN TBBDR_EMPRESA AV ON ( AV.ID = OV.IDBDR ) 
#                           LEFT JOIN TBCORRETORA C  ON ( C.ID = OV.IDCORRETORA )
#                         WHERE OV.IDUSUARIO = :IDUSUARIO
#                           AND AV.CODIGO = :CODIGO
#                           AND OV.TIPO = 'V'
#                           AND EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO OC WHERE OC.IDUSUARIO = OV.IDUSUARIO AND OC.IDBDR = OV.IDBDR AND OC.TIPO IN ('C', 'B') AND OC.DATA = OV.DATA AND OC.ID < OV.ID )  
#                         ORDER BY OV.DATA, OV.ID DESC
#                     """
#         params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
#         return db.session.execute(query, params)

#     @classmethod
#     def buscar_por_qtde_pend_maior_que_zero(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT O.ID, O.IDUSUARIO, O.IDBDR AS IDBDR, E.CODIGO AS CODIGOBDR, E.SITUACAO AS SITUACAOBDR, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
#                            O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
#                            O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO, O.TROCA, O.SITUACAO 
#                     FROM TBBDR_LANCAMENTO O
#                       INNER JOIN TBBDR_EMPRESA   E ON ( E.ID = O.IDBDR     )  
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
#                     WHERE O.IDUSUARIO = :IDUSUARIO AND E.CODIGO = :CODIGO AND O.QUANTPEND > 0 AND O.TIPO IN ('C', 'V', 'B')
#                     ORDER BY O.DATA, O.TIPO, O.ID
#                     """
#         params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
#         return db.session.execute(query, params).fetchall()

#     @classmethod
#     def buscar_desdobro_grupamento(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT O.ID, O.IDUSUARIO, O.IDBDR AS IDBDR, E.CODIGO AS CODIGOBDR, E.SITUACAO AS SITUACAOBDR, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
#                            O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
#                            O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO, O.TROCA, O.SITUACAO 
#                     FROM TBBDR_LANCAMENTO O
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = O.IDBDR     )  
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
#                     WHERE O.IDUSUARIO = :IDUSUARIO
#                       AND E.CODIGO    = :CODIGO
#                       AND O.TIPO      IN ('D', 'G')
#                       AND O.QUANT     > 0
#                     ORDER BY O.DATA, O.TIPO, O.ID
#                     """
#         params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
#         return db.session.execute(query, params).fetchall()

#     @classmethod
#     def buscar_menor_ano(cls, id_usuario: int = None, id_bdr: int = None):
#         query = """ SELECT SUBSTRING(MIN(L.DATA), 1, 4) AS MENORANO FROM TBBDR_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO """
#         if id_bdr: query += """ AND L.IDBDR = :IDBDR """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_bdr: params['IDBDR'] = id_bdr
#         return db.session.execute(query, params)

#     @classmethod
#     def buscar_maior_ano(cls, id_usuario: int = None, id_bdr: int = None):
#         query = """ SELECT SUBSTRING(MAX(L.DATA), 1, 4) AS MAIORANO FROM TBBDR_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO """
#         if id_bdr: query += """ AND L.IDBDR = :IDBDR """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_bdr: params['IDBDR'] = id_bdr
#         return db.session.execute(query, params)

#     @classmethod
#     def buscar_total_compra(cls, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(L.QUANT) AS QTDE FROM TBBDR_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO AND L.IDBDR = :IDBDR AND L.TIPO IN ( 'C', 'B') """
#         if dt_fim: query += """ AND L.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDBDR'] = id_bdr
#         if dt_fim: params['DATAFIM'] = dt_fim
#         rows = db.session.execute(query, params).first()
#         return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0

#     @classmethod
#     def buscar_total_venda(cls, id_usuario: int = None, id_bdr: int = None, id_lanc: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(L.QUANT) AS QTDE FROM TBBDR_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO AND L.IDBDR = :IDBDR AND L.TIPO = 'V' """
#         if id_lanc: query += """ AND L.ID <> :ID """
#         if dt_fim: query += """ AND L.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDBDR'] = id_bdr
#         if dt_fim: params['ID'] = id_lanc
#         if dt_fim: params['DATAFIM'] = dt_fim
#         rows = db.session.execute(query, params).first()
#         return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0

#     @classmethod
#     def buscar_quant_operacao(cls, id_usuario: int = None, situacao: str = None, tipo: str = None):
#         try:

#             query = " SELECT COUNT(1) AS QTDE FROM TBBDR_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO "
#             if situacao: query += " AND L.SITUACAO = :SITUACAO "
#             if tipo: query += """ AND L.TIPO = :TIPO """

#             params = {}
#             params['IDUSUARIO'] = id_usuario
#             if situacao: params['SITUACAO'] = situacao
#             if tipo: params['TIPO'] = tipo

#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] and rows[0] > 0 else 0

#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     @asyncio.coroutine
#     async def buscar_qtde_total_base(cls, tipo: str = None):
#         query = """ SELECT COUNT(1) AS QTDE FROM TBBDR_LANCAMENTO L WHERE 1 = 1 """
#         if tipo: query += """ AND L.TIPO = :TIPO """
#         params = {}
#         if tipo: params['TIPO'] = tipo
#         rows = db.session.execute(query, params).first()
#         return rows[0] if rows and rows[0] and rows[0] > 0 else 0

#     @classmethod
#     def buscar_dados_grid_irpf(cls, id_usuario: int = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT MAX(E.CODIGO) AS CODIGO, MAX(E.CNPJ) AS CNPJ, MAX(E.RAZAOSOCIAL) AS RAZAOSOCIAL, SUM(L.TOTVLR) AS TOTVLR
#                     FROM TBBDR_LANCAMENTO L
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = L.IDBDR )
#                     WHERE L.IDUSUARIO = :IDUSUARIO AND L.TIPO = :TIPO AND L.DATA >= :DATAINICIO AND L.DATA <= :DATAFIM
#                     GROUP BY L.IDBDR
#                     ORDER BY E.RAZAOSOCIAL
#                 """
#         params = {'IDUSUARIO': id_usuario, 'TIPO': tipo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
#         return db.session.execute(query, params)

#     @classmethod
#     def buscar_lista_datas_day_trade(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT DISTINCT LV.DATA
#                     FROM TBBDR_LANCAMENTO LV
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = LV.IDBDR )
#                     WHERE LV.IDUSUARIO = :IDUSUARIO
#                       AND E.CODIGO     = :CODIGO
#                       AND LV.TIPO      = 'V'
#                       AND EXISTS( SELECT 1
#                                   FROM TBBDR_LANCAMENTO LC
#                                   WHERE LC.IDUSUARIO = LV.IDUSUARIO
#                                     AND LC.IDBDR   = LV.IDBDR
#                                     AND LC.TIPO      IN ('C', 'B')
#                                     AND LC.DATA      = LV.DATA
#                                     AND LC.ID        < LV.ID
#                                 )
#                     ORDER BY LV.DATA
#                 """
#         params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
#         return db.session.execute(query, params).fetchall()

#     @classmethod
#     def atualizar_qtd_pend_situacao(cls, id_usuario: int, id_lanc: int, qtd_pend: int, situacao: str, commit: bool = True):
#         try:
#             query = "UPDATE TBBDR_LANCAMENTO SET QUANTPEND = :QUANTPEND, SITUACAO = :SITUACAO WHERE IDUSUARIO = :IDUSUARIO AND ID = :ID "
#             params = {'IDUSUARIO': id_usuario, 'ID': id_lanc, 'QUANTPEND': qtd_pend, 'SITUACAO': situacao}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise

#     @classmethod
#     def resetar_ativos(cls, id_usuario: int, id_bdr: int, commit: bool = True):
#         try:
#             query = "UPDATE TBBDR_LANCAMENTO SET QUANTPEND = QUANT, SITUACAO = 'P' WHERE IDUSUARIO = :IDUSUARIO AND IDBDR = :IDBDR"
#             params = {'IDUSUARIO': id_usuario, 'IDBDR': id_bdr}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBBDR_LANCAMENTO WHERE IDUSUARIO = :IDUSUARIO"
#             params = {'IDUSUARIO': id_usuario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise

#     def salvar(self, commit: bool = True):
#         try:
#             db.session.add(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise

#     def excluir(self, commit: bool = True):
#         try:
#             db.session.delete(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             raise

#     def calc_tot_preco(self) -> None:
#         self.tot_vlr_preco = self.calcular_tot_preco(quant=self.quant, vlr_preco=self.vlr_preco)

#     def calc_tot_taxa(self) -> None:
#         self.tot_vlr_taxa = self.calcular_tot_taxa(vlr_liquidacao=self.vlr_liquidacao, vlr_emolumentos=self.vlr_emolumentos, vlr_corretagem=self.vlr_corretagem, vlr_iss=self.vlr_iss, vlr_outras=self.vlr_outras)

#     def calc_total(self) -> None:
#         self.tot_vlr = self.calcular_total(tipo=self.tipo, tot_vlr_preco=self.tot_vlr_preco, tot_vlr_taxa=self.tot_vlr_taxa)

#     def calc_custo(self) -> None:
#         self.vlr_custo = self.calcular_custo(quant=self.quant, tot_vlr=self.tot_vlr)

#     def data_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def quant_format(self) -> str:
#         return inteiro_to_str(valor=self.quant)

#     def quant_pend_format(self) -> str:
#         return inteiro_to_str(valor=self.quant_pend)

#     def vlr_preco_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco)

#     def tot_vlr_preco_format(self) -> str:
#         return decimal_to_str(valor=self.tot_vlr_preco)

#     def vlr_liquidacao_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_liquidacao)

#     def vlr_emolumentos_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_emolumentos)

#     def vlr_corretagem_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_corretagem)

#     def vlr_irpf_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_irpf)

#     def vlr_iss_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_iss)

#     def vlr_outras_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_outras)

#     def tot_vlr_taxa_format(self) -> str:
#         return decimal_to_str(valor=self.tot_vlr_taxa)

#     def tot_vlr_format(self) -> str:
#         return decimal_to_str(valor=self.tot_vlr)

#     def vlr_custo_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_custo)

#     def tipo_descr(self) -> str:
#         return self.descricao_tipo(tipo=self.tipo, troca=self.troca)

#     def situacao_descr(self) -> str:
#         return self.descricao_situacao(situacao=self.situacao)

#     @classmethod
#     def calcular_tot_preco(cls, quant: float, vlr_preco: float) -> float:
#         return float(quant) * float(vlr_preco) if quant > 0.0 and vlr_preco > 0.0 else 0.0

#     @classmethod
#     def calcular_tot_taxa(cls, vlr_liquidacao: float, vlr_emolumentos: float, vlr_corretagem: float, vlr_iss: float, vlr_outras: float) -> float:
#         return float(vlr_liquidacao) + float(vlr_emolumentos) + float(vlr_corretagem) + float(vlr_iss) + float(vlr_outras)

#     @classmethod
#     def calcular_total(cls, tipo: str, tot_vlr_preco: float, tot_vlr_taxa: float) -> float:
#         tot_vlr = 0.0
#         if str(tipo) == 'C' or str(tipo) == 'B':
#             tot_vlr = float(tot_vlr_preco) + float(tot_vlr_taxa)
#         elif str(tipo) == 'V':
#             tot_vlr = float(tot_vlr_preco) - float(tot_vlr_taxa)
#         return tot_vlr

#     @classmethod
#     def calcular_custo(cls, quant: float, tot_vlr: float) -> float:
#         return (float(tot_vlr) / float(quant)) if quant > 0.0 and tot_vlr > 0.0 else 0.0

#     @classmethod
#     def descricao_tipo(cls, tipo: str, troca: str = 'N') -> str:
#         if tipo == 'C' and str(troca) != 'S': return 'Compra'
#         elif tipo == 'C' and troca == 'S': return 'Compra/Troca'
#         elif tipo == 'V' and str(troca) != 'S': return 'Venda'
#         elif tipo == 'V' and troca == 'S': return 'Venda/Troca'
#         elif tipo == 'B': return 'Bonificação'
#         elif tipo == 'D': return 'Desdobramento'
#         elif tipo == 'G': return 'Grupamento'
#         elif tipo == 'P': return 'Projetado'
#         else: return 'Desconhecido'

#     @classmethod
#     def descricao_situacao(cls, situacao: str) -> str:
#         if situacao == 'A': return 'Ativo'
#         elif situacao == 'P': return 'Pendente'
#         else: return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioEmpresaLancamento {str(self.id)}>'
