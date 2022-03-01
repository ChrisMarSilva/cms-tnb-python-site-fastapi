# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class ACAOEmpresaFinanceiroDFCTrimestral(_database.session.Base):

    __tablename__ = "TBEMPRESA_FINAN_DFC_TRIMESTRAL"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    cod_cvm = _sql.Column('CD_CVM', _sql.String(6), nullable=True, index=True)
    ano_refer = _sql.Column('ANO_REFER', _sql.String(4), nullable=True, index=True)
    tri_refer = _sql.Column('TRI_REFER', _sql.String(6), nullable=True, index=True)
    vlr_caixa_liquido_operac = _sql.Column('VLR_CAIXA_LIQUIDO_OPERAC', _sql.Float(29, 10), nullable=True)
    vlr_caixa_liquido_operac_gerado = _sql.Column('VLR_CAIXA_LIQUIDO_OPERAC_CAIXA_GERADO', _sql.Float(29, 10), nullable=True)
    vlr_caixa_liquido_operac_variacoes = _sql.Column('VLR_CAIXA_LIQUIDO_OPERAC_VARIACOES', _sql.Float(29, 10), nullable=True)
    vlr_caixa_liquido_operac_outros = _sql.Column('VLR_CAIXA_LIQUIDO_OPERAC_OUTROS', _sql.Float(29, 10), nullable=True)
    vlr_caixa_liquido_operac_depre_amort = _sql.Column('VLR_CAIXA_LIQUIDO_OPERAC_DEPRECIACAO_AMORTIZACAO', _sql.Float(29, 10), nullable=True)
    vlr_caixa_liquido_invest = _sql.Column('VLR_CAIXA_LIQUIDO_INVEST', _sql.Float(29, 10), nullable=True)
    vlr_caixa_liquido_finan = _sql.Column('VLR_CAIXA_LIQUIDO_FINAN', _sql.Float(29, 10), nullable=True)
    vlr_variacao_cambial = _sql.Column('VLR_VARIACOES_CAMBIAL', _sql.Float(29, 10), nullable=True)
    vlr_caixa_equivalente = _sql.Column('VLR_CAIXA_EQUIVALENTE', _sql.Float(29, 10), nullable=True)
    vlr_caixa_equivalente_saldo_ini = _sql.Column('VLR_CAIXA_EQUIVALENTE_SALDO_INICIA', _sql.Float(29, 10), nullable=True)
    vlr_caixa_equivalente_saldo_fim = _sql.Column('VLR_CAIXA_EQUIVALENTE_SALDO_FINAL', _sql.Float(29, 10), nullable=True)
    vlr_caixa_total = _sql.Column('VLR_CAIXA_TOTAL', _sql.Float(29, 10), nullable=True)
    vlr_caixa_livre = _sql.Column('VLR_CAIXA_LIVRE', _sql.Float(29, 10), nullable=True)

    def __init__(self, id: int = None, cod_cvm: str = None, ano_refer: str = None, tri_refer: str = None, vlr_caixa_liquido_operac: float = 0.0,
                 vlr_caixa_liquido_operac_gerado: float = 0.0, vlr_caixa_liquido_operac_variacoes: float = 0.0,
                 vlr_caixa_liquido_operac_outros: float = 0.0, vlr_caixa_liquido_operac_depre_amort: float = 0.0,
                 vlr_caixa_liquido_invest: float = 0.0, vlr_caixa_liquido_finan: float = 0.0, vlr_variacao_cambial: float = 0.0,
                 vlr_caixa_equivalente: float = 0.0, vlr_caixa_equivalente_saldo_ini: float = 0.0, vlr_caixa_equivalente_saldo_fim: float = 0.0,
                 vlr_caixa_total: float = 0.0, vlr_caixa_livre: float = 0.0):
        self.id = id
        self.cod_cvm = cod_cvm
        self.ano_refer = ano_refer
        self.tri_refer = tri_refer
        self.vlr_caixa_liquido_operac = vlr_caixa_liquido_operac
        self.vlr_caixa_liquido_operac_gerado = vlr_caixa_liquido_operac_gerado
        self.vlr_caixa_liquido_operac_variacoes = vlr_caixa_liquido_operac_variacoes
        self.vlr_caixa_liquido_operac_outros = vlr_caixa_liquido_operac_outros
        self.vlr_caixa_liquido_operac_depre_amort = vlr_caixa_liquido_operac_depre_amort
        self.vlr_caixa_liquido_invest = vlr_caixa_liquido_invest
        self.vlr_caixa_liquido_finan = vlr_caixa_liquido_finan
        self.vlr_variacao_cambial = vlr_variacao_cambial
        self.vlr_caixa_equivalente = vlr_caixa_equivalente
        self.vlr_caixa_equivalente_saldo_ini = vlr_caixa_equivalente_saldo_ini
        self.vlr_caixa_equivalente_saldo_fim = vlr_caixa_equivalente_saldo_fim
        self.vlr_caixa_total = vlr_caixa_total
        self.vlr_caixa_livre = vlr_caixa_livre

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<ACAOEmpresaFinanceiroDFCTrimestral {str(self.id)}>'

