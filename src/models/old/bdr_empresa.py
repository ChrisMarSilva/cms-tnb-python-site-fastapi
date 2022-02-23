# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro


class BDREmpresa(db.Model):

    __tablename__ = "TBBDR_EMPRESA"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_setor = db.Column('IDSETOR', db.Integer, nullable=True, index=True)
    id_subsetor = db.Column('IDSUBSETOR', db.Integer, nullable=True, index=True)
    id_segmento = db.Column('IDSEGMENTO', db.Integer, nullable=True, index=True)
    nome = db.Column('NOME', db.String(100), nullable=False, index=True)
    razao_social = db.Column('RAZAOSOCIAL', db.String(255), nullable=False, index=True)
    cnpj = db.Column('CNPJ', db.String(18), nullable=True)
    atividade = db.Column('ATIVIDADE', db.String(255), nullable=True)
    cod_cvm = db.Column('CODCVM', db.String(50), nullable=True)
    sit_cvm = db.Column('SITCVM', db.String(255), nullable=True)
    codigo = db.Column('CODIGO', db.String(10), nullable=False, index=True)
    codigo_isin = db.Column('CODISIN', db.String(50), nullable=True)
    tipo = db.Column('TIPO', db.String(100), nullable=False, index=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_setor: int = None, id_subsetor: int = None, id_segmento: int = None, nome: str = None, razao_social: str = None, cnpj: str = None, atividade: str = None, cod_cvm: str = None, sit_cvm: str = None, codigo: str = None, codigo_isin: str = None, tipo: str = None, situacao: str = None):
        self.id = id
        self.id_setor = id_setor
        self.id_subsetor = id_subsetor
        self.id_segmento = id_segmento
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.atividade = atividade
        self.cod_cvm = cod_cvm
        self.sit_cvm = sit_cvm
        self.codigo = codigo
        self.codigo_isin = codigo_isin
        self.tipo = tipo
        self.situacao = situacao

    @classmethod
    def get_all(cls):
        try:
            return cls.query.order_by(cls.nome).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_id(cls, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_codigo(cls, codigo: str):
        try:
            return cls.query.filter_by(codigo=codigo).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_lista_razao_social(cls):
        try:
            return cls.query.filter(cls.situacao == 'A').order_by(cls.razao_social).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_all_codigos(cls):
        try:
            return cls.query.filter(cls.situacao == 'A').order_by(cls.codigo).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls):
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
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos_completo(cls, id_usuario: int = None, setor: str = None, subsetor: str = None, segmento: str = None, codigo: str = None, tipo: str = None, situacao_empresa: str = None):
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
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id: int = None):
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
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_codigo(cls, codigo: str = None):
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
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_nome(cls, nome: str = None):
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
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_razao_social(cls, razao_social: str = None):
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
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_cnpj(cls, cnpj: str = None):
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
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_lista_razao_social(cls):
        query = """ SELECT E.ID, E.RAZAOSOCIAL FROM TBBDR_EMPRESA E WHERE E.SITUACAO = 'A' ORDER BY E.RAZAOSOCIAL """
        params = {}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos_codigos_comprados(cls, id_usuario: int, codigo: str = None):
        query = """ SELECT A.ID, A.CODIGO FROM TBBDR_EMPRESA A WHERE A.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO O WHERE O.IDBDR = A.ID AND O.IDUSUARIO = :IDUSUARIO ) """
        if codigo: query += " AND A.CODIGO = :CODIGO "
        query += " ORDER BY A.CODIGO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo

        try:
            try:
                return db.session.execute(query, params)
            except Exception as e:
                db.session.rollback()
                db.session.close()
                return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos_codigos_proventos(cls, id_usuario: int, codigo: str = None, dt_ini: str = None, dt_fim: str = None):
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
                return db.session.execute(query, params)
            except Exception as e:
                db.session.rollback()
                db.session.close()
                return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_pendentes_situacao(cls, id_usuario: int = None, codigo: str = None):
        query = """ SELECT A.CODIGO, A.ID FROM TBBDR_EMPRESA A WHERE EXISTS( SELECT 1 FROM TBBDR_LANCAMENTO O WHERE O.IDBDR = A.ID AND O.IDUSUARIO = :IDUSUARIO AND O.SITUACAO = 'P' ) """
        if codigo:query += " AND A.CODIGO = :CODIGO "
        query += " ORDER BY A.CODIGO "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo:params['CODIGO'] = codigo

        try:
            try:
                return db.session.execute(query, params).fetchall()
            except Exception as e:
                db.session.rollback()
                db.session.close()
                return db.session.execute(query, params).fetchall()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_lista_irpf(cls, id_usuario: int = None, dt_fim: str = None):
        query = """ SELECT E.ID, E.CODIGO, E.CNPJ, E.RAZAOSOCIAL FROM TBBDR_EMPRESA E WHERE E.SITUACAO = 'A' AND EXISTS( SELECT 1 FROM TBBDR_OPERACAO O WHERE O.IDBDR = E.ID AND O.IDUSUARIO = :IDUSUARIO AND O.DATA <= :DATAFIM ) ORDER BY E.CODIGO """
        params = {'IDUSUARIO': id_usuario, 'DATAFIM': dt_fim}
        try:
            try:
                return db.session.execute(query, params)
            except Exception as e:
                db.session.rollback()
                db.session.close()
                return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def salvar(self, commit: bool = True):
        try:
            db.session.add(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def excluir(self, commit: bool = True):
        try:
            db.session.delete(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':return 'Ativo'
        elif situacao == 'I': return 'Inativo'
        elif situacao == 'E': return 'Encerrado'
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<Empresa {str(self.id)} - {self.nome} - {self.razao_social}>'
