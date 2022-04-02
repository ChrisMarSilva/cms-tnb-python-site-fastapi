# -*- coding: utf-8 -*-
import sys
import os
import sqlalchemy.orm as _orm
from src.models.bdr_empresa import BDREmpresaModel
# from app.models.log_erro import LogErro


class BDREmpresaRepository:

    @classmethod
    async def get_all(cls, db: _orm.Session):
        try:
            return db.query(BDREmpresaModel).order_by(BDREmpresaModel.nome).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(BDREmpresaModel).filter_by(id=id).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_codigo(cls, db: _orm.Session, codigo: str):
        try:
            return db.query(BDREmpresaModel).filter_by(codigo=codigo).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_razao_social(cls, db: _orm.Session):
        try:
            return db.query(BDREmpresaModel).filter(BDREmpresaModel.situacao == 'A').order_by(BDREmpresaModel.razao_social).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_all_codigos(cls, db: _orm.Session):
        try:
            return db.query(BDREmpresaModel).filter(BDREmpresaModel.situacao == 'A').order_by(BDREmpresaModel.codigo).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session):
        query = """ SELECT E.ID, 
                           E.NOME, 
                           E.RAZAOSOCIAL, 
                           E.CNPJ, 
                           E.ATIVIDADE, 
                           E.CODCVM, 
                           E.SITCVM, 
                           E.CODIGO, 
                           E.TIPO, 
                           E.CODISIN, 
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
                    FROM TBBDR_EMPRESA E
                      LEFT JOIN TBBDR_EMPRESA_SETOR    SR ON ( SR.ID = E.IDSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SUBSETOR SS ON ( SS.ID = E.IDSUBSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO )
                    WHERE E.SITUACAO = 'A'
                    ORDER BY E.NOME, E.ID
                """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_completo(cls, db: _orm.Session, id_usuario: int = None, setor: str = None, subsetor: str = None, segmento: str = None, codigo: str = None, tipo: str = None, situacao_empresa: str = None):
        query = """ SELECT E.ID, 
                           E.NOME, 
                           E.RAZAOSOCIAL, 
                           E.CNPJ, 
                           E.ATIVIDADE, 
                           E.CODCVM, 
                           E.SITCVM, 
                           E.CODIGO, 
                           E.TIPO, 
                           E.CODISIN, 
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
                    FROM TBBDR_EMPRESA E
                      LEFT JOIN TBBDR_EMPRESA_SETOR    SR ON ( SR.ID = E.IDSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SUBSETOR SS ON ( SS.ID = E.IDSUBSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO )
                      WHERE 1 = 1
                """

        if setor: query += " AND SR.ID = :IDSETOR "
        if subsetor: query += " AND SS.ID = :IDSUBSETOR "
        if segmento: query += " AND SG.ID = :IDSEGMENTO "
        if codigo: query += " AND E.CODIGO = :CODIGO "
        if situacao_empresa: query += " AND E.SITUACAO = :SITUACAO_EMPRESA "
        if tipo:
            query += " AND EXISTS( SELECT 1 FROM TBBDR_OPERACAO O WHERE O.IDBDR = E.ID AND O.IDUSUARIO = :IDUSUARIO01 AND QUANTACUMULADO > 0 ) "
            query += " AND NOT EXISTS( SELECT 1 FROM TBBDR_OPERACAO O WHERE O.IDBDR = E.ID AND O.IDUSUARIO = :IDUSUARIO02 AND QUANTACUMULADO = 0 ) "

        query += " ORDER BY E.NOME, E.ID "

        params = {}
        if setor: params['IDSETOR'] = codigo
        if subsetor: params['IDSUBSETOR'] = subsetor
        if segmento: params['IDSEGMENTO'] = segmento
        if codigo: params['CODIGO'] = codigo
        if situacao_empresa: params['SITUACAO_EMPRESA'] = situacao_empresa
        if tipo:
            params['IDUSUARIO01'] = id_usuario
            params['IDUSUARIO02'] = id_usuario

        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id: int = None):
        query = """ SELECT E.ID, 
                           E.NOME, 
                           E.RAZAOSOCIAL, 
                           E.CNPJ, 
                           E.ATIVIDADE, 
                           E.CODCVM, 
                           E.SITCVM, 
                           E.CODIGO, 
                           E.TIPO, 
                           E.CODISIN, 
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
                    FROM TBBDR_EMPRESA E
                      LEFT JOIN TBBDR_EMPRESA_SETOR    SR ON ( SR.ID = E.IDSETOR    )
                      LEFT JOIN TBBDR_EMPRESA_SUBSETOR SS ON ( SS.ID = E.IDSUBSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO )
                    WHERE E.ID = :ID 
                """
        params = {'ID': id}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_codigo(cls, db: _orm.Session, codigo: str = None):
        query = """ SELECT E.ID, 
                           E.NOME, 
                           E.RAZAOSOCIAL, 
                           E.CNPJ, 
                           E.ATIVIDADE, 
                           E.CODCVM, 
                           E.SITCVM, 
                           E.CODIGO, 
                           E.TIPO, 
                           E.CODISIN, 
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
                    FROM TBBDR_EMPRESA E
                      LEFT JOIN TBBDR_EMPRESA_SETOR    SR ON ( SR.ID = E.IDSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SUBSETOR SS ON ( SS.ID = E.IDSUBSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO )
                    WHERE E.CODIGO = :CODIGO 
                """
        params = {'CODIGO': codigo}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_nome(cls, db: _orm.Session, nome: str = None):
        query = """ SELECT E.ID, 
                           E.NOME,  
                           E.RAZAOSOCIAL, 
                           E.CNPJ, 
                           E.ATIVIDADE, 
                           E.CODCVM, 
                           E.SITCVM, 
                           E.CODIGO, 
                           E.TIPO, 
                           E.CODISIN, 
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
                    FROM TBBDR_EMPRESA E
                      LEFT JOIN TBBDR_EMPRESA_SETOR    SR ON ( SR.ID = E.IDSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SUBSETOR SS ON ( SS.ID = E.IDSUBSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID = E.IDSEGMENTO )
                    WHERE E.NOME = :NOME 
                """
        params = {'NOME': nome}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_razao_social(cls, db: _orm.Session, razao_social: str = None):
        query = """ SELECT E.ID, 
                           E.NOME, 
                           E.RAZAOSOCIAL, 
                           E.CNPJ, 
                           E.ATIVIDADE, 
                           E.CODCVM, 
                           E.SITCVM, 
                           E.CODIGO, 
                           E.TIPO, 
                           E.CODISIN, 
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
                    FROM TBBDR_EMPRESA E
                      LEFT JOIN TBBDR_EMPRESA_SETOR    SR ON ( SR.ID       = E.IDSETOR    )
                      LEFT JOIN TBBDR_EMPRESA_SUBSETOR SS ON ( SS.ID       = E.IDSUBSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID       = E.IDSEGMENTO )
                    WHERE E.RAZAOSOCIAL = :RAZAOSOCIAL 
                """
        params = {'RAZAOSOCIAL': razao_social}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_cnpj(cls, db: _orm.Session, cnpj: str = None):
        query = """ SELECT E.ID, 
                           E.NOME, 
                           E.RAZAOSOCIAL, 
                           E.CNPJ, 
                           E.ATIVIDADE, 
                           E.CODCVM, 
                           E.SITCVM, 
                           E.CODIGO, 
                           E.TIPO, 
                           E.CODISIN, 
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
                    FROM TBBDR_EMPRESA E
                      LEFT JOIN TBBDR_EMPRESA_SETOR    SR ON ( SR.ID       = E.IDSETOR    )
                      LEFT JOIN TBBDR_EMPRESA_SUBSETOR SS ON ( SS.ID       = E.IDSUBSETOR )
                      LEFT JOIN TBBDR_EMPRESA_SEGMENTO SG ON ( SG.ID       = E.IDSEGMENTO )
                    WHERE E.CNPJ = :CNPJ 
                """
        params = {'CNPJ': cnpj}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_razao_social(cls, db: _orm.Session):
        query = """ SELECT E.ID, E.RAZAOSOCIAL FROM TBBDR_EMPRESA E WHERE E.SITUACAO = 'A' ORDER BY E.RAZAOSOCIAL """
        params = {}
        try:
            return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos_codigos_comprados(cls, db: _orm.Session, id_usuario: int, codigo: str = None):
        query = """ SELECT A.ID, A.CODIGO FROM TBBDR_EMPRESA A WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO O WHERE O.IDBDR = A.ID AND O.IDUSUARIO = :IDUSUARIO ) """
        if codigo: query += " AND A.CODIGO = :CODIGO "
        query += " ORDER BY A.CODIGO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo

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
    async def buscar_todos_codigos_proventos(cls, db: _orm.Session, id_usuario: int, codigo: str = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT A.ID AS ID, A.CODIGO AS CODIGO FROM TBBDR_EMPRESA A WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBBDR_PROVENTO P WHERE P.IDBDR = A.ID AND P.IDUSUARIO = :IDUSUARIO """
        if dt_ini: query += " AND P.DATAPAGTO >= :DATAINICIO "
        if dt_fim: query += " AND P.DATAPAGTO <= :DATAFIM "
        query += " ) "
        if codigo: query += " AND A.CODIGO = :CODIGO "
        query += " ORDER BY A.CODIGO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim
        if codigo:params['CODIGO'] = codigo

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
    async def buscar_pendentes_situacao(cls, db: _orm.Session, id_usuario: int = None, codigo: str = None):
        query = """ SELECT A.CODIGO, A.ID FROM TBBDR_EMPRESA A WHERE EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO O WHERE O.IDBDR = A.ID AND O.IDUSUARIO = :IDUSUARIO AND O.SITUACAO = 'P' ) """
        if codigo:query += " AND A.CODIGO = :CODIGO "
        query += " ORDER BY A.CODIGO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo:params['CODIGO'] = codigo

        try:
            try:
                return db.execute(query, params).fetchall()
            except Exception as e:
                db.rollback()
                db.close()
                return db.execute(query, params).fetchall()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_irpf(cls, db: _orm.Session, id_usuario: int = None, dt_fim: str = None):
        query = """ SELECT E.ID, E.CODIGO, E.CNPJ, E.RAZAOSOCIAL FROM TBBDR_EMPRESA E WHERE E.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBBDR_OPERACAO O WHERE O.IDBDR = E.ID AND O.IDUSUARIO = :IDUSUARIO AND O.DATA <= :DATAFIM ) ORDER BY E.CODIGO """
        params = {'IDUSUARIO': id_usuario, 'DATAFIM': dt_fim}
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
    async def salvar(cls, db: _orm.Session, row: BDREmpresaModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: BDREmpresaModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
