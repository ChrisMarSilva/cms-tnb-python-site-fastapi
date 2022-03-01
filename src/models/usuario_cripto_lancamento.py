# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str, inteiro_to_str
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioCriptoLancamento(_database.session.Base):

    __tablename__ = "TBCRIPTO_LANCAMENTO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    id_cripto = _sql.Column('IDCRIPTO', _sql.Integer, _sql.ForeignKey('TBCRIPTO_EMPRESA.ID'), nullable=False, index=True)
    id_corretora = _sql.Column('IDCORRETORA', _sql.Integer, _sql.ForeignKey('TBCORRETORA.ID'), nullable=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    data = _sql.Column('DATA', _sql.String(8), nullable=False, index=True)
    quant = _sql.Column('QUANT', _sql.Float(30, 15), nullable=False)
    quant_orig = _sql.Column('QUANTORIG', _sql.Float(30, 15), nullable=False, index=True)
    vlr_preco = _sql.Column('VLRPRECO', _sql.Float(30, 15), nullable=True)
    tot_vlr_preco = _sql.Column('TOTVLRPRECO', _sql.Float(30, 15), nullable=True)
    vlr_corretagem = _sql.Column('VLRTAXA', _sql.Float(17, 2), nullable=True)
    tot_vlr = _sql.Column('TOTVLR', _sql.Float(17, 2), nullable=True)
    vlr_custo = _sql.Column('VLRCUSTO', _sql.Float(30, 15), nullable=True)
    tot_vlr_custo = _sql.Column('TOTVLRCUSTO', _sql.Float(17, 2), nullable=True)
    vlr_preco_medio = _sql.Column('VLRPRECOMEDIO', _sql.Float(30, 15), nullable=True)
    tot_vlr_valorizacao = _sql.Column('TOTVLRVALORIZACAO', _sql.Float(17, 2), nullable=True)
    perc_valorizacao = _sql.Column('PERCVALORIZACAO', _sql.Float(17, 2), nullable=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, id_cripto: int = None, id_corretora: int = None,
                 tipo: str = None, data: str = None, quant: float = 0.0, quant_orig: float = 0.0,
                 vlr_preco: float = 0.0, tot_vlr_preco: float = 0.0, vlr_corretagem: float = 0.0, tot_vlr: float = 0.0,
                 vlr_custo: float = 0.0, tot_vlr_custo: float = 0.0, vlr_preco_medio: float = 0.0,
                 tot_vlr_valorizacao: float = 0.0,  perc_valorizacao: float = 0.0,
                 situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_cripto = id_cripto
        self.id_corretora = id_corretora
        self.tipo = tipo
        self.data = data
        self.quant = quant
        self.quant_orig = quant_orig
        self.vlr_preco = vlr_preco
        self.tot_vlr_preco = tot_vlr_preco
        self.vlr_corretagem = vlr_corretagem
        self.tot_vlr = tot_vlr
        self.vlr_custo = vlr_custo
        self.tot_vlr_custo = tot_vlr_custo
        self.vlr_preco_medio = vlr_preco_medio
        self.tot_vlr_valorizacao = tot_vlr_valorizacao
        self.perc_valorizacao = perc_valorizacao
        self.situacao = situacao

    def calc_tot_preco(self) -> None:
        self.tot_vlr_preco = self.calcular_tot_preco(quant=self.quant, vlr_preco=self.vlr_preco)

    def calc_tot_taxa(self) -> None:
        # self.vlr_corretagem = self.vlr_corretagem
        pass

    def calc_total(self) -> None:
        self.tot_vlr = self.calcular_total(tipo=self.tipo, tot_vlr_preco=self.tot_vlr_preco, vlr_corretagem=self.vlr_corretagem)

    def calc_custo(self) -> None:
        self.vlr_custo = self.calcular_custo(quant=self.quant, tot_vlr=self.tot_vlr)

    def calc_preco_medio(self, qtde_atual: float = 0.0, preco_medio_atual: float = 0.0):
        self.vlr_preco_medio = 0.0
        if str(self.tipo) == 'C':
            tot_vlr_custo = float(self.vlr_custo) * float(self.quant) if float(self.vlr_custo) > 0.0 and float(self.quant) > 0.0 else 0.0
            if qtde_atual > 0.0 and preco_medio_atual > 0.0:
                tot_vlr_custo += (float(qtde_atual) * float(preco_medio_atual)) if float(qtde_atual) > 0.0 and float(preco_medio_atual) > 0.0 else 0.0
            qtde_atual += float(self.quant)
            if qtde_atual > 0.0 and tot_vlr_custo > 0.0:
                preco_medio_atual = (float(tot_vlr_custo) / float(qtde_atual)) if float(tot_vlr_custo) > 0.0 and float(qtde_atual) > 0.0 else 0.0
        elif str(self.tipo) == 'V' or str(self.tipo) == 'P':
            qtde_atual -= float(self.quant)
        self.vlr_preco_medio = float(preco_medio_atual)
        return float(qtde_atual), float(preco_medio_atual)

    def calc_vlr_valorizacao(self) -> None:
        self.tot_vlr_valorizacao = self.calcular_vlr_valorizacao(tipo=str(self.tipo), quant=float(self.quant), vlr_preco_medio=float(self.vlr_preco_medio), tot_vlr_custo=float(self.tot_vlr_custo))

    def calc_perc_valorizacao(self) -> None:
        # self.calc_vlr_valorizacao()
        self.perc_valorizacao = self.calcular_perc_valorizacao(tipo=str(self.tipo), quant=float(self.quant), vlr_preco_medio=float(self.vlr_preco_medio), tot_vlr_valorizacao=float(self.tot_vlr_valorizacao))

    def data_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def data_format_xml(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.data, fmt='%Y%m%d'), fmt='%Y-%m-%d')

    def quant_format(self) -> str:
        return inteiro_to_str(valor=self.quant)

    def quant_orig_format(self) -> str:
        return inteiro_to_str(valor=self.quant_orig)

    def vlr_preco_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco)

    def tot_vlr_preco_format(self) -> str:
        return decimal_to_str(valor=self.tot_vlr_preco)

    def vlr_corretagem_format(self) -> str:
        return decimal_to_str(valor=self.vlr_corretagem)

    def tot_vlr_format(self) -> str:
        return decimal_to_str(valor=self.tot_vlr)

    def vlr_custo_format(self) -> str:
        return decimal_to_str(valor=self.vlr_custo)

    def tot_vlr_custo_format(self) -> str:
        return decimal_to_str(valor=self.tot_vlr_custo)

    def vlr_preco_medio_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_medio)

    def tot_vlr_valorizacao_format(self) -> str:
        return decimal_to_str(valor=self.tot_vlr_valorizacao)

    def perc_valorizacao_format(self) -> str:
        return decimal_to_str(valor=self.perc_valorizacao)

    def tipo_descr(self) -> str:
        return self.descricao_tipo(tipo=self.tipo)

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def calcular_tot_preco(cls, quant: float, vlr_preco: float) -> float:
        return float(quant) * float(vlr_preco) if quant > 0.0 and vlr_preco > 0.0 else 0.0

    @classmethod
    def calcular_total(cls, tipo: str, tot_vlr_preco: float, vlr_corretagem: float) -> float:
        tot_vlr = 0.0
        if str(tipo) == 'C':
            tot_vlr = float(tot_vlr_preco) + float(vlr_corretagem)
        elif str(tipo) == 'V':
            tot_vlr = float(tot_vlr_preco) - float(vlr_corretagem)
        return tot_vlr

    @classmethod
    def calcular_custo(cls, quant: float, tot_vlr: float) -> float:
        return (float(tot_vlr) / float(quant)) if quant > 0.0 and tot_vlr > 0.0 else 0.0

    @classmethod
    def calcular_vlr_valorizacao(cls, tipo: str, quant: float, vlr_preco_medio: float, tot_vlr_custo: float) -> float:
        tot_vlr_valorizacao = 0.0
        if (str(tipo) == 'V' or str(tipo) == 'P') and float(vlr_preco_medio) > 0.0 and float(quant) > 0.0:
            tot_vlr_valorizacao = float(tot_vlr_custo) - (float(vlr_preco_medio) * float(quant))
        return float(tot_vlr_valorizacao)

    @classmethod
    def calcular_perc_valorizacao(cls, tipo: str, quant: float, vlr_preco_medio: float, tot_vlr_valorizacao: float) -> float:
        perc_valorizacao = 0.0
        if (str(tipo) == 'V' or str(tipo) == 'P') and float(tot_vlr_valorizacao) != 0.0 and float(vlr_preco_medio) > 0.0 and float(quant) > 0.0:
            perc_valorizacao = (float(tot_vlr_valorizacao) / (float(vlr_preco_medio) * float(quant))) * 100
        return float(perc_valorizacao)

    @classmethod
    def descricao_tipo(cls, tipo: str) -> str:
        if tipo == 'C': return 'Compra'
        elif tipo == 'V': return 'Venda'
        elif tipo == 'P': return 'Projetado'
        else: return 'Desconhecido'

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A': return 'Ativo'
        elif situacao == 'P': return 'Pendente'
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioCriptoLancamento {str(self.id)}>'
