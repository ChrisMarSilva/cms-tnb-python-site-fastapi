# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class UsuarioRadarFiiModel(_database.session.Base):

    __tablename__ = "TBUSUARIO_ACOMP_FUNDO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_grupo = _sql.Column('IDGRUPO', _sql.Integer, _sql.ForeignKey('TBUSUARIO_ACOMP_GRUPO.ID'), nullable=False, index=True)
    id_fundo = _sql.Column('IDFUNDO', _sql.Integer, _sql.ForeignKey('TBFII_FUNDOIMOB.ID'), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_grupo: int = None, id_fundo: int = None, situacao: str = None):
        self.id = id
        self.id_grupo = id_grupo
        self.id_fundo = id_fundo
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
        return '<UsuarioRadarFundoImob {str(self.id)}>'
