# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str


class UsuarioCorretora(_database.session.Base):

    __tablename__ = "TBCORRETORA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    id_corretora_lista = _sql.Column('IDCORRETORALISTA', _sql.Integer, nullable=False)
    nome = _sql.Column('NOME', _sql.String(100), nullable=False)
    cnpj = _sql.Column('CNPJ', _sql.String(14), nullable=False)
    valor = _sql.Column('VLRCORRETAGEM', _sql.Float(17, 2), nullable=False)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, id_corretora_lista: int = None, nome: str = None, cnpj: str = None, valor: float = 0.0, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_corretora_lista = id_corretora_lista
        self.nome = nome
        self.cnpj = cnpj
        self.valor = valor
        self.situacao = situacao

    def valor_format(self) -> str:
        return decimal_to_str(valor=self.valor)

    def situacao_descr(self) -> str:
        if self.situacao == 'A':
            return 'Ativa'
        elif self.situacao == 'I':
            return 'Inativa'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<Corretora {str(self.id)} - {self.nome} - {self.cnpj}>'
