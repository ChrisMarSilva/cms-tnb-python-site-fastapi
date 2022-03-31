# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class BDREmpresaCotacaoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_ativo(cls, db: _orm.Session, id_bdr: int):
        try:
            return cls.query.filter_by(id_bdr=id_bdr).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT C.DATA, 
                           C.IDBDR    AS IDBDR, 
                           E.CODIGO   AS CODIGOBDR, 
                           E.SITUACAO AS SITUACAOBDR,
                           C.VLRPRECOABERTURA,  
                           C.VLRPRECOFECHAMENTO,  
                           C.VLRPRECOMAXIMO, 
                           C.VLRPRECOMINIMO,
                           C.VLRPRECOANTERIOR, 
                           C.VLRVARIACAO, 
                           C.DATAHORAALTERACO 
                    FROM TBBDR_EMPRESA_COTACAO C
                      INNER JOIN TBEMPRESA_ATIVO E ON ( E.ID = C.IDBDR )
                    WHERE E.SITUACAO = 'A'
                    ORDER BY E.CODIGO
                """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_completo(cls, db: _orm.Session, id_usuario: int = None, setor: str = None, subsetor: str = None, segmento: str = None, codigo: str = None, tipo: str = None):
        query = """ SELECT C.DATA, 
                           C.IDBDR  AS IDBDR, 
                           E.CODIGO   AS CODIGOBDR, 
                           E.SITUACAO AS SITUACAOBDR,
                           E.NOME     AS NOMEEMPRESA,
                           E.RAZAOSOCIAL AS RAZAOSOCIALEMPRESA,
                           C.VLRPRECOABERTURA,  
                           C.VLRPRECOFECHAMENTO,  
                           C.VLRPRECOMAXIMO, 
                           C.VLRPRECOMINIMO,
                           C.VLRPRECOANTERIOR, 
                           C.VLRVARIACAO, 
                           C.DATAHORAALTERACO 
                    FROM TBBDR_EMPRESA_COTACAO C
                      INNER JOIN TBEMPRESA E  ON ( E.ID  = C.IDBDR  )
                      LEFT  JOIN TBEMPRESA_SETOR    SR ON ( SR.ID = E.IDSETOR    )
                      LEFT  JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID = E.IDSUBSETOR )
                      LEFT  JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO )
                    WHERE E.SITUACAO = 'A'
                """

        if setor:
            query += " AND SR.ID = :IDSETOR "
        if subsetor:
            query += " AND SS.ID = :IDSUBSETOR "
        if segmento:
            query += " AND SG.ID = :IDSEGMENTO "
        if codigo:
            query += " AND E.CODIGO = :CODIGO "
        if tipo == 'M':  # M-Meus Ativos
            query += " AND EXISTS( SELECT 1 FROM TBCARTEIRA CT INNER JOIN TBCARTEIRA_BDR CA ON ( CT.ID = CA.IDCARTEIRA ) WHERE CA.IDBDR = E.ID AND CT.IDUSUARIO = :IDUSUARIO AND (CA.QUANT + CA.QUANTBONUS ) > 0 ) "
        elif tipo == 'C':  #C-Ativos Comprados por Todos
            query += " AND EXISTS( SELECT 1 FROM TBCARTEIRA CT INNER JOIN TBCARTEIRA_BDR CA ON ( CT.ID = CA.IDCARTEIRA ) WHERE CA.IDBDR = E.ID AND (CA.QUANT + CA.QUANTBONUS ) > 0 ) "

        query += " ORDER BY E.CODIGO "

        params = {}
        if setor:
            params['IDSETOR'] = setor
        if subsetor:
            params['IDSUBSETOR'] = subsetor
        if segmento:
            params['IDSEGMENTO'] = segmento
        if codigo:
            params['CODIGO'] = codigo
        if tipo == 'M':  # M-Meus Ativos
            params['IDUSUARIO'] = id_usuario
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, codigo: str):
        query = """ SELECT C.DATA, 
                           C.IDBDR  AS IDBDR, 
                           E.CODIGO   AS CODIGOBDR, 
                           E.SITUACAO AS SITUACAOBDR,
                           C.VLRPRECOABERTURA,  
                           C.VLRPRECOFECHAMENTO,  
                           C.VLRPRECOMAXIMO, 
                           C.VLRPRECOMINIMO,
                           C.VLRPRECOANTERIOR, 
                           C.VLRVARIACAO, 
                           C.DATAHORAALTERACO 
                    FROM TBBDR_EMPRESA_COTACAO C
                      INNER JOIN TBBDR_EMPRESA E ON ( E.ID = C.IDBDR )
                    WHERE E.CODIGO   = :CODIGO 
                      AND E.SITUACAO = 'A'
                """
        params = {'CODIGO': codigo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id_bdr(cls, db: _orm.Session, id_bdr: int):
        query = """ SELECT C.VLRPRECOFECHAMENTO FROM TBBDR_EMPRESA_COTACAO C WHERE C.IDBDR = :IDBDR """
        params = {'IDBDR': id_bdr}
        try:
            return db.execute(query, params).first()
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
