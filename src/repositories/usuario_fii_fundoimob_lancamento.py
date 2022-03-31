# -*- coding: utf-8 -*-
import sys
import os
import asyncio
import sqlalchemy.orm as _orm
from src.models.xxxxxxxxxxx import xxxxxxxxxxxModel
# from app.models.log_erro import LogErro


class UsuarioFiiFundoImobLancamentoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None):
        try:

            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if id_fundo: filters.append(cls, db: _orm.id_fundo == id_fundo)
            if dt_ini: filters.append(cls, db: _orm.data >= dt_ini)
            if dt_fim: filters.append(cls, db: _orm.data <= dt_fim)
            if tipo: filters.append(cls, db: _orm.tipo == tipo)

            return cls.query.filter(*filters).order_by(cls, db: _orm.id).all()

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
    async def get_all_by_fundo(cls, db: _orm.Session, id_fundo: int):
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

            return db.query(db.func.min(cls, db: _orm.data)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if id_fundo: filters.append(cls, db: _orm.id_fundo == id_fundo)

            return db.query(db.func.max(cls, db: _orm.data)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None, ordem: str = None, id_corretora: str = None, troca: str = None):
        query = """ SELECT FL.ID, 
                           FL.IDUSUARIO, 
                           FL.IDFUNDO     AS IDFUNDO, 
                           F.NOME         AS NOMEFUNDO, 
                           F.CODIGO       AS CODIGOFUNDO, 
                           F.SITUACAO     AS SITUACAOFUNDO, 
                           FL.IDCORRETORA AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           FL.TIPO, 
                           FL.DATA, 
                           FL.QUANTORIG, 
                           FL.QUANT, 
                           FL.VLRPRECO, 
                           FL.TOTVLRPRECO, 
                           FL.VLRTXLIQUIDACAO, 
                           FL.VLRTXEMOLUMENTOS, 
                           FL.VLRTXCORRETAGEM, 
                           FL.VLRTXISS, 
                           FL.VLRTXIRRF, 
                           FL.VLRTXOUTRAS, 
                           FL.TOTVLRTX, 
                           FL.TOTVLR, 
                           FL.VLRCUSTO, 
                           FL.TOTVLRCUSTO, 
                           FL.VLRPRECOMEDIO, 
                           FL.TOTVLRVALORIZACAO, 
                           FL.PERCVALORIZACAO, 
                           FL.TROCA, 
                           FL.SITUACAO 
                    FROM TBFII_LANCAMENTO FL
                      INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
                    WHERE FL.IDUSUARIO = :IDUSUARIO
        """

        if codigo: query += " AND F.CODIGO = :CODIGO "
        if dt_ini: query += " AND FL.DATA >= :DATAINICIO "
        if dt_fim: query += " AND FL.DATA <= :DATAFIM "
        if tipo: query += " AND FL.TIPO = :TIPO "
        if id_corretora: query += " AND FL.IDCORRETORA = :IDCORRETORA "
        if troca: query += " AND IFNULL(FL.TROCA, 'N') = :TROCA "

        if ordem: query += " ORDER BY FL.DATA DESC, FL.ID, FL.TIPO "
        else: query += " ORDER BY FL.DATA, FL.ID, FL.TIPO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim
        if tipo: params['TIPO'] = tipo
        if id_corretora: params['IDCORRETORA'] = id_corretora
        if troca: params['TROCA'] = troca

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise


    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int = None, id: int = None):
        query = """ SELECT FL.ID, 
                           FL.IDUSUARIO, 
                           FL.IDFUNDO     AS IDFUNDO, 
                           F.NOME         AS NOMEFUNDO, 
                           F.CODIGO       AS CODIGOFUNDO, 
                           F.SITUACAO     AS SITUACAOFUNDO, 
                           FL.IDCORRETORA AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           FL.TIPO, 
                           FL.DATA, 
                           FL.QUANTORIG, 
                           FL.QUANT, 
                           FL.VLRPRECO, 
                           FL.TOTVLRPRECO, 
                           FL.VLRTXLIQUIDACAO, 
                           FL.VLRTXEMOLUMENTOS, 
                           FL.VLRTXCORRETAGEM, 
                           FL.VLRTXISS, 
                           FL.VLRTXIRRF, 
                           FL.VLRTXOUTRAS, 
                           FL.TOTVLRTX, 
                           FL.TOTVLR, 
                           FL.VLRCUSTO, 
                           FL.TOTVLRCUSTO, 
                           FL.VLRPRECOMEDIO, 
                           FL.TOTVLRVALORIZACAO, 
                           FL.PERCVALORIZACAO, 
                           FL.TROCA, 
                           FL.SITUACAO 
                    FROM TBFII_LANCAMENTO FL
                      INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
                    WHERE FL.ID        = :ID
                      AND FL.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT FL.ID, 
                           FL.IDUSUARIO, 
                           FL.IDFUNDO     AS IDFUNDO, 
                           F.NOME         AS NOMEFUNDO, 
                           F.CODIGO       AS CODIGOFUNDO, 
                           F.SITUACAO     AS SITUACAOFUNDO, 
                           FL.IDCORRETORA AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           FL.TIPO, 
                           FL.DATA, 
                           FL.QUANTORIG, 
                           FL.QUANT, 
                           FL.VLRPRECO, 
                           FL.TOTVLRPRECO, 
                           FL.VLRTXLIQUIDACAO, 
                           FL.VLRTXEMOLUMENTOS, 
                           FL.VLRTXCORRETAGEM, 
                           FL.VLRTXISS, 
                           FL.VLRTXIRRF, 
                           FL.VLRTXOUTRAS, 
                           FL.TOTVLRTX, 
                           FL.TOTVLR, 
                           FL.VLRCUSTO, 
                           FL.TOTVLRCUSTO, 
                           FL.VLRPRECOMEDIO, 
                           FL.TOTVLRVALORIZACAO, 
                           FL.PERCVALORIZACAO, 
                           FL.TROCA, 
                           FL.SITUACAO 
                    FROM TBFII_LANCAMENTO FL
                      INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
                    WHERE FL.IDUSUARIO = :IDUSUARIO
                      AND F.CODIGO     = :CODIGO
                    ORDER BY FL.DATA, FL.TIPO 
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_desdobro_grupamento(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT FL.ID, 
                           FL.IDUSUARIO, 
                           FL.IDFUNDO     AS IDFUNDO, 
                           F.NOME         AS NOMEFUNDO, 
                           F.CODIGO       AS CODIGOFUNDO, 
                           F.SITUACAO     AS SITUACAOFUNDO, 
                           FL.IDCORRETORA AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           FL.TIPO, 
                           FL.DATA, 
                           FL.QUANTORIG, 
                           FL.QUANT, 
                           FL.VLRPRECO, 
                           FL.TOTVLRPRECO, 
                           FL.VLRTXLIQUIDACAO, 
                           FL.VLRTXEMOLUMENTOS, 
                           FL.VLRTXCORRETAGEM, 
                           FL.VLRTXISS, 
                           FL.VLRTXIRRF, 
                           FL.VLRTXOUTRAS, 
                           FL.TOTVLRTX, 
                           FL.TOTVLR, 
                           FL.VLRCUSTO, 
                           FL.TOTVLRCUSTO, 
                           FL.VLRPRECOMEDIO, 
                           FL.TOTVLRVALORIZACAO, 
                           FL.PERCVALORIZACAO, 
                           FL.TROCA, 
                           FL.SITUACAO 
                    FROM TBFII_LANCAMENTO FL
                      INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
                    WHERE FL.IDUSUARIO = :IDUSUARIO
                      AND F.CODIGO     = :CODIGO
                      AND FL.TIPO      IN ('D', 'G')
                      AND FL.QUANT     > 0
                    ORDER BY FL.DATA, FL.TIPO, FL.ID
                    """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params).fetchall()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None):
        query = """ SELECT SUBSTRING(MIN(FL.DATA), 1, 4) AS MENORANO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += """ AND FL.IDFUNDO = :IDFUNDO """
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
        query = """ SELECT SUBSTRING(MAX(FL.DATA), 1, 4) AS MAIORANO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO """
        if id_fundo: query += """ AND FL.IDFUNDO = :IDFUNDO """
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_total_compra(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'C' """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
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
    async def buscar_total_bonus(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'B' """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
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
    async def buscar_total_venda(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'V' """
        if id_lanc: query += """ AND FL.ID <> :ID """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDFUNDO'] = id_fundo
        if id_lanc: params['ID'] = id_lanc
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_valor_total_compra(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'C' """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
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
    async def buscar_valor_total_bonus(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'B' """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
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
    async def buscar_valor_total_amortizacao(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'A' """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
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
    async def buscar_valor_total_venda(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDFUNDO = :IDFUNDO AND FL.TIPO = 'V' """
        if id_lanc: query += """ AND FL.ID <> :ID """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDFUNDO'] = id_fundo
        if id_lanc: params['ID'] = id_lanc
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_quant_operacao(cls, db: _orm.Session, id_usuario: int = None, situacao: str = None, tipo: str = None):
        try:

            query = " SELECT COUNT(1) AS QTDE FROM TBFII_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO "
            if situacao: query += " AND L.SITUACAO = :SITUACAO "
            if tipo: query += """ AND L.TIPO = :TIPO """

            params = {}
            params['IDUSUARIO'] = id_usuario
            if situacao: params['SITUACAO'] = situacao
            if tipo: params['TIPO'] = tipo

            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] and rows[0] > 0 else 0

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    @asyncio.coroutine
    async def buscar_qtde_total_base(cls, db: _orm.Session, tipo: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBFII_LANCAMENTO L WHERE 1 = 1 """
        if tipo: query += """ AND L.TIPO = :TIPO """
        params = {}
        if tipo: params['TIPO'] = tipo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] and rows[0] > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_quant_ativo(cls, db: _orm.Session, id_usuario: int = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBFII_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'A' """
        params = {'IDUSUARIO': id_usuario }
        try:
            rows = db.execute(query, params).first()
            return int(rows[0]) if rows and rows[0] and int(rows[0]) > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_preco_medio(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT FL.VLRPRECOMEDIO FROM TBFII_LANCAMENTO FL WHERE FL.ID = ( SELECT MAX(FLANT.ID) FROM TBFII_LANCAMENTO FLANT WHERE FLANT.IDUSUARIO = :IDUSUARIO AND FLANT.IDFUNDO = :IDFUNDO AND FLANT.SITUACAO = 'A' """
        if dt_fim: query += """ AND FLANT.DATA <= :DATAFIM """
        query += " ) "
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
    async def buscar_preco_medio_antes(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, dt_fim: str = None):
        query = """ SELECT FL.VLRPRECOMEDIO FROM TBFII_LANCAMENTO FL WHERE FL.ID = ( SELECT MAX(FLANT.ID) FROM TBFII_LANCAMENTO FLANT WHERE FLANT.IDUSUARIO = :IDUSUARIO AND FLANT.IDFUNDO = :IDFUNDO AND FLANT.SITUACAO = 'A' """
        if dt_fim: query += """ AND FLANT.DATA < :DATAFIM """
        query += " ) "
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
    async def buscar_dados_grid_irpf(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT MAX(F.CODIGO)      AS CODIGO,
                           MAX(F.CNPJ)        AS CNPJ,
                           MAX(F.RAZAOSOCIAL) AS RAZAOSOCIAL,
                           SUM(FL.TOTVLR)      AS TOTVLR
                    FROM TBFII_LANCAMENTO FL
                      INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = FL.IDFUNDO   )
                    WHERE FL.IDUSUARIO = :IDUSUARIO
                      AND FL.TIPO      = :TIPO
                      AND FL.DATA      >= :DATAINICIO
                      AND FL.DATA      <= :DATAFIM
                    GROUP BY FL.IDFUNDO
                    ORDER BY F.RAZAOSOCIAL
                """
        params = {'IDUSUARIO': id_usuario, 'TIPO': tipo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def atualizar_qtd_pend_situacao(cls, db: _orm.Session, id_usuario: int, id_lanc: int, situacao: str, commit: bool = True):
        try:
            query = "UPDATE TBFII_LANCAMENTO SET SITUACAO = :SITUACAO WHERE IDUSUARIO = :IDUSUARIO AND ID = :ID "
            params = {'IDUSUARIO': id_usuario, 'ID': id_lanc, 'SITUACAO': situacao}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def resetar_ativos(cls, db: _orm.Session, id_usuario: int, id_fundo: int, commit: bool = True):
        try:
            query = "UPDATE TBFII_LANCAMENTO SET QUANT = QUANTORIG, TOTVLRCUSTO = 0.00, VLRPRECOMEDIO = 0.00, TOTVLRVALORIZACAO = 0.00, PERCVALORIZACAO = 0.00, SITUACAO = 'P' WHERE IDFUNDO = :IDFUNDO AND IDUSUARIO = :IDUSUARIO "
            params = {'IDUSUARIO': id_usuario, 'IDFUNDO': id_fundo}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo_fundo(cls, db: _orm.Session, id_usuario: int, id_fundo: int, commit: bool = True):
        try:
            query = "DELETE FROM TBFII_LANCAMENTO WHERE IDFUNDO = :IDFUNDO AND IDUSUARIO = :IDUSUARIO"
            params = {'IDFUNDO': id_fundo, 'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBFII_LANCAMENTO WHERE IDUSUARIO = :IDUSUARIO"
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
