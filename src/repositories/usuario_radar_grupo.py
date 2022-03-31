# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_radar_grupo import UsuarioRadarGrupoModel
# from app.models.log_erro import LogErro


class UsuarioRadarGrupoRepository:

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
            return cls.query.filter_by(id_usuario=id_usuario).order_by(cls, db: _orm.id_usuario, cls.descricao).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id_and_id_usuario(cls, db: _orm.Session, id: int, id_usuario: int):
        try:
            return cls.query.filter_by(id=id, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_descricao(cls, db: _orm.Session, id_usuario: int, descricao: str):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, descricao=descricao).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_descricoes_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, situacao='A', ).order_by(cls, db: _orm.descricao).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT G.ID, G.DESCRICAO, G.SITUACAO FROM TBUSUARIO_ACOMP_GRUPO G WHERE G.IDUSUARIO = :IDUSUARIO ORDER BY G.DESCRICAO """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int, id: int):
        query = """ SELECT G.ID, G.DESCRICAO, G.SITUACAO FROM TBUSUARIO_ACOMP_GRUPO G WHERE G.ID = :ID AND G.IDUSUARIO = :IDUSUARIO """
        params = {'IDUSUARIO': id_usuario, 'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_nome(cls, db: _orm.Session, id_usuario: int, nome: str):
        query = """ SELECT G.ID, G.DESCRICAO, G.SITUACAO FROM TBUSUARIO_ACOMP_GRUPO G WHERE G.DESCRICAO = :DESCRICAO AND G.IDUSUARIO = :IDUSUARIO """
        params = {'IDUSUARIO': id_usuario, 'DESCRICAO': nome}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT G.ID, G.DESCRICAO FROM TBUSUARIO_ACOMP_GRUPO G WHERE G.SITUACAO = 'A' AND G.IDUSUARIO = :IDUSUARIO ORDER BY G.DESCRICAO """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO"
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
            params = {'IDGRUPO': self.id}
            db.execute("DELETE FROM TBUSUARIO_ACOMP_CRIPTO WHERE IDGRUPO = :IDGRUPO", params)
            db.execute("DELETE FROM TBUSUARIO_ACOMP_INDICE WHERE IDGRUPO = :IDGRUPO", params)
            db.execute("DELETE FROM TBUSUARIO_ACOMP_FUNDO  WHERE IDGRUPO = :IDGRUPO", params)
            db.execute("DELETE FROM TBUSUARIO_ACOMP_ATIVO  WHERE IDGRUPO = :IDGRUPO", params)
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
