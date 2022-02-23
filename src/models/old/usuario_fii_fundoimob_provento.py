# -*- coding: utf-8 -*-
import sys
import os
import asyncio
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str, inteiro_to_str
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioFiiFundoImobProvento(db.Model):

    __tablename__ = "TBFII_PROVENTO"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    id_fundo = db.Column('IDFUNDO', db.Integer, db.ForeignKey('TBFII_FUNDOIMOB.ID'), nullable=False, index=True)
    id_corretora = db.Column('IDCORRETORA', db.Integer, db.ForeignKey('TBCORRETORA.ID'), nullable=True, index=True)
    tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
    data_ex = db.Column('DATAEX', db.String(8), nullable=False, index=True)
    data_pagto = db.Column('DATAPAGTO', db.String(8), nullable=False, index=True)
    quantidade = db.Column('QUANTIDADE', db.Float(20, 10), nullable=False)
    vlr_preco = db.Column('VLRPRECO', db.Float(20, 10), nullable=False)
    tot_vlr = db.Column('TOTVLR', db.Float(17, 2), nullable=False)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, id_fundo: int = None, id_corretora: int = None,
                 tipo: str = None, data_ex: str = None, data_pagto: str = None, quantidade: float = 0.0,
                 vlr_preco: float = 0.0, tot_vlr: float = 0.0, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_fundo = id_fundo
        self.id_corretora = id_corretora
        self.tipo = tipo
        self.data_ex = data_ex
        self.data_pagto = data_pagto
        self.quantidade = quantidade
        self.vlr_preco = vlr_preco
        self.tot_vlr = tot_vlr
        self.situacao = situacao

    @classmethod
    def get_all(cls):
        try:
            return cls.query.all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_all_by_usuario(cls, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_all_by_ativo(cls, id_fundo: int):
        try:
            return cls.query.filter_by(id_fundo=id_fundo).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_id(cls, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_usuario(cls, id: int, id_usuario: int):
        try:
            return cls.query.filter_by(id=id, id_usuario=id_usuario).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_menor_ano(cls, id_usuario: int = None, id_fundo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls.id_usuario == id_usuario)
            if id_fundo: filters.append(cls.id_fundo == id_fundo)

            return db.session.query(db.func.min(cls.data_pagto)).filter(*filters).first()
            # return db.session.query(db.func.min(cls.data_pagto)).filter_by(id_usuario=id_usuario).first()

        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_menor_ano_ex(cls, id_usuario: int = None, id_fundo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls.id_usuario == id_usuario)
            if id_fundo: filters.append(cls.id_fundo == id_fundo)

            return db.session.query(db.func.min(cls.data_ex)).filter(*filters).first()
            # return db.session.query(db.func.min(cls.data_ex)).filter_by(id_usuario=id_usuario).first()

        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_maior_ano(cls, id_usuario: int = None, id_fundo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls.id_usuario == id_usuario)
            if id_fundo: filters.append(cls.id_fundo == id_fundo)

            return db.session.query(db.func.max(cls.data_pagto)).filter(*filters).first()
            # return db.session.query(db.func.max(cls.data_pagto)).filter_by(id_usuario=id_usuario).first()

        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_maior_ano_ex(cls, id_usuario: int = None, id_fundo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls.id_usuario == id_usuario)
            if id_fundo: filters.append(cls.id_fundo == id_fundo)

            return db.session.query(db.func.max(cls.data_ex)).filter(*filters).first()
            # return db.session.query(db.func.max(cls.data_ex)).filter_by(id_usuario=id_usuario).first()

        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int = None, codigo: str = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None, id_corretora: str = None, situacao: str = None):

        query = """ SELECT FP.ID, 
                           FP.IDFUNDO      AS IDFUNDO, 
                           F.NOME          AS NOMEFUNDO, 
                           F.CODIGO        AS CODIGOFUNDO, 
                           F.SITUACAO      AS SITUACAOFUNDO, 
                           FP.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME          AS NOMECORRETORA, 
                           FP.TIPO,  
                           FP.DATAEX,  
                           FP.DATAPAGTO, 
                           FP.QUANTIDADE, 
                           FP.VLRPRECO, 
                           FP.TOTVLR, 
                           FP.SITUACAO 
                    FROM TBFII_PROVENTO            FP
                        INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FP.IDFUNDO     )
                        LEFT  JOIN TBCORRETORA     C ON ( C.ID = FP.IDCORRETORA )
                    WHERE FP.IDUSUARIO = :IDUSUARIO
                """

        if codigo:
            query += " AND F.CODIGO = :CODIGO "
        if tipo:
            query += " AND FP.TIPO = :TIPO "
        if dt_ini:
            query += " AND FP.DATAPAGTO >= :DATAINICIO"
        if dt_fim:
            query += " AND FP.DATAPAGTO <= :DATAFIM "
        if id_corretora:
            query += " AND FP.IDCORRETORA = :IDCORRETORA "
        if situacao:
            query += " AND FP.SITUACAO = :SITUACAO "

        query += " ORDER BY FP.DATAPAGTO, FP.TIPO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo:
            params['CODIGO'] = codigo
        if tipo:
            params['TIPO'] = tipo
        if dt_ini:
            params['DATAINICIO'] = dt_ini
        if dt_fim:
            params['DATAFIM'] = dt_fim
        if id_corretora:
            params['IDCORRETORA'] = id_corretora
        if situacao:
            params['SITUACAO'] = situacao

        try:
            try:
                return db.session.execute(query, params)
            except Exception as e:
                return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id_usuario: int = None, id: int = None):
        query = """ SELECT FP.ID, 
                           FP.IDFUNDO      AS IDFUNDO, 
                           F.NOME          AS NOMEFUNDO, 
                           F.CODIGO        AS CODIGOFUNDO, 
                           F.SITUACAO      AS SITUACAOFUNDO, 
                           FP.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME          AS NOMECORRETORA, 
                           FP.TIPO,  
                           FP.DATAEX,  
                           FP.DATAPAGTO, 
                           FP.QUANTIDADE, 
                           FP.VLRPRECO, 
                           FP.TOTVLR, 
                           FP.SITUACAO 
                    FROM TBFII_PROVENTO            FP
                        INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FP.IDFUNDO     )
                        LEFT  JOIN TBCORRETORA     C ON ( C.ID = FP.IDCORRETORA )
                    WHERE FP.ID        = :ID
                      AND FP.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_codigo(cls, id_usuario: int = None, codigo: str = None):
        query = """ SELECT FP.ID, 
                           FP.IDFUNDO      AS IDFUNDO, 
                           F.NOME          AS NOMEFUNDO, 
                           F.CODIGO        AS CODIGOFUNDO, 
                           F.SITUACAO      AS SITUACAOFUNDO, 
                           FP.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME          AS NOMECORRETORA, 
                           FP.TIPO,  
                           FP.DATAEX,  
                           FP.DATAPAGTO, 
                           FP.QUANTIDADE, 
                           FP.VLRPRECO, 
                           FP.TOTVLR, 
                           FP.SITUACAO 
                    FROM TBFII_PROVENTO            FP
                        INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FP.IDFUNDO     )
                        LEFT  JOIN TBCORRETORA     C ON ( C.ID = FP.IDCORRETORA )
                    WHERE F.CODIGO     = :CODIGO
                      AND FP.IDUSUARIO = :IDUSUARIO
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_dados_grid_irpf(cls, id_usuario: int = None, tipo: str = None, dt_ex_ini: str = None, dt_ex_fim: str = None, dt_pagto_ini: str = None, dt_pagto_fim: str = None):

        query = """ SELECT MAX(F.CODIGO)      AS CODIGO,
                           MAX(F.CNPJ)        AS CNPJ,
                           MAX(F.RAZAOSOCIAL) AS RAZAOSOCIAL,
                           SUM(FP.TOTVLR)     AS TOTVLR
                    FROM TBFII_PROVENTO FP
                        INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FP.IDFUNDO )
                    WHERE FP.IDUSUARIO  = :IDUSUARIO
                      AND FP.TIPO       = :TIPO
                      AND FP.DATAPAGTO >= :DATAINICIO
                      AND FP.DATAPAGTO <= :DATAFIM
                """

        if dt_ex_ini: query += " AND FP.DATAEX >= :DATAEXINI "
        if dt_ex_fim: query += " AND FP.DATAEX <= :DATAEXFIM "

        query += " GROUP BY FP.IDFUNDO "
        query += " ORDER BY F.RAZAOSOCIAL "

        params = {}
        params['IDUSUARIO'] = id_usuario
        params['TIPO'] = tipo
        params['DATAINICIO'] = dt_pagto_ini
        params['DATAFIM'] = dt_pagto_fim
        if dt_ex_ini: params['DATAEXINI'] = dt_ex_ini
        if dt_ex_fim: params['DATAEXFIM'] = dt_ex_fim
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_vlr_total(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(FP.TOTVLR), 0.00 ) AS TOTAL FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO AND FP.IDFUNDO = :IDFUNDO AND FP.SITUACAO = 'A' """
        if dt_fim: query += " AND FP.DATAPAGTO <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDFUNDO'] = id_fundo
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_vlr_total_periodo(cls, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(FP.TOTVLR), 0.00 ) AS TOTAL FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        if dt_ini: query += " AND FP.DATAPAGTO >= :DATAINICIO "
        if dt_fim: query += " AND FP.DATAPAGTO <= :DATAFIM "

        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDFUNDO'] = id_fundo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_vlr_total_periodo_ex(cls, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(FP.TOTVLR), 0.00 ) AS TOTAL
                    FROM TBFII_PROVENTO FP
                    WHERE FP.IDUSUARIO = :IDUSUARIO
                      AND FP.IDFUNDO   = :IDFUNDO
                      AND FP.DATAEX    >= :DATAINICIO
                      AND FP.DATAEX    <= :DATAFIM
                """
        params = {'IDUSUARIO': id_usuario, 'IDFUNDO': id_fundo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_vlr_preco(cls, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(FP.VLRPRECO), 0.00 ) AS VALOR
                    FROM TBFII_PROVENTO FP
                    WHERE FP.IDUSUARIO = :IDUSUARIO
                      AND FP.IDFUNDO   = :IDFUNDO
                      AND FP.DATAPAGTO >= :DATAINICIO
                      AND FP.DATAPAGTO <= :DATAFIM
                """
        params = {'IDUSUARIO': id_usuario, 'IDFUNDO': id_fundo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_vlr_preco_ex(cls, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(FP.VLRPRECO), 0.00 ) AS VALOR
                    FROM TBFII_PROVENTO FP
                    WHERE FP.IDUSUARIO = :IDUSUARIO
                      AND FP.IDFUNDO   = :IDFUNDO
                      AND FP.DATAEX    >= :DATAINICIO
                      AND FP.DATAEX    <= :DATAFIM
                """
        params = {'IDUSUARIO': id_usuario, 'IDFUNDO': id_fundo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    @asyncio.coroutine
    async def buscar_qtde_total_base(cls, id_usuario: int = None, tipo: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBFII_PROVENTO FP WHERE 1 = 1 """
        if tipo: query += " AND FP.TIPO = :TIPO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        try:
            rows = db.session.execute(query, params).first()
            return rows[0] if rows and rows[0] and rows[0] > 0 else 0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_qtd_operacao_usuario(cls, id_usuario: int = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        params = {'IDUSUARIO': id_usuario}
        try:
            rows = db.session.execute(query, params).first()
            return rows[0] if rows and rows[0] > 0 else 0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_menor_ano(cls, id_usuario: int = None, id_fundo: int = None):
        query = """ SELECT SUBSTRING(MIN(FP.DATAPAGTO), 1, 4) AS MENORANO FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_menor_ano_ex(cls, id_usuario: int = None, id_fundo: int = None):
        query = """ SELECT SUBSTRING(MIN(FP.DATAEX), 1, 4) AS MENORANO FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_maior_ano(cls, id_usuario: int = None, id_fundo: int = None):
        query = """ SELECT SUBSTRING(MAX(FP.DATAPAGTO), 1, 4) AS MAIORANO FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        try:
            rows = db.session.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_maior_ano_ex(cls, id_usuario: int = None, id_fundo: int = None):
        query = """ SELECT SUBSTRING(MAX(FP.DATAEX), 1, 4) AS MAIORANO FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        try:
            rows = db.session.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_maior_data(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT MAX(FP.DATAPAGTO) AS MAIORDATA FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        if dt_fim: query += " AND FP.DATAEX <= :DATAFIM   "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_maior_data_ex(cls, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT MAX(FP.DATAEX) AS MAIORDATA FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        if dt_fim: query += " AND FP.DATAEX <= :DATAFIM   "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBFII_PROVENTO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def salvar(self, commit: bool = True):
        try:
            db.session.add(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def excluir(self, commit: bool = True):
        try:
            db.session.delete(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def calc_total(self) -> float:
        return self.calcular_total(quantidade=self.quantidade, vlr_preco=self.vlr_preco)

    def data_ex_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_pagto_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%d/%m/%Y')
    def data_ex_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def data_pagto_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def quantidade_format(self) -> str:
        return inteiro_to_str(valor=self.quantidade)

    def vlr_preco_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco)

    def tot_vlr_format(self) -> str:
        return decimal_to_str(valor=self.tot_vlr)

    def tipo_descr(self) -> str:
        return self.descricao_tipo(tipo=self.tipo)

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def calcular_total(cls, quantidade: float, vlr_preco: float) -> float:
        return float(quantidade) * float(vlr_preco) if quantidade > 0.0 and vlr_preco > 0.0 else 0.0

    @classmethod
    def descricao_tipo(cls, tipo: str) -> str:
        if tipo == 'R':
            return 'RENDIMENTO'
        else:
            return 'Desconhecido'

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':
            return 'Ativo'
        elif situacao == 'B':
            return 'Pendente Aprovação/Confirmação'
        elif situacao == 'I':
            return 'Inativo'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioFiiFundoImobProvento {str(self.id)}>'
