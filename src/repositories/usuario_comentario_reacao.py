# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_comentario_reacao import UsuarioComentarioReacaoModel
# from app.models.log_erro import LogErro


class UsuarioComentarioReacaoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioComentarioReacaoModel).order_by(UsuarioComentarioReacaoModel.id_comentario, UsuarioComentarioReacaoModel.tipo, UsuarioComentarioReacaoModel.id_usuario).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioComentarioReacaoModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id_comentario(cls, db: _orm.Session, id_comentario: int, id_usuario: int):
        try:
            return db.query(UsuarioComentarioReacaoModel).filter_by(id_comentario=id_comentario, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_verifica(cls, db: _orm.Session, id_usuario: int, id_comentario: int = None, tipo: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBCOMENTARIO_REACAO R WHERE R.IDCOMENTARIO = :IDCOMENTARIO AND R.IDUSUARIO = :IDUSUARIO """
        if tipo: query += " AND R.TIPO = :TIPO "
        params = {}
        params['IDCOMENTARIO'] = id_comentario
        params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        try:
            rows = db.execute(query, params).first()
            return 'S' if rows and rows[0] > 0 else 'N'
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_qtde_total(cls, db: _orm.Session, id_comentario: int = None, tipo: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBCOMENTARIO_REACAO R WHERE R.IDCOMENTARIO = :IDCOMENTARIO """
        if tipo: query += " AND R.TIPO = :TIPO "
        params = {}
        params['IDCOMENTARIO'] = id_comentario
        if tipo: params['TIPO'] = tipo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_respostas(cls, db: _orm.Session, id_comentario: int, commit: bool = True):
        try:
            query = " DELETE FROM TBCOMENTARIO_REACAO WHERE IDCOMENTARIO IN ( SELECT C.ID FROM TBCOMENTARIO C WHERE C.IDPAI = :IDPAI AND C.TIPO = 'B' ) "
            params = {'IDPAI': id_comentario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()

    @classmethod
    async def excluir_comentario(cls, db: _orm.Session, id_comentario: int, commit: bool = True):
        try:
            query = " DELETE FROM TBCOMENTARIO_REACAO WHERE IDCOMENTARIO = :IDCOMENTARIO "
            params = {'IDCOMENTARIO': id_comentario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = " DELETE FROM TBCOMENTARIO_REACAO WHERE IDUSUARIO = :IDUSUARIO "
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioComentarioReacaoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioComentarioReacaoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise()
