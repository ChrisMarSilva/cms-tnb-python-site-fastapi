# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str


class UsuarioCarteiraProjecaoItemModel(_database.session.Base):

    __tablename__ = "TBCARTEIRA_PROJECAO_ITEM"

    id_projecao = _sql.Column('IDPROJECAO', _sql.Integer, _sql.ForeignKey('TBCARTEIRA_PROJECAO.ID'), primary_key=True, nullable=False, index=True)
    numero = _sql.Column('NUMERO', _sql.Integer, primary_key=True, nullable=False, index=True)
    ano = _sql.Column('ANO', _sql.Integer, nullable=False)
    mes = _sql.Column('MES', _sql.Integer, nullable=False)
    vlr_invest_ini = _sql.Column('VLRINVESTINI', _sql.Float(17, 2), nullable=True)
    vlr_invest_mes = _sql.Column('VLRINVESTMES', _sql.Float(17, 2), nullable=True)
    vlr_invest_fim = _sql.Column('VLRINVESTFIM', _sql.Float(17, 2), nullable=True)
    rend_messal = _sql.Column('RENDMENSAL', _sql.Float(5, 2), nullable=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id_projecao: int = None, numero: int = None, ano: str = None, mes: str = None,
                 vlr_invest_ini: float = 0.0, vlr_invest_mes: float = 0.0, vlr_invest_fim: float = 0.0,
                 rend_messal: float = 0.0, tipo: str = None, situacao: str = None):
        self.id_projecao = id_projecao
        self.numero = numero
        self.ano = ano
        self.mes = mes
        self.vlr_invest_ini = vlr_invest_ini
        self.vlr_invest_mes = vlr_invest_mes
        self.vlr_invest_fim = vlr_invest_fim
        self.rend_messal = rend_messal
        self.tipo = tipo
        self.situacao = situacao

    def vlr_invest_ini_format(self) -> str:
        return decimal_to_str(valor=self.vlr_invest_ini)

    def vlr_invest_mes_format(self) -> str:
        return decimal_to_str(valor=self.vlr_invest_mes)

    def vlr_invest_fim_format(self) -> str:
        return decimal_to_str(valor=self.vlr_invest_fim)

    def rend_messal_format(self) -> str:
        return decimal_to_str(valor=self.rend_messal)

    def tipo_descr(self) -> str:
        if self.tipo == 'C':
            return 'Calculado'
        elif self.tipo == 'M':
            return 'Modificado'
        else:
            return 'Desconhecido'

    def situacao_descr(self) -> str:
        if self.situacao == 'A':
            return 'Ativo'
        elif self.situacao == 'I':
            return 'Inativo'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioCarteiraProjecaoItem {str(self.id)}>'
