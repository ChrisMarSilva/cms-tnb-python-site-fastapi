# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioComentarioAlertaModel(_database.session.Base):

    __tablename__ = "TBCOMENTARIO_ALERTA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_comentario = _sql.Column('IDCOMENTARIO', _sql.Integer, _sql.ForeignKey('TBCOMENTARIO.ID'), nullable=False, index=True)
    id_usuario_orig = _sql.Column('IDUSUARIOORIG', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    id_usuario_dest = _sql.Column('IDUSUARIODSST', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    data_hora = _sql.Column('DTHR', _sql.String(14), nullable=False, index=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_comentario: int = None, id_usuario_orig: int = None,
                 id_usuario_dest: int = None, data_hora: str = None, tipo: str = None, situacao: str = None):
        self.id = id
        self.id_comentario = id_comentario
        self.id_usuario_orig = id_usuario_orig
        self.id_usuario_dest = id_usuario_dest
        self.data_hora = data_hora
        self.tipo = tipo
        self.situacao = situacao

    def data_hora_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def tipo_descr(self) -> str:
        if self.tipo == 'C':
            return 'Comentário'
        elif self.tipo == 'R':
            return 'Resposta'
        elif self.tipo == 'D':
            return 'Denúncia'
        else:
            return 'Desconhecido'

    def situacao_descr(self) -> str:
        if self.situacao == 'L':
            return 'Lido'
        elif self.situacao == 'P':
            return 'Pendente'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioComentarioAlerta - {str(self.id_comentario)} - {str(self.id_usuario)}>'
