# -*- coding: utf-8 -*-
import sys
import os
import asyncio
import sqlalchemy.orm as _orm
from src.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamentoModel
# from app.models.log_erro import LogErro


class UsuarioETFIndiceLancamentoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioETFIndiceLancamentoModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(UsuarioETFIndiceLancamentoModel).filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_indice(cls, db: _orm.Session, id_indice: int):
        try:
            return db.query(UsuarioETFIndiceLancamentoModel).filter_by(id_indice=id_indice).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioETFIndiceLancamentoModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_usuario(cls, db: _orm.Session, id: int, id_usuario: int):
        try:
            return db.query(UsuarioETFIndiceLancamentoModel).filter_by(id=id, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_indice: int = None):
        try:

            filters = []
            if id_usuario: filters.append(UsuarioETFIndiceLancamentoModel.id_usuario == id_usuario)
            if id_indice: filters.append(UsuarioETFIndiceLancamentoModel.id_indice == id_indice)

            return db.query(db.func.min(UsuarioETFIndiceLancamentoModel.data)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_indice: int = None):
        try:

            filters = []
            if id_usuario: filters.append(UsuarioETFIndiceLancamentoModel.id_usuario == id_usuario)
            if id_indice: filters.append(UsuarioETFIndiceLancamentoModel.id_indice == id_indice)

            return db.query(db.func.max(UsuarioETFIndiceLancamentoModel.data)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None, ordem: str = None, id_corretora: str = None, troca: str = None):
        query = """ SELECT O.ID, 
                           O.IDUSUARIO, 
                           O.IDINDICE     AS IDINDICE, 
                           A.CODIGO       AS CODIGOINDICE, 
                           A.SITUACAO     AS SITUACAOINDICE, 
                           O.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           O.TIPO, 
                           O.DATA, 
                           O.QUANT, 
                           O.QUANTPEND, 
                           O.VLRPRECO, 
                           O.TOTVLRPRECO, 
                           O.VLRTXLIQUIDACAO, 
                           O.VLRTXEMOLUMENTOS, 
                           O.VLRTXCORRETAGEM, 
                           O.VLRTXISS, 
                           O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, 
                           O.TOTVLRTX, 
                           O.TOTVLR, 
                           O.VLRCUSTO, 
                           ( SELECT MAX(OP.VLRPRECOMEDIO)     FROM TBETF_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDINDICE = O.IDINDICE AND OP.IDLANC = O.ID ) AS VLRPRECOMEDIO, 
                           ( SELECT SUM(OP.TOTVLRVALORIZACAO) FROM TBETF_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDINDICE = O.IDINDICE AND OP.IDLANC = O.ID ) AS TOTVLRVALORIZACAO, 
                           ( SELECT SUM(OP.PERCVALORIZACAO)   FROM TBETF_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDINDICE = O.IDINDICE AND OP.IDLANC = O.ID ) AS PERCVALORIZACAO, 
                           O.TROCA, 
                           O.SITUACAO 
                    FROM TBETF_LANCAMENTO        O
                      INNER JOIN TBETF_INDICE    A ON ( A.ID = O.IDINDICE    )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
        """

        if codigo: query += " AND A.CODIGO = :CODIGO "
        if dt_ini: query += " AND O.DATA >= :DATAINICIO "
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        if tipo: query += " AND O.TIPO = :TIPO "
        if id_corretora: query += " AND O.IDCORRETORA = :IDCORRETORA "
        if troca: query += " AND IFNULL(O.TROCA, 'N') = :TROCA "

        if ordem: query += " ORDER BY O.DATA DESC, O.TIPO, O.ID "
        else: query += " ORDER BY O.DATA, O.TIPO, O.ID "

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
    async def buscar_por_data(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, data: str = None, tipo: str = None):
        query = """ SELECT O.ID, 
                           O.IDUSUARIO, 
                           O.IDINDICE     AS IDINDICE, 
                           A.CODIGO       AS CODIGOINDICE, 
                           A.SITUACAO     AS SITUACAOINDICE, 
                           O.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           O.TIPO, 
                           O.DATA, 
                           O.QUANT, 
                           O.QUANTPEND, 
                           O.VLRPRECO, 
                           O.TOTVLRPRECO, 
                           O.VLRTXLIQUIDACAO, 
                           O.VLRTXEMOLUMENTOS, 
                           O.VLRTXCORRETAGEM, 
                           O.VLRTXISS, 
                           O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, 
                           O.TOTVLRTX, 
                           O.TOTVLR, 
                           O.VLRCUSTO, 
                           ( SELECT MAX(OP.VLRPRECOMEDIO)     FROM TBETF_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDINDICE = O.IDINDICE AND OP.IDLANC = O.ID ) AS VLRPRECOMEDIO, 
                           ( SELECT SUM(OP.TOTVLRVALORIZACAO) FROM TBETF_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDINDICE = O.IDINDICE AND OP.IDLANC = O.ID ) AS TOTVLRVALORIZACAO, 
                           ( SELECT SUM(OP.PERCVALORIZACAO)   FROM TBETF_OPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDINDICE = O.IDINDICE AND OP.IDLANC = O.ID ) AS PERCVALORIZACAO, 
                           O.TROCA, 
                           O.SITUACAO 
                    FROM TBETF_LANCAMENTO        O
                      INNER JOIN TBETF_INDICE    A ON ( A.ID = O.IDINDICE    )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
                      AND O.QUANTPEND > 0
                """

        if codigo: query += " AND A.CODIGO = :CODIGO "
        if data: query += " AND O.DATA = :DATA"
        if tipo: query += " AND O.TIPO = :TIPO "

        query += " ORDER BY O.ID "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        if data: params['DATA'] = data
        if tipo: params['TIPO'] = tipo
        try:
            return db.execute(query, params).fetchall()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int = None, id: int = None):
        query = """ SELECT O.ID, 
                           O.IDUSUARIO, 
                           O.IDINDICE     AS IDINDICE, 
                           A.CODIGO       AS CODIGOINDICE, 
                           A.SITUACAO     AS SITUACAOINDICE, 
                           O.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           O.TIPO, 
                           O.DATA, 
                           O.QUANT, 
                           O.QUANTPEND, 
                           O.VLRPRECO, 
                           O.TOTVLRPRECO, 
                           O.VLRTXLIQUIDACAO, 
                           O.VLRTXEMOLUMENTOS, 
                           O.VLRTXCORRETAGEM, 
                           O.VLRTXISS, 
                           O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, 
                           O.TOTVLRTX, 
                           O.TOTVLR, 
                           O.VLRCUSTO, 
                           0.00 AS VLRPRECOMEDIO, 
                           0.00 AS TOTVLRVALORIZACAO, 
                           0.00 AS PERCVALORIZACAO, 
                           O.TROCA, 
                           O.SITUACAO 
                    FROM TBETF_LANCAMENTO        O
                      INNER JOIN TBETF_INDICE    A ON ( A.ID = O.IDINDICE    )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.ID        = :ID
                      AND O.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT O.ID, 
                           O.IDUSUARIO, 
                           O.IDINDICE     AS IDINDICE, 
                           A.CODIGO       AS CODIGOINDICE, 
                           A.SITUACAO     AS SITUACAOINDICE, 
                           O.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           O.TIPO, 
                           O.DATA, 
                           O.QUANT, 
                           O.QUANTPEND, 
                           O.VLRPRECO, 
                           O.TOTVLRPRECO, 
                           O.VLRTXLIQUIDACAO, 
                           O.VLRTXEMOLUMENTOS, 
                           O.VLRTXCORRETAGEM, 
                           O.VLRTXISS, 
                           O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, 
                           O.TOTVLRTX, 
                           O.TOTVLR, 
                           O.VLRCUSTO, 
                           0.00 AS VLRPRECOMEDIO, 
                           0.00 AS TOTVLRVALORIZACAO, 
                           0.00 AS PERCVALORIZACAO, 
                           O.TROCA, 
                           O.SITUACAO 
                    FROM TBETF_LANCAMENTO        O
                      INNER JOIN TBETF_INDICE    A ON ( A.ID = O.IDINDICE    )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
                      AND A.CODIGO    = :CODIGO
                    ORDER BY O.DATA, O.ID, O.TIPO 
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_day_trade(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, tipo: str = None):
        query = ''
        if tipo == 'C' or tipo == 'B':
            query = """ SELECT OC.ID, 
                               OC.IDUSUARIO, 
                               OC.IDINDICE    AS IDINDICE, 
                               AC.CODIGO      AS CODIGOINDICE, 
                               AC.SITUACAO    AS SITUACAOINDICE, 
                               OC.IDCORRETORA AS IDCORRETORA, 
                               C.NOME         AS NOMECORRETORA, 
                               OC.TIPO, 
                               OC.DATA, 
                               OC.QUANT, 
                               OC.QUANTPEND, 
                               OC.VLRPRECO, 
                               OC.TOTVLRPRECO, 
                               OC.VLRTXLIQUIDACAO, 
                               OC.VLRTXEMOLUMENTOS, 
                               OC.VLRTXCORRETAGEM, 
                               OC.VLRTXISS, 
                               OC.VLRTXIRRF, 
                               OC.VLRTXOUTRAS, 
                               OC.TOTVLRTX, 
                               OC.TOTVLR, 
                               OC.VLRCUSTO, 
                               0.00 AS VLRPRECOMEDIO, 
                               0.00 AS TOTVLRVALORIZACAO, 
                               0.00 AS PERCVALORIZACAO, 
                               OC.TROCA, 
                               OC.SITUACAO 
                        FROM TBETF_LANCAMENTO        OC
                          INNER JOIN TBETF_INDICE    AC ON ( AC.ID = OC.IDINDICE    )	
                          LEFT  JOIN TBCORRETORA     C  ON ( C.ID  = OC.IDCORRETORA )
                        WHERE OC.IDUSUARIO = :IDUSUARIO
                          AND AC.CODIGO    = :CODIGO
                          AND OC.TIPO      IN ('C', 'B')
                          AND EXISTS( SELECT 1
                                      FROM TBETF_LANCAMENTO OV
                                      WHERE OV.IDUSUARIO = OC.IDUSUARIO
                                        AND OV.IDINDICE  = OC.IDINDICE
                                        AND OV.TIPO      = 'V'
                                        AND OV.DATA      = OC.DATA
                                    ) 
                        ORDER BY OC.DATA, OC.ID
                    """
        if tipo == 'V':
            query = """ SELECT OV.ID, 
                               OV.IDUSUARIO, 
                               OV.IDINDICE     AS IDINDICE, 
                               AV.CODIGO       AS CODIGOINDICE, 
                               AV.SITUACAO     AS SITUACAOINDICE, 
                               OV.IDCORRETORA  AS IDCORRETORA, 
                               C.NOME          AS NOMECORRETORA, 
                               OV.TIPO, 
                               OV.DATA, 
                               OV.QUANT, 
                               OV.QUANTPEND, 
                               OV.VLRPRECO, 
                               OV.TOTVLRPRECO, 
                               OV.VLRTXLIQUIDACAO, 
                               OV.VLRTXEMOLUMENTOS, 
                               OV.VLRTXCORRETAGEM, 
                               OV.VLRTXISS, 
                               OV.VLRTXIRRF, 
                               OV.VLRTXOUTRAS, 
                               OV.TOTVLRTX, 
                               OV.TOTVLR, 
                               OV.VLRCUSTO, 
                               0.00 AS VLRPRECOMEDIO, 
                               0.00 AS TOTVLRVALORIZACAO, 
                               0.00 AS PERCVALORIZACAO, 
                               OV.TROCA, 
                               OV.SITUACAO 
                        FROM TBETF_LANCAMENTO        OV
                          INNER JOIN TBETF_INDICE    AV ON ( AV.ID = OV.IDINDICE     )	
                          LEFT  JOIN TBCORRETORA     C  ON ( C.ID  = OV.IDCORRETORA )
                        WHERE OV.IDUSUARIO = :IDUSUARIO
                          AND AV.CODIGO    = :CODIGO
                          AND OV.TIPO      = 'V'
                          AND EXISTS( SELECT 1
                                      FROM TBETF_LANCAMENTO OC
                                      WHERE OC.IDUSUARIO = OV.IDUSUARIO
                                        AND OC.IDINDICE  = OV.IDINDICE
                                        AND OC.TIPO      IN ('C', 'B')
                                        AND OC.DATA      = OV.DATA
                                        AND OC.ID        < OV.ID
                                    )  
                        ORDER BY OV.DATA, OV.ID DESC
                    """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_qtde_pend_maior_que_zero(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT O.ID, 
                           O.IDUSUARIO, 
                           O.IDINDICE     AS IDINDICE, 
                           A.CODIGO       AS CODIGOINDICE, 
                           A.SITUACAO     AS SITUACAOINDICE, 
                           O.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           O.TIPO, 
                           O.DATA, 
                           O.QUANT, 
                           O.QUANTPEND, 
                           O.VLRPRECO, 
                           O.TOTVLRPRECO, 
                           O.VLRTXLIQUIDACAO, 
                           O.VLRTXEMOLUMENTOS, 
                           O.VLRTXCORRETAGEM, 
                           O.VLRTXISS, 
                           O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, 
                           O.TOTVLRTX, 
                           O.TOTVLR, 
                           O.VLRCUSTO, 
                           0.00 AS VLRPRECOMEDIO, 
                           0.00 AS TOTVLRVALORIZACAO, 
                           0.00 AS PERCVALORIZACAO, 
                           O.TROCA, 
                           O.SITUACAO 
                    FROM TBETF_LANCAMENTO        O
                      INNER JOIN TBETF_INDICE    A ON ( A.ID = O.IDINDICE    )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
                      AND A.CODIGO    = :CODIGO
                      AND O.QUANTPEND > 0
                      AND O.TIPO      IN ('C', 'V', 'B')
                    ORDER BY DATA, TIPO, ID
                    """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params).fetchall()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_desdobro_grupamento(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT O.ID, 
                           O.IDUSUARIO, 
                           O.IDINDICE     AS IDINDICE, 
                           A.CODIGO       AS CODIGOINDICE, 
                           A.SITUACAO     AS SITUACAOINDICE, 
                           O.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           O.TIPO, 
                           O.DATA, 
                           O.QUANT, 
                           O.QUANTPEND, 
                           O.VLRPRECO, 
                           O.TOTVLRPRECO, 
                           O.VLRTXLIQUIDACAO, 
                           O.VLRTXEMOLUMENTOS, 
                           O.VLRTXCORRETAGEM, 
                           O.VLRTXISS, 
                           O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, 
                           O.TOTVLRTX, 
                           O.TOTVLR, 
                           O.VLRCUSTO, 
                           0.00 AS VLRPRECOMEDIO, 
                           0.00 AS TOTVLRVALORIZACAO, 
                           0.00 AS PERCVALORIZACAO, 
                           O.TROCA, 
                           O.SITUACAO 
                    FROM TBETF_LANCAMENTO        O
                      INNER JOIN TBETF_INDICE    A ON ( A.ID = O.IDINDICE    )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
                      AND A.CODIGO    = :CODIGO
                      AND O.TIPO      IN ('D', 'G')
                      AND O.QUANT     > 0
                    ORDER BY DATA, TIPO, ID
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params).fetchall()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_indice: int = None):
        query = """ SELECT SUBSTRING(MIN(L.DATA), 1, 4) AS MENORANO FROM TBETF_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO """
        if id_indice: query += """ AND L.IDINDICE = :IDINDICE """
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_indice: params['IDINDICE'] = id_indice
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_indice: int = None):
        query = """ SELECT SUBSTRING(MAX(L.DATA), 1, 4) AS MAIORANO FROM TBETF_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO """
        if id_indice: query += """ AND L.IDINDICE = :IDINDICE """
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_indice: params['IDINDICE'] = id_indice
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_total_compra(cls, db: _orm.Session, id_usuario: int = None, id_indice: int = None, dt_fim: str = None):
        query = """ SELECT SUM(L.QUANT) AS QTDE FROM TBETF_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO AND L.IDINDICE = :IDINDICE AND L.TIPO IN ( 'C', 'B') """
        if dt_fim: query += """ AND L.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_total_venda(cls, db: _orm.Session, id_usuario: int = None, id_indice: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(L.QUANT) AS QTDE FROM TBETF_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO AND L.IDINDICE = :IDINDICE AND L.TIPO = 'V' """
        if id_lanc: query += """ AND L.ID <> :ID """
        if dt_fim: query += """ AND L.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if dt_fim: params['ID'] = id_lanc
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

            query = " SELECT COUNT(1) AS QTDE FROM TBETF_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO "
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
        query = """ SELECT COUNT(1) AS QTDE FROM TBETF_LANCAMENTO L WHERE 1 = 1 """
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
    async def buscar_dados_grid_irpf(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT MAX(E.CODIGO)      AS CODIGO,
                           MAX(E.CNPJ)        AS CNPJ,
                           MAX(E.RAZAOSOCIAL) AS RAZAOSOCIAL,
                           SUM(L.TOTVLR)      AS TOTVLR
                    FROM TBETF_LANCAMENTO     L
                      INNER JOIN TBETF_INDICE E ON ( E.ID = L.IDINDICE )
                    WHERE L.IDUSUARIO  = :IDUSUARIO
                      AND L.TIPO       = :TIPO
                      AND L.DATA      >= :DATAINICIO
                      AND L.DATA      <= :DATAFIM
                    GROUP BY L.IDINDICE
                    ORDER BY E.RAZAOSOCIAL
                """
        params = {'IDUSUARIO': id_usuario, 'TIPO': tipo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_datas_day_trade(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT DISTINCT LV.DATA
                    FROM TBETF_LANCAMENTO     LV
                      INNER JOIN TBETF_INDICE A  ON ( A.ID = LV.IDINDICE )
                    WHERE LV.IDUSUARIO = :IDUSUARIO
                      AND A.CODIGO     = :CODIGO
                      AND LV.TIPO      = 'V'
                      AND EXISTS( SELECT 1
                                  FROM TBETF_LANCAMENTO LC
                                  WHERE LC.IDUSUARIO = LV.IDUSUARIO
                                    AND LC.IDINDICE  = LV.IDINDICE
                                    AND LC.TIPO      IN ('C', 'B')
                                    AND LC.DATA      = LV.DATA
                                    AND LC.ID        < LV.ID
                                )
                    ORDER BY LV.DATA
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def atualizar_qtd_pend_situacao(cls, db: _orm.Session, id_usuario: int, id_lanc: int, qtd_pend: int, situacao: str, commit: bool = True):
        try:
            query = "UPDATE TBETF_LANCAMENTO SET QUANTPEND = :QUANTPEND, SITUACAO = :SITUACAO WHERE IDUSUARIO = :IDUSUARIO AND ID = :ID "
            params = {'IDUSUARIO': id_usuario, 'ID': id_lanc, 'QUANTPEND': qtd_pend, 'SITUACAO': situacao}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def resetar_ativos(cls, db: _orm.Session, id_usuario: int, id_indice: int, commit: bool = True):
        try:
            query = "UPDATE TBETF_LANCAMENTO SET QUANTPEND = QUANT, SITUACAO = 'P' WHERE IDINDICE = :IDINDICE AND IDUSUARIO = :IDUSUARIO "
            params = {'IDUSUARIO': id_usuario, 'IDINDICE': id_indice}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBETF_LANCAMENTO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioETFIndiceLancamentoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioETFIndiceLancamentoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
