# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro


class UsuarioComentarioReacao(db.Model):

    __tablename__ = "TBCOMENTARIO_REACAO"

    id_comentario = db.Column('IDCOMENTARIO', db.Integer, db.ForeignKey('TBCOMENTARIO.ID'), primary_key=True, nullable=False, index=True)
    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), primary_key=True, nullable=False, index=True)
    tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)

    def __init__(self, id_comentario: int = None, id_usuario: int = None, tipo: str = None):
        self.id_comentario = id_comentario
        self.id_usuario = id_usuario
        self.tipo = tipo

    @classmethod
    def get_all(cls):
        try:
            return cls.query.order_by(cls.id_comentario, cls.tipo, cls.id_usuario).all()
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
    def get_by_id_comentario(cls, id_comentario: int, id_usuario: int):
        try:
            return cls.query.filter_by(id_comentario=id_comentario, id_usuario=id_usuario).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_verifica(cls, id_usuario: int, id_comentario: int = None, tipo: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBCOMENTARIO_REACAO R WHERE R.IDCOMENTARIO = :IDCOMENTARIO AND R.IDUSUARIO = :IDUSUARIO """
        if tipo: query += " AND R.TIPO = :TIPO "
        params = {}
        params['IDCOMENTARIO'] = id_comentario
        params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        try:
            rows = db.session.execute(query, params).first()
            return 'S' if rows and rows[0] > 0 else 'N'
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_qtde_total(cls, id_comentario: int = None, tipo: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBCOMENTARIO_REACAO R WHERE R.IDCOMENTARIO = :IDCOMENTARIO """
        if tipo: query += " AND R.TIPO = :TIPO "
        params = {}
        params['IDCOMENTARIO'] = id_comentario
        if tipo: params['TIPO'] = tipo
        try:
            rows = db.session.execute(query, params).first()
            return rows[0] if rows and rows[0] > 0 else 0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_respostas(cls, id_comentario: int, commit: bool = True):
        try:
            query = " DELETE FROM TBCOMENTARIO_REACAO WHERE IDCOMENTARIO IN ( SELECT C.ID FROM TBCOMENTARIO C WHERE C.IDPAI = :IDPAI AND C.TIPO = 'B' ) "
            params = {'IDPAI': id_comentario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()

    @classmethod
    def excluir_comentario(cls, id_comentario: int, commit: bool = True):
        try:
            query = " DELETE FROM TBCOMENTARIO_REACAO WHERE IDCOMENTARIO = :IDCOMENTARIO "
            params = {'IDCOMENTARIO': id_comentario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = " DELETE FROM TBCOMENTARIO_REACAO WHERE IDUSUARIO = :IDUSUARIO "
            params = {'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()

    def salvar(self, commit: bool = True):
        try:
            db.session.add(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()

    def excluir(self, commit: bool = True):
        try:
            db.session.delete(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()

    def tipo_descr(self) -> str:
        if self.tipo == 'A':
            return 'Gostei'
        elif self.tipo == 'B':
            return 'Não Gostei'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioComentarioReacao {str(self.id)}>'
