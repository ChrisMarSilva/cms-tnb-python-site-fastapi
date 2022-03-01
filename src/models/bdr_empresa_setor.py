# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class BDREmpresaSetor(_database.session.Base):

    __tablename__ = "TBBDR_EMPRESA_SETOR"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    descricao = _sql.Column('DESCRICAO', _sql.String(255), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, descricao: str = None, situacao: str = None):
        self.id = id
        self.descricao = descricao
        self.situacao = situacao

    def situacao_descr(self) -> str:
        if self.situacao == 'A': return 'Ativo'
        elif self.situacao == 'I': return 'Inativo'
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<EmpresaSetor {str(self.id)} - {self.cpf}>'
