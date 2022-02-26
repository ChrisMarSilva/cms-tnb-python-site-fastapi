# # -*- coding: utf-8 -*-
# import sys
# import os
# import asyncio
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str, inteiro_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class UsuarioCriptoLancamento(db.Model):

#     __tablename__ = "TBCRIPTO_LANCAMENTO"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
#     id_cripto = db.Column('IDCRIPTO', db.Integer, db.ForeignKey('TBCRIPTO_EMPRESA.ID'), nullable=False, index=True)
#     id_corretora = db.Column('IDCORRETORA', db.Integer, db.ForeignKey('TBCORRETORA.ID'), nullable=True)
#     tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
#     data = db.Column('DATA', db.String(8), nullable=False, index=True)
#     quant = db.Column('QUANT', db.Float(30, 15), nullable=False)
#     quant_orig = db.Column('QUANTORIG', db.Float(30, 15), nullable=False, index=True)
#     vlr_preco = db.Column('VLRPRECO', db.Float(30, 15), nullable=True)
#     tot_vlr_preco = db.Column('TOTVLRPRECO', db.Float(30, 15), nullable=True)
#     vlr_corretagem = db.Column('VLRTAXA', db.Float(17, 2), nullable=True)
#     tot_vlr = db.Column('TOTVLR', db.Float(17, 2), nullable=True)
#     vlr_custo = db.Column('VLRCUSTO', db.Float(30, 15), nullable=True)
#     tot_vlr_custo = db.Column('TOTVLRCUSTO', db.Float(17, 2), nullable=True)
#     vlr_preco_medio = db.Column('VLRPRECOMEDIO', db.Float(30, 15), nullable=True)
#     tot_vlr_valorizacao = db.Column('TOTVLRVALORIZACAO', db.Float(17, 2), nullable=True)
#     perc_valorizacao = db.Column('PERCVALORIZACAO', db.Float(17, 2), nullable=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_usuario: int = None, id_cripto: int = None, id_corretora: int = None,
#                  tipo: str = None, data: str = None, quant: float = 0.0, quant_orig: float = 0.0,
#                  vlr_preco: float = 0.0, tot_vlr_preco: float = 0.0, vlr_corretagem: float = 0.0, tot_vlr: float = 0.0,
#                  vlr_custo: float = 0.0, tot_vlr_custo: float = 0.0, vlr_preco_medio: float = 0.0,
#                  tot_vlr_valorizacao: float = 0.0,  perc_valorizacao: float = 0.0,
#                  situacao: str = None):
#         self.id = id
#         self.id_usuario = id_usuario
#         self.id_cripto = id_cripto
#         self.id_corretora = id_corretora
#         self.tipo = tipo
#         self.data = data
#         self.quant = quant
#         self.quant_orig = quant_orig
#         self.vlr_preco = vlr_preco
#         self.tot_vlr_preco = tot_vlr_preco
#         self.vlr_corretagem = vlr_corretagem
#         self.tot_vlr = tot_vlr
#         self.vlr_custo = vlr_custo
#         self.tot_vlr_custo = tot_vlr_custo
#         self.vlr_preco_medio = vlr_preco_medio
#         self.tot_vlr_valorizacao = tot_vlr_valorizacao
#         self.perc_valorizacao = perc_valorizacao
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls, id_usuario: int = None, id_cripto: int = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None):
#         try:

#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_cripto: filters.append(cls.id_cripto == id_cripto)
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
#     def get_all_by_cripto(cls, id_cripto: int):
#         try:
#             return cls.query.filter_by(id_cripto=id_cripto).all()
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
#     def get_menor_ano(cls, id_usuario: int = None, id_cripto: int = None):
#         try:

#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_cripto: filters.append(cls.id_cripto == id_cripto)

#             return db.session.query(db.func.min(cls.data)).filter(*filters).first()

#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_maior_ano(cls, id_usuario: int = None, id_cripto: int = None):
#         try:

#             filters = []
#             if id_usuario: filters.append(cls.id_usuario == id_usuario)
#             if id_cripto: filters.append(cls.id_cripto == id_cripto)

#             return db.session.query(db.func.max(cls.data)).filter(*filters).first()

#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None, ordem: str = None, id_corretora: str = None):
#         query = """ SELECT FL.ID, FL.IDUSUARIO, FL.IDCRIPTO AS IDCRIPTO, F.NOME AS NOMECRIPTO, F.CODIGO AS CODIGOCRIPTO, F.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO, F.VLRPRECOANTERIOR AS VLRPRECOANTERIOR, F.VLRVARIACAO AS VLRVARIACAO, F.SITUACAO AS SITUACAOCRIPTO, FL.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, FL.TIPO, FL.DATA, FL.QUANTORIG, FL.QUANT, FL.VLRPRECO, FL.TOTVLRPRECO, FL.VLRTAXA, FL.TOTVLR, FL.VLRCUSTO, FL.TOTVLRCUSTO, FL.VLRPRECOMEDIO, FL.TOTVLRVALORIZACAO, FL.PERCVALORIZACAO, FL.SITUACAO 
#                     FROM TBCRIPTO_LANCAMENTO FL
#                       INNER JOIN TBCRIPTO_EMPRESA F ON ( F.ID = FL.IDCRIPTO )
#                       LEFT  JOIN TBCORRETORA C ON ( C.ID = FL.IDCORRETORA )
#                     WHERE FL.IDUSUARIO = :IDUSUARIO
#         """

#         if codigo: query += " AND F.CODIGO = :CODIGO "
#         if dt_ini: query += " AND FL.DATA >= :DATAINICIO "
#         if dt_fim: query += " AND FL.DATA <= :DATAFIM "
#         if tipo: query += " AND FL.TIPO = :TIPO "
#         if id_corretora: query += " AND FL.IDCORRETORA = :IDCORRETORA "

#         if ordem: query += " ORDER BY FL.DATA DESC, FL.ID, FL.TIPO "
#         else: query += " ORDER BY FL.DATA, FL.ID, FL.TIPO "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         if dt_ini: params['DATAINICIO'] = dt_ini
#         if dt_fim: params['DATAFIM'] = dt_fim
#         if tipo: params['TIPO'] = tipo
#         if id_corretora: params['IDCORRETORA'] = id_corretora

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise


#     @classmethod
#     def buscar_por_id(cls, id_usuario: int = None, id: int = None):
#         query = """ SELECT FL.ID, FL.IDUSUARIO, FL.IDCRIPTO AS IDCRIPTO, F.NOME AS NOMECRIPTO, F.CODIGO AS CODIGOCRIPTO, F.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO, F.VLRPRECOANTERIOR AS VLRPRECOANTERIOR, F.VLRVARIACAO AS VLRVARIACAO, F.SITUACAO AS SITUACAOCRIPTO, FL.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, FL.TIPO, FL.DATA, FL.QUANTORIG, FL.QUANT, FL.VLRPRECO, FL.TOTVLRPRECO, FL.VLRTAXA, FL.TOTVLR, FL.VLRCUSTO, FL.TOTVLRCUSTO, FL.VLRPRECOMEDIO, FL.TOTVLRVALORIZACAO, FL.PERCVALORIZACAO, FL.SITUACAO
#                     FROM TBCRIPTO_LANCAMENTO FL
#                       INNER JOIN TBCRIPTO_EMPRESA F ON ( F.ID = FL.IDCRIPTO )
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
#         query = """ SELECT FL.ID, FL.IDUSUARIO, FL.IDCRIPTO AS IDCRIPTO, F.NOME AS NOMECRIPTO, F.CODIGO AS CODIGOCRIPTO, F.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO, F.VLRPRECOANTERIOR AS VLRPRECOANTERIOR, F.VLRVARIACAO AS VLRVARIACAO, F.SITUACAO AS SITUACAOCRIPTO, FL.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, FL.TIPO, FL.DATA, FL.QUANTORIG, FL.QUANT, FL.VLRPRECO, FL.TOTVLRPRECO, FL.VLRTAXA, FL.TOTVLR, FL.VLRCUSTO, FL.TOTVLRCUSTO, FL.VLRPRECOMEDIO, FL.TOTVLRVALORIZACAO, FL.PERCVALORIZACAO, FL.SITUACAO
#                     FROM TBCRIPTO_LANCAMENTO FL
#                       INNER JOIN TBCRIPTO_EMPRESA F ON ( F.ID = FL.IDCRIPTO )
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
#     def buscar_menor_ano(cls, id_usuario: int = None, id_cripto: int = None):
#         query = """ SELECT SUBSTRING(MIN(FL.DATA), 1, 4) AS MENORANO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO """
#         if id_cripto: query += """ AND FL.IDCRIPTO = :IDCRIPTO """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_cripto: params['IDCRIPTO'] = id_cripto
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_maior_ano(cls, id_usuario: int = None, id_cripto: int = None):
#         query = """ SELECT SUBSTRING(MAX(FL.DATA), 1, 4) AS MAIORANO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO """
#         if id_cripto: query += """ AND FL.IDCRIPTO = :IDCRIPTO """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_cripto: params['IDCRIPTO'] = id_cripto
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_total_compra(cls, id_usuario: int = None, id_cripto: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDCRIPTO = :IDCRIPTO AND FL.TIPO = 'C' """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDCRIPTO'] = id_cripto
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_total_venda(cls, id_usuario: int = None, id_cripto: int = None, id_lanc: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDCRIPTO = :IDCRIPTO AND FL.TIPO = 'V' """
#         if id_lanc: query += """ AND FL.ID <> :ID """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDCRIPTO'] = id_cripto
#         if id_lanc: params['ID'] = id_lanc
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_valor_total_compra(cls, id_usuario: int = None, id_cripto: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDCRIPTO = :IDCRIPTO AND FL.TIPO = 'C' """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDCRIPTO'] = id_cripto
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_valor_total_venda(cls, id_usuario: int = None, id_cripto: int = None, id_lanc: int = None, dt_fim: str = None):
#         query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDCRIPTO = :IDCRIPTO AND FL.TIPO = 'V' """
#         if id_lanc: query += """ AND FL.ID <> :ID """
#         if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDCRIPTO'] = id_cripto
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

#             query = " SELECT COUNT(1) AS QTDE FROM TBCRIPTO_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO "
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
#         query = """ SELECT COUNT(1) AS QTDE FROM TBCRIPTO_LANCAMENTO L WHERE 1 = 1 """
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
#         query = """ SELECT COUNT(1) AS QTDE FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'A' """
#         params = {'IDUSUARIO': id_usuario }
#         try:
#             rows = db.session.execute(query, params).first()
#             return int(rows[0]) if rows and rows[0] and int(rows[0]) > 0 else 0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_preco_medio(cls, id_usuario: int = None, id_cripto: int = None, dt_fim: str = None):
#         query = """ SELECT FL.VLRPRECOMEDIO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.ID = ( SELECT MAX(FLANT.ID) FROM TBCRIPTO_LANCAMENTO FLANT WHERE FLANT.IDUSUARIO = :IDUSUARIO AND FLANT.IDCRIPTO = :IDCRIPTO AND FLANT.SITUACAO = 'A' """
#         if dt_fim: query += """ AND FLANT.DATA <= :DATAFIM """
#         query += " ) "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDCRIPTO'] = id_cripto
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_preco_medio_antes(cls, id_usuario: int = None, id_cripto: int = None, dt_fim: str = None):
#         query = """ SELECT FL.VLRPRECOMEDIO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.ID = ( SELECT MAX(FLANT.ID) FROM TBCRIPTO_LANCAMENTO FLANT WHERE FLANT.IDUSUARIO = :IDUSUARIO AND FLANT.IDCRIPTO = :IDCRIPTO AND FLANT.SITUACAO = 'A' """
#         if dt_fim: query += """ AND FLANT.DATA < :DATAFIM """
#         query += " ) "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDCRIPTO'] = id_cripto
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_dados_grid_irpf(cls, id_usuario: int = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT MAX(F.CODIGO) AS CODIGO,
#                            MAX(F.NOME)   AS NOME,
#                            SUM(FL.TOTVLR)      AS TOTVLR
#                     FROM TBCRIPTO_LANCAMENTO FL
#                       INNER JOIN TBCRIPTO_EMPRESA F ON ( F.ID = FL.IDCRIPTO )
#                     WHERE FL.IDUSUARIO = :IDUSUARIO
#                       AND FL.TIPO      = :TIPO
#                       AND FL.DATA      >= :DATAINICIO
#                       AND FL.DATA      <= :DATAFIM
#                     GROUP BY FL.IDCRIPTO
#                     ORDER BY F.NOME
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
#             query = "UPDATE TBCRIPTO_LANCAMENTO SET SITUACAO = :SITUACAO WHERE IDUSUARIO = :IDUSUARIO AND ID = :ID "
#             params = {'IDUSUARIO': id_usuario, 'ID': id_lanc, 'SITUACAO': situacao}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def resetar_ativos(cls, id_usuario: int, id_cripto: int, commit: bool = True):
#         try:
#             query = " UPDATE TBCRIPTO_LANCAMENTO SET QUANT = QUANTORIG, TOTVLRCUSTO = 0.00, VLRPRECOMEDIO = 0.00, TOTVLRVALORIZACAO = 0.00, PERCVALORIZACAO = 0.00, SITUACAO = 'P' WHERE IDCRIPTO = :IDCRIPTO AND IDUSUARIO = :IDUSUARIO "
#             params = {'IDUSUARIO': id_usuario, 'IDCRIPTO': id_cripto}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo_fundo(cls, id_usuario: int, id_cripto: int, commit: bool = True):
#         try:
#             query = " DELETE FROM TBCRIPTO_LANCAMENTO WHERE IDCRIPTO = :IDCRIPTO AND IDUSUARIO = :IDUSUARIO "
#             params = {'IDCRIPTO': id_cripto, 'IDUSUARIO': id_usuario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = " DELETE FROM TBCRIPTO_LANCAMENTO WHERE IDUSUARIO = :IDUSUARIO "
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
#         # self.vlr_corretagem = self.vlr_corretagem
#         pass

#     def calc_total(self) -> None:
#         self.tot_vlr = self.calcular_total(tipo=self.tipo, tot_vlr_preco=self.tot_vlr_preco, vlr_corretagem=self.vlr_corretagem)

#     def calc_custo(self) -> None:
#         self.vlr_custo = self.calcular_custo(quant=self.quant, tot_vlr=self.tot_vlr)

#     def calc_preco_medio(self, qtde_atual: float = 0.0, preco_medio_atual: float = 0.0):
#         self.vlr_preco_medio = 0.0
#         if str(self.tipo) == 'C':
#             tot_vlr_custo = float(self.vlr_custo) * float(self.quant) if float(self.vlr_custo) > 0.0 and float(self.quant) > 0.0 else 0.0
#             if qtde_atual > 0.0 and preco_medio_atual > 0.0:
#                 tot_vlr_custo += (float(qtde_atual) * float(preco_medio_atual)) if float(qtde_atual) > 0.0 and float(preco_medio_atual) > 0.0 else 0.0
#             qtde_atual += float(self.quant)
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

#     def vlr_corretagem_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_corretagem)

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
#         return self.descricao_tipo(tipo=self.tipo)

#     def situacao_descr(self) -> str:
#         return self.descricao_situacao(situacao=self.situacao)

#     @classmethod
#     def calcular_tot_preco(cls, quant: float, vlr_preco: float) -> float:
#         return float(quant) * float(vlr_preco) if quant > 0.0 and vlr_preco > 0.0 else 0.0

#     @classmethod
#     def calcular_total(cls, tipo: str, tot_vlr_preco: float, vlr_corretagem: float) -> float:
#         tot_vlr = 0.0
#         if str(tipo) == 'C':
#             tot_vlr = float(tot_vlr_preco) + float(vlr_corretagem)
#         elif str(tipo) == 'V':
#             tot_vlr = float(tot_vlr_preco) - float(vlr_corretagem)
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
#     def descricao_tipo(cls, tipo: str) -> str:
#         if tipo == 'C': return 'Compra'
#         elif tipo == 'V': return 'Venda'
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
#         return '<UsuarioCriptoLancamento {str(self.id)}>'
