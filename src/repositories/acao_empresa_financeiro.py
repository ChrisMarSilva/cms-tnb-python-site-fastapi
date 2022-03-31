# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.xxxxxxxxxxx import xxxxxxxxxxxModel
# from app.models.log_erro import LogErro


class ACAOEmpresaFinanceiroRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.order_by(nome).all()
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
    async def get_by_cod_cvmd(cls, db: _orm.Session, cod_cvm: str):
        try:
            return cls.query.filter_by(cod_cvm=cod_cvm).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_listar_anos_finan_anual(cls, db: _orm.Session, cod_cvm: str):
        try:
            query = """ SELECT DISTINCT ANO_REREF FROM TBEMPRESA_DFP WHERE CD_CVM = :CD_CVM ORDER BY ANO_REREF """
           params = {'CD_CVM': cod_cvm}
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
    
    @classmethod
    def buscar_contas_finan_anual(cls, db: _orm.Session, cod_cvm: str, tipo_arqv: str, tipo_info: str):
        try:
            query = """ SELECT CD_CVM, ANO_REREF, DT_REFER, VERSAO, CD_CONTA, DS_CONTA, VL_CONTA FROM TBEMPRESA_""" + tipo_arqv + """_""" + tipo_info + """ WHERE CD_CVM = :CD_CVM ORDER BY DT_REFER, CD_CONTA """
            params = {'CD_CVM': cod_cvm}
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

