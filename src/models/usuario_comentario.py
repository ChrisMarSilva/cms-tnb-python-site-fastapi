# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioComentarioModel(_database.session.Base):

    __tablename__ = "TBCOMENTARIO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_pai = _sql.Column('IDPAI', _sql.Integer, _sql.ForeignKey('TBCOMENTARIO.ID'), nullable=True, index=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    texto = _sql.Column('TEXTO', _sql.Text(), nullable=False)
    data_hora = _sql.Column('DATAHORA', _sql.String(14), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_pai: int = None, id_usuario: int = None, tipo: str = None, texto: str = None,
                 data_hora: str = None, situacao: str = None):
        self.id = id
        self.id_pai = id_pai
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.texto = texto
        self.data_hora = data_hora
        self.situacao = situacao

    def data_hora_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def tipo_descr(self) -> str:
        if self.tipo == 'A':
            return 'Principal'
        elif self.tipo == 'B':
            return 'Resposta'
        elif self.tipo == 'C':
            return 'Réplica'
        else:
            return 'Desconhecido'

    def situacao_descr(self) -> str:
        if self.situacao == 'A':
            return 'Ativa'
        elif self.situacao == 'D':
            return 'Denunciado'
        elif self.situacao == 'E':
            return 'Excluído'
        elif self.situacao == 'I':
            return 'Inativa'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioComentario {str(self.id)}>'
