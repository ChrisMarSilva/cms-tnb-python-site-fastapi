# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class ACAOEmpresaFinanceiroDRETrimestral(db.Model):

#     __tablename__ = "TBEMPRESA_FINAN_DRE_TRIMESTRAL"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     cod_cvm = db.Column('CD_CVM', db.String(6), nullable=True, index=True)
#     ano_refer = db.Column('ANO_REFER', db.String(4), nullable=True, index=True)
#     tri_refer = db.Column('TRI_REFER', db.String(6), nullable=True, index=True)
#     vlr_receita_liq = db.Column('VLR_RECEITA_LIQ', db.Float(29, 10), nullable=True)
#     vlr_custo = db.Column('VLR_CUSTO', db.Float(29, 10), nullable=True)
#     vlr_lucro_bruto = db.Column('VLR_LUCRO_BRUTO', db.Float(29, 10), nullable=True)
#     vlr_margem_bruta = db.Column('VLR_MARGEM_BRUTA', db.Float(5, 2), nullable=True)
#     vlr_despesa_operac = db.Column('VLR_DESPESA_OPERAC', db.Float(29, 10), nullable=True)
#     vlr_resultado_operac = db.Column('VLR_RESULTADO_OPERAC', db.Float(29, 10), nullable=True)
#     vlr_margem_operac = db.Column('VLR_MARGEM_OPERAC', db.Float(5, 2), nullable=True)
#     vlr_resultado_finan = db.Column('VLR_RESULTADO_FINAN', db.Float(29, 10), nullable=True)
#     vlr_resultado_antes_ir = db.Column('VLR_RESULTADO_ANTES_IR', db.Float(29, 10), nullable=True)
#     vlr_imposto = db.Column('VLR_IMPOSTO', db.Float(29, 10), nullable=True)
#     vlr_operac_cont = db.Column('VLR_OPERAC_CONT', db.Float(29, 10), nullable=True)
#     vlr_operac_descont = db.Column('VLR_OPERAC_DESCONT', db.Float(29, 10), nullable=True)
#     vlr_lucro_liquido = db.Column('VLR_LUCRO_LIQUIDO', db.Float(29, 10), nullable=True)
#     vlr_margem_liquida = db.Column('VLR_MARGEM_LIQUIDA', db.Float(5, 2), nullable=True)

#     def __init__(self, id: int = None, cod_cvm: str = None, ano_refer: str = None, tri_refer: str = None, vlr_receita_liq: float = 0.0,
#                  vlr_custo: float = 0.0, vlr_lucro_bruto: float = 0.0, vlr_margem_bruta: float = 0.0,
#                  vlr_despesa_operac: float = 0.0, vlr_resultado_operac: float = 0.0, vlr_margem_operac: float = 0.0,
#                  vlr_resultado_finan: float = 0.0, vlr_resultado_antes_ir: float = 0.0, vlr_imposto: float = 0.0,
#                  vlr_operac_cont: float = 0.0, vlr_operac_descont: float = 0.0, vlr_lucro_liquido: float = 0.0,
#                  vlr_margem_liquida: float = 0.0):
#         self.id = id
#         self.cod_cvm = cod_cvm
#         self.ano_refer = ano_refer
#         self.tri_refer = tri_refer
#         self.vlr_receita_liq = vlr_receita_liq
#         self.vlr_custo = vlr_custo
#         self.vlr_lucro_bruto = vlr_lucro_bruto
#         self.vlr_margem_bruta = vlr_margem_bruta
#         self.vlr_despesa_operac = vlr_despesa_operac
#         self.vlr_resultado_operac = vlr_resultado_operac
#         self.vlr_margem_operac = vlr_margem_operac
#         self.vlr_resultado_finan = vlr_resultado_finan
#         self.vlr_resultado_antes_ir = vlr_resultado_antes_ir
#         self.vlr_imposto = vlr_imposto
#         self.vlr_operac_cont = vlr_operac_cont
#         self.vlr_operac_descont = vlr_operac_descont
#         self.vlr_lucro_liquido = vlr_lucro_liquido
#         self.vlr_magem_liquida = vlr_margem_liquida

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
#         return '<ACAOEmpresaFinanceiroDRETrimestral {str(self.id)}>'

