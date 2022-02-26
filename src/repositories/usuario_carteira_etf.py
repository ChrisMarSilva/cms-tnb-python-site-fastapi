# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str, inteiro_to_str


# class UsuarioCarteiraEtf(db.Model):

#     __tablename__ = "TBCARTEIRA_INDICE"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_carteira = db.Column('IDCARTEIRA', db.Integer, db.ForeignKey('TBCARTEIRA.ID'), nullable=False, index=True)
#     id_indice = db.Column('IDINDICE', db.Integer, db.ForeignKey('TBETF_INDICE.ID'), nullable=False, index=True)
#     quant = db.Column('QUANT', db.Integer, nullable=True)
#     quant_bonus = db.Column('QUANTBONUS', db.Integer, nullable=True)
#     vlr_preco_medio = db.Column('VLRPRECOMEDIO', db.Float(20, 10), nullable=True)
#     vlr_preco_teto = db.Column('VLRPRECOTETO', db.Float(17, 2), nullable=True)
#     percent_balac = db.Column('PERCENTBALAC', db.Float(17, 2), nullable=True)
#     nota_balac = db.Column('NOTABALAC', db.Integer, nullable=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_carteira: int = None, id_indice: int = None, quant: int = None,
#                  quant_bonus: int = None, vlr_preco_medio: float = 0.0, vlr_preco_teto: float = 0.0,
#                  percent_balac: float = 0.0, nota_balac: int = None, situacao: str = None):
#         self.id = id
#         self.id_carteira = id_carteira
#         self.id_indice = id_indice
#         self.quant = quant
#         self.quant_bonus = quant_bonus
#         self.vlr_preco_medio = vlr_preco_medio
#         self.vlr_preco_teto = vlr_preco_teto
#         self.percent_balac = percent_balac
#         self.nota_balac = nota_balac
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls, id: int = None, id_carteira: int = None, id_indice: int = None):
#         filters = []
#         if id: filters.append(cls.id == id)
#         if id_carteira: filters.append(cls.id_carteira == id_carteira)
#         if id_indice: filters.append(cls.id_indice == id_indice)
#         try:
#             return cls.query.filter(*filters).order_by(cls.id).all()
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
#     def buscar_todos(cls, id_usuario: int = None, id_carteira: int = None, situacao: str = None):
#         query = """ SELECT FND.ID            AS ID, 
#                            FND.IDCARTEIRA    AS IDCARTEIRA, 
#                            C.DESCRICAO       AS DESCRICAOCARTEIRA,
#                            C.TIPO            AS TIPOCARTEIRA,
#                            FND.IDINDICE      AS IDINDICE, 
#                            F.NOME            AS NOMEINDICE, 
#                            F.CODIGO          AS CODIGOINDICE, 
#                            F.SITUACAO        AS SITUACAOINDICE, 
#                            FND.QUANT         AS QUANT, 
#                            FND.QUANTBONUS    AS QUANTBONUS, 
#                            FND.VLRPRECOMEDIO AS VLRPRECOMEDIO,
#                            FND.VLRPRECOTETO  AS VLRPRECOTETO,  
#                            FND.PERCENTBALAC  AS PERCENTBALAC,  
#                            FND.NOTABALAC     AS NOTABALAC,  
#                            FND.SITUACAO      AS SITUACAO ,  
#                            COT.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO,  
#                            COT.VLRPRECOANTERIOR AS VLRPRECOANTERIOR,  
#                            COT.VLRVARIACAO AS VLRVARIACAO 
#                     FROM TBCARTEIRA_INDICE       FND
#                       INNER JOIN TBCARTEIRA      C ON ( C.ID = FND.IDCARTEIRA )
#                       INNER JOIN TBETF_INDICE    F ON ( F.ID = FND.IDINDICE   )
#                       LEFT JOIN TBETF_INDICE_COTACAO COT ON ( COT.IDINDICE = FND.IDINDICE )
#                     WHERE C.IDUSUARIO = :IDUSUARIO
#                 """
#         if id_carteira: query += " AND FND.IDCARTEIRA = :IDCARTEIRA "
#         if situacao: query += " AND FND.SITUACAO = :SITUACAO "
#         query += " ORDER BY F.CODIGO "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_carteira: params['IDCARTEIRA'] = id_carteira
#         if situacao: params['SITUACAO'] = situacao

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_simples(cls, id_usuario: int = None, id_carteira: int = None, situacao: str = None):
#         query = """ SELECT FND.ID AS ID, 
#                            FND.IDCARTEIRA AS IDCARTEIRA, 
#                            FND.IDINDICE AS IDINDICE, 
#                            F.CODIGO AS CODIGOINDICE, 
#                            FND.QUANT AS QUANT, 
#                            FND.QUANTBONUS AS QUANTBONUS, 
#                            FND.VLRPRECOMEDIO AS VLRPRECOMEDIO,
#                            FND.VLRPRECOTETO AS VLRPRECOTETO,  
#                            FND.PERCENTBALAC AS PERCENTBALAC,  
#                            FND.NOTABALAC AS NOTABALAC,   
#                            FND.SITUACAO AS SITUACAO,  
#                            COT.VLRPRECOFECHAMENTO AS VLRPRECOFECHAMENTO,  
#                            COT.VLRPRECOANTERIOR AS VLRPRECOANTERIOR,  
#                            COT.VLRVARIACAO AS VLRVARIACAO 
#                     FROM TBCARTEIRA_INDICE FND
#                       INNER JOIN TBCARTEIRA C ON ( C.ID = FND.IDCARTEIRA )
#                       INNER JOIN TBETF_INDICE F ON ( F.ID = FND.IDINDICE )
#                       LEFT JOIN TBETF_INDICE_COTACAO COT ON ( COT.IDINDICE = FND.IDINDICE )
#                     WHERE C.IDUSUARIO = :IDUSUARIO
#                 """
#         if id_carteira: query += " AND FND.IDCARTEIRA = :IDCARTEIRA "
#         if situacao: query += " AND FND.SITUACAO = :SITUACAO "
#         query += " ORDER BY F.CODIGO "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if id_carteira: params['IDCARTEIRA'] = id_carteira
#         if situacao: params['SITUACAO'] = situacao

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise


#     @classmethod
#     def buscar_por_id(cls, id_usuario: int = None, id: int = None):
#         query = """ SELECT FND.ID            AS ID, 
#                            FND.IDCARTEIRA    AS IDCARTEIRA, 
#                            C.DESCRICAO       AS DESCRICAOCARTEIRA,
#                            C.TIPO            AS TIPOCARTEIRA,
#                            FND.IDINDICE      AS IDINDICE, 
#                            F.NOME            AS NOMEINDICE, 
#                            F.CODIGO          AS CODIGOINDICE, 
#                            F.SITUACAO        AS SITUACAOINDICE, 
#                            FND.QUANT         AS QUANT, 
#                            FND.QUANTBONUS    AS QUANTBONUS, 
#                            FND.VLRPRECOMEDIO AS VLRPRECOMEDIO,
#                            FND.VLRPRECOTETO  AS VLRPRECOTETO,  
#                            FND.PERCENTBALAC  AS PERCENTBALAC,  
#                            FND.NOTABALAC    AS NOTABALAC,  
#                            FND.SITUACAO      AS SITUACAO 
#                     FROM TBCARTEIRA_INDICE       FND
#                       INNER JOIN TBCARTEIRA      C ON ( C.ID = FND.IDCARTEIRA )
#                       INNER JOIN TBETF_INDICE    F ON ( F.ID = FND.IDINDICE   )
#                     WHERE FND.ID      = :ID
#                       AND C.IDUSUARIO = :IDUSUARIO
#                 """
#         params = {'ID': id, 'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_ativo(cls, id_usuario: int = None, id_indice: int = None):
#         query = """ SELECT FND.ID            AS ID, 
#                            FND.IDCARTEIRA    AS IDCARTEIRA, 
#                            C.DESCRICAO       AS DESCRICAOCARTEIRA,
#                            C.TIPO            AS TIPOCARTEIRA,
#                            FND.IDINDICE      AS IDINDICE, 
#                            F.NOME            AS NOMEINDICE, 
#                            F.CODIGO          AS CODIGOINDICE, 
#                            F.SITUACAO        AS SITUACAOINDICE, 
#                            FND.QUANT         AS QUANT, 
#                            FND.QUANTBONUS    AS QUANTBONUS, 
#                            FND.VLRPRECOMEDIO AS VLRPRECOMEDIO,
#                            FND.VLRPRECOTETO  AS VLRPRECOTETO,  
#                            FND.PERCENTBALAC  AS PERCENTBALAC,  
#                            FND.NOTABALAC    AS NOTABALAC,  
#                            FND.SITUACAO      AS SITUACAO 
#                     FROM TBCARTEIRA_INDICE       FND
#                       INNER JOIN TBCARTEIRA      C ON ( C.ID = FND.IDCARTEIRA )
#                       INNER JOIN TBETF_INDICE    F ON ( F.ID = FND.IDINDICE   )
#                     WHERE C.IDUSUARIO  = :IDUSUARIO
#                       AND FND.IDINDICE = :IDINDICE
#                 """
#         params = {'IDUSUARIO': id_usuario, 'IDINDICE': id_indice}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_dados_grid_radar(cls, id_usuario: int = None):
#         query = """ SELECT F.NOME                 AS RAZAOSOCIAL, 
#                            F.CODIGO               AS CODIGOATIVO, 
#                            'ETF'                  AS DESCRICAOSETOR, 
#                            'ETF'                  AS DESCRICAOSUBSETOR, 
#                            'ETF'                  AS DESCRICAOSEGMENTO, 
#                            CO.VLRPRECOFECHAMENTO  AS PRECO, 
#                            CO.VLRVARIACAO         AS VARIACAO 
#                     FROM TBCARTEIRA_INDICE           FND
#                       INNER JOIN TBCARTEIRA          C  ON ( C.ID        = FND.IDCARTEIRA )
#                       INNER JOIN TBETF_INDICE        F  ON ( F.ID        = FND.IDINDICE   )
#                       LEFT JOIN TBETF_INDICE_COTACAO CO ON ( CO.IDINDICE = FND.IDINDICE   )
#                     WHERE C.IDUSUARIO = :IDUSUARIO
#                       AND FND.SITUACAO = 'A'
#                     ORDER BY F.NOME, F.CODIGO
#                 """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def atualizar_preco_teto(cls, id: int, preco_teto: float, commit: bool = True):
#         try:
#             query = """ UPDATE TBCARTEIRA_INDICE SET VLRPRECOTETO = :VLRPRECOTETO WHERE ID = :ID """
#             params = {'VLRPRECOTETO': preco_teto, 'ID': id}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def atualizar_percent_balanc(cls, id: int, percent_balac: float, commit: bool = True):
#         try:
#             query = """ UPDATE TBCARTEIRA_INDICE SET PERCENTBALAC = :PERCENTBALAC WHERE ID = :ID """
#             params = {'PERCENTBALAC': percent_balac, 'ID': id}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def atualizar_nota_balanc(cls, id: int, nota_balac: int, commit: bool = True):
#         try:
#             query = """ UPDATE TBCARTEIRA_INDICE SET NOTABALAC = :NOTABALAC WHERE ID = :ID """
#             params = {'NOTABALAC': nota_balac, 'ID': id}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def atualizar_id_carteira(cls, id_usuario: int, id: int, id_portfolio: int, commit: bool = True):
#         try:
#             query = "UPDATE TBCARTEIRA_INDICE SET IDCARTEIRA = :IDCARTEIRA WHERE ID = :ID AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO )"
#             params = {'IDUSUARIO': id_usuario, 'ID': id, 'IDCARTEIRA': id_portfolio}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def atualizar_novo_id_carteira(cls, id_usuario: int, id_portfolio_old: int, id_portfolio_new: int, commit: bool = True):
#         try:
#             query = "UPDATE TBCARTEIRA_INDICE SET IDCARTEIRA = :IDCARTEIRA_NEW WHERE IDCARTEIRA = :IDCARTEIRA_OLD AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO )"
#             params = {'IDUSUARIO': id_usuario, 'IDCARTEIRA_OLD': id_portfolio_old, 'IDCARTEIRA_NEW': id_portfolio_new}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def trocar_ativos(cls, id_usuario: int, id_indice_atual: int, id_indice_novo: int, commit: bool = True):
#         try:
#             params = {'IDUSUARIO': id_usuario, 'IDINDICEATUAL': id_indice_atual, 'IDINDICENOVO': id_indice_novo}
#             db.session.execute("UPDATE TBETF_LANCAMENTO       SET IDINDICE = :IDINDICENOVO WHERE IDUSUARIO = :IDUSUARIO AND IDINDICE = :IDINDICEATUAL ", params)
#             db.session.execute("UPDATE TBETF_OPERACAO         SET IDINDICE = :IDINDICENOVO WHERE IDUSUARIO = :IDUSUARIO AND IDINDICE = :IDINDICEATUAL ", params)
#             db.session.execute("UPDATE TBUSUARIO_ACOMP_INDICE SET IDINDICE = :IDINDICENOVO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO) AND IDINDICE = :IDINDICEATUAL ", params)
#             try:
#                 db.session.execute("UPDATE TBCARTEIRA_INDICE      SET IDINDICE = :IDINDICENOVO WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO) AND IDINDICE = :IDINDICEATUAL ", params)
#             except Exception as e:
#                 pass
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def resetar_ativos(cls, id_usuario: int, id_indice: int, commit: bool = True):
#         try:
#             query = "UPDATE TBCARTEIRA_INDICE SET QUANT = 0, QUANTBONUS = 0, VLRPRECOMEDIO = 0.00, SITUACAO = 'F' WHERE IDINDICE = :IDINDICE AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) "
#             params = {'IDUSUARIO': id_usuario, 'IDINDICE': id_indice}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_carteira(cls, id_usuario: int, id_carteira: int, commit: bool = True):
#         try:
#             query = """ DELETE FROM TBCARTEIRA_INDICE WHERE IDCARTEIRA = :IDCARTEIRA AND IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) """
#             params = {'IDCARTEIRA': id_carteira, 'IDUSUARIO': id_usuario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = """ DELETE FROM TBCARTEIRA_INDICE WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) """
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

#     def quant_format(self) -> str:
#         return inteiro_to_str(valor=self.quant)

#     def quant_bonus_format(self) -> str:
#         return inteiro_to_str(valor=self.quant_bonus)

#     def vlr_preco_medio_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_medio)

#     def vlr_preco_teto_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_teto)

#     def percent_balac_format(self) -> str:
#         return decimal_to_str(valor=self.percent_balac)

#     def situacao_descr(self) -> str:
#         if self.situacao == 'A':
#             return 'Ativo'
#         elif self.situacao == 'I':
#             return 'Inativo'
#         elif self.situacao == 'F':
#             return 'Finalizado'
#         else:
#             return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioCarteiraIndice {str(self.id)}>'
