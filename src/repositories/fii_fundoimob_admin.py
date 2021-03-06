# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.fii_fundoimob_admin import FiiFundoImobAdminModel
# from app.models.log_erro import LogErro


class FiiFundoImobAdminRepository:

    @classmethod
    async def find_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(MODEL).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_nomes(cls, db: _orm.Session):
        try:
            return db.query(MODEL).order_by(MODEL.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome_admin(cls, db: _orm.Session):
        query = """ SELECT ID, NOME FROM TBFII_FUNDOIMOB_ADMIN ORDER BY NOME """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
