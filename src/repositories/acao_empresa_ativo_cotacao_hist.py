# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro


class ACAOEmpresaAtivoCotacaoHistRepository:

    @staticmethod
    async def get_table_name(categoria: str, codigo: str) -> str:
        if categoria == 'ACAO': return 'TBEMPRESA_ATIVOCOTACAO_' + codigo
        if categoria == 'FII': return 'TBFII_FUNDOIMOB_COTACAO_' + codigo
        if categoria == 'ETF': return 'TBETF_INDICE_COTACAO_' + codigo
        if categoria == 'BDR': return 'TTBBDR_EMPRESA_COTACAO_' + codigo
        if categoria == 'CRIPTO': return 'TBCRIPTO_EMPRESA_COTACAO_' + codigo
        return ""

    @classmethod
    async def tabela_existe(cls, db: _orm.Session, categoria: str, codigo: str):
        table_name = ACAOEmpresaAtivoCotacaoHistRepository.get_table_name(categoria=categoria, codigo=codigo)
        query = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = :TABLE_NAME"
        params = {'TABLE_NAME': table_name}
        return db.execute(query, params).first()

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, categoria: str, codigo: str, dt_ini: str = None, dt_fim: str = None):
        try:
            # if not cls.tabela_existe(categoria=categoria, codigo=codigo): return []

            table_name = ACAOEmpresaAtivoCotacaoHistRepository.get_table_name(categoria=categoria, codigo=codigo)

            query = """ SELECT C.DATA, C.COTACAO, C.VARIACAO FROM """ + table_name + """ C WHERE 1 = 1 """
            if dt_ini: query += " AND C.DATA >= :DATAINICIO "
            if dt_fim: query += " AND C.DATA <= :DATAFIM "
            query += " ORDER BY C.DATA "

            params = {}
            if dt_ini: params['DATAINICIO'] = dt_ini
            if dt_fim: params['DATAFIM'] = dt_fim
            return db.execute(query, params)

        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            # raise
            return None

    @classmethod
    async def buscar_valor_data_min(cls, db: _orm.Session, categoria: str, codigo: str, dt_ini: str, dt_fim: str) -> float:
        try:

            # if not cls.tabela_existe(categoria=categoria, codigo=codigo): return 0.0

            table_name = ACAOEmpresaAtivoCotacaoHistRepository.get_table_name(categoria=categoria, codigo=codigo)

            query = "SELECT C.COTACAO FROM " + table_name + " C WHERE C.DATA = ( SELECT MIN(S.DATA) FROM " + table_name + " S WHERE S.DATA >= :DATAINICIO AND S.DATA <= :DATAFIM ) "
            params = {'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}

            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and float(rows[0]) > 0.0 else 0.0

        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            # raise
            return float(0.0)

    @classmethod
    async def buscar_valor_data_max(cls, db: _orm.Session, categoria: str, codigo: str, dt_ini: str, dt_fim: str) -> float:
        try:

            # if not cls.tabela_existe(categoria=categoria, codigo=codigo): return 0.0

            table_name = ACAOEmpresaAtivoCotacaoHistRepository.get_table_name(categoria=categoria, codigo=codigo)

            query = "SELECT C.COTACAO FROM " + table_name + " C WHERE C.DATA = ( SELECT MAX(S.DATA) FROM " + table_name + " S WHERE S.DATA >= :DATAINICIO AND S.DATA <= :DATAFIM ) "
            params = {'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}

            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and float(rows[0]) > 0.0 else 0.0

        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            # raise
            return float(0.0)

    @classmethod
    async def buscar_maxima(cls, db: _orm.Session, categoria: str, codigo: str, dt_ini: str = None, dt_fim: str = None) -> float:
        try:

            # if not cls.tabela_existe(categoria=categoria, codigo=codigo): return 0.0

            table_name = ACAOEmpresaAtivoCotacaoHistRepository.get_table_name(categoria=categoria, codigo=codigo)

            query = """ SELECT MAX(C.COTACAO) AS COTACAO FROM """ + table_name + """ C WHERE 1 = 1 """
            if dt_ini: query += " AND C.DATA >= :DATAINICIO "
            if dt_fim: query += " AND C.DATA <= :DATAFIM "

            params = {}
            if dt_ini: params['DATAINICIO'] = dt_ini
            if dt_fim: params['DATAFIM'] = dt_fim

            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and float(rows[0]) > 0.0 else 0.0

        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            # raise
            return float(0.0)

