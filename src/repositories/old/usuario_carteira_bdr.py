# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str, inteiro_to_str


class UsuarioCarteiraBdr(db.Model):

    __tablename__ = "TBCARTEIRA_BDR"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_carteira = db.Column('IDCARTEIRA', db.Integer, db.ForeignKey('TBCARTEIRA.ID'), nullable=False, index=True)
    id_bdr = db.Column('IDBDR', db.Integer, db.ForeignKey('TBBDR_EMPRESA.ID'), nullable=False, index=True)
    quant = db.Column('QUANT', db.Integer, nullable=True)
    quant_bonus = db.Column('QUANTBONUS', db.Integer, nullable=True)
    vlr_preco_medio = db.Column('VLRPRECOMEDIO', db.Float(20, 10), nullable=True)
    vlr_preco_teto = db.Column('VLRPRECOTETO', db.Float(17, 2), nullable=True)
    percent_balac = db.Column('PERCENTBALAC', db.Float(17, 2), nullable=True)
    nota_balac = db.Column('NOTABALAC', db.Integer, nullable=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_carteira: int = None, id_bdr: int = None, quant: int = None,
                 quant_bonus: int = None, vlr_preco_medio: float = 0.0, vlr_preco_teto: float = 0.0,
                 percent_balac: float = 0.0, nota_balac: int = None, situacao: str = None):
        self.id = id
        self.id_carteira = id_carteira
        self.id_bdr = id_bdr
        self.quant = quant
        self.quant_bonus = quant_bonus
        self.vlr_preco_medio = vlr_preco_medio
        self.vlr_preco_teto = vlr_preco_teto
        self.percent_balac = percent_balac
        self.nota_balac = nota_balac
        self.situacao = situacao

    @classmethod
    def get_all(cls, id: int = None, id_carteira: int = None, id_bdr: int = None):
        filters = []
        if id: filters.append(cls.id == id)
        if id_carteira: filters.append(cls.id_carteira == id_carteira)
        if id_bdr: filters.append(cls.id_bdr == id_bdr)
        try:
            return cls.query.filter(*filters).order_by(cls.id).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_id(cls, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int = None, id_carteira: int = None, situacao: str = None, ordem: str = None):
        query = """ SELECT ATV.ID            AS ID, 
                           ATV.IDCARTEIRA    AS IDCARTEIRA, 
                           C.DESCRICAO       AS DESCRICAOCARTEIRA,
                           C.TIPO            AS TIPOCARTEIRA,
                           ATV.IDBDR         AS IDBDR, 
                           E.CODIGO          AS CODIGOBDR,
                           E.NOME            AS NOMEBDR,
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
                    FROM TBCARTEIRA_BDR            ATV
                      INNER JOIN TBCARTEIRA             C  ON ( C.ID  = ATV.IDCARTEIRA )
                      INNER JOIN TBBDR_EMPRESA          E  ON ( E.ID  = ATV.IDBDR    )
                      LEFT JOIN TBBDR_EMPRESA_SETOR    ST ON ( ST.ID = E.IDSETOR      )
                      LEFT JOIN TBBDR_EMPRESA_SUBSETOR SB ON ( SB.ID = E.IDSUBSETOR   )
                      LEFT JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO   )
                      LEFT JOIN TBBDR_EMPRESA_COTACAO COT ON ( COT.IDBDR = ATV.IDBDR )
                    WHERE C.IDUSUARIO = :IDUSUARIO
                """
        if id_carteira: query += " AND ATV.IDCARTEIRA = :IDCARTEIRA "
        if situacao: query += " AND ATV.SITUACAO = :SITUACAO "
        if ordem: query += " ORDER BY E.CODIGO "
        else: query += " ORDER BY ST.DESCRICAO, SB.DESCRICAO, SG.DESCRICAO, E.CODIGO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_carteira: params['IDCARTEIRA'] = id_carteira
        if situacao: params['SITUACAO'] = situacao

        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos_simples(cls, id_usuario: int = None, id_carteira: int = None, situacao: str = None):
        query = """ SELECT ATV.ID AS ID, 
                           ATV.IDCARTEIRA AS IDCARTEIRA, 
                           ATV.IDBDR AS IDBDR, 
                           E.CODIGO AS CODIGOBDR,
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
                    FROM TBCARTEIRA_BDR ATV
                      INNER JOIN TBCARTEIRA C ON ( C.ID = ATV.IDCARTEIRA )
                      INNER JOIN TBBDR_EMPRESA E ON ( E.ID = ATV.IDBDR )
                      LEFT JOIN TBBDR_EMPRESA_COTACAO COT ON ( COT.IDBDR = ATV.IDBDR )
                    WHERE C.IDUSUARIO = :IDUSUARIO
                """
        if id_carteira: query += " AND ATV.IDCARTEIRA = :IDCARTEIRA "
        if situacao: query += " AND ATV.SITUACAO = :SITUACAO "
        query += " ORDER BY E.CODIGO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_carteira: params['IDCARTEIRA'] = id_carteira
        if situacao: params['SITUACAO'] = situacao

        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id_usuario: int = None, id: int = None):
        query = """ SELECT ATV.ID            AS ID, 
                            ATV.IDCARTEIRA    AS IDCARTEIRA, 
                            C.DESCRICAO       AS DESCRICAOCARTEIRA,
                            C.TIPO            AS TIPOCARTEIRA,
                            ATV.IDBDR         AS IDBDR, 
                            E.CODIGO          AS CODIGOBDR,
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
                    FROM TBCARTEIRA_BDR             ATV
                        INNER JOIN TBCARTEIRA         C  ON ( C.ID  = ATV.IDCARTEIRA )
                        INNER JOIN TBBDR_EMPRESA        E  ON ( E.ID  = ATV.IDBDR    )
                        INNER JOIN TBBDR_EMPRESA_SETOR    ST ON ( ST.ID = E.IDSETOR      )
                        INNER JOIN TBBDR_EMPRESA_SUBSETOR SB ON ( SB.ID = E.IDSUBSETOR   )
                        INNER JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO   )
                    WHERE ATV.ID      = :ID
                      AND C.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}

        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_ativo(cls, id_usuario: int = None, id_bdr: int = None):
        query = """ SELECT  ATV.ID            AS ID, 
                            ATV.IDCARTEIRA    AS IDCARTEIRA, 
                            C.DESCRICAO       AS DESCRICAOCARTEIRA,
                            C.TIPO            AS TIPOCARTEIRA,
                            ATV.IDBDR         AS IDBDR, 
                            E.CODIGO          AS CODIGOBDR,
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
                    FROM TBCARTEIRA_BDR             ATV
                        INNER JOIN TBCARTEIRA         C  ON ( C.ID  = ATV.IDCARTEIRA )
                        INNER JOIN TBBDR_EMPRESA    E  ON ( E.ID  = ATV.IDBDR    )
                        INNER JOIN TBBDR_EMPRESA_SETOR    ST ON ( ST.ID = E.IDSETOR      )
                        INNER JOIN TBBDR_EMPRESA_SUBSETOR SB ON ( SB.ID = E.IDSUBSETOR   )
                        INNER JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO   )
                    WHERE C.IDUSUARIO    = :IDUSUARIO
                      AND ATV.IDBDR    = :IDBDR
                """
        params = {'IDUSUARIO': id_usuario, 'IDBDR': id_bdr}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_lista_setores(cls, id_usuario: int = None, id_carteira: int = None, tipo: str = None):
        query = """ SELECT S.ID AS ID, S.DESCRICAO AS DESCRICAO """
        if tipo == 'ST': query += " FROM TBBDR_EMPRESA_SETOR S "
        if tipo == 'SS': query += " FROM TBBDR_EMPRESA_SUBSETOR S "
        if tipo == 'SG': query += " FROM TBBDR_EMPRESA_SEGMENTO S "
        query += """ WHERE EXISTS( SELECT 1
                                   FROM TBCARTEIRA_BDR  CA
                                       INNER JOIN TBCARTEIRA    C ON ( C.ID = CA.IDCARTEIRA )
                                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = CA.IDBDR )
                                   WHERE C.IDUSUARIO = :IDUSUARIO
                                     AND C.SITUACAO  = 'A'
                                     AND CA.SITUACAO = 'A'
                                     AND ( CA.QUANT > 0 OR CA.QUANTBONUS > 0 )
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
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_lista_ativos_setores(cls, id_usuario: int = None, id_carteira: int = None, id_setor: int = None, tipo: str = None):
        query = """ SELECT CA.IDBDR, A.CODIGO, CA.QUANT, CA.QUANTBONUS, COT.VLRPRECOFECHAMENTO  
                    FROM TBCARTEIRA_BDR CA
                         INNER JOIN TBCARTEIRA    C ON ( C.ID = CA.IDCARTEIRA )
                         INNER JOIN TBBDR_EMPRESA E ON ( E.ID = CA.IDBDR  )
                         LEFT JOIN TBBDR_EMPRESA_COTACAO COT ON ( COT.IDBDR = CA.IDBDR )
                """
        if tipo == 'ST': query += " INNER JOIN TBBDR_EMPRESA_SETOR S ON ( S.ID = E.IDSETOR ) "
        if tipo == 'SS': query += " INNER JOIN TBBDR_EMPRESA_SUBSETOR S ON ( S.ID = E.IDSUBSETOR ) "
        if tipo == 'SG': query += " INNER JOIN TBBDR_EMPRESA_SEGMENTO S ON ( S.ID = E.IDSEGMENTO ) "
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
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_dados_grid_radar(cls, id_usuario: int = None):
        query = """ SELECT E.NOME                 AS RAZAOSOCIAL, 
                           E.CODIGO               AS CODIGOBDR,
                           ST.DESCRICAO           AS DESCRICAOSETOR,
                           SB.DESCRICAO           AS DESCRICAOSUBSETOR,
                           SG.DESCRICAO           AS DESCRICAOSEGMENTO,
                           CO.VLRPRECOFECHAMENTO  AS PRECO,
                           CO.VLRVARIACAO         AS VARIACAO
                    FROM TBCARTEIRA_BDR ATV
                      INNER JOIN TBCARTEIRA                 C  ON ( C.ID        = ATV.IDCARTEIRA )
                      INNER JOIN TBBDR_EMPRESA              E  ON ( E.ID        = ATV.IDBDR    )
                      INNER JOIN TBBDR_EMPRESA_COTACAO      CO ON ( CO.IDBDR    = ATV.IDBDR    )
                      INNER JOIN TBBDR_EMPRESA_SETOR        ST ON ( ST.ID       = E.IDSETOR      )
                      INNER JOIN TBBDR_EMPRESA_SUBSETOR     SB ON ( SB.ID       = E.IDSUBSETOR   )
                      INNER JOIN TBBDR_EMPRESA_SEGMENTO     SG ON ( SG.ID       = E.IDSEGMENTO   )
                    WHERE C.IDUSUARIO  = :IDUSUARIO
                      AND ATV.SITUACAO = 'A'
                    ORDER BY E.NOME, E.CODIGO
                """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def atualizar_preco_teto(cls, id: int, preco_teto: float, commit: bool = True):
        try:
            query = """ UPDATE TBCARTEIRA_BDR SET VLRPRECOTETO = :VLRPRECOTETO WHERE ID = :ID """
            params = {'VLRPRECOTETO': preco_teto, 'ID': id}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise

    @classmethod
    def atualizar_percent_balanc(cls, id: int, percent_balac: float, commit: bool = True):
        try:
            query = """ UPDATE TBCARTEIRA_BDR SET PERCENTBALAC = :PERCENTBALAC WHERE ID = :ID """
            params = {'PERCENTBALAC': percent_balac, 'ID': id}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def atualizar_nota_balanc(cls, id: int, nota_balac: int, commit: bool = True):
        try:
            query = """ UPDATE TBCARTEIRA_BDR SET NOTABALAC = :NOTABALAC WHERE ID = :ID """
            params = {'NOTABALAC': nota_balac, 'ID': id}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def atualizar_id_carteira(cls, id_usuario: int, id: int, id_portfolio: int, commit: bool = True):
        try:
            query = "UPDATE TBCARTEIRA_BDR SET IDCARTEIRA = :IDCARTEIRA WHERE ID = :ID AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO )"
            params = {'IDUSUARIO': id_usuario, 'ID': id, 'IDCARTEIRA': id_portfolio}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def atualizar_novo_id_carteira(cls, id_usuario: int, id_portfolio_old: int, id_portfolio_new: int, commit: bool = True):
        try:
            query = "UPDATE TBCARTEIRA_BDR SET IDCARTEIRA = :IDCARTEIRA_NEW WHERE IDCARTEIRA = :IDCARTEIRA_OLD AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO )"
            params = {'IDUSUARIO': id_usuario, 'IDCARTEIRA_OLD': id_portfolio_old, 'IDCARTEIRA_NEW': id_portfolio_new}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def trocar_ativos(cls, id_usuario: int, id_bdr_atual: int, id_bdr_novo: int, commit: bool = True):
        try:
            params = {'IDUSUARIO': id_usuario, 'IDBDRATUAL': id_bdr_atual, 'IDBDRNOVO': id_bdr_novo}
            db.session.execute("UPDATE TBBDR_LANCAMENTO    SET IDBDR = :IDBDRNOVO WHERE IDUSUARIO = :IDUSUARIO AND IDBDR = :IDBDRATUAL ", params)
            db.session.execute("UPDATE TBBDR_OPERACAO      SET IDBDR = :IDBDRNOVO WHERE IDUSUARIO = :IDUSUARIO AND IDBDR = :IDBDRATUAL ", params)
            db.session.execute("UPDATE TBBDR_PROVENTO      SET IDBDR = :IDBDRNOVO WHERE IDUSUARIO = :IDUSUARIO AND IDBDR = :IDBDRATUAL ", params)
            db.session.execute("UPDATE TBUSUARIO_ACOMP_BDR SET IDBDR = :IDBDRNOVO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO) AND IDBDR = :IDBDRATUAL ", params)
            try:
                db.session.execute("UPDATE TBCARTEIRA_BDR      SET IDBDR = :IDBDRNOVO WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO) AND IDBDR = :IDBDRATUAL ", params)
            except Exception as e:
                pass
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def resetar_ativos(cls, id_usuario: int, id_bdr: int, commit: bool = True):
        try:
            query = "UPDATE TBCARTEIRA_BDR SET QUANT = 0, QUANTBONUS = 0, VLRPRECOMEDIO = 0.00, SITUACAO = 'F' WHERE IDBDR = :IDBDR AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) "
            params = {'IDUSUARIO': id_usuario, 'IDBDR': id_bdr}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_carteira(cls, id_usuario: int, id_carteira: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_BDR WHERE IDCARTEIRA = :IDCARTEIRA AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) """
            params = {'IDCARTEIRA': id_carteira, 'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_BDR WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) """
            params = {'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def salvar(self, commit: bool = True):
        try:
            db.session.add(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def excluir(self, commit: bool = True):
        try:
            db.session.delete(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def quant_format(self) -> str:
        return inteiro_to_str(valor=self.quant)

    def quant_bonus_format(self) -> str:
        return inteiro_to_str(valor=self.quant_bonus)

    def vlr_preco_medio_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_medio)

    def vlr_preco_teto_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_teto)

    def percent_balac_format(self) -> str:
        return decimal_to_str(valor=self.percent_balac)

    def situacao_descr(self) -> str:
        if self.situacao == 'A': return 'Ativo'
        elif self.situacao == 'I': return 'Inativo'
        elif self.situacao == 'F': return 'Finalizado'
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioCarteiraAtivo {str(self.id)}>'
