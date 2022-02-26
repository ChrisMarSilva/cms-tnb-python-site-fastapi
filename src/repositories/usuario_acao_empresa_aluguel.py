# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class UsuarioACAOEmpresaAluguel(db.Model):

#     __tablename__ = "TBALUGUEL_ATIVO"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
#     id_ativo = db.Column('IDATIVO', db.Integer, db.ForeignKey('TBEMPRESA_ATIVO.ID'), nullable=False, index=True)
#     data = db.Column('DATA', db.String(8), nullable=False, index=True)
#     valor_bruto = db.Column('VLRBRUTO', db.Float(17, 2), nullable=False)
#     valor_ir = db.Column('VLRIR', db.Float(17, 2), nullable=False)
#     valor_liquido = db.Column('VLRLIQUIDO', db.Float(17, 2), nullable=False)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_usuario: int = None, id_ativo: int = None, data: str = None,
#                  valor_bruto: float = 0.0, valor_ir: float = 0.0, valor_liquido: float = 0.0,
#                  situacao: str = None):
#         self.id = id
#         self.id_usuario = id_usuario
#         self.id_ativo = id_ativo
#         self.data = data
#         self.valor_bruto = valor_bruto
#         self.valor_ir = valor_ir
#         self.valor_liquido = valor_liquido
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_all_by_usuario(cls, id_usuario: int):
#         try:
#             return cls.query.filter_by(id_usuario=id_usuario).order_by(cls.data, cls.id_ativo).all()
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
#     def get_by_usuario(cls, id_usuario: int, id: int):
#         try:
#             return cls.query.filter_by(id_usuario=id_usuario, id=id).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     # from app.models.usuario_empresa_aluguel import UsuarioEmpresaAluguel
#     # return cls.query\
#     #     .join(UsuarioEmpresaAluguel, UsuarioEmpresaAluguel.id_ativo == cls.id)\
#     #     .filter(cls.situacao == 'A', UsuarioEmpresaAluguel.id_usuario == id_usuario)\
#     #     .order_by(cls.codigo)\
#     #     .all()
#     # from app.models.usuario_empresa_lancamento import UsuarioEmpresaLancamento
#     # return cls.query\
#     #     .join(UsuarioEmpresaLancamento, UsuarioEmpresaLancamento.id_ativo == cls.id)\
#     #     .filter(EmpresaAtivo.situacao == 'A', UsuarioEmpresaLancamento.id_usuario == id_usuario)\
#     #     .order_by(cls.codigo)\
#     #     .all()
#     # from app.models.empresa_ativo import EmpresaAtivo
#     # filters = []
#     # filters.append(cls.id_usuario == id_usuario)
#     # if cod_ativo: filters.append(EmpresaAtivo.codigo == cod_ativo)
#     # if dt_ini: filters.append(cls.data >= dt_ini)
#     # if dt_fim: filters.append(cls.data <= dt_fim)
#     # return cls.query\
#     #     .join(EmpresaAtivo, EmpresaAtivo.id == cls.id_ativo) \
#     #     .filter(*filters) \
#     #     .add_columns(EmpresaAtivo.codigo) \
#     #     .order_by(cls.data, cls.id_ativo)\
#     #     .all()

#     @classmethod
#     def buscar_todos(cls, id_usuario: int, codigo: str = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT AL.ID, AL.IDATIVO  AS IDATIVO, A.CODIGO AS CODIGOATIVO, AL.DATA, AL.VLRBRUTO, AL.VLRIR, AL.VLRLIQUIDO, AL.SITUACAO FROM TBALUGUEL_ATIVO AL INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = AL.IDATIVO ) WHERE AL.IDUSUARIO = :IDUSUARIO """
#         if codigo: query += " AND A.CODIGO = :CODIGO "
#         if dt_ini: query += " AND AL.DATA >= :DATAINICIO "
#         if dt_fim: query += " AND AL.DATA <= :DATAFIM "
#         query += " ORDER BY AL.DATA, AL.IDATIVO "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         if dt_ini: params['DATAINICIO'] = dt_ini
#         if dt_fim: params['DATAFIM'] = dt_fim
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int, id_usuario: int):
#         query = """ SELECT AL.ID, 
#                            AL.IDATIVO  AS IDATIVO, 
#                            A.CODIGO    AS CODIGOATIVO, 
#                            AL.DATA, 
#                            AL.VLRBRUTO, 
#                            AL.VLRIR, 
#                            AL.VLRLIQUIDO, 
#                            AL.SITUACAO 
#                     FROM TBALUGUEL_ATIVO AL
#                         INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = AL.IDATIVO )
#                     WHERE AL.ID        = :ID
#                       AND AL.IDUSUARIO = :IDUSUARIO
#                 """
#         params = {'ID': id, 'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_dados_grid_irpf(cls, id_usuario: int, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT MAX(A.CODIGO)      AS CODIGO,
#                            MAX(E.CNPJ)        AS CNPJ,
#                            MAX(E.RAZAOSOCIAL) AS RAZAOSOCIAL,
#                            SUM(AL.VLRLIQUIDO) AS TOTVLR
#                     FROM TBALUGUEL_ATIVO AL
#                       INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = AL.IDATIVO  )
#                       INNER JOIN TBEMPRESA       E ON ( E.ID = A.IDEMPRESA )
#                     WHERE AL.IDUSUARIO = :IDUSUARIO
#                       AND AL.DATA     >= :DATAINICIO
#                       AND AL.DATA     <= :DATAFIM
#                     GROUP BY AL.IDATIVO
#                     ORDER BY E.RAZAOSOCIAL
#                 """
#         params = {'IDUSUARIO': id_usuario, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_vlr_total(cls, id_usuario: int, id_ativo: int, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT IFNULL(SUM(A.VLRLIQUIDO), 0.00 ) AS TOTAL FROM TBALUGUEL_ATIVO A WHERE A.IDUSUARIO = :IDUSUARIO AND A.IDATIVO = :IDATIVO """
#         if dt_ini: query += " AND A.DATA >= :DATAINICIO "
#         if dt_fim: query += " AND A.DATA <= :DATAFIM "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         params['IDATIVO'] = id_ativo
#         if dt_ini: params['DATAINICIO'] = dt_ini
#         if dt_fim: params['DATAFIM'] = dt_fim

#         try:
#             rows = db.session.execute(query, params).first()
#             return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBALUGUEL_ATIVO WHERE IDUSUARIO = :IDUSUARIO"
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

#     def data_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def valor_bruto_format(self) -> str:
#         return decimal_to_str(valor=self.valor_bruto)

#     def valor_ir_format(self) -> str:
#         return decimal_to_str(valor=self.valor_ir)

#     def valor_liquido_format(self) -> str:
#         return decimal_to_str(valor=self.valor_liquido)

#     def situacao_descr(self) -> str:
#         if self.situacao == 'A':
#             return 'Ativo'
#         elif self.situacao == 'I':
#             return 'Inativo'
#         else:
#             return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioEmpresaAluguel {str(self.id)} - {self.nome} - {self.cnpj}>'
