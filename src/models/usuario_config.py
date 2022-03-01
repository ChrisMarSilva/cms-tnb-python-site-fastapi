# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class UsuarioConfig(_database.session.Base):

    __tablename__ = "TBUSUARIO_CONFIG"

    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)
    tipo = _sql.Column('TIPO', _sql.String(50), primary_key=True, nullable=False, index=True)
    valor = _sql.Column('VALOR', _sql.String(250), nullable=False)

    def __init__(self, id_usuario: int = None, tipo: str = None, valor: str = None):
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.valor = valor

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioConfig - IdUser: {str(self.id_usuario)} - Tp: {self.tipo} - Vlr: {self.valor}>'
