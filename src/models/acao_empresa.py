# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class ACAOEmpresa(_database.session.Base):

    __tablename__ = "TBEMPRESA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_setor = _sql.Column('IDSETOR', _sql.Integer, nullable=True, index=True)
    id_subsetor = _sql.Column('IDSUBSETOR', _sql.Integer, nullable=True, index=True)
    id_segmento = _sql.Column('IDSEGMENTO', _sql.Integer, nullable=True, index=True)
    nome = _sql.Column('NOME', _sql.String(100), nullable=False, index=True)
    nome_resumido = _sql.Column('NOMRESUMIDO', _sql.String(100), nullable=True)
    razao_social = _sql.Column('RAZAOSOCIAL', _sql.String(255), nullable=False, index=True)
    cnpj = _sql.Column('CNPJ', _sql.String(18), nullable=True)
    atividade = _sql.Column('ATIVIDADE', _sql.String(255), nullable=True)
    cod_cvm = _sql.Column('CODCVM', _sql.String(50), nullable=True)
    sit_cvm = _sql.Column('SITCVM', _sql.String(255), nullable=True)
    slug = _sql.Column('SLUG', _sql.String(20), nullable=True)
    site = _sql.Column('SITE', _sql.String(250), nullable=True)
    tipo_mercado = _sql.Column('TIPO_MERCADO', _sql.String(100), nullable=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_setor: int = None, id_subsetor: int = None, id_segmento: int = None,
                 nome: str = None, nome_resumido: str = None, razao_social: str = None, cnpj: str = None,
                 atividade: str = None, cod_cvm: str = None, sit_cvm: str = None, slug: str = None, site: str = None,
                 tipo_mercado: str = None, situacao: str = None):
        self.id = id
        self.id_setor = id_setor
        self.id_subsetor = id_subsetor
        self.id_segmento = id_segmento
        self.nome = nome
        self.nome_resumido = nome_resumido
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.atividade = atividade
        self.cod_cvm = cod_cvm
        self.sit_cvm = sit_cvm
        self.slug = slug
        self.site = site
        self.tipo_mercado = tipo_mercado
        self.situacao = situacao

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
        return '<Empresa {str(self.id)} - {self.nome} - {self.razao_social}>'
