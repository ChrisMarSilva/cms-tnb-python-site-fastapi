# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_comentario_alerta import UsuarioComentarioAlertaModel
# from app.models.log_erro import LogErro
from src.util.util_datahora import pegar_data_hora_atual


class UsuarioComentarioAlertaRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioComentarioAlertaModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioComentarioAlertaModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None, situacao: str = None):

        query = """ SELECT  ALRT.ID,
                            ALRT.IDCOMENTARIO,
                            ALRT.IDUSUARIOORIG AS IDUSUARIOORIGEM,
                            UO.NOME            AS NMUSUARIOORIGEM,
                            UO.FOTO            AS FTUSUARIOORIGEM,
                            ALRT.IDUSUARIODSST AS IDUSUARIODESTINO,
                            UD.NOME            AS NMUSUARIODESTINO,
                            ALRT.DTHR          AS DTHRALERTA,
                            ALRT.TIPO          AS TIPOALERTA,
                            ALRT.SITUACAO
                    FROM TBCOMENTARIO_ALERTA ALRT
                        JOIN TBUSUARIO UO ON ( UO.ID = ALRT.IDUSUARIOORIG )
                        JOIN TBUSUARIO UD ON ( UD.ID = ALRT.IDUSUARIODSST )
                    WHERE ALRT.IDUSUARIODSST = :IDUSUARIODSST
                """
        if tipo: query += " AND ALRT.TIPO = :TIPO "
        if situacao: query += " AND ALRT.SITUACAO = :SITUACAO "
        query += " ORDER BY ALRT.DTHR DESC, ALRT.ID "

        params = {}
        params['IDUSUARIODSST'] = id_usuario
        if tipo: params['TIPO'] = tipo
        if situacao: params['SITUACAO'] = situacao
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar_todos(cls, db: _orm.Session, id_usuario: int = None, id_comentario: int = None, tipo_alerta: str = None, tipo_usuario: str = None, commit: bool = True):
        try:
            query = """ INSERT INTO TBCOMENTARIO_ALERTA( ID, IDCOMENTARIO, IDUSUARIOORIG, IDUSUARIODSST, DTHR, TIPO, SITUACAO ) 
                        SELECT NULL AS ID, :IDCOMENTARIO, :IDUSUARIOORIG, U.ID AS IDUSUARIODSST, :DTHRALERTA, :TIPOALERTA, 'P' AS SITUACAO
                        FROM TBUSUARIO U 
                        WHERE U.SITUACAO = 'A' AND U.TIPO = :TIPOUSUARIO AND U.ID <> :ID
                    """
            params = {'IDCOMENTARIO': id_comentario, 'IDUSUARIOORIG': id_usuario, 'DTHRALERTA': pegar_data_hora_atual(), 'TIPOALERTA': tipo_alerta, 'TIPOUSUARIO': tipo_usuario, 'ID': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
            return True
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar_todas_resp(cls, db: _orm.Session, id_usuario: int = None, id_comentario: int = None, commit: bool = True):
        try:
            query = """ INSERT INTO TBCOMENTARIO_ALERTA( ID, IDCOMENTARIO, IDUSUARIOORIG, IDUSUARIODSST, DTHR, TIPO, SITUACAO ) 
                        SELECT NULL AS ID, :IDCOMENTARIO, :IDUSUARIOORIG, U.ID AS IDUSUARIODSST, :DTHRALERTA, 'R' AS TIPO, 'P' AS SITUACAO
                        FROM TBUSUARIO U
                        WHERE U.SITUACAO = 'A' AND U.ID <> :IDPRINC AND EXISTS( SELECT 1 FROM TBCOMENTARIO C WHERE C.IDUSUARIO = U.ID AND ( C.ID = :ID OR C.IDPAI = :IDPAI ) )
                    """
            params = {'IDCOMENTARIO': id_comentario, 'IDUSUARIOORIG': id_usuario, 'DTHRALERTA': pegar_data_hora_atual(), 'IDPRINC': id_usuario, 'ID': id_comentario, 'IDPAI': id_comentario}
            db.execute(query, params)
            if commit: db.commit()
            return True
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def marcar_todos_pendentes(cls, db: _orm.Session, id_usuario: int = None, commit: bool = True):
        try:
            query = """ UPDATE TBCOMENTARIO_ALERTA SET SITUACAO = 'L' WHERE IDUSUARIODSST = :IDUSUARIODSST """
            params = {'IDUSUARIODSST': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
            return True
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_resposta(cls, db: _orm.Session, id_comentario: int, commit: bool = True):
        try:
            query = """DELETE FROM TBCOMENTARIO_ALERTA WHERE IDCOMENTARIO IN ( SELECT C.ID FROM TBCOMENTARIO C WHERE C.IDPAI = :IDPAI AND C.TIPO = 'B')"""
            params = {'IDPAI': id_comentario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_comentario(cls, db: _orm.Session, id_comentario: int, commit: bool = True):
        try:
            query = """DELETE FROM TBCOMENTARIO_ALERTA WHERE IDCOMENTARIO = :IDCOMENTARIO """
            params = {'IDCOMENTARIO': id_comentario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBCOMENTARIO_ALERTA WHERE IDUSUARIOORIG = :IDUSUARIOORIG"
            params = {'IDUSUARIOORIG': id_usuario}
            db.execute(query, params)
            query = "DELETE FROM TBCOMENTARIO_ALERTA WHERE IDUSUARIODSST = :IDUSUARIODSST"
            params = {'IDUSUARIODSST': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioComentarioAlertaModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioComentarioAlertaModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
