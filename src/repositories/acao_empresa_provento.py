# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.acao_empresa_provento import ACAOEmpresaProventoModel
# from app.models.log_erro import LogErro


class ACAOEmpresaProventoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(ACAOEmpresaProventoModel).order_by(ACAOEmpresaProventoModel.id).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_empresa(cls, db: _orm.Session, id_empresa: int):
        try:
            return db.query(ACAOEmpresaProventoModel).filter_by(id_empresa=id_empresa).order_by(ACAOEmpresaProventoModel.id).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_codigo_isin(cls, db: _orm.Session, codigo_isin: str):
        try:
            return db.query(ACAOEmpresaProventoModel).filter_by(codigo_isin=codigo_isin).order_by(ACAOEmpresaProventoModel.data_ex).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_codigo_isin_empresa(cls, db: _orm.Session, id_empresa: int, codigo_isin: str):
        try:
            return db.query(ACAOEmpresaProventoModel).filter_by(id_empresa=id_empresa, codigo_isin=codigo_isin).order_by(ACAOEmpresaProventoModel.data_ex).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(ACAOEmpresaProventoModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_empr: int = None, codigo: str = None, tipo: str = None, dt_ex_ini: str = None, dt_ex_fim: str = None, dt_pagto_ini: str = None, dt_pagto_fim: str = None ):
        query = """ SELECT P.ID,
                        P.IDEMPRESA   AS IDEMPRESA,
                        E.NOME        AS NMEMPRESA,
                        E.RAZAOSOCIAL AS RZEMPRESA,
                        A.ID          AS IDATIVO,
                        A.CODIGO      AS CODATIVO,
                        P.TIPO,
                        P.CATEGORIA,
                        P.CODISIN,
                        P.DATAAPROV,
                        P.DATACOM,
                        P.DATAEX,
                        P.DATAPAGTO,
                        P.VLRPRECO,
                        P.SITUACAO
                    FROM TBEMPRESA_PROVENTO  P
                        JOIN TBEMPRESA       E ON ( E.ID = P.IDEMPRESA )
                        JOIN TBEMPRESA_ATIVO A ON ( A.IDEMPRESA = P.IDEMPRESA AND A.CODISIN = P.CODISIN  )
                    WHERE P.SITUACAO = 'A'
                """

        if id_empr: query += " AND P.IDEMPRESA = :IDEMPRESA "
        if codigo: query += " AND A.CODIGO = :CODIGO "
        if tipo: query += " AND P.TIPO = :TIPO "
        if dt_ex_ini: query += " AND P.DATAEX >= :DATAEXINI "
        if dt_ex_fim: query += " AND P.DATAEX <= :DATAEXFIM "
        if dt_pagto_ini: query += " AND P.DATAPAGTO >= :DATAPAGTOINI "
        if dt_pagto_fim: query += " AND P.DATAPAGTO <= :DATAPAGTOFIM "

        if dt_ex_ini and dt_ex_fim: query += " ORDER BY P.DATAEX "
        elif dt_pagto_ini and dt_pagto_fim: query += " ORDER BY P.DATAPAGTO "
        else: query += " ORDER BY P.DATAEX DESC "

        params = {}
        if id_empr: params['IDEMPRESA'] = id_empr
        if codigo: params['CODIGO'] = codigo
        if tipo: params['TIPO'] = tipo
        if dt_ex_ini: params['DATAEXINI'] = dt_ex_ini
        if dt_ex_fim: params['DATAEXFIM'] = dt_ex_fim
        if dt_pagto_ini: params['DATAPAGTOINI'] = dt_pagto_ini
        if dt_pagto_fim: params['DATAPAGTOFIM'] = dt_pagto_fim

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int = None):
        query = """ SELECT P.ID,
                            P.IDEMPRESA   AS IDEMPRESA,
                            E.NOME        AS NMEMPRESA,
                            E.RAZAOSOCIAL AS RZEMPRESA,
                            A.ID          AS IDATIVO,
                            A.CODIGO      AS CODATIVO,
                            P.TIPO,
                            P.CATEGORIA,
                            P.CODISIN,
                            P.DATAAPROV,
                            P.DATACOM,
                            P.DATAEX,
                            P.DATAPAGTO,
                            P.VLRPRECO,
                            P.SITUACAO
                    FROM TBEMPRESA_PROVENTO P
                    JOIN TBEMPRESA          E ON ( E.ID = P.IDEMPRESA )
                    JOIN TBEMPRESA_ATIVO    A ON ( A.IDEMPRESA = P.IDEMPRESA AND A.CODISIN = P.CODISIN  )
                    WHERE P.ID  = :ID 
                """
        params = {'ID': id}

        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_usuario(cls, db: _orm.Session, id_usuario: int = None, id_empresa: int = None, codigo: str = None, tipo: str = None, dt_ex: str = None, dt_pagto: str = None):

        query = """ SELECT 	P.ID,
                            P.IDEMPRESA   AS IDEMPRESA,
                            E.NOME        AS NMEMPRESA,
                            E.RAZAOSOCIAL AS RZEMPRESA,
                            A.ID          AS IDATIVO,
                            A.CODIGO      AS CODATIVO,
                            P.TIPO,
                            P.CATEGORIA,
                            P.CODISIN,
                            P.DATAAPROV,
                            P.DATACOM,
                            P.DATAEX,
                            P.DATAPAGTO,
                            P.VLRPRECO,
                            P.SITUACAO
                    FROM TBEMPRESA_PROVENTO  P
                        JOIN TBEMPRESA       E ON ( E.ID = P.IDEMPRESA )
                        JOIN TBEMPRESA_ATIVO A ON ( A.IDEMPRESA = P.IDEMPRESA AND A.CODISIN = P.CODISIN  )
                    WHERE P.SITUACAO = 'A'
                """

        if id_empresa: query += " AND P.IDEMPRESA = :IDEMPRESA "
        if codigo: query += " AND A.CODIGO = :CODIGO "
        if tipo: query += " AND P.TIPO = :TIPO "

        if dt_ex and dt_pagto: query += " AND ( P.DATAEX >= :DATAEX OR P.DATAPAGTO >= :DATAPAGTO ) "
        elif dt_ex: query += " AND P.DATAEX >= :DATAEX "
        elif dt_pagto: query += " AND P.DATAPAGTO >= :DATAPAGTO "
        query += """ AND ( SELECT 1 FROM TBCARTEIRA_ATIVO CA JOIN TBCARTEIRA C ON ( C.ID = CA.IDCARTEIRA ) WHERE CA.IDATIVO  = A.ID AND C.IDUSUARIO = :IDUSUARIO AND CA.SITUACAO = 'A') AND NOT EXISTS( SELECT 1 FROM TBEMPRESA_PROVENTO_ATIVO PRVA WHERE PRVA.IDEMPRPROV = P.ID AND PRVA.IDUSUARIO = :IDUSUARIO_PROVATIVO ) """
        query += " ORDER BY P.DATAEX DESC, P.DATAPAGTO DESC "

        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDUSUARIO_PROVATIVO'] = id_usuario
        if id_empresa: params['IDEMPRESA'] = id_empresa
        if codigo: params['CODIGO'] = codigo
        if tipo: params['TIPO'] = tipo
        if dt_ex: params['DATAEX'] = dt_ex
        if dt_pagto: params['DATAPAGTO'] = dt_pagto

        try:
            try:
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar__dados_tab_finan(cls, db: _orm.Session, id_empresa: int = None, codigo_isin: str = None, is_data_pagto: bool = False):

        query = """   SELECT TRIM(P.DATAEX) AS DATA, SUM(IFNULL(P.VLRPRECO,0.0)) AS VLRPRECO
                      FROM TBEMPRESA_PROVENTO P
                      WHERE P.IDEMPRESA = :IDEMPRESA
                        AND P.CODISIN   = :CODISIN
                        AND P.TIPO     IN ('J','D')
                        AND P.DATAEX   <> ''
                        AND P.DATAEX   <> '99991231'
                      GROUP BY P.DATAEX
                      ORDER BY P.DATAEX
                """
        if is_data_pagto:
            query = """   SELECT TRIM(P.DATAPAGTO) AS DATA, SUM(IFNULL(P.VLRPRECO,0.0)) AS VLRPRECO
                          FROM TBEMPRESA_PROVENTO P
                          WHERE P.IDEMPRESA = :IDEMPRESA
                            AND P.CODISIN   = :CODISIN
                            AND P.TIPO     IN ('J','D')
                            AND P.DATAPAGTO   <> ''
                            AND P.DATAPAGTO   <> '99991231'
                          GROUP BY P.DATAPAGTO
                          ORDER BY P.DATAPAGTO
                    """

        params = {'IDEMPRESA': id_empresa, 'CODISIN': codigo_isin}

        try:
            try:
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: ACAOEmpresaProventoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: ACAOEmpresaProventoModel, commit: bool = True):
        try:
            params = {'IDEMPRPROV': row.id}
            db.execute("DELETE FROM TBEMPRESA_PROVENTO_ATIVO WHERE IDEMPRPROV = :IDEMPRPROV", params)
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
