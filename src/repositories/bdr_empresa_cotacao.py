# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class BDREmpresaCotacao(db.Model):

#     __tablename__ = "TBBDR_EMPRESA_COTACAO"

#     data = db.Column('DATA', db.String(8), nullable=False, index=True)
#     id_bdr = db.Column('IDBDR', db.Integer, db.ForeignKey('TBBDR_EMPRESA.ID'), primary_key=True, nullable=False, index=True)
#     vlr_preco_abertura = db.Column('VLRPRECOABERTURA', db.Float(17, 2), nullable=False)
#     vlr_preco_fechamento = db.Column('VLRPRECOFECHAMENTO', db.Float(17, 2), nullable=False)
#     vlr_preco_maximo = db.Column('VLRPRECOMAXIMO', db.Float(17, 2), nullable=False)
#     vlr_preco_minimo = db.Column('VLRPRECOMINIMO', db.Float(17, 2), nullable=False)
#     vlr_preco_anterior = db.Column('VLRPRECOANTERIOR', db.Float(17, 2), nullable=False)
#     vlr_variacao = db.Column('VLRVARIACAO', db.Float(17, 2), nullable=False)
#     data_hora_alteracao = db.Column('DATAHORAALTERACO', db.String(14), nullable=False)

#     def __init__(self, data: str = None, id_bdr: int = None, vlr_preco_abertura: float = 0.0,
#                  vlr_preco_fechamento: float = 0.0, vlr_preco_maximo: float = 0.0, vlr_preco_minimo: float = 0.0,
#                  vlr_preco_anterior: float = 0.0, vlr_variacao: float = 0.0, data_hora_alteracao: str = None):
#         self.data = data
#         self.id_bdr = id_bdr
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
#     def get_by_ativo(cls, id_bdr: int):
#         try:
#             return cls.query.filter_by(id_bdr=id_bdr).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls):
#         query = """ SELECT C.DATA, 
#                            C.IDBDR    AS IDBDR, 
#                            E.CODIGO   AS CODIGOBDR, 
#                            E.SITUACAO AS SITUACAOBDR,
#                            C.VLRPRECOABERTURA,  
#                            C.VLRPRECOFECHAMENTO,  
#                            C.VLRPRECOMAXIMO, 
#                            C.VLRPRECOMINIMO,
#                            C.VLRPRECOANTERIOR, 
#                            C.VLRVARIACAO, 
#                            C.DATAHORAALTERACO 
#                     FROM TBBDR_EMPRESA_COTACAO C
#                       INNER JOIN TBEMPRESA_ATIVO E ON ( E.ID = C.IDBDR )
#                     WHERE E.SITUACAO = 'A'
#                     ORDER BY E.CODIGO
#                 """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_completo(cls, id_usuario: int = None, setor: str = None, subsetor: str = None, segmento: str = None, codigo: str = None, tipo: str = None):
#         query = """ SELECT C.DATA, 
#                            C.IDBDR  AS IDBDR, 
#                            E.CODIGO   AS CODIGOBDR, 
#                            E.SITUACAO AS SITUACAOBDR,
#                            E.NOME     AS NOMEEMPRESA,
#                            E.RAZAOSOCIAL AS RAZAOSOCIALEMPRESA,
#                            C.VLRPRECOABERTURA,  
#                            C.VLRPRECOFECHAMENTO,  
#                            C.VLRPRECOMAXIMO, 
#                            C.VLRPRECOMINIMO,
#                            C.VLRPRECOANTERIOR, 
#                            C.VLRVARIACAO, 
#                            C.DATAHORAALTERACO 
#                     FROM TBBDR_EMPRESA_COTACAO C
#                       INNER JOIN TBEMPRESA E  ON ( E.ID  = C.IDBDR  )
#                       LEFT  JOIN TBEMPRESA_SETOR    SR ON ( SR.ID = E.IDSETOR    )
#                       LEFT  JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID = E.IDSUBSETOR )
#                       LEFT  JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO )
#                     WHERE E.SITUACAO = 'A'
#                 """

#         if setor:
#             query += " AND SR.ID = :IDSETOR "
#         if subsetor:
#             query += " AND SS.ID = :IDSUBSETOR "
#         if segmento:
#             query += " AND SG.ID = :IDSEGMENTO "
#         if codigo:
#             query += " AND E.CODIGO = :CODIGO "
#         if tipo == 'M':  # M-Meus Ativos
#             query += " AND EXISTS( SELECT 1 FROM TBCARTEIRA CT INNER JOIN TBCARTEIRA_BDR CA ON ( CT.ID = CA.IDCARTEIRA ) WHERE CA.IDBDR = E.ID AND CT.IDUSUARIO = :IDUSUARIO AND (CA.QUANT + CA.QUANTBONUS ) > 0 ) "
#         elif tipo == 'C':  #C-Ativos Comprados por Todos
#             query += " AND EXISTS( SELECT 1 FROM TBCARTEIRA CT INNER JOIN TBCARTEIRA_BDR CA ON ( CT.ID = CA.IDCARTEIRA ) WHERE CA.IDBDR = E.ID AND (CA.QUANT + CA.QUANTBONUS ) > 0 ) "

#         query += " ORDER BY E.CODIGO "

#         params = {}
#         if setor:
#             params['IDSETOR'] = setor
#         if subsetor:
#             params['IDSUBSETOR'] = subsetor
#         if segmento:
#             params['IDSEGMENTO'] = segmento
#         if codigo:
#             params['CODIGO'] = codigo
#         if tipo == 'M':  # M-Meus Ativos
#             params['IDUSUARIO'] = id_usuario
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_codigo(cls, codigo: str):
#         query = """ SELECT C.DATA, 
#                            C.IDBDR  AS IDBDR, 
#                            E.CODIGO   AS CODIGOBDR, 
#                            E.SITUACAO AS SITUACAOBDR,
#                            C.VLRPRECOABERTURA,  
#                            C.VLRPRECOFECHAMENTO,  
#                            C.VLRPRECOMAXIMO, 
#                            C.VLRPRECOMINIMO,
#                            C.VLRPRECOANTERIOR, 
#                            C.VLRVARIACAO, 
#                            C.DATAHORAALTERACO 
#                     FROM TBBDR_EMPRESA_COTACAO C
#                       INNER JOIN TBBDR_EMPRESA E ON ( E.ID = C.IDBDR )
#                     WHERE E.CODIGO   = :CODIGO 
#                       AND E.SITUACAO = 'A'
#                 """
#         params = {'CODIGO': codigo}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id_bdr(cls, id_bdr: int):
#         query = """ SELECT C.VLRPRECOFECHAMENTO FROM TBBDR_EMPRESA_COTACAO C WHERE C.IDBDR = :IDBDR """
#         params = {'IDBDR': id_bdr}
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
#         return '<BDREmpresaAtivoCotacao {str(self.id)}>'
