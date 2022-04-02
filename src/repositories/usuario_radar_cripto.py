# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.usuario_radar_cripto import UsuarioRadarCriptoModel
# from app.models.log_erro import LogErro


class UsuarioRadarCriptoRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(UsuarioRadarCriptoModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_grupo(cls, db: _orm.Session, id_grupo: int):
        try:
            return db.query(UsuarioRadarCriptoModel).filter_by(id_grupo=id_grupo).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(UsuarioRadarCriptoModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id_grupo(cls, db: _orm.Session, id_grupo: int, id: int):
        try:
            return db.query(UsuarioRadarCriptoModel).filter_by(id_grupo=id_grupo, id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_cripto(cls, db: _orm.Session, id_grupo: int, id_cripto: int):
        try:
            return db.query(UsuarioRadarCriptoModel).filter_by(id_grupo=id_grupo, id_cripto=id_cripto).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT UA.ID        AS ID, 
                           UA.IDGRUPO   AS IDGRUPO, 
                           UG.DESCRICAO AS DESCRICAOGRUPO,
                           UA.IDCRIPTO  AS IDCRIPTO, 
                           F.NOME       AS NOMECRIPTO,
                           F.CODIGO     AS CODIGOCRIPTO,
                           F.SITUACAO   AS SITUACAOCRIPTO,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_CRIPTO UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
                      INNER JOIN TBCRIPTO_EMPRESA       F  ON ( F.ID  = UA.IDCRIPTO )
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
                           UA.IDCRIPTO  AS IDCRIPTO, 
                           F.NOME       AS NOMECRIPTO,
                           F.CODIGO     AS CODIGOCRIPTO,
                           F.SITUACAO   AS SITUACAOCRIPTO,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_CRIPTO UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
                      INNER JOIN TBCRIPTO_EMPRESA       F  ON ( F.ID  = UA.IDCRIPTO )
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
    async def buscar_por_ativo_por_grupo(cls, db: _orm.Session, id_usuario: int, id_grupo: int, id_cripto: int):
        query = """ SELECT UA.ID        AS ID, 
                           UA.IDGRUPO   AS IDGRUPO, 
                           UG.DESCRICAO AS DESCRICAOGRUPO,
                           UA.IDCRIPTO  AS IDCRIPTO, 
                           F.NOME       AS NOMECRIPTO,
                           F.CODIGO     AS CODIGOCRIPTO,
                           F.SITUACAO   AS SITUACAOCRIPTO,
                           UA.SITUACAO  AS SITUACAO 
                    FROM TBUSUARIO_ACOMP_CRIPTO UA
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
                      INNER JOIN TBCRIPTO_EMPRESA       F  ON ( F.ID  = UA.IDCRIPTO )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND UA.IDGRUPO   = :IDGRUPO
                      AND UA.IDCRIPTO   = :IDCRIPTO
                """
        params = {'IDUSUARIO': id_usuario, 'IDGRUPO': id_grupo, 'IDCRIPTO': id_cripto}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid(cls, db: _orm.Session, id_grupo: int = None, id_usuario: int = None):
        query = """ SELECT FND.ID                AS IDUSERATIVO, 
                           FND.IDGRUPO           AS IDUSERGRUPO, 
                           FND.IDCRIPTO          AS IDCRIPTO,
                           F.CODIGO              AS CODIGOCRIPTO,
                           F.NOME                AS NOMECRIPTO, 
                           F.NOME                AS RAZAOSOCIAL, 
                           'CRIPTO'                 AS DESCRICAOSETOR, 
                           'CRIPTO'                 AS DESCRICAOSUBSETOR, 
                           'CRIPTO'                 AS DESCRICAOSEGMENTO, 
                           F.VLRPRECOFECHAMENTO  AS PRECO, 
                           F.VLRVARIACAO         AS VARIACAO 
                    FROM TBUSUARIO_ACOMP_CRIPTO FND
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO  UG ON ( UG.ID      = FND.IDGRUPO )
                      LEFT JOIN TBCRIPTO_EMPRESA         F  ON ( F.ID       = FND.IDCRIPTO  )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND FND.IDGRUPO  = :IDGRUPO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_CRIPTO CARTFND
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTFND.IDCARTEIRA )
                                       WHERE CARTFND.IDCRIPTO  = FND.IDCRIPTO
                                         AND CART.IDUSUARIO   = UG.IDUSUARIO
                                         AND CARTFND.SITUACAO = 'A'
                                     )
                    ORDER BY F.NOME, F.CODIGO
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
                           F.NOME                AS NOMECRIPTO, 
                           F.VLRPRECOFECHAMENTO  AS PRECO, 
                           F.VLRPRECOANTERIOR    AS ANTERIOR, 
                           F.VLRVARIACAO         AS VARIACAO 
                    FROM TBUSUARIO_ACOMP_CRIPTO FND
                      INNER JOIN TBUSUARIO_ACOMP_GRUPO  UG ON ( UG.ID      = FND.IDGRUPO )
                      LEFT JOIN TBCRIPTO_EMPRESA         F  ON ( F.ID       = FND.IDCRIPTO  )
                    WHERE UG.IDUSUARIO = :IDUSUARIO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_CRIPTO CARTFND
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTFND.IDCARTEIRA )
                                       WHERE CARTFND.IDCRIPTO  = FND.IDCRIPTO
                                         AND CART.IDUSUARIO   = UG.IDUSUARIO
                                         AND CARTFND.SITUACAO = 'A'
                                     )
                    ORDER BY F.VLRVARIACAO DESC, F.CODIGO
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
                    FROM TBUSUARIO_ACOMP_CRIPTO F
                    WHERE F.IDGRUPO = :IDGRUPO
                      AND NOT EXISTS ( SELECT 1
                                       FROM TBCARTEIRA_CRIPTO CARTFND
                                          INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTFND.IDCARTEIRA )
                                       WHERE CARTFND.IDCRIPTO  = F.IDCRIPTO
                                         AND CART.IDUSUARIO   = :IDUSUARIO
                                         AND CARTFND.SITUACAO = 'A'
                                     )
                """
        params = {'IDGRUPO': id_grupo, 'IDUSUARIO': id_usuario}
        try:
            try:
                return db.execute(query, params)
            except Exception as e:
                db.rollback()
                db.close()
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_por_grupo(cls, db: _orm.Session, id_grupo: int, commit: bool = True):
        try:
            query = " DELETE FROM TBUSUARIO_ACOMP_CRIPTO WHERE IDGRUPO = :IDGRUPO "
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
            query = "DELETE FROM TBUSUARIO_ACOMP_CRIPTO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO )"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioRadarCriptoModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioRadarCriptoModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
