# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class ACAOEmpresaFinanceiroDREAnual(_database.session.Base):

    __tablename__ = "TBEMPRESA_FINAN_DRE_ANUAL"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    cod_cvm = _sql.Column('CD_CVM', _sql.String(6), nullable=True, index=True)
    ano_refer = _sql.Column('ANO_REFER', _sql.String(4), nullable=True, index=True)
    vlr_receita_liq = _sql.Column('VLR_RECEITA_LIQ', _sql.Float(29, 10), nullable=True)
    vlr_custo = _sql.Column('VLR_CUSTO', _sql.Float(29, 10), nullable=True)
    vlr_lucro_bruto = _sql.Column('VLR_LUCRO_BRUTO', _sql.Float(29, 10), nullable=True)
    vlr_margem_bruta = _sql.Column('VLR_MARGEM_BRUTA', _sql.Float(5, 2), nullable=True)
    vlr_despesa_operac = _sql.Column('VLR_DESPESA_OPERAC', _sql.Float(29, 10), nullable=True)
    vlr_resultado_operac = _sql.Column('VLR_RESULTADO_OPERAC', _sql.Float(29, 10), nullable=True)
    vlr_margem_operac = _sql.Column('VLR_MARGEM_OPERAC', _sql.Float(5, 2), nullable=True)
    vlr_resultado_finan = _sql.Column('VLR_RESULTADO_FINAN', _sql.Float(29, 10), nullable=True)
    vlr_resultado_antes_ir = _sql.Column('VLR_RESULTADO_ANTES_IR', _sql.Float(29, 10), nullable=True)
    vlr_imposto = _sql.Column('VLR_IMPOSTO', _sql.Float(29, 10), nullable=True)
    vlr_operac_cont = _sql.Column('VLR_OPERAC_CONT', _sql.Float(29, 10), nullable=True)
    vlr_operac_descont = _sql.Column('VLR_OPERAC_DESCONT', _sql.Float(29, 10), nullable=True)
    vlr_lucro_liquido = _sql.Column('VLR_LUCRO_LIQUIDO', _sql.Float(29, 10), nullable=True)
    vlr_margem_liquida = _sql.Column('VLR_MARGEM_LIQUIDA', _sql.Float(5, 2), nullable=True)

    def __init__(self, id: int = None, cod_cvm: str = None, ano_refer: str = None, vlr_receita_liq: float = 0.0,
                 vlr_custo: float = 0.0, vlr_lucro_bruto: float = 0.0, vlr_margem_bruta: float = 0.0,
                 vlr_despesa_operac: float = 0.0, vlr_resultado_operac: float = 0.0, vlr_margem_operac: float = 0.0,
                 vlr_resultado_finan: float = 0.0, vlr_resultado_antes_ir: float = 0.0, vlr_imposto: float = 0.0,
                 vlr_operac_cont: float = 0.0, vlr_operac_descont: float = 0.0, vlr_lucro_liquido: float = 0.0,
                 vlr_margem_liquida: float = 0.0):
        self.id = id
        self.cod_cvm = cod_cvm
        self.ano_refer = ano_refer
        self.vlr_receita_liq = vlr_receita_liq
        self.vlr_custo = vlr_custo
        self.vlr_lucro_bruto = vlr_lucro_bruto
        self.vlr_margem_bruta = vlr_margem_bruta
        self.vlr_despesa_operac = vlr_despesa_operac
        self.vlr_resultado_operac = vlr_resultado_operac
        self.vlr_margem_operac = vlr_margem_operac
        self.vlr_resultado_finan = vlr_resultado_finan
        self.vlr_resultado_antes_ir = vlr_resultado_antes_ir
        self.vlr_imposto = vlr_imposto
        self.vlr_operac_cont = vlr_operac_cont
        self.vlr_operac_descont = vlr_operac_descont
        self.vlr_lucro_liquido = vlr_lucro_liquido
        self.vlr_magem_liquida = vlr_margem_liquida

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<ACAOEmpresaFinanceiroDREAnual {str(self.id)}>'

