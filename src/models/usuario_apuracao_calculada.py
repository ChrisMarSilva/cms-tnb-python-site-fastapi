# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioApuracaoCalculada(_database.session.Base):

    __tablename__ = "TBAPURACAO_CALCULADA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    categoria = _sql.Column('CATEGORIA', _sql.String(1), nullable=False, index=True)
    ano_mes = _sql.Column('MESANO', _sql.String(6), nullable=False, index=True)
    vlr_venda = _sql.Column('VLR_VENDA', _sql.Float(17, 2), nullable=True)
    vlr_lucro_apurado = _sql.Column('VLR_LUCRO_APURADO', _sql.Float(17, 2), nullable=True)
    vlr_prejuizo_compensar = _sql.Column('VLR_PREJUIZO_COMPENSAR', _sql.Float(17, 2), nullable=True)
    vlr_base_calculo = _sql.Column('VLR_BASE_CALCULO', _sql.Float(17, 2), nullable=True)
    vlr_ir_devido = _sql.Column('VLR_IR_DEVIDO', _sql.Float(17, 2), nullable=True)
    vlr_ir_pago = _sql.Column('VLR_IR_PAGO', _sql.Float(17, 2), nullable=True)
    vlr_ir_pagar = _sql.Column('VLR_IR_PAGAR', _sql.Float(17, 2), nullable=True)

    def __init__(self, id: int = None, id_usuario: int = None, categoria: str = None, ano_mes: str = None,
                 vlr_venda: float = 0.0, vlr_lucro_apurado: float = 0.0, vlr_prejuizo_compensar: float = 0.0,
                 vlr_base_calculo: float = 0.0, vlr_ir_devido: float = 0.0, vlr_ir_pago: float = 0.0,
                 vlr_ir_pagar: float = 0.0):
        self.id = id
        self.id_usuario = id_usuario
        self.categoria = categoria
        self.ano_mes = ano_mes
        self.vlr_venda = vlr_venda
        self.vlr_lucro_apurado = vlr_lucro_apurado
        self.vlr_prejuizo_compensar = vlr_prejuizo_compensar
        self.vlr_base_calculo = vlr_base_calculo
        self.vlr_ir_devido = vlr_ir_devido
        self.vlr_ir_pago = vlr_ir_pago
        self.vlr_ir_pagar = vlr_ir_pagar

    def ano_mes_format(self, fmt: str = '%d/%m/%Y') -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.ano_mes+'01', fmt='%Y%m%d'), fmt=fmt)

    def vlr_venda_format(self) -> str:
        return decimal_to_str(valor=self.vlr_venda)

    def vlr_lucro_apurado_format(self) -> str:
        return decimal_to_str(valor=self.vlr_lucro_apurado)

    def vlr_prejuizo_compensar_format(self) -> str:
        return decimal_to_str(valor=self.vlr_prejuizo_compensar)

    def vlr_base_calculo_format(self) -> str:
        return decimal_to_str(valor=self.vlr_base_calculo)

    def vlr_ir_devido_format(self) -> str:
        return decimal_to_str(valor=self.vlr_ir_devido)

    def vlr_ir_pago_format(self) -> str:
        return decimal_to_str(valor=self.vlr_ir_pago)

    def vlr_ir_pagar_format(self) -> str:
        return decimal_to_str(valor=self.vlr_ir_pagar)

    def categoria_descr(self) -> str:
        if self.categoria == 'C': return 'AÇÂO-Comum'
        elif self.categoria == 'D': return 'AÇÂO-Day-Trade'
        elif self.categoria == 'F': return 'FII'
        elif self.categoria == 'E': return 'ETF-Comun'
        elif self.categoria == 'G': return 'ETF-Day-Trade'
        elif self.categoria == 'I': return 'BDR-Comun'
        elif self.categoria == 'J': return 'BDR-Day-Trade'
        elif self.categoria == 'K': return 'CRIPTO' # Cripto
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioApuracaoCalculada {str(self.id)}>'
