# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro


class UsuarioACAOEmpresaFatoRelevanteAtivo(db.Model):

    __tablename__ = "TBEMPRESA_FATORELEVANTE_ATIVO"

    id_fato = db.Column('IDFATO', db.Integer, db.ForeignKey('TBEMPRESA_FATORELEVANTE.ID'), primary_key=True, nullable=False, index=True)
    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)

    def __init__(self, id_fato: int = None, id_usuario: int = None):
        self.id_fato = id_fato
        self.id_usuario = id_usuario

    @classmethod
    def get_all(cls):
        try:
            return cls.query.all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_fato_and_usuario(cls, id_usuario: int, id_fato: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, id_fato=id_fato).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_by_usuario(cls, id_usuario: int, commit: bool = True):
        try:
            cls.query.filter_by(id_usuario=id_usuario).delete()
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM " + cls.__tablename__ + " WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def salvar(self, commit: bool = True):
        try:
            if self.get_by_fato_and_usuario(id_fato=self.id_fato, id_usuario=self.id_usuario): return False
            db.session.add(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            #raise

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
        return '<UsuarioEmpresaFatoRelevanteAtivo - {str(self.id_fato)} -  {str(self.id_usuario)}>'
