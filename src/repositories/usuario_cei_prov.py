# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.xxxxxxxxxxx import xxxxxxxxxxxModel
# from app.models.log_erro import LogErro


class UsuarioCeiProvRepository:

    @classmethod
    async def tabela_existe(cls, db: _orm.Session, id_usuario: int):
        query = " SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = :TABLE_NAME"
        params = {'TABLE_NAME': cls.tablename + str(id_usuario)}
        return db.execute(query, params).first()

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, dt_ini: str = None, dt_fim: str = None, codigo: str = None, categoria: str = None):

        if not cls.tabela_existe(id_usuario=id_usuario):
            return []

        query = """ SELECT CP.ID, CP.IDUSUARIO, CP.CATEGORIA, CP.CODIGO, CP.DATA_PAGTO, CP.TIPO, CP.QUANT, CP.TOTAL_BRUTO, CP.TOTAL_LIQUIDO, CP.CORRET_ID, CP.CORRET_NOME, CP.CORRET_CONTA, CP.SITUACAO
                    FROM """ + cls.tablename + str(id_usuario) + """ CP 
                    WHERE CP.IDUSUARIO = :IDUSUARIO
                """

        if dt_ini: query += " AND CP.DATA_PAGTO >= :DATAINICIO "
        if dt_fim: query += " AND CP.DATA_PAGTO <= :DATAFIM "
        if codigo: query += " AND CP.CODIGO = :CODIGO "
        if categoria: query += " AND CP.CATEGORIA = :CATEGORIA "

        query += " ORDER BY CP.ID "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim
        if codigo: params['CODIGO'] = codigo
        if categoria: params['CATEGORIA'] = categoria
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id_prov(cls, db: _orm.Session, id_usuario: int = None, id: int = None):

        if not cls.tabela_existe(id_usuario=id_usuario):
            return []

        query = """ SELECT CP.ID, CP.IDUSUARIO, CP.CATEGORIA, CP.CODIGO, CP.DATA_PAGTO, CP.TIPO, CP.QUANT, CP.TOTAL_BRUTO, CP.TOTAL_LIQUIDO, CP.CORRET_ID, CP.CORRET_NOME, CP.CORRET_CONTA, CP.SITUACAO 
                    FROM """ + cls.tablename + str(id_usuario) + """ CP 
                    WHERE CP.ID = :ID
                """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_codigo(cls, db: _orm.Session, id_usuario: int = None):

        if not cls.tabela_existe(id_usuario=id_usuario):
            return []

        query = """ SELECT DISTINCT CP.CODIGO FROM """ + cls.tablename + str(id_usuario) + """ CP ORDER BY CP.CODIGO """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def atualizar_situacao(cls, db: _orm.Session, id_usuario: int = None, id: int = None, situacao: str = None, commit: bool = True):
        try:
            if not cls.tabela_existe(id_usuario=id_usuario):
                return True
            query = """ UPDATE """ + cls.tablename + str(id_usuario) + """ SET SITUACAO = :SITUACAO WHERE ID = :ID """
            params = {'ID': id, 'SITUACAO': situacao}
            db.execute(query, params)
            if commit: db.commit()
            return True
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def resetar_situacao(cls, db: _orm.Session, id_usuario: int = None, commit: bool = True):
        try:
            if not cls.tabela_existe(id_usuario=id_usuario):
                return True
            query = """ UPDATE """ + cls.tablename + str(id_usuario) + """ SET SITUACAO = 'I' WHERE IDUSUARIO = :IDUSUARIO """
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
            return True
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
