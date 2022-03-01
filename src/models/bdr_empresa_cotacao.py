# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class BDREmpresaCotacaoModel(_database.session.Base):

    __tablename__ = "TBBDR_EMPRESA_COTACAO"

    data = _sql.Column('DATA', _sql.String(8), nullable=False, index=True)
    id_bdr = _sql.Column('IDBDR', _sql.Integer, _sql.ForeignKey('TBBDR_EMPRESA.ID'), primary_key=True, nullable=False, index=True)
    vlr_preco_abertura = _sql.Column('VLRPRECOABERTURA', _sql.Float(17, 2), nullable=False)
    vlr_preco_fechamento = _sql.Column('VLRPRECOFECHAMENTO', _sql.Float(17, 2), nullable=False)
    vlr_preco_maximo = _sql.Column('VLRPRECOMAXIMO', _sql.Float(17, 2), nullable=False)
    vlr_preco_minimo = _sql.Column('VLRPRECOMINIMO', _sql.Float(17, 2), nullable=False)
    vlr_preco_anterior = _sql.Column('VLRPRECOANTERIOR', _sql.Float(17, 2), nullable=False)
    vlr_variacao = _sql.Column('VLRVARIACAO', _sql.Float(17, 2), nullable=False)
    data_hora_alteracao = _sql.Column('DATAHORAALTERACO', _sql.String(14), nullable=False)

    def __init__(self, data: str = None, id_bdr: int = None, vlr_preco_abertura: float = 0.0,
                 vlr_preco_fechamento: float = 0.0, vlr_preco_maximo: float = 0.0, vlr_preco_minimo: float = 0.0,
                 vlr_preco_anterior: float = 0.0, vlr_variacao: float = 0.0, data_hora_alteracao: str = None):
        self.data = data
        self.id_bdr = id_bdr
        self.vlr_preco_abertura = vlr_preco_abertura
        self.vlr_preco_fechamento = vlr_preco_fechamento
        self.vlr_preco_maximo = vlr_preco_maximo
        self.vlr_preco_minimo = vlr_preco_minimo
        self.vlr_preco_anterior = vlr_preco_anterior
        self.vlr_variacao = vlr_variacao
        self.data_hora_alteracao = data_hora_alteracao

    def vlr_preco_abertura_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_abertura)

    def vlr_preco_fechamento_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_fechamento)

    def vlr_preco_maximo_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_maximo)

    def vlr_preco_minimo_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_minimo)

    def vlr_preco_anterior_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_anterior)

    def vlr_variacao_format(self) -> str:
        return decimal_to_str(valor=self.vlr_variacao)

    def data_hora_alteracao_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora_alteracao, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<BDREmpresaAtivoCotacao {str(self.id)}>'
