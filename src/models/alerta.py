# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class Alerta(_database.session.Base):

    __tablename__ = "TBALERTA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    dthr_registro = _sql.Column('DTHRREGISTRO', _sql.String(14), nullable=False)
    data_envio = _sql.Column('DTENVIO', _sql.String(8), nullable=False)
    tipo = _sql.Column('TIPO', _sql.String(20), nullable=False, index=True)
    mensagem = _sql.Column('MENSAGEM', _sql.Text(), nullable=True)
    qtd_proc = _sql.Column('QTD_PROC', _sql.Integer, nullable=True)
    situacao_telegram = _sql.Column('SITUACAO_TELEGRAM', _sql.String(1), nullable=False, index=True)
    situacao_email = _sql.Column('SITUACAO_EMAIL', _sql.String(1), nullable=False, index=True)

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
