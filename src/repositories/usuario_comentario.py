# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_comentario import UsuarioComentarioModel
# from app.models.log_erro import LogErro


class UsuarioComentarioRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioComentarioModel).order_by(UsuarioComentarioModel.id).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(UsuarioComentarioModel).filter_by(id_usuario=id_usuario).order_by(UsuarioComentarioModel.id).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioComentarioModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id_and_id_usuario(cls, db: _orm.Session, id_usuario: int, id: int):
        try:
            return db.query(UsuarioComentarioModel).filter_by(id_usuario=id_usuario, id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id_pai(cls, db: _orm.Session, id_usuario: int, id_pai: int):
        try:
            return db.query(UsuarioComentarioModel).filter_by(id_usuario=id_usuario, id_pai=id_pai).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_qtde_total_coment_princ(cls, db: _orm.Session):
        try:
            return db.query(UsuarioComentarioModel).filter_by(tipo='A', situacao='A').count()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT C.ID, C.IDPAI, C.IDUSUARIO, C.TIPO, C.TEXTO, C.DATAHORA, C.SITUACAO FROM TBCOMENTARIO C WHERE C.IDUSUARIO = :IDUSUARIO ORDER BY C.ID """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int, id: int = None):
        query = """ SELECT C.ID, C.IDPAI, C.IDUSUARIO, C.TIPO, C.TEXTO, C.DATAHORA, C.SITUACAO FROM TBCOMENTARIO C WHERE C.ID = :ID AND C.IDUSUARIO = :IDUSUARIO ORDER BY C.ID """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_qtde_total_coment_princ(cls, db: _orm.Session):
        query = "SELECT COUNT(1) AS QTDE FROM TBCOMENTARIO C WHERE C.TIPO = 'A' AND C.SITUACAO = 'A'"
        params = {}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_coment_grid_princ(cls, db: _orm.Session, reg_inicio: int = 1, qtde_pagina: int = 100):
        query = """ SELECT C.IDUSUARIO AS IDUSUARIO, 
                           U.NOME      AS NOMEUSUARIO, 
                           U.FOTO      AS FOTOUSUARIO, 
                           C.ID        AS IDCOMENTARIO, 
                           C.TEXTO     AS TXTCOMENTARIO,  
                           C.DATAHORA  AS DTHRCOMENTARIO
                    FROM TBCOMENTARIO C
                      INNER JOIN TBUSUARIO U ON ( U.ID = C.IDUSUARIO )
                    WHERE C.TIPO     = 'A'
                      AND C.SITUACAO = 'A'
                    ORDER BY C.DATAHORA DESC, C.ID
                    LIMIT """ + str(reg_inicio) + """, """ + str(qtde_pagina) + """
                """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_coment_grid_resp(cls, db: _orm.Session, id_comentario: int):
        query = """ SELECT C.IDUSUARIO AS IDUSUARIO, 
                           U.NOME      AS NOMEUSUARIO, 
                           U.FOTO      AS FOTOUSUARIO, 
                           C.ID        AS IDCOMENTARIO, 
                           C.TEXTO     AS TXTCOMENTARIO,  
                           C.DATAHORA  AS DTHRCOMENTARIO
                    FROM TBCOMENTARIO C
                      INNER JOIN TBUSUARIO U ON ( U.ID = C.IDUSUARIO )
                    WHERE C.IDPAI    = :IDPAI
                      AND C.TIPO     = 'B'
                      AND C.SITUACAO = 'A'
                    ORDER BY C.DATAHORA ASC, C.ID
                """
        params = {'IDPAI': id_comentario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_user_alerta(cls, db: _orm.Session, id_comentario: int):
        query = """ SELECT CA.IDUSUARIODSST AS IDUSUARIO, 
                           U.NOME       AS NOMEUSUARIO,  
                           U.FOTO       AS FOTOUSUARIO, 
                           U.EMAIL      AS EMAILUSUARIO
                    FROM TBCOMENTARIO_ALERTA CA
                        INNER JOIN TBUSUARIO U ON ( U.ID = CA.IDUSUARIODSST )
                    WHERE CA.IDCOMENTARIO = :IDCOMENTARIO
                   AND CA.TIPO IN ('C','R')
                   AND CA.SITUACAO = 'L'
                """
        params = {'IDCOMENTARIO': id_comentario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_user_reacao(cls, db: _orm.Session, id_comentario: int, tipo: str):
        query = """ SELECT CR.IDUSUARIO AS IDUSUARIO, 
                           U.NOME       AS NOMEUSUARIO,  
                           U.FOTO       AS FOTOUSUARIO, 
                           U.EMAIL      AS EMAILUSUARIO
                    FROM TBCOMENTARIO_REACAO CR
                        INNER JOIN TBUSUARIO U ON ( U.ID = CR.IDUSUARIO )
                    WHERE CR.IDCOMENTARIO = :IDCOMENTARIO
                      AND CR.TIPO         = :TIPO
                """
        params = {'IDCOMENTARIO': id_comentario, 'TIPO': tipo}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_respostas(cls, db: _orm.Session, id_comentario: int, commit: bool = True):
        try:
            query = """DELETE FROM TBCOMENTARIO WHERE IDPAI = :IDPAI AND TIPO = 'B'"""
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
            query = " DELETE FROM TBCOMENTARIO WHERE ID = :ID "
            params = {'ID': id_comentario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBCOMENTARIO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioComentarioModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioComentarioModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
