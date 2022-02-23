# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str, pegar_data_hora_atual


class UsuarioComentarioAlerta(db.Model):

    __tablename__ = "TBCOMENTARIO_ALERTA"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_comentario = db.Column('IDCOMENTARIO', db.Integer, db.ForeignKey('TBCOMENTARIO.ID'), nullable=False, index=True)
    id_usuario_orig = db.Column('IDUSUARIOORIG', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    id_usuario_dest = db.Column('IDUSUARIODSST', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    data_hora = db.Column('DTHR', db.String(14), nullable=False, index=True)
    tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_comentario: int = None, id_usuario_orig: int = None,
                 id_usuario_dest: int = None, data_hora: str = None, tipo: str = None, situacao: str = None):
        self.id = id
        self.id_comentario = id_comentario
        self.id_usuario_orig = id_usuario_orig
        self.id_usuario_dest = id_usuario_dest
        self.data_hora = data_hora
        self.tipo = tipo
        self.situacao = situacao

    @classmethod
    def get_all(cls):
        try:
            return cls.query.all()
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
    def buscar_todos(cls, id_usuario: int = None, tipo: str = None, situacao: str = None):

        query = """ SELECT  ALRT.ID,
                            ALRT.IDCOMENTARIO,
                            ALRT.IDUSUARIOORIG AS IDUSUARIOORIGEM,
                            UO.NOME            AS NMUSUARIOORIGEM,
                            UO.FOTO            AS FTUSUARIOORIGEM,
                            ALRT.IDUSUARIODSST AS IDUSUARIODESTINO,
                            UD.NOME            AS NMUSUARIODESTINO,
                            ALRT.DTHR          AS DTHRALERTA,
                            ALRT.TIPO          AS TIPOALERTA,
                            ALRT.SITUACAO
                    FROM TBCOMENTARIO_ALERTA ALRT
                        JOIN TBUSUARIO UO ON ( UO.ID = ALRT.IDUSUARIOORIG )
                        JOIN TBUSUARIO UD ON ( UD.ID = ALRT.IDUSUARIODSST )
                    WHERE ALRT.IDUSUARIODSST = :IDUSUARIODSST
                """
        if tipo: query += " AND ALRT.TIPO = :TIPO "
        if situacao: query += " AND ALRT.SITUACAO = :SITUACAO "
        query += " ORDER BY ALRT.DTHR DESC, ALRT.ID "

        params = {}
        params['IDUSUARIODSST'] = id_usuario
        if tipo: params['TIPO'] = tipo
        if situacao: params['SITUACAO'] = situacao
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def salvar_todos(cls, id_usuario: int = None, id_comentario: int = None, tipo_alerta: str = None, tipo_usuario: str = None, commit: bool = True):
        try:
            query = """ INSERT INTO TBCOMENTARIO_ALERTA( ID, IDCOMENTARIO, IDUSUARIOORIG, IDUSUARIODSST, DTHR, TIPO, SITUACAO ) 
                        SELECT NULL AS ID, :IDCOMENTARIO, :IDUSUARIOORIG, U.ID AS IDUSUARIODSST, :DTHRALERTA, :TIPOALERTA, 'P' AS SITUACAO
                        FROM TBUSUARIO U 
                        WHERE U.SITUACAO = 'A' AND U.TIPO = :TIPOUSUARIO AND U.ID <> :ID
                    """
            params = {'IDCOMENTARIO': id_comentario, 'IDUSUARIOORIG': id_usuario, 'DTHRALERTA': pegar_data_hora_atual(), 'TIPOALERTA': tipo_alerta, 'TIPOUSUARIO': tipo_usuario, 'ID': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def salvar_todas_resp(cls, id_usuario: int = None, id_comentario: int = None, commit: bool = True):
        try:
            query = """ INSERT INTO TBCOMENTARIO_ALERTA( ID, IDCOMENTARIO, IDUSUARIOORIG, IDUSUARIODSST, DTHR, TIPO, SITUACAO ) 
                        SELECT NULL AS ID, :IDCOMENTARIO, :IDUSUARIOORIG, U.ID AS IDUSUARIODSST, :DTHRALERTA, 'R' AS TIPO, 'P' AS SITUACAO
                        FROM TBUSUARIO U
                        WHERE U.SITUACAO = 'A' AND U.ID <> :IDPRINC AND EXISTS( SELECT 1 FROM TBCOMENTARIO C WHERE C.IDUSUARIO = U.ID AND ( C.ID = :ID OR C.IDPAI = :IDPAI ) )
                    """
            params = {'IDCOMENTARIO': id_comentario, 'IDUSUARIOORIG': id_usuario, 'DTHRALERTA': pegar_data_hora_atual(), 'IDPRINC': id_usuario, 'ID': id_comentario, 'IDPAI': id_comentario}
            db.session.execute(query, params)
            if commit: db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def marcar_todos_pendentes(cls, id_usuario: int = None, commit: bool = True):
        try:
            query = """ UPDATE TBCOMENTARIO_ALERTA SET SITUACAO = 'L' WHERE IDUSUARIODSST = :IDUSUARIODSST """
            params = {'IDUSUARIODSST': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_resposta(cls, id_comentario: int, commit: bool = True):
        try:
            query = """DELETE FROM TBCOMENTARIO_ALERTA WHERE IDCOMENTARIO IN ( SELECT C.ID FROM TBCOMENTARIO C WHERE C.IDPAI = :IDPAI AND C.TIPO = 'B')"""
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
            query = """DELETE FROM TBCOMENTARIO_ALERTA WHERE IDCOMENTARIO = :IDCOMENTARIO """
            params = {'IDCOMENTARIO': id_comentario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBCOMENTARIO_ALERTA WHERE IDUSUARIOORIG = :IDUSUARIOORIG"
            params = {'IDUSUARIOORIG': id_usuario}
            db.session.execute(query, params)
            query = "DELETE FROM TBCOMENTARIO_ALERTA WHERE IDUSUARIODSST = :IDUSUARIODSST"
            params = {'IDUSUARIODSST': id_usuario}
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
        if self.tipo == 'C':
            return 'Comentário'
        elif self.tipo == 'R':
            return 'Resposta'
        elif self.tipo == 'D':
            return 'Denúncia'
        else:
            return 'Desconhecido'

    def situacao_descr(self) -> str:
        if self.situacao == 'L':
            return 'Lido'
        elif self.situacao == 'P':
            return 'Pendente'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioComentarioAlerta - {str(self.id_comentario)} - {str(self.id_usuario)}>'
