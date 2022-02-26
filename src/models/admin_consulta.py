# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro



# class AdminConsulta():

#     def __init__(self):
#         pass

#     @classmethod
#     def buscar_tabelas(cls):
#         query = """ SELECT TABLE_NAME, TABLE_ROWS
#                     FROM INFORMATION_SCHEMA.TABLES
#                     WHERE TABLE_SCHEMA = 'tamonabo_BDCMSTamoNaBolsa'
#                       AND TABLE_TYPE   = 'BASE TABLE'
#                     ORDER BY TABLE_NAME
#             """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_campos(cls):
#         query = """ SELECT TABLE_NAME, 
#                            ORDINAL_POSITION, 
#                            COLUMN_NAME, 
#                            DATA_TYPE, 
#                            IS_NULLABLE, 
#                            COLUMN_DEFAULT, 
#                            COLUMN_TYPE, 
#                            COLUMN_KEY
#                     FROM INFORMATION_SCHEMA.COLUMNS
#                     WHERE TABLE_SCHEMA = 'tamonabo_BDCMSTamoNaBolsa'
#                     ORDER BY TABLE_NAME, ORDINAL_POSITION
#             """
#         params = {}
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_consulta_dinamica(cls, query: str = '', params: dict = {}):
#         try:
#             return db.session.execute(query, params) #.fetchall()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<AdminConsulta >'
