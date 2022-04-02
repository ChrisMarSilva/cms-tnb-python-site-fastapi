# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_carteira_etf import UsuarioCarteiraEtfModel
# from app.models.log_erro import LogErro


class UsuarioCarteiraEtfRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session, id: int = None, id_carteira: int = None, id_indice: int = None):
        filters = []
        if id: filters.append(UsuarioCarteiraEtfModel.id == id)
        if id_carteira: filters.append(UsuarioCarteiraEtfModel.id_carteira == id_carteira)
        if id_indice: filters.append(UsuarioCarteiraEtfModel.id_indice == id_indice)
        try:
            return db.query(UsuarioCarteiraEtfModel).filter(*filters).order_by(UsuarioCarteiraEtfModel.id).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioCarteiraEtfModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, id_carteira: int = None, situacao: str = None):
        query = """ SELECT FND.ID            AS ID, 
                           FND.IDCARTEIRA    AS IDCARTEIRA, 
                           C.DESCRICAO       AS DESCRICAOCARTEIRA,
                           C.TIPO            AS TIPOCARTEIRA,
                           FND.IDINDICE      AS IDINDICE, 
                           F.NOME            AS NOMEINDICE, 
                           F.CODIGO          AS CODIGOINDICE, 
                           F.SITUACAO        AS SITUACAOINDICE, 
                           FND.QUANT         AS QUANT, 
                           FND.QUANTBONUS    AS QUANTBONUS, 
                           FND.VLRPRECOMEDIO AS VLRPRECOMEDIO,
                           FND.VLRPRECOTETO  AS VLRPRECOTETO,  
                           FND.PERCENTBALAC  AS PERCENTBALAC,  
                           FND.NOTABALAC     AS NOTABALAC,  
                           FND.SITUACAO      AS SITUACAO ,  
                           COT.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO,  
                           COT.VLRPRECOANTERIOR AS VLRPRECOANTERIOR,  
                           COT.VLRVARIACAO AS VLRVARIACAO 
                    FROM TBCARTEIRA_INDICE       FND
                      INNER JOIN TBCARTEIRA      C ON ( C.ID = FND.IDCARTEIRA )
                      INNER JOIN TBETF_INDICE    F ON ( F.ID = FND.IDINDICE   )
                      LEFT JOIN TBETF_INDICE_COTACAO COT ON ( COT.IDINDICE = FND.IDINDICE )
                    WHERE C.IDUSUARIO = :IDUSUARIO
                """
        if id_carteira: query += " AND FND.IDCARTEIRA = :IDCARTEIRA "
        if situacao: query += " AND FND.SITUACAO = :SITUACAO "
        query += " ORDER BY F.CODIGO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_carteira: params['IDCARTEIRA'] = id_carteira
        if situacao: params['SITUACAO'] = situacao

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_simples(cls, db: _orm.Session, id_usuario: int = None, id_carteira: int = None, situacao: str = None):
        query = """ SELECT FND.ID AS ID, 
                           FND.IDCARTEIRA AS IDCARTEIRA, 
                           FND.IDINDICE AS IDINDICE, 
                           F.CODIGO AS CODIGOINDICE, 
                           FND.QUANT AS QUANT, 
                           FND.QUANTBONUS AS QUANTBONUS, 
                           FND.VLRPRECOMEDIO AS VLRPRECOMEDIO,
                           FND.VLRPRECOTETO AS VLRPRECOTETO,  
                           FND.PERCENTBALAC AS PERCENTBALAC,  
                           FND.NOTABALAC AS NOTABALAC,   
                           FND.SITUACAO AS SITUACAO,  
                           COT.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO,  
                           COT.VLRPRECOANTERIOR AS VLRPRECOANTERIOR,  
                           COT.VLRVARIACAO AS VLRVARIACAO 
                    FROM TBCARTEIRA_INDICE FND
                      INNER JOIN TBCARTEIRA C ON ( C.ID = FND.IDCARTEIRA )
                      INNER JOIN TBETF_INDICE F ON ( F.ID = FND.IDINDICE )
                      LEFT JOIN TBETF_INDICE_COTACAO COT ON ( COT.IDINDICE = FND.IDINDICE )
                    WHERE C.IDUSUARIO = :IDUSUARIO
                """
        if id_carteira: query += " AND FND.IDCARTEIRA = :IDCARTEIRA "
        if situacao: query += " AND FND.SITUACAO = :SITUACAO "
        query += " ORDER BY F.CODIGO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_carteira: params['IDCARTEIRA'] = id_carteira
        if situacao: params['SITUACAO'] = situacao

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise


    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int = None, id: int = None):
        query = """ SELECT FND.ID            AS ID, 
                           FND.IDCARTEIRA    AS IDCARTEIRA, 
                           C.DESCRICAO       AS DESCRICAOCARTEIRA,
                           C.TIPO            AS TIPOCARTEIRA,
                           FND.IDINDICE      AS IDINDICE, 
                           F.NOME            AS NOMEINDICE, 
                           F.CODIGO          AS CODIGOINDICE, 
                           F.SITUACAO        AS SITUACAOINDICE, 
                           FND.QUANT         AS QUANT, 
                           FND.QUANTBONUS    AS QUANTBONUS, 
                           FND.VLRPRECOMEDIO AS VLRPRECOMEDIO,
                           FND.VLRPRECOTETO  AS VLRPRECOTETO,  
                           FND.PERCENTBALAC  AS PERCENTBALAC,  
                           FND.NOTABALAC    AS NOTABALAC,  
                           FND.SITUACAO      AS SITUACAO 
                    FROM TBCARTEIRA_INDICE       FND
                      INNER JOIN TBCARTEIRA      C ON ( C.ID = FND.IDCARTEIRA )
                      INNER JOIN TBETF_INDICE    F ON ( F.ID = FND.IDINDICE   )
                    WHERE FND.ID      = :ID
                      AND C.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_ativo(cls, db: _orm.Session, id_usuario: int = None, id_indice: int = None):
        query = """ SELECT FND.ID            AS ID, 
                           FND.IDCARTEIRA    AS IDCARTEIRA, 
                           C.DESCRICAO       AS DESCRICAOCARTEIRA,
                           C.TIPO            AS TIPOCARTEIRA,
                           FND.IDINDICE      AS IDINDICE, 
                           F.NOME            AS NOMEINDICE, 
                           F.CODIGO          AS CODIGOINDICE, 
                           F.SITUACAO        AS SITUACAOINDICE, 
                           FND.QUANT         AS QUANT, 
                           FND.QUANTBONUS    AS QUANTBONUS, 
                           FND.VLRPRECOMEDIO AS VLRPRECOMEDIO,
                           FND.VLRPRECOTETO  AS VLRPRECOTETO,  
                           FND.PERCENTBALAC  AS PERCENTBALAC,  
                           FND.NOTABALAC    AS NOTABALAC,  
                           FND.SITUACAO      AS SITUACAO 
                    FROM TBCARTEIRA_INDICE       FND
                      INNER JOIN TBCARTEIRA      C ON ( C.ID = FND.IDCARTEIRA )
                      INNER JOIN TBETF_INDICE    F ON ( F.ID = FND.IDINDICE   )
                    WHERE C.IDUSUARIO  = :IDUSUARIO
                      AND FND.IDINDICE = :IDINDICE
                """
        params = {'IDUSUARIO': id_usuario, 'IDINDICE': id_indice}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid_radar(cls, db: _orm.Session, id_usuario: int = None):
        query = """ SELECT F.NOME                 AS RAZAOSOCIAL, 
                           F.CODIGO               AS CODIGOATIVO, 
                           'ETF'                  AS DESCRICAOSETOR, 
                           'ETF'                  AS DESCRICAOSUBSETOR, 
                           'ETF'                  AS DESCRICAOSEGMENTO, 
                           CO.VLRPRECOFECHAMENTO  AS PRECO, 
                           CO.VLRVARIACAO         AS VARIACAO 
                    FROM TBCARTEIRA_INDICE           FND
                      INNER JOIN TBCARTEIRA          C  ON ( C.ID        = FND.IDCARTEIRA )
                      INNER JOIN TBETF_INDICE        F  ON ( F.ID        = FND.IDINDICE   )
                      LEFT JOIN TBETF_INDICE_COTACAO CO ON ( CO.IDINDICE = FND.IDINDICE   )
                    WHERE C.IDUSUARIO = :IDUSUARIO
                      AND FND.SITUACAO = 'A'
                    ORDER BY F.NOME, F.CODIGO
                """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def atualizar_preco_teto(cls, db: _orm.Session, id: int, preco_teto: float, commit: bool = True):
        try:
            query = """ UPDATE TBCARTEIRA_INDICE SET VLRPRECOTETO = :VLRPRECOTETO WHERE ID = :ID """
            params = {'VLRPRECOTETO': preco_teto, 'ID': id}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def atualizar_percent_balanc(cls, db: _orm.Session, id: int, percent_balac: float, commit: bool = True):
        try:
            query = """ UPDATE TBCARTEIRA_INDICE SET PERCENTBALAC = :PERCENTBALAC WHERE ID = :ID """
            params = {'PERCENTBALAC': percent_balac, 'ID': id}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def atualizar_nota_balanc(cls, db: _orm.Session, id: int, nota_balac: int, commit: bool = True):
        try:
            query = """ UPDATE TBCARTEIRA_INDICE SET NOTABALAC = :NOTABALAC WHERE ID = :ID """
            params = {'NOTABALAC': nota_balac, 'ID': id}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def atualizar_id_carteira(cls, db: _orm.Session, id_usuario: int, id: int, id_portfolio: int, commit: bool = True):
        try:
            query = "UPDATE TBCARTEIRA_INDICE SET IDCARTEIRA = :IDCARTEIRA WHERE ID = :ID AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO )"
            params = {'IDUSUARIO': id_usuario, 'ID': id, 'IDCARTEIRA': id_portfolio}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def atualizar_novo_id_carteira(cls, db: _orm.Session, id_usuario: int, id_portfolio_old: int, id_portfolio_new: int, commit: bool = True):
        try:
            query = "UPDATE TBCARTEIRA_INDICE SET IDCARTEIRA = :IDCARTEIRA_NEW WHERE IDCARTEIRA = :IDCARTEIRA_OLD AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO )"
            params = {'IDUSUARIO': id_usuario, 'IDCARTEIRA_OLD': id_portfolio_old, 'IDCARTEIRA_NEW': id_portfolio_new}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def trocar_ativos(cls, db: _orm.Session, id_usuario: int, id_indice_atual: int, id_indice_novo: int, commit: bool = True):
        try:
            params = {'IDUSUARIO': id_usuario, 'IDINDICEATUAL': id_indice_atual, 'IDINDICENOVO': id_indice_novo}
            db.execute("UPDATE TBETF_LANCAMENTO       SET IDINDICE = :IDINDICENOVO WHERE IDUSUARIO = :IDUSUARIO AND IDINDICE = :IDINDICEATUAL ", params)
            db.execute("UPDATE TBETF_OPERACAO         SET IDINDICE = :IDINDICENOVO WHERE IDUSUARIO = :IDUSUARIO AND IDINDICE = :IDINDICEATUAL ", params)
            db.execute("UPDATE TBUSUARIO_ACOMP_INDICE SET IDINDICE = :IDINDICENOVO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO) AND IDINDICE = :IDINDICEATUAL ", params)
            try:
                db.execute("UPDATE TBCARTEIRA_INDICE      SET IDINDICE = :IDINDICENOVO WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO) AND IDINDICE = :IDINDICEATUAL ", params)
            except Exception as e:
                pass
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def resetar_ativos(cls, db: _orm.Session, id_usuario: int, id_indice: int, commit: bool = True):
        try:
            query = "UPDATE TBCARTEIRA_INDICE SET QUANT = 0, QUANTBONUS = 0, VLRPRECOMEDIO = 0.00, SITUACAO = 'F' WHERE IDINDICE = :IDINDICE AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) "
            params = {'IDUSUARIO': id_usuario, 'IDINDICE': id_indice}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_carteira(cls, db: _orm.Session, id_usuario: int, id_carteira: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_INDICE WHERE IDCARTEIRA = :IDCARTEIRA AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) """
            params = {'IDCARTEIRA': id_carteira, 'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_INDICE WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) """
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioCarteiraEtfModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioCarteiraEtfModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
