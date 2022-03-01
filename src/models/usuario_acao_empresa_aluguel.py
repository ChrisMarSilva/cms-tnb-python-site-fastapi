# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioACAOEmpresaAluguelModel(_database.session.Base):

    __tablename__ = "TBALUGUEL_ATIVO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    id_ativo = _sql.Column('IDATIVO', _sql.Integer, _sql.ForeignKey('TBEMPRESA_ATIVO.ID'), nullable=False, index=True)
    data = _sql.Column('DATA', _sql.String(8), nullable=False, index=True)
    valor_bruto = _sql.Column('VLRBRUTO', _sql.Float(17, 2), nullable=False)
    valor_ir = _sql.Column('VLRIR', _sql.Float(17, 2), nullable=False)
    valor_liquido = _sql.Column('VLRLIQUIDO', _sql.Float(17, 2), nullable=False)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, id_ativo: int = None, data: str = None,
                 valor_bruto: float = 0.0, valor_ir: float = 0.0, valor_liquido: float = 0.0,
                 situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_ativo = id_ativo
        self.data = data
        self.valor_bruto = valor_bruto
        self.valor_ir = valor_ir
        self.valor_liquido = valor_liquido
        self.situacao = situacao

    def data_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def valor_bruto_format(self) -> str:
        return decimal_to_str(valor=self.valor_bruto)

    def valor_ir_format(self) -> str:
        return decimal_to_str(valor=self.valor_ir)

    def valor_liquido_format(self) -> str:
        return decimal_to_str(valor=self.valor_liquido)

    def situacao_descr(self) -> str:
        if self.situacao == 'A':
            return 'Ativo'
        elif self.situacao == 'I':
            return 'Inativo'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioEmpresaAluguel {str(self.id)} - {self.nome} - {self.cnpj}>'
