# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.xxxxxxxxxxx import xxxxxxxxxxxModel
# from app.models.log_erro import LogErro


class UsuarioCarteiraProjecaoItemRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_projecao(cls, db: _orm.Session, id_projecao: int):
        try:
            return cls.query.filter_by(id_projecao=id_projecao).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int, id_projecao: int = None, situacao: str = None):
        query = """ SELECT ITEM.IDPROJECAO    AS IDPROJECAO, 
                           PROJ.DESCRICAO     AS DESCRICAOPROJECAO, 
                           ITEM.NUMERO        AS NUMERO,
                           ITEM.ANO           AS ANO,
                           ITEM.MES           AS MES,
                           ITEM.VLRINVESTINI  AS VLRINVESTINI,
                           ITEM.VLRINVESTMES  AS VLRINVESTMES,
                           ITEM.VLRINVESTFIM  AS VLRINVESTFIM,
                           ITEM.RENDMENSAL    AS RENDMENSAL,
                           ITEM.TIPO          AS TIPO,
                           ITEM.SITUACAO      AS SITUACAO 
                    FROM TBCARTEIRA_PROJECAO_ITEM    ITEM
                      INNER JOIN TBCARTEIRA_PROJECAO PROJ  ON ( PROJ.ID  = ITEM.IDPROJECAO )
                    WHERE PROJ.IDUSUARIO = :IDUSUARIO
                """
        if id_projecao: query += " AND ITEM.IDPROJECAO = :IDPROJECAO "
        if situacao: query += " AND ITEM.SITUACAO = :SITUACAO "
        query += " ORDER BY ITEM.IDPROJECAO, ITEM.NUMERO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_projecao: params['IDPROJECAO'] = id_projecao
        if situacao: params['SITUACAO'] = situacao

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_carteira_projecao(cls, db: _orm.Session, id_usuario: int, id_projecao: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_PROJECAO_ITEM WHERE IDPROJECAO = :IDPROJECAO AND IDPROJECAO IN (SELECT ID FROM TBCARTEIRA_PROJECAO PROJ WHERE PROJ.IDUSUARIO = :IDUSUARIO) """
            params = {'IDPROJECAO': id_projecao, 'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_PROJECAO_ITEM WHERE IDPROJECAO IN (SELECT ID FROM TBCARTEIRA_PROJECAO PROJ WHERE PROJ.IDUSUARIO = :IDUSUARIO) """
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
            if commit:
                db.commit()
        except Exception as e:
            db.rollback()
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, commit: bool = True):
        try:
            db.delete(self)
            if commit:
                db.commit()
        except Exception as e:
            db.rollback()
            raise
