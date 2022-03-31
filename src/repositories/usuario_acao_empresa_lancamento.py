# -*- coding: utf-8 -*-
import sys
import os
import asyncio
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str, inteiro_to_str
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioACAOEmpresaLancamentoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        return cls.query.all()

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        return cls.query.filter_by(id_usuario=id_usuario).all()

    @classmethod
    async def get_all_by_ativo(cls, db: _orm.Session, id_ativo: int):
        return cls.query.filter_by(id_ativo=id_ativo).all()

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        return cls.query.filter_by(id=id).first()

    @classmethod
    async def get_by_usuario(cls, db: _orm.Session, id: int, id_usuario: int):
        return cls.query.filter_by(id=id, id_usuario=id_usuario).first()

    @classmethod
    async def get_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        filters = []
        if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
        if id_ativo: filters.append(cls, db: _orm.id_ativo == id_ativo)
        return db.query(db.func.min(cls, db: _orm.data)).filter(*filters).first()

    @classmethod
    async def get_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        filters = []
        if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
        if id_ativo: filters.append(cls, db: _orm.id_ativo == id_ativo)
        return db.query(db.func.max(cls, db: _orm.data)).filter(*filters).first()

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None, tipo: str = None, ordem: str = None, id_corretora: str = None, troca: str = None):
        try:

            query = """ SELECT O.ID, O.IDUSUARIO, O.IDATIVO AS IDATIVO, A.CODIGO AS CODIGOATIVO, A.SITUACAO AS SITUACAOATIVO, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
                               O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
                               O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, O.TROCA, O.SITUACAO,
                               ( SELECT MAX(OP.VLRPRECOMEDIO)     FROM TBOPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDATIVO = O.IDATIVO AND OP.IDLANC = O.ID ) AS VLRPRECOMEDIO, 
                               ( SELECT SUM(OP.TOTVLRVALORIZACAO) FROM TBOPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDATIVO = O.IDATIVO AND OP.IDLANC = O.ID ) AS TOTVLRVALORIZACAO, 
                               ( SELECT SUM(OP.PERCVALORIZACAO)   FROM TBOPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDATIVO = O.IDATIVO AND OP.IDLANC = O.ID ) AS PERCVALORIZACAO
                        FROM TBLANCAMENTO O
                          INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = O.IDATIVO )
                          LEFT  JOIN TBCORRETORA C ON ( C.ID = O.IDCORRETORA )
                        WHERE O.IDUSUARIO = :IDUSUARIO
                    """

            if codigo: query += " AND A.CODIGO = :CODIGO "
            if dt_ini: query += " AND O.DATA >= :DATAINICIO "
            if dt_fim: query += " AND O.DATA <= :DATAFIM "
            if tipo: query += " AND O.TIPO = :TIPO "
            if id_corretora: query += " AND O.IDCORRETORA = :IDCORRETORA "
            if troca: query += " AND IFNULL(O.TROCA, 'N') = :TROCA "

            if ordem: query += " ORDER BY O.DATA DESC, O.TIPO, O.ID "
            else: query += "  ORDER BY O.DATA, O.TIPO, O.ID "

            params = {}
            params['IDUSUARIO'] = id_usuario
            if codigo: params['CODIGO'] = codigo
            if dt_ini: params['DATAINICIO'] = dt_ini
            if dt_fim: params['DATAFIM'] = dt_fim
            if tipo: params['TIPO'] = tipo
            if id_corretora: params['IDCORRETORA'] = id_corretora
            if troca: params['TROCA'] = troca

            return db.execute(query, params)

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_data(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, data: str = None, tipo: str = None):
        query = """ SELECT O.ID, O.IDUSUARIO, O.IDATIVO AS IDATIVO, A.CODIGO AS CODIGOATIVO, A.SITUACAO AS SITUACAOATIVO, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
                           O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, O.TROCA, O.SITUACAO,
                           ( SELECT MAX(OP.VLRPRECOMEDIO)     FROM TBOPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDATIVO = O.IDATIVO AND OP.IDLANC = O.ID ) AS VLRPRECOMEDIO, 
                           ( SELECT SUM(OP.TOTVLRVALORIZACAO) FROM TBOPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDATIVO = O.IDATIVO AND OP.IDLANC = O.ID ) AS TOTVLRVALORIZACAO, 
                           ( SELECT SUM(OP.PERCVALORIZACAO)   FROM TBOPERACAO OP WHERE OP.IDUSUARIO = O.IDUSUARIO AND OP.IDATIVO = O.IDATIVO AND OP.IDLANC = O.ID ) AS PERCVALORIZACAO
                    FROM TBLANCAMENTO O
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = O.IDATIVO )
                      LEFT  JOIN TBCORRETORA C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO AND O.QUANTPEND > 0
                """

        if codigo: query += " AND A.CODIGO = :CODIGO "
        if data: query += " AND O.DATA = :DATA"
        if tipo: query += " AND O.TIPO = :TIPO "

        query += " ORDER BY O.ID "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        if data: params['DATA'] = data
        if tipo: params['TIPO'] = tipo

        return db.execute(query, params).fetchall()

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int = None, id: int = None):
        query = """ SELECT O.ID, O.IDUSUARIO, O.IDATIVO AS IDATIVO, A.CODIGO AS CODIGOATIVO, A.SITUACAO AS SITUACAOATIVO, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
                           O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, O.TROCA, O.SITUACAO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO
                    FROM TBLANCAMENTO O
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = O.IDATIVO )
                      LEFT JOIN TBCORRETORA C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.ID = :ID AND O.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        return db.execute(query, params).first()

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT O.ID, O.IDUSUARIO, O.IDATIVO AS IDATIVO, A.CODIGO AS CODIGOATIVO, A.SITUACAO AS SITUACAOATIVO, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
                           O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, O.TROCA, O.SITUACAO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO
                    FROM TBLANCAMENTO O
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = O.IDATIVO     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO AND A.CODIGO = :CODIGO
                    ORDER BY O.DATA, O.ID, O.TIPO 
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        return db.execute(query, params)

    @classmethod
    async def buscar_por_day_trade(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, tipo: str = None):
        query = ''
        if tipo == 'C' or tipo == 'B':
            query = """ SELECT OC.ID, OC.IDUSUARIO, OC.IDATIVO AS IDATIVO, AC.CODIGO AS CODIGOATIVO, AC.SITUACAO AS SITUACAOATIVO, OC.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
                               OC.TIPO, OC.DATA, OC.QUANT, OC.QUANTPEND, OC.VLRPRECO, OC.TOTVLRPRECO, OC.VLRTXLIQUIDACAO, OC.VLRTXEMOLUMENTOS, OC.VLRTXCORRETAGEM, OC.VLRTXISS, OC.VLRTXIRRF, 
                               OC.VLRTXOUTRAS, OC.TOTVLRTX, OC.TOTVLR, OC.VLRCUSTO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO, OC.TROCA, OC.SITUACAO 
                        FROM TBLANCAMENTO OC
                          INNER JOIN TBEMPRESA_ATIVO AC ON ( AC.ID = OC.IDATIVO )	
                          LEFT  JOIN TBCORRETORA C ON ( C.ID = OC.IDCORRETORA )
                        WHERE OC.IDUSUARIO = :IDUSUARIO AND AC.CODIGO = :CODIGO AND OC.TIPO IN ('C', 'B')
                          AND EXISTS( SELECT 1 FROM TBLANCAMENTO OV WHERE OV.IDUSUARIO = OC.IDUSUARIO AND OV.IDATIVO = OC.IDATIVO AND OV.TIPO = 'V' AND OV.DATA = OC.DATA ) 
                        ORDER BY OC.DATA, OC.ID
                    """
        if tipo == 'V':
            query = """ SELECT OV.ID, OV.IDUSUARIO, OV.IDATIVO AS IDATIVO, AV.CODIGO AS CODIGOATIVO, AV.SITUACAO AS SITUACAOATIVO, OV.IDCORRETORA AS IDCORRETORA, 
                               C.NOME AS NOMECORRETORA, OV.TIPO, OV.DATA, OV.QUANT, OV.QUANTPEND, OV.VLRPRECO, OV.TOTVLRPRECO, OV.VLRTXLIQUIDACAO, OV.VLRTXEMOLUMENTOS, 
                               OV.VLRTXCORRETAGEM, OV.VLRTXISS, OV.VLRTXIRRF, OV.VLRTXOUTRAS, OV.TOTVLRTX, OV.TOTVLR, OV.VLRCUSTO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 
                               0.00 AS PERCVALORIZACAO, OV.TROCA, OV.SITUACAO 
                        FROM TBLANCAMENTO OV
                          INNER JOIN TBEMPRESA_ATIVO AV ON ( AV.ID = OV.IDATIVO )	
                          LEFT JOIN TBCORRETORA C  ON ( C.ID = OV.IDCORRETORA )
                        WHERE OV.IDUSUARIO = :IDUSUARIO
                          AND AV.CODIGO = :CODIGO
                          AND OV.TIPO = 'V'
                          AND EXISTS( SELECT 1 FROM TBLANCAMENTO OC WHERE OC.IDUSUARIO = OV.IDUSUARIO AND OC.IDATIVO = OV.IDATIVO AND OC.TIPO IN ('C', 'B') AND OC.DATA = OV.DATA AND OC.ID < OV.ID )  
                        ORDER BY OV.DATA, OV.ID DESC
                    """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        return db.execute(query, params)

    @classmethod
    async def buscar_por_qtde_pend_maior_que_zero(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT O.ID, O.IDUSUARIO, O.IDATIVO AS IDATIVO, A.CODIGO AS CODIGOATIVO, A.SITUACAO AS SITUACAOATIVO, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
                           O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO, O.TROCA, O.SITUACAO 
                    FROM TBLANCAMENTO O
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = O.IDATIVO     )	
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO AND A.CODIGO = :CODIGO AND O.QUANTPEND > 0 AND O.TIPO IN ('C', 'V', 'B')
                    ORDER BY DATA, TIPO, ID
                    """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        return db.execute(query, params).fetchall()

    @classmethod
    async def buscar_desdobro_grupamento(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT O.ID, O.IDUSUARIO, O.IDATIVO AS IDATIVO, A.CODIGO AS CODIGOATIVO, A.SITUACAO AS SITUACAOATIVO, O.IDCORRETORA AS IDCORRETORA, C.NOME AS NOMECORRETORA, 
                           O.TIPO, O.DATA, O.QUANT, O.QUANTPEND, O.VLRPRECO, O.TOTVLRPRECO, O.VLRTXLIQUIDACAO, O.VLRTXEMOLUMENTOS, O.VLRTXCORRETAGEM, O.VLRTXISS, O.VLRTXIRRF, 
                           O.VLRTXOUTRAS, O.TOTVLRTX, O.TOTVLR, O.VLRCUSTO, 0.00 AS VLRPRECOMEDIO, 0.00 AS TOTVLRVALORIZACAO, 0.00 AS PERCVALORIZACAO, O.TROCA, O.SITUACAO 
                    FROM TBLANCAMENTO O
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = O.IDATIVO     )	
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
                      AND A.CODIGO    = :CODIGO
                      AND O.TIPO      IN ('D', 'G')
                      AND O.QUANT     > 0
                    ORDER BY DATA, TIPO, ID
                    """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        return db.execute(query, params).fetchall()

    @classmethod
    async def buscar_menor_ano(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        query = """ SELECT SUBSTRING(MIN(L.DATA), 1, 4) AS MENORANO FROM TBLANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO """
        if id_ativo: query += """ AND L.IDATIVO = :IDATIVO """
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_ativo: params['IDATIVO'] = id_ativo
        return db.execute(query, params)

    @classmethod
    async def buscar_maior_ano(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        query = """ SELECT SUBSTRING(MAX(L.DATA), 1, 4) AS MAIORANO FROM TBLANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO """
        if id_ativo: query += """ AND L.IDATIVO = :IDATIVO """
        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_ativo: params['IDATIVO'] = id_ativo
        return db.execute(query, params)

    @classmethod
    async def buscar_total_compra(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None, dt_fim: str = None):
        query = """ SELECT SUM(L.QUANT) AS QTDE FROM TBLANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO AND L.IDATIVO = :IDATIVO AND L.TIPO IN ( 'C', 'B') """
        if dt_fim: query += """ AND L.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDATIVO'] = id_ativo
        if dt_fim: params['DATAFIM'] = dt_fim
        rows = db.execute(query, params).first()
        return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0

    @classmethod
    async def buscar_total_venda(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(L.QUANT) AS QTDE FROM TBLANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO AND L.IDATIVO = :IDATIVO AND L.TIPO = 'V' """
        if id_lanc: query += """ AND L.ID <> :ID """
        if dt_fim: query += """ AND L.DATA <= :DATAFIM """
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDATIVO'] = id_ativo
        if dt_fim: params['ID'] = id_lanc
        if dt_fim: params['DATAFIM'] = dt_fim
        rows = db.execute(query, params).first()
        return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0

    @classmethod
    async def buscar_quant_operacao(cls, db: _orm.Session, id_usuario: int = None, situacao: str = None, tipo: str = None):
        try:

            query = " SELECT COUNT(1) AS QTDE FROM TBLANCAMENTO L WHERE L.IDUSUARIO = :IDUSUARIO "
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
        query = """ SELECT COUNT(1) AS QTDE FROM TBLANCAMENTO L WHERE 1 = 1 """
        if tipo: query += """ AND L.TIPO = :TIPO """
        params = {}
        if tipo: params['TIPO'] = tipo
        rows = db.execute(query, params).first()
        return rows[0] if rows and rows[0] and rows[0] > 0 else 0

    @classmethod
    async def buscar_dados_grid_irpf(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT MAX(A.CODIGO) AS CODIGO, MAX(E.CNPJ) AS CNPJ, MAX(E.RAZAOSOCIAL) AS RAZAOSOCIAL, SUM(L.TOTVLR) AS TOTVLR
                    FROM TBLANCAMENTO L
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = L.IDATIVO )
                      INNER JOIN TBEMPRESA E ON ( E.ID = A.IDEMPRESA )
                    WHERE L.IDUSUARIO = :IDUSUARIO AND L.TIPO = :TIPO AND L.DATA >= :DATAINICIO AND L.DATA <= :DATAFIM
                    GROUP BY L.IDATIVO
                    ORDER BY E.RAZAOSOCIAL
                """
        params = {'IDUSUARIO': id_usuario, 'TIPO': tipo, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        return db.execute(query, params)

    @classmethod
    async def buscar_lista_datas_day_trade(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT DISTINCT LV.DATA
                    FROM TBLANCAMENTO LV
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = LV.IDATIVO )
                    WHERE LV.IDUSUARIO = :IDUSUARIO
                      AND A.CODIGO     = :CODIGO
                      AND LV.TIPO      = 'V'
                      AND EXISTS( SELECT 1
                                  FROM TBLANCAMENTO LC
                                  WHERE LC.IDUSUARIO = LV.IDUSUARIO
                                    AND LC.IDATIVO   = LV.IDATIVO
                                    AND LC.TIPO      IN ('C', 'B')
                                    AND LC.DATA      = LV.DATA
                                    AND LC.ID        < LV.ID
                                )
                    ORDER BY LV.DATA
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        return db.execute(query, params).fetchall()

    @classmethod
    async def atualizar_qtd_pend_situacao(cls, db: _orm.Session, id_usuario: int, id_lanc: int, qtd_pend: int, situacao: str, commit: bool = True):
        try:
            query = "UPDATE TBLANCAMENTO SET QUANTPEND = :QUANTPEND, SITUACAO = :SITUACAO WHERE IDUSUARIO = :IDUSUARIO AND ID = :ID "
            params = {'IDUSUARIO': id_usuario, 'ID': id_lanc, 'QUANTPEND': qtd_pend, 'SITUACAO': situacao}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            raise

    @classmethod
    async def resetar_ativos(cls, db: _orm.Session, id_usuario: int, id_ativo: int, commit: bool = True):
        try:
            query = "UPDATE TBLANCAMENTO SET QUANTPEND = QUANT, SITUACAO = 'P' WHERE IDUSUARIO = :IDUSUARIO AND IDATIVO = :IDATIVO"
            params = {'IDUSUARIO': id_usuario, 'IDATIVO': id_ativo}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBLANCAMENTO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, commit: bool = True):
        try:
            db.add(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, commit: bool = True):
        try:
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            raise
