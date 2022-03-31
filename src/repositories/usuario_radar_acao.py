# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro


class UsuarioRadarAcaoRepository:

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
    async def get_by_ativo(cls, db: _orm.Session, id_grupo: int, id_ativo: int):
        try:
            return cls.query.filter_by(id_grupo=id_grupo, id_ativo=id_ativo).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT UA.ID        AS ID, 
                           UA.IDGRUPO   AS IDGRUPO, 
                           UG.DESCRICAO AS DESCRICAOGRUPO,
                           UA.IDATIVO   AS IDATIVO, 
                           A.CODIGO     AS CODIGOATIVO,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_ATIVO UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
                      INNER JOIN TBEMPRESA_ATIVO       A  ON ( A.ID  = UA.IDATIVO )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                    ORDER BY UG.DESCRICAO, A.CODIGO
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
                           UA.IDATIVO   AS IDATIVO, 
                           A.CODIGO     AS CODIGOATIVO,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_ATIVO UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
                      INNER JOIN TBEMPRESA_ATIVO       A  ON ( A.ID  = UA.IDATIVO )
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
    async def buscar_por_ativo_por_grupo(cls, db: _orm.Session, id_usuario: int, id_grupo: int, id_ativo: int):
        query = """ SELECT UA.ID        AS ID, 
                           UA.IDGRUPO   AS IDGRUPO, 
                           UG.DESCRICAO AS DESCRICAOGRUPO,
                           UA.IDATIVO   AS IDATIVO, 
                           A.CODIGO     AS CODIGOATIVO,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_ATIVO UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
                      INNER JOIN TBEMPRESA_ATIVO       A  ON ( A.ID  = UA.IDATIVO )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND UA.IDGRUPO   = :IDGRUPO
                      AND UA.IDATIVO   = :IDATIVO
                """
        params = {'IDUSUARIO': id_usuario, 'IDGRUPO': id_grupo, 'IDATIVO': id_ativo}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid(cls, db: _orm.Session, id_grupo: int = None, id_usuario: int = None):
        query = """ SELECT ATV.ID                AS IDUSERATIVO, 
                           ATV.IDGRUPO           AS IDUSERGRUPO, 
                           ATV.IDATIVO           AS IDATIVO,
                           A.CODIGO              AS CODIGOATIVO,
                           E.NOME                AS NOMEEMPRESA,
                           E.NOMRESUMIDO         AS NOMRESUMIDOEMPRESA,
                           E.RAZAOSOCIAL         AS RAZAOSOCIAL, 
                           SR.DESCRICAO          AS DESCRICAOSETOR, 
                           SS.DESCRICAO          AS DESCRICAOSUBSETOR, 
                           SG.DESCRICAO          AS DESCRICAOSEGMENTO, 
                           C.VLRPRECOFECHAMENTO  AS PRECO, 
                           C.VLRVARIACAO         AS VARIACAO 
                    FROM TBUSUARIO_ACOMP_ATIVO ATV
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID      = ATV.IDGRUPO )
                      LEFT JOIN TBEMPRESA_ATIVOCOTACAO C  ON ( C.IDATIVO  = ATV.IDATIVO  )
                      LEFT JOIN TBEMPRESA_ATIVO        A  ON ( A.ID       = ATV.IDATIVO  )
                      LEFT JOIN TBEMPRESA              E  ON ( E.ID       = A.IDEMPRESA  )
                      LEFT JOIN TBEMPRESA_SETOR        SR ON ( SR.ID      = E.IDSETOR    )
                      LEFT JOIN TBEMPRESA_SUBSETOR     SS ON ( SS.ID      = E.IDSUBSETOR )
                      LEFT JOIN TBEMPRESA_SEGMENTO     SG ON ( SG.ID      = E.IDSEGMENTO )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND ATV.IDGRUPO  = :IDGRUPO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_ATIVO CARTATV
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTATV.IDCARTEIRA )
                                       WHERE CARTATV.IDATIVO  = ATV.IDATIVO
                                         AND CART.IDUSUARIO   = UG.IDUSUARIO
                                         AND CARTATV.SITUACAO = 'A'
                                     )
                    ORDER BY E.RAZAOSOCIAL, A.CODIGO
                """
        params = {'IDGRUPO': id_grupo, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid_port(cls, db: _orm.Session, id_usuario: int = None):
        query = """ SELECT A.ID                  AS IDATIVO,
                           A.CODIGO              AS CODIGOATIVO,
                           E.NOME                AS NOMEEMPRESA,
                           E.NOMRESUMIDO         AS NOMRESUMIDOEMPRESA,
                           C.VLRPRECOFECHAMENTO  AS PRECO, 
                           C.VLRPRECOANTERIOR    AS ANTERIOR, 
                           C.VLRVARIACAO         AS VARIACAO 
                    FROM TBUSUARIO_ACOMP_ATIVO ATV
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID      = ATV.IDGRUPO )
                      LEFT JOIN TBEMPRESA_ATIVOCOTACAO C  ON ( C.IDATIVO  = ATV.IDATIVO )
                      LEFT JOIN TBEMPRESA_ATIVO        A  ON ( A.ID       = ATV.IDATIVO )
                      LEFT JOIN TBEMPRESA              E  ON ( E.ID       = A.IDEMPRESA )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_ATIVO CARTATV
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTATV.IDCARTEIRA )
                                       WHERE CARTATV.IDATIVO  = ATV.IDATIVO
                                         AND CART.IDUSUARIO   = UG.IDUSUARIO
                                         AND CARTATV.SITUACAO = 'A'
                                     )
                    ORDER BY C.VLRVARIACAO DESC, A.CODIGO
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
                    FROM TBUSUARIO_ACOMP_ATIVO A
                    WHERE A.IDGRUPO = :IDGRUPO
                    AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_ATIVO CARTATV
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTATV.IDCARTEIRA )
                                       WHERE CARTATV.IDATIVO  = A.IDATIVO
                                         AND CART.IDUSUARIO   = :IDUSUARIO
                                         AND CARTATV.SITUACAO = 'A'
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
            query = "DELETE FROM TBUSUARIO_ACOMP_ATIVO WHERE IDGRUPO = :IDGRUPO"
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
            query = "DELETE FROM TBUSUARIO_ACOMP_ATIVO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO )"
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
