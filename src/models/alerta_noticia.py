# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class AlertaNoticiaModel(_database.session.Base):

    __tablename__ = "TBALERTA_NOTICIA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    site = _sql.Column('SITE', _sql.String(50), nullable=False)
    dthr_registro = _sql.Column('DTHRREGISTRO', _sql.String(14), nullable=False)
    tipo = _sql.Column('TIPO', _sql.String(255), nullable=False)
    titulo = _sql.Column('TITULO', _sql.String(4000), nullable=False)
    link = _sql.Column('LINK', _sql.String(500), nullable=False)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, site: str = None, dthr_registro: str = None, tipo: str = None,
                 titulo: str = None,  link: str = None, situacao: str = None):
        self.id = id
        self.site = site
        self.dthr_registro = dthr_registro
        self.tipo = tipo
        self.titulo = titulo
        self.link = link
        self.situacao = situacao

    def dthr_registro_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.dthr_registro, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def situacao_descr(self) -> str:
        if self.situacao == 'P':
            return 'Pendente'
        elif self.situacao == 'G':
            return 'Gerado'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<AlertaNoticia {str(self.id)}>'
