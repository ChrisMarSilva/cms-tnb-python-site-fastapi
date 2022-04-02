# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.corretora_lista import CorretoraListaModel
# from app.models.log_erro import LogErro


class CorretoraListaRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(CorretoraListaModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(CorretoraListaModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_nome(cls, db: _orm.Session, nome: str):
        try:
            return db.query(CorretoraListaModel).filter_by(nome=nome).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_cnpj(cls, db: _orm.Session, cnpj: str):
        try:
            return db.query(CorretoraListaModel).filter_by(cnpj=cnpj).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_nomes(cls, db: _orm.Session):
        try:
            try:
                return db.query(CorretoraListaModel).filter_by(situacao='A').order_by(CorretoraListaModel.nome).all()
            except Exception as e:
                return db.query(CorretoraListaModel).filter_by(situacao='A').order_by(CorretoraListaModel.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L ORDER BY L.NOME """
        params = {}
        try:
            try:
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int = None):
        query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.ID = :ID """
        params = {'ID': id}
        try:
            try:
                return db.execute(query, params).first()
            except Exception as e:
                return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_nome(cls, db: _orm.Session, nome: str = None):
        query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.NOME = :NOME """
        params = {'NOME': nome}
        try:
            try:
                return db.execute(query, params).first()
            except Exception as e:
                return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_cnpj(cls, db: _orm.Session, cnpj: str = None):
        query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.CNPJ = :CNPJ """
        params = {'CNPJ': cnpj}
        try:
            try:
                return db.execute(query, params).first()
            except Exception as e:
                return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome(cls, db: _orm.Session):
        try:
            query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.SITUACAO = 'A' ORDER BY L.NOME """
            params = {}
            try:
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome_cadastradas(cls, db: _orm.Session, id_usuario: int):
        try:
            query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBCORRETORA C WHERE C.IDCORRETORALISTA = L.ID AND C.IDUSUARIO = :IDUSUARIO ) ORDER BY L.NOME """
            params = {'IDUSUARIO': id_usuario}
            try:
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome_nao_cadastradas(cls, db: _orm.Session, id_usuario: int):
        try:
            query = """ SELECT L.ID, L.NOME, L.CNPJ, L.IMPORTAR_NOTA, L.SITUACAO FROM TBCORRETORA_LISTA L WHERE L.SITUACAO = 'A' AND NOT EXISTS( SELECT 1 FROM TBCORRETORA C WHERE C.IDCORRETORALISTA = L.ID AND C.IDUSUARIO = :IDUSUARIO ) ORDER BY L.NOME """
            params = {'IDUSUARIO': id_usuario}
            try:
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id: int, commit: bool = True):
        try:

            query = "UPDATE TBCORRETORA SET IDCORRETORALISTA = NULL WHERE IDCORRETORALISTA = :IDCORRETORALISTA"
            params = {'IDCORRETORALISTA': id}
            db.execute(query, params)

            query = "DELETE FROM TBCORRETORA_LISTA WHERE ID = :ID"
            params = {'ID': id}
            db.execute(query, params)

            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: CorretoraListaModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: CorretoraListaModel, commit: bool = True):
        try:
            params = {'IDCORRETORALISTA': row.id}
            db.execute('UPDATE TBCORRETORA SET IDCORRETORALISTA = NULL WHERE IDCORRETORALISTA = :IDCORRETORALISTA', params)
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
