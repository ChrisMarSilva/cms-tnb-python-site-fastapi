# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.xxxxxxxxxxx import xxxxxxxxxxxModel
# from app.models.log_erro import LogErro


class UsuarioRadarEtfRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_grupo(cls, db: _orm.Session, id_grupo: int):
        try:
            return cls.query.filter_by(id_grupo=id_grupo).all()
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
    async def get_by_id_grupo(cls, db: _orm.Session, id_grupo: int, id: int):
        try:
            return cls.query.filter_by(id_grupo=id_grupo, id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_indice(cls, db: _orm.Session, id_grupo: int, id_indice: int):
        try:
            return cls.query.filter_by(id_grupo=id_grupo, id_indice=id_indice).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int):
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
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int, id_usuario: int):
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
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_ativo_por_grupo(cls, db: _orm.Session, id_usuario: int, id_grupo: int, id_indice: int):
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
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid(cls, db: _orm.Session, id_grupo: int = None, id_usuario: int = None):
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
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid_port(cls, db: _orm.Session, id_usuario: int = None):
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
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_quant_grupo(cls, db: _orm.Session, id_grupo: int = None, id_usuario: int = None):
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
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_por_grupo(cls, db: _orm.Session, id_grupo: int, commit: bool = True):
        try:
            query = "DELETE FROM TBUSUARIO_ACOMP_INDICE WHERE IDGRUPO = :IDGRUPO"
            params = {'IDGRUPO': id_grupo}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBUSUARIO_ACOMP_INDICE WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO )"
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
            if commit:
                db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
