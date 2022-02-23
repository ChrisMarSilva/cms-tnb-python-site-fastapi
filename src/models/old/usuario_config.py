# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro


class UsuarioConfig(db.Model):

    __tablename__ = "TBUSUARIO_CONFIG"

    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)
    tipo = db.Column('TIPO', db.String(50), primary_key=True, nullable=False, index=True)
    valor = db.Column('VALOR', db.String(250), nullable=False)

    def __init__(self, id_usuario: int = None, tipo: str = None, valor: str = None):
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.valor = valor

    @classmethod
    def get_all(cls):
        try:
            return cls.query.all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_all_by_iusuario(cls, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_tipo(cls, id_usuario: int, tipo: str):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, tipo=tipo).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int = None):
        query = """ SELECT C.TIPO, C.VALOR FROM TBUSUARIO_CONFIG C WHERE C.IDUSUARIO = :IDUSUARIO ORDER BY C.TIPO """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_tipo(cls, tipo: str = None):
        query = """ SELECT C.TIPO, C.VALOR FROM TBUSUARIO_CONFIG C WHERE C.IDUSUARIO = :IDUSUARIO AND C.TIPO = :TIPO """
        params = {'TIPO': tipo}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBUSUARIO_CONFIG WHERE IDUSUARIO = :IDUSUARIO"
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

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioConfig - IdUser: {str(self.id_usuario)} - Tp: {self.tipo} - Vlr: {self.valor}>'
