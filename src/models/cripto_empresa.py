# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_formatacao import decimal_to_str
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class CriptoEmpresa(db.Model):

#     __tablename__ = "TBCRIPTO_EMPRESA"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True, index=True)
#     nome = db.Column('NOME', db.String(100), nullable=False, index=True)
#     codigo = db.Column('CODIGO', db.String(10), nullable=False, index=True)
#     vlr_preco_fechamento = db.Column('VLRPRECOFECHAMENTO', db.Float(17, 2), nullable=False)
#     vlr_preco_anterior = db.Column('VLRPRECOANTERIOR', db.Float(17, 2), nullable=False)
#     vlr_variacao = db.Column('VLRVARIACAO', db.Float(17, 2), nullable=False)
#     data_hora_alteracao = db.Column('DATAHORAALTERACO', db.String(14), nullable=False)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, nome: str = None, codigo: str = None, vlr_preco_fechamento: float = 0.0,
#                  vlr_preco_anterior: float = 0.0, vlr_variacao: float = 0.0, data_hora_alteracao: str = None,
#                  situacao: str = None):
#         self.id = id
#         self.nome = nome
#         self.codigo = codigo
#         self.vlr_preco_fechamento = vlr_preco_fechamento
#         self.vlr_preco_anterior = vlr_preco_anterior
#         self.vlr_variacao = vlr_variacao
#         self.data_hora_alteracao = data_hora_alteracao
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.order_by(cls.nome).all()
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
#     def get_by_codigo(cls, codigo: str):
#         try:
#             return cls.query.filter_by(codigo=codigo).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_lista_nomes(cls):
#         try:
#             return cls.query.filter(cls.situacao.in_(['A', 'E'])).order_by(cls.nome).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_lista_codigos(cls):
#         try:
#             return cls.query.filter(cls.situacao.in_(['A', 'E'])).order_by(cls.codigo).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls):
#         query = """ SELECT FI.ID, FI.NOME, FI.CODIGO, FI.VLRPRECOFECHAMENTO, FI.VLRPRECOANTERIOR, FI.VLRVARIACAO, FI.DATAHORAALTERACO, FI.SITUACAO FROM TBCRIPTO_EMPRESA FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.NOME """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int = None):
#         query = """ SELECT FI.ID, FI.NOME, FI.CODIGO, FI.VLRPRECOFECHAMENTO, FI.VLRPRECOANTERIOR, FI.VLRVARIACAO, FI.DATAHORAALTERACO, FI.SITUACAO FROM TBCRIPTO_EMPRESA FI WHERE FI.ID = :ID """
#         params = {'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_codigo(cls, codigo: str = None):
#         query = """ SELECT FI.ID, FI.NOME, FI.CODIGO, FI.VLRPRECOFECHAMENTO, FI.VLRPRECOANTERIOR, FI.VLRVARIACAO, FI.DATAHORAALTERACO, FI.SITUACAO FROM TBCRIPTO_EMPRESA FI WHERE FI.CODIGO = :CODIGO """
#         params = {'CODIGO': codigo}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_nome(cls, nome: str = None):
#         query = """ SELECT FI.ID, FI.NOME, FI.CODIGO, FI.VLRPRECOFECHAMENTO, FI.VLRPRECOANTERIOR, FI.VLRVARIACAO, FI.DATAHORAALTERACO, FI.SITUACAO FROM TBCRIPTO_EMPRESA FI WHERE FI.NOME = :NOME """
#         params = {'NOME': nome}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_nome(cls):
#         query = """ SELECT FI.ID, FI.NOME FROM TBCRIPTO_EMPRESA FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.NOME """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_codigo(cls):
#         query = """ SELECT FI.ID, FI.CODIGO FROM TBCRIPTO_EMPRESA FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.CODIGO """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_pendentes_situacao(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT F.CODIGO, F.ID FROM TBCRIPTO_EMPRESA F WHERE EXISTS( SELECT 1 FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDCRIPTO = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'P' ) """
#         if codigo: query += " AND F.CODIGO = :CODIGO "
#         query += " ORDER BY F.CODIGO "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         try:
#             return db.session.execute(query, params).fetchall()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_irpf(cls, id_usuario: int = None, dt_fim: str = None):
#         query = """ SELECT F.ID, F.CODIGO, F.NOME FROM TBCRIPTO_EMPRESA F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDCRIPTO = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.DATA <= :DATAFIM ) ORDER BY F.CODIGO """
#         params = {'IDUSUARIO': id_usuario, 'DATAFIM': dt_fim}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_codigos_comprados(cls, id_usuario: int = None, codigo: str = None):
#         query = """ SELECT F.ID, F.CODIGO, F.NOME FROM TBCRIPTO_EMPRESA F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBCRIPTO_LANCAMENTO FL WHERE FL.IDCRIPTO = F.ID AND FL.IDUSUARIO = :IDUSUARIO ) """
#         if codigo: query += " AND F.CODIGO = :CODIGO "
#         query += " ORDER BY F.CODIGO "
#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if codigo: params['CODIGO'] = codigo
#         try:
#             return db.session.execute(query, params)
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

#     def vlr_preco_fechamento_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_fechamento)

#     def vlr_preco_anterior_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_preco_anterior)

#     def vlr_variacao_format(self) -> str:
#         return decimal_to_str(valor=self.vlr_variacao)

#     def data_hora_alteracao_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora_alteracao, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

#     def situacao_descr(self) -> str:
#         return self.descricao_situacao(situacao=self.situacao)

#     @classmethod
#     def descricao_situacao(cls, situacao: str) -> str:
#         if situacao == 'A': return 'Ativo'
#         elif situacao == 'I': return 'Inativo'
#         elif situacao == 'E': return 'Encerrado'
#         else: return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<CriptoEmpresa {str(self.id)} - {self.nome} - {self.nome}>'
