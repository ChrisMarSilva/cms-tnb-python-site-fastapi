# # -*- coding: utf-8 -*-
# import sys
# import os
# from app.banco import db
# from app.models.log_erro import LogErro
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


# class ETFIndiceFatoRelevante(db.Model):

#     __tablename__ = "TBETF_FATORELEVANTE"

#     id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
#     id_indice = db.Column('IDINDICE', db.Integer, nullable=True, index=True) # db.ForeignKey('TBFII_FUNDOIMOB.ID')
#     nm_indice = db.Column('NMINDICE', db.String(250), nullable=True, index=True)
#     data_env = db.Column('DATA_ENV', db.String(14), nullable=False)
#     data_ref = db.Column('DATA_REF', db.String(8), nullable=False, index=True)
#     protocolo = db.Column('PROTOCOLO', db.String(50), nullable=False)
#     link = db.Column('LINK', db.String(250), nullable=False)
#     assunto = db.Column('ASSUNTO', db.String(4000), nullable=True)
#     conteudo = db.Column('CONTEUDO', db.Text(), nullable=True)
#     situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

#     def __init__(self, id: int = None, id_indice: int = None, nm_indice: str = None, data_env: str = None,
#                  data_ref: str = None, protocolo: str = None, link: str = None, assunto: str = None,
#                  conteudo: str = None, situacao: str = None):
#         self.id = id
#         self.id_indice = id_indice
#         self.nm_indice = nm_indice
#         self.data_env = data_env
#         self.data_ref = data_ref
#         self.protocolo = protocolo
#         self.link = link
#         self.assunto = assunto
#         self.conteudo = conteudo
#         self.situacao = situacao

#     @classmethod
#     def get_all(cls, id_indice: int = None, dt_env_ini: str = None, dt_env_fim: str = None, reg_inicio: int = 1, qtde_por_pagina: int = 100):
#         filters = []
#         filters.append(cls.situacao == 'A')
#         if id_indice: filters.append(cls.id_indice == id_indice)
#         if dt_env_ini: filters.append(cls.data_env >= dt_env_ini)
#         if dt_env_fim: filters.append(cls.data_env <= dt_env_fim)
#         try:
#             return cls.query.filter(*filters).order_by(cls.data_env.desc()).offset(reg_inicio).limit(qtde_por_pagina).all()
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
#     def get_all_by_indice(cls, id_indice: int):
#         try:
#             return cls.query.filter_by(id_indice=id_indice).all()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_total(cls, id_indice: int = None, dt_env_ini: str = None, dt_env_fim: str = None):
#         filters = []
#         filters.append(cls.situacao == 'A')
#         if id_indice: filters.append(cls.id_indice == id_indice)
#         if dt_env_ini: filters.append(cls.data_env >= dt_env_ini)
#         if dt_env_fim: filters.append(cls.data_env <= dt_env_fim)
#         try:
#             return cls.query.filter(*filters).count()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls, id_indice: int = None, dt_env_ini: str = None, dt_env_fim: str = None, reg_inicio: int = 1, qtde_por_pagina: int = 100):
#         query = """ SELECT F.ID, F.IDINDICE, F.NMINDICE, F.DATA_ENV, F.DATA_REF, F.PROTOCOLO, F.LINK, F.ASSUNTO, F.CONTEUDO, F.SITUACAO  FROM TBETF_FATORELEVANTE F WHERE F.SITUACAO = 'A' """
#         if id_indice: query += " AND F.IDINDICE = :IDINDICE "
#         if dt_env_ini: query += " AND F.DATA_ENV >= :DATAINICIO "
#         if dt_env_fim: query += " AND F.DATA_ENV <= :DATAFIM "
#         query += " ORDER BY F.DATA_ENV DESC "
#         query += " LIMIT " + str(reg_inicio) + ", " + str(qtde_por_pagina)
#         params = {}
#         if id_indice: params['IDINDICE'] = id_indice
#         if dt_env_ini: params['DATAINICIO'] = dt_env_ini
#         if dt_env_fim: params['DATAFIM'] = dt_env_fim
#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls, id: int = None):
#         query = """ SELECT F.ID, F.IDINDICE, F.NMINDICE, F.DATA_ENV, F.DATA_REF, F.PROTOCOLO, F.LINK, F.ASSUNTO, F.CONTEUDO, F.SITUACAO  FROM TBETF_FATORELEVANTE F WHERE F.ID = :ID """
#         params = {'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_ano_mes(cls, id_usuario: int, dt_env: str = None):
#         query = """ SELECT F.ID, F.IDINDICE, F.NMINDICE, F.DATA_ENV, F.DATA_REF, F.PROTOCOLO, F.LINK, F.ASSUNTO, F.CONTEUDO, F.SITUACAO 
#                     FROM TBETF_FATORELEVANTE F
#                         JOIN TBETF_INDICE ETF ON ( ETF.ID = F.IDINDICE )
#                     WHERE F.SITUACAO  = 'A'
#                       AND F.DATA_ENV >= :DATAENV
#                       AND ( EXISTS( SELECT 1
#                                       FROM TBCARTEIRA_INDICE CF
#                                         JOIN TBCARTEIRA C ON ( C.ID = CF.IDCARTEIRA )
#                                       WHERE CF.IDINDICE = ETF.ID
#                                         AND C.IDUSUARIO = :IDUSUARIOCARTEIRA
#                                         AND CF.SITUACAO = 'A'
#                                         AND C.SITUACAO  = 'A'
#                                 )
#                                 OR 
#                                 EXISTS( SELECT 1
#                                         FROM TBUSUARIO_ACOMP_INDICE RF
#                                         JOIN TBUSUARIO_ACOMP_GRUPO R ON ( R.ID = RF.IDGRUPO )
#                                         WHERE RF.IDINDICE = ETF.ID
#                                           AND R.IDUSUARIO = :IDUSUARIORADAR
#                                           AND RF.SITUACAO = 'A'
#                                           AND R.SITUACAO  = 'A'
#                                 )
#                            )
#                       AND NOT EXISTS( SELECT 1 FROM TBETF_FATORELEVANTE_ATIVO FTVA WHERE FTVA.IDFATO = F.ID AND FTVA.IDUSUARIO = :IDUSUARIOFATO )
#                     ORDER BY F.DATA_ENV DESC
#                 """

#         params = {'DATAENV': dt_env, 'IDUSUARIOCARTEIRA': id_usuario, 'IDUSUARIORADAR': id_usuario, 'IDUSUARIOFATO': id_usuario}
#         try:
#             try:
#                 return db.session.execute(query, params)
#             except Exception as e:
#                 return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_qtde_total_fato(cls, id_indice: int = None, dt_env_ini: str = None, dt_env_fim: str = None):
#         query = """ SELECT COUNT(1) AS QTDE FROM TBETF_FATORELEVANTE F WHERE F.SITUACAO = 'A' """
#         if id_indice: query += " AND F.IDINDICE = :IDINDICE "
#         if dt_env_ini: query += " AND F.DATA_ENV >= :DATAINICIO "
#         if dt_env_fim: query += " AND F.DATA_ENV <= :DATAFIM "
#         params = {}
#         if id_indice: params['IDINDICE'] = id_indice
#         if dt_env_ini: params['DATAINICIO'] = dt_env_ini
#         if dt_env_fim: params['DATAFIM'] = dt_env_fim

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def data_env_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_env, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_ref_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ref, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def data_env_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_env, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def data_ref_format_xml(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_ref, fmt='%Y%m%d'), fmt='%Y-%m-%d')

#     def situacao_descr(self) -> str:
#         if self.situacao == 'A':
#             return 'Ativo'
#         elif self.situacao == 'B':
#             return 'Pendente Baixar PDF'
#         elif self.situacao == 'C':
#             return 'Erro ao Baixar PDF'
#         elif self.situacao == 'D':
#             return 'Pendente Processar PDF'
#         elif self.situacao == 'E':
#             return 'Erro ao Processar PDF'
#         else:
#             return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<ETFIndiceFatoRelevante {str(self.id)} - {self.nome} - {self.cnpj}>'
