# # -*- coding: utf-8 -*-
# import sys
# import os
# import asyncio
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str, inteiro_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class UsuarioFiiFundoImobLancamento(db.Model):

#     __tablename__ = "TBFII_LANCAMENTO"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
#     id_fundo = db.Column('IDFUNDO', db.Integer, db.ForeignKey('TBFII_FUNDOIMOB.ID'), nullable=False, index=True)
#     id_corretora = db.Column('IDCORRETORA', db.Integer, db.ForeignKey('TBCORRETORA.ID'), nullable=True)
#     tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
#     data = db.Column('DATA', db.String(8), nullable=False, index=True)
#     quant = db.Column('QUANT', db.Float(20, 10), nullable=False)
#     quant_orig = db.Column('QUANTORIG', db.Float(20, 10), nullable=False, index=True)
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
#     tot_vlr_custo = db.Column('TOTVLRCUSTO', db.Float(17, 2), nullable=True)
#     vlr_preco_medio = db.Column('VLRPRECOMEDIO', db.Float(20, 10), nullable=True)
#     tot_vlr_valorizacao = db.Column('TOTVLRVALORIZACAO', db.Float(17, 2), nullable=True)
#     perc_valorizacao = db.Column('PERCVALORIZACAO', db.Float(17, 2), nullable=True)
#     troca = db.Column('TROCA', db.String(1), nullable=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_usuario: int = None, id_fundo: int = None, id_corretora: int = None,
#                  tipo: str = None, data: str = None, quant: float = 0.0, quant_orig: float = 0.0,
#                  vlr_preco: float = 0.0, tot_vlr_preco: float = 0.0, vlr_liquidacao: float = 0.0,
#                  vlr_emolumentos: float = 0.0, vlr_corretagem: float = 0.0, vlr_irpf: float = 0.0,
#                  vlr_iss: float = 0.0, vlr_outras: float = 0.0, tot_vlr_taxa: float = 0.0, tot_vlr: float = 0.0,
#                  vlr_custo: float = 0.0, tot_vlr_custo: float = 0.0, vlr_preco_medio: float = 0.0,
#                  tot_vlr_valorizacao: float = 0.0,  perc_valorizacao: float = 0.0, troca: str = 'N',
#                  situacao: str = None):
#         self.id = id
#         self.id_usuario = id_usuario
#         self.id_fundo = id_fundo
#         self.id_corretora = id_corretora
#         self.tipo = tipo
#         self.data = data
#         self.quant = quant
#         self.quant_orig = quant_orig
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
#         self.tot_vlr_custo = tot_vlr_custo
#         self.vlr_preco_medio = vlr_preco_medio
#         self.tot_vlr_valorizacao = tot_vlr_valorizacao
#         self.perc_valorizacao = perc_valorizacao
#         self.troca = troca
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None):
#         try:

#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_fundo: filters.append(cls.id_fundo == id_fundo)
#             if dt_ini: filters.append(cls.data >= dt_ini)
#             if dt_fim: filters.append(cls.data <= dt_fim)
#             if tipo: filters.append(cls.tipo == tipo)

#             return cls.query.filter(*filters).order_by(cls.id).all()

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
#     def get_all_by_fundo(cls, id_fundo: int):
#         try:
#             return cls.query.filter_by(id_fundo=id_fundo).all()
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
#     def get_menor_ano(cls, id_usuario: int = None, id_fundo: int = None):
#         try:

#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_fundo: filters.append(cls.id_fundo == id_fundo)

#             return db.session.query(db.func.min(cls.data)).filter(*filters).first()

#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_maior_ano(cls, id_usuario: int = None, id_fundo: int = None):
#         try:

#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_fundo: filters.append(cls.id_fundo == id_fundo)

#             return db.session.query(db.func.max(cls.data)).filter(*filters).first()

#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None, ordem: str = None, id_corretora: str = None, troca: str = None):
#         query = """ SELECT FL.ID, 
#                            FL.IDUSUARIO, 
#                            FL.IDFUNDO     AS IDFUNDO, 
#                            F.NOME         AS NOMEFUNDO, 
#                            F.CODIGO       AS CODIGOFUNDO, 
#                            F.SITUACAO     AS SITUACAOFUNDO, 
#                            FL.IDCORRETORA AS IDCORRETORA, 
#                            C.NOME         AS NOMECORRETORA, 
#                            FL.TIPO, 
#                            FL.DATA, 
#                            FL.QUANTORIG, 
#                            FL.QUANT, 
#                            FL.VLRPRECO, 
#                            FL.TOTVLRPRECO, 
#                            FL.VLRTXLIQUIDACAO, 
#                            FL.VLRTXEMOLUMENTOS, 
#                            FL.VLRTXCORRETAGEM, 
#                            FL.VLRTXISS, 
#                            FL.VLRTXIRRF, 
#                            FL.VLRTXOUTRAS, 
#                            FL.TOTVLRTX, 
#                            FL.TOTVLR, 
#                            FL.VLRCUSTO, 
#                            FL.TOTVLRCUSTO, 
#                            FL.VLRPRECOMEDIO, 
#                            FL.TOTVLRVALORIZACAO, 
#                            FL.PERCVALORIZACAO, 
#                            FL.TROCA, 
#                            FL.SITUACAO 
#                     FROM TBFII_LANCAMENTO FL
#                       INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO     )
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
#                     WHERE FL.IDUSUARIO = :IDUSUARIO
#         """

#         if codigo: query += " AND F.CODIGO = :CODIGO "
#         if dt_ini: query += " AND FL.DATA >= :DATAINICIO "
#         if dt_fim: query += " AND FL.DATA <= :DATAFIM "
#         if tipo: query += " AND FL.TIPO = :TIPO "
#         if id_corretora: query += " AND FL.IDCORRETORA = :IDCORRETORA "
#         if troca: query += " AND IFNULL(FL.TROCA, 'N') = :TROCA "

#         if ordem: query += " ORDER BY FL.DATA DESC, FL.ID, FL.TIPO "
#         else: query += " ORDER BY FL.DATA, FL.ID, FL.TIPO "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         if dt_ini: params['DATAINICIO'] = dt_ini
#         if dt_fim: params['DATAFIM'] = dt_fim
#         if tipo: params['TIPO'] = tipo
#         if id_corretora: params['IDCORRETORA'] = id_corretora
#         if troca: params['TROCA'] = troca

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise


#     @classmethod
#     def buscar_por_id(cls, id_usuario: int = None, id: int = None):
#         query = """ SELECT FL.ID, 
#                            FL.IDUSUARIO, 
#                            FL.IDFUNDO     AS IDFUNDO, 
#                            F.NOME         AS NOMEFUNDO, 
#                            F.CODIGO       AS CODIGOFUNDO, 
#                            F.SITUACAO     AS SITUACAOFUNDO, 
#                            FL.IDCORRETORA AS IDCORRETORA, 
#                            C.NOME         AS NOMECORRETORA, 
#                            FL.TIPO, 
#                            FL.DATA, 
#                            FL.QUANTORIG, 
#                            FL.QUANT, 
#                            FL.VLRPRECO, 
#                            FL.TOTVLRPRECO, 
#                            FL.VLRTXLIQUIDACAO, 
#                            FL.VLRTXEMOLUMENTOS, 
#                            FL.VLRTXCORRETAGEM, 
#                            FL.VLRTXISS, 
#                            FL.VLRTXIRRF, 
#                            FL.VLRTXOUTRAS, 
#                            FL.TOTVLRTX, 
#                            FL.TOTVLR, 
#                            FL.VLRCUSTO, 
#                            FL.TOTVLRCUSTO, 
#                            FL.VLRPRECOMEDIO, 
#                            FL.TOTVLRVALORIZACAO, 
#                            FL.PERCVALORIZACAO, 
#                            FL.TROCA, 
#                            FL.SITUACAO 
#                     FROM TBFII_LANCAMENTO FL
#                       INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO     )
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
#                     WHERE FL.ID        = :ID
#                       AND FL.IDUSUARIO = :IDUSUARIO
#                 """
#         params = {'ID': id, 'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_codigo(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT FL.ID, 
#                            FL.IDUSUARIO, 
#                            FL.IDFUNDO     AS IDFUNDO, 
#                            F.NOME         AS NOMEFUNDO, 
#                            F.CODIGO       AS CODIGOFUNDO, 
#                            F.SITUACAO     AS SITUACAOFUNDO, 
#                            FL.IDCORRETORA AS IDCORRETORA, 
#                            C.NOME         AS NOMECORRETORA, 
#                            FL.TIPO, 
#                            FL.DATA, 
#                            FL.QUANTORIG, 
#                            FL.QUANT, 
#                            FL.VLRPRECO, 
#                            FL.TOTVLRPRECO, 
#                            FL.VLRTXLIQUIDACAO, 
#                            FL.VLRTXEMOLUMENTOS, 
#                            FL.VLRTXCORRETAGEM, 
#                            FL.VLRTXISS, 
#                            FL.VLRTXIRRF, 
#                            FL.VLRTXOUTRAS, 
#                            FL.TOTVLRTX, 
#                            FL.TOTVLR, 
#                            FL.VLRCUSTO, 
#                            FL.TOTVLRCUSTO, 
#                            FL.VLRPRECOMEDIO, 
#                            FL.TOTVLRVALORIZACAO, 
#                            FL.PERCVALORIZACAO, 
#                            FL.TROCA, 
#                            FL.SITUACAO 
#                     FROM TBFII_LANCAMENTO FL
#                       INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO     )
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
#                     WHERE FL.IDUSUARIO = :IDUSUARIO
#                       AND F.CODIGO     = :CODIGO
#                     ORDER BY FL.DATA, FL.TIPO 
#                 """
#         params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_desdobro_grupamento(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT FL.ID, 
#                            FL.IDUSUARIO, 
#                            FL.IDFUNDO     AS IDFUNDO, 
#                            F.NOME         AS NOMEFUNDO, 
#                            F.CODIGO       AS CODIGOFUNDO, 
#                            F.SITUACAO     AS SITUACAOFUNDO, 
#                            FL.IDCORRETORA AS IDCORRETORA, 
#                            C.NOME         AS NOMECORRETORA, 
#                            FL.TIPO, 
#                            FL.DATA, 
#                            FL.QUANTORIG, 
#                            FL.QUANT, 
#                            FL.VLRPRECO, 
#                            FL.TOTVLRPRECO, 
#                            FL.VLRTXLIQUIDACAO, 
#                            FL.VLRTXEMOLUMENTOS, 
#                            FL.VLRTXCORRETAGEM, 
#                            FL.VLRTXISS, 
#                            FL.VLRTXIRRF, 
#                            FL.VLRTXOUTRAS, 
#                            FL.TOTVLRTX, 
#                            FL.TOTVLR, 
#                            FL.VLRCUSTO, 
#                            FL.TOTVLRCUSTO, 
#                            FL.VLRPRECOMEDIO, 
#                            FL.TOTVLRVALORIZACAO, 
#                            FL.PERCVALORIZACAO, 
#                            FL.TROCA, 
#                            FL.SITUACAO 
#                     FROM TBFII_LANCAMENTO FL
#                       INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO     )
#                       LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
#                     WHERE FL.IDUSUARIO = :IDUSUARIO
#                       AND F.CODIGO     = :CODIGO
#                       AND FL.TIPO      IN ('D', 'G')
#                       AND FL.QUANT     > 0
#                     ORDER BY FL.DATA, FL.TIPO, FL.ID
#                     """
#         params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
#         try:
#             return db.session.execute(query, params).fetchall()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_menor_ano(cls, id_usuario: int = None, id_fundo: int = None):
#         query = """ SELECT SUBSTRING(MIN(FL.DATA), 1, 4) AS MENORANO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO """
#         if id_fundo: query += """ AND FL.IDFUNDO = :IDFUNDO """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_fundo: params['IDFUNDO'] = id_fundo
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_maior_ano(cls, id_usuario: int = None, id_fundo: int = None):
#         query = """ SELECT SUBSTRING(MAX(FL.DATA), 1, 4) AS MAIORANO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO """
#         if id_fundo: query += """ AND FL.IDFUNDO = :IDFUNDO """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_fundo: params['IDFUNDO'] = id_fundo
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_total_compra(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'C' """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDFUNDO'] = id_fundo
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_total_bonus(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'B' """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDFUNDO'] = id_fundo
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_total_venda(cls, id_usuario: int = None, id_fundo: int = None, id_lanc: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'V' """
#         if id_lanc: query += """ AND FL.ID <> :ID """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDFUNDO'] = id_fundo
#         if id_lanc: params['ID'] = id_lanc
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_valor_total_compra(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'C' """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDFUNDO'] = id_fundo
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_valor_total_bonus(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'B' """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDFUNDO'] = id_fundo
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_valor_total_amortizacao(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'A' """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDFUNDO'] = id_fundo
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_valor_total_venda(cls, id_usuario: int = None, id_fundo: int = None, id_lanc: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'V' """
#         if id_lanc: query += """ AND FL.ID <> :ID """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDFUNDO'] = id_fundo
#         if id_lanc: params['ID'] = id_lanc
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_quant_operacao(cls, id_usuario: int = None, situacao: str = None, tipo: str = None):
#         try:

#             query = " SELECT COUNT(1) AS QTDE FROM TBFII_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO "
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
#         query = """ SELECT COUNT(1) AS QTDE FROM TBFII_LANCAMENTO L WHERE 1 = 1 """
#         if tipo: query += """ AND L.TIPO = :TIPO """
#         params = {}
#         if tipo: params['TIPO'] = tipo
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] and rows[0] > 0 else 0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_quant_ativo(cls, id_usuario: int = None):
#         query = """ SELECT COUNT(1) AS QTDE FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'A' """
#         params = {'IDUSUARIO': id_usuario }
#         try:
#             rows = db.session.execute(query, params).first()
#             return int(rows[0]) if rows and rows[0] and int(rows[0]) > 0 else 0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_preco_medio(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
#         query = """ SELECT FL.VLRPRECOMEDIO FROM TBFII_LANCAMENTO FL WHERE FL.ID = ( SELECT MAX(FLANT.ID) FROM TBFII_LANCAMENTO FLANT WHERE FLANT.IDUSUARIO = :IDUSUARIO AND FLANT.IDFUNDO = :IDFUNDO AND FLANT.SITUACAO = 'A' """
#         if dt_fim: query += """ AND FLANT.DATA <= :DATAFIM """
#         query += " ) "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDFUNDO'] = id_fundo
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_preco_medio_antes(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
#         query = """ SELECT FL.VLRPRECOMEDIO FROM TBFII_LANCAMENTO FL WHERE FL.ID = ( SELECT MAX(FLANT.ID) FROM TBFII_LANCAMENTO FLANT WHERE FLANT.IDUSUARIO = :IDUSUARIO AND FLANT.IDFUNDO = :IDFUNDO AND FLANT.SITUACAO = 'A' """
#         if dt_fim: query += """ AND FLANT.DATA < :DATAFIM """
#         query += " ) "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDFUNDO'] = id_fundo
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_dados_grid_irpf(cls, id_usuario: int = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT MAX(F.CODIGO)      AS CODIGO,
#                            MAX(F.CNPJ)        AS CNPJ,
#                            MAX(F.RAZAOSOCIAL) AS RAZAOSOCIAL,
#                            SUM(FL.TOTVLR)      AS TOTVLR
#                     FROM TBFII_LANCAMENTO FL
#                       INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO   )
#                     WHERE FL.IDUSUARIO = :IDUSUARIO
#                       AND FL.TIPO      = :TIPO
#                       AND FL.DATA      >= :DATAINICIO
#                       AND FL.DATA      <= :DATAFIM
#                     GROUP BY FL.IDFUNDO
#                     ORDER BY F.RAZAOSOCIAL
#                 """
#         params = {'IDUSUARIO': id_usuario, 'TIPO': tipo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def atualizar_qtd_pend_situacao(cls, id_usuario: int, id_lanc: int, situacao: str, commit: bool = True):
#         try:
#             query = "UPDATE TBFII_LANCAMENTO SET SITUACAO = :SITUACAO WHERE IDUSUARIO = :IDUSUARIO AND ID = :ID "
#             params = {'IDUSUARIO': id_usuario, 'ID': id_lanc, 'SITUACAO': situacao}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def resetar_ativos(cls, id_usuario: int, id_fundo: int, commit: bool = True):
#         try:
#             query = "UPDATE TBFII_LANCAMENTO SET QUANT = QUANTORIG, TOTVLRCUSTO = 0.00, VLRPRECOMEDIO = 0.00, TOTVLRVALORIZACAO = 0.00, PERCVALORIZACAO = 0.00, SITUACAO = 'P' WHERE IDFUNDO = :IDFUNDO AND IDUSUARIO = :IDUSUARIO "
#             params = {'IDUSUARIO': id_usuario, 'IDFUNDO': id_fundo}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo_fundo(cls, id_usuario: int, id_fundo: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBFII_LANCAMENTO WHERE IDFUNDO = :IDFUNDO AND IDUSUARIO = :IDUSUARIO"
#             params = {'IDFUNDO': id_fundo, 'IDUSUARIO': id_usuario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBFII_LANCAMENTO WHERE IDUSUARIO = :IDUSUARIO"
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

#     def calc_tot_preco(self) -> None:
#         self.tot_vlr_preco = self.calcular_tot_preco(quant=self.quant, vlr_preco=self.vlr_preco)

#     def calc_tot_taxa(self) -> None:
#         self.tot_vlr_taxa = self.calcular_tot_taxa(vlr_liquidacao=self.vlr_liquidacao, vlr_emolumentos=self.vlr_emolumentos, vlr_corretagem=self.vlr_corretagem, vlr_iss=self.vlr_iss, vlr_outras=self.vlr_outras)

#     def calc_total(self) -> None:
#         self.tot_vlr = self.calcular_total(tipo=self.tipo, tot_vlr_preco=self.tot_vlr_preco, tot_vlr_taxa=self.tot_vlr_taxa)

#     def calc_custo(self) -> None:
#         self.vlr_custo = self.calcular_custo(quant=self.quant, tot_vlr=self.tot_vlr)

#     def calc_preco_medio(self, qtde_atual: float = 0.0, preco_medio_atual: float = 0.0):
#         self.vlr_preco_medio = 0.0
#         if str(self.tipo) == 'C' or str(self.tipo) == 'B':
#             tot_vlr_custo = float(self.vlr_custo) * float(self.quant) if float(self.vlr_custo) > 0.0 and float(self.quant) > 0.0 else 0.0
#             if qtde_atual > 0.0 and preco_medio_atual > 0.0:
#                 tot_vlr_custo += (float(qtde_atual) * float(preco_medio_atual)) if float(qtde_atual) > 0.0 and float(preco_medio_atual) > 0.0 else 0.0
#             qtde_atual += float(self.quant)
#             if qtde_atual > 0.0 and tot_vlr_custo > 0.0:
#                 preco_medio_atual = (float(tot_vlr_custo) / float(qtde_atual)) if float(tot_vlr_custo) > 0.0 and float(qtde_atual) > 0.0 else 0.0
#         elif str(self.tipo) == 'A':
#             tot_vlr_custo = float(self.vlr_custo) * float(self.quant) if float(self.vlr_custo) > 0.0 and float(self.quant) > 0.0 else 0.0
#             if qtde_atual > 0.0 and preco_medio_atual > 0.0:
#                 tot_vlr_custo -= (float(qtde_atual) * float(preco_medio_atual)) if float(qtde_atual) > 0.0 and float(preco_medio_atual) > 0.0 else 0.0
#             if qtde_atual > 0.0 and tot_vlr_custo > 0.0:
#                 preco_medio_atual = (float(tot_vlr_custo) / float(qtde_atual)) if float(tot_vlr_custo) > 0.0 and float(qtde_atual) > 0.0 else 0.0
#         elif str(self.tipo) == 'V' or str(self.tipo) == 'P':
#             qtde_atual -= float(self.quant)
#         self.vlr_preco_medio = float(preco_medio_atual)
#         return float(qtde_atual), float(preco_medio_atual)

#     def calc_vlr_valorizacao(self) -> None:
#         self.tot_vlr_valorizacao = self.calcular_vlr_valorizacao(tipo=str(self.tipo), quant=float(self.quant), vlr_preco_medio=float(self.vlr_preco_medio), tot_vlr_custo=float(self.tot_vlr_custo))

#     def calc_perc_valorizacao(self) -> None:
#         # self.calc_vlr_valorizacao()
#         self.perc_valorizacao = self.calcular_perc_valorizacao(tipo=str(self.tipo), quant=float(self.quant), vlr_preco_medio=float(self.vlr_preco_medio), tot_vlr_valorizacao=float(self.tot_vlr_valorizacao))

#     def data_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%Y-%m-%d')
#     def quant_format(self) -> str:
#         return inteiro_to_str(valor=self.quant)

#     def quant_orig_format(self) -> str:
#         return inteiro_to_str(valor=self.quant_orig)

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

#     def tot_vlr_custo_format(self) -> str:
#         return decimal_to_str(valor=self.tot_vlr_custo)

#     def vlr_preco_medio_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_medio)

#     def tot_vlr_valorizacao_format(self) -> str:
#         return decimal_to_str(valor=self.tot_vlr_valorizacao)

#     def perc_valorizacao_format(self) -> str:
#         return decimal_to_str(valor=self.perc_valorizacao)

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
#         if str(tipo) == 'A' or str(tipo) == 'C' or str(tipo) == 'B':
#             tot_vlr = float(tot_vlr_preco) + float(tot_vlr_taxa)
#         elif str(tipo) == 'V':
#             tot_vlr = float(tot_vlr_preco) - float(tot_vlr_taxa)
#         return tot_vlr

#     @classmethod
#     def calcular_custo(cls, quant: float, tot_vlr: float) -> float:
#         return (float(tot_vlr) / float(quant)) if quant > 0.0 and tot_vlr > 0.0 else 0.0

#     @classmethod
#     def calcular_vlr_valorizacao(cls, tipo: str, quant: float, vlr_preco_medio: float, tot_vlr_custo: float) -> float:
#         tot_vlr_valorizacao = 0.0
#         if (str(tipo) == 'V' or str(tipo) == 'P') and float(vlr_preco_medio) > 0.0 and float(quant) > 0.0:
#             tot_vlr_valorizacao = float(tot_vlr_custo) - (float(vlr_preco_medio) * float(quant))
#         return float(tot_vlr_valorizacao)

#     @classmethod
#     def calcular_perc_valorizacao(cls, tipo: str, quant: float, vlr_preco_medio: float, tot_vlr_valorizacao: float) -> float:
#         perc_valorizacao = 0.0
#         if (str(tipo) == 'V' or str(tipo) == 'P') and float(tot_vlr_valorizacao) != 0.0 and float(vlr_preco_medio) > 0.0 and float(quant) > 0.0:
#             perc_valorizacao = (float(tot_vlr_valorizacao) / (float(vlr_preco_medio) * float(quant))) * 100
#         return float(perc_valorizacao)

#     @classmethod
#     def descricao_tipo(cls, tipo: str, troca: str = 'N') -> str:
#         if tipo == 'C' and str(troca) != 'S': return 'Compra'
#         elif tipo == 'C' and troca == 'S': return 'Compra/Troca'
#         elif tipo == 'V' and str(troca) != 'S': return 'Venda'
#         elif tipo == 'V' and troca == 'S': return 'Venda/Troca'
#         elif tipo == 'A': return 'Amortização'
#         elif tipo == 'B': return 'Bonificação'
#         elif tipo == 'D': return 'Desdobramento'
#         elif tipo == 'G': return 'Grupamento'
#         elif tipo == 'P': return 'Projetado'
#         else: return 'Desconhecido'

#     @classmethod
#     def descricao_situacao(cls, situacao: str) -> str:
#         if situacao == 'A':
#             return 'Ativo'
#         elif situacao == 'P':
#             return 'Pendente'
#         else:
#             return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioFiiFundoImobLancamento {str(self.id)}>'
