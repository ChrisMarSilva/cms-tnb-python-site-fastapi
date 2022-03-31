# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro


class UsuarioCarteiraProjecaoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.order_by(cls, db: _orm.id).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, situacao='A').order_by(cls, db: _orm.descricao).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return cls.query.filter_by(id=id, situacao='A').first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id_and_usuario(cls, db: _orm.Session, id_usuario: int, id: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, id=id, situacao='A').first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_descricao(cls, db: _orm.Session, id_usuario: int, descricao: str):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, descricao=descricao, situacao='A').first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT C.ID, C.DESCRICAO, C.SITUACAO FROM TBCARTEIRA_PROJECAO C WHERE C.IDUSUARIO = :IDUSUARIO AND C.SITUACAO = 'A' ORDER BY C.DESCRICAO """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int, id: int):
        query = """ SELECT C.ID, C.DESCRICAO, C.SITUACAO FROM TBCARTEIRA_PROJECAO C WHERE C.IDUSUARIO = :IDUSUARIO AND C.ID = :ID AND C.SITUACAO = 'A' """
        params = {'IDUSUARIO': id_usuario, 'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_descricao(cls, db: _orm.Session, id_usuario: int, descricao: str):
        query = """ SELECT C.ID, C.DESCRICAO, C.SITUACAO FROM TBCARTEIRA_PROJECAO C WHERE C.IDUSUARIO = :IDUSUARIO AND C.DESCRICAO = :DESCRICAO AND C.SITUACAO = 'A' """
        params = {'IDUSUARIO': id_usuario, 'DESCRICAO': descricao}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT C.ID, C.DESCRICAO FROM TBCARTEIRA_PROJECAO C WHERE C.IDUSUARIO = :IDUSUARIO AND C.SITUACAO = 'A' ORDER BY C.DESCRICAO """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_PROJECAO WHERE IDUSUARIO = :IDUSUARIO """
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, commit: bool = True):
        try:
            db.add(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, commit: bool = True):
        try:
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
