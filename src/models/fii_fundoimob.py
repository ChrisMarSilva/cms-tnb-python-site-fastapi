# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class FiiFundoImob(_database.session.Base):

    __tablename__ = "TBFII_FUNDOIMOB"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True, index=True)
    id_tipo = _sql.Column('IDFIITIPO', _sql.Integer, nullable=True, index=True)
    id_admin = _sql.Column('IDFIIADMIN', _sql.Integer, nullable=True, index=True)
    nome = _sql.Column('NOME', _sql.String(100), nullable=False, index=True)
    razao_social = _sql.Column('RAZAOSOCIAL', _sql.String(255), nullable=False, index=True)
    cnpj = _sql.Column('CNPJ', _sql.String(18), nullable=False)
    codigo = _sql.Column('CODIGO', _sql.String(10), nullable=False, index=True)
    codigo_isin = _sql.Column('CODISIN', _sql.String(50), nullable=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_tipo: int = None, id_admin: int = None, nome: str = None,
                 razao_social: str = None, cnpj: str = None, codigo: str = None, codigo_isin: str = None,
                 situacao: str = None):
        self.id = id
        self.id_tipo = id_tipo
        self.id_admin = id_admin
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.codigo = codigo
        self.codigo_isin = codigo_isin
        self.situacao = situacao

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':
            return 'Ativo'
        elif situacao == 'I':
            return 'Inativo'
        elif situacao == 'E':
            return 'Encerrado'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<FiiFundoImob {str(self.id)} - {self.nome} - {self.razao_social}>'
