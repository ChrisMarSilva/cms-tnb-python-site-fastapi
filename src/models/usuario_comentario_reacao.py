# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class UsuarioComentarioReacao(_database.session.Base):

    __tablename__ = "TBCOMENTARIO_REACAO"

    id_comentario = _sql.Column('IDCOMENTARIO', _sql.Integer, _sql.ForeignKey('TBCOMENTARIO.ID'), primary_key=True, nullable=False, index=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id_comentario: int = None, id_usuario: int = None, tipo: str = None):
        self.id_comentario = id_comentario
        self.id_usuario = id_usuario
        self.tipo = tipo

    def tipo_descr(self) -> str:
        if self.tipo == 'A':
            return 'Gostei'
        elif self.tipo == 'B':
            return 'Não Gostei'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioComentarioReacao {str(self.id)}>'
