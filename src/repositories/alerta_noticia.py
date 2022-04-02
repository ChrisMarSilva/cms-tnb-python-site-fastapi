# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.alerta_noticia import AlertaNoticiaModel
# from app.models.log_erro import LogErro


class AlertaNoticiaRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(AlertaNoticiaModel).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(AlertaNoticiaModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, dt_hr_ini: str = None, dt_hr_fim: str = None):
        query = """ SELECT AN.ID, AN.SITE, AN.DTHRREGISTRO, AN.TIPO, AN.TITULO, AN.LINK, AN.SITUACAO FROM TBALERTA_NOTICIA AN WHERE 1 = 1 """
        if dt_hr_ini: query += " AND AN.DTHRREGISTRO >= :DATAINICIO "
        if dt_hr_fim: query += " AND AN.DTHRREGISTRO <= :DATAFIM "
        query += " ORDER BY AN.DTHRREGISTRO DESC, ID DESC "

        params = {}
        if dt_hr_ini: params['DATAINICIO'] = dt_hr_ini
        if dt_hr_fim: params['DATAFIM'] = dt_hr_fim

        try:
            try:
                return db.execute(query, params)
            except Exception as e:
                db.rollback()
                db.close()
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: AlertaNoticiaModel, commit: bool = True):
        try:
            db.add(row)
            if commit:db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: AlertaNoticiaModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
