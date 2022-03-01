# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class BDREmpresaModel(_database.session.Base):

    __tablename__ = "TBBDR_EMPRESA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_setor = _sql.Column('IDSETOR', _sql.Integer, nullable=True, index=True)
    id_subsetor = _sql.Column('IDSUBSETOR', _sql.Integer, nullable=True, index=True)
    id_segmento = _sql.Column('IDSEGMENTO', _sql.Integer, nullable=True, index=True)
    nome = _sql.Column('NOME', _sql.String(100), nullable=False, index=True)
    razao_social = _sql.Column('RAZAOSOCIAL', _sql.String(255), nullable=False, index=True)
    cnpj = _sql.Column('CNPJ', _sql.String(18), nullable=True)
    atividade = _sql.Column('ATIVIDADE', _sql.String(255), nullable=True)
    cod_cvm = _sql.Column('CODCVM', _sql.String(50), nullable=True)
    sit_cvm = _sql.Column('SITCVM', _sql.String(255), nullable=True)
    codigo = _sql.Column('CODIGO', _sql.String(10), nullable=False, index=True)
    codigo_isin = _sql.Column('CODISIN', _sql.String(50), nullable=True)
    tipo = _sql.Column('TIPO', _sql.String(100), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_setor: int = None, id_subsetor: int = None, id_segmento: int = None, nome: str = None, razao_social: str = None, cnpj: str = None, atividade: str = None, cod_cvm: str = None, sit_cvm: str = None, codigo: str = None, codigo_isin: str = None, tipo: str = None, situacao: str = None):
        self.id = id
        self.id_setor = id_setor
        self.id_subsetor = id_subsetor
        self.id_segmento = id_segmento
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.atividade = atividade
        self.cod_cvm = cod_cvm
        self.sit_cvm = sit_cvm
        self.codigo = codigo
        self.codigo_isin = codigo_isin
        self.tipo = tipo
        self.situacao = situacao

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':return 'Ativo'
        elif situacao == 'I': return 'Inativo'
        elif situacao == 'E': return 'Encerrado'
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<Empresa {str(self.id)} - {self.nome} - {self.razao_social}>'
