# -*- coding: utf-8 -*-


class UsuarioCeiOperModel():

    tablename = "TBCEI_OPER_USER_"

    def __init__(self, id: int = None, id_usuario: int = None, tipo: str = None, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.situacao = situacao

    @classmethod
    def descricao_tipo(cls, tipo: str = '') -> str:
        if tipo == 'C':
            return 'Compra'
        elif tipo == 'V':
            return 'Venda'
        return 'Desconhecido'

    @classmethod
    def descricao_situacao(cls, situacao: str = '') -> str:
        if situacao == 'I':
            return 'Importada'
        elif situacao == 'L':
            return 'Lançada'
        elif situacao == 'C':
            return 'Conferida'
        return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioCeiOper {str(self.id)}>'

