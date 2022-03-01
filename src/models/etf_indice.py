# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class ETFIndice(_database.session.Base):

    __tablename__ = "TBETF_INDICE"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True, index=True)
    razao_social = _sql.Column('RAZAOSOCIAL', _sql.String(255), nullable=False, index=True)
    fundo = _sql.Column('FUNDO', _sql.String(100), nullable=False)
    indice = _sql.Column('INDICE', _sql.String(100), nullable=False, index=True)
    nome = _sql.Column('NOME', _sql.String(100), nullable=False, index=True)
    cnpj = _sql.Column('CNPJ', _sql.String(18), nullable=False)
    codigo = _sql.Column('CODIGO', _sql.String(10), nullable=False, index=True)
    codigo_isin = _sql.Column('CODISIN', _sql.String(50), nullable=True, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, razao_social: str = None, fundo: str = None, indice: str = None,
                 nome: str = None, cnpj: str = None, codigo: str = None, codigo_isin: str = None, situacao: str = None):
        self.id = id
        self.razao_social = razao_social
        self.fundo = fundo
        self.indice = indice
        self.nome = nome
        self.cnpj = cnpj
        self.codigo = codigo
        self.codigo_isin = codigo_isin
        self.situacao = situacao

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A': return 'Ativo'
        elif situacao == 'I': return 'Inativo'
        elif situacao == 'E': return 'Encerrado'
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<ETFIndice {str(self.id)} - {self.nome} - {self.razao_social}>'
