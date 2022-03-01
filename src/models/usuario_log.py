# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioLog(_database.session.Base):

    __tablename__ = "TBUSUARIO_LOG"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    data = _sql.Column('DATA', _sql.String(8), nullable=False, index=True)
    data_hora = _sql.Column('DATAHORA', _sql.String(20), nullable=False)
    host_ip = _sql.Column('HOSTIP', _sql.String(50))
    host_name = _sql.Column('HOSTNAME', _sql.String(255))
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self):
        pass

    def data_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_hora_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioLog %r>' % str(self.id_usuario)
