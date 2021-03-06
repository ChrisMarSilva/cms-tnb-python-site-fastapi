# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_bdr_empresa_operacao import UsuarioBDREmpresaOperacaoModel
# # from app.models.log_erro import LogErro


class UsuarioBDREmpresaOperacaoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, dt_ini: str = None, dt_fim: str = None, categoria: str = None, tipo: str = None):
        try:

            filters = []
            if id_usuario: filters.append(UsuarioBDREmpresaOperacaoModel.id_usuario == id_usuario)
            if id_bdr: filters.append(UsuarioBDREmpresaOperacaoModel.id_bdr == id_bdr)
            if dt_ini: filters.append(UsuarioBDREmpresaOperacaoModel.data >= dt_ini)
            if dt_fim: filters.append(UsuarioBDREmpresaOperacaoModel.data <= dt_fim)
            if categoria: filters.append(UsuarioBDREmpresaOperacaoModel.categoria == categoria)
            if tipo: filters.append(UsuarioBDREmpresaOperacaoModel.tipo == tipo)

            return db.query(UsuarioBDREmpresaOperacaoModel).filter(*filters).order_by(UsuarioBDREmpresaOperacaoModel.id).all()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioBDREmpresaOperacaoModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(UsuarioBDREmpresaOperacaoModel).filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_ativo(cls, db: _orm.Session, id_bdr: int):
        try:
            return db.query(UsuarioBDREmpresaOperacaoModel).filter_by(id_bdr=id_bdr).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_menor_ano(cls, db: _orm.Session, id_usuario: int = None):
        try:
            return db.query(db.func.min(UsuarioBDREmpresaOperacaoModel.data)).filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_maior_ano(cls, db: _orm.Session, id_usuario: int = None):
        try:
            return db.query(db.func.max(UsuarioBDREmpresaOperacaoModel.data)).filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None, categoria: str = None, tipo: str = None, troca: str = None):
        query = """ SELECT O.ID, O.IDLANC, O.IDUSUARIO, O.IDBDR AS IDBDR, A.CODIGO AS CODIGOBDR, A.SITUACAO AS SITUACAOBDR, O.IDCORRETORA AS IDCORRETORA, 
                           C.NOME AS NOMECORRETORA, O.TIPO, O.CATEGORIA, O.DATA, O.QUANT, O.QUANTACUMULADO, O.VLRCUSTO, O.TOTVLRCUSTO, O.VLRPRECOMEDIO, 
                           O.TOTVLRVALORIZACAO, O.PERCVALORIZACAO, O.TROCA, O.SITUACAO 
                    FROM TBBDR_OPERACAO O
                      INNER JOIN TBBDR_EMPRESA   A ON ( A.ID = O.IDBDR     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
                """
        if codigo: query += " AND A.CODIGO = :CODIGO "
        if dt_ini: query += " AND O.DATA >= :DATAINICIO "
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        if categoria: query += " AND O.CATEGORIA = :CATEGORIA "
        if tipo: query += " AND O.TIPO = :TIPO "
        if troca: query += " AND IFNULL(O.TROCA, 'N') = :TROCA "
        query += " ORDER BY O.DATA, O.CATEGORIA, O.TIPO, O.ID "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim
        if categoria: params['CATEGORIA'] = categoria
        if tipo: params['TIPO'] = tipo
        if troca: params['TROCA'] = troca

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int = None, id: int = None):
        query = """ SELECT O.ID, O.IDLANC, O.IDUSUARIO, O.IDBDR AS IDBDR, A.CODIGO AS CODIGOBDR, A.SITUACAO AS SITUACAOBDR, O.IDCORRETORA AS IDCORRETORA, 
                           C.NOME AS NOMECORRETORA, O.TIPO, O.CATEGORIA, O.DATA, O.QUANT, O.QUANTACUMULADO, O.VLRCUSTO, O.TOTVLRCUSTO, O.VLRPRECOMEDIO, 
                           O.TOTVLRVALORIZACAO, O.PERCVALORIZACAO, O.TROCA, O.SITUACAO 
                    FROM TBBDR_OPERACAO O
                      INNER JOIN TBBDR_EMPRESA A ON ( A.ID = O.IDBDR     )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.ID        = :ID
                      AND O.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT O.ID, O.IDLANC, O.IDUSUARIO, O.IDBDR AS IDBDR, A.CODIGO AS CODIGOBDR, A.SITUACAO AS SITUACAOBDR, O.IDCORRETORA AS IDCORRETORA, 
                           C.NOME AS NOMECORRETORA, O.TIPO, O.CATEGORIA, O.DATA, O.QUANT, O.QUANTACUMULADO, O.VLRCUSTO, O.TOTVLRCUSTO, O.VLRPRECOMEDIO, 
                           O.TOTVLRVALORIZACAO, O.PERCVALORIZACAO, O.TROCA, O.SITUACAO 
                    FROM TBBDR_OPERACAO O
                      INNER JOIN TBBDR_EMPRESA A ON ( A.ID = O.IDBDR )
                      LEFT  JOIN TBCORRETORA     C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
                      AND A.CODIGO    = :CODIGO
                    ORDER BY O.DATA, O.TIPO 
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_quant_ativo(cls, db: _orm.Session, id_usuario: int = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBBDR_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.SITUACAO = 'A' """
        params = {'IDUSUARIO': id_usuario}
        try:
            rows = db.execute(query, params).first()
            return int(rows[0]) if rows and rows[0] and int(rows[0]) > 0 else 0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_preco_medio(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
        query = """ SELECT O.VLRPRECOMEDIO FROM TBBDR_OPERACAO O WHERE O.ID = ( SELECT MAX(OO.ID) FROM TBBDR_OPERACAO OO WHERE OO.IDUSUARIO = :IDUSUARIO AND OO.IDBDR = :IDBDR AND OO.QUANTACUMULADO > 0 AND OO.SITUACAO = 'A' """
        if dt_fim: query += " AND OO.DATA <= :DATAFIM "
        query += " ) "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDBDR'] = id_bdr
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_preco_medio_antes(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
        query = """ SELECT O.VLRPRECOMEDIO FROM TBBDR_OPERACAO O WHERE O.ID = ( SELECT MAX(OO.ID) FROM TBBDR_OPERACAO OO WHERE OO.IDUSUARIO = :IDUSUARIO and OO.IDBDR = :IDBDR AND OO.QUANTACUMULADO > 0 AND OO.SITUACAO = 'A' """
        if dt_fim: query += " AND OO.DATA < :DATAFIM "
        query += " ) "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDBDR'] = id_bdr
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_total_compra(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.QUANT) AS QTDE FROM TBBDR_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDBDR = :IDBDR AND O.TIPO = 'C' """
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDBDR'] = id_bdr
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_total_bonus(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.QUANT) AS QTDE FROM TBBDR_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDBDR = :IDBDR AND O.TIPO = 'B' """
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDBDR'] = id_bdr
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_total_venda(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.QUANT) AS QTDE FROM TBBDR_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDBDR = :IDBDR AND O.TIPO = 'V' """
        if id_lanc: query += " AND O.ID <> :ID "
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDBDR'] = id_bdr
        if id_lanc: params['ID'] = id_lanc
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_valor_total_compra(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBBDR_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDBDR = :IDBDR AND O.TIPO = 'C' """
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDBDR'] = id_bdr
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_valor_total_bonus(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBBDR_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDBDR = :IDBDR AND O.TIPO = 'B' """
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDBDR'] = id_bdr
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_valor_total_venda(cls, db: _orm.Session, id_usuario: int = None, id_bdr: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBBDR_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDBDR = :IDBDR AND O.TIPO = 'V' """
        if id_lanc: query += " AND O.ID <> :ID "
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDBDR'] = id_bdr
        if id_lanc: params['ID'] = id_lanc
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def resetar_ativos(cls, db: _orm.Session, id_usuario: int, id_bdr: int, commit: bool = True):
        try:
            query = "DELETE FROM TBBDR_OPERACAO WHERE IDUSUARIO = :IDUSUARIO AND IDBDR = :IDBDR "
            params = {'IDUSUARIO': id_usuario, 'IDBDR': id_bdr}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo_ativo(cls, db: _orm.Session, id_usuario: int, id_bdr: int, commit: bool = True):
        try:
            query = "DELETE FROM TBBDR_OPERACAO WHERE IDBDR = :IDBDR AND IDUSUARIO = :IDUSUARIO"
            params = {'IDBDR': id_bdr, 'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBBDR_OPERACAO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioBDREmpresaOperacaoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioBDREmpresaOperacaoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
