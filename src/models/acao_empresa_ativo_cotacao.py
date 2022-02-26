# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class ACAOEmpresaAtivoCotacao(db.Model):

#     __tablename__ = "TBEMPRESA_ATIVOCOTACAO"

#     data = db.Column('DATA', db.String(8), nullable=False, index=True)
#     id_ativo = db.Column('IDATIVO', db.Integer, db.ForeignKey('TBEMPRESA_ATIVO.ID'), primary_key=True, nullable=False, index=True)
#     vlr_preco_abertura = db.Column('VLRPRECOABERTURA', db.Float(17, 2), nullable=False)
#     vlr_preco_fechamento = db.Column('VLRPRECOFECHAMENTO', db.Float(17, 2), nullable=False)
#     vlr_preco_maximo = db.Column('VLRPRECOMAXIMO', db.Float(17, 2), nullable=False)
#     vlr_preco_minimo = db.Column('VLRPRECOMINIMO', db.Float(17, 2), nullable=False)
#     vlr_preco_anterior = db.Column('VLRPRECOANTERIOR', db.Float(17, 2), nullable=False)
#     vlr_variacao = db.Column('VLRVARIACAO', db.Float(17, 2), nullable=False)
#     data_hora_alteracao = db.Column('DATAHORAALTERACO', db.String(14), nullable=False)

#     def __init__(self, data: str = None, id_ativo: int = None, vlr_preco_abertura: float = 0.0,
#                  vlr_preco_fechamento: float = 0.0, vlr_preco_maximo: float = 0.0, vlr_preco_minimo: float = 0.0,
#                  vlr_preco_anterior: float = 0.0, vlr_variacao: float = 0.0, data_hora_alteracao: str = None):
#         self.data = data
#         self.id_ativo = id_ativo
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
#     def get_by_ativo(cls, id_ativo: int):
#         try:
#             return cls.query.filter_by(id_ativo=id_ativo).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_total(cls):
#         try:
#             return cls.query.count()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls):
#         query = """ SELECT C.DATA, 
#                            C.IDATIVO  AS IDATIVO, 
#                            A.CODIGO   AS CODIGOATIVO, 
#                            A.SITUACAO AS SITUACAOATIVO,
#                            C.VLRPRECOABERTURA,  
#                            C.VLRPRECOFECHAMENTO,  
#                            C.VLRPRECOMAXIMO, 
#                            C.VLRPRECOMINIMO,
#                            C.VLRPRECOANTERIOR, 
#                            C.VLRVARIACAO, 
#                            C.DATAHORAALTERACO 
#                     FROM TBEMPRESA_ATIVOCOTACAO C
#                       INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = C.IDATIVO )
#                     WHERE A.SITUACAO = 'A'
#                     ORDER BY A.CODIGO
#                 """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_completo(cls, id_usuario: int = None, setor: str = None, subsetor: str = None, segmento: str = None, codigo: str = None, tipo: str = None, reg_inicio: int = None, qtde_por_pagina: int = None):
#         query = """ SELECT C.DATA, 
#                            C.IDATIVO  AS IDATIVO, 
#                            A.CODIGO   AS CODIGOATIVO, 
#                            A.SITUACAO AS SITUACAOATIVO,
#                            E.NOME     AS NOMEEMPRESA,
#                            E.NOMRESUMIDO AS NOMRESUMIDOEMPRESA,
#                            E.RAZAOSOCIAL AS RAZAOSOCIALEMPRESA,
#                            SR.ID             AS IDSETOR,
#                            SR.DESCRICAO      AS DESCRICAOSETOR,
#                            SS.ID             AS IDSUBSETOR,
#                            SS.DESCRICAO      AS DESCRICAOSUBSETOR,
#                            SG.ID             AS IDSEGMENTO,
#                            SG.DESCRICAO      AS DESCRICAOSEGMENTO,
#                            C.VLRPRECOABERTURA,  
#                            C.VLRPRECOFECHAMENTO,  
#                            C.VLRPRECOMAXIMO, 
#                            C.VLRPRECOMINIMO,
#                            C.VLRPRECOANTERIOR, 
#                            C.VLRVARIACAO, 
#                            C.DATAHORAALTERACO 
#                     FROM TBEMPRESA_ATIVOCOTACAO C
#                       INNER JOIN TBEMPRESA_ATIVO    A  ON ( A.ID  = C.IDATIVO    )
#                       INNER JOIN TBEMPRESA          E  ON ( E.ID  = A.IDEMPRESA  )
#                       LEFT  JOIN TBEMPRESA_SETOR    SR ON ( SR.ID = E.IDSETOR    )
#                       LEFT  JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID = E.IDSUBSETOR )
#                       LEFT  JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO )
#                     WHERE A.SITUACAO = 'A'
#                 """

#         if setor: query += " AND SR.ID = :IDSETOR "
#         if subsetor: query += " AND SS.ID = :IDSUBSETOR "
#         if segmento: query += " AND SG.ID = :IDSEGMENTO "
#         if codigo: query += " AND A.CODIGO = :CODIGO "
#         if tipo == 'M':  # M-Meus Ativos
#             query += " AND EXISTS( SELECT 1 FROM TBCARTEIRA CT INNER JOIN TBCARTEIRA_ATIVO CA ON ( CT.ID = CA.IDCARTEIRA ) WHERE CA.IDATIVO = A.ID AND CT.IDUSUARIO = :IDUSUARIO AND (CA.QUANT + CA.QUANTBONUS ) > 0 ) "
#         elif tipo == 'C':  # C-Ativos Comprados por Todos
#             query += " AND EXISTS( SELECT 1 FROM TBCARTEIRA CT INNER JOIN TBCARTEIRA_ATIVO CA ON ( CT.ID = CA.IDCARTEIRA ) WHERE CA.IDATIVO = A.ID AND (CA.QUANT + CA.QUANTBONUS ) > 0 ) "

#         query += " ORDER BY A.CODIGO "
#         if reg_inicio and qtde_por_pagina: query += " LIMIT " + str(reg_inicio) + ", " + str(qtde_por_pagina)

#         params = {}
#         if setor: params['IDSETOR'] = setor
#         if subsetor: params['IDSUBSETOR'] = subsetor
#         if segmento: params['IDSEGMENTO'] = segmento
#         if codigo: params['CODIGO'] = codigo
#         if tipo == 'M': params['IDUSUARIO'] = id_usuario

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_codigo(cls, codigo: str):
#         query = """ SELECT C.DATA, 
#                            C.IDATIVO  AS IDATIVO, 
#                            A.CODIGO   AS CODIGOATIVO, 
#                            A.SITUACAO AS SITUACAOATIVO,
#                            C.VLRPRECOABERTURA,  
#                            C.VLRPRECOFECHAMENTO,  
#                            C.VLRPRECOMAXIMO, 
#                            C.VLRPRECOMINIMO,
#                            C.VLRPRECOANTERIOR, 
#                            C.VLRVARIACAO, 
#                            C.DATAHORAALTERACO 
#                     FROM TBEMPRESA_ATIVOCOTACAO C
#                       INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = C.IDATIVO )
#                     WHERE A.CODIGO   = :CODIGO 
#                       AND A.SITUACAO = 'A'
#                 """
#         params = {'CODIGO': codigo}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id_ativo(cls, id_ativo: int):
#         query = """ SELECT C.VLRPRECOFECHAMENTO FROM TBEMPRESA_ATIVOCOTACAO C WHERE C.IDATIVO = :IDATIVO """
#         params = {'IDATIVO': id_ativo}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_total(cls):
#         try:
#             query = """ SELECT COUNT(1) AS QTDE FROM TBEMPRESA_ATIVOCOTACAO C INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = C.IDATIVO ) WHERE A.SITUACAO = 'A' """
#             params = {}
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] and rows[0] > 0 else 0
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
#         return '<EmpresaAtivoCotacao {str(self.id)}>'
