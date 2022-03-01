# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioCeiModel(_database.session.Base):

    __tablename__ = "TBCEI"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    cpf = _sql.Column('CPF', _sql.String(50), nullable=True)
    senha = _sql.Column('SENHA', _sql.String(150), nullable=True)
    dthr_registro = _sql.Column('DTHRREGISTRO', _sql.String(14), nullable=False)
    dthr_alteracao = _sql.Column('DTHRALTERACAO', _sql.String(14), nullable=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, cpf: str = None, senha: str = None,
                 dthr_registro: str = None, dthr_alteracao: str = None, tipo: str = None,
                 situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.cpf = cpf
        self.senha = senha
        self.dthr_registro = dthr_registro
        self.dthr_alteracao = dthr_alteracao
        self.tipo = tipo
        self.situacao = situacao

    def dthr_registro_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.dthr_registro, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def dthr_alteracao_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.dthr_alteracao, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def tipo_descr(self) -> str:
        if self.tipo == 'A':
            return 'Ativo'
        elif self.tipo == 'I':
            return 'Inativo'
        else:
            return 'Desconhecido'

    def situacao_descr(self) -> str:
        if self.situacao == 'C':
            return 'Importar'  # C- Carregar
        elif self.situacao == 'I':
            return 'Integrar'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioCei {str(self.id)} - {self.cpf}>'
