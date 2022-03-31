# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.acao_empresa import ACAOEmpresaModel
# # from app.models.log_erro import LogErro


class ACAOEmpresaRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(ACAOEmpresaModel).order_by(ACAOEmpresaModel.nome).all()
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(ACAOEmpresaModel).filter(id=id).first()
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_razao_social(cls, db: _orm.Session):
        try:
            return db.query(ACAOEmpresaModel).filter(ACAOEmpresaModel.situacao == 'A').order_by(ACAOEmpresaModel.razao_social).all()
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT E.ID,
                           E.NOME,
                           E.NOMRESUMIDO,
                           E.RAZAOSOCIAL,
                           E.CNPJ,
                           E.ATIVIDADE,
                           E.CODCVM,
                           E.SITCVM,
                           E.IDSETOR,
                           SR.DESCRICAO AS DESCRICAOSETOR,
                           SR.SITUACAO  AS SITUACAOSETOR,
                           E.IDSUBSETOR,
                           SS.DESCRICAO AS DESCRICAOSUBSETOR,
                           SS.SITUACAO  AS SITUACAOSUBSETOR,
                           E.IDSEGMENTO,
                           SG.DESCRICAO AS DESCRICAOSEGMENTO,
                           SG.SITUACAO  AS SITUACAOSEGMENTO,
                           E.SITUACAO
                    FROM TBEMPRESA E
                      LEFT JOIN TBEMPRESA_SETOR    SR ON ( SR.ID       = E.IDSETOR    )
                      LEFT JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID       = E.IDSUBSETOR )
                      LEFT JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID       = E.IDSEGMENTO )
                    WHERE E.SITUACAO = 'A'
                    ORDER BY E.NOME, E.ID
                """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_completo(cls, db: _orm.Session, id_usuario: int = None, setor: str = None, subsetor: str = None, segmento: str = None, codigo: str = None, tipo: str = None, situacao_empresa: str = None, situacao_ativo: str = None):
        query = """ SELECT E.ID,
                           E.NOME,
                           E.NOMRESUMIDO,
                           E.RAZAOSOCIAL,
                           E.CNPJ,
                           E.ATIVIDADE,
                           E.CODCVM,
                           E.SITCVM,
                           A.ID AS IDATIVO,
                           A.CODIGO  AS CODIGOATIVO,
                           E.IDSETOR,
                           SR.DESCRICAO AS DESCRICAOSETOR,
                           SR.SITUACAO  AS SITUACAOSETOR,
                           E.IDSUBSETOR,
                           SS.DESCRICAO AS DESCRICAOSUBSETOR,
                           SS.SITUACAO  AS SITUACAOSUBSETOR,
                           E.IDSEGMENTO,
                           SG.DESCRICAO AS DESCRICAOSEGMENTO,
                           SG.SITUACAO  AS SITUACAOSEGMENTO,
                           E.SITUACAO
                    FROM TBEMPRESA E
                      LEFT JOIN TBEMPRESA_ATIVO    A  ON ( A.IDEMPRESA = E.ID         )
                      LEFT JOIN TBEMPRESA_SETOR    SR ON ( SR.ID       = E.IDSETOR    )
                      LEFT JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID       = E.IDSUBSETOR )
                      LEFT JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID       = E.IDSEGMENTO )
                      WHERE 1 = 1
                """

        if setor: query += " AND SR.ID = :IDSETOR "
        if subsetor: query += " AND SS.ID = :IDSUBSETOR "
        if segmento: query += " AND SG.ID = :IDSEGMENTO "
        if codigo: query += " AND A.CODIGO = :CODIGO "
        if situacao_empresa: query += " AND E.SITUACAO = :SITUACAO_EMPRESA "
        if situacao_ativo: query += " AND A.SITUACAO = :SITUACAO_ATIVO "
        if tipo:
            query += " AND EXISTS( SELECT 1 FROM TBOPERACAO O WHERE O.IDATIVO = A.ID AND O.IDUSUARIO = :IDUSUARIO01 AND QUANTACUMULADO > 0 ) "
            query += " AND NOT EXISTS( SELECT 1 FROM TBOPERACAO O WHERE O.IDATIVO = A.ID AND O.IDUSUARIO = :IDUSUARIO02 AND QUANTACUMULADO = 0 ) "

        query += " ORDER BY E.NOME, E.ID "

        params = {}
        if setor: params['IDSETOR'] = codigo
        if subsetor: params['IDSUBSETOR'] = subsetor
        if segmento: params['IDSEGMENTO'] = segmento
        if codigo: params['CODIGO'] = codigo
        if situacao_empresa: params['SITUACAO_EMPRESA'] = situacao_empresa
        if situacao_ativo: params['SITUACAO_ATIVO'] = situacao_ativo
        if tipo:
            params['IDUSUARIO01'] = id_usuario
            params['IDUSUARIO02'] = id_usuario

        try:
            return db.execute(query, params)
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int = None):
        query = """ SELECT E.ID,
                           E.NOME,
                           E.NOMRESUMIDO,
                           E.RAZAOSOCIAL,
                           E.CNPJ,
                           E.ATIVIDADE,
                           E.CODCVM,
                           E.SITCVM,
                           E.IDSETOR,
                           SR.DESCRICAO AS DESCRICAOSETOR,
                           SR.SITUACAO  AS SITUACAOSETOR,
                           E.IDSUBSETOR,
                           SS.DESCRICAO AS DESCRICAOSUBSETOR,
                           SS.SITUACAO  AS SITUACAOSUBSETOR,
                           E.IDSEGMENTO,
                           SG.DESCRICAO AS DESCRICAOSEGMENTO,
                           SG.SITUACAO  AS SITUACAOSEGMENTO,
                           E.SITUACAO
                    FROM TBEMPRESA E
                      LEFT JOIN TBEMPRESA_SETOR    SR ON ( SR.ID       = E.IDSETOR    )
                      LEFT JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID       = E.IDSUBSETOR )
                      LEFT JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID       = E.IDSEGMENTO )
                    WHERE E.ID = :ID
                """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, codigo: str = None):
        query = """ SELECT E.ID,
                           E.NOME,
                           E.NOMRESUMIDO,
                           E.RAZAOSOCIAL,
                           E.CNPJ,
                           E.ATIVIDADE,
                           E.CODCVM,
                           E.SITCVM,
                           E.SLUG,
                           E.SITE,
                           E.TIPO_MERCADO,
                           A.ID      AS IDATIVO,
                           A.CODIGO   AS CODIGOATIVO,
                           A.CODISIN   AS CODISINATIVO,
                           A.SITUACAO AS SITUACAOATIVO,
                           E.IDSETOR,
                           SR.DESCRICAO AS DESCRICAOSETOR,
                           SR.SITUACAO  AS SITUACAOSETOR,
                           E.IDSUBSETOR,
                           SS.DESCRICAO AS DESCRICAOSUBSETOR,
                           SS.SITUACAO  AS SITUACAOSUBSETOR,
                           E.IDSEGMENTO,
                           SG.DESCRICAO AS DESCRICAOSEGMENTO,
                           SG.SITUACAO  AS SITUACAOSEGMENTO,
                           E.SITUACAO
                    FROM TBEMPRESA E
                      LEFT JOIN TBEMPRESA_ATIVO    A  ON ( A.IDEMPRESA = E.ID         )
                      LEFT JOIN TBEMPRESA_SETOR    SR ON ( SR.ID       = E.IDSETOR    )
                      LEFT JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID       = E.IDSUBSETOR )
                      LEFT JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID       = E.IDSEGMENTO )
                    WHERE A.CODIGO = :CODIGO
                """
        params = {'CODIGO': codigo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_nome(cls, db: _orm.Session, nome: str = None):
        query = """ SELECT E.ID,
                           E.NOME,
                           E.NOMRESUMIDO,
                           E.RAZAOSOCIAL,
                           E.CNPJ,
                           E.ATIVIDADE,
                           E.CODCVM,
                           E.SITCVM,
                           E.IDSETOR,
                           SR.DESCRICAO AS DESCRICAOSETOR,
                           SR.SITUACAO  AS SITUACAOSETOR,
                           E.IDSUBSETOR,
                           SS.DESCRICAO AS DESCRICAOSUBSETOR,
                           SS.SITUACAO  AS SITUACAOSUBSETOR,
                           E.IDSEGMENTO,
                           SG.DESCRICAO AS DESCRICAOSEGMENTO,
                           SG.SITUACAO  AS SITUACAOSEGMENTO,
                           E.SITUACAO
                    FROM TBEMPRESA E
                      LEFT JOIN TBEMPRESA_SETOR    SR ON ( SR.ID       = E.IDSETOR    )
                      LEFT JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID       = E.IDSUBSETOR )
                      LEFT JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID       = E.IDSEGMENTO )
                    WHERE E.NOME = :NOME
                """
        params = {'NOME': nome}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_razao_social(cls, db: _orm.Session, razao_social: str = None):
        query = """ SELECT E.ID,
                           E.NOME,
                           E.NOMRESUMIDO,
                           E.RAZAOSOCIAL,
                           E.CNPJ,
                           E.ATIVIDADE,
                           E.CODCVM,
                           E.SITCVM,
                           E.IDSETOR,
                           SR.DESCRICAO AS DESCRICAOSETOR,
                           SR.SITUACAO  AS SITUACAOSETOR,
                           E.IDSUBSETOR,
                           SS.DESCRICAO AS DESCRICAOSUBSETOR,
                           SS.SITUACAO  AS SITUACAOSUBSETOR,
                           E.IDSEGMENTO,
                           SG.DESCRICAO AS DESCRICAOSEGMENTO,
                           SG.SITUACAO  AS SITUACAOSEGMENTO,
                           E.SITUACAO
                    FROM TBEMPRESA E
                      LEFT JOIN TBEMPRESA_SETOR    SR ON ( SR.ID       = E.IDSETOR    )
                      LEFT JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID       = E.IDSUBSETOR )
                      LEFT JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID       = E.IDSEGMENTO )
                    WHERE E.RAZAOSOCIAL = :RAZAOSOCIAL
                """
        params = {'RAZAOSOCIAL': razao_social}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_cnpj(cls, db: _orm.Session, cnpj: str = None):
        query = """ SELECT E.ID,
                           E.NOME,
                           E.NOMRESUMIDO,
                           E.RAZAOSOCIAL,
                           E.CNPJ,
                           E.ATIVIDADE,
                           E.CODCVM,
                           E.SITCVM,
                           E.IDSETOR,
                           SR.DESCRICAO AS DESCRICAOSETOR,
                           SR.SITUACAO  AS SITUACAOSETOR,
                           E.IDSUBSETOR,
                           SS.DESCRICAO AS DESCRICAOSUBSETOR,
                           SS.SITUACAO  AS SITUACAOSUBSETOR,
                           E.IDSEGMENTO,
                           SG.DESCRICAO AS DESCRICAOSEGMENTO,
                           SG.SITUACAO  AS SITUACAOSEGMENTO,
                           E.SITUACAO
                    FROM TBEMPRESA E
                      LEFT JOIN TBEMPRESA_SETOR    SR ON ( SR.ID       = E.IDSETOR    )
                      LEFT JOIN TBEMPRESA_SUBSETOR SS ON ( SS.ID       = E.IDSUBSETOR )
                      LEFT JOIN TBEMPRESA_SEGMENTO SG ON ( SG.ID       = E.IDSEGMENTO )
                    WHERE E.CNPJ = :CNPJ
                """
        params = {'CNPJ': cnpj}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_razao_social(cls, db: _orm.Session):
        query = """ SELECT E.ID, E.RAZAOSOCIAL FROM TBEMPRESA E WHERE E.SITUACAO = 'A' ORDER BY E.RAZAOSOCIAL """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: ACAOEmpresaModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: ACAOEmpresaModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            # LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

