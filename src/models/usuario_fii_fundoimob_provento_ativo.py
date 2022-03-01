# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class UsuarioFiiFundoImobProventoAtivo(_database.session.Base):

    __tablename__ = "TBFII_FUNDOIMOB_PROVENTO_ATIVO"

    id_provento = _sql.Column('IDEMPRPROV', _sql.Integer, _sql.ForeignKey('TBFII_FUNDOIMOB_PROVENTO.ID'), primary_key=True, nullable=False, index=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)
    id_fundo = _sql.Column('IDFUNDO', _sql.Integer, _sql.ForeignKey('TBFII_FUNDOIMOB.ID'), nullable=False, index=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    data_ex = _sql.Column('DATAEX', _sql.String(1), nullable=False, index=True)

    def __init__(self, id_provento: int = None, id_usuario: int = None, id_fundo: int = None, tipo: str = None,
                 data_ex: str = None):
        self.id_provento = id_provento
        self.id_usuario = id_usuario
        self.id_fundo = id_fundo
        self.tipo = tipo
        self.data_ex = data_ex

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioFiiFundoImobProventoAtivo - {str(self.id_fato)} -  {str(self.id_usuario)}>'
