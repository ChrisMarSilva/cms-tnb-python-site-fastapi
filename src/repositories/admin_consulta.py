# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro



class AdminConsultaRepository:

    @classmethod
    async def buscar_tabelas(cls, db: _orm.Session):
        query = """ SELECT TABLE_NAME, TABLE_ROWS
                    FROM INFORMATION_SCHEMA.TABLES
                    WHERE TABLE_SCHEMA = 'tamonabo_BDCMSTamoNaBolsa'
                      AND TABLE_TYPE   = 'BASE TABLE'
                    ORDER BY TABLE_NAME
            """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_campos(cls, db: _orm.Session):
        query = """ SELECT TABLE_NAME, 
                           ORDINAL_POSITION, 
                           COLUMN_NAME, 
                           DATA_TYPE, 
                           IS_NULLABLE, 
                           COLUMN_DEFAULT, 
                           COLUMN_TYPE, 
                           COLUMN_KEY
                    FROM INFORMATION_SCHEMA.COLUMNS
                    WHERE TABLE_SCHEMA = 'tamonabo_BDCMSTamoNaBolsa'
                    ORDER BY TABLE_NAME, ORDINAL_POSITION
            """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_consulta_dinamica(cls, db: _orm.Session, query: str = '', params: dict = {}):
        try:
            return db.execute(query, params) #.fetchall()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
