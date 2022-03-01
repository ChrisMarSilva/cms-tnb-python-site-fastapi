# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class ACAOEmpresaFinanceiroBPATrimestralModel(_database.session.Base):

    __tablename__ = "TBEMPRESA_FINAN_BPA_TRIMESTRAL"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    cod_cvm = _sql.Column('CD_CVM', _sql.String(6), nullable=True, index=True)
    ano_refer = _sql.Column('ANO_REFER', _sql.String(4), nullable=True, index=True)
    tri_refer = _sql.Column('TRI_REFER', _sql.String(6), nullable=True, index=True)
    vlr_ativo_total = _sql.Column('VLR_ATIVO_TOTAL', _sql.Float(29, 10), nullable=True)
    vlr_circulante = _sql.Column('VLR_CIRCULANTE', _sql.Float(29, 10), nullable=True)
    vlr_circulante_caixa = _sql.Column('VLR_CIRCULANTE_CAIXA', _sql.Float(29, 10), nullable=True)
    vlr_circulante_aplic_finan = _sql.Column('VLR_CIRCULANTE_APLIC_FINAN', _sql.Float(29, 10), nullable=True)
    vlr_circulante_contas_rec = _sql.Column('VLR_CIRCULANTE_CONTAS_REC', _sql.Float(29, 10), nullable=True)
    vlr_circulante_estoque = _sql.Column('VLR_CIRCULANTE_ESTOQUE', _sql.Float(29, 10), nullable=True)
    vlr_circulante_outros = _sql.Column('VLR_CIRCULANTE_OUTROS', _sql.Float(29, 10), nullable=True)
    vlr_nao_circulante = _sql.Column('VLR_NAO_CIRCULANTE', _sql.Float(29, 10), nullable=True)
    vlr_nao_circulante_longo_prazo = _sql.Column('VLR_NAO_CIRCULANTE_LONGO_PRAZO', _sql.Float(29, 10), nullable=True)
    vlr_nao_circulante_investimentos = _sql.Column('VLR_NAO_CIRCULANTE_INVESTIMENTOS', _sql.Float(29, 10), nullable=True)
    vlr_nao_circulante_imobilizado = _sql.Column('VLR_NAO_CIRCULANTE_IMOBILIZADO', _sql.Float(29, 10), nullable=True)
    vlr_nao_circulante_intangivel = _sql.Column('VLR_NAO_CIRCULANTE_INTANGIVEL', _sql.Float(29, 10), nullable=True)
    vlr_nao_circulante_outros = _sql.Column('VLR_NAO_CIRCULANTE_OUTROS', _sql.Float(29, 10), nullable=True)

    def __init__(self, id: int = None, cod_cvm: str = None, ano_refer: str = None, tri_refer: str = None, vlr_ativo_total: float = 0.0, vlr_circulante: float = 0.0,
                 vlr_circulante_caixa: float = 0.0, vlr_circulante_aplic_finan: float = 0.0, vlr_circulante_contas_rec: float = 0.0,
                 vlr_circulante_estoque: float = 0.0, vlr_circulante_outros: float = 0.0, vlr_nao_circulante: float = 0.0,
                 vlr_nao_circulante_longo_prazo: float = 0.0, vlr_nao_circulante_investimentos: float = 0.0, vlr_nao_circulante_imobilizado: float = 0.0,
                 vlr_nao_circulante_intangivel: float = 0.0, vlr_nao_circulante_outros: float = 0.0):
        self.id = id
        self.cod_cvm = cod_cvm
        self.ano_refer = ano_refer
        self.tri_refer = tri_refer
        self.vlr_ativo_total = vlr_ativo_total
        self.vlr_circulante = vlr_circulante
        self.vlr_circulante_caixa = vlr_circulante_caixa
        self.vlr_circulante_aplic_finan = vlr_circulante_aplic_finan
        self.vlr_circulante_contas_rec = vlr_circulante_contas_rec
        self.vlr_circulante_estoque = vlr_circulante_estoque
        self.vlr_circulante_outros = vlr_circulante_outros
        self.vlr_nao_circulante = vlr_nao_circulante
        self.vlr_nao_circulante_longo_prazo = vlr_nao_circulante_longo_prazo
        self.vlr_nao_circulante_investimentos = vlr_nao_circulante_investimentos
        self.vlr_nao_circulante_imobilizado = vlr_nao_circulante_imobilizado
        self.vlr_nao_circulante_intangivel = vlr_nao_circulante_intangivel
        self.vlr_nao_circulante_outros = vlr_nao_circulante_outros

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<ACAOEmpresaFinanceiroBPATrimestral {str(self.id)}>'

