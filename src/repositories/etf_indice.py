# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.etf_indice import ETFIndiceModel
# from app.models.log_erro import LogErro


class ETFIndiceRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(ETFIndiceModel).filter(ETFIndiceModel.situacao.in_(['A', 'E'])).order_by(ETFIndiceModel.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(ETFIndiceModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_codigo(cls, db: _orm.Session, codigo: str):
        try:
            return db.query(ETFIndiceModel).filter_by(codigo=codigo).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_razao_social(cls, db: _orm.Session, razao_social: str):
        try:
            return db.query(ETFIndiceModel).filter_by(razao_social=razao_social).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_fundo(cls, db: _orm.Session, fundo: str):
        try:
            return db.query(ETFIndiceModel).filter_by(fundo=fundo).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_indice(cls, db: _orm.Session, indice: str):
        try:
            return db.query(ETFIndiceModel).filter_by(indice=indice).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_nome(cls, db: _orm.Session, nome: str):
        try:
            return db.query(ETFIndiceModel).filter_by(nome=nome).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_cnpj(cls, db: _orm.Session, cnpj: str):
        try:
            return db.query(ETFIndiceModel).filter_by(cnpj=cnpj).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_nomes(cls, db: _orm.Session):
        try:
            return db.query(ETFIndiceModel).filter(ETFIndiceModel.situacao.in_(['A', 'E'])).order_by(ETFIndiceModel.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_codigos(cls, db: _orm.Session):
        try:
            return db.query(ETFIndiceModel).filter(ETFIndiceModel.situacao.in_(['A', 'E'])).order_by(ETFIndiceModel.codigo).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.SITUACAO IN ( 'A' ,'E' ) ORDER BY FI.NOME """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int = None):
        query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.ID = :ID """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, codigo: str = None):
        query = """SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.CODIGO = :CODIGO """
        params = {'CODIGO': codigo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_razao_social(cls, db: _orm.Session, razao_social: str = None):
        query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.RAZAOSOCIAL = :RAZAOSOCIAL """
        params = {'RAZAOSOCIAL': razao_social}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_fundo(cls, db: _orm.Session, fundo: str = None):
        query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.FUNDO = :FUNDO """
        params = {'FUNDO': fundo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_indice(cls, db: _orm.Session, indice: str = None):
        query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.INDICE = :INDICE """
        params = {'INDICE': indice}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_nome(cls, db: _orm.Session, nome: str = None):
        query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.NOME = :NOME """
        params = {'NOME': nome}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_cnpj(cls, db: _orm.Session, cnpj: str = None):
        query = """ SELECT FI.ID, FI.RAZAOSOCIAL, FI.FUNDO, FI.INDICE, FI.NOME, FI.CNPJ, FI.CODIGO, FI.CODISIN, FI.SITUACAO FROM TBETF_INDICE FI WHERE FI.CNPJ = :CNPJ """
        params = {'CNPJ': cnpj}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome(cls, db: _orm.Session):
        query = """ SELECT FI.ID, FI.NOME FROM TBETF_INDICE FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.NOME """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_codigo(cls, db: _orm.Session):
        query = """ SELECT FI.ID, FI.CODIGO FROM TBETF_INDICE FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.CODIGO """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_pendentes_situacao(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT F.CODIGO, F.ID FROM TBETF_INDICE F WHERE EXISTS( SELECT 1 FROM TBETF_LANCAMENTO FL WHERE FL.IDINDICE = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'P' ) """
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
        query = """ SELECT F.ID,F.CODIGO, F.CNPJ, F.RAZAOSOCIAL FROM TBETF_INDICE F WHERE F.SITUACAO IN ( 'A' ,'E' ) AND EXISTS( SELECT 1 FROM TBETF_LANCAMENTO FL WHERE FL.IDINDICE = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.DATA <= :DATAFIM ) ORDER BY F.CODIGO """
        params = {'IDUSUARIO': id_usuario, 'DATAFIM': dt_fim}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_codigos_comprados(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT F.ID, F.CODIGO FROM TBETF_INDICE F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBETF_LANCAMENTO FL WHERE FL.IDINDICE = F.ID AND FL.IDUSUARIO = :IDUSUARIO ) """
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
    async def salvar(cls, db: _orm.Session, row: ETFIndiceModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: ETFIndiceModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
