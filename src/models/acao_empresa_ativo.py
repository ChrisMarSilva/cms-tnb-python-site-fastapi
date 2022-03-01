# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class ACAOEmpresaAtivoModel(_database.session.Base):

    __tablename__ = "TBEMPRESA_ATIVO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_empresa = _sql.Column('IDEMPRESA', _sql.Integer, _sql.ForeignKey('TBEMPRESA.ID'), nullable=False, index=True)
    codigo = _sql.Column('CODIGO', _sql.String(10), nullable=False, index=True)
    tipo = _sql.Column('TIPO', _sql.String(100), nullable=True)
    codigo_isin = _sql.Column('CODISIN', _sql.String(50), nullable=True, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_empresa: int = None, codigo: str = None, tipo: str = None, codigo_isin: str = None, situacao: str = None):
        self.id = id
        self.id_empresa = id_empresa
        self.codigo = codigo
        self.tipo = tipo
        self.codigo_isin = codigo_isin
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
        return '<EmpresaAtivo {str(self.id)} - {self.nome} - {self.cnpj}>'
