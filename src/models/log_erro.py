# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class LogErroModel(_database.session.Base):

    __tablename__ = "TBLOGERRO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True, nullable=False)
    data_hora = _sql.Column('DATAHORA', _sql.String(20), nullable=False, index=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=True)
    arquivo = _sql.Column('ARQUIVO', _sql.String(250), nullable=True)
    linha = _sql.Column('LINHA', _sql.Integer, nullable=True)
    codigo = _sql.Column('CODIGO', _sql.Integer, nullable=True)
    texto = _sql.Column('TEXTO', _sql.Text(), nullable=False)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, data_hora: str = None, id_usuario: int = None, arquivo: str = None,
                 linha: int = None, codigo: int = None, texto: str = None, situacao: str = None):
        self.id = id
        self.data_hora = data_hora
        self.id_usuario = id_usuario
        self.arquivo = arquivo
        self.linha = linha
        self.codigo = codigo
        self.texto = texto
        self.situacao = situacao

    def data_hora_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def situacao_descr(self) -> str:
        if self.situacao == 'L':
            return 'Lido'
        elif self.situacao == 'N':
            return 'Não Lido'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<LogErro - IdUser: {str(self.id_usuario)}>'
