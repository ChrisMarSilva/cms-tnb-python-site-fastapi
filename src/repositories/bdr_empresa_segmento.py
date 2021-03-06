# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.bdr_empresa_segmento import BDREmpresaSegmentoModel
# from app.models.log_erro import LogErro


class BDREmpresaSegmentoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(BDREmpresaSegmentoModel).filter_by(situacao='A').order_by(BDREmpresaSegmentoModel.descricao).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(BDREmpresaSegmentoModel).filter_by(id=id, situacao='A').first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_descricao(cls, db: _orm.Session, descricao: str):
        try:
            return db.query(BDREmpresaSegmentoModel).filter_by(descricao=descricao, situacao='A').first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT S.ID, S.DESCRICAO, S.SITUACAO FROM TBBDR_EMPRESA_SEGMENTO S WHERE S.SITUACAO = 'A' ORDER BY S.DESCRICAO """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int):
        query = """ SELECT S.ID, S.DESCRICAO, S.SITUACAO FROM TBBDR_EMPRESA_SEGMENTO S WHERE S.SITUACAO = 'A' AND S.ID = :ID """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_descricao(cls, db: _orm.Session, descricao: str):
        query = """ SELECT S.ID, S.DESCRICAO, S.SITUACAO FROM TBBDR_EMPRESA_SEGMENTO S WHERE S.SITUACAO = 'A' AND S.DESCRICAO = :DESCRICAO """
        params = {'DESCRICAO': descricao}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista(cls, db: _orm.Session):
        query = """ SELECT S.ID, S.DESCRICAO FROM TBBDR_EMPRESA_SEGMENTO S WHERE S.SITUACAO = 'A' ORDER BY S.DESCRICAO """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_cotacao(cls, db: _orm.Session):
        query = """ SELECT S.ID, S.DESCRICAO
                    FROM TBBDR_EMPRESA_SEGMENTO S
                    WHERE S.SITUACAO = 'A'
                      AND EXISTS( SELECT 1
                                  FROM TBBDR_EMPRESA E
                                  WHERE E.IDSETOR = S.ID
                                   AND EXISTS( SELECT 1 FROM TBBDR_EMPRESA_COTACAO C WHERE C.IDBDR = E.ID ) 
                                )
                    ORDER BY S.DESCRICAO
                """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
