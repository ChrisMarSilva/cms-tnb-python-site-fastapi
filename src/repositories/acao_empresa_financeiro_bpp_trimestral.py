# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class ACAOEmpresaFinanceiroBPPTrimestral(db.Model):

#     __tablename__ = "TBEMPRESA_FINAN_BPP_TRIMESTRAL"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     cod_cvm = db.Column('CD_CVM', db.String(6), nullable=True, index=True)
#     ano_refer = db.Column('ANO_REFER', db.String(4), nullable=True, index=True)
#     tri_refer = db.Column('TRI_REFER', db.String(6), nullable=True, index=True)
#     vlr_passivo_total = db.Column('VLR_PASSIVO_TOTAL', db.Float(29, 10), nullable=True)
#     vlr_circulante = db.Column('VLR_CIRCULANTE', db.Float(29, 10), nullable=True)
#     vlr_circulante_salarios = db.Column('VLR_CIRCULANTE_SALARIOS', db.Float(29, 10), nullable=True)
#     vlr_circulante_fornecedores = db.Column('VLR_CIRCULANTE_FORNECEDORES', db.Float(29, 10), nullable=True)
#     vlr_circulante_emprestimos = db.Column('VLR_CIRCULANTE_EMPRESTIMOSS', db.Float(29, 10), nullable=True)
#     vlr_circulante_outros = db.Column('VLR_CIRCULANTE_OUTROS', db.Float(29, 10), nullable=True)
#     vlr_nao_circulante = db.Column('VLR_NAO_CIRCULANTE', db.Float(29, 10), nullable=True)
#     vlr_nao_circulante_emprestimos = db.Column('VLR_NAO_CIRCULANTE_EMPRESTIMOSS', db.Float(29, 10), nullable=True)
#     vlr_nao_circulante_outros = db.Column('VLR_NAO_CIRCULANTE_OUTROS', db.Float(29, 10), nullable=True)
#     vlr_patrimonio_liquido_consolidado = db.Column('VLR_PATRIMONIO_LIQUIDO_CONSOLIDADO', db.Float(29, 10), nullable=True)
#     vlr_patrimonio_capital_social_realizado = db.Column('VLR_PATRIMONIO_CAPITAL_SOCIAL_REALIZADO', db.Float(29, 10), nullable=True)
#     vlr_patrimonio_lucro_prejuizo_acumulado = db.Column('VLR_PATRIMONIO_LUCRO_PREJUIZO_ACUMULADO', db.Float(29, 10), nullable=True)
#     vlr_patrimonio_reserva_capital = db.Column('VLR_PATRIMONIO_RESERVA_CAPITAL', db.Float(29, 10), nullable=True)
#     vlr_patrimonio_reserva_lucros = db.Column('VLR_PATRIMONIO_RESERVA_LUCROS', db.Float(29, 10), nullable=True)
#     vlr_patrimonio_participacoes = db.Column('VLR_PATRIMONIO_PARTICIPACAO_NAO_CONTROLADORES', db.Float(29, 10), nullable=True)
#     vlr_patrimonio_outros = db.Column('VLR_PATRIMONIO_OUTROS', db.Float(29, 10), nullable=True)

#     def __init__(self, id: int = None, cod_cvm: str = None, ano_refer: str = None, tri_refer: str = None, vlr_passivo_total: float = 0.0, vlr_circulante: float = 0.0,
#                  vlr_circulante_salarios: float = 0.0, vlr_circulante_fornecedores: float = 0.0, vlr_circulante_emprestimos: float = 0.0,
#                  vlr_circulante_outros: float = 0.0, vlr_nao_circulante: float = 0.0, vlr_nao_circulante_emprestimos: float = 0.0,
#                  vlr_nao_circulante_outros: float = 0.0, vlr_patrimonio_liquido_consolidado: float = 0.0, vlr_patrimonio_capital_social_realizado: float = 0.0,
#                  vlr_patrimonio_lucro_prejuizo_acumulado: float = 0.0, vlr_patrimonio_reserva_capital: float = 0.0, vlr_patrimonio_reserva_lucros: float = 0.0,
#                  vlr_patrimonio_participacoes: float = 0.0, vlr_patrimonio_outros: float = 0.0):
#         self.id = id
#         self.cod_cvm = cod_cvm
#         self.ano_refer = ano_refer
#         self.tri_refer = tri_refer
#         self.vlr_passivo_total = vlr_passivo_total
#         self.vlr_circulante = vlr_circulante
#         self.vlr_circulante_salarios = vlr_circulante_salarios
#         self.vlr_circulante_fornecedores = vlr_circulante_fornecedores
#         self.vlr_circulante_emprestimos = vlr_circulante_emprestimos
#         self.vlr_circulante_outros = vlr_circulante_outros
#         self.vlr_nao_circulante = vlr_nao_circulante
#         self.vlr_nao_circulante_emprestimos = vlr_nao_circulante_emprestimos
#         self.vlr_nao_circulante_outros = vlr_nao_circulante_outros
#         self.vlr_patrimonio_liquido_consolidado = vlr_patrimonio_liquido_consolidado
#         self.vlr_patrimonio_capital_social_realizado = vlr_patrimonio_capital_social_realizado
#         self.vlr_patrimonio_lucro_prejuizo_acumulado = vlr_patrimonio_lucro_prejuizo_acumulado
#         self.vlr_patrimonio_reserva_capital = vlr_patrimonio_reserva_capital
#         self.vlr_patrimonio_reserva_lucros = vlr_patrimonio_reserva_lucros
#         self.vlr_patrimonio_participacoes = vlr_patrimonio_participacoes
#         self.vlr_patrimonio_outros = vlr_patrimonio_outros

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
#         return '<ACAOEmpresaFinanceiroBPPTrimestral {str(self.id)}>'

