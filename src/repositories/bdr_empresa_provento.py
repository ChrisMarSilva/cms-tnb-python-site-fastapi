# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.bdr_empresa_provento import BDREmpresaProventoModel
# from app.models.log_erro import LogErro


class BDREmpresaProventoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.order_by(cls, db: _orm.id).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_empresa(cls, db: _orm.Session, id_bdr: int):
        try:
            return cls.query.filter_by(id_bdr=id_bdr).order_by(cls, db: _orm.id).all()
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
    async def buscar_todos(cls, db: _orm.Session, id_empr: int = None, codigo: str = None, tipo: str = None, dt_ex_ini: str = None, dt_ex_fim: str = None, dt_pagto_ini: str = None, dt_pagto_fim: str = None ):
        query = """ SELECT P.ID,
                        P.IDBDR       AS IDBDR,
                        E.NOME        AS NMEMPRESA,
                        E.RAZAOSOCIAL AS RZEMPRESA,
                        E.ID          AS IDBDR,
                        E.CODIGO      AS CODIGOBDR,
                        P.TIPO,
                        P.CATEGORIA,
                        P.CODISIN,
                        P.DATAAPROV,
                        P.DATACOM,
                        P.DATAEX,
                        P.DATAPAGTO,
                        P.VLRPRECO,
                        P.SITUACAO
                    FROM TBBDR_EMPRESA_PROVENTO  P
                        JOIN TBBDR_EMPRESA  E ON ( E.ID = P.IDBDR AND E.CODISIN = P.CODISIN  )
                    WHERE P.SITUACAO = 'A'
                """

        if id_empr: query += " AND P.IDBDR = :IDBDR "
        if codigo: query += " AND E.CODIGO = :CODIGO "
        if tipo: query += " AND P.TIPO = :TIPO "
        if dt_ex_ini: query += " AND P.DATAEX >= :DATAEXINI "
        if dt_ex_fim: query += " AND P.DATAEX <= :DATAEXFIM "
        if dt_pagto_ini: query += " AND P.DATAPAGTO >= :DATAPAGTOINI "
        if dt_pagto_fim: query += " AND P.DATAPAGTO <= :DATAPAGTOFIM "

        if dt_ex_ini and dt_ex_fim: query += " ORDER BY P.DATAEX "
        elif dt_pagto_ini and dt_pagto_fim: query += " ORDER BY P.DATAPAGTO "
        else: query += " ORDER BY P.DATAEX DESC "

        params = {}
        if id_empr: params['IDBDR'] = id_empr
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
                            P.IDBDR       AS IDBDR,
                            E.NOME        AS NMEMPRESA,
                            E.RAZAOSOCIAL AS RZEMPRESA,
                            E.ID          AS IDBDR,
                            E.CODIGO      AS CODIGOBDR,
                            P.TIPO,
                            P.CATEGORIA,
                            P.CODISIN,
                            P.DATAAPROV,
                            P.DATACOM,
                            P.DATAEX,
                            P.DATAPAGTO,
                            P.VLRPRECO,
                            P.SITUACAO
                    FROM TBBDR_EMPRESA_PROVENTO P
                    JOIN TBBDR_EMPRESA E ON ( E.ID = P.IDBDR AND E.CODISIN = P.CODISIN  )
                    WHERE P.ID = :ID 
                """
        params = {'ID': id}

        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_usuario(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, codigo: str = None, tipo: str = None, dt_ex: str = None, dt_pagto: str = None):

        query = """ SELECT  P.ID,
                            P.IDBDR   AS IDBDR,
                            E.NOME        AS NMEMPRESA,
                            E.RAZAOSOCIAL AS RZEMPRESA,
                            E.ID          AS IDBDR,
                            E.CODIGO      AS CODIGOBDR,
                            P.TIPO,
                            P.CATEGORIA,
                            P.CODISIN,
                            P.DATAAPROV,
                            P.DATACOM,
                            P.DATAEX,
                            P.DATAPAGTO,
                            P.VLRPRECO,
                            P.SITUACAO
                    FROM TBBDR_EMPRESA_PROVENTO  P
                        JOIN TBBDR_EMPRESA E ON ( E.ID = P.IDBDR AND E.CODISIN = P.CODISIN  )
                    WHERE P.SITUACAO = 'A'
                """

        if id_bdr: query += " AND P.IDBDR = :IDBDR "
        if codigo: query += " AND E.CODIGO = :CODIGO "
        if tipo: query += " AND P.TIPO = :TIPO "

        if dt_ex and dt_pagto: query += " AND ( P.DATAEX >= :DATAEX OR P.DATAPAGTO >= :DATAPAGTO ) "
        elif dt_ex: query += " AND P.DATAEX >= :DATAEX "
        elif dt_pagto: query += " AND P.DATAPAGTO >= :DATAPAGTO "
        query += """ AND ( SELECT 1 FROM TBCARTEIRA_BDR CA JOIN TBCARTEIRA C ON ( C.ID = CA.IDCARTEIRA ) WHERE CA.IDBDR = E.ID AND C.IDUSUARIO = :IDUSUARIO AND CA.SITUACAO = 'A') 
                     AND NOT EXISTS( SELECT 1 FROM TBBDR_EMPRESA_PROVENTO_ATIVO PRVA WHERE PRVA.IDBDRPROV = P.ID AND PRVA.IDUSUARIO = :IDUSUARIO_PROVATIVO ) """
        query += " ORDER BY P.DATAEX DESC, P.DATAPAGTO DESC "

        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDUSUARIO_PROVATIVO'] = id_usuario
        if id_bdr: params['IDBDR'] = id_bdr
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
            params = {'IDBDRPROV': self.id}
            db.execute("DELETE FROM TBBDR_EMPRESA_PROVENTO_ATIVO WHERE IDBDRPROV = :IDBDRPROV", params)
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
