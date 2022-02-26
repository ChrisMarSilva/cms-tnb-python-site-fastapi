# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_datahora import pegar_data_atual, pegar_data_hora_atual, converter_str_to_datetime, converter_datetime_str


# class UsuarioLog(db.Model):

#     __tablename__ = "TBUSUARIO_LOG"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
#     data = db.Column('DATA', db.String(8), nullable=False, index=True)
#     data_hora = db.Column('DATAHORA', db.String(20), nullable=False)
#     host_ip = db.Column('HOSTIP', db.String(50))
#     host_name = db.Column('HOSTNAME', db.String(255))
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self):
#         pass

#     @classmethod
#     def get_all(cls):
#         try:
#             return cls.query.all()
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
#     def get_by_usuario(cls, id_usuario: int):
#         try:
#             return cls.query.filter_by(id_usuario=id_usuario).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_ultimo_acesso(cls, id_usuario: int):
#         query = """ SELECT MAX(UL.DATAHORA) ACESSO FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = :IDUSUARIO AND UL.SITUACAO IN ( 'L', 'P' ) """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_penultimo_acesso(cls, id_usuario: int):
#         query = """ SELECT MAX(PUL.DATAHORA) ACESSO FROM TBUSUARIO_LOG PUL WHERE PUL.IDUSUARIO = :IDUSUARIO AND PUL.SITUACAO IN ( 'L', 'P' ) AND PUL.DATAHORA < ( SELECT MAX(UL.DATAHORA) FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = PUL.IDUSUARIO AND UL.SITUACAO = PUL.SITUACAO ) """
#         params = {'IDUSUARIO': id_usuario}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_ultimo_acesso_usuario(cls, id_usuario: int, situacao: str = None):
#         query = """ SELECT MAX(UL.DATAHORA) ACESSO FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = :IDUSUARIO AND UL.SITUACAO = :SITUACAO """
#         params = {'IDUSUARIO': id_usuario, 'SITUACAO': situacao}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_teve_acesso(cls, id_usuario: int, data: str = None, situacao: str = None):
#         query = """ SELECT MAX(UL.ID) ID FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = :IDUSUARIO AND UL.SITUACAO = :SITUACAO AND UL.DATA = :DATA """
#         params = {'IDUSUARIO': id_usuario, 'DATA': data, 'SITUACAO': situacao}
#         try:
#             rows = db.session.execute(query, params).first()
#             return 'S' if rows and rows[0] and rows[0] > 0 else 'N'
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_by_usuario(cls, id_usuario: int, commit: bool = True):
#         try:
#             cls.query.filter_by(id_usuario=id_usuario).delete()
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def excluir_tudo(cls, id_usuario: int, commit: bool = True):
#         try:
#             query = "DELETE FROM TBUSUARIO_LOG WHERE IDUSUARIO = :IDUSUARIO"
#             params = {'IDUSUARIO': id_usuario}
#             db.session.execute(query, params)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @staticmethod
#     def registrar(id_usuario: int, situacao: str = 'L'):
#         try:

#             # L-Login Site
#             # P-Login App
#             # S-logout
#             # I-Senha Invalida
#             # B-Inativar Usuario
#             # A-Alterou Senha
#             # D-Redefinir Senha
#             # R-Resetar Operações

#             try:
#                 (dt, micro) = pegar_data_hora_atual(fmt='%Y%m%d%H%M%S.%f').split('.')
#                 data_hora = "%s%03d" % (dt, int(micro) / 1000)
#             except Exception as e:
#                 data_hora = pegar_data_hora_atual()

#             usuario_log = UsuarioLog()
#             usuario_log.id_usuario = id_usuario
#             usuario_log.data = pegar_data_atual()
#             usuario_log.data_hora = data_hora
#             usuario_log.situacao = situacao
#             db.session.add(usuario_log)
#             db.session.commit()

#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))

#     def data_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_hora_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<UsuarioLog %r>' % str(self.id_usuario)
