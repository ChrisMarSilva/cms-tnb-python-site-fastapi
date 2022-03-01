# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str, inteiro_to_str
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioFiiFundoImobProventoModel(_database.session.Base):

    __tablename__ = "TBFII_PROVENTO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    id_fundo = _sql.Column('IDFUNDO', _sql.Integer, _sql.ForeignKey('TBFII_FUNDOIMOB.ID'), nullable=False, index=True)
    id_corretora = _sql.Column('IDCORRETORA', _sql.Integer, _sql.ForeignKey('TBCORRETORA.ID'), nullable=True, index=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    data_ex = _sql.Column('DATAEX', _sql.String(8), nullable=False, index=True)
    data_pagto = _sql.Column('DATAPAGTO', _sql.String(8), nullable=False, index=True)
    quantidade = _sql.Column('QUANTIDADE', _sql.Float(20, 10), nullable=False)
    vlr_preco = _sql.Column('VLRPRECO', _sql.Float(20, 10), nullable=False)
    tot_vlr = _sql.Column('TOTVLR', _sql.Float(17, 2), nullable=False)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, id_fundo: int = None, id_corretora: int = None,
                 tipo: str = None, data_ex: str = None, data_pagto: str = None, quantidade: float = 0.0,
                 vlr_preco: float = 0.0, tot_vlr: float = 0.0, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_fundo = id_fundo
        self.id_corretora = id_corretora
        self.tipo = tipo
        self.data_ex = data_ex
        self.data_pagto = data_pagto
        self.quantidade = quantidade
        self.vlr_preco = vlr_preco
        self.tot_vlr = tot_vlr
        self.situacao = situacao

    def calc_total(self) -> float:
        return self.calcular_total(quantidade=self.quantidade, vlr_preco=self.vlr_preco)

    def data_ex_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_pagto_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%d/%m/%Y')
    def data_ex_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def data_pagto_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def quantidade_format(self) -> str:
        return inteiro_to_str(valor=self.quantidade)

    def vlr_preco_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco)

    def tot_vlr_format(self) -> str:
        return decimal_to_str(valor=self.tot_vlr)

    def tipo_descr(self) -> str:
        return self.descricao_tipo(tipo=self.tipo)

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def calcular_total(cls, quantidade: float, vlr_preco: float) -> float:
        return float(quantidade) * float(vlr_preco) if quantidade > 0.0 and vlr_preco > 0.0 else 0.0

    @classmethod
    def descricao_tipo(cls, tipo: str) -> str:
        if tipo == 'R':
            return 'RENDIMENTO'
        else:
            return 'Desconhecido'

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':
            return 'Ativo'
        elif situacao == 'B':
            return 'Pendente Aprovação/Confirmação'
        elif situacao == 'I':
            return 'Inativo'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioFiiFundoImobProvento {str(self.id)}>'
