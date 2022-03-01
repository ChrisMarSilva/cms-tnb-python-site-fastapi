# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str, decimal_prov_to_str
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class ACAOEmpresaProventoModel(_database.session.Base):

    __tablename__ = "TBEMPRESA_PROVENTO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_empresa = _sql.Column('IDEMPRESA', _sql.Integer, nullable=True, index=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    categoria = _sql.Column('CATEGORIA', _sql.String(1), nullable=True)
    codigo_isin = _sql.Column('CODISIN', _sql.String(50), nullable=True)
    data_aprov = _sql.Column('DATAAPROV', _sql.String(8), nullable=False)
    data_com = _sql.Column('DATACOM', _sql.String(8), nullable=True, index=True)
    data_ex = _sql.Column('DATAEX', _sql.String(8), nullable=True, index=True)
    data_pagto = _sql.Column('DATAPAGTO', _sql.String(8), nullable=True, index=True)
    vlr_preco = _sql.Column('VLRPRECO', _sql.Float(20, 12), nullable=False)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_empresa: int = None, tipo: str = None, categoria: str = None,
                 codigo_isin: str = None, data_aprov: str = None, data_com: str = None, data_ex: str = None,
                 data_pagto: str = None, vlr_preco: float = 0.0, situacao: str = None):
        self.id = id
        self.id_empresa = id_empresa
        self.tipo = tipo
        self.categoria = categoria
        self.codigo_isin = codigo_isin
        self.data_aprov = data_aprov
        self.data_com = data_com
        self.data_ex = data_ex
        self.data_pagto = data_pagto
        self.vlr_preco = vlr_preco
        self.situacao = situacao

    def data_aprov_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_aprov, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_com_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_com, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_ex_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_pagto_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_aprov_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_aprov, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def data_com_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_com, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def data_ex_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def data_pagto_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def vlr_preco_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco)

    def vlr_preco_format_2(self) -> str:
        return decimal_prov_to_str(valor=self.vlr_preco)

    def tipo_descr(self) -> str:
        return self.descricao_tipo(tipo=self.tipo)

    def categoria_descr(self) -> str:
        return self.descricao_categoria(categoria=self.categoria)

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def descricao_categoria(cls, categoria: str) -> str:
        if categoria == 'ON':
            return 'Ordinárias'
        elif categoria == 'PN':
            return 'Preferencial'
        elif categoria == 'UN' or categoria == 'UNT':
            return 'Units'
        else:
            return 'Desconhecida'

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':
            return 'Ativo'
        elif situacao == 'I':
            return 'Inativo'
        else:
            return 'Desconhecida'

    @classmethod
    def descricao_tipo(cls, tipo: str) -> str:
        if tipo == 'D':
            return 'DIVIDENDOS'
        elif tipo == 'J':
            return 'JRS CAP PRÓPRIO'
        elif tipo == 'S':
            return 'Subscrição'
        elif tipo == 'G':
            return 'Grupamento'
        elif tipo == 'E':
            return 'Desdobramento'
        elif tipo == 'B':
            return 'Bonificação'
        elif tipo == 'R':
            return 'REST CAP DIN'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<EmpresaProvento {str(self.id)}>'
