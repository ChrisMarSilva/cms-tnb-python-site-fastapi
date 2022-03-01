# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class FiiFundoImobAdmin(_database.session.Base):

    __tablename__ = "TBFII_FUNDOIMOB_ADMIN"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    nome = _sql.Column('NOME', _sql.String(250), nullable=False, index=True)
    cnpj = _sql.Column('CNPJ', _sql.String(18), nullable=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, nome: str = None, cnpj: str = None, situacao: str = None):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
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
        return '<FiiFundoImobAdmin {str(self.id)} - {self.cpf}>'
