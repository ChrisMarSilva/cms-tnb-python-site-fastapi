# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class ACAOEmpresaFinanceiroDFCTrimestral(db.Model):

#     __tablename__ = "TBEMPRESA_FINAN_DFC_TRIMESTRAL"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     cod_cvm = db.Column('CD_CVM', db.String(6), nullable=True, index=True)
#     ano_refer = db.Column('ANO_REFER', db.String(4), nullable=True, index=True)
#     tri_refer = db.Column('TRI_REFER', db.String(6), nullable=True, index=True)
#     vlr_caixa_liquido_operac = db.Column('VLR_CAIXA_LIQUIDO_OPERAC', db.Float(29, 10), nullable=True)
#     vlr_caixa_liquido_operac_gerado = db.Column('VLR_CAIXA_LIQUIDO_OPERAC_CAIXA_GERADO', db.Float(29, 10), nullable=True)
#     vlr_caixa_liquido_operac_variacoes = db.Column('VLR_CAIXA_LIQUIDO_OPERAC_VARIACOES', db.Float(29, 10), nullable=True)
#     vlr_caixa_liquido_operac_outros = db.Column('VLR_CAIXA_LIQUIDO_OPERAC_OUTROS', db.Float(29, 10), nullable=True)
#     vlr_caixa_liquido_operac_depre_amort = db.Column('VLR_CAIXA_LIQUIDO_OPERAC_DEPRECIACAO_AMORTIZACAO', db.Float(29, 10), nullable=True)
#     vlr_caixa_liquido_invest = db.Column('VLR_CAIXA_LIQUIDO_INVEST', db.Float(29, 10), nullable=True)
#     vlr_caixa_liquido_finan = db.Column('VLR_CAIXA_LIQUIDO_FINAN', db.Float(29, 10), nullable=True)
#     vlr_variacao_cambial = db.Column('VLR_VARIACOES_CAMBIAL', db.Float(29, 10), nullable=True)
#     vlr_caixa_equivalente = db.Column('VLR_CAIXA_EQUIVALENTE', db.Float(29, 10), nullable=True)
#     vlr_caixa_equivalente_saldo_ini = db.Column('VLR_CAIXA_EQUIVALENTE_SALDO_INICIA', db.Float(29, 10), nullable=True)
#     vlr_caixa_equivalente_saldo_fim = db.Column('VLR_CAIXA_EQUIVALENTE_SALDO_FINAL', db.Float(29, 10), nullable=True)
#     vlr_caixa_total = db.Column('VLR_CAIXA_TOTAL', db.Float(29, 10), nullable=True)
#     vlr_caixa_livre = db.Column('VLR_CAIXA_LIVRE', db.Float(29, 10), nullable=True)

#     def __init__(self, id: int = None, cod_cvm: str = None, ano_refer: str = None, tri_refer: str = None, vlr_caixa_liquido_operac: float = 0.0,
#                  vlr_caixa_liquido_operac_gerado: float = 0.0, vlr_caixa_liquido_operac_variacoes: float = 0.0,
#                  vlr_caixa_liquido_operac_outros: float = 0.0, vlr_caixa_liquido_operac_depre_amort: float = 0.0,
#                  vlr_caixa_liquido_invest: float = 0.0, vlr_caixa_liquido_finan: float = 0.0, vlr_variacao_cambial: float = 0.0,
#                  vlr_caixa_equivalente: float = 0.0, vlr_caixa_equivalente_saldo_ini: float = 0.0, vlr_caixa_equivalente_saldo_fim: float = 0.0,
#                  vlr_caixa_total: float = 0.0, vlr_caixa_livre: float = 0.0):
#         self.id = id
#         self.cod_cvm = cod_cvm
#         self.ano_refer = ano_refer
#         self.tri_refer = tri_refer
#         self.vlr_caixa_liquido_operac = vlr_caixa_liquido_operac
#         self.vlr_caixa_liquido_operac_gerado = vlr_caixa_liquido_operac_gerado
#         self.vlr_caixa_liquido_operac_variacoes = vlr_caixa_liquido_operac_variacoes
#         self.vlr_caixa_liquido_operac_outros = vlr_caixa_liquido_operac_outros
#         self.vlr_caixa_liquido_operac_depre_amort = vlr_caixa_liquido_operac_depre_amort
#         self.vlr_caixa_liquido_invest = vlr_caixa_liquido_invest
#         self.vlr_caixa_liquido_finan = vlr_caixa_liquido_finan
#         self.vlr_variacao_cambial = vlr_variacao_cambial
#         self.vlr_caixa_equivalente = vlr_caixa_equivalente
#         self.vlr_caixa_equivalente_saldo_ini = vlr_caixa_equivalente_saldo_ini
#         self.vlr_caixa_equivalente_saldo_fim = vlr_caixa_equivalente_saldo_fim
#         self.vlr_caixa_total = vlr_caixa_total
#         self.vlr_caixa_livre = vlr_caixa_livre

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.order_by(cls.ano_refer, cls.cod_cvm).all()
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
#     def get_all_by_cod_cvm(cls, cod_cvm: str):
#         try:
#             return cls.query.filter_by(cod_cvm=cod_cvm).order_by(cls.ano_refer, cls.tri_refer).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<ACAOEmpresaFinanceiroDFCTrimestral {str(self.id)}>'

