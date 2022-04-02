# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_log import UsuarioLogModel
# from app.models.log_erro import LogErro
from src.util.util_datahora import pegar_data_hora_atual, pegar_data_atual


class UsuarioLogRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioLogModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioLogModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(UsuarioLogModel).filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_ultimo_acesso(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT MAX(UL.DATAHORA) ACESSO FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = :IDUSUARIO AND UL.SITUACAO IN ( 'L', 'P' ) """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_penultimo_acesso(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT MAX(PUL.DATAHORA) ACESSO FROM TBUSUARIO_LOG PUL WHERE PUL.IDUSUARIO = :IDUSUARIO AND PUL.SITUACAO IN ( 'L', 'P' ) AND PUL.DATAHORA < ( SELECT MAX(UL.DATAHORA) FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = PUL.IDUSUARIO AND UL.SITUACAO = PUL.SITUACAO ) """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_ultimo_acesso_usuario(cls, db: _orm.Session, id_usuario: int, situacao: str = None):
        query = """ SELECT MAX(UL.DATAHORA) ACESSO FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = :IDUSUARIO AND UL.SITUACAO = :SITUACAO """
        params = {'IDUSUARIO': id_usuario, 'SITUACAO': situacao}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_teve_acesso(cls, db: _orm.Session, id_usuario: int, data: str = None, situacao: str = None):
        query = """ SELECT MAX(UL.ID) ID FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = :IDUSUARIO AND UL.SITUACAO = :SITUACAO AND UL.DATA = :DATA """
        params = {'IDUSUARIO': id_usuario, 'DATA': data, 'SITUACAO': situacao}
        try:
            rows = db.execute(query, params).first()
            return 'S' if rows and rows[0] and rows[0] > 0 else 'N'
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_by_usuario(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            db.query(UsuarioLogModel).filter_by(id_usuario=id_usuario).delete()
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBUSUARIO_LOG WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @staticmethod
    async def registrar(db: _orm.Session, id_usuario: int, situacao: str = 'L'):
        try:

            # L-Login Site
            # P-Login App
            # S-logout
            # I-Senha Invalida
            # B-Inativar Usuario
            # A-Alterou Senha
            # D-Redefinir Senha
            # R-Resetar Operações

            try:
                (dt, micro) = pegar_data_hora_atual(fmt='%Y%m%d%H%M%S.%f').split('.')
                data_hora = "%s%03d" % (dt, int(micro) / 1000)
            except Exception as e:
                data_hora = pegar_data_hora_atual()

            usuario_log = UsuarioLogModel()
            usuario_log.id_usuario = id_usuario
            usuario_log.data = pegar_data_atual()
            usuario_log.data_hora = data_hora
            usuario_log.situacao = situacao
            db.add(usuario_log)
            db.commit()

        except Exception as e:
            pass #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))

