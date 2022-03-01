# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class UsuarioBDREmpresaFatoRelevanteAtivoModel(_database.session.Base):

    __tablename__ = "TBBDR_EMPRESA_FATORELEVANTE_ATIVO"

    id_fato = _sql.Column('IDFATO', _sql.Integer, _sql.ForeignKey('TBBDR_EMPRESA_FATORELEVANTE.ID'), primary_key=True, nullable=False, index=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)

    def __init__(self, id_fato: int = None, id_usuario: int = None):
        self.id_fato = id_fato
        self.id_usuario = id_usuario

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioEmpresaFatoRelevanteAtivo - {str(self.id_fato)} -  {str(self.id_usuario)}>'
