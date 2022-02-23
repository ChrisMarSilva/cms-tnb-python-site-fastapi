# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro


class ACAOEmpresaFinanceiroBPAAnual(db.Model):

    __tablename__ = "TBEMPRESA_FINAN_BPA_ANUAL"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    cod_cvm = db.Column('CD_CVM', db.String(6), nullable=True, index=True)
    ano_refer = db.Column('ANO_REFER', db.String(4), nullable=True, index=True)
    vlr_ativo_total = db.Column('VLR_ATIVO_TOTAL', db.Float(29, 10), nullable=True)
    vlr_circulante = db.Column('VLR_CIRCULANTE', db.Float(29, 10), nullable=True)
    vlr_circulante_caixa = db.Column('VLR_CIRCULANTE_CAIXA', db.Float(29, 10), nullable=True)
    vlr_circulante_aplic_finan = db.Column('VLR_CIRCULANTE_APLIC_FINAN', db.Float(29, 10), nullable=True)
    vlr_circulante_contas_rec = db.Column('VLR_CIRCULANTE_CONTAS_REC', db.Float(29, 10), nullable=True)
    vlr_circulante_estoque = db.Column('VLR_CIRCULANTE_ESTOQUE', db.Float(29, 10), nullable=True)
    vlr_circulante_outros = db.Column('VLR_CIRCULANTE_OUTROS', db.Float(29, 10), nullable=True)
    vlr_nao_circulante = db.Column('VLR_NAO_CIRCULANTE', db.Float(29, 10), nullable=True)
    vlr_nao_circulante_longo_prazo = db.Column('VLR_NAO_CIRCULANTE_LONGO_PRAZO', db.Float(29, 10), nullable=True)
    vlr_nao_circulante_investimentos = db.Column('VLR_NAO_CIRCULANTE_INVESTIMENTOS', db.Float(29, 10), nullable=True)
    vlr_nao_circulante_imobilizado = db.Column('VLR_NAO_CIRCULANTE_IMOBILIZADO', db.Float(29, 10), nullable=True)
    vlr_nao_circulante_intangivel = db.Column('VLR_NAO_CIRCULANTE_INTANGIVEL', db.Float(29, 10), nullable=True)
    vlr_nao_circulante_outros = db.Column('VLR_NAO_CIRCULANTE_OUTROS', db.Float(29, 10), nullable=True)

    def __init__(self, id: int = None, cod_cvm: str = None, ano_refer: str = None, vlr_ativo_total: float = 0.0, vlr_circulante: float = 0.0,
                 vlr_circulante_caixa: float = 0.0, vlr_circulante_aplic_finan: float = 0.0, vlr_circulante_contas_rec: float = 0.0,
                 vlr_circulante_estoque: float = 0.0, vlr_circulante_outros: float = 0.0, vlr_nao_circulante: float = 0.0,
                 vlr_nao_circulante_longo_prazo: float = 0.0, vlr_nao_circulante_investimentos: float = 0.0, vlr_nao_circulante_imobilizado: float = 0.0,
                 vlr_nao_circulante_intangivel: float = 0.0, vlr_nao_circulante_outros: float = 0.0):
        self.id = id
        self.cod_cvm = cod_cvm
        self.ano_refer = ano_refer
        self.vlr_ativo_total = vlr_ativo_total
        self.vlr_circulante = vlr_circulante
        self.vlr_circulante_caixa = vlr_circulante_caixa
        self.vlr_circulante_aplic_finan = vlr_circulante_aplic_finan
        self.vlr_circulante_contas_rec = vlr_circulante_contas_rec
        self.vlr_circulante_estoque = vlr_circulante_estoque
        self.vlr_circulante_outros = vlr_circulante_outros
        self.vlr_nao_circulante = vlr_nao_circulante
        self.vlr_nao_circulante_longo_prazo = vlr_nao_circulante_longo_prazo
        self.vlr_nao_circulante_investimentos = vlr_nao_circulante_investimentos
        self.vlr_nao_circulante_imobilizado = vlr_nao_circulante_imobilizado
        self.vlr_nao_circulante_intangivel = vlr_nao_circulante_intangivel
        self.vlr_nao_circulante_outros = vlr_nao_circulante_outros

    @classmethod
    def get_all(cls):
        try:
            return cls.query.order_by(cls.ano_refer, cls.cod_cvm).all()
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
    def get_all_by_cod_cvm(cls, cod_cvm: str):
        try:
            return cls.query.filter_by(cod_cvm=cod_cvm).order_by(cls.ano_refer).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<ACAOEmpresaFinanceiroBPAAnual {str(self.id)}>'

