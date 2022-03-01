# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioApuracao(_database.session.Base):

    __tablename__ = "TBAPURACAO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False)
    categoria = _sql.Column('CATEGORIA', _sql.String(1), nullable=False)
    ano_mes = _sql.Column('MESANO', _sql.String(6), nullable=False, index=True)
    valor = _sql.Column('VALOR', _sql.Float(17, 2), nullable=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, tipo: str = None, categoria: str = None,
                 ano_mes: str = None, valor: float = 0.0, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.categoria = categoria
        self.ano_mes = ano_mes
        self.valor = valor
        self.situacao = situacao

    def valor_format(self) -> str:
        return decimal_to_str(valor=self.valor)

    def data_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.ano_mes+'01', fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def tipo_descr(self) -> str:
        if self.tipo == 'N':
            return 'Normal'
        elif self.tipo == 'M':
            return 'Manual'
        else:
            return 'Desconhecido'

    def categoria_descr(self) -> str:
        if self.categoria == 'C': return 'Comum'
        elif self.categoria == 'D': return 'Day-Trade'
        elif self.categoria == 'F': return 'FII'
        elif self.categoria == 'E': return 'ETF-Comun'
        elif self.categoria == 'G': return 'ETF-Day-Trade'
        elif self.categoria == 'I': return 'BDR-Comun'
        elif self.categoria == 'J': return 'BDR-Day-Trade'
        else: return 'Desconhecido'

    def situacao_descr(self) -> str:
        if self.situacao == 'A': return 'Ativo'
        elif self.situacao == 'I': return 'Inativo'
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioApuracao {str(self.id)}>'
