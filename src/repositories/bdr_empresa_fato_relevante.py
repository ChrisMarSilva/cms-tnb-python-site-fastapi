# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.xxxxxxxxxxx import xxxxxxxxxxxModel
# from app.models.log_erro import LogErro


class BDREmpresaFatoRelevanteRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session, id_empresa: int = None, dt_env_ini: str = None, dt_env_fim: str = None, reg_inicio: int = 1, qtde_por_pagina: int = 100):
        filters = []
        filters.append(cls, db: _orm.situacao == 'A')
        if id_empresa: filters.append(cls, db: _orm.id_empresa == id_empresa)
        if dt_env_ini: filters.append(cls, db: _orm.data_env >= dt_env_ini)
        if dt_env_fim: filters.append(cls, db: _orm.data_env <= dt_env_fim)
        try:
            return cls.query.filter(*filters).order_by(cls, db: _orm.data_env.desc()).offset(reg_inicio).limit(qtde_por_pagina).all()
            # return cls.query.order_by(cls, db: _orm.reg_inicio.desc()).paginate(page=reg_inicio, per_page=qtde_por_pagina)
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
    async def get_all_by_empresa(cls, db: _orm.Session, id_empresa: int):
        try:
            return cls.query.filter_by(id_empresa=id_empresa).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_total(cls, db: _orm.Session, id_empresa: int = None, dt_env_ini: str = None, dt_env_fim: str = None):
        filters = []
        filters.append(cls, db: _orm.situacao == 'A')
        if id_empresa: filters.append(cls, db: _orm.id_empresa == id_empresa)
        if dt_env_ini: filters.append(cls, db: _orm.data_env >= dt_env_ini)
        if dt_env_fim: filters.append(cls, db: _orm.data_env <= dt_env_fim)
        try:
            return cls.query.filter(*filters).count()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_empresa: int = None, dt_env_ini: str = None, dt_env_fim: str = None, reg_inicio: int = 1, qtde_por_pagina: int = 100):
        query = """ SELECT F.ID, F.IDBDR, F.NMEMPRESA, F.DATA_ENV, F.DATA_REF, F.PROTOCOLO, F.LINK, F.ASSUNTO, F.CONTEUDO, F.SITUACAO FROM TBBDR_EMPRESA_FATORELEVANTE F WHERE F.SITUACAO = 'A' """
        if id_empresa: query += " AND F.IDBDR = :IDBDR "
        if dt_env_ini: query += " AND F.DATA_ENV >= :DATAINICIO "
        if dt_env_fim: query += " AND F.DATA_ENV <= :DATAFIM "
        query += " ORDER BY F.DATA_ENV DESC "
        query += " LIMIT " + str(reg_inicio) + ", " + str(qtde_por_pagina)
        params = {}
        if id_empresa: params['IDBDR'] = id_empresa
        if dt_env_ini: params['DATAINICIO'] = dt_env_ini
        if dt_env_fim: params['DATAFIM'] = dt_env_fim
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int = None):
        query = """ SELECT F.ID, F.IDBDR, F.NMEMPRESA, F.DATA_ENV, F.DATA_REF, F.PROTOCOLO, F.LINK, F.ASSUNTO, F.CONTEUDO, F.SITUACAO FROM TBBDR_EMPRESA_FATORELEVANTE F WHERE F.ID = :ID """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_ano_mes(cls, db: _orm.Session, id_usuario: int, dt_env: str = None):
        query = """ SELECT F.ID, F.IDBDR, F.NMEMPRESA, F.DATA_ENV, F.DATA_REF, F.PROTOCOLO, F.LINK, F.ASSUNTO, F.CONTEUDO, F.SITUACAO 
                    FROM TBBDR_EMPRESA_FATORELEVANTE F
                        JOIN TBBDR_EMPRESA E ON ( E.ID = F.IDBDR )
                    WHERE F.SITUACAO  = 'A'
                      AND F.DATA_ENV >= :DATAENV
                      AND ( EXISTS( SELECT 1
                                    FROM TBCARTEIRA_BDR CA
                                      JOIN TBCARTEIRA C ON ( C.ID = CA.IDCARTEIRA )
                                    WHERE CA.IDBDR  = E.ID
                                      AND C.IDUSUARIO = :IDUSUARIOCARTEIRA
                                      AND CA.SITUACAO = 'A'
                                      AND C.SITUACAO  = 'A'
                            )
                            OR 
                            EXISTS( SELECT 1
                                    FROM TBUSUARIO_ACOMP_BDR RA
                                      JOIN TBUSUARIO_ACOMP_GRUPO R ON ( R.ID = RA.IDGRUPO )
                                    WHERE RA.IDBDR  = E.ID
                                      AND R.IDUSUARIO = :IDUSUARIORADAR
                                      AND RA.SITUACAO = 'A'
                                      AND R.SITUACAO  = 'A'
                            )
                        )
                      AND NOT EXISTS( SELECT 1 FROM TBBDR_EMPRESA_FATORELEVANTE_ATIVO FTVA WHERE FTVA.IDFATO = F.ID AND FTVA.IDUSUARIO = :IDUSUARIOFATO )
                    ORDER BY F.DATA_ENV DESC
                """

        params = {'DATAENV': dt_env, 'IDUSUARIOCARTEIRA': id_usuario, 'IDUSUARIORADAR': id_usuario, 'IDUSUARIOFATO': id_usuario}
        try:
            try:
                return db.execute(query, params)
            except Exception as e:
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_qtde_total_fato(cls, db: _orm.Session, id_empresa: int = None, dt_env_ini: str = None, dt_env_fim: str = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBBDR_EMPRESA_FATORELEVANTE F WHERE F.SITUACAO = 'A' """
        if id_empresa: query += " AND F.IDBDR = :IDBDR "
        if dt_env_ini: query += " AND F.DATA_ENV >= :DATAINICIO "
        if dt_env_fim: query += " AND F.DATA_ENV <= :DATAFIM "
        params = {}
        if id_empresa: params['IDBDR'] = id_empresa
        if dt_env_ini: params['DATAINICIO'] = dt_env_ini
        if dt_env_fim: params['DATAFIM'] = dt_env_fim
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
