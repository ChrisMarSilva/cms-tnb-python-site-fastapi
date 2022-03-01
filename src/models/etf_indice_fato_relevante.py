# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class ETFIndiceFatoRelevante(_database.session.Base):

    __tablename__ = "TBETF_FATORELEVANTE"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_indice = _sql.Column('IDINDICE', _sql.Integer, nullable=True, index=True)
    nm_indice = _sql.Column('NMINDICE', _sql.String(250), nullable=True, index=True)
    data_env = _sql.Column('DATA_ENV', _sql.String(14), nullable=False)
    data_ref = _sql.Column('DATA_REF', _sql.String(8), nullable=False, index=True)
    protocolo = _sql.Column('PROTOCOLO', _sql.String(50), nullable=False)
    link = _sql.Column('LINK', _sql.String(250), nullable=False)
    assunto = _sql.Column('ASSUNTO', _sql.String(4000), nullable=True)
    conteudo = _sql.Column('CONTEUDO', _sql.Text(), nullable=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_indice: int = None, nm_indice: str = None, data_env: str = None,
                 data_ref: str = None, protocolo: str = None, link: str = None, assunto: str = None,
                 conteudo: str = None, situacao: str = None):
        self.id = id
        self.id_indice = id_indice
        self.nm_indice = nm_indice
        self.data_env = data_env
        self.data_ref = data_ref
        self.protocolo = protocolo
        self.link = link
        self.assunto = assunto
        self.conteudo = conteudo
        self.situacao = situacao

    def data_env_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_env, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_ref_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ref, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_env_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_env, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def data_ref_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ref, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def situacao_descr(self) -> str:
        if self.situacao == 'A':
            return 'Ativo'
        elif self.situacao == 'B':
            return 'Pendente Baixar PDF'
        elif self.situacao == 'C':
            return 'Erro ao Baixar PDF'
        elif self.situacao == 'D':
            return 'Pendente Processar PDF'
        elif self.situacao == 'E':
            return 'Erro ao Processar PDF'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<ETFIndiceFatoRelevante {str(self.id)} - {self.nome} - {self.cnpj}>'
