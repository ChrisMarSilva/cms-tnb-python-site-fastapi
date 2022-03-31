# -*- coding: utf-8 -*-
import sys
import os
#from flask_login import current_user
from src.models.log_erro import LogErroModel
import sqlalchemy.orm as _orm


class LogErroRepository:

    @classmethod
    async def find_all(cls, db: _orm.Session):
        try:
            return cls.query.order_by(cls, db: _orm.data_hora, cls.id).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def find_by_id(cls, db: _orm.Session, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, situacao : str = None):
        query = """ SELECT E.ID, E.DATAHORA, E.IDUSUARIO, U.NOME AS NOMEUSUARIO, E.ARQUIVO, E.LINHA, E.CODIGO, E.TEXTO, E.SITUACAO 
                    FROM TBLOGERRO E LEFT JOIN TBUSUARIO U ON ( U.ID = E.IDUSUARIO ) 
                    WHERE 1 = 1
                """
        if situacao: query += """ AND E.SITUACAO = :SITUACAO  """
        query += """ ORDER BY E.DATAHORA, E.ID  """

        params = {}
        if situacao: params['SITUACAO'] = situacao

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int = None):
        query = """ SELECT E.ID, E.DATAHORA, E.IDUSUARIO, U.NOME AS NOMEUSUARIO, E.ARQUIVO, E.LINHA, E.CODIGO, E.TEXTO, E.SITUACAO FROM TBLOGERRO E LEFT JOIN TBUSUARIO U ON ( U.ID = E.IDUSUARIO ) WHERE E.ID = :ID """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def marcar_tudo(cls, db: _orm.Session, commit: bool = True):
        try:
            query = "UPDATE TBLOGERRO SET SITUACAO = 'L' " # L - LIDO
            params = {}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, commit: bool = True):
        try:
            query = "DELETE FROM TBLOGERRO "
            params = {}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    async def salvar(cls, db: _orm.Session, commit: bool = True):
        try:
            db.add(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    async def excluir(cls, db: _orm.Session, commit: bool = True):
        try:
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @staticmethod
    async def descricao_erro(texto: str = None) -> str:
        try:
            if str(current_user.tipo) == 'A': return str(texto)
            return "Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!"
        except:
            return "Ocorreu um erro ao processar a requisição. Tente novamente mais tarde!"

    @staticmethod
    async def registrar(id_usuario: int = None, arqv: str = None, linha: int = None, texto: str = None) -> bool:
        try:

            try:
                db.rollback()
            except:
                pass

            if texto.strip() == '': return False

            try:
                if not id_usuario: id_usuario = current_user.id
                if id_usuario is not None and str(id_usuario).strip() == '': id_usuario = None
            except:
                id_usuario = None

            try:
                if arqv is not None and arqv.strip() == '': arqv = None
            except:
                arqv = None

            try:
                if linha is not None and str(linha).strip() == '': linha = None
            except:
                linha = None

            try:
                (dt, micro) = pegar_data_hora_atual(fmt='%Y%m%d%H%M%S.%f').split('.')
                data_hora = "%s%03d" % (dt, int(micro) / 1000)
            except Exception as e:
                data_hora = pegar_data_hora_atual()

            log_erro = LogErro()
            log_erro.data_hora = data_hora
            log_erro.id_usuario = id_usuario
            log_erro.arquivo = arqv
            log_erro.linha = linha
            log_erro.texto = texto
            log_erro.situacao = 'N'

            db.add(log_erro)
            db.commit()

            return True

        except Exception as e:
            pass
