# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro


class UsuarioRadarEtf(db.Model):

    __tablename__ = "TBUSUARIO_ACOMP_INDICE"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_grupo = db.Column('IDGRUPO', db.Integer, db.ForeignKey('TBUSUARIO_ACOMP_GRUPO.ID'), nullable=False, index=True)
    id_indice = db.Column('IDINDICE', db.Integer, db.ForeignKey('TBETF_INDICE.ID'), nullable=False, index=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_grupo: int = None, id_indice: int = None, situacao: str = None):
        self.id = id
        self.id_grupo = id_grupo
        self.id_indice = id_indice
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
    def get_by_indice(cls, id_grupo: int, id_indice: int):
        try:
            return cls.query.filter_by(id_grupo=id_grupo, id_indice=id_indice).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int):
        query = """ SELECT UA.ID        AS ID, 
                           UA.IDGRUPO   AS IDGRUPO, 
                           UG.DESCRICAO AS DESCRICAOGRUPO,
                           UA.IDINDICE  AS IDINDICE, 
                           F.NOME       AS NOMEINDICE,
                           F.CODIGO     AS CODIGOINDICE,
                           F.SITUACAO   AS SITUACAOINDICE,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_INDICE UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO  )
                      INNER JOIN TBETF_INDICE          F  ON ( F.ID  = UA.IDINDICE )
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
                           UA.IDINDICE  AS IDINDICE, 
                           F.NOME       AS NOMEINDICE,
                           F.CODIGO     AS CODIGOINDICE,
                           F.SITUACAO   AS SITUACAOINDICE,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_INDICE UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO  )
                      INNER JOIN TBETF_INDICE          F  ON ( F.ID  = UA.IDINDICE )
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
    def buscar_por_ativo_por_grupo(cls, id_usuario: int, id_grupo: int, id_indice: int):
        query = """ SELECT UA.ID        AS ID, 
                           UA.IDGRUPO   AS IDGRUPO, 
                           UG.DESCRICAO AS DESCRICAOGRUPO,
                           UA.IDINDICE  AS IDINDICE, 
                           F.NOME       AS NOMEINDICE,
                           F.CODIGO     AS CODIGOINDICE,
                           F.SITUACAO   AS SITUACAOINDICE,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_INDICE UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO  )
                      INNER JOIN TBETF_INDICE          F  ON ( F.ID  = UA.IDINDICE )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND UA.IDGRUPO   = :IDGRUPO
                      AND UA.IDINDICE  = :IDINDICE
                """
        params = {'IDUSUARIO': id_usuario, 'IDGRUPO': id_grupo, 'IDINDICE': id_indice}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_dados_grid(cls, id_grupo: int = None, id_usuario: int = None):
        query = """ SELECT FND.ID                AS IDUSERATIVO, 
                           FND.IDGRUPO           AS IDUSERGRUPO, 
                           FND.IDINDICE          AS IDINDICE,
                           F.CODIGO              AS CODIGOATIVO,
                           F.NOME                AS NOMEINDICE, 
                           F.RAZAOSOCIAL         AS RAZAOSOCIAL, 
                           'ETF'                 AS DESCRICAOSETOR, 
                           'ETF'                 AS DESCRICAOSUBSETOR, 
                           'ETF'                 AS DESCRICAOSEGMENTO, 
                           C.VLRPRECOFECHAMENTO  AS PRECO, 
                           C.VLRVARIACAO         AS VARIACAO 
                    FROM TBUSUARIO_ACOMP_INDICE         FND
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO  UG  ON ( UG.ID      = FND.IDGRUPO   )
                      LEFT JOIN TBETF_INDICE_COTACAO    C   ON ( C.IDINDICE = FND.IDINDICE  )
                      LEFT JOIN TBETF_INDICE            F   ON ( F.ID       = FND.IDINDICE  )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND FND.IDGRUPO  = :IDGRUPO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_INDICE CARTFND
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTFND.IDCARTEIRA )
                                       WHERE CARTFND.IDINDICE = FND.IDINDICE
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
                           F.NOME                AS NOMEINDICE, 
                           C.VLRPRECOFECHAMENTO  AS PRECO, 
                           C.VLRPRECOANTERIOR    AS ANTERIOR, 
                           C.VLRVARIACAO         AS VARIACAO 
                    FROM TBUSUARIO_ACOMP_INDICE         FND
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO  UG  ON ( UG.ID      = FND.IDGRUPO   )
                      LEFT JOIN TBETF_INDICE_COTACAO    C   ON ( C.IDINDICE = FND.IDINDICE  )
                      LEFT JOIN TBETF_INDICE            F   ON ( F.ID       = FND.IDINDICE  )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_INDICE CARTFND
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTFND.IDCARTEIRA )
                                       WHERE CARTFND.IDINDICE = FND.IDINDICE
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
                    FROM TBUSUARIO_ACOMP_INDICE F
                    WHERE F.IDGRUPO = :IDGRUPO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_INDICE CARTFND
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTFND.IDCARTEIRA )
                                       WHERE CARTFND.IDINDICE  = F.IDINDICE
                                         AND CART.IDUSUARIO   = :IDUSUARIO
                                         AND CARTFND.SITUACAO = 'A'
                                     )
                """
        params = {'IDGRUPO': id_grupo, 'IDUSUARIO': id_usuario}
        try:
            try:
                return db.session.execute(query, params)
            except Exception as e:
                return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_por_grupo(cls, id_grupo: int, commit: bool = True):
        try:
            query = "DELETE FROM TBUSUARIO_ACOMP_INDICE WHERE IDGRUPO = :IDGRUPO"
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
            query = "DELETE FROM TBUSUARIO_ACOMP_INDICE WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO )"
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
            if commit:
                db.session.commit()
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
        return '<UsuarioRadarETFIndice {str(self.id)}>'
