# -*- coding: utf-8 -*-
import sys
import os
import asyncio
import sqlalchemy.orm as _orm
from src.models.usuario_fii_fundoimob_provento import UsuarioFiiFundoImobProventoModel
# from app.models.log_erro import LogErro


class UsuarioFiiFundoImobProventoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_ativo(cls, db: _orm.Session, id_fundo: int):
        try:
            return cls.query.filter_by(id_fundo=id_fundo).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_usuario(cls, db: _orm.Session, id: int, id_usuario: int):
        try:
            return cls.query.filter_by(id=id, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if id_fundo: filters.append(cls, db: _orm.id_fundo == id_fundo)

            return db.query(db.func.min(cls, db: _orm.data_pagto)).filter(*filters).first()
            # return db.query(db.func.min(cls, db: _orm.data_pagto)).filter_by(id_usuario=id_usuario).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_menor_ano_ex(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if id_fundo: filters.append(cls, db: _orm.id_fundo == id_fundo)

            return db.query(db.func.min(cls, db: _orm.data_ex)).filter(*filters).first()
            # return db.query(db.func.min(cls, db: _orm.data_ex)).filter_by(id_usuario=id_usuario).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if id_fundo: filters.append(cls, db: _orm.id_fundo == id_fundo)

            return db.query(db.func.max(cls, db: _orm.data_pagto)).filter(*filters).first()
            # return db.query(db.func.max(cls, db: _orm.data_pagto)).filter_by(id_usuario=id_usuario).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_maior_ano_ex(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if id_fundo: filters.append(cls, db: _orm.id_fundo == id_fundo)

            return db.query(db.func.max(cls, db: _orm.data_ex)).filter(*filters).first()
            # return db.query(db.func.max(cls, db: _orm.data_ex)).filter_by(id_usuario=id_usuario).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None, id_corretora: str = None, situacao: str = None):

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
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int = None, id: int = None):
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
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
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
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid_irpf(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None, dt_ex_ini: str = None, dt_ex_fim: str = None, dt_pagto_ini: str = None, dt_pagto_fim: str = None):

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
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_total(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(FP.TOTVLR), 0.00 ) AS TOTAL FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO AND FP.IDFUNDO = :IDFUNDO AND FP.SITUACAO = 'A' """
        if dt_fim: query += " AND FP.DATAPAGTO <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDFUNDO'] = id_fundo
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_total_periodo(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None):
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
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_total_periodo_ex(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(FP.TOTVLR), 0.00 ) AS TOTAL
                    FROM TBFII_PROVENTO FP
                    WHERE FP.IDUSUARIO = :IDUSUARIO
                      AND FP.IDFUNDO   = :IDFUNDO
                      AND FP.DATAEX    >= :DATAINICIO
                      AND FP.DATAEX    <= :DATAFIM
                """
        params = {'IDUSUARIO': id_usuario, 'IDFUNDO': id_fundo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_preco(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(FP.VLRPRECO), 0.00 ) AS VALOR
                    FROM TBFII_PROVENTO FP
                    WHERE FP.IDUSUARIO = :IDUSUARIO
                      AND FP.IDFUNDO   = :IDFUNDO
                      AND FP.DATAPAGTO >= :DATAINICIO
                      AND FP.DATAPAGTO <= :DATAFIM
                """
        params = {'IDUSUARIO': id_usuario, 'IDFUNDO': id_fundo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_preco_ex(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(FP.VLRPRECO), 0.00 ) AS VALOR
                    FROM TBFII_PROVENTO FP
                    WHERE FP.IDUSUARIO = :IDUSUARIO
                      AND FP.IDFUNDO   = :IDFUNDO
                      AND FP.DATAEX    >= :DATAINICIO
                      AND FP.DATAEX    <= :DATAFIM
                """
        params = {'IDUSUARIO': id_usuario, 'IDFUNDO': id_fundo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    @asyncio.coroutine
    async def buscar_qtde_total_base(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBFII_PROVENTO FP WHERE 1 = 1 """
        if tipo: query += " AND FP.TIPO = :TIPO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] and rows[0] > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_qtd_operacao_usuario(cls, db: _orm.Session, id_usuario: int = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        params = {'IDUSUARIO': id_usuario}
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        query = """ SELECT SUBSTRING(MIN(FP.DATAPAGTO), 1, 4) AS MENORANO FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_menor_ano_ex(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        query = """ SELECT SUBSTRING(MIN(FP.DATAEX), 1, 4) AS MENORANO FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        query = """ SELECT SUBSTRING(MAX(FP.DATAPAGTO), 1, 4) AS MAIORANO FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_ano_ex(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        query = """ SELECT SUBSTRING(MAX(FP.DATAEX), 1, 4) AS MAIORANO FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_data(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT MAX(FP.DATAPAGTO) AS MAIORDATA FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        if dt_fim: query += " AND FP.DATAEX <= :DATAFIM   "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_data_ex(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT MAX(FP.DATAEX) AS MAIORDATA FROM TBFII_PROVENTO FP WHERE FP.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        if dt_fim: query += " AND FP.DATAEX <= :DATAFIM   "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBFII_PROVENTO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, commit: bool = True):
        try:
            db.add(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, commit: bool = True):
        try:
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
