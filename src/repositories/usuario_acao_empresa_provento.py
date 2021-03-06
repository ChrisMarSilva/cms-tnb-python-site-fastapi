# -*- coding: utf-8 -*-
import sys
import os
import asyncio
import sqlalchemy.orm as _orm
from src.models.usuario_acao_empresa_provento import UsuarioACAOEmpresaProventoModel
# from app.models.log_erro import LogErro


class UsuarioACAOEmpresaProventoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioACAOEmpresaProventoModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(UsuarioACAOEmpresaProventoModel).filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_ativo(cls, db: _orm.Session, id_ativo: int):
        try:
            return db.query(UsuarioACAOEmpresaProventoModel).filter_by(id_ativo=id_ativo).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioACAOEmpresaProventoModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_usuario(cls, db: _orm.Session, id: int, id_usuario: int):
        try:
            return db.query(UsuarioACAOEmpresaProventoModel).filter_by(id=id, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(UsuarioACAOEmpresaProventoModel.id_usuario == id_usuario)
            if id_ativo: filters.append(UsuarioACAOEmpresaProventoModel.id_ativo == id_ativo)

            return db.query(db.func.min(UsuarioACAOEmpresaProventoModel.data_pagto)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_menor_ano_ex(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(UsuarioACAOEmpresaProventoModel.id_usuario == id_usuario)
            if id_ativo: filters.append(UsuarioACAOEmpresaProventoModel.id_ativo == id_ativo)
            return db.query(db.func.min(UsuarioACAOEmpresaProventoModel.data_ex)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(UsuarioACAOEmpresaProventoModel.id_usuario == id_usuario)
            if id_ativo: filters.append(UsuarioACAOEmpresaProventoModel.id_ativo == id_ativo)

            return db.query(db.func.max(UsuarioACAOEmpresaProventoModel.data_pagto)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_maior_ano_ex(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        try:

            filters = []
            if id_usuario: filters.append(UsuarioACAOEmpresaProventoModel.id_usuario == id_usuario)
            if id_ativo: filters.append(UsuarioACAOEmpresaProventoModel.id_ativo == id_ativo)

            return db.query(db.func.max(UsuarioACAOEmpresaProventoModel.data_ex)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None, id_corretora: str = None, situacao: str = None):

        query = """ SELECT P.ID, 
                           P.IDUSUARIO, 
                           P.IDATIVO      AS IDATIVO, 
                           A.CODIGO       AS CODIGOATIVO, 
                           A.SITUACAO     AS SITUACAOATIVO,
                           P.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           P.TIPO,  
                           P.DATAEX,  
                           P.DATAPAGTO, 
                           P.DESCRICAO,
                           P.QUANTIDADE, 
                           P.CALCVLRLIQUIDO, 
                           P.VLRPRECOBRUTO, 
                           P.VLRPRECO, 
                           P.TOTVLRBRUTO, 
                           P.TOTVLR, 
                           P.SITUACAO 
                    FROM TBPROVENTO P
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = P.IDATIVO     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = P.IDCORRETORA )
                    WHERE P.IDUSUARIO = :IDUSUARIO
                """

        if codigo: query += " AND A.CODIGO = :CODIGO "
        if tipo: query += " AND P.TIPO =  :TIPO "
        if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO "
        if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
        if id_corretora: query += " AND P.IDCORRETORA = :IDCORRETORA "
        if situacao: query += " AND P.SITUACAO = :SITUACAO "
        query += " ORDER BY P.DATAPAGTO, P.TIPO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        if tipo: params['TIPO'] = tipo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim
        if id_corretora: params['IDCORRETORA'] = id_corretora
        if situacao: params['SITUACAO'] = situacao
        try:
            try:
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int = None, id: int = None):
        query = """ SELECT P.ID, 
                           P.IDUSUARIO, 
                           P.IDATIVO      AS IDATIVO, 
                           A.CODIGO       AS CODIGOATIVO, 
                           A.SITUACAO     AS SITUACAOATIVO,
                           P.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           P.TIPO,  
                           P.DATAEX,  
                           P.DATAPAGTO, 
                           P.DESCRICAO,
                           P.QUANTIDADE, 
                           P.CALCVLRLIQUIDO, 
                           P.VLRPRECOBRUTO, 
                           P.VLRPRECO, 
                           P.TOTVLRBRUTO, 
                           P.TOTVLR, 
                           P.SITUACAO 
                    FROM TBPROVENTO P
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = P.IDATIVO     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = P.IDCORRETORA )
                    WHERE P.ID        = :ID
                      AND P.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT P.ID, 
                           P.IDUSUARIO, 
                           P.IDATIVO      AS IDATIVO, 
                           A.CODIGO       AS CODIGOATIVO, 
                           A.SITUACAO     AS SITUACAOATIVO,
                           P.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           P.TIPO,  
                           P.DATAEX,  
                           P.DATAPAGTO, 
                           P.DESCRICAO,
                           P.QUANTIDADE, 
                           P.CALCVLRLIQUIDO, 
                           P.VLRPRECOBRUTO, 
                           P.VLRPRECO, 
                           P.TOTVLRBRUTO, 
                           P.TOTVLR, 
                           P.SITUACAO 
                    FROM TBPROVENTO P
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = P.IDATIVO     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = P.IDCORRETORA )
                    WHERE A.CODIGO    = :CODIGO
                      AND P.IDUSUARIO = :IDUSUARIO
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid_irpf(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None, dt_pagto_ini: str = None, dt_pagto_fim: str = None, dt_ex_ini: str = None, dt_ex_fim: str = None):
        query = """ SELECT MAX(A.CODIGO) AS CODIGO, MAX(E.CNPJ) AS CNPJ, MAX(E.RAZAOSOCIAL) AS RAZAOSOCIAL, SUM(P.TOTVLR) AS TOTVLR
                    FROM TBPROVENTO P INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = P.IDATIVO ) INNER JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA )
                    WHERE P.IDUSUARIO = :IDUSUARIO AND P.TIPO = :TIPO AND P.DATAPAGTO >= :DATAINICIO AND P.DATAPAGTO <= :DATAFIM
                """
        if dt_ex_ini: query += " AND P.DATAEX >= :DATAEXINI "
        if dt_ex_fim: query += " AND P.DATAEX <= :DATAEXFIM "
        query += " GROUP BY P.IDATIVO "
        query += " ORDER BY E.RAZAOSOCIAL "

        params = {}
        params['IDUSUARIO'] = id_usuario
        params['TIPO'] = tipo
        params['DATAINICIO'] = dt_pagto_ini
        params['DATAFIM'] = dt_pagto_fim
        if dt_ex_ini: params['DATAEXINI'] = dt_ex_ini
        if dt_ex_fim: params['DATAEXFIM'] = dt_ex_fim
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_total(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(P.TOTVLR), 0.00 ) AS TOTAL FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO AND P.IDATIVO = :IDATIVO AND P.SITUACAO = 'A' """
        if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDATIVO'] = id_ativo
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_total_periodo(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(P.TOTVLR), 0.00 ) AS TOTAL FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
        if id_ativo: query += " AND P.IDATIVO = :IDATIVO "
        if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO "
        if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDATIVO'] = id_ativo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_total_periodo_ex(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(P.TOTVLR), 0.00 ) AS TOTAL FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO AND P.IDATIVO = :IDATIVO AND P.DATAEX >= :DATAINICIO AND P.DATAEX <= :DATAFIM """
        params = {'IDUSUARIO': id_usuario, 'IDATIVO': id_ativo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_preco(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(P.VLRPRECO), 0.00 ) AS VALOR FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO AND P.IDATIVO = :IDATIVO AND P.DATAPAGTO >= :DATAINICIO AND P.DATAPAGTO <= :DATAFIM """
        params = {'IDUSUARIO': id_usuario, 'IDATIVO': id_ativo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_preco_ex(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(P.VLRPRECO), 0.00 ) AS VALOR FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO AND P.IDATIVO = :IDATIVO AND P.DATAEX >= :DATAINICIO AND P.DATAEX <= :DATAFIM """
        params = {'IDUSUARIO': id_usuario, 'IDATIVO': id_ativo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    @asyncio.coroutine
    async def buscar_qtde_total_base(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBPROVENTO P WHERE 1 = 1 """
        if tipo: query += " AND P.TIPO = :TIPO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] and rows[0] > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_qtd_operacao_usuario(cls, db: _orm.Session, id_usuario: int = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO"""
        params = {'IDUSUARIO': id_usuario}
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] and rows[0] > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        query = """ SELECT SUBSTRING(MIN(P.DATAPAGTO), 1, 4) AS MENORANO FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
        if id_ativo: query += " AND P.IDATIVO = :IDATIVO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_ativo: params['IDATIVO'] = id_ativo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_menor_ano_ex(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        query = """ SELECT SUBSTRING(MIN(P.DATAEX), 1, 4) AS MENORANO FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
        if id_ativo: query += " AND P.IDATIVO = :IDATIVO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_ativo: params['IDATIVO'] = id_ativo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        query = """ SELECT SUBSTRING(MAX(P.DATAPAGTO), 1, 4) AS MAIORANO FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
        if id_ativo: query += " AND P.IDATIVO = :IDATIVO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_ativo: params['IDATIVO'] = id_ativo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_ano_ex(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        query = """ SELECT SUBSTRING(MAX(P.DATAEX), 1, 4) AS MAIORANO FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
        if id_ativo: query += " AND P.IDATIVO = :IDATIVO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_ativo: params['IDATIVO'] = id_ativo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_data(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None, dt_fim: str = None):
        query = """ SELECT MAX(P.DATAPAGTO) AS MAIORDATA FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
        if id_ativo: query += " AND P.IDATIVO = :IDATIVO "
        if dt_fim: query += " AND P.DATAEX <= :DATAFIM  "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_ativo: params['IDATIVO'] = id_ativo
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_data_ex(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None, dt_fim: str = None):
        query = """ SELECT MAX(P.DATAEX) AS MAIORDATA FROM TBPROVENTO P WHERE P.IDUSUARIO = :IDUSUARIO """
        if id_ativo: query += " AND P.IDATIVO = :IDATIVO "
        if dt_fim: query += " AND P.DATAEX <= :DATAFIM  "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_ativo: params['IDATIVO'] = id_ativo
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] else ''
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBPROVENTO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioACAOEmpresaProventoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioACAOEmpresaProventoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
