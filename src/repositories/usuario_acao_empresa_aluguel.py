# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioACAOEmpresaAluguelRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return cls.query.all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_by_usuario(cls, db: _orm.Session, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).order_by(cls, db: _orm.data, cls.id_ativo).all()
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
    async def get_by_usuario(cls, db: _orm.Session, id_usuario: int, id: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    # from app.models.usuario_empresa_aluguel import UsuarioEmpresaAluguel
    # return cls.query\
    #     .join(UsuarioEmpresaAluguel, UsuarioEmpresaAluguel.id_ativo == cls.id)\
    #     .filter(cls, db: _orm.situacao == 'A', UsuarioEmpresaAluguel.id_usuario == id_usuario)\
    #     .order_by(cls, db: _orm.codigo)\
    #     .all()
    # from app.models.usuario_empresa_lancamento import UsuarioEmpresaLancamento
    # return cls.query\
    #     .join(UsuarioEmpresaLancamento, UsuarioEmpresaLancamento.id_ativo == cls.id)\
    #     .filter(EmpresaAtivo.situacao == 'A', UsuarioEmpresaLancamento.id_usuario == id_usuario)\
    #     .order_by(cls, db: _orm.codigo)\
    #     .all()
    # from app.models.empresa_ativo import EmpresaAtivo
    # filters = []
    # filters.append(cls, db: _orm.id_usuario == id_usuario)
    # if cod_ativo: filters.append(EmpresaAtivo.codigo == cod_ativo)
    # if dt_ini: filters.append(cls, db: _orm.data >= dt_ini)
    # if dt_fim: filters.append(cls, db: _orm.data <= dt_fim)
    # return cls.query\
    #     .join(EmpresaAtivo, EmpresaAtivo.id == cls.id_ativo) \
    #     .filter(*filters) \
    #     .add_columns(EmpresaAtivo.codigo) \
    #     .order_by(cls, db: _orm.data, cls.id_ativo)\
    #     .all()

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int, codigo: str = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT AL.ID, AL.IDATIVO  AS IDATIVO, A.CODIGO AS CODIGOATIVO, AL.DATA, AL.VLRBRUTO, AL.VLRIR, AL.VLRLIQUIDO, AL.SITUACAO FROM TBALUGUEL_ATIVO AL INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = AL.IDATIVO ) WHERE AL.IDUSUARIO = :IDUSUARIO """
        if codigo: query += " AND A.CODIGO = :CODIGO "
        if dt_ini: query += " AND AL.DATA >= :DATAINICIO "
        if dt_fim: query += " AND AL.DATA <= :DATAFIM "
        query += " ORDER BY AL.DATA, AL.IDATIVO "
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
    async def buscar_por_id(cls, db: _orm.Session, id: int, id_usuario: int):
        query = """ SELECT AL.ID, 
                           AL.IDATIVO  AS IDATIVO, 
                           A.CODIGO    AS CODIGOATIVO, 
                           AL.DATA, 
                           AL.VLRBRUTO, 
                           AL.VLRIR, 
                           AL.VLRLIQUIDO, 
                           AL.SITUACAO 
                    FROM TBALUGUEL_ATIVO AL
                        INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = AL.IDATIVO )
                    WHERE AL.ID        = :ID
                      AND AL.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_dados_grid_irpf(cls, db: _orm.Session, id_usuario: int, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT MAX(A.CODIGO)      AS CODIGO,
                           MAX(E.CNPJ)        AS CNPJ,
                           MAX(E.RAZAOSOCIAL) AS RAZAOSOCIAL,
                           SUM(AL.VLRLIQUIDO) AS TOTVLR
                    FROM TBALUGUEL_ATIVO AL
                      INNER JOIN TBEMPRESA_ATIVO A ON ( A.ID = AL.IDATIVO  )
                      INNER JOIN TBEMPRESA       E ON ( E.ID = A.IDEMPRESA )
                    WHERE AL.IDUSUARIO = :IDUSUARIO
                      AND AL.DATA     >= :DATAINICIO
                      AND AL.DATA     <= :DATAFIM
                    GROUP BY AL.IDATIVO
                    ORDER BY E.RAZAOSOCIAL
                """
        params = {'IDUSUARIO': id_usuario, 'DATAINICIO': dt_ini, 'DATAFIM': dt_fim}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_vlr_total(cls, db: _orm.Session, id_usuario: int, id_ativo: int, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT IFNULL(SUM(A.VLRLIQUIDO), 0.00 ) AS TOTAL FROM TBALUGUEL_ATIVO A WHERE A.IDUSUARIO = :IDUSUARIO AND A.IDATIVO = :IDATIVO """
        if dt_ini: query += " AND A.DATA >= :DATAINICIO "
        if dt_fim: query += " AND A.DATA <= :DATAFIM "

        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDATIVO'] = id_ativo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim

        try:
            rows = db.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBALUGUEL_ATIVO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, commit: bool = True):
        try:
            db.add(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, commit: bool = True):
        try:
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
