# # -*- coding: utf-8 -*-
# import sys
# import os
# import asyncio
# import hashlib
import inspect
import sqlalchemy.orm as _orm
# from app.banco import db
from src.models.usuario import UsuarioModel
# from app.models.log_erro import LogErro
# from app.login import login_manager
# from app.cache import get_cache_user, set_cache_user
# from app.models.usuario_hash import UsuarioHash
# from app.models.usuario_log import UsuarioLog
# from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str
import src.config.config_trace as _tracer

class UsuarioRepository:

    @classmethod
    async def get_by_email_full(cls, db: _orm.Session, email: str) -> UsuarioModel:
        with _tracer.tracer.start_as_current_span(f"{cls.__name__}.{inspect.stack()[0][3]}") as span:
            span.set_attribute("parametro_email", email)
            try:
                return db.query(UsuarioModel).filter((UsuarioModel.email == email) | (UsuarioModel.email.like(email+'@%'))).first()
            except Exception as e:
                span.record_exception(e)
                #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
                raise

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
#     def get_by_email(cls, email: str):
#         try:
#             result = cls.query.filter_by(email=email).first()
#             # db.session.close()
#             return result
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def get_by_email_parcial(cls, email: str):
#         try:
#             result = cls.query.filter(cls.email.like(email+'@%')).first()
#             # db.session.close()
#             return result
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise


#     @classmethod
#     def get_total(cls, data_registro: str = None, situacao: str = None):
#         filters = []
#         if data_registro: filters.append(cls.data_registro == data_registro)
#         if situacao: filters.append(cls.situacao == situacao)
#         try:
#             return cls.query.filter(*filters).count()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos(cls, situacao: str = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT U.ID, U.NOME, U.EMAIL, U.SENHA, U.DTREGISTRO, U.TENTATIVA, U.TIPO, U.FOTO, U.CHATID, U.SITUACAO FROM TBUSUARIO U WHERE 1 = 1 """
#         if situacao: query += " AND U.SITUACAO  = :SITUACAO "
#         if dt_ini: query += " AND EXISTS(SELECT 1 FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = U.ID AND UL.SITUACAO IN ('L','P') AND DATAHORA >= :DATAHORAINI) "
#         if dt_fim: query += " AND EXISTS(SELECT 1 FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = U.ID AND UL.SITUACAO IN ('L','P') AND DATAHORA <= :DATAHORAFIM) "
#         query += " ORDER BY U.NOME, U.ID "

#         params = {}
#         if situacao: params['SITUACAO'] = situacao
#         if dt_ini: params['DATAHORAINI'] = dt_ini
#         if dt_fim: params['DATAHORAFIM'] = dt_fim

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_id(cls,  id: int = None):
#         query = """ SELECT U.ID, U.NOME, U.EMAIL, U.SENHA, U.DTREGISTRO, U.TENTATIVA, U.TIPO, U.FOTO, U.CHATID, U.SITUACAO FROM TBUSUARIO U WHERE U.ID = :ID """
#         params = {'ID': id}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_email(cls, email: str = None):
#         query = """ SELECT U.ID, U.NOME, U.EMAIL, U.SENHA, U.DTREGISTRO, U.TENTATIVA, U.TIPO, U.FOTO, U.CHATID, U.SITUACAO FROM TBUSUARIO U WHERE U.EMAIL = :EMAIL """
#         params = {'EMAIL': email}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_por_email_prefixo(cls, email: str = None):
#         query = """ SELECT U.ID, U.NOME, U.EMAIL, U.SENHA, U.DTREGISTRO, U.TENTATIVA, U.TIPO, U.FOTO, U.CHATID, U.SITUACAO FROM TBUSUARIO U WHERE U.EMAIL LIKE :EMAIL """
#         params = {'EMAIL': email + '@%'}
#         try:
#             return db.session.execute(query, params).first()
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     @asyncio.coroutine
#     async def buscar_total_base(cls, situacao: str = None):
#         query = """ SELECT COUNT(1) AS QTDE FROM TBUSUARIO A WHERE 1 = 1 """
#         if situacao: query += " AND A.SITUACAO = :SITUACAO "
#         params = {}
#         if situacao: params['SITUACAO'] = situacao
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] and rows[0] > 0 else 0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     @asyncio.coroutine
#     async def buscar_total_base_criado(cls, situacao: str = None, data_registro: str = None):
#         query = """ SELECT COUNT(1) AS QTDE FROM TBUSUARIO A WHERE DTREGISTRO = :DTREGISTRO """
#         if situacao: query += " AND A.SITUACAO = :SITUACAO "
#         params = {}
#         params['DTREGISTRO'] = data_registro
#         if situacao: params['SITUACAO'] = situacao
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] and rows[0] > 0 else 0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     @asyncio.coroutine
#     async def buscar_total_base_logado(cls, data: str = None, situacao: str = 'L'):
#         query = """ SELECT COUNT(1) AS QTDE FROM TBUSUARIO U WHERE EXISTS( SELECT 1 FROM TBUSUARIO_LOG L WHERE L.IDUSUARIO = U.ID AND L.DATA = :DATA AND L.SITUACAO = :SITUACAO ) """
#         params = {'DATA': data, 'SITUACAO': situacao}
#         try:
#             rows = db.session.execute(query, params).first()
#             return rows[0] if rows and rows[0] and rows[0] > 0 else 0
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     @classmethod
#     def buscar_todos_grid_investidor(cls, situacao: str = None, dt_ini: str = None, dt_fim: str = None):
#         query = """ SELECT U.ID, U.NOME, U.EMAIL, U.SENHA, U.DTREGISTRO, U.TENTATIVA, U.TIPO, U.FOTO, U.CHATID, U.SITUACAO, 
#                            ( SELECT COUNT(1) FROM TBLANCAMENTO        L WHERE L.IDUSUARIO = U.ID ) AS QTDE_EMPR_LANC,
#                            ( SELECT COUNT(1) FROM TBPROVENTO          L WHERE L.IDUSUARIO = U.ID ) AS QTDE_EMPR_PROV,
#                            ( SELECT COUNT(1) FROM TBFII_LANCAMENTO    L WHERE L.IDUSUARIO = U.ID ) AS QTDE_FII_LANC,
#                            ( SELECT COUNT(1) FROM TBFII_PROVENTO      L WHERE L.IDUSUARIO = U.ID ) AS QTDE_FII_PROV,
#                            ( SELECT COUNT(1) FROM TBETF_LANCAMENTO    L WHERE L.IDUSUARIO = U.ID ) AS QTDE_ETF_LANC,
#                            ( SELECT COUNT(1) FROM TBBDR_LANCAMENTO    L WHERE L.IDUSUARIO = U.ID ) AS QTDE_BDR_LANC,
#                            ( SELECT COUNT(1) FROM TBBDR_PROVENTO      L WHERE L.IDUSUARIO = U.ID ) AS QTDE_BDR_PROV,
#                            ( SELECT COUNT(1) FROM TBCRIPTO_LANCAMENTO L WHERE L.IDUSUARIO = U.ID ) AS QTDE_CRIPTO_LANC,
#                            ( SELECT MAX(UL.DATAHORA) ACESSO FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = U.ID AND UL.SITUACAO = 'L' ) AS DATA_HORA_SITE,
#                            ( SELECT MAX(UL.DATAHORA) ACESSO FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = U.ID AND UL.SITUACAO = 'P' ) AS DATA_HORA_APP
#                     FROM TBUSUARIO U
#                     WHERE 1 = 1
#                 """

#         if situacao: query += " AND U.SITUACAO = :SITUACAO "
#         if dt_ini: query += " AND EXISTS(SELECT 1 FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = U.ID AND UL.SITUACAO IN ('L','P') AND DATAHORA >= :DATAHORAINI ) "
#         if dt_fim: query += " AND EXISTS(SELECT 1 FROM TBUSUARIO_LOG UL WHERE UL.IDUSUARIO = U.ID AND UL.SITUACAO IN ('L','P') AND DATAHORA <= :DATAHORAFIM ) "
#         query += " ORDER BY U.NOME, U.ID "

#         params = {}
#         if situacao: params['SITUACAO'] = str(situacao)
#         if dt_ini: params['DATAHORAINI'] = str(dt_ini)
#         if dt_fim: params['DATAHORAFIM'] = str(dt_fim)

#         try:
#             return db.session.execute(query, params)
#         except Exception as e:
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def resetar_dados(self, commit: bool = True):
#         try:

#             params = {'IDUSUARIO': self.id}

#             try:
#                 db.session.execute("UPDATE TBCEI_OPER_USER_" + str(self.id) + " SET SITUACAO = 'I' WHERE IDUSUARIO = :IDUSUARIO", params)
#             except:
#                 pass
#             try:
#                 db.session.execute("UPDATE TBCEI_PROV_USER_"+str(self.id)+" SET SITUACAO = 'I' WHERE IDUSUARIO = :IDUSUARIO", params)
#             except:
#                 pass

#             db.session.execute("DELETE FROM TBCARTEIRA_PROJECAO_ITEM WHERE IDPROJECAO IN ( SELECT ID FROM TBCARTEIRA_PROJECAO PROJ WHERE PROJ.IDUSUARIO = :IDUSUARIO )", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_PROJECAO      WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_CRIPTO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_BDR    WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_INDICE WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_FUNDO  WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_ATIVO  WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_GRUPO  WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBCARTEIRA_CRIPTO WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_BDR    WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_INDICE WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_FUNDO  WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_ATIVO  WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA        WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBEMPRESA_FATORELEVANTE_ATIVO       WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBFII_FUNDOIMOB_FATORELEVANTE_ATIVO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBETF_FATORELEVANTE_ATIVO           WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBBDR_EMPRESA_FATORELEVANTE_ATIVO   WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBEMPRESA_PROVENTO_ATIVO       WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBFII_FUNDOIMOB_PROVENTO_ATIVO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBBDR_EMPRESA_PROVENTO_ATIVO   WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBPROVENTO     WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBFII_PROVENTO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBBDR_PROVENTO WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBOPERACAO     WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBETF_OPERACAO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBBDR_OPERACAO WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBLANCAMENTO        WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBFII_LANCAMENTO    WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBETF_LANCAMENTO    WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBBDR_LANCAMENTO    WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBCRIPTO_LANCAMENTO WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBAPURACAO           WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBAPURACAO_CALCULADA WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBALUGUEL_ATIVO  WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBCORRETORA      WHERE IDUSUARIO = :IDUSUARIO", params)

#             if commit: db.session.commit()

#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def excluir_tudo(self, commit: bool = True):
#         try:

#             params = {'IDUSUARIO': self.id}

#             try:
#                 db.session.execute("UPDATE TBCEI_OPER_USER_" + str(self.id) + " SET SITUACAO = 'I' WHERE IDUSUARIO = :IDUSUARIO", params)
#             except:
#                 pass

#             try:
#                 db.session.execute("UPDATE TBCEI_PROV_USER_"+str(self.id)+" SET SITUACAO = 'I' WHERE IDUSUARIO = :IDUSUARIO", params)
#             except:
#                 pass

#             db.session.execute("DELETE FROM TBCEI WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBCARTEIRA_PROJECAO_ITEM WHERE IDPROJECAO IN ( SELECT ID FROM TBCARTEIRA_PROJECAO PROJ WHERE PROJ.IDUSUARIO = :IDUSUARIO )", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_PROJECAO      WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_CRIPTO WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_BDR    WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_INDICE WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_FUNDO  WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_ATIVO  WHERE IDGRUPO IN ( SELECT ID FROM TBUSUARIO_ACOMP_GRUPO WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBUSUARIO_ACOMP_GRUPO  WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBCARTEIRA_CRIPTO WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_BDR    WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_INDICE WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_FUNDO  WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA_ATIVO  WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO)", params)
#             db.session.execute("DELETE FROM TBCARTEIRA        WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBBDR_EMPRESA_PROVENTO_ATIVO   WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBFII_FUNDOIMOB_PROVENTO_ATIVO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBEMPRESA_PROVENTO_ATIVO       WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBBDR_PROVENTO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBFII_PROVENTO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBPROVENTO     WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBBDR_OPERACAO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBETF_OPERACAO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBOPERACAO     WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBCRIPTO_LANCAMENTO WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBBDR_LANCAMENTO    WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBETF_LANCAMENTO    WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBFII_LANCAMENTO    WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBLANCAMENTO        WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBCOMENTARIO_ALERTA   WHERE IDUSUARIOORIG = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBCOMENTARIO_ALERTA   WHERE IDUSUARIODSST = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBCOMENTARIO_DENUNCIA WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBCOMENTARIO_REACAO   WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBCOMENTARIO          WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBAPURACAO           WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBAPURACAO_CALCULADA WHERE IDUSUARIO = :IDUSUARIO", params)

#             db.session.execute("DELETE FROM TBALUGUEL_ATIVO  WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBCORRETORA      WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBUSUARIO_CONFIG WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBUSUARIO_LOG    WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBUSUARIO_HASH   WHERE IDUSUARIO = :IDUSUARIO", params)
#             db.session.execute("DELETE FROM TBUSUARIO        WHERE ID = :IDUSUARIO", params)

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
#             raise

#     def excluir(self, commit: bool = True):
#         try:
#             db.session.delete(self)
#             if commit: db.session.commit()
#         except Exception as e:
#             db.session.rollback()
#             LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
#             raise

#     def data_registro_format(self) -> str:
#         return converter_datetime_str(data=converter_str_to_datetime(data=self.data_registro, fmt='%Y%m%d'), fmt='%d/%m/%Y')

#     def tipo_descr(self) -> str:
#         return self.descricao_tipo(tipo=self.tipo)

#     def situacao_descr(self) -> str:
#         return self.descricao_situacao(situacao=self.situacao)

#     @classmethod
#     def descricao_tipo(cls, tipo: str) -> str:
#         if tipo == 'A': return 'Adminstrador'
#         elif tipo == 'I': return 'Investidor'
#         else: return 'Desconhecido'

#     @classmethod
#     def descricao_situacao(cls, situacao: str) -> str:
#         if situacao == 'A': return 'Ativo'
#         elif situacao == 'B': return 'Aguardando Confirmação'
#         elif situacao == 'I': return 'Inativo'
#         elif situacao == 'X': return 'Bloqueado'
#         else: return 'Desconhecido'

#     def __enter__(self):
#         return self

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         pass

#     def __repr__(self):
#         return '<Usuario {str(self.id)} - {self.nome} - {self.email}>'
