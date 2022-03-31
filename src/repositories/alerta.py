# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro
from app.util.util_datahora import pegar_data_atual, pegar_data_hora_atual, converter_str_to_datetime, converter_datetime_str


class AlertaRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.order_by(cls, db: _orm.dthr_registro).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).order_by(cls, db: _orm.dthr_registro).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id_usuarios(cls, db: _orm.Session, id_usuario: int, id: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT AL.ID, AL.IDUSUARIO, US.NOME AS NMUSUARIO, AL.DTHRREGISTRO, AL.DTENVIO, AL.TIPO, AL.MENSAGEM, AL.QTD_PROC, AL.SITUACAO_TELEGRAM, AL.SITUACAO_EMAIL
                    FROM TBALERTA AL LEFT JOIN TBUSUARIO US ON ( US.ID = AL.IDUSUARIO )
                    WHERE 1 = 1
                """
        if id_usuario: query += " AND AL.IDUSUARIO = :IDUSUARIO  "
        if tipo: query += " AND AL.TIPO = :TIPO "
        if dt_ini: query += " AND AL.DTENVIO  >= :DATAINICIO "
        if dt_fim: query += " AND AL.DTENVIO  <= :DATAFIM "
        query += " ORDER BY AL.DTENVIO, AL.DTHRREGISTRO, AL.ID "

        params = {}
        if id_usuario: params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int):
        query = """ SELECT AL.ID, AL.IDUSUARIO, US.NOME AS NMUSUARIO, AL.DTHRREGISTRO, AL.DTENVIO, AL.TIPO, AL.MENSAGEM, AL.QTD_PROC, AL.SITUACAO_TELEGRAM, AL.SITUACAO_EMAIL
                    FROM TBALERTA AL
                         JOIN TBUSUARIO US ON ( US.ID = AL.IDUSUARIO )
                    WHERE AL.ID = :ID 
                """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_user(cls, db: _orm.Session):
        query = """ SELECT U.ID, U.NOME FROM TBUSUARIO U WHERE EXISTS( SELECT 1 FROM TBALERTA AL WHERE AL.IDUSUARIO = U.ID ) ORDER BY U.NOME """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @staticmethod
    async def registrar(id_usuario: int = None, tipo: str = None, mensagem: str = None):
        try:

            alerta = Alerta()
            alerta.id_usuario = id_usuario
            alerta.dthr_registro = pegar_data_hora_atual()
            alerta.data_envio = pegar_data_atual()
            alerta.tipo = tipo
            alerta.mensagem = mensagem
            alerta.qtd_proc = 0
            alerta.situacao_telegram = 'P'  # P-Pendente
            alerta.situacao_email = 'P'  # P-Pendente

            db.add(alerta)
            db.commit()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))

    @classmethod
    async def excluir(cls, db: _orm.Session, commit: bool = True):
        try:
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
