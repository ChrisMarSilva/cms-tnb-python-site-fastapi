# -*- coding: utf-8 -*-


class ACAOEmpresaAtivoCotacaoHistModel():

    @staticmethod
    def get_table_name(categoria: str, codigo: str) -> str:
        if categoria == 'ACAO': return 'TBEMPRESA_ATIVOCOTACAO_' + codigo
        if categoria == 'FII': return 'TBFII_FUNDOIMOB_COTACAO_' + codigo
        if categoria == 'ETF': return 'TBETF_INDICE_COTACAO_' + codigo
        if categoria == 'BDR': return 'TTBBDR_EMPRESA_COTACAO_' + codigo
        if categoria == 'CRIPTO': return 'TBCRIPTO_EMPRESA_COTACAO_' + codigo
        return ""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<ACAOEmpresaAtivoCotacaoHist {str(self.id)}>'

