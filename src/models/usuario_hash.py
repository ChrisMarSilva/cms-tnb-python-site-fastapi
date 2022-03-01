# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioHash(_database.session.Base):

    __tablename__ = "TBUSUARIO_HASH"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    hash = _sql.Column('HASH', _sql.String(255), nullable=False, unique=True, index=True)
    data_registro = _sql.Column('DTREGISTRO', _sql.String(8), nullable=False)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, hash: str = None, data_registro: str = None,
                 situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.hash = hash
        self.data_registro = data_registro
        self.situacao = situacao

    def data_registro_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_registro, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioHash %r>' % self.hash
