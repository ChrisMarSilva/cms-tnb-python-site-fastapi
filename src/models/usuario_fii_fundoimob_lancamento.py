# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str, inteiro_to_str
from src.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioFiiFundoImobLancamentoModel(_database.session.Base):

    __tablename__ = "TBFII_LANCAMENTO"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_usuario = _sql.Column('IDUSUARIO', _sql.Integer, _sql.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    id_fundo = _sql.Column('IDFUNDO', _sql.Integer, _sql.ForeignKey('TBFII_FUNDOIMOB.ID'), nullable=False, index=True)
    id_corretora = _sql.Column('IDCORRETORA', _sql.Integer, _sql.ForeignKey('TBCORRETORA.ID'), nullable=True)
    tipo = _sql.Column('TIPO', _sql.String(1), nullable=False, index=True)
    data = _sql.Column('DATA', _sql.String(8), nullable=False, index=True)
    quant = _sql.Column('QUANT', _sql.Float(20, 10), nullable=False)
    quant_orig = _sql.Column('QUANTORIG', _sql.Float(20, 10), nullable=False, index=True)
    vlr_preco = _sql.Column('VLRPRECO', _sql.Float(17, 2), nullable=True)
    tot_vlr_preco = _sql.Column('TOTVLRPRECO', _sql.Float(17, 2), nullable=True)
    vlr_liquidacao = _sql.Column('VLRTXLIQUIDACAO', _sql.Float(17, 2), nullable=True)
    vlr_emolumentos = _sql.Column('VLRTXEMOLUMENTOS', _sql.Float(17, 2), nullable=True)
    vlr_corretagem = _sql.Column('VLRTXCORRETAGEM', _sql.Float(17, 2), nullable=True)
    vlr_irpf = _sql.Column('VLRTXIRRF', _sql.Float(17, 2), nullable=True)
    vlr_iss = _sql.Column('VLRTXISS', _sql.Float(17, 2), nullable=True)
    vlr_outras = _sql.Column('VLRTXOUTRAS', _sql.Float(17, 2), nullable=True)
    tot_vlr_taxa = _sql.Column('TOTVLRTX', _sql.Float(17, 2), nullable=True)
    tot_vlr = _sql.Column('TOTVLR', _sql.Float(17, 2), nullable=True)
    vlr_custo = _sql.Column('VLRCUSTO', _sql.Float(20, 10), nullable=True)
    tot_vlr_custo = _sql.Column('TOTVLRCUSTO', _sql.Float(17, 2), nullable=True)
    vlr_preco_medio = _sql.Column('VLRPRECOMEDIO', _sql.Float(20, 10), nullable=True)
    tot_vlr_valorizacao = _sql.Column('TOTVLRVALORIZACAO', _sql.Float(17, 2), nullable=True)
    perc_valorizacao = _sql.Column('PERCVALORIZACAO', _sql.Float(17, 2), nullable=True)
    troca = _sql.Column('TROCA', _sql.String(1), nullable=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, id_fundo: int = None, id_corretora: int = None,
                 tipo: str = None, data: str = None, quant: float = 0.0, quant_orig: float = 0.0,
                 vlr_preco: float = 0.0, tot_vlr_preco: float = 0.0, vlr_liquidacao: float = 0.0,
                 vlr_emolumentos: float = 0.0, vlr_corretagem: float = 0.0, vlr_irpf: float = 0.0,
                 vlr_iss: float = 0.0, vlr_outras: float = 0.0, tot_vlr_taxa: float = 0.0, tot_vlr: float = 0.0,
                 vlr_custo: float = 0.0, tot_vlr_custo: float = 0.0, vlr_preco_medio: float = 0.0,
                 tot_vlr_valorizacao: float = 0.0,  perc_valorizacao: float = 0.0, troca: str = 'N',
                 situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_fundo = id_fundo
        self.id_corretora = id_corretora
        self.tipo = tipo
        self.data = data
        self.quant = quant
        self.quant_orig = quant_orig
        self.vlr_preco = vlr_preco
        self.tot_vlr_preco = tot_vlr_preco
        self.vlr_liquidacao = vlr_liquidacao
        self.vlr_emolumentos = vlr_emolumentos
        self.vlr_corretagem = vlr_corretagem
        self.vlr_irpf = vlr_irpf
        self.vlr_iss = vlr_iss
        self.vlr_outras = vlr_outras
        self.tot_vlr_taxa = tot_vlr_taxa
        self.tot_vlr = tot_vlr
        self.vlr_custo = vlr_custo
        self.tot_vlr_custo = tot_vlr_custo
        self.vlr_preco_medio = vlr_preco_medio
        self.tot_vlr_valorizacao = tot_vlr_valorizacao
        self.perc_valorizacao = perc_valorizacao
        self.troca = troca
        self.situacao = situacao

    def calc_tot_preco(self) -> None:
        self.tot_vlr_preco = self.calcular_tot_preco(quant=self.quant, vlr_preco=self.vlr_preco)

    def calc_tot_taxa(self) -> None:
        self.tot_vlr_taxa = self.calcular_tot_taxa(vlr_liquidacao=self.vlr_liquidacao, vlr_emolumentos=self.vlr_emolumentos, vlr_corretagem=self.vlr_corretagem, vlr_iss=self.vlr_iss, vlr_outras=self.vlr_outras)

    def calc_total(self) -> None:
        self.tot_vlr = self.calcular_total(tipo=self.tipo, tot_vlr_preco=self.tot_vlr_preco, tot_vlr_taxa=self.tot_vlr_taxa)

    def calc_custo(self) -> None:
        self.vlr_custo = self.calcular_custo(quant=self.quant, tot_vlr=self.tot_vlr)

    def calc_preco_medio(self, qtde_atual: float = 0.0, preco_medio_atual: float = 0.0):
        self.vlr_preco_medio = 0.0
        if str(self.tipo) == 'C' or str(self.tipo) == 'B':
            tot_vlr_custo = float(self.vlr_custo) * float(self.quant) if float(self.vlr_custo) > 0.0 and float(self.quant) > 0.0 else 0.0
            if qtde_atual > 0.0 and preco_medio_atual > 0.0:
                tot_vlr_custo += (float(qtde_atual) * float(preco_medio_atual)) if float(qtde_atual) > 0.0 and float(preco_medio_atual) > 0.0 else 0.0
            qtde_atual += float(self.quant)
            if qtde_atual > 0.0 and tot_vlr_custo > 0.0:
                preco_medio_atual = (float(tot_vlr_custo) / float(qtde_atual)) if float(tot_vlr_custo) > 0.0 and float(qtde_atual) > 0.0 else 0.0
        elif str(self.tipo) == 'A':
            tot_vlr_custo = float(self.vlr_custo) * float(self.quant) if float(self.vlr_custo) > 0.0 and float(self.quant) > 0.0 else 0.0
            if qtde_atual > 0.0 and preco_medio_atual > 0.0:
                tot_vlr_custo -= (float(qtde_atual) * float(preco_medio_atual)) if float(qtde_atual) > 0.0 and float(preco_medio_atual) > 0.0 else 0.0
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

    def vlr_liquidacao_format(self) -> str:
        return decimal_to_str(valor=self.vlr_liquidacao)

    def vlr_emolumentos_format(self) -> str:
        return decimal_to_str(valor=self.vlr_emolumentos)

    def vlr_corretagem_format(self) -> str:
        return decimal_to_str(valor=self.vlr_corretagem)

    def vlr_irpf_format(self) -> str:
        return decimal_to_str(valor=self.vlr_irpf)

    def vlr_iss_format(self) -> str:
        return decimal_to_str(valor=self.vlr_iss)

    def vlr_outras_format(self) -> str:
        return decimal_to_str(valor=self.vlr_outras)

    def tot_vlr_taxa_format(self) -> str:
        return decimal_to_str(valor=self.tot_vlr_taxa)

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
        return self.descricao_tipo(tipo=self.tipo, troca=self.troca)

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

    @classmethod
    def calcular_tot_preco(cls, quant: float, vlr_preco: float) -> float:
        return float(quant) * float(vlr_preco) if quant > 0.0 and vlr_preco > 0.0 else 0.0

    @classmethod
    def calcular_tot_taxa(cls, vlr_liquidacao: float, vlr_emolumentos: float, vlr_corretagem: float, vlr_iss: float, vlr_outras: float) -> float:
        return float(vlr_liquidacao) + float(vlr_emolumentos) + float(vlr_corretagem) + float(vlr_iss) + float(vlr_outras)

    @classmethod
    def calcular_total(cls, tipo: str, tot_vlr_preco: float, tot_vlr_taxa: float) -> float:
        tot_vlr = 0.0
        if str(tipo) == 'A' or str(tipo) == 'C' or str(tipo) == 'B':
            tot_vlr = float(tot_vlr_preco) + float(tot_vlr_taxa)
        elif str(tipo) == 'V':
            tot_vlr = float(tot_vlr_preco) - float(tot_vlr_taxa)
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
    def descricao_tipo(cls, tipo: str, troca: str = 'N') -> str:
        if tipo == 'C' and str(troca) != 'S': return 'Compra'
        elif tipo == 'C' and troca == 'S': return 'Compra/Troca'
        elif tipo == 'V' and str(troca) != 'S': return 'Venda'
        elif tipo == 'V' and troca == 'S': return 'Venda/Troca'
        elif tipo == 'A': return 'Amortiza????o'
        elif tipo == 'B': return 'Bonifica????o'
        elif tipo == 'D': return 'Desdobramento'
        elif tipo == 'G': return 'Grupamento'
        elif tipo == 'P': return 'Projetado'
        else: return 'Desconhecido'

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':
            return 'Ativo'
        elif situacao == 'P':
            return 'Pendente'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioFiiFundoImobLancamento {str(self.id)}>'
