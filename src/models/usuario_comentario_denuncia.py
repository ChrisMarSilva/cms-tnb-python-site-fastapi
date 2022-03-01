# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class UsuarioComentarioDenunciaModel(_database.session.Base):

    __tablename__ = "TBCOMENTARIO_DENUNCIA"

    id_comentario = _sql.Column('IDCOMENTARIO', _sql.Integer, _sql.ForeignKey('TBCOMENTARIO.ID'), primary_key=True, nullable=False, index=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id_comentario: int = None, id_usuario: int = None, tipo: str = None, situacao: str = None):
        self.id_comentario = id_comentario
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.situacao = situacao

    def tipo_descr(self) -> str:
        if self.tipo == 'A':
            return 'Conteúdo Impróprio com Apelo Sexual'
        elif self.tipo == 'B':
            return 'Conteúdo Violento, Repulsivo, Ofensivo ou Proibido'
        elif self.tipo == 'C':
            return 'Conteúdo Enganaso ou é uma Fraude'
        elif self.tipo == 'D':
            return 'Não Concordo com isso'
        elif self.tipo == 'E':
            return 'Conteúdo de Incitação de Ódio ou Abusivo'
        elif self.tipo == 'F':
            return 'Spam'
        elif self.tipo == 'Z':
            return 'Outra coisa'
        else:
            return 'Desconhecido'

    def situacao_descr(self) -> str:
        if self.situacao == 'A':
            return 'Em Avaliação pelo ADM'
        elif self.situacao == 'B':
            return 'Avaliado Pelo ADM'
        elif self.situacao == 'C':
            return 'Ignorado pelo ADM'
        elif self.situacao == 'D':
            return 'Cancelado pelo Usuário'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioComentarioDenuncia - {str(self.id_comentario)} - {str(self.id_usuario)}>'
