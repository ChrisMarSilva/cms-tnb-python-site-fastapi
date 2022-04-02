# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_apuracao import UsuarioApuracaoModel
# # from app.models.log_erro import LogErro


class UsuarioApuracaoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session, id_usuario: int, tipo: str = None, categoria: str = None, ano_mes: str = None):
        filters = []
        filters.append(UsuarioApuracaoModel.id_usuario == id_usuario)
        if tipo: filters.append(UsuarioApuracaoModel.tipo == tipo)
        if categoria: filters.append(UsuarioApuracaoModel.categoria == categoria)
        if ano_mes: filters.append(UsuarioApuracaoModel.ano_mes == ano_mes)
        try:
            return db.query(UsuarioApuracaoModel).filter(*filters).order_by(UsuarioApuracaoModel.ano_mes, cls.tipo, cls.categoria).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(UsuarioApuracaoModel).filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioApuracaoModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_menor_ano(cls, db: _orm.Session, id_usuario: int = None):
        try:
            return db.query(db.func.min(UsuarioApuracaoModel.ano_mes)).filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_maior_ano(cls, db: _orm.Session, id_usuario: int = None):
        try:
            return db.query(db.func.max(UsuarioApuracaoModel.ano_mes)).filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int, tipo: str = None, categoria: str = None, ano_mes: str = None):
        query = """ SELECT AP.ID, AP.TIPO, AP.CATEGORIA, AP.MESANO, AP.VALOR, AP.SITUACAO FROM TBAPURACAO AP WHERE AP.IDUSUARIO = :IDUSUARIO """
        if tipo: query += " AND AP.TIPO = :TIPO "
        if categoria: query += " AND AP.CATEGORIA = :CATEGORIA "
        if ano_mes: query += " AND AP.MESANO = :MESANO "
        query += " ORDER BY AP.MESANO, AP.TIPO, AP.CATEGORIA "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        if categoria: params['CATEGORIA'] = categoria
        if ano_mes: params['MESANO'] = ano_mes
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int, id: int):
        query = """ SELECT AP.ID, AP.TIPO, AP.CATEGORIA, AP.MESANO, AP.VALOR, AP.SITUACAO FROM TBAPURACAO AP WHERE AP.IDUSUARIO = :IDUSUARIO AND AP.ID = :ID """
        params = {'IDUSUARIO': id_usuario, 'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_menor_ano(cls, db: _orm.Session, id_usuario: int, tipo: str = None, categoria: str = None):
        query = """ SELECT SUBSTRING(MIN(AP.MESANO), 1, 4) AS MENORANO FROM TBAPURACAO AP WHERE AP.IDUSUARIO = :IDUSUARIO """
        if tipo: query += " AND AP.TIPO = :TIPO  "
        if categoria: query += " AND AP.CATEGORIA = :CATEGORIA "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        if categoria: params['CATEGORIA'] = categoria
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_ano(cls, db: _orm.Session, id_usuario: int, tipo: str = None, categoria: str = None, ano: str = None, commit: bool = True):
        try:
            query = "DELETE FROM TBAPURACAO WHERE IDUSUARIO = :IDUSUARIO "
            if tipo: query += " AND TIPO = :TIPO  "
            if categoria: query += " AND CATEGORIA = :CATEGORIA "
            if ano: query += " AND MESANO >= :JANANO AND MESANO <= :DEZANO "

            params = {}
            params['IDUSUARIO'] = id_usuario
            if tipo: params['TIPO'] = tipo
            if categoria: params['CATEGORIA'] = categoria
            if ano:
                params['JANANO'] = ano + '01'
                params['DEZANO'] = ano + '12'

            db.execute(query, params)
            if commit: db.commit()

        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBAPURACAO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioApuracaoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioApuracaoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
