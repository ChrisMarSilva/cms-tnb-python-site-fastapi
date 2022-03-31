# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_carteira_acao import UsuarioCarteiraAcaoModel
# # from app.models.log_erro import LogErro


class UsuarioCarteiraAcaoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session, id: int = None, id_carteira: int = None, id_ativo: int = None):
        filters = []
        if id: filters.append(cls, db: _orm.id == id)
        if id_carteira: filters.append(cls, db: _orm.id_carteira == id_carteira)
        if id_ativo: filters.append(cls, db: _orm.id_ativo == id_ativo)
        try:
            return cls.query.filter(*filters).order_by(cls, db: _orm.id).all()
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
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, id_carteira: int = None, situacao: str = None, ordem: str = None):
        query = """ SELECT ATV.ID            AS ID, 
                           ATV.IDCARTEIRA    AS IDCARTEIRA, 
                           C.DESCRICAO       AS DESCRICAOCARTEIRA,
                           C.TIPO            AS TIPOCARTEIRA,
                           ATV.IDATIVO       AS IDATIVO, 
                           A.CODIGO          AS CODIGOATIVO,
                           E.NOME            AS NOMEEMPRESA,
                           E.RAZAOSOCIAL     AS RAZAOSOCIALEMPRESA,
                           E.NOMRESUMIDO     AS NOMRESUMIDOEMPRESA,
                           ST.ID             AS IDSETOR,
                           ST.DESCRICAO      AS DESCRICAOSETOR,
                           SB.ID             AS IDSUBSETOR,
                           SB.DESCRICAO      AS DESCRICAOSUBSETOR,
                           SG.ID             AS IDSEGMENTO,
                           SG.DESCRICAO      AS DESCRICAOSEGMENTO,
                           ATV.QUANT         AS QUANT, 
                           ATV.QUANTBONUS    AS QUANTBONUS, 
                           ATV.VLRPRECOMEDIO AS VLRPRECOMEDIO,
                           ATV.VLRPRECOTETO  AS VLRPRECOTETO,  
                           ATV.PERCENTBALAC  AS PERCENTBALAC,  
                           ATV.NOTABALAC     AS NOTABALAC,  
                           ATV.SITUACAO      AS SITUACAO ,  
                           COT.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO,  
                           COT.VLRPRECOANTERIOR AS VLRPRECOANTERIOR,  
                           COT.VLRVARIACAO AS VLRVARIACAO 
                    FROM TBCARTEIRA_ATIVO           ATV
                      INNER JOIN TBCARTEIRA         C  ON ( C.ID  = ATV.IDCARTEIRA )
                      INNER JOIN TBEMPRESA_ATIVO    A  ON ( A.ID  = ATV.IDATIVO    )
                      INNER JOIN TBEMPRESA          E  ON ( E.ID  = A.IDEMPRESA    )
                      INNER JOIN TBEMPRESA_SETOR    ST ON ( ST.ID = E.IDSETOR      )
                      INNER JOIN TBEMPRESA_SUBSETOR SB ON ( SB.ID = E.IDSUBSETOR   )
                      INNER JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO   )
                      LEFT JOIN TBEMPRESA_ATIVOCOTACAO COT ON ( COT.IDATIVO = ATV.IDATIVO )
                    WHERE C.IDUSUARIO = :IDUSUARIO
                """
        if id_carteira: query += " AND ATV.IDCARTEIRA = :IDCARTEIRA "
        if situacao: query += " AND ATV.SITUACAO = :SITUACAO "
        if ordem: query += " ORDER BY A.CODIGO "
        else: query += " ORDER BY ST.DESCRICAO, SB.DESCRICAO, SG.DESCRICAO, A.CODIGO "

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
        query = """ SELECT ATV.ID AS ID, 
                           ATV.IDCARTEIRA AS IDCARTEIRA, 
                           ATV.IDATIVO AS IDATIVO, 
                           A.CODIGO AS CODIGOATIVO,
                           ATV.QUANT AS QUANT, 
                           ATV.QUANTBONUS AS QUANTBONUS, 
                           ATV.VLRPRECOMEDIO AS VLRPRECOMEDIO,
                           ATV.VLRPRECOTETO AS VLRPRECOTETO,  
                           ATV.PERCENTBALAC AS PERCENTBALAC,  
                           ATV.NOTABALAC AS NOTABALAC,   
                           ATV.SITUACAO AS SITUACAO,  
                           COT.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO,  
                           COT.VLRPRECOANTERIOR AS VLRPRECOANTERIOR,  
                           COT.VLRVARIACAO AS VLRVARIACAO 
                    FROM TBCARTEIRA_ATIVO ATV
                      INNER JOIN TBCARTEIRA C ON ( C.ID = ATV.IDCARTEIRA )
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = ATV.IDATIVO )
                      LEFT JOIN TBEMPRESA_ATIVOCOTACAO COT ON ( COT.IDATIVO = ATV.IDATIVO )
                    WHERE C.IDUSUARIO = :IDUSUARIO
                """
        if id_carteira: query += " AND ATV.IDCARTEIRA = :IDCARTEIRA "
        if situacao: query += " AND ATV.SITUACAO = :SITUACAO "
        query += " ORDER BY A.CODIGO "

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
        query = """ SELECT ATV.ID            AS ID, 
                            ATV.IDCARTEIRA    AS IDCARTEIRA, 
                            C.DESCRICAO       AS DESCRICAOCARTEIRA,
                            C.TIPO            AS TIPOCARTEIRA,
                            ATV.IDATIVO       AS IDATIVO, 
                            A.CODIGO          AS CODIGOATIVO,
                            ST.ID             AS IDSETOR,
                            ST.DESCRICAO      AS DESCRICAOSETOR,
                            SB.ID             AS IDSUBSETOR,
                            SB.DESCRICAO      AS DESCRICAOSUBSETOR,
                            SG.ID             AS IDSEGMENTO,
                            SG.DESCRICAO      AS DESCRICAOSEGMENTO,
                            ATV.QUANT         AS QUANT, 
                            ATV.QUANTBONUS    AS QUANTBONUS, 
                            ATV.VLRPRECOMEDIO AS VLRPRECOMEDIO,
                            ATV.VLRPRECOTETO  AS VLRPRECOTETO,  
                            ATV.PERCENTBALAC  AS PERCENTBALAC,  
                            ATV.NOTABALAC     AS NOTABALAC,  
                            ATV.SITUACAO      AS SITUACAO 
                    FROM TBCARTEIRA_ATIVO             ATV
                        INNER JOIN TBCARTEIRA         C  ON ( C.ID  = ATV.IDCARTEIRA )
                        INNER JOIN TBEMPRESA_ATIVO    A  ON ( A.ID  = ATV.IDATIVO    )
                        INNER JOIN TBEMPRESA          E  ON ( E.ID  = A.IDEMPRESA    )
                        INNER JOIN TBEMPRESA_SETOR    ST ON ( ST.ID = E.IDSETOR      )
                        INNER JOIN TBEMPRESA_SUBSETOR SB ON ( SB.ID = E.IDSUBSETOR   )
                        INNER JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO   )
                    WHERE ATV.ID      = :ID
                      AND C.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}

        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_ativo(cls, db: _orm.Session, id_usuario: int = None, id_ativo: int = None):
        query = """ SELECT ATV.ID            AS ID, 
                            ATV.IDCARTEIRA    AS IDCARTEIRA, 
                            C.DESCRICAO       AS DESCRICAOCARTEIRA,
                            C.TIPO            AS TIPOCARTEIRA,
                            ATV.IDATIVO       AS IDATIVO, 
                            A.CODIGO          AS CODIGOATIVO,
                            ST.ID             AS IDSETOR,
                            ST.DESCRICAO      AS DESCRICAOSETOR,
                            SB.ID             AS IDSUBSETOR,
                            SB.DESCRICAO      AS DESCRICAOSUBSETOR,
                            SG.ID             AS IDSEGMENTO,
                            SG.DESCRICAO      AS DESCRICAOSEGMENTO,
                            ATV.QUANT         AS QUANT, 
                            ATV.QUANTBONUS    AS QUANTBONUS, 
                            ATV.VLRPRECOMEDIO AS VLRPRECOMEDIO,
                            ATV.VLRPRECOTETO  AS VLRPRECOTETO,  
                            ATV.PERCENTBALAC  AS PERCENTBALAC,  
                            ATV.NOTABALAC     AS NOTABALAC,  
                        ATV.SITUACAO      AS SITUACAO 
                    FROM TBCARTEIRA_ATIVO             ATV
                        INNER JOIN TBCARTEIRA         C  ON ( C.ID  = ATV.IDCARTEIRA )
                        INNER JOIN TBEMPRESA_ATIVO    A  ON ( A.ID  = ATV.IDATIVO    )
                        INNER JOIN TBEMPRESA          E  ON ( E.ID  = A.IDEMPRESA    )
                        INNER JOIN TBEMPRESA_SETOR    ST ON ( ST.ID = E.IDSETOR      )
                        INNER JOIN TBEMPRESA_SUBSETOR SB ON ( SB.ID = E.IDSUBSETOR   )
                        INNER JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO   )
                    WHERE C.IDUSUARIO    = :IDUSUARIO
                      AND ATV.IDATIVO    = :IDATIVO
                """
        params = {'IDUSUARIO': id_usuario, 'IDATIVO': id_ativo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_setores(cls, db: _orm.Session, id_usuario: int = None, id_carteira: int = None, tipo: str = None):
        query = """ SELECT S.ID AS ID, S.DESCRICAO AS DESCRICAO """
        if tipo == 'ST': query += " FROM TBEMPRESA_SETOR S "
        if tipo == 'SS': query += " FROM TBEMPRESA_SUBSETOR S "
        if tipo == 'SG': query += " FROM TBEMPRESA_SEGMENTO S "
        query += """ WHERE EXISTS( SELECT 1
                                   FROM TBCARTEIRA_ATIVO  CA
                                           INNER JOIN TBCARTEIRA      C ON ( C.ID = CA.IDCARTEIRA )
                                           INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = CA.IDATIVO    )
                                           INNER JOIN TBEMPRESA       E ON ( E.ID = A.IDEMPRESA   )
                                   WHERE C.IDUSUARIO = :IDUSUARIO
                                     AND C.SITUACAO  = 'A'
                                     AND CA.SITUACAO = 'A'
                                     AND ( CA.QUANT > 0  OR CA.QUANTBONUS > 0 )
                """
        if tipo == 'ST': query += " AND E.IDSETOR = S.ID "
        if tipo == 'SS': query += " AND E.IDSUBSETOR = S.ID "
        if tipo == 'SG': query += " AND E.IDSEGMENTO = S.ID "
        if id_carteira: query += " AND CA.IDCARTEIRA = :IDCARTEIRA "
        query += " ) "
        query += " ORDER BY S.DESCRICAO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_carteira: params['IDCARTEIRA'] = id_carteira

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_ativos_setores(cls, db: _orm.Session, id_usuario: int = None, id_carteira: int = None, id_setor: int = None, tipo: str = None):
        query = """ SELECT CA.IDATIVO, A.CODIGO, CA.QUANT, CA.QUANTBONUS, COT.VLRPRECOFECHAMENTO  
                    FROM TBCARTEIRA_ATIVO CA
                         INNER JOIN TBCARTEIRA      C ON ( C.ID = CA.IDCARTEIRA )
                         INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = CA.IDATIVO    )
                         INNER JOIN TBEMPRESA       E ON ( E.ID = A.IDEMPRESA   )
                         LEFT JOIN TBEMPRESA_ATIVOCOTACAO COT ON ( COT.IDATIVO = CA.IDATIVO )
                """
        if tipo == 'ST': query += " INNER JOIN TBEMPRESA_SETOR S ON ( S.ID = E.IDSETOR ) "
        if tipo == 'SS': query += " INNER JOIN TBEMPRESA_SUBSETOR S ON ( S.ID = E.IDSUBSETOR ) "
        if tipo == 'SG': query += " INNER JOIN TBEMPRESA_SEGMENTO S ON ( S.ID = E.IDSEGMENTO ) "
        query += """  WHERE C.IDUSUARIO = :IDUSUARIO
                        AND C.SITUACAO  = 'A'
                        AND CA.SITUACAO = 'A'
                        AND ( CA.QUANT  > 0  OR CA.QUANTBONUS > 0 )
                        AND S.ID        = :IDSETOR
                """
        if id_carteira: query += " AND CA.IDCARTEIRA = :IDCARTEIRA "
        query += " ) "
        query += " ORDER BY S.DESCRICAO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDSETOR'] = id_setor
        if id_carteira:params['IDCARTEIRA'] = id_carteira

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid_radar(cls, db: _orm.Session, id_usuario: int = None):
        query = """ SELECT E.NOMRESUMIDO          AS RAZAOSOCIAL, 
                           A.CODIGO               AS CODIGOATIVO,
                           ST.DESCRICAO           AS DESCRICAOSETOR,
                           SB.DESCRICAO           AS DESCRICAOSUBSETOR,
                           SG.DESCRICAO           AS DESCRICAOSEGMENTO,
                           CO.VLRPRECOFECHAMENTO  AS PRECO,
                           CO.VLRVARIACAO         AS VARIACAO
                    FROM TBCARTEIRA_ATIVO               ATV
                      INNER JOIN TBCARTEIRA             C  ON ( C.ID        = ATV.IDCARTEIRA )
                      INNER JOIN TBEMPRESA_ATIVO        A  ON ( A.ID        = ATV.IDATIVO    )
                      INNER JOIN TBEMPRESA_ATIVOCOTACAO CO ON ( CO.IDATIVO  = ATV.IDATIVO    )
                      INNER JOIN TBEMPRESA              E  ON ( E.ID        = A.IDEMPRESA    )
                      INNER JOIN TBEMPRESA_SETOR        ST ON ( ST.ID       = E.IDSETOR      )
                      INNER JOIN TBEMPRESA_SUBSETOR     SB ON ( SB.ID       = E.IDSUBSETOR   )
                      INNER JOIN TBEMPRESA_SEGMENTO     SG ON ( SG.ID       = E.IDSEGMENTO   )
                    WHERE C.IDUSUARIO  = :IDUSUARIO
                      AND ATV.SITUACAO = 'A'
                    ORDER BY E.NOMRESUMIDO, A.CODIGO
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
            query = """ UPDATE TBCARTEIRA_ATIVO SET VLRPRECOTETO = :VLRPRECOTETO WHERE ID = :ID """
            params = {'VLRPRECOTETO': preco_teto, 'ID': id}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            raise

    @classmethod
    async def atualizar_percent_balanc(cls, db: _orm.Session, id: int, percent_balac: float, commit: bool = True):
        try:
            query = """ UPDATE TBCARTEIRA_ATIVO SET PERCENTBALAC = :PERCENTBALAC WHERE ID = :ID """
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
            query = """ UPDATE TBCARTEIRA_ATIVO SET NOTABALAC = :NOTABALAC WHERE ID = :ID """
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
            query = "UPDATE TBCARTEIRA_ATIVO SET IDCARTEIRA = :IDCARTEIRA WHERE ID = :ID AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO )"
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
            query = "UPDATE TBCARTEIRA_ATIVO SET IDCARTEIRA = :IDCARTEIRA_NEW WHERE IDCARTEIRA = :IDCARTEIRA_OLD AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO )"
            params = {'IDUSUARIO': id_usuario, 'IDCARTEIRA_OLD': id_portfolio_old, 'IDCARTEIRA_NEW': id_portfolio_new}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def trocar_ativos(cls, db: _orm.Session, id_usuario: int, id_ativo_atual: int, id_ativo_novo: int, commit: bool = True):
        try:
            params = {'IDUSUARIO': id_usuario, 'IDATIVOATUAL': id_ativo_atual, 'IDATIVONOVO': id_ativo_novo}
            db.execute("UPDATE TBLANCAMENTO          SET IDATIVO = :IDATIVONOVO WHERE IDUSUARIO = :IDUSUARIO AND IDATIVO = :IDATIVOATUAL ", params)
            db.execute("UPDATE TBOPERACAO            SET IDATIVO = :IDATIVONOVO WHERE IDUSUARIO = :IDUSUARIO AND IDATIVO = :IDATIVOATUAL ", params)
            db.execute("UPDATE TBPROVENTO            SET IDATIVO = :IDATIVONOVO WHERE IDUSUARIO = :IDUSUARIO AND IDATIVO = :IDATIVOATUAL ", params)
            db.execute("UPDATE TBUSUARIO_ACOMP_ATIVO SET IDATIVO = :IDATIVONOVO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO) AND IDATIVO = :IDATIVOATUAL ", params)
            db.execute("UPDATE TBALUGUEL_ATIVO       SET IDATIVO = :IDATIVONOVO WHERE IDUSUARIO = :IDUSUARIO AND IDATIVO = :IDATIVOATUAL ", params)
            try:
                db.execute("UPDATE TBCARTEIRA_ATIVO      SET IDATIVO = :IDATIVONOVO WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO) AND IDATIVO = :IDATIVOATUAL ", params)
            except Exception as e:
                pass
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def resetar_ativos(cls, db: _orm.Session, id_usuario: int, id_ativo: int, commit: bool = True):
        try:
            query = "UPDATE TBCARTEIRA_ATIVO SET QUANT = 0, QUANTBONUS = 0, VLRPRECOMEDIO = 0.00, SITUACAO = 'F' WHERE IDATIVO = :IDATIVO AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) "
            params = {'IDUSUARIO': id_usuario, 'IDATIVO': id_ativo}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_carteira(cls, db: _orm.Session, id_usuario: int, id_carteira: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_ATIVO WHERE IDCARTEIRA = :IDCARTEIRA AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) """
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
            query = """ DELETE FROM TBCARTEIRA_ATIVO WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) """
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
