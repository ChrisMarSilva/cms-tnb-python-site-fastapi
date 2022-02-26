# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class AlertaNoticia(db.Model):

#     __tablename__ = "TBALERTA_NOTICIA"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     site = db.Column('SITE', db.String(50), nullable=False)
#     dthr_registro = db.Column('DTHRREGISTRO', db.String(14), nullable=False)
#     tipo = db.Column('TIPO', db.String(255), nullable=False)
#     titulo = db.Column('TITULO', db.String(4000), nullable=False)
#     link = db.Column('LINK', db.String(500), nullable=False)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, site: str = None, dthr_registro: str = None, tipo: str = None,
#                  titulo: str = None,  link: str = None, situacao: str = None):
#         self.id = id
#         self.site = site
#         self.dthr_registro = dthr_registro
#         self.tipo = tipo
#         self.titulo = titulo
#         self.link = link
#         self.situacao = situacao

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
#     def buscar_todos(cls, dt_hr_ini: str = None, dt_hr_fim: str = None):
#         query = """ SELECT AN.ID, AN.SITE, AN.DTHRREGISTRO, AN.TIPO, AN.TITULO, AN.LINK, AN.SITUACAO FROM TBALERTA_NOTICIA AN WHERE 1 = 1 """
#         if dt_hr_ini: query += " AND AN.DTHRREGISTRO >= :DATAINICIO "
#         if dt_hr_fim: query += " AND AN.DTHRREGISTRO <= :DATAFIM "
#         query += " ORDER BY AN.DTHRREGISTRO DESC, ID DESC "

#         params = {}
#         if dt_hr_ini: params['DATAINICIO'] = dt_hr_ini
#         if dt_hr_fim: params['DATAFIM'] = dt_hr_fim

#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 db.session.rollback()
#                 db.session.close()
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def salvar(self, commit: bool = True):
#         try:
#             db.session.add(self)
#             if commit:db.session.commit()
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

#     def dthr_registro_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.dthr_registro, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

#     def situacao_descr(self) -> str:
#         if self.situacao == 'P':
#             return 'Pendente'
#         elif self.situacao == 'G':
#             return 'Gerado'
#         else:
#             return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<AlertaNoticia {str(self.id)}>'
