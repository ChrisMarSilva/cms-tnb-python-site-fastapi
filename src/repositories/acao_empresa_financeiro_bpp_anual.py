# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.acao_empresa_financeiro_bpp_anual import ACAOEmpresaFinanceiroBPPAnualModel
# from app.models.log_erro import LogErro


class ACAOEmpresaFinanceiroBPPAnualRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(ACAOEmpresaFinanceiroBPPAnualModel).order_by(ACAOEmpresaFinanceiroBPPAnualModel.ano_refer, ACAOEmpresaFinanceiroBPPAnualModel.cod_cvm).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(ACAOEmpresaFinanceiroBPPAnualModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_cod_cvm(cls, db: _orm.Session, cod_cvm: str):
        try:
            return db.query(ACAOEmpresaFinanceiroBPPAnualModel).filter_by(cod_cvm=cod_cvm).order_by(ACAOEmpresaFinanceiroBPPAnualModel.ano_refer).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

