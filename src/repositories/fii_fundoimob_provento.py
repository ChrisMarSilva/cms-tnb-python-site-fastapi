# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.fii_fundoimob_provento import FiiFundoImobProventoModel
# from app.models.log_erro import LogErro


class FiiFundoImobProventoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.order_by(cls, db: _orm.id).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_fundo(cls, db: _orm.Session, id_fundo: int):
        try:
            return cls.query.filter_by(id_fundo=id_fundo).order_by(cls, db: _orm.id).all()
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
    async def buscar_todos(cls, db: _orm.Session, id_fundo: int = None, codigo: str = None, tipo: str = None, dt_ex_ini: str = None, dt_ex_fim: str = None, dt_pagto_ini: str = None, dt_pagto_fim: str = None ):

        query = """ SELECT FP.ID,
                           FP.IDFUNDO  AS IDFUNDO, 
                           F.NOME      AS NOMEFUNDO, 
                           F.CODIGO    AS CODIGOFUNDO, 
                           F.SITUACAO  AS SITUACAOFUNDO, 
                           FP.TIPO,
                           FP.CATEGORIA,
                           FP.CODISIN,
                           FP.DATAAPROV,
                           FP.DATACOM,
                           FP.DATAEX,
                           FP.DATAPAGTO,
                           FP.VLRPRECO,
                           FP.SITUACAO
                    FROM TBFII_FUNDOIMOB_PROVENTO  FP
                        JOIN TBFII_FUNDOIMOB F ON ( F.ID = FP.IDFUNDO )
                    WHERE FP.SITUACAO = 'A'
                """

        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        if codigo: query += " AND F.CODIGO = :CODIGO "
        if tipo: query += " AND FP.TIPO = :TIPO "
        if dt_ex_ini: query += " AND FP.DATAEX >= :DATAEXINI "
        if dt_ex_fim: query += " AND FP.DATAEX <= :DATAEXFIM "
        if dt_pagto_ini: query += " AND FP.DATAPAGTO >= :DATAPAGTOINI "
        if dt_pagto_fim: query += " AND FP.DATAPAGTO <= :DATAPAGTOFIM "

        if dt_ex_ini and dt_ex_fim: query += " ORDER BY FP.DATAEX "
        elif dt_pagto_ini and dt_pagto_fim: query += " ORDER BY FP.DATAPAGTO "
        else: query += " ORDER BY FP.DATAEX DESC "

        params = {}
        if id_fundo: params['IDFUNDO'] = id_fundo
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
        query = """ SELECT FP.ID,
                           FP.IDFUNDO  AS IDFUNDO, 
                           F.NOME      AS NOMEFUNDO, 
                           F.CODIGO    AS CODIGOFUNDO, 
                           F.SITUACAO  AS SITUACAOFUNDO, 
                           FP.TIPO,
                           FP.CATEGORIA,
                           FP.CODISIN,
                           FP.DATAAPROV,
                           FP.DATACOM,
                           FP.DATAEX,
                           FP.DATAPAGTO,
                           FP.VLRPRECO,
                           FP.SITUACAO
                    FROM TBFII_FUNDOIMOB_PROVENTO  FP
                        JOIN TBFII_FUNDOIMOB F ON ( F.ID = FP.IDFUNDO )
                    WHERE FP.ID = :ID 
                """
        params = {'ID': id}

        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_usuario(cls, db: _orm.Session, id_usuario: int = None, id_fundo: int = None, codigo: str = None, tipo: str = None, dt_ex: str = None, dt_pagto: str = None):

        query = """ SELECT FP.ID,
                           FP.IDFUNDO  AS IDFUNDO, 
                           F.NOME      AS NOMEFUNDO, 
                           F.CODIGO    AS CODIGOFUNDO, 
                           F.SITUACAO  AS SITUACAOFUNDO, 
                           FP.TIPO,
                           FP.CATEGORIA,
                           FP.CODISIN,
                           FP.DATAAPROV,
                           FP.DATACOM,
                           FP.DATAEX,
                           FP.DATAPAGTO,
                           FP.VLRPRECO,
                           FP.SITUACAO
                    FROM TBFII_FUNDOIMOB_PROVENTO  FP
                        JOIN TBFII_FUNDOIMOB F ON ( F.ID = FP.IDFUNDO )
                    WHERE FP.SITUACAO = 'A'
                """

        if id_fundo: query += " AND FP.IDFUNDO = :IDFUNDO "
        if codigo: query += " AND F.CODIGO = :CODIGO "
        if tipo: query += " AND FP.TIPO = :TIPO "

        if dt_ex and dt_pagto: query += " AND ( FP.DATAEX >= :DATAEX OR FP.DATAPAGTO >= :DATAPAGTO ) "
        elif dt_ex: query += " AND FP.DATAEX >= :DATAEX "
        elif dt_pagto: query += " AND FP.DATAPAGTO >= :DATAPAGTO "

        query += """ AND ( SELECT 1 FROM TBCARTEIRA_FUNDO CF JOIN TBCARTEIRA C ON ( C.ID = CF.IDCARTEIRA ) WHERE CF.IDFUNDO  = F.ID AND C.IDUSUARIO = :IDUSUARIO AND CF.SITUACAO = 'A') AND NOT EXISTS( SELECT 1 FROM TBFII_FUNDOIMOB_PROVENTO_ATIVO PRVA WHERE PRVA.IDEMPRPROV = FP.ID AND PRVA.IDUSUARIO = :IDUSUARIO_PROVATIVO ) """
        query += " ORDER BY FP.DATAEX DESC, FP.DATAPAGTO DESC "

        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDUSUARIO_PROVATIVO'] = id_usuario
        if id_fundo: params['IDFUNDO'] = id_fundo
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
            params = {'IDEMPRPROV': self.id}
            db.execute("DELETE FROM TBFII_FUNDOIMOB_PROVENTO_ATIVO WHERE IDEMPRPROV = :IDEMPRPROV", params)
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
