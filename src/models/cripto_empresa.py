# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class CriptoEmpresa(_database.session.Base):

    __tablename__ = "TBCRIPTO_EMPRESA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True, index=True)
    nome = _sql.Column('NOME', _sql.String(100), nullable=False, index=True)
    codigo = _sql.Column('CODIGO', _sql.String(10), nullable=False, index=True)
    vlr_preco_fechamento = _sql.Column('VLRPRECOFECHAMENTO', _sql.Float(17, 2), nullable=False)
    vlr_preco_anterior = _sql.Column('VLRPRECOANTERIOR', _sql.Float(17, 2), nullable=False)
    vlr_variacao = _sql.Column('VLRVARIACAO', _sql.Float(17, 2), nullable=False)
    data_hora_alteracao = _sql.Column('DATAHORAALTERACO', _sql.String(14), nullable=False)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, nome: str = None, codigo: str = None, vlr_preco_fechamento: float = 0.0,
                 vlr_preco_anterior: float = 0.0, vlr_variacao: float = 0.0, data_hora_alteracao: str = None,
                 situacao: str = None):
        self.id = id
        self.nome = nome
        self.codigo = codigo
        self.vlr_preco_fechamento = vlr_preco_fechamento
        self.vlr_preco_anterior = vlr_preco_anterior
        self.vlr_variacao = vlr_variacao
        self.data_hora_alteracao = data_hora_alteracao
        self.situacao = situacao

    def vlr_preco_fechamento_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_fechamento)

    def vlr_preco_anterior_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_anterior)

    def vlr_variacao_format(self) -> str:
        return decimal_to_str(valor=self.vlr_variacao)

    def data_hora_alteracao_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora_alteracao, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A': return 'Ativo'
        elif situacao == 'I': return 'Inativo'
        elif situacao == 'E': return 'Encerrado'
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<CriptoEmpresa {str(self.id)} - {self.nome} - {self.nome}>'
