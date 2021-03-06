# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.fii_fundoimob_cotacao import FiiFundoImobCotacaoModel
# from app.models.log_erro import LogErro


class FiiFundoImobCotacaoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(FiiFundoImobCotacaoModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_fundo(cls, db: _orm.Session, id_fundo: int):
        try:
            return db.query(FiiFundoImobCotacaoModel).filter_by(id_fundo=id_fundo).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT C.DATA, 
                           C.VLRPRECOABERTURA,  
                           C.VLRPRECOFECHAMENTO,  
                           C.VLRPRECOMAXIMO, 
                           C.VLRPRECOMINIMO,
                           C.VLRPRECOANTERIOR, 
                           C.VLRVARIACAO, 
                           C.DATAHORAALTERACO ,
                           F.ID       AS FUNDOID, 
                           F.NOME     AS FUNDONOME, 
                           F.CODIGO   AS FUNDOCODIGO, 
                           F.SITUACAO AS FUNDOSIT
                    FROM TBFII_FUNDOIMOB_COTACAO C
                      INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = C.IDFUNDO )
                    WHERE F.SITUACAO = 'A'
                    ORDER BY F.NOME
                """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, codigo: str):
        query = """ SELECT C.DATA, 
                           C.VLRPRECOABERTURA,  
                           C.VLRPRECOFECHAMENTO,  
                           C.VLRPRECOMAXIMO, 
                           C.VLRPRECOMINIMO,
                           C.VLRPRECOANTERIOR, 
                           C.VLRVARIACAO, 
                           C.DATAHORAALTERACO ,
                           F.ID       AS FUNDOID, 
                           F.NOME     AS FUNDONOME, 
                           F.CODIGO   AS FUNDOCODIGO, 
                           F.SITUACAO AS FUNDOSIT
                    FROM TBFII_FUNDOIMOB_COTACAO C
                      INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = C.IDFUNDO )
                    WHERE F.CODIGO = :CODIGO 
                """
        params = {'CODIGO': codigo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id_fundo(cls, db: _orm.Session, id_fundo: int):
        query = """ SSELECT C.VLRPRECOFECHAMENTO FROM TBFII_FUNDOIMOB_COTACAO C WHERE C.IDFUNDO = :IDFUNDO """
        params = {'IDFUNDO': id_fundo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: FiiFundoImobCotacaoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: FiiFundoImobCotacaoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
