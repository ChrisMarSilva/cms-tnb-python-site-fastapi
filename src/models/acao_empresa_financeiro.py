# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class ACAOEmpresaFinanceiro(_database.session.Base):

    __tablename__ = "TBEMPRESA_FINAN"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    cod_cvm = _sql.Column('CD_CVM', _sql.String(6), nullable=True, index=True)
    nome = _sql.Column('DENOM_CIA', _sql.String(100), nullable=True)
    cnpj = _sql.Column('CNPJ_CIA', _sql.String(20), nullable=True)
    ult_ano_refer = _sql.Column('ULT_ANO_REFER', _sql.String(4), nullable=True)
    ult_tri_refer = _sql.Column('ULT_TRI_REFER', _sql.String(6), nullable=True)

    def __init__(self, id: int = None, cod_cvm: str = None, nome: str = None,
                 cnpj: str = None, ult_ano_refer: str = None, ult_tri_refer: str = None):
        self.id = id
        self.cod_cvm = cod_cvm
        self.nome = nome
        self.cnpj = cnpj
        self.ult_ano_refer = ult_ano_refer
        self.ult_tri_refer = ult_tri_refer

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<EmpresaFinanceiro {str(self.id)}>'

