# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class UsuarioRadarBdr(db.Model):

#     __tablename__ = "TBUSUARIO_ACOMP_BDR"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_grupo = db.Column('IDGRUPO', db.Integer, db.ForeignKey('TBUSUARIO_ACOMP_GRUPO.ID'), nullable=False, index=True)
#     id_bdr = db.Column('IDBDR', db.Integer, db.ForeignKey('TBBDR_EMPRESA.ID'), nullable=False, index=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_grupo: int = None, id_bdr: int = None, situacao: str = None):
#         self.id = id
#         self.id_grupo = id_grupo
#         self.id_bdr = id_bdr
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_all_by_grupo(cls, id_grupo: int):
#         try:
#             return cls.query.filter_by(id_grupo=id_grupo).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_id(cls, id: int):
#         try:
#             return cls.query.filter_by(id=id).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_id_grupo(cls, id_grupo: int, id: int):
#         try:
#             return cls.query.filter_by(id_grupo=id_grupo, id=id).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_ativo(cls, id_grupo: int, id_bdr: int):
#         try:
#             return cls.query.filter_by(id_grupo=id_grupo, id_bdr=id_bdr).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls, id_usuario: int):
#         query = """ SELECT UA.ID        AS ID, 
#                            UA.IDGRUPO   AS IDGRUPO, 
#                            UG.DESCRICAO AS DESCRICAOGRUPO,
#                            UA.IDBDR     AS IDBDR, 
#                            E.CODIGO     AS CODIGOBDR,
#                            UA.SITUACAO  AS SITUACAO 
#                     FROM TBUSUARIO_ACOMP_BDR UA
#                       INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
#                       INNER JOIN TBBDR_EMPRESA            E  ON ( E.ID  = UA.IDBDR )
#                     WHERE UG.IDUSUARIO = :IDUSUARIO
#                     ORDER BY UG.DESCRICAO, E.CODIGO
#                 """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int, id_usuario: int):
#         query = """ SELECT UA.ID        AS ID, 
#                            UA.IDGRUPO   AS IDGRUPO, 
#                            UG.DESCRICAO AS DESCRICAOGRUPO,
#                            UA.IDBDR     AS IDBDR, 
#                            E.CODIGO     AS CODIGOBDR,
#                            UA.SITUACAO  AS SITUACAO 
#                     FROM TBUSUARIO_ACOMP_BDR UA
#                       INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
#                       INNER JOIN TBBDR_EMPRESA             E  ON ( E.ID  = UA.IDBDR )
#                     WHERE UG.IDUSUARIO = :IDUSUARIO
#                       AND UA.ID        = :ID
#                 """
#         params = {'IDUSUARIO': id_usuario, 'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_ativo_por_grupo(cls, id_usuario: int, id_grupo: int, id_bdr: int):
#         query = """ SELECT UA.ID        AS ID, 
#                            UA.IDGRUPO   AS IDGRUPO, 
#                            UG.DESCRICAO AS DESCRICAOGRUPO,
#                            UA.IDBDR     AS IDBDR, 
#                            E.CODIGO     AS CODIGOBDR,
#                            UA.SITUACAO  AS SITUACAO 
#                     FROM TBUSUARIO_ACOMP_BDR UA
#                       INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID = UA.IDGRUPO )
#                       INNER JOIN TBBDR_EMPRESA             E  ON ( E.ID  = UA.IDBDR )
#                     WHERE UG.IDUSUARIO = :IDUSUARIO
#                       AND UA.IDGRUPO   = :IDGRUPO
#                       AND UA.IDBDR     = :IDBDR
#                 """
#         params = {'IDUSUARIO': id_usuario, 'IDGRUPO': id_grupo, 'IDBDR': id_bdr}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_dados_grid(cls, id_grupo: int = None, id_usuario: int = None):
#         query = """ SELECT ATV.ID                AS IDUSERATIVO, 
#                            ATV.IDGRUPO           AS IDUSERGRUPO, 
#                            ATV.IDBDR             AS IDBDR,
#                            E.CODIGO              AS CODIGOBDR,
#                            E.NOME                AS NOMEBDR,
#                            E.RAZAOSOCIAL         AS RAZAOSOCIAL, 
#                            SR.DESCRICAO          AS DESCRICAOSETOR, 
#                            SS.DESCRICAO          AS DESCRICAOSUBSETOR, 
#                            SG.DESCRICAO          AS DESCRICAOSEGMENTO, 
#                            C.VLRPRECOFECHAMENTO  AS PRECO, 
#                            C.VLRVARIACAO         AS VARIACAO 
#                     FROM TBUSUARIO_ACOMP_BDR ATV
#                       INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID      = ATV.IDGRUPO  )
#                       LEFT JOIN TBBDR_EMPRESA_COTACAO  C  ON ( C.IDBDR    = ATV.IDBDR    )
#                       LEFT JOIN TBBDR_EMPRESA              E  ON ( E.ID       = ATV.IDBDR    )
#                       LEFT JOIN TBBDR_EMPRESA_SETOR        SR ON ( SR.ID      = E.IDSETOR    )
#                       LEFT JOIN TBBDR_EMPRESA_SUBSETOR     SS ON ( SS.ID      = E.IDSUBSETOR )
#                       LEFT JOIN TBBDR_EMPRESA_SEGMENTO     SG ON ( SG.ID      = E.IDSEGMENTO )
#                     WHERE UG.IDUSUARIO = :IDUSUARIO
#                       AND ATV.IDGRUPO  = :IDGRUPO
#                       AND NOT EXISTS ( SELECT 1
#                                        FROM TBCARTEIRA_BDR CARTATV
#                                           INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTATV.IDCARTEIRA )
#                                        WHERE CARTATV.IDBDR    = ATV.IDBDR
#                                          AND CART.IDUSUARIO   = UG.IDUSUARIO
#                                          AND CARTATV.SITUACAO = 'A'
#                                      )
#                     ORDER BY E.RAZAOSOCIAL, E.CODIGO
#                 """
#         params = {'IDGRUPO': id_grupo, 'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_dados_grid_port(cls, id_usuario: int = None):
#         query = """ SELECT E.ID                  AS IDBDR,
#                            E.CODIGO              AS CODIGOBDR,
#                            E.NOME                AS NOMEBDR,
#                            C.VLRPRECOFECHAMENTO  AS PRECO, 
#                            C.VLRPRECOANTERIOR    AS ANTERIOR, 
#                            C.VLRVARIACAO         AS VARIACAO 
#                     FROM TBUSUARIO_ACOMP_BDR ATV
#                       INNER JOIN TBUSUARIO_ACOMP_GRUPO UG ON ( UG.ID   = ATV.IDGRUPO )
#                       LEFT JOIN TBBDR_EMPRESA_COTACAO  C  ON ( C.IDBDR = ATV.IDBDR  )
#                       LEFT JOIN TBBDR_EMPRESA          E  ON ( E.ID    = ATV.IDBDR  )
#                     WHERE UG.IDUSUARIO = :IDUSUARIO
#                       AND NOT EXISTS ( SELECT 1
#                                        FROM TBCARTEIRA_BDR CARTATV
#                                           INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTATV.IDCARTEIRA )
#                                        WHERE CARTATV.IDBDR    = ATV.IDBDR
#                                          AND CART.IDUSUARIO   = UG.IDUSUARIO
#                                          AND CARTATV.SITUACAO = 'A'
#                                      )
#                     ORDER BY C.VLRVARIACAO DESC, E.CODIGO
#                 """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_quant_grupo(cls, id_grupo: int = None, id_usuario: int = None):
#         query = """ SELECT COUNT(1) AS QTDE
#                     FROM TBUSUARIO_ACOMP_BDR E
#                     WHERE E.IDGRUPO = :IDGRUPO
#                     AND NOT EXISTS ( SELECT 1
#                                        FROM TBCARTEIRA_BDR CARTATV
#                                           INNER JOIN TBCARTEIRA CART ON ( CART.ID = CARTATV.IDCARTEIRA )
#                                        WHERE CARTATV.IDBDR    = E.IDBDR
#                                          AND CART.IDUSUARIO   = :IDUSUARIO
#                                          AND CARTATV.SITUACAO = 'A'
#                                      )
#                 """
#         params = {'IDGRUPO': id_grupo, 'IDUSUARIO': id_usuario}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_por_grupo(cls, id_grupo: int, commit: bool = True):
#         try:
#             query = " DELETE FROM TBUSUARIO_ACOMP_BDR WHERE IDGRUPO = :IDGRUPO "
#             params = {'IDGRUPO': id_grupo}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBUSUARIO_ACOMP_BDR WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO )"
#             params = {'IDUSUARIO': id_usuario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def salvar(self, commit: bool = True):
#         try:
#             db.session.add(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def excluir(self, commit: bool = True):
#         try:
#             db.session.delete(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def situacao_descr(self) -> str:
#         if self.situacao == 'A': return 'Ativo'
#         elif self.situacao == 'I': return 'Inativo'
#         else: return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioRadarAtivo {str(self.id)}>'
