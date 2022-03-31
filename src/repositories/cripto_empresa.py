# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.xxxxxxxxxxx import xxxxxxxxxxxModel
# from app.models.log_erro import LogErro


class CriptoEmpresaRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.order_by(cls, db: _orm.nome).all()
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
    async def get_by_codigo(cls, db: _orm.Session, codigo: str):
        try:
            return cls.query.filter_by(codigo=codigo).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_nomes(cls, db: _orm.Session):
        try:
            return cls.query.filter(cls, db: _orm.situacao.in_(['A', 'E'])).order_by(cls, db: _orm.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_codigos(cls, db: _orm.Session):
        try:
            return cls.query.filter(cls, db: _orm.situacao.in_(['A', 'E'])).order_by(cls, db: _orm.codigo).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT FI.ID, FI.NOME, FI.CODIGO, FI.VLRPRECOFECHAMENTO, FI.VLRPRECOANTERIOR, FI.VLRVARIACAO, FI.DATAHORAALTERACO, FI.SITUACAO FROM TBCRIPTO_EMPRESA FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.NOME """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int = None):
        query = """ SELECT FI.ID, FI.NOME, FI.CODIGO, FI.VLRPRECOFECHAMENTO, FI.VLRPRECOANTERIOR, FI.VLRVARIACAO, FI.DATAHORAALTERACO, FI.SITUACAO FROM TBCRIPTO_EMPRESA FI WHERE FI.ID = :ID """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, codigo: str = None):
        query = """ SELECT FI.ID, FI.NOME, FI.CODIGO, FI.VLRPRECOFECHAMENTO, FI.VLRPRECOANTERIOR, FI.VLRVARIACAO, FI.DATAHORAALTERACO, FI.SITUACAO FROM TBCRIPTO_EMPRESA FI WHERE FI.CODIGO = :CODIGO """
        params = {'CODIGO': codigo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_nome(cls, db: _orm.Session, nome: str = None):
        query = """ SELECT FI.ID, FI.NOME, FI.CODIGO, FI.VLRPRECOFECHAMENTO, FI.VLRPRECOANTERIOR, FI.VLRVARIACAO, FI.DATAHORAALTERACO, FI.SITUACAO FROM TBCRIPTO_EMPRESA FI WHERE FI.NOME = :NOME """
        params = {'NOME': nome}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome(cls, db: _orm.Session):
        query = """ SELECT FI.ID, FI.NOME FROM TBCRIPTO_EMPRESA FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.NOME """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_codigo(cls, db: _orm.Session):
        query = """ SELECT FI.ID, FI.CODIGO FROM TBCRIPTO_EMPRESA FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.CODIGO """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_pendentes_situacao(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT F.CODIGO, F.ID FROM TBCRIPTO_EMPRESA F WHERE EXISTS( SELECT 1 FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDCRIPTO = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'P' ) """
        if codigo: query += " AND F.CODIGO = :CODIGO "
        query += " ORDER BY F.CODIGO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        try:
            return db.execute(query, params).fetchall()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_irpf(cls, db: _orm.Session, id_usuario: int = None, dt_fim: str = None):
        query = """ SELECT F.ID, F.CODIGO, F.NOME FROM TBCRIPTO_EMPRESA F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDCRIPTO = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.DATA <= :DATAFIM ) ORDER BY F.CODIGO """
        params = {'IDUSUARIO': id_usuario, 'DATAFIM': dt_fim}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_codigos_comprados(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT F.ID, F.CODIGO, F.NOME FROM TBCRIPTO_EMPRESA F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDCRIPTO = F.ID AND FL.IDUSUARIO = :IDUSUARIO ) """
        if codigo: query += " AND F.CODIGO = :CODIGO "
        query += " ORDER BY F.CODIGO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        try:
            return db.execute(query, params)
        except Exception as e:
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
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
