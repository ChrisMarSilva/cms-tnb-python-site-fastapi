# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class UsuarioRadarGrupo(_database.session.Base):

    __tablename__ = "TBUSUARIO_ACOMP_GRUPO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    descricao = _sql.Column('DESCRICAO', _sql.String(255), nullable=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, descricao: str = None, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.descricao = descricao
        self.situacao = situacao

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
        return '<UsuarioRadarGrupo {str(self.id)}>'
