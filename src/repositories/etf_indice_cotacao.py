# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.etf_indice_cotacao import ETFIndiceCotacaoModel
# from app.models.log_erro import LogErro


class ETFIndiceCotacaoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(ETFIndiceCotacaoModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_indice(cls, db: _orm.Session, id_indice: int):
        try:
            return db.query(ETFIndiceCotacaoModel).filter_by(id_indice=id_indice).first()
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
                           F.ID       AS INDICEID, 
                           F.NOME     AS INDICENOME, 
                           F.CODIGO   AS INDICECODIGO, 
                           F.SITUACAO AS INDICESIT
                    FROM TBETF_INDICE_COTACAO C
                      INNER JOIN TBETF_INDICE F ON ( F.ID = C.IDINDICE )
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
                           F.ID       AS INDICEID, 
                           F.NOME     AS INDICENOME, 
                           F.CODIGO   AS INDICECODIGO, 
                           F.SITUACAO AS INDICESIT
                    FROM TBETF_INDICE_COTACAO C
                      INNER JOIN TBETF_INDICE F ON ( F.ID = C.IDINDICE )
                    WHERE F.CODIGO = :CODIGO 
                    ORDER BY F.NOME
                """
        params = {'CODIGO': codigo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id_indice(cls, db: _orm.Session, id_indice: int):
        query = """ SSELECT C.VLRPRECOFECHAMENTO FROM TBETF_INDICE_COTACAO C WHERE C.IDINDICE = :IDINDICE """
        params = {'IDINDICE': id_indice}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: ETFIndiceCotacaoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: ETFIndiceCotacaoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
