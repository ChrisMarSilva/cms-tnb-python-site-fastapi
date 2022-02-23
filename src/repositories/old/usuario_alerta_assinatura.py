# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioAlertaAssinatura(db.Model):

    __tablename__ = "TBALERTA_ASSINATURA"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    dthr_registro = db.Column('DTHRREGISTRO', db.String(14), nullable=False)
    dthr_alteracao = db.Column('DTHRALTERACAO', db.String(14), nullable=True)
    tipo_alerta = db.Column('TIPO_ALERTA', db.String(20), nullable=False, index=True)
    tipo_assinatura = db.Column('TIPO_ASSINATURA', db.String(1), nullable=False, index=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, dthr_registro: str = None, dthr_alteracao: str = None,
                 tipo_alerta: str = None, tipo_assinatura: str = None, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.dthr_registro = dthr_registro
        self.dthr_alteracao = dthr_alteracao
        self.tipo_alerta = tipo_alerta
        self.tipo_assinatura = tipo_assinatura
        self.situacao = situacao

    @classmethod
    def get_all(cls):
        try:
            return cls.query.all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_all_by_usuario(cls, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).all()
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
    def get_by_tipos(cls, id_usuario: int, tipo_assinatura: str, tipo_alerta: str):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, tipo_assinatura=tipo_assinatura, tipo_alerta=tipo_alerta).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int = None):
        query = """ SELECT AA.ID, AA.IDUSUARIO, US.NOME AS NMUSUARIO, AA.DTHRREGISTRO, AA.DTHRALTERACAO, AA.TIPO_ALERTA, AA.TIPO_ASSINATURA, AA.SITUACAO
                    FROM TBALERTA_ASSINATURA AA JOIN TBUSUARIO US ON ( US.ID = AA.IDUSUARIO )
                    WHERE 1 = 1 
                """
        if id_usuario: query += " AND AA.IDUSUARIO = :IDUSUARIO "
        query += " ORDER BY AA.TIPO_ALERTA, AA.TIPO_ASSINATURA "
        params = {}
        if id_usuario: params['IDUSUARIO'] = id_usuario
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id: int):
        query = """ SELECT AA.ID, AA.IDUSUARIO, US.NOME AS NMUSUARIO, AA.DTHRREGISTRO, AA.DTHRALTERACAO, AA.TIPO_ALERTA, AA.TIPO_ASSINATURA, AA.SITUACAO
                    FROM TBALERTA_ASSINATURA AA JOIN TBUSUARIO US ON ( US.ID = AA.IDUSUARIO )
                    WHERE AA.ID = :ID 
                """
        params = {'ID': id}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_tipo_alerta_assinatura(cls, id_usuario: int = None, tipo_alerta: str = None, tipo_assinatura: str = None):
        query = """ SELECT AA.ID, AA.IDUSUARIO, US.NOME AS NMUSUARIO, AA.DTHRREGISTRO, AA.DTHRALTERACAO, AA.TIPO_ALERTA, AA.TIPO_ASSINATURA, AA.SITUACAO
                    FROM TBALERTA_ASSINATURA AA
                         JOIN TBUSUARIO US ON ( US.ID = AA.IDUSUARIO )
                    WHERE AA.IDUSUARIO = :IDUSUARIO 
                      AND AA.TIPO_ALERTA = :TIPO_ALERTA 
                      AND AA.TIPO_ASSINATURA = :TIPO_ASSINATURA 
                """
        params = {'IDUSUARIO': id_usuario, 'TIPO_ALERTA': tipo_alerta, 'TIPO_ASSINATURA': tipo_assinatura}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_lista_user(cls, tipo_alerta: str = None, tipo_assinatura: str = None):
        query = """ SELECT U.ID, U.NOME FROM TBUSUARIO U WHERE EXISTS( SELECT 1 FROM TBALERTA_ASSINATURA AA WHERE AA.IDUSUARIO = U.ID """
        if tipo_alerta: query += " AND AA.TIPO_ALERTA = :TIPO_ALERTA "
        if tipo_assinatura: query += " AND AA.TIPO_ASSINATURA = :TIPO_ASSINATURA "
        query += " ) "
        query += " ORDER BY U.NOME "

        params = {}
        if tipo_alerta: params['TIPO_ALERTA'] = tipo_alerta
        if tipo_assinatura: params['TIPO_ASSINATURA'] = tipo_assinatura

        try:
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

    def dthr_registro_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.dthr_registro, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def dthr_alteracao_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.dthr_alteracao, fmt='%Y%m%d%H%M%S'), fmt='%d/%m/%Y %H:%M:%S')

    def tipo_alerta_descr(self) -> str:
        return self.descricao_tipo_alerta(tipo_alerta=self.tipo_alerta)

    def tipo_assinatura_descr(self) -> str:
        return self.descricao_tipo_assinatura(tipo_assinatura=self.tipo_assinatura)

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def descricao_tipo_alerta(cls, tipo_alerta: str) -> str:
        if tipo_alerta == "ADMIN-01":
            return "Admin-Todos"
        elif tipo_alerta == "ADMIN-02":
            return "Admin-Alguem"
        elif tipo_alerta == "LOGIN-01":
            return "Login-Login-Realizado"
        elif tipo_alerta == "LOGIN-02":
            return "Login-Tentativa-Login"
        elif tipo_alerta == "LOGIN-03":
            return "Login-Ativado-Bloqueado-Inativado"
        elif tipo_alerta == "PERFIL-01":
            return "Perfil-Alterar-Senha"
        elif tipo_alerta == "PERFIL-02":
            return "Perfil-Limpar-Dados"
        elif tipo_alerta == "PERFIL-03":
            return "Perfil-Limpar-Operacoes"
        elif tipo_alerta == "PERFIL-04":
            return "Perfil-Limpar-Proventos"
        elif tipo_alerta == "PORTFOLIO-01":
            return "Portfolio-Desempenho-Dia"
        elif tipo_alerta == "PROVENTOS-01":
            return "Proventos-Data-Aprovacao"
        elif tipo_alerta == "PROVENTOS-02":
            return "Proventos-Data-Ex"
        elif tipo_alerta == "PROVENTOS-03":
            return "Proventos-Data-Pagto"
        elif tipo_alerta == "CEI-01":
            return "Cei-Ativada-Inativada"
        elif tipo_alerta == "CEI-02":
            return "Cei-Falha-Login"
        elif tipo_alerta == "CEI-03":
            return "Cei-Integrado"
        elif tipo_alerta == "FATOS-01":
            return "Fatos-Fato-Relevante"
        elif tipo_alerta == "FATOS-02":
            return "Fatos-Aviso-Acionistas"
        elif tipo_alerta == "FATOS-03":
            return "Fatos-Comunicado-Mercado"
        elif tipo_alerta == "FATOS-04":
            return "Fatos-Dados-Financeiro"
        elif tipo_alerta == "FATOS-05":
            return "Fatos-Ata-Reuniao"
        elif tipo_alerta == "FATOS-06":
            return "Fatos-Recompra-Acoes"
        elif tipo_alerta == "FATOS-07":
            return "Fatos-Calendario-Eventos"
        elif tipo_alerta == "FATOS-08":
            return "Fatos-Aumento-Capital"
        elif tipo_alerta == "FATOS-09":
            return "Fatos-Outros"
        else:
            return 'Desconhecido'

    @classmethod
    def descricao_tipo_assinatura(cls, tipo_assinatura: str) -> str:
        if tipo_assinatura == 'E':
            return 'Email'
        elif tipo_assinatura == 'T':
            return 'Telegram'
        else:
            return 'Desconhecido'

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':
            return 'Ativa'
        elif situacao == 'I':
            return 'Inativa'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioAlertaAssinatura' \
               ' id: {str(self.id)}' \
               ' id_usuario: {str(self.id_usuario)}' \
               ' dthr_registro: {str(self.dthr_registro)}' \
               ' dthr_alteracao: {str(self.dthr_alteracao)}' \
               ' tipo_alerta: {str(self.tipo_alerta)}' \
               ' tipo_assinatura: {str(self.tipo_assinatura)}' \
               ' situacao: {str(self.situacao)}' \
               '>'