# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro

class UsuarioRadarFii(db.Model):

    __tablename__ = "TBUSUARIO_ACOMP_FUNDO"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_grupo = db.Column('IDGRUPO', db.Integer, db.ForeignKey('TBUSUARIO_ACOMP_GRUPO.ID'), nullable=False, index=True)
    id_fundo = db.Column('IDFUNDO', db.Integer, db.ForeignKey('TBFII_FUNDOIMOB.ID'), nullable=False, index=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_grupo: int = None, id_fundo: int = None, situacao: str = None):
        self.id = id
        self.id_grupo = id_grupo
        self.id_fundo = id_fundo
        self.situacao = situacao

    @classmethod
    def get_all(cls):
        try:
            return cls.query.all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_all_by_grupo(cls, id_grupo: int):
        try:
            return cls.query.filter_by(id_grupo=id_grupo).all()
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
    def get_by_id_grupo(cls, id_grupo: int, id: int):
        try:
            return cls.query.filter_by(id_grupo=id_grupo, id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_fundo(cls, id_grupo: int, id_fundo: int):
        try:
            return cls.query.filter_by(id_grupo=id_grupo, id_fundo=id_fundo).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int):
        query = """ SELECT UA.ID        AS ID, 
                           UA.IDGRUPO   AS IDGRUPO, 
                           UG.DESCRICAO AS DESCRICAOGRUPO,
                           UA.IDFUNDO   AS IDFUNDO, 
                           F.NOME       AS NOMEFUNDO,
                           F.CODIGO     AS CODIGOFUNDO,
                           F.SITUACAO   AS SITUACAOFUNDO,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_FUNDO UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
                      INNER JOIN TBFII_FUNDOIMOB       F  ON ( F.ID  = UA.IDFUNDO )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                    ORDER BY UG.DESCRICAO, F.CODIGO
                """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id: int, id_usuario: int):
        query = """ SELECT UA.ID        AS ID, 
                           UA.IDGRUPO   AS IDGRUPO, 
                           UG.DESCRICAO AS DESCRICAOGRUPO,
                           UA.IDFUNDO   AS IDFUNDO, 
                           F.NOME       AS NOMEFUNDO,
                           F.CODIGO     AS CODIGOFUNDO,
                           F.SITUACAO   AS SITUACAOFUNDO,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_FUNDO UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
                      INNER JOIN TBFII_FUNDOIMOB       F  ON ( F.ID  = UA.IDFUNDO )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND UA.ID        = :ID
                """
        params = {'IDUSUARIO': id_usuario, 'ID': id}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_ativo_por_grupo(cls, id_usuario: int, id_grupo: int, id_fundo: int):
        query = """ SELECT UA.ID        AS ID, 
                           UA.IDGRUPO   AS IDGRUPO, 
                           UG.DESCRICAO AS DESCRICAOGRUPO,
                           UA.IDFUNDO   AS IDFUNDO, 
                           F.NOME       AS NOMEFUNDO,
                           F.CODIGO     AS CODIGOFUNDO,
                           F.SITUACAO   AS SITUACAOFUNDO,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_FUNDO UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
                      INNER JOIN TBFII_FUNDOIMOB       F  ON ( F.ID  = UA.IDFUNDO )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND UA.IDGRUPO   = :IDGRUPO
                      AND UA.IDFUNDO   = :IDFUNDO
                """
        params = {'IDUSUARIO': id_usuario, 'IDGRUPO': id_grupo, 'IDFUNDO': id_fundo}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_dados_grid(cls, id_grupo: int = None, id_usuario: int = None):
        query = """ SELECT FND.ID                AS IDUSERATIVO, 
                           FND.IDGRUPO           AS IDUSERGRUPO, 
                           FND.IDFUNDO           AS IDFUNDO,
                           F.CODIGO              AS CODIGOATIVO,
                           F.NOME                AS NOMEFUNDO, 
                           F.RAZAOSOCIAL         AS RAZAOSOCIAL, 
                           'FII'                 AS DESCRICAOSETOR, 
                           'FII'                 AS DESCRICAOSUBSETOR, 
                           'FII'                 AS DESCRICAOSEGMENTO, 
                           C.VLRPRECOFECHAMENTO  AS PRECO, 
                           C.VLRVARIACAO         AS VARIACAO 
                    FROM TBUSUARIO_ACOMP_FUNDO FND
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO  UG ON ( UG.ID      = FND.IDGRUPO )
                      LEFT JOIN TBFII_FUNDOIMOB_COTACAO C  ON ( C.IDFUNDO  = FND.IDFUNDO  )
                      LEFT JOIN TBFII_FUNDOIMOB         F  ON ( F.ID       = FND.IDFUNDO  )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND FND.IDGRUPO  = :IDGRUPO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_FUNDO CARTFND
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTFND.IDCARTEIRA )
                                       WHERE CARTFND.IDFUNDO  = FND.IDFUNDO
                                         AND CART.IDUSUARIO   = UG.IDUSUARIO
                                         AND CARTFND.SITUACAO = 'A'
                                     )
                    ORDER BY F.RAZAOSOCIAL, F.CODIGO
                """
        params = {'IDGRUPO': id_grupo, 'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_dados_grid_port(cls, id_usuario: int = None):
        query = """ SELECT F.ID                  AS IDATIVO,
                           F.CODIGO              AS CODIGOATIVO,
                           F.NOME                AS NOMEFUNDO, 
                           C.VLRPRECOFECHAMENTO  AS PRECO, 
                           C.VLRPRECOANTERIOR    AS ANTERIOR, 
                           C.VLRVARIACAO         AS VARIACAO 
                    FROM TBUSUARIO_ACOMP_FUNDO FND
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO  UG ON ( UG.ID      = FND.IDGRUPO )
                      LEFT JOIN TBFII_FUNDOIMOB_COTACAO C  ON ( C.IDFUNDO  = FND.IDFUNDO  )
                      LEFT JOIN TBFII_FUNDOIMOB         F  ON ( F.ID       = FND.IDFUNDO  )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_FUNDO CARTFND
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTFND.IDCARTEIRA )
                                       WHERE CARTFND.IDFUNDO  = FND.IDFUNDO
                                         AND CART.IDUSUARIO   = UG.IDUSUARIO
                                         AND CARTFND.SITUACAO = 'A'
                                     )
                    ORDER BY C.VLRVARIACAO DESC, F.CODIGO
                """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_quant_grupo(cls, id_grupo: int = None, id_usuario: int = None):
        query = """ SELECT COUNT(1) AS QTDE
                    FROM TBUSUARIO_ACOMP_FUNDO F
                    WHERE F.IDGRUPO = :IDGRUPO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_FUNDO CARTFND
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTFND.IDCARTEIRA )
                                       WHERE CARTFND.IDFUNDO  = F.IDFUNDO
                                         AND CART.IDUSUARIO   = :IDUSUARIO
                                         AND CARTFND.SITUACAO = 'A'
                                     )
                """
        params = {'IDGRUPO': id_grupo, 'IDUSUARIO': id_usuario}
        try:
            try:
                return db.session.execute(query, params)
            except Exception as e:
                db.session.rollback()
                db.session.close()
                return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_por_grupo(cls, id_grupo: int, commit: bool = True):
        try:
            query = "DELETE FROM TBUSUARIO_ACOMP_FUNDO WHERE IDGRUPO = :IDGRUPO"
            params = {'IDGRUPO': id_grupo}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBUSUARIO_ACOMP_FUNDO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO )"
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

    def situacao_descr(self) -> str:
        if self.situacao == 'A':
            return 'Ativo'
        elif self.situacao == 'I':
            return 'Inativo'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioRadarFundoImob {str(self.id)}>'
