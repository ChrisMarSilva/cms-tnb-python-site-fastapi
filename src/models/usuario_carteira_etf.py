# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database
from src.util.util_formatacao import decimal_to_str, inteiro_to_str


class UsuarioCarteiraEtfModel(_database.session.Base):

    __tablename__ = "TBCARTEIRA_INDICE"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    id_carteira = _sql.Column('IDCARTEIRA', _sql.Integer, _sql.ForeignKey('TBCARTEIRA.ID'), nullable=False, index=True)
    id_indice = _sql.Column('IDINDICE', _sql.Integer, _sql.ForeignKey('TBETF_INDICE.ID'), nullable=False, index=True)
    quant = _sql.Column('QUANT', _sql.Integer, nullable=True)
    quant_bonus = _sql.Column('QUANTBONUS', _sql.Integer, nullable=True)
    vlr_preco_medio = _sql.Column('VLRPRECOMEDIO', _sql.Float(20, 10), nullable=True)
    vlr_preco_teto = _sql.Column('VLRPRECOTETO', _sql.Float(17, 2), nullable=True)
    percent_balac = _sql.Column('PERCENTBALAC', _sql.Float(17, 2), nullable=True)
    nota_balac = _sql.Column('NOTABALAC', _sql.Integer, nullable=True)
    situacao = _sql.Column('SITUACAO', _sql.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_carteira: int = None, id_indice: int = None, quant: int = None,
                 quant_bonus: int = None, vlr_preco_medio: float = 0.0, vlr_preco_teto: float = 0.0,
                 percent_balac: float = 0.0, nota_balac: int = None, situacao: str = None):
        self.id = id
        self.id_carteira = id_carteira
        self.id_indice = id_indice
        self.quant = quant
        self.quant_bonus = quant_bonus
        self.vlr_preco_medio = vlr_preco_medio
        self.vlr_preco_teto = vlr_preco_teto
        self.percent_balac = percent_balac
        self.nota_balac = nota_balac
        self.situacao = situacao

    def quant_format(self) -> str:
        return inteiro_to_str(valor=self.quant)

    def quant_bonus_format(self) -> str:
        return inteiro_to_str(valor=self.quant_bonus)

    def vlr_preco_medio_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_medio)

    def vlr_preco_teto_format(self) -> str:
        return decimal_to_str(valor=self.vlr_preco_teto)

    def percent_balac_format(self) -> str:
        return decimal_to_str(valor=self.percent_balac)

    def situacao_descr(self) -> str:
        if self.situacao == 'A':
            return 'Ativo'
        elif self.situacao == 'I':
            return 'Inativo'
        elif self.situacao == 'F':
            return 'Finalizado'
        else:
            return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioCarteiraIndice {str(self.id)}>'
