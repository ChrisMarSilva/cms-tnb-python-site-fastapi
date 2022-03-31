# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.acao_empresa_ativo_cotacao import ACAOEmpresaAtivoCotacaoModel
# from app.models.log_erro import LogErro


class ACAOEmpresaAtivoCotacaoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(ACAOEmpresaAtivoCotacaoModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_ativo(cls, db: _orm.Session, id_ativo: int):
        try:
            return db.query(ACAOEmpresaAtivoCotacaoModel).filter_by(id_ativo=id_ativo).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_total(cls, db: _orm.Session):
        try:
            return db.query(ACAOEmpresaAtivoCotacaoModel).count()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT C.DATA, 
                           C.IDATIVO  AS IDATIVO, 
                           A.CODIGO   AS CODIGOATIVO, 
                           A.SITUACAO AS SITUACAOATIVO,
                           C.VLRPRECOABERTURA,  
                           C.VLRPRECOFECHAMENTO,  
                           C.VLRPRECOMAXIMO, 
                           C.VLRPRECOMINIMO,
                           C.VLRPRECOANTERIOR, 
                           C.VLRVARIACAO, 
                           C.DATAHORAALTERACO 
                    FROM TBEMPRESA_ATIVOCOTACAO C
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = C.IDATIVO )
                    WHERE A.SITUACAO = 'A'
                    ORDER BY A.CODIGO
                """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_completo(cls, db: _orm.Session, id_usuario: int = None, setor: str = None, subsetor: str = None, segmento: str = None, codigo: str = None, tipo: str = None, reg_inicio: int = None, qtde_por_pagina: int = None):
        query = """ SELECT C.DATA, 
                           C.IDATIVO  AS IDATIVO, 
                           A.CODIGO   AS CODIGOATIVO, 
                           A.SITUACAO AS SITUACAOATIVO,
                           E.NOME     AS NOMEEMPRESA,
                           E.NOMRESUMIDO AS NOMRESUMIDOEMPRESA,
                           E.RAZAOSOCIAL AS RAZAOSOCIALEMPRESA,
                           SR.ID             AS IDSETOR,
                           SR.DESCRICAO      AS DESCRICAOSETOR,
                           SS.ID             AS IDSUBSETOR,
                           SS.DESCRICAO      AS DESCRICAOSUBSETOR,
                           SG.ID             AS IDSEGMENTO,
                           SG.DESCRICAO      AS DESCRICAOSEGMENTO,
                           C.VLRPRECOABERTURA,  
                           C.VLRPRECOFECHAMENTO,  
                           C.VLRPRECOMAXIMO, 
                           C.VLRPRECOMINIMO,
                           C.VLRPRECOANTERIOR, 
                           C.VLRVARIACAO, 
                           C.DATAHORAALTERACO 
                    FROM TBEMPRESA_ATIVOCOTACAO C
                      INNER JOIN TBEMPRESA_ATIVO    A  ON ( A.ID  = C.IDATIVO    )
                      INNER JOIN TBEMPRESA          E  ON ( E.ID  = A.IDEMPRESA  )
                      LEFT  JOIN TBEMPRESA_SETOR    SR ON ( SR.ID = E.IDSETOR    )
                      LEFT  JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID = E.IDSUBSETOR )
                      LEFT  JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO )
                    WHERE A.SITUACAO = 'A'
                """

        if setor: query += " AND SR.ID = :IDSETOR "
        if subsetor: query += " AND SS.ID = :IDSUBSETOR "
        if segmento: query += " AND SG.ID = :IDSEGMENTO "
        if codigo: query += " AND A.CODIGO = :CODIGO "
        if tipo == 'M':  # M-Meus Ativos
            query += " AND EXISTS( SELECT 1 FROM TBCARTEIRA CT INNER JOIN TBCARTEIRA_ATIVO CA ON ( CT.ID = CA.IDCARTEIRA ) WHERE CA.IDATIVO = A.ID AND CT.IDUSUARIO = :IDUSUARIO AND (CA.QUANT + CA.QUANTBONUS ) > 0 ) "
        elif tipo == 'C':  # C-Ativos Comprados por Todos
            query += " AND EXISTS( SELECT 1 FROM TBCARTEIRA CT INNER JOIN TBCARTEIRA_ATIVO CA ON ( CT.ID = CA.IDCARTEIRA ) WHERE CA.IDATIVO = A.ID AND (CA.QUANT + CA.QUANTBONUS ) > 0 ) "

        query += " ORDER BY A.CODIGO "
        if reg_inicio and qtde_por_pagina: query += " LIMIT " + str(reg_inicio) + ", " + str(qtde_por_pagina)

        params = {}
        if setor: params['IDSETOR'] = setor
        if subsetor: params['IDSUBSETOR'] = subsetor
        if segmento: params['IDSEGMENTO'] = segmento
        if codigo: params['CODIGO'] = codigo
        if tipo == 'M': params['IDUSUARIO'] = id_usuario

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, codigo: str):
        query = """ SELECT C.DATA, 
                           C.IDATIVO  AS IDATIVO, 
                           A.CODIGO   AS CODIGOATIVO, 
                           A.SITUACAO AS SITUACAOATIVO,
                           C.VLRPRECOABERTURA,  
                           C.VLRPRECOFECHAMENTO,  
                           C.VLRPRECOMAXIMO, 
                           C.VLRPRECOMINIMO,
                           C.VLRPRECOANTERIOR, 
                           C.VLRVARIACAO, 
                           C.DATAHORAALTERACO 
                    FROM TBEMPRESA_ATIVOCOTACAO C
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = C.IDATIVO )
                    WHERE A.CODIGO   = :CODIGO 
                      AND A.SITUACAO = 'A'
                """
        params = {'CODIGO': codigo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id_ativo(cls, db: _orm.Session, id_ativo: int):
        query = """ SELECT C.VLRPRECOFECHAMENTO FROM TBEMPRESA_ATIVOCOTACAO C WHERE C.IDATIVO = :IDATIVO """
        params = {'IDATIVO': id_ativo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_total(cls, db: _orm.Session):
        try:
            query = """ SELECT COUNT(1) AS QTDE FROM TBEMPRESA_ATIVOCOTACAO C INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = C.IDATIVO ) WHERE A.SITUACAO = 'A' """
            params = {}
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] and rows[0] > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: ACAOEmpresaAtivoCotacaoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: ACAOEmpresaAtivoCotacaoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
