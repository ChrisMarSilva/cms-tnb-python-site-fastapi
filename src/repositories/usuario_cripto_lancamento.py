# -*- coding: utf-8 -*-
import sys
import os
import asyncio
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str, inteiro_to_str
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioCriptoLancamentoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None):
        try:

            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if id_cripto: filters.append(cls, db: _orm.id_cripto == id_cripto)
            if dt_ini: filters.append(cls, db: _orm.data >= dt_ini)
            if dt_fim: filters.append(cls, db: _orm.data <= dt_fim)
            if tipo: filters.append(cls, db: _orm.tipo == tipo)

            return cls.query.filter(*filters).order_by(cls, db: _orm.id).all()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_cripto(cls, db: _orm.Session, id_cripto: int):
        try:
            return cls.query.filter_by(id_cripto=id_cripto).all()
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
    async def get_by_usuario(cls, db: _orm.Session, id: int, id_usuario: int):
        try:
            return cls.query.filter_by(id=id, id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if id_cripto: filters.append(cls, db: _orm.id_cripto == id_cripto)

            return db.query(db.func.min(cls, db: _orm.data)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None):
        try:

            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if id_cripto: filters.append(cls, db: _orm.id_cripto == id_cripto)

            return db.query(db.func.max(cls, db: _orm.data)).filter(*filters).first()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None, ordem: str = None, id_corretora: str = None):
        query = """ SELECT FL.ID, FL.IDUSUARIO, FL.IDCRIPTO AS IDCRIPTO, F.NOME AS NOMECRIPTO, F.CODIGO AS CODIGOCRIPTO, F.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO, F.VLRPRECOANTERIOR AS VLRPRECOANTERIOR, F.VLRVARIACAO AS VLRVARIACAO, F.SITUACAO AS SITUACAOCRIPTO, FL.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, FL.TIPO, FL.DATA, FL.QUANTORIG, FL.QUANT, FL.VLRPRECO, FL.TOTVLRPRECO, FL.VLRTAXA, FL.TOTVLR, FL.VLRCUSTO, FL.TOTVLRCUSTO, FL.VLRPRECOMEDIO, FL.TOTVLRVALORIZACAO, FL.PERCVALORIZACAO, FL.SITUACAO 
                    FROM TBCRIPTO_LANCAMENTO FL
                      INNER JOIN TBCRIPTO_EMPRESA F ON ( F.ID = FL.IDCRIPTO )
                      LEFT  JOIN TBCORRETORA C ON ( C.ID = FL.IDCORRETORA )
                    WHERE FL.IDUSUARIO = :IDUSUARIO
        """

        if codigo: query += " AND F.CODIGO = :CODIGO "
        if dt_ini: query += " AND FL.DATA >= :DATAINICIO "
        if dt_fim: query += " AND FL.DATA <= :DATAFIM "
        if tipo: query += " AND FL.TIPO = :TIPO "
        if id_corretora: query += " AND FL.IDCORRETORA = :IDCORRETORA "

        if ordem: query += " ORDER BY FL.DATA DESC, FL.ID, FL.TIPO "
        else: query += " ORDER BY FL.DATA, FL.ID, FL.TIPO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim
        if tipo: params['TIPO'] = tipo
        if id_corretora: params['IDCORRETORA'] = id_corretora

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise


    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int = None, id: int = None):
        query = """ SELECT FL.ID, FL.IDUSUARIO, FL.IDCRIPTO AS IDCRIPTO, F.NOME AS NOMECRIPTO, F.CODIGO AS CODIGOCRIPTO, F.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO, F.VLRPRECOANTERIOR AS VLRPRECOANTERIOR, F.VLRVARIACAO AS VLRVARIACAO, F.SITUACAO AS SITUACAOCRIPTO, FL.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, FL.TIPO, FL.DATA, FL.QUANTORIG, FL.QUANT, FL.VLRPRECO, FL.TOTVLRPRECO, FL.VLRTAXA, FL.TOTVLR, FL.VLRCUSTO, FL.TOTVLRCUSTO, FL.VLRPRECOMEDIO, FL.TOTVLRVALORIZACAO, FL.PERCVALORIZACAO, FL.SITUACAO
                    FROM TBCRIPTO_LANCAMENTO FL
                      INNER JOIN TBCRIPTO_EMPRESA F ON ( F.ID = FL.IDCRIPTO )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
                    WHERE FL.ID        = :ID
                      AND FL.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT FL.ID, FL.IDUSUARIO, FL.IDCRIPTO AS IDCRIPTO, F.NOME AS NOMECRIPTO, F.CODIGO AS CODIGOCRIPTO, F.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO, F.VLRPRECOANTERIOR AS VLRPRECOANTERIOR, F.VLRVARIACAO AS VLRVARIACAO, F.SITUACAO AS SITUACAOCRIPTO, FL.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, FL.TIPO, FL.DATA, FL.QUANTORIG, FL.QUANT, FL.VLRPRECO, FL.TOTVLRPRECO, FL.VLRTAXA, FL.TOTVLR, FL.VLRCUSTO, FL.TOTVLRCUSTO, FL.VLRPRECOMEDIO, FL.TOTVLRVALORIZACAO, FL.PERCVALORIZACAO, FL.SITUACAO
                    FROM TBCRIPTO_LANCAMENTO FL
                      INNER JOIN TBCRIPTO_EMPRESA F ON ( F.ID = FL.IDCRIPTO )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = FL.IDCORRETORA )
                    WHERE FL.IDUSUARIO = :IDUSUARIO
                      AND F.CODIGO     = :CODIGO
                    ORDER BY FL.DATA, FL.TIPO 
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None):
        query = """ SELECT SUBSTRING(MIN(FL.DATA), 1, 4) AS MENORANO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO """
        if id_cripto: query += """ AND FL.IDCRIPTO = :IDCRIPTO """
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_cripto: params['IDCRIPTO'] = id_cripto
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None):
        query = """ SELECT SUBSTRING(MAX(FL.DATA), 1, 4) AS MAIORANO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO """
        if id_cripto: query += """ AND FL.IDCRIPTO = :IDCRIPTO """
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_cripto: params['IDCRIPTO'] = id_cripto
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_total_compra(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDCRIPTO = :IDCRIPTO AND FL.TIPO = 'C' """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDCRIPTO'] = id_cripto
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_total_venda(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.QUANT) AS QTDE FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDCRIPTO = :IDCRIPTO AND FL.TIPO = 'V' """
        if id_lanc: query += """ AND FL.ID <> :ID """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDCRIPTO'] = id_cripto
        if id_lanc: params['ID'] = id_lanc
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_valor_total_compra(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDCRIPTO = :IDCRIPTO AND FL.TIPO = 'C' """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDCRIPTO'] = id_cripto
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_valor_total_venda(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(FL.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.IDCRIPTO = :IDCRIPTO AND FL.TIPO = 'V' """
        if id_lanc: query += """ AND FL.ID <> :ID """
        if dt_fim: query += """ AND FL.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDCRIPTO'] = id_cripto
        if id_lanc: params['ID'] = id_lanc
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_quant_operacao(cls, db: _orm.Session, id_usuario: int = None, situacao: str = None, tipo: str = None):
        try:

            query = " SELECT COUNT(1) AS QTDE FROM TBCRIPTO_LANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO "
            if situacao: query += " AND L.SITUACAO = :SITUACAO "
            if tipo: query += """ AND L.TIPO = :TIPO """

            params = {}
            params['IDUSUARIO'] = id_usuario
            if situacao: params['SITUACAO'] = situacao
            if tipo: params['TIPO'] = tipo

            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] and rows[0] > 0 else 0

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    @asyncio.coroutine
    async def buscar_qtde_total_base(cls, db: _orm.Session, tipo: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBCRIPTO_LANCAMENTO L WHERE 1 = 1 """
        if tipo: query += """ AND L.TIPO = :TIPO """
        params = {}
        if tipo: params['TIPO'] = tipo
        try:
            rows = db.execute(query, params).first()
            return rows[0] if rows and rows[0] and rows[0] > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_quant_ativo(cls, db: _orm.Session, id_usuario: int = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'A' """
        params = {'IDUSUARIO': id_usuario }
        try:
            rows = db.execute(query, params).first()
            return int(rows[0]) if rows and rows[0] and int(rows[0]) > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_preco_medio(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None, dt_fim: str = None):
        query = """ SELECT FL.VLRPRECOMEDIO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.ID = ( SELECT MAX(FLANT.ID) FROM TBCRIPTO_LANCAMENTO FLANT WHERE FLANT.IDUSUARIO = :IDUSUARIO AND FLANT.IDCRIPTO = :IDCRIPTO AND FLANT.SITUACAO = 'A' """
        if dt_fim: query += """ AND FLANT.DATA <= :DATAFIM """
        query += " ) "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDCRIPTO'] = id_cripto
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_preco_medio_antes(cls, db: _orm.Session, id_usuario: int = None, id_cripto: int = None, dt_fim: str = None):
        query = """ SELECT FL.VLRPRECOMEDIO FROM TBCRIPTO_LANCAMENTO FL WHERE FL.ID = ( SELECT MAX(FLANT.ID) FROM TBCRIPTO_LANCAMENTO FLANT WHERE FLANT.IDUSUARIO = :IDUSUARIO AND FLANT.IDCRIPTO = :IDCRIPTO AND FLANT.SITUACAO = 'A' """
        if dt_fim: query += """ AND FLANT.DATA < :DATAFIM """
        query += " ) "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDCRIPTO'] = id_cripto
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid_irpf(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT MAX(F.CODIGO) AS CODIGO,
                           MAX(F.NOME)   AS NOME,
                           SUM(FL.TOTVLR)      AS TOTVLR
                    FROM TBCRIPTO_LANCAMENTO FL
                      INNER JOIN TBCRIPTO_EMPRESA F ON ( F.ID = FL.IDCRIPTO )
                    WHERE FL.IDUSUARIO = :IDUSUARIO
                      AND FL.TIPO      = :TIPO
                      AND FL.DATA      >= :DATAINICIO
                      AND FL.DATA      <= :DATAFIM
                    GROUP BY FL.IDCRIPTO
                    ORDER BY F.NOME
                """
        params = {'IDUSUARIO': id_usuario, 'TIPO': tipo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def atualizar_qtd_pend_situacao(cls, db: _orm.Session, id_usuario: int, id_lanc: int, situacao: str, commit: bool = True):
        try:
            query = "UPDATE TBCRIPTO_LANCAMENTO SET SITUACAO = :SITUACAO WHERE IDUSUARIO = :IDUSUARIO AND ID = :ID "
            params = {'IDUSUARIO': id_usuario, 'ID': id_lanc, 'SITUACAO': situacao}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def resetar_ativos(cls, db: _orm.Session, id_usuario: int, id_cripto: int, commit: bool = True):
        try:
            query = " UPDATE TBCRIPTO_LANCAMENTO SET QUANT = QUANTORIG, TOTVLRCUSTO = 0.00, VLRPRECOMEDIO = 0.00, TOTVLRVALORIZACAO = 0.00, PERCVALORIZACAO = 0.00, SITUACAO = 'P' WHERE IDCRIPTO = :IDCRIPTO AND IDUSUARIO = :IDUSUARIO "
            params = {'IDUSUARIO': id_usuario, 'IDCRIPTO': id_cripto}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo_fundo(cls, db: _orm.Session, id_usuario: int, id_cripto: int, commit: bool = True):
        try:
            query = " DELETE FROM TBCRIPTO_LANCAMENTO WHERE IDCRIPTO = :IDCRIPTO AND IDUSUARIO = :IDUSUARIO "
            params = {'IDCRIPTO': id_cripto, 'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = " DELETE FROM TBCRIPTO_LANCAMENTO WHERE IDUSUARIO = :IDUSUARIO "
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
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
