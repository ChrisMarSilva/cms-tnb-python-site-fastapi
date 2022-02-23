# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro


class UsuarioRadarAcao(db.Model):

    __tablename__ = "TBUSUARIO_ACOMP_ATIVO"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_grupo = db.Column('IDGRUPO', db.Integer, db.ForeignKey('TBUSUARIO_ACOMP_GRUPO.ID'), nullable=False, index=True)
    id_ativo = db.Column('IDATIVO', db.Integer, db.ForeignKey('TBEMPRESA_ATIVO.ID'), nullable=False, index=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_grupo: int = None, id_ativo: int = None, situacao: str = None):
        self.id = id
        self.id_grupo = id_grupo
        self.id_ativo = id_ativo
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
    def get_by_ativo(cls, id_grupo: int, id_ativo: int):
        try:
            return cls.query.filter_by(id_grupo=id_grupo, id_ativo=id_ativo).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int):
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
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id: int, id_usuario: int):
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
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_ativo_por_grupo(cls, id_usuario: int, id_grupo: int, id_ativo: int):
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
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_dados_grid(cls, id_grupo: int = None, id_usuario: int = None):
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
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_dados_grid_port(cls, id_usuario: int = None):
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
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_quant_grupo(cls, id_grupo: int = None, id_usuario: int = None):
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
                return db.session.execute(query, params)
            except Exception as e:
                return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_por_grupo(cls, id_grupo: int, commit: bool = True):
        try:
            query = "DELETE FROM TBUSUARIO_ACOMP_ATIVO WHERE IDGRUPO = :IDGRUPO"
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
            query = "DELETE FROM TBUSUARIO_ACOMP_ATIVO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO )"
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
        return '<UsuarioRadarAtivo {str(self.id)}>'
