# -*- coding: utf-8 -*-
import sqlalchemy as _sql
import src.database as _database


class ACAOEmpresaFinanceiroBPPTrimestralModel(_database.session.Base):

    __tablename__ = "TBEMPRESA_FINAN_BPP_TRIMESTRAL"

    id = _sql.Column('ID', _sql.Integer, primary_key=True, autoincrement=True)
    cod_cvm = _sql.Column('CD_CVM', _sql.String(6), nullable=True, index=True)
    ano_refer = _sql.Column('ANO_REFER', _sql.String(4), nullable=True, index=True)
    tri_refer = _sql.Column('TRI_REFER', _sql.String(6), nullable=True, index=True)
    vlr_passivo_total = _sql.Column('VLR_PASSIVO_TOTAL', _sql.Float(29, 10), nullable=True)
    vlr_circulante = _sql.Column('VLR_CIRCULANTE', _sql.Float(29, 10), nullable=True)
    vlr_circulante_salarios = _sql.Column('VLR_CIRCULANTE_SALARIOS', _sql.Float(29, 10), nullable=True)
    vlr_circulante_fornecedores = _sql.Column('VLR_CIRCULANTE_FORNECEDORES', _sql.Float(29, 10), nullable=True)
    vlr_circulante_emprestimos = _sql.Column('VLR_CIRCULANTE_EMPRESTIMOSS', _sql.Float(29, 10), nullable=True)
    vlr_circulante_outros = _sql.Column('VLR_CIRCULANTE_OUTROS', _sql.Float(29, 10), nullable=True)
    vlr_nao_circulante = _sql.Column('VLR_NAO_CIRCULANTE', _sql.Float(29, 10), nullable=True)
    vlr_nao_circulante_emprestimos = _sql.Column('VLR_NAO_CIRCULANTE_EMPRESTIMOSS', _sql.Float(29, 10), nullable=True)
    vlr_nao_circulante_outros = _sql.Column('VLR_NAO_CIRCULANTE_OUTROS', _sql.Float(29, 10), nullable=True)
    vlr_patrimonio_liquido_consolidado = _sql.Column('VLR_PATRIMONIO_LIQUIDO_CONSOLIDADO', _sql.Float(29, 10), nullable=True)
    vlr_patrimonio_capital_social_realizado = _sql.Column('VLR_PATRIMONIO_CAPITAL_SOCIAL_REALIZADO', _sql.Float(29, 10), nullable=True)
    vlr_patrimonio_lucro_prejuizo_acumulado = _sql.Column('VLR_PATRIMONIO_LUCRO_PREJUIZO_ACUMULADO', _sql.Float(29, 10), nullable=True)
    vlr_patrimonio_reserva_capital = _sql.Column('VLR_PATRIMONIO_RESERVA_CAPITAL', _sql.Float(29, 10), nullable=True)
    vlr_patrimonio_reserva_lucros = _sql.Column('VLR_PATRIMONIO_RESERVA_LUCROS', _sql.Float(29, 10), nullable=True)
    vlr_patrimonio_participacoes = _sql.Column('VLR_PATRIMONIO_PARTICIPACAO_NAO_CONTROLADORES', _sql.Float(29, 10), nullable=True)
    vlr_patrimonio_outros = _sql.Column('VLR_PATRIMONIO_OUTROS', _sql.Float(29, 10), nullable=True)

    def __init__(self, id: int = None, cod_cvm: str = None, ano_refer: str = None, tri_refer: str = None, vlr_passivo_total: float = 0.0, vlr_circulante: float = 0.0,
                 vlr_circulante_salarios: float = 0.0, vlr_circulante_fornecedores: float = 0.0, vlr_circulante_emprestimos: float = 0.0,
                 vlr_circulante_outros: float = 0.0, vlr_nao_circulante: float = 0.0, vlr_nao_circulante_emprestimos: float = 0.0,
                 vlr_nao_circulante_outros: float = 0.0, vlr_patrimonio_liquido_consolidado: float = 0.0, vlr_patrimonio_capital_social_realizado: float = 0.0,
                 vlr_patrimonio_lucro_prejuizo_acumulado: float = 0.0, vlr_patrimonio_reserva_capital: float = 0.0, vlr_patrimonio_reserva_lucros: float = 0.0,
                 vlr_patrimonio_participacoes: float = 0.0, vlr_patrimonio_outros: float = 0.0):
        self.id = id
        self.cod_cvm = cod_cvm
        self.ano_refer = ano_refer
        self.tri_refer = tri_refer
        self.vlr_passivo_total = vlr_passivo_total
        self.vlr_circulante = vlr_circulante
        self.vlr_circulante_salarios = vlr_circulante_salarios
        self.vlr_circulante_fornecedores = vlr_circulante_fornecedores
        self.vlr_circulante_emprestimos = vlr_circulante_emprestimos
        self.vlr_circulante_outros = vlr_circulante_outros
        self.vlr_nao_circulante = vlr_nao_circulante
        self.vlr_nao_circulante_emprestimos = vlr_nao_circulante_emprestimos
        self.vlr_nao_circulante_outros = vlr_nao_circulante_outros
        self.vlr_patrimonio_liquido_consolidado = vlr_patrimonio_liquido_consolidado
        self.vlr_patrimonio_capital_social_realizado = vlr_patrimonio_capital_social_realizado
        self.vlr_patrimonio_lucro_prejuizo_acumulado = vlr_patrimonio_lucro_prejuizo_acumulado
        self.vlr_patrimonio_reserva_capital = vlr_patrimonio_reserva_capital
        self.vlr_patrimonio_reserva_lucros = vlr_patrimonio_reserva_lucros
        self.vlr_patrimonio_participacoes = vlr_patrimonio_participacoes
        self.vlr_patrimonio_outros = vlr_patrimonio_outros

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<ACAOEmpresaFinanceiroBPPTrimestral {str(self.id)}>'

