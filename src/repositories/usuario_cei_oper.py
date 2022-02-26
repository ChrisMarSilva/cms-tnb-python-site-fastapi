# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro


# class UsuarioCeiOper():

#     tablename = "TBCEI_OPER_USER_"

#     def __init__(self, id: int = None, id_usuario: int = None, tipo: str = None, situacao: str = None):
#         self.id = id
#         self.id_usuario = id_usuario
#         self.tipo = tipo
#         self.situacao = situacao

#     @classmethod
#     def tabela_existe(cls, id_usuario: int):
#         # // $sql  = "SELECT 1 FROM ".self::$table_name." LIMIT 1";
#         # // $sql  = "SHOW TABLES LIKE ".self::$table_name;
#         # // $sql  = "DESCRIBE ".self::$table_name;
#         query = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = :TABLE_NAME"
#         params = {'TABLE_NAME': cls.tablename + str(id_usuario)}
#         return db.session.execute(query, params).first()

#     @classmethod
#     def buscar_todos(cls, id_usuario: int = None, dt_ini: str = None, dt_fim: str = None, codigo: str = None, categoria: str = None):

#         if not cls.tabela_existe(id_usuario=id_usuario):
#             return []

#         query = """ SELECT CO.ID, CO.IDUSUARIO, CO.CATEGORIA, CO.DATA, CO.TIPO, CO.CODIGO, CO.QUANT, CO.PRECO, CO.TOTAL, CO.CORRET_ID, CO.CORRET_NOME, CO.CORRET_CONTA, CO.SITUACAO 
#                     FROM """ + cls.tablename + str(id_usuario) + """ CO 
#                     WHERE CO.IDUSUARIO = :IDUSUARIO
#                 """
#         if dt_ini: query += " AND CO.DATA >= :DATAINICIO "
#         if dt_fim: query += " AND CO.DATA <= :DATAFIM "
#         if codigo: query += " AND CO.CODIGO = :CODIGO "
#         if categoria: query += " AND CO.CATEGORIA = :CATEGORIA "
#         query += " ORDER BY CO.ID "

#         params = {}
#         params['IDUSUARIO'] = id_usuario
#         if dt_ini: params['DATAINICIO'] = dt_ini
#         if dt_fim: params['DATAFIM'] = dt_fim
#         if codigo: params['CODIGO'] = codigo
#         if categoria: params['CATEGORIA'] = categoria

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id_oper(cls, id_usuario: int = None, id: int = None):

#         if not cls.tabela_existe(id_usuario=id_usuario):
#             return []

#         query = """ SELECT CO.ID, CO.IDUSUARIO, CO.CATEGORIA, CO.DATA, CO.TIPO, CO.CODIGO, CO.QUANT, CO.PRECO, CO.TOTAL, CO.CORRET_ID, CO.CORRET_NOME, CO.CORRET_CONTA, CO.SITUACAO 
#                     FROM """ + cls.tablename + str(id_usuario) + """ CO 
#                     WHERE CO.ID = :ID
#                 """
#         params = {'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_lista_codigo(cls, id_usuario: int = None):

#         if not cls.tabela_existe(id_usuario=id_usuario):
#             return []

#         query = """ SELECT DISTINCT CP.CODIGO FROM """ + cls.tablename + str(id_usuario) + """ CP ORDER BY CP.CODIGO """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def atualizar_situacao(cls, id_usuario: int = None, id: int = None, situacao: str = None, commit: bool = True):
#         try:
#             if not cls.tabela_existe(id_usuario=id_usuario):
#                 return True
#             query = """ UPDATE """ + cls.tablename + str(id_usuario) + """ SET SITUACAO = :SITUACAO WHERE ID = :ID """
#             params = {'ID': id, 'SITUACAO': situacao}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#             return True
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def resetar_situacao(cls, id_usuario: int = None, commit: bool = True):
#         try:
#             if not cls.tabela_existe(id_usuario=id_usuario):
#                 return True
#             query = """ UPDATE """ + cls.tablename + str(id_usuario) + """ SET SITUACAO = 'I' WHERE IDUSUARIO = :IDUSUARIO """
#             params = {'IDUSUARIO': id_usuario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#             return True
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def descricao_tipo(cls, tipo: str = '') -> str:
#         if tipo == 'C':
#             return 'Compra'
#         elif tipo == 'V':
#             return 'Venda'
#         return 'Desconhecido'

#     @classmethod
#     def descricao_situacao(cls, situacao: str = '') -> str:
#         if situacao == 'I':
#             return 'Importada'
#         elif situacao == 'L':
#             return 'Lançada'
#         elif situacao == 'C':
#             return 'Conferida'
#         return 'Desconhecida'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioCeiOper {str(self.id)}>'

