# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioApuracao(db.Model):

    __tablename__ = "TBAPURACAO"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    tipo = db.Column('TIPO', db.String(1), nullable=False)
    categoria = db.Column('CATEGORIA', db.String(1), nullable=False)
    ano_mes = db.Column('MESANO', db.String(6), nullable=False, index=True)
    valor = db.Column('VALOR', db.Float(17, 2), nullable=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, tipo: str = None, categoria: str = None,
                 ano_mes: str = None, valor: float = 0.0, situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.tipo = tipo
        self.categoria = categoria
        self.ano_mes = ano_mes
        self.valor = valor
        self.situacao = situacao

    @classmethod
    def get_all(cls, id_usuario: int, tipo: str = None, categoria: str = None, ano_mes: str = None):
        filters = []
        filters.append(cls.id_usuario == id_usuario)
        if tipo: filters.append(cls.tipo == tipo)
        if categoria: filters.append(cls.categoria == categoria)
        if ano_mes: filters.append(cls.ano_mes == ano_mes)
        try:
            return cls.query.filter(*filters).order_by(cls.ano_mes, cls.tipo, cls.categoria).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_all_by_usuario(cls, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_id(cls, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_menor_ano(cls, id_usuario: int = None):
        try:
            return db.session.query(db.func.min(cls.ano_mes)).filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_maior_ano(cls, id_usuario: int = None):
        try:
            return db.session.query(db.func.max(cls.ano_mes)).filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int, tipo: str = None, categoria: str = None, ano_mes: str = None):
        query = """ SELECT AP.ID, AP.TIPO, AP.CATEGORIA, AP.MESANO, AP.VALOR, AP.SITUACAO FROM TBAPURACAO AP WHERE AP.IDUSUARIO = :IDUSUARIO """
        if tipo: query += " AND AP.TIPO = :TIPO "
        if categoria: query += " AND AP.CATEGORIA = :CATEGORIA "
        if ano_mes: query += " AND AP.MESANO = :MESANO "
        query += " ORDER BY AP.MESANO, AP.TIPO, AP.CATEGORIA "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        if categoria: params['CATEGORIA'] = categoria
        if ano_mes: params['MESANO'] = ano_mes
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_id(cls, id_usuario: int, id: int):
        query = """ SELECT AP.ID, AP.TIPO, AP.CATEGORIA, AP.MESANO, AP.VALOR, AP.SITUACAO FROM TBAPURACAO AP WHERE AP.IDUSUARIO = :IDUSUARIO AND AP.ID = :ID """
        params = {'IDUSUARIO': id_usuario, 'ID': id}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_menor_ano(cls, id_usuario: int, tipo: str = None, categoria: str = None):
        query = """ SELECT SUBSTRING(MIN(AP.MESANO), 1, 4) AS MENORANO FROM TBAPURACAO AP WHERE AP.IDUSUARIO = :IDUSUARIO """
        if tipo: query += " AND AP.TIPO = :TIPO  "
        if categoria: query += " AND AP.CATEGORIA = :CATEGORIA "
        params = {}
        params['IDUSUARIO'] = id_usuario
        if tipo: params['TIPO'] = tipo
        if categoria: params['CATEGORIA'] = categoria
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_ano(cls, id_usuario: int, tipo: str = None, categoria: str = None, ano: str = None, commit: bool = True):
        try:
            query = "DELETE FROM TBAPURACAO WHERE IDUSUARIO = :IDUSUARIO "
            if tipo: query += " AND TIPO = :TIPO  "
            if categoria: query += " AND CATEGORIA = :CATEGORIA "
            if ano: query += " AND MESANO >= :JANANO AND MESANO <= :DEZANO "

            params = {}
            params['IDUSUARIO'] = id_usuario
            if tipo: params['TIPO'] = tipo
            if categoria: params['CATEGORIA'] = categoria
            if ano:
                params['JANANO'] = ano + '01'
                params['DEZANO'] = ano + '12'

            db.session.execute(query, params)
            if commit: db.session.commit()

        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBAPURACAO WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def salvar(self, commit: bool = True):
        try:
            db.session.add(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def excluir(self, commit: bool = True):
        try:
            db.session.delete(self)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    def valor_format(self) -> str:
        return decimal_to_str(valor=self.valor)

    def data_format(self) -> str:
        return converter_datetime_str(data=converter_str_to_datetime(data=self.ano_mes+'01', fmt='%Y%m%d'), fmt='%d/%m/%Y')

    def tipo_descr(self) -> str:
        if self.tipo == 'N':
            return 'Normal'
        elif self.tipo == 'M':
            return 'Manual'
        else:
            return 'Desconhecido'

    def categoria_descr(self) -> str:
        if self.categoria == 'C': return 'Comum'
        elif self.categoria == 'D': return 'Day-Trade'
        elif self.categoria == 'F': return 'FII'
        elif self.categoria == 'E': return 'ETF-Comun'
        elif self.categoria == 'G': return 'ETF-Day-Trade'
        elif self.categoria == 'I': return 'BDR-Comun'
        elif self.categoria == 'J': return 'BDR-Day-Trade'
        else: return 'Desconhecido'

    def situacao_descr(self) -> str:
        if self.situacao == 'A': return 'Ativo'
        elif self.situacao == 'I': return 'Inativo'
        else: return 'Desconhecido'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioApuracao {str(self.id)}>'
