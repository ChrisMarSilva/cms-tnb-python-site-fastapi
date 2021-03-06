# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_etf_indice_fato_relevante_ativo import UsuarioETFIndiceFatoRelevanteAtivoModel
# from app.models.log_erro import LogErro


class UsuarioETFIndiceFatoRelevanteAtivoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioETFIndiceFatoRelevanteAtivoModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_fato_and_usuario(cls, db: _orm.Session, id_usuario: int, id_fato: int):
        try:
            return db.query(UsuarioETFIndiceFatoRelevanteAtivoModel).filter_by(id_usuario=id_usuario, id_fato=id_fato).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_by_usuario(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            db.query(UsuarioETFIndiceFatoRelevanteAtivoModel).filter_by(id_usuario=id_usuario).delete()
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBETF_FATORELEVANTE_ATIVO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioETFIndiceFatoRelevanteAtivoModel, commit: bool = True):
        try:
            if cls.get_by_fato_and_usuario(id_fato=row.id_fato, id_usuario=row.id_usuario): return False
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            #raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioETFIndiceFatoRelevanteAtivoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
