# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioCei(db.Model):

    __tablename__ = "TBCEI"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    cpf = db.Column('CPF', db.String(50), nullable=True)
    senha = db.Column('SENHA', db.String(150), nullable=True)
    dthr_registro = db.Column('DTHRREGISTRO', db.String(14), nullable=False)
    dthr_alteracao = db.Column('DTHRALTERACAO', db.String(14), nullable=True)
    tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

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

    @classmethod
    def get_all(cls):
        try:
            return cls.query.all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_id(cls, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_usuario(cls, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls):
        query = """ SELECT C.ID, C.IDUSUARIO, C.CPF, C.SENHA, C.DTHRREGISTRO, C.DTHRALTERACAO, C.TIPO, C.SITUACAO FROM TBCEI C """
        params = {}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id: int = None):
        query = """ SELECT C.ID, C.IDUSUARIO, C.CPF, C.SENHA, C.DTHRREGISTRO, C.DTHRALTERACAO, C.TIPO, C.SITUACAO FROM TBCEI C WHERE C.ID = :ID """
        params = {'ID': id}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id_usuario(cls, id_usuario: int = None):
        query = """ SELECT C.ID, C.IDUSUARIO, C.CPF, C.SENHA, C.DTHRREGISTRO, C.DTHRALTERACAO, C.TIPO, C.SITUACAO FROM TBCEI C WHERE C.IDUSUARIO = :IDUSUARIO """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBCEI WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def salvar(self, commit: bool = True):
        try:
            db.session.add(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def excluir(self, commit: bool = True):
        try:
            db.session.delete(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

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
