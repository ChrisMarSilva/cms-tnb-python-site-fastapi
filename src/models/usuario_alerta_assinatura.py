# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioAlertaAssinaturaModel(_database.session.Base):

    __tablename__ = "TBALERTA_ASSINATURA"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    dthr_registro = _sql.Column('DTHRREGISTRO', _sql.String(14), nullable=False)
    dthr_alteracao = _sql.Column('DTHRALTERACAO', _sql.String(14), nullable=True)
    tipo_alerta = _sql.Column('TIPO_ALERTA', _sql.String(20), nullable=False, index=True)
    tipo_assinatura = _sql.Column('TIPO_ASSINATURA', _sql.String(1), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, dthr_registro: str = None, dthr_alteracao: str = None,
                 tipo_alerta: str = None, tipo_assinatura: str = None, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.dthr_registro = dthr_registro
        self.dthr_alteracao = dthr_alteracao
        self.tipo_alerta = tipo_alerta
        self.tipo_assinatura = tipo_assinatura
        self.situacao = situacao

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