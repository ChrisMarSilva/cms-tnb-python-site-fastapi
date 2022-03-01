# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class UsuarioCarteira(_database.session.Base):

    __tablename__ = "TBCARTEIRA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    descricao = _sql.Column('DESCRICAO', _sql.String(255), nullable=False)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, descricao: str = None, tipo: str = None, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.descricao = descricao
        self.tipo = tipo
        self.situacao = situacao

    def tipo_descr(self) -> str:
        if self.tipo == 'D': return 'Default'
        elif self.tipo == 'P': return 'Personalizada'
        else: return 'Desconhecida'

    def situacao_descr(self) -> str:
        if self.situacao == 'A': return 'Ativa'
        elif self.situacao == 'I': return 'Inativa'
        else: return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioCarteira {str(self.id)}>'