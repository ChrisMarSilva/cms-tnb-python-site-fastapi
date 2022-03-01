# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class ACAOEmpresaFinanceiroAgendaModel(_database.session.Base):

    __tablename__ = "TBEMPRESA_FINAN_AGENDA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_empresa = _sql.Column('IDEMPRESA', _sql.Integer, nullable=True, index=True)
    nome = _sql.Column('NOME', _sql.String(100), nullable=True, index=True)
    codigo = _sql.Column('CODIGO', _sql.String(20), nullable=True, index=True)
    divulgacao = _sql.Column('DIVULGACAO', _sql.String(12), nullable=True)
    horario = _sql.Column('HORARIO', _sql.String(50), nullable=True)

    def __init__(self, id: int = None, id_empresa: int = None, nome: str = None,
                 codigo: str = None, divulgacao: str = None, horario: str = None):
        self.id = id
        self.id_empresa = id_empresa
        self.nome = nome
        self.codigo = codigo
        self.divulgacao = divulgacao
        self.horario = horario

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<ACAOEmpresaFinanceiroAgenda {str(self.id)}>'

