# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class FiiFundoImobCotacao(db.Model):

#     __tablename__ = "TBFII_FUNDOIMOB_COTACAO"

#     data = db.Column('DATA', db.String(8), nullable=False, index=True)
#     id_fundo = db.Column('IDFUNDO', db.Integer, db.ForeignKey('TBFII_FUNDOIMOB.ID'), primary_key=True, nullable=False, index=True)
#     vlr_preco_abertura = db.Column('VLRPRECOABERTURA', db.Float(17, 2), nullable=False)
#     vlr_preco_fechamento = db.Column('VLRPRECOFECHAMENTO', db.Float(17, 2), nullable=False)
#     vlr_preco_maximo = db.Column('VLRPRECOMAXIMO', db.Float(17, 2), nullable=False)
#     vlr_preco_minimo = db.Column('VLRPRECOMINIMO', db.Float(17, 2), nullable=False)
#     vlr_preco_anterior = db.Column('VLRPRECOANTERIOR', db.Float(17, 2), nullable=False)
#     vlr_variacao = db.Column('VLRVARIACAO', db.Float(17, 2), nullable=False)
#     data_hora_alteracao = db.Column('DATAHORAALTERACO', db.String(14), nullable=False)

#     def __init__(self, data: str = None, id_fundo: int = None, vlr_preco_abertura: float = 0.0,
#                  vlr_preco_fechamento: float = 0.0, vlr_preco_maximo: float = 0.0, vlr_preco_minimo: float = 0.0,
#                  vlr_preco_anterior: float = 0.0, vlr_variacao: float = 0.0, data_hora_alteracao: str = None):
#         self.data = data
#         self.id_fundo = id_fundo
#         self.vlr_preco_abertura = vlr_preco_abertura
#         self.vlr_preco_fechamento = vlr_preco_fechamento
#         self.vlr_preco_maximo = vlr_preco_maximo
#         self.vlr_preco_minimo = vlr_preco_minimo
#         self.vlr_preco_anterior = vlr_preco_anterior
#         self.vlr_variacao = vlr_variacao
#         self.data_hora_alteracao = data_hora_alteracao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_fundo(cls, id_fundo: int):
#         try:
#             return cls.query.filter_by(id_fundo=id_fundo).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls):
#         query = """ SELECT C.DATA, 
#                            C.VLRPRECOABERTURA,  
#                            C.VLRPRECOFECHAMENTO,  
#                            C.VLRPRECOMAXIMO, 
#                            C.VLRPRECOMINIMO,
#                            C.VLRPRECOANTERIOR, 
#                            C.VLRVARIACAO, 
#                            C.DATAHORAALTERACO ,
#                            F.ID       AS FUNDOID, 
#                            F.NOME     AS FUNDONOME, 
#                            F.CODIGO   AS FUNDOCODIGO, 
#                            F.SITUACAO AS FUNDOSIT
#                     FROM TBFII_FUNDOIMOB_COTACAO C
#                       INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = C.IDFUNDO )
#                     WHERE F.SITUACAO = 'A'
#                     ORDER BY F.NOME
#                 """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_codigo(cls, codigo: str):
#         query = """ SELECT C.DATA, 
#                            C.VLRPRECOABERTURA,  
#                            C.VLRPRECOFECHAMENTO,  
#                            C.VLRPRECOMAXIMO, 
#                            C.VLRPRECOMINIMO,
#                            C.VLRPRECOANTERIOR, 
#                            C.VLRVARIACAO, 
#                            C.DATAHORAALTERACO ,
#                            F.ID       AS FUNDOID, 
#                            F.NOME     AS FUNDONOME, 
#                            F.CODIGO   AS FUNDOCODIGO, 
#                            F.SITUACAO AS FUNDOSIT
#                     FROM TBFII_FUNDOIMOB_COTACAO C
#                       INNER JOIN TBFII_FUNDOIMOB F ON ( F.ID = C.IDFUNDO )
#                     WHERE F.CODIGO = :CODIGO 
#                 """
#         params = {'CODIGO': codigo}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id_fundo(cls, id_fundo: int):
#         query = """ SSELECT C.VLRPRECOFECHAMENTO FROM TBFII_FUNDOIMOB_COTACAO C WHERE C.IDFUNDO = :IDFUNDO """
#         params = {'IDFUNDO': id_fundo}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
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

#     def vlr_preco_abertura_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_abertura)

#     def vlr_preco_fechamento_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_fechamento)

#     def vlr_preco_maximo_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_maximo)

#     def vlr_preco_minimo_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_minimo)

#     def vlr_preco_anterior_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_anterior)

#     def vlr_variacao_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_variacao)

#     def data_hora_alteracao_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora_alteracao, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<FiiFundoImobCotacao {str(self.id)}>'