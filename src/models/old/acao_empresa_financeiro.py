# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro


class ACAOEmpresaFinanceiro(db.Model):

    __tablename__ = "TBEMPRESA_FINAN"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    cod_cvm = db.Column('CD_CVM', db.String(6), nullable=True, index=True)
    nome = db.Column('DENOM_CIA', db.String(100), nullable=True)
    cnpj = db.Column('CNPJ_CIA', db.String(20), nullable=True)
    ult_ano_refer = db.Column('ULT_ANO_REFER', db.String(4), nullable=True)
    ult_tri_refer = db.Column('ULT_TRI_REFER', db.String(6), nullable=True)

    def __init__(self, id: int = None, cod_cvm: str = None, nome: str = None,
                 cnpj: str = None, ult_ano_refer: str = None, ult_tri_refer: str = None):
        self.id = id
        self.cod_cvm = cod_cvm
        self.nome = nome
        self.cnpj = cnpj
        self.ult_ano_refer = ult_ano_refer
        self.ult_tri_refer = ult_tri_refer

    @classmethod
    def get_all(cls):
        try:
            return cls.query.order_by(cls.nome).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_id(cls, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_cod_cvmd(cls, cod_cvm: str):
        try:
            return cls.query.filter_by(cod_cvm=cod_cvm).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    # @classmethod
    # def buscar_listar_anos_finan_anual(cls, cod_cvm: str):
    #     try:
    #         query = """ SELECT DISTINCT ANO_REREF FROM TBEMPRESA_DFP WHERE CD_CVM = :CD_CVM ORDER BY ANO_REREF """
    #         params = {'CD_CVM': cod_cvm}
    #         return db.session.execute(query, params)
    #     except Exception as e:
    #         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
    #         raise
    #
    # @classmethod
    # def buscar_contas_finan_anual(cls, cod_cvm: str, tipo_arqv: str, tipo_info: str):
    #     try:
    #         query = """ SELECT CD_CVM, ANO_REREF, DT_REFER, VERSAO, CD_CONTA, DS_CONTA, VL_CONTA FROM TBEMPRESA_""" + tipo_arqv + """_""" + tipo_info + """ WHERE CD_CVM = :CD_CVM ORDER BY DT_REFER, CD_CONTA """
    #         params = {'CD_CVM': cod_cvm}
    #         return db.session.execute(query, params)
    #     except Exception as e:
    #         LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
    #         raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<EmpresaFinanceiro {str(self.id)}>'

