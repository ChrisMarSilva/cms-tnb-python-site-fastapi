# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.fii_fundoimob import FiiFundoImobModel
# from app.models.log_erro import LogErro


class FiiFundoImobRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(FiiFundoImobModel).order_by(FiiFundoImobModel.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(FiiFundoImobModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_codigo(cls, db: _orm.Session, codigo: str):
        try:
            return db.query(FiiFundoImobModel).filter_by(codigo=codigo).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_nomes(cls, db: _orm.Session):
        try:
            return db.query(FiiFundoImobModel).filter(FiiFundoImobModel.situacao.in_(['A', 'E'])).order_by(FiiFundoImobModel.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_codigos(cls, db: _orm.Session):
        try:
            return db.query(FiiFundoImobModel).filter(FiiFundoImobModel.situacao.in_(['A', 'E'])).order_by(FiiFundoImobModel.codigo).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT FI.ID, 
                           FI.NOME, 
                           FI.RAZAOSOCIAL, 
                           FI.CNPJ, 
                           FI.CODIGO, 
                           FI.CODISIN, 
                           FI.SITUACAO, 
                           FITP.ID        AS IDFIITIPO, 
                           FITP.DESCRICAO AS DESCRICAOFIITIPO, 
                           FITP.SITUACAO  AS SITUACAOFIITIPO, 
                           FIADM.ID       AS IDFIIADMIN, 
                           FIADM.NOME     AS NOMEFIIADMIN, 
                           FIADM.CNPJ     AS CNPJFIIADMIN, 
                           FIADM.SITUACAO AS SITUACAOFIIADMIN
                    FROM TBFII_FUNDOIMOB FI
                      LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
                      LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
                    WHERE FI.SITUACAO IN ( 'A' ,'E')
                    ORDER BY FI.NOME
                """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int = None):
        query = """ SELECT FI.ID, 
                           FI.NOME, 
                           FI.RAZAOSOCIAL, 
                           FI.CNPJ, 
                           FI.CODIGO, 
                           FI.CODISIN, 
                           FI.SITUACAO, 
                           FITP.ID        AS IDFIITIPO, 
                           FITP.DESCRICAO AS DESCRICAOFIITIPO, 
                           FITP.SITUACAO  AS SITUACAOFIITIPO, 
                           FIADM.ID       AS IDFIIADMIN, 
                           FIADM.NOME     AS NOMEFIIADMIN, 
                           FIADM.CNPJ     AS CNPJFIIADMIN, 
                           FIADM.SITUACAO AS SITUACAOFIIADMIN
                    FROM TBFII_FUNDOIMOB FI
                        LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
                        LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
                    WHERE FI.ID = :ID 
                """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, codigo: str = None):
        query = """ SELECT 	FI.ID, 
                            FI.NOME, 
                            FI.RAZAOSOCIAL, 
                            FI.CNPJ, 
                            FI.CODIGO, 
                            FI.CODISIN, 
                            FI.SITUACAO, 
                            FITP.ID        AS IDFIITIPO, 
                            FITP.DESCRICAO AS DESCRICAOFIITIPO, 
                            FITP.SITUACAO  AS SITUACAOFIITIPO, 
                            FIADM.ID       AS IDFIIADMIN, 
                            FIADM.NOME     AS NOMEFIIADMIN, 
                            FIADM.CNPJ     AS CNPJFIIADMIN, 
                            FIADM.SITUACAO AS SITUACAOFIIADMIN
                        FROM TBFII_FUNDOIMOB FI
                            LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
                            LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
                        WHERE FI.CODIGO = :CODIGO 
                """
        params = {'CODIGO': codigo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_nome(cls, db: _orm.Session, nome: str = None):
        query = """ SELECT 	FI.ID, 
                            FI.NOME, 
                            FI.RAZAOSOCIAL, 
                            FI.CNPJ, 
                            FI.CODIGO, 
                            FI.CODISIN, 
                            FI.SITUACAO, 
                            FITP.ID        AS IDFIITIPO, 
                            FITP.DESCRICAO AS DESCRICAOFIITIPO, 
                            FITP.SITUACAO  AS SITUACAOFIITIPO, 
                            FIADM.ID       AS IDFIIADMIN, 
                            FIADM.NOME     AS NOMEFIIADMIN, 
                            FIADM.CNPJ     AS CNPJFIIADMIN, 
                            FIADM.SITUACAO AS SITUACAOFIIADMIN
                        FROM TBFII_FUNDOIMOB FI
                            LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
                            LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
                        WHERE FI.NOME = :NOME 
                """
        params = {'NOME': nome}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_razao_social(cls, db: _orm.Session, razao_social: str = None):
        query = """ SELECT 	FI.ID, 
                            FI.NOME, 
                            FI.RAZAOSOCIAL, 
                            FI.CNPJ, 
                            FI.CODIGO, 
                            FI.CODISIN, 
                            FI.SITUACAO, 
                            FITP.ID        AS IDFIITIPO, 
                            FITP.DESCRICAO AS DESCRICAOFIITIPO, 
                            FITP.SITUACAO  AS SITUACAOFIITIPO, 
                            FIADM.ID       AS IDFIIADMIN, 
                            FIADM.NOME     AS NOMEFIIADMIN, 
                            FIADM.CNPJ     AS CNPJFIIADMIN, 
                            FIADM.SITUACAO AS SITUACAOFIIADMIN
                        FROM TBFII_FUNDOIMOB FI
                            LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
                            LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
                        WHERE FI.RAZAOSOCIAL = :RAZAOSOCIAL 
                """
        params = {'RAZAOSOCIAL': razao_social}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_cnpj(cls, db: _orm.Session, cnpj: str = None):
        query = """ SELECT 	FI.ID, 
                            FI.NOME, 
                            FI.RAZAOSOCIAL, 
                            FI.CNPJ, 
                            FI.CODIGO, 
                            FI.CODISIN, 
                            FI.SITUACAO, 
                            FITP.ID        AS IDFIITIPO, 
                            FITP.DESCRICAO AS DESCRICAOFIITIPO, 
                            FITP.SITUACAO  AS SITUACAOFIITIPO, 
                            FIADM.ID       AS IDFIIADMIN, 
                            FIADM.NOME     AS NOMEFIIADMIN, 
                            FIADM.CNPJ     AS CNPJFIIADMIN, 
                            FIADM.SITUACAO AS SITUACAOFIIADMIN
                        FROM TBFII_FUNDOIMOB FI
                            LEFT JOIN TBFII_FUNDOIMOB_TIPO  FITP  ON ( FITP.ID  = FI.IDFIITIPO  )
                            LEFT JOIN TBFII_FUNDOIMOB_ADMIN FIADM ON ( FIADM.ID = FI.IDFIIADMIN )
                        WHERE FI.CNPJ = :CNPJ 
                """
        params = {'CNPJ': cnpj}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome(cls, db: _orm.Session):
        query = """ SSELECT FI.ID, FI.NOME FROM TBFII_FUNDOIMOB FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.NOME """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_codigo(cls, db: _orm.Session):
        query = """ SELECT FI.ID, FI.CODIGO FROM TBFII_FUNDOIMOB FI WHERE FI.SITUACAO IN ( 'A' ,'E') ORDER BY FI.CODIGO """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_codigos_proventos(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT F.ID AS ID, F.CODIGO AS CODIGO, 'FII' AS TIPO		
                    FROM TBFII_FUNDOIMOB F
                    WHERE F.SITUACAO IN ('A','E') AND EXISTS( SELECT 1 FROM TBFII_PROVENTO P WHERE P.IDFUNDO   = F.ID AND P.IDUSUARIO = :IDUSUARIO
                """
        if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO "
        if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
        query += " ) "
        if codigo: query += " AND F.CODIGO = :CODIGO "
        query += " ORDER BY F.CODIGO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_pendentes_situacao(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT F.CODIGO, F.ID FROM TBFII_FUNDOIMOB F WHERE EXISTS( SELECT 1 FROM TBFII_LANCAMENTO FL WHERE FL.IDFUNDO = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.SITUACAO = 'P' ) """
        if codigo: query += " AND F.CODIGO = :CODIGO "
        query += " ORDER BY F.CODIGO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        try:
            return db.execute(query, params).fetchall()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_irpf(cls, db: _orm.Session, id_usuario: int = None, dt_fim: str = None):
        query = """ SELECT F.ID, F.CODIGO, F.CNPJ, F.RAZAOSOCIAL FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBFII_LANCAMENTO FL WHERE FL.IDFUNDO = F.ID AND FL.IDUSUARIO = :IDUSUARIO AND FL.DATA <= :DATAFIM ) ORDER BY F.CODIGO """
        params = {'IDUSUARIO': id_usuario, 'DATAFIM': dt_fim}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_codigos_comprados(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT F.ID, F.CODIGO FROM TBFII_FUNDOIMOB F WHERE F.SITUACAO IN ( 'A' ,'E') AND EXISTS( SELECT 1 FROM TBFII_LANCAMENTO FL WHERE FL.IDFUNDO = F.ID AND FL.IDUSUARIO = :IDUSUARIO ) """
        if codigo: query += " AND F.CODIGO = :CODIGO "
        query += " ORDER BY F.CODIGO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: FiiFundoImobModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: FiiFundoImobModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
