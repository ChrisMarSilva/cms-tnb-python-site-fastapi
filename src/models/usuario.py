# -*- coding: utf-8 -*-
import hashlib
import sqlalchemy as _sql
# import sqlalchemy.orm as _orm
import src.database as _database
# from src.models.usuario_hash import UsuarioHash
# from src.models.usuario_log import UsuarioLog
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioModel(_database.session.Base):
    __tablename__ = "TBUSUARIO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    nome = _sql.Column('NOME', _sql.String(150), nullable=False)
    email = _sql.Column('EMAIL', _sql.String(250), nullable=False, unique=True, index=True)
    senha = _sql.Column('SENHA', _sql.String(150), nullable=False)
    data_registro = _sql.Column('DTREGISTRO', _sql.String(8), nullable=False)
    tentatia = _sql.Column('TENTATIVA', _sql.Integer)
    foto = _sql.Column('FOTO', _sql.String(255))
    chat_id = _sql.Column('CHATID', _sql.String(50))
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)
    # email_hash = _orm.relationship('UsuarioHashModel', lazy=True, backref='TBUSUARIO', uselist=False)
    # logs = _orm.relationship('UsuarioLogModel', lazy=True, backref='TBUSUARIO', uselist=True)

    def __init__(self, id: int = None, nome: str = None, email: str = None, senha: str = None, data_registro: str = None, tentatia: int = None, foto: str = None, chat_id: str = None, tipo: str = None, situacao: str = None, active=True):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_registro = data_registro
        self.tentatia = tentatia
        self.foto = foto
        self.chat_id = chat_id
        self.tipo = tipo
        self.situacao = situacao
        self.active = active

    def senha_sha256(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

    def validar_senha(self, senha):
        return self.senha == hashlib.sha256(senha.encode()).hexdigest()

    def criptografar_hash(self, email):
        import base64
        key = '#Chrs123-juju78¨&*%$=='
        message = email + key
        message = base64.b64encode(message.encode())
        message = message.decode()
        return message

    def descriptografar_hash(self, message):
        import base64
        key = '#C5121213-juju78¨&*%$=='
        message = base64.b64decode(message)
        message = message.decode()
        message = str(message).replace(key, '')
        return message

    def data_registro_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_registro, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def tipo_descr(self) -> str:
        return self.descricao_tipo(tipo=self.tipo)

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def descricao_tipo(cls, tipo: str) -> str:
        if tipo == 'A':
            return 'Adminstrador'
        elif tipo == 'I':
            return 'Investidor'
        else:
            return 'Desconhecido'

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':
            return 'Ativo'
        elif situacao == 'B':
            return 'Aguardando Confirmação'
        elif situacao == 'I':
            return 'Inativo'
        elif situacao == 'X':
            return 'Bloqueado'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return "<UsuarioModel(" \
               f"id={self.id}, " \
               f"email=\"{self.email}\", " \
               f"hashed_password=\"{self.hashed_password}\", " \
               f"is_active={self.is_active}" \
               ")>"
