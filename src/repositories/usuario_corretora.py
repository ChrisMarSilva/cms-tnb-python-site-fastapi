# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_corretora import UsuarioCorretoraModel
# from app.models.log_erro import LogErro


class UsuarioCorretoraRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioCorretoraModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(UsuarioCorretoraModel).filter_by(id_usuario=id_usuario).order_by(UsuarioCorretoraModel.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioCorretoraModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_usuario(cls, db: _orm.Session, id: int, id_usuario: int):
        try:
            return db.query(UsuarioCorretoraModel).filter_by(id=id, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_cnpj(cls, db: _orm.Session, cnpj: str, id_usuario: int):
        try:
            return db.query(UsuarioCorretoraModel).filter_by(cnpj=cnpj, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_nome(cls, db: _orm.Session, nome: str, id_usuario: int):
        try:
            return db.query(UsuarioCorretoraModel).filter_by(nome=nome, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id_corretora_lista(cls, db: _orm.Session, id_corretora_lista: int, id_usuario: int):
        try:
            return db.query(UsuarioCorretoraModel).filter_by(id_corretora_lista=id_corretora_lista, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_nomes(cls, db: _orm.Session, id_usuario: int):
        try:
            try:
                return db.query(UsuarioCorretoraModel).filter_by(situacao='A', id_usuario=id_usuario).order_by(UsuarioCorretoraModel.nome).all()
            except Exception as e:
                return db.query(UsuarioCorretoraModel).filter_by(situacao='A', id_usuario=id_usuario).order_by(UsuarioCorretoraModel.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT C.ID, C.IDUSUARIO, C.NOME, C.CNPJ, C.VLRCORRETAGEM, C.SITUACAO FROM TBCORRETORA C WHERE C.IDUSUARIO = :IDUSUARIO ORDER BY C.NOME """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int, id: int = None):
        query = """ SELECT C.ID, C.IDUSUARIO, C.NOME, C.CNPJ, C.VLRCORRETAGEM, C.SITUACAO FROM TBCORRETORA C WHERE C.ID = :ID AND C.IDUSUARIO = :IDUSUARIO """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT C.ID, C.IDUSUARIO, C.NOME FROM TBCORRETORA C WHERE C.SITUACAO = 'A' AND C.IDUSUARIO = :IDUSUARIO ORDER BY C.NOME """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBCORRETORA WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioCorretoraModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioCorretoraModel, commit: bool = True):
        try:
            params = {'IDUSUARIO': row.id_usuario, 'IDCORRETORA': row.id}
            db.execute('UPDATE TBPROVENTO       SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
            db.execute('UPDATE TBOPERACAO       SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
            db.execute('UPDATE TBLANCAMENTO     SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
            db.execute('UPDATE TBFII_PROVENTO   SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
            db.execute('UPDATE TBFII_LANCAMENTO SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
            db.execute('UPDATE TBETF_OPERACAO   SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
            db.execute('UPDATE TBETF_LANCAMENTO SET IDCORRETORA = NULL WHERE IDUSUARIO = :IDUSUARIO AND IDCORRETORA = :IDCORRETORA', params)
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
