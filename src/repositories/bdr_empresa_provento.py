# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class BDREmpresaProvento(db.Model):

#     __tablename__ = "TBBDR_EMPRESA_PROVENTO"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     # id_bdr = db.Column('IDBDR', db.Integer, db.ForeignKey('TBBDR_EMPRESA.ID'), nullable=True, index=True)
#     id_bdr = db.Column('IDBDR', db.Integer, nullable=True, index=True)
#     tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
#     categoria = db.Column('CATEGORIA', db.String(1), nullable=True)
#     codigo_isin = db.Column('CODISIN', db.String(50), nullable=True)
#     data_aprov = db.Column('DATAAPROV', db.String(8), nullable=False)
#     data_com = db.Column('DATACOM', db.String(8), nullable=True, index=True)
#     data_ex = db.Column('DATAEX', db.String(8), nullable=True, index=True)
#     data_pagto = db.Column('DATAPAGTO', db.String(8), nullable=True, index=True)
#     vlr_preco = db.Column('VLRPRECO', db.Float(20, 12), nullable=False)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_bdr: int = None, tipo: str = None, categoria: str = None,
#                  codigo_isin: str = None, data_aprov: str = None, data_com: str = None, data_ex: str = None,
#                  data_pagto: str = None, vlr_preco: float = 0.0, situacao: str = None):
#         self.id = id
#         self.id_bdr = id_bdr
#         self.tipo = tipo
#         self.categoria = categoria
#         self.codigo_isin = codigo_isin
#         self.data_aprov = data_aprov
#         self.data_com = data_com
#         self.data_ex = data_ex
#         self.data_pagto = data_pagto
#         self.vlr_preco = vlr_preco
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.order_by(cls.id).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_all_by_empresa(cls, id_bdr: int):
#         try:
#             return cls.query.filter_by(id_bdr=id_bdr).order_by(cls.id).all()
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
#     def buscar_todos(cls, id_empr: int = None, codigo: str = None, tipo: str = None, dt_ex_ini: str = None, dt_ex_fim: str = None, dt_pagto_ini: str = None, dt_pagto_fim: str = None ):
#         query = """ SELECT P.ID,
#                         P.IDBDR       AS IDBDR,
#                         E.NOME        AS NMEMPRESA,
#                         E.RAZAOSOCIAL AS RZEMPRESA,
#                         E.ID          AS IDBDR,
#                         E.CODIGO      AS CODIGOBDR,
#                         P.TIPO,
#                         P.CATEGORIA,
#                         P.CODISIN,
#                         P.DATAAPROV,
#                         P.DATACOM,
#                         P.DATAEX,
#                         P.DATAPAGTO,
#                         P.VLRPRECO,
#                         P.SITUACAO
#                     FROM TBBDR_EMPRESA_PROVENTO  P
#                         JOIN TBBDR_EMPRESA  E ON ( E.ID = P.IDBDR AND E.CODISIN = P.CODISIN  )
#                     WHERE P.SITUACAO = 'A'
#                 """

#         if id_empr: query += " AND P.IDBDR = :IDBDR "
#         if codigo: query += " AND E.CODIGO = :CODIGO "
#         if tipo: query += " AND P.TIPO = :TIPO "
#         if dt_ex_ini: query += " AND P.DATAEX >= :DATAEXINI "
#         if dt_ex_fim: query += " AND P.DATAEX <= :DATAEXFIM "
#         if dt_pagto_ini: query += " AND P.DATAPAGTO >= :DATAPAGTOINI "
#         if dt_pagto_fim: query += " AND P.DATAPAGTO <= :DATAPAGTOFIM "

#         if dt_ex_ini and dt_ex_fim: query += " ORDER BY P.DATAEX "
#         elif dt_pagto_ini and dt_pagto_fim: query += " ORDER BY P.DATAPAGTO "
#         else: query += " ORDER BY P.DATAEX DESC "

#         params = {}
#         if id_empr: params['IDBDR'] = id_empr
#         if codigo: params['CODIGO'] = codigo
#         if tipo: params['TIPO'] = tipo
#         if dt_ex_ini: params['DATAEXINI'] = dt_ex_ini
#         if dt_ex_fim: params['DATAEXFIM'] = dt_ex_fim
#         if dt_pagto_ini: params['DATAPAGTOINI'] = dt_pagto_ini
#         if dt_pagto_fim: params['DATAPAGTOFIM'] = dt_pagto_fim

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int = None):
#         query = """ SELECT P.ID,
#                             P.IDBDR       AS IDBDR,
#                             E.NOME        AS NMEMPRESA,
#                             E.RAZAOSOCIAL AS RZEMPRESA,
#                             E.ID          AS IDBDR,
#                             E.CODIGO      AS CODIGOBDR,
#                             P.TIPO,
#                             P.CATEGORIA,
#                             P.CODISIN,
#                             P.DATAAPROV,
#                             P.DATACOM,
#                             P.DATAEX,
#                             P.DATAPAGTO,
#                             P.VLRPRECO,
#                             P.SITUACAO
#                     FROM TBBDR_EMPRESA_PROVENTO P
#                     JOIN TBBDR_EMPRESA E ON ( E.ID = P.IDBDR AND E.CODISIN = P.CODISIN  )
#                     WHERE P.ID = :ID 
#                 """
#         params = {'ID': id}

#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_usuario(cls, id_usuario: int = None, id_bdr: int = None, codigo: str = None, tipo: str = None, dt_ex: str = None, dt_pagto: str = None):

#         query = """ SELECT  P.ID,
#                             P.IDBDR   AS IDBDR,
#                             E.NOME        AS NMEMPRESA,
#                             E.RAZAOSOCIAL AS RZEMPRESA,
#                             E.ID          AS IDBDR,
#                             E.CODIGO      AS CODIGOBDR,
#                             P.TIPO,
#                             P.CATEGORIA,
#                             P.CODISIN,
#                             P.DATAAPROV,
#                             P.DATACOM,
#                             P.DATAEX,
#                             P.DATAPAGTO,
#                             P.VLRPRECO,
#                             P.SITUACAO
#                     FROM TBBDR_EMPRESA_PROVENTO  P
#                         JOIN TBBDR_EMPRESA E ON ( E.ID = P.IDBDR AND E.CODISIN = P.CODISIN  )
#                     WHERE P.SITUACAO = 'A'
#                 """

#         if id_bdr: query += " AND P.IDBDR = :IDBDR "
#         if codigo: query += " AND E.CODIGO = :CODIGO "
#         if tipo: query += " AND P.TIPO = :TIPO "

#         if dt_ex and dt_pagto: query += " AND ( P.DATAEX >= :DATAEX OR P.DATAPAGTO >= :DATAPAGTO ) "
#         elif dt_ex: query += " AND P.DATAEX >= :DATAEX "
#         elif dt_pagto: query += " AND P.DATAPAGTO >= :DATAPAGTO "
#         query += """ AND ( SELECT 1 FROM TBCARTEIRA_BDR CA JOIN TBCARTEIRA C ON ( C.ID = CA.IDCARTEIRA ) WHERE CA.IDBDR = E.ID AND C.IDUSUARIO = :IDUSUARIO AND CA.SITUACAO = 'A') 
#                      AND NOT EXISTS( SELECT 1 FROM TBBDR_EMPRESA_PROVENTO_ATIVO PRVA WHERE PRVA.IDBDRPROV = P.ID AND PRVA.IDUSUARIO = :IDUSUARIO_PROVATIVO ) """
#         query += " ORDER BY P.DATAEX DESC, P.DATAPAGTO DESC "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDUSUARIO_PROVATIVO'] = id_usuario
#         if id_bdr: params['IDBDR'] = id_bdr
#         if codigo: params['CODIGO'] = codigo
#         if tipo: params['TIPO'] = tipo
#         if dt_ex: params['DATAEX'] = dt_ex
#         if dt_pagto: params['DATAPAGTO'] = dt_pagto

#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 return db.session.execute(query, params)
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
#             params = {'IDBDRPROV': self.id}
#             db.session.execute("DELETE FROM TBBDR_EMPRESA_PROVENTO_ATIVO WHERE IDBDRPROV = :IDBDRPROV", params)
#             db.session.delete(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def data_aprov_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_aprov, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_com_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_com, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_ex_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_pagto_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_aprov_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_aprov, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def data_com_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_com, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def data_ex_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ex, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def data_pagto_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_pagto, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def vlr_preco_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco)

#     def tipo_descr(self) -> str:
#         return self.descricao_tipo(tipo=self.tipo)

#     def categoria_descr(self) -> str:
#         return self.descricao_categoria(categoria=self.categoria)

#     def situacao_descr(self) -> str:
#         return self.descricao_situacao(situacao=self.situacao)

#     @classmethod
#     def descricao_categoria(cls, categoria: str) -> str:
#         if categoria == 'DRN': return 'BDR Não Patrocinado'
#         elif categoria == 'DR1': return 'BDR Nível 1'
#         elif categoria == 'DR2': return 'BDR Nível 2'
#         elif categoria == 'DR3': return 'BDR Nível 3'
#         else: return 'Desconhecida'

#     @classmethod
#     def descricao_situacao(cls, situacao: str) -> str:
#         if situacao == 'A': return 'Ativo'
#         elif situacao == 'I': return 'Inativo'
#         else: return 'Desconhecida'

#     @classmethod
#     def descricao_tipo(cls, tipo: str) -> str:
#         if tipo == 'D': return 'DIVIDENDOS'
#         elif tipo == 'J': return 'JRS CAP PRÓPRIOo'
#         elif tipo == 'S': return 'Subscrição'
#         elif tipo == 'G': return 'Grupamento'
#         elif tipo == 'E': return 'Desdobramento'
#         elif tipo == 'B': return 'Bonificação'
#         elif tipo == 'R': return 'REST CAP DIN'
#         else: return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<EmpresaProvento {str(self.id)}>'