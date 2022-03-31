# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
# from app.models.log_erro import LogErro


class ACAOEmpresaFinanceiroAgendaRepository:

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None, divulgacao: str = None, tipo: str = None):
        try:

            query = """ SELECT AG.ID, AG.IDEMPRESA, AG.NOME, A.CODIGO, AG.DIVULGACAO, AG.HORARIO
                        FROM TBEMPRESA_FINAN_AGENDA AG
                          JOIN TBEMPRESA_ATIVO A ON ( A.CODIGO = AG.CODIGO )
                        WHERE 1 = 1
                    """

            if divulgacao: query += " AND AG.DIVULGACAO >= :DIVULGACAO "
            if codigo: query += " AND AG.CODIGO = :CODIGO "

            if id_usuario and tipo == 'P':  # P-Portfolio
                query += " AND EXISTS( SELECT 1 FROM TBCARTEIRA C JOIN TBCARTEIRA_ATIVO CA ON ( CA.IDCARTEIRA = C.ID ) WHERE C.IDUSUARIO = :IDUSUARIO_P AND C.SITUACAO = 'A' AND CA.IDATIVO = A.ID AND CA.SITUACAO = 'A' ) "

            if id_usuario and tipo == 'R': # R-Radar
                query += """ AND EXISTS( SELECT 1 FROM TBUSUARIO_ACOMP_GRUPO C JOIN TBUSUARIO_ACOMP_ATIVO CA ON ( CA.IDGRUPO = C.ID ) WHERE C.IDUSUARIO = :IDUSUARIO_R1 AND C.SITUACAO = 'A' AND CA.IDATIVO = A.ID AND CA.SITUACAO = 'A' )
                             AND NOT EXISTS( SELECT 1 FROM TBCARTEIRA C JOIN TBCARTEIRA_ATIVO CA ON ( CA.IDCARTEIRA = C.ID ) WHERE C.IDUSUARIO = :IDUSUARIO_R2 AND C.SITUACAO = 'A' AND CA.IDATIVO = A.ID AND CA.SITUACAO = 'A' ) 
                         """

            query += " ORDER BY AG.DIVULGACAO "

            params = {}

            if divulgacao:
                params['DIVULGACAO'] = divulgacao

            if codigo:
                params['CODIGO'] = codigo

            if id_usuario and tipo == 'P':  # P-Portfolio
                params['IDUSUARIO_P'] = id_usuario

            if id_usuario and tipo == 'R': # R-Radar
                params['IDUSUARIO_R1'] = id_usuario
                params['IDUSUARIO_R2'] = id_usuario

            try:
                return db.execute(query, params)
            except Exception as e:
                db.rollback()
                db.close()
                return db.execute(query, params)

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

