# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class CorretoraLista(_database.session.Base):

    __tablename__ = "TBCORRETORA_LISTA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    nome = _sql.Column('NOME', _sql.String(100), nullable=False, index=True)
    cnpj = _sql.Column('CNPJ', _sql.String(14), nullable=False, index=True)
    importar_nota = _sql.Column('IMPORTAR_NOTA', _sql.String(1), nullable=False)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, nome: str = None, cnpj: str = None, importar_nota: str = None, situacao: str = None):
        self.id = id
        self.nome = nome
        self.cnpj = cnpj
        self.importar_nota = importar_nota
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
        return '<Corretora {str(self.id)} - {self.nome} - {self.cnpj}>'
