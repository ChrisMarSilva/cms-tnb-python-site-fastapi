# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_datahora import pegar_data_atual, pegar_data_hora_atual, converter_str_to_datetime, converter_datetime_str


class Alerta(db.Model):

    __tablename__ = "TBALERTA"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    dthr_registro = db.Column('DTHRREGISTRO', db.String(14), nullable=False)
    data_envio = db.Column('DTENVIO', db.String(8), nullable=False)
    tipo = db.Column('TIPO', db.String(20), nullable=False, index=True)
    mensagem = db.Column('MENSAGEM', db.Text(), nullable=True)
    qtd_proc = db.Column('QTD_PROC', db.Integer, nullable=True)
    situacao_telegram = db.Column('SITUACAO_TELEGRAM', db.String(1), nullable=False, index=True)
    situacao_email = db.Column('SITUACAO_EMAIL', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, dthr_registro: str = None, data_envio: str = None,
                 tipo: str = None, mensagem: str = None, qtd_proc: int = None, situacao_telegram: str = None,
                 situacao_email: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.dthr_registro = dthr_registro
        self.data_envio = data_envio
        self.tipo = tipo
        self.mensagem = mensagem
        self.qtd_proc = qtd_proc
        self.situacao_telegram = situacao_telegram
        self.situacao_email = situacao_email

    @classmethod
    def get_all(cls):
        try:
            return cls.query.order_by(cls.dthr_registro).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_all_by_usuario(cls, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).order_by(cls.dthr_registro).all()
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
    def get_by_id_usuarios(cls, id_usuario: int, id: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario, id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int = None, tipo: str = None, dt_ini: str = None, dt_fim: str = None):
        query = """ SELECT AL.ID, AL.IDUSUARIO, US.NOME AS NMUSUARIO, AL.DTHRREGISTRO, AL.DTENVIO, AL.TIPO, AL.MENSAGEM, AL.QTD_PROC, AL.SITUACAO_TELEGRAM, AL.SITUACAO_EMAIL
                    FROM TBALERTA AL LEFT JOIN TBUSUARIO US ON ( US.ID = AL.IDUSUARIO )
                    WHERE 1 = 1
                """
        if id_usuario: query += " AND AL.IDUSUARIO = :IDUSUARIO  "
        if tipo: query += " AND AL.TIPO = :TIPO "
        if dt_ini: query += " AND AL.DTENVIO  >= :DATAINICIO "
        if dt_fim: query += " AND AL.DTENVIO  <= :DATAFIM "
        query += " ORDER BY AL.DTENVIO, AL.DTHRREGISTRO, AL.ID "

        params = {}
        if id_usuario: params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim

        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id: int):
        query = """ SELECT AL.ID, AL.IDUSUARIO, US.NOME AS NMUSUARIO, AL.DTHRREGISTRO, AL.DTENVIO, AL.TIPO, AL.MENSAGEM, AL.QTD_PROC, AL.SITUACAO_TELEGRAM, AL.SITUACAO_EMAIL
                    FROM TBALERTA AL
                         JOIN TBUSUARIO US ON ( US.ID = AL.IDUSUARIO )
                    WHERE AL.ID = :ID 
                """
        params = {'ID': id}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_lista_user(cls):
        query = """ SELECT U.ID, U.NOME FROM TBUSUARIO U WHERE EXISTS( SELECT 1 FROM TBALERTA AL WHERE AL.IDUSUARIO = U.ID ) ORDER BY U.NOME """
        params = {}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @staticmethod
    def registrar(id_usuario: int = None, tipo: str = None, mensagem: str = None):
        try:

            alerta = Alerta()
            alerta.id_usuario = id_usuario
            alerta.dthr_registro = pegar_data_hora_atual()
            alerta.data_envio = pegar_data_atual()
            alerta.tipo = tipo
            alerta.mensagem = mensagem
            alerta.qtd_proc = 0
            alerta.situacao_telegram = 'P'  # P-Pendente
            alerta.situacao_email = 'P'  # P-Pendente

            db.session.add(alerta)
            db.session.commit()

        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))

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

    def data_envio_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_envio, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_envio_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data_envio, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def tipo_descr(self) -> str:
        return self.descricao_tipo(tipo=self.tipo)

    def situacao_telegram_descr(self) -> str:
        return self.descricao_situacao_telegram(situacao_telegram=self.situacao_telegram)

    def situacao_email_descr(self) -> str:
        return self.descricao_situacao_email(situacao_email=self.situacao_email)

    @classmethod
    def descricao_tipo(cls, tipo: str) -> str:
        if tipo == "ADMIN-01":
            return "Admin-Todos"
        elif tipo == "ADMIN-02":
            return "Admin-Alguem"
        elif tipo == "LOGIN-01":
            return "Login-Login-Realizado"
        elif tipo == "LOGIN-02":
            return "Login-Tentativa-Login"
        elif tipo == "LOGIN-03":
            return "Login-Ativado-Bloqueado-Inativado"
        elif tipo == "PERFIL-01":
            return "Perfil-Alterar-Senha"
        elif tipo == "PERFIL-02":
            return "Perfil-Limpar-Dados"
        elif tipo == "PERFIL-03":
            return "Perfil-Limpar-Operacoes"
        elif tipo == "PERFIL-04":
            return "Perfil-Limpar-Proventos"
        elif tipo == "PORTFOLIO-01":
            return "Portfolio-Desempenho-Dia"
        elif tipo == "PROVENTOS-01":
            return "Proventos-Data-Aprovacao"
        elif tipo == "PROVENTOS-02":
            return "Proventos-Data-Ex"
        elif tipo == "PROVENTOS-03":
            return "Proventos-Data-Pagto"
        elif tipo == "CEI-01":
            return "Cei-Ativada-Inativada"
        elif tipo == "CEI-02":
            return "Cei-Falha-Login"
        elif tipo == "CEI-03":
            return "Cei-Integrado"
        elif tipo == "FATOS-01":
            return "Fatos-Fato-Relevante"
        elif tipo == "FATOS-02":
            return "Fatos-Aviso-Acionistas"
        elif tipo == "FATOS-03":
            return "Fatos-Comunicado-Mercado"
        elif tipo == "FATOS-04":
            return "Fatos-Dados-Financeiro"
        elif tipo == "FATOS-05":
            return "Fatos-Ata-Reuniao"
        elif tipo == "FATOS-06":
            return "Fatos-Recompra-Acoes"
        elif tipo == "FATOS-07":
            return "Fatos-Calendario-Eventos"
        elif tipo == "FATOS-08":
            return "Fatos-Aumento-Capital"
        elif tipo == "FATOS-09":
            return "Fatos-Outros"
        else:
            return 'Desconhecido'

    @classmethod
    def descricao_situacao_telegram(cls, situacao_telegram: str) -> str:
        if situacao_telegram == 'E':
            return 'Enviado'
        elif situacao_telegram == 'P':
            return 'Pendente'
        elif situacao_telegram == 'I':
            return 'Ignorado'
        elif situacao_telegram == 'X':
            return 'Erro'
        else:
            return 'Desconhecido'

    @classmethod
    def descricao_situacao_email(cls, situacao_email: str) -> str:
        if situacao_email == 'E':
            return 'Enviado'
        elif situacao_email == 'P':
            return 'Pendente'
        elif situacao_email == 'I':
            return 'Ignorado'
        elif situacao_email == 'X':
            return 'Erro'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<Alerta {str(self.id)}>'
