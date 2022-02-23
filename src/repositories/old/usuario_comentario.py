# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioComentario(db.Model):

    __tablename__ = "TBCOMENTARIO"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_pai = db.Column('IDPAI', db.Integer, db.ForeignKey('TBCOMENTARIO.ID'), nullable=True, index=True)
    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
    texto = db.Column('TEXTO', db.Text(), nullable=False)
    data_hora = db.Column('DATAHORA', db.String(14), nullable=False, index=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_pai: int = None, id_usuario: int = None, tipo: str = None, texto: str = None,
                 data_hora: str = None, situacao: str = None):
        self.id = id
        self.id_pai = id_pai
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.texto = texto
        self.data_hora = data_hora
        self.situacao = situacao

    @classmethod
    def get_all(cls):
        try:
            return cls.query.order_by(cls.id).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_all_by_usuario(cls, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).order_by(cls.id).all()
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
    def get_by_id_and_id_usuario(cls, id_usuario: int, id: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_id_pai(cls, id_usuario: int, id_pai: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, id_pai=id_pai).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_qtde_total_coment_princ(cls):
        try:
            return cls.query.filter_by(tipo='A', situacao='A').count()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int):
        query = """ SELECT C.ID, C.IDPAI, C.IDUSUARIO, C.TIPO, C.TEXTO, C.DATAHORA, C.SITUACAO FROM TBCOMENTARIO C WHERE C.IDUSUARIO = :IDUSUARIO ORDER BY C.ID """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id_usuario: int, id: int = None):
        query = """ SELECT C.ID, C.IDPAI, C.IDUSUARIO, C.TIPO, C.TEXTO, C.DATAHORA, C.SITUACAO FROM TBCOMENTARIO C WHERE C.ID = :ID AND C.IDUSUARIO = :IDUSUARIO ORDER BY C.ID """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_qtde_total_coment_princ(cls):
        query = "SELECT COUNT(1) AS QTDE FROM TBCOMENTARIO C WHERE C.TIPO = 'A' AND C.SITUACAO = 'A'"
        params = {}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_coment_grid_princ(cls, reg_inicio: int = 1, qtde_pagina: int = 100):
        query = """ SELECT C.IDUSUARIO AS IDUSUARIO, 
                           U.NOME      AS NOMEUSUARIO, 
                           U.FOTO      AS FOTOUSUARIO, 
                           C.ID        AS IDCOMENTARIO, 
                           C.TEXTO     AS TXTCOMENTARIO,  
                           C.DATAHORA  AS DTHRCOMENTARIO
                    FROM TBCOMENTARIO C
                      INNER JOIN TBUSUARIO U ON ( U.ID = C.IDUSUARIO )
                    WHERE C.TIPO     = 'A'
                      AND C.SITUACAO = 'A'
                    ORDER BY C.DATAHORA DESC, C.ID
                    LIMIT """ + str(reg_inicio) + """, """ + str(qtde_pagina) + """
                """
        params = {}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_coment_grid_resp(cls, id_comentario: int):
        query = """ SELECT C.IDUSUARIO AS IDUSUARIO, 
                           U.NOME      AS NOMEUSUARIO, 
                           U.FOTO      AS FOTOUSUARIO, 
                           C.ID        AS IDCOMENTARIO, 
                           C.TEXTO     AS TXTCOMENTARIO,  
                           C.DATAHORA  AS DTHRCOMENTARIO
                    FROM TBCOMENTARIO C
                      INNER JOIN TBUSUARIO U ON ( U.ID = C.IDUSUARIO )
                    WHERE C.IDPAI    = :IDPAI
                      AND C.TIPO     = 'B'
                      AND C.SITUACAO = 'A'
                    ORDER BY C.DATAHORA ASC, C.ID
                """
        params = {'IDPAI': id_comentario}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_lista_user_alerta(cls, id_comentario: int):
        query = """ SELECT CA.IDUSUARIODSST AS IDUSUARIO, 
                           U.NOME       AS NOMEUSUARIO,  
                           U.FOTO       AS FOTOUSUARIO, 
                           U.EMAIL      AS EMAILUSUARIO
                    FROM TBCOMENTARIO_ALERTA CA
                        INNER JOIN TBUSUARIO U ON ( U.ID = CA.IDUSUARIODSST )
                    WHERE CA.IDCOMENTARIO = :IDCOMENTARIO
                   AND CA.TIPO IN ('C','R')
                   AND CA.SITUACAO = 'L'
                """
        params = {'IDCOMENTARIO': id_comentario}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_lista_user_reacao(cls, id_comentario: int, tipo: str):
        query = """ SELECT CR.IDUSUARIO AS IDUSUARIO, 
                           U.NOME       AS NOMEUSUARIO,  
                           U.FOTO       AS FOTOUSUARIO, 
                           U.EMAIL      AS EMAILUSUARIO
                    FROM TBCOMENTARIO_REACAO CR
                        INNER JOIN TBUSUARIO U ON ( U.ID = CR.IDUSUARIO )
                    WHERE CR.IDCOMENTARIO = :IDCOMENTARIO
                      AND CR.TIPO         = :TIPO
                """
        params = {'IDCOMENTARIO': id_comentario, 'TIPO': tipo}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_respostas(cls, id_comentario: int, commit: bool = True):
        try:
            query = """DELETE FROM TBCOMENTARIO WHERE IDPAI = :IDPAI AND TIPO = 'B'"""
            params = {'IDPAI': id_comentario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_comentario(cls, id_comentario: int, commit: bool = True):
        try:
            query = " DELETE FROM TBCOMENTARIO WHERE ID = :ID "
            params = {'ID': id_comentario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBCOMENTARIO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
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

    def data_hora_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_hora, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def tipo_descr(self) -> str:
        if self.tipo == 'A':
            return 'Principal'
        elif self.tipo == 'B':
            return 'Resposta'
        elif self.tipo == 'C':
            return 'Réplica'
        else:
            return 'Desconhecido'

    def situacao_descr(self) -> str:
        if self.situacao == 'A':
            return 'Ativa'
        elif self.situacao == 'D':
            return 'Denunciado'
        elif self.situacao == 'E':
            return 'Excluído'
        elif self.situacao == 'I':
            return 'Inativa'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioComentario {str(self.id)}>'
