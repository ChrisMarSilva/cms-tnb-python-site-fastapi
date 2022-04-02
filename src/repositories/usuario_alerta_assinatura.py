# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_alerta_assinatura import UsuarioAlertaAssinaturaModel
# from app.models.log_erro import LogErro


class UsuarioAlertaAssinaturaRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioAlertaAssinaturaModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(UsuarioAlertaAssinaturaModel).filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioAlertaAssinaturaModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_tipos(cls, db: _orm.Session, id_usuario: int, tipo_assinatura: str, tipo_alerta: str):
        try:
            return db.query(UsuarioAlertaAssinaturaModel).filter_by(id_usuario=id_usuario, tipo_assinatura=tipo_assinatura, tipo_alerta=tipo_alerta).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None):
        query = """ SELECT AA.ID, AA.IDUSUARIO, US.NOME AS NMUSUARIO, AA.DTHRREGISTRO, AA.DTHRALTERACAO, AA.TIPO_ALERTA, AA.TIPO_ASSINATURA, AA.SITUACAO
                    FROM TBALERTA_ASSINATURA AA JOIN TBUSUARIO US ON ( US.ID = AA.IDUSUARIO )
                    WHERE 1 = 1 
                """
        if id_usuario: query += " AND AA.IDUSUARIO = :IDUSUARIO "
        query += " ORDER BY AA.TIPO_ALERTA, AA.TIPO_ASSINATURA "
        params = {}
        if id_usuario: params['IDUSUARIO'] = id_usuario
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int):
        query = """ SELECT AA.ID, AA.IDUSUARIO, US.NOME AS NMUSUARIO, AA.DTHRREGISTRO, AA.DTHRALTERACAO, AA.TIPO_ALERTA, AA.TIPO_ASSINATURA, AA.SITUACAO
                    FROM TBALERTA_ASSINATURA AA JOIN TBUSUARIO US ON ( US.ID = AA.IDUSUARIO )
                    WHERE AA.ID = :ID 
                """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_tipo_alerta_assinatura(cls, db: _orm.Session, id_usuario: int = None, tipo_alerta: str = None, tipo_assinatura: str = None):
        query = """ SELECT AA.ID, AA.IDUSUARIO, US.NOME AS NMUSUARIO, AA.DTHRREGISTRO, AA.DTHRALTERACAO, AA.TIPO_ALERTA, AA.TIPO_ASSINATURA, AA.SITUACAO
                    FROM TBALERTA_ASSINATURA AA
                         JOIN TBUSUARIO US ON ( US.ID = AA.IDUSUARIO )
                    WHERE AA.IDUSUARIO = :IDUSUARIO 
                      AND AA.TIPO_ALERTA = :TIPO_ALERTA 
                      AND AA.TIPO_ASSINATURA = :TIPO_ASSINATURA 
                """
        params = {'IDUSUARIO': id_usuario, 'TIPO_ALERTA': tipo_alerta, 'TIPO_ASSINATURA': tipo_assinatura}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_user(cls, db: _orm.Session, tipo_alerta: str = None, tipo_assinatura: str = None):
        query = """ SELECT U.ID, U.NOME FROM TBUSUARIO U WHERE EXISTS( SELECT 1 FROM TBALERTA_ASSINATURA AA WHERE AA.IDUSUARIO = U.ID """
        if tipo_alerta: query += " AND AA.TIPO_ALERTA = :TIPO_ALERTA "
        if tipo_assinatura: query += " AND AA.TIPO_ASSINATURA = :TIPO_ASSINATURA "
        query += " ) "
        query += " ORDER BY U.NOME "

        params = {}
        if tipo_alerta: params['TIPO_ALERTA'] = tipo_alerta
        if tipo_assinatura: params['TIPO_ASSINATURA'] = tipo_assinatura

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioAlertaAssinaturaModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioAlertaAssinaturaModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise