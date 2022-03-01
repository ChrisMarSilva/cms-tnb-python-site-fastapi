# -*- coding: utf-8 -*-


class UsuarioCeiProv():

    tablename = "TBCEI_PROV_USER_"

    def __init__(self, id: int = None, id_usuario: int = None, tipo: str = None, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.situacao = situacao


    @classmethod
    def descricao_tipo(cls, tipo: str = '') -> str:
        if tipo == 'B':
            return 'Bonificação'
        elif tipo == 'D':
            return 'DIVIDENDOS'
        elif tipo == 'E':
            return 'Desdobramento'
        elif tipo == 'F':
            return 'Rendimento'
        elif tipo == 'G':
            return 'Grupamento'
        elif tipo == 'J':
            return 'JRS CAP PRÓPRIO'
        elif tipo == 'R':
            return 'REST CAP DIN'
        elif tipo == 'S':
            return 'Subscrição'
        return 'DESCONHECIDO'

    @classmethod
    def descricao_situacao(cls, situacao: str = '') -> str:
        if situacao == 'I':
            return 'Importado'
        elif situacao == 'L':
            return 'Lançado'
        elif situacao == 'C':
            return 'Conferido'
        return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioCeiProv {str(self.id)}>'
