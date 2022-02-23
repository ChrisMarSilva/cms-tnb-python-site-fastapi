# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str


class UsuarioCarteiraProjecaoItem(db.Model):

    __tablename__ = "TBCARTEIRA_PROJECAO_ITEM"

    id_projecao = db.Column('IDPROJECAO', db.Integer, db.ForeignKey('TBCARTEIRA_PROJECAO.ID'), primary_key=True, nullable=False, index=True)
    numero = db.Column('NUMERO', db.Integer, primary_key=True, nullable=False, index=True)
    ano = db.Column('ANO', db.Integer, nullable=False)
    mes = db.Column('MES', db.Integer, nullable=False)
    vlr_invest_ini = db.Column('VLRINVESTINI', db.Float(17, 2), nullable=True)
    vlr_invest_mes = db.Column('VLRINVESTMES', db.Float(17, 2), nullable=True)
    vlr_invest_fim = db.Column('VLRINVESTFIM', db.Float(17, 2), nullable=True)
    rend_messal = db.Column('RENDMENSAL', db.Float(5, 2), nullable=True)
    tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

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

    @classmethod
    def get_all(cls):
        try:
            return cls.query.all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_by_projecao(cls, id_projecao: int):
        try:
            return cls.query.filter_by(id_projecao=id_projecao).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int, id_projecao: int = None, situacao: str = None):
        query = """ SELECT ITEM.IDPROJECAO    AS IDPROJECAO, 
                           PROJ.DESCRICAO     AS DESCRICAOPROJECAO, 
                           ITEM.NUMERO        AS NUMERO,
                           ITEM.ANO           AS ANO,
                           ITEM.MES           AS MES,
                           ITEM.VLRINVESTINI  AS VLRINVESTINI,
                           ITEM.VLRINVESTMES  AS VLRINVESTMES,
                           ITEM.VLRINVESTFIM  AS VLRINVESTFIM,
                           ITEM.RENDMENSAL    AS RENDMENSAL,
                           ITEM.TIPO          AS TIPO,
                           ITEM.SITUACAO      AS SITUACAO 
                    FROM TBCARTEIRA_PROJECAO_ITEM    ITEM
                      INNER JOIN TBCARTEIRA_PROJECAO PROJ  ON ( PROJ.ID  = ITEM.IDPROJECAO )
                    WHERE PROJ.IDUSUARIO = :IDUSUARIO
                """
        if id_projecao: query += " AND ITEM.IDPROJECAO = :IDPROJECAO "
        if situacao: query += " AND ITEM.SITUACAO = :SITUACAO "
        query += " ORDER BY ITEM.IDPROJECAO, ITEM.NUMERO "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if id_projecao: params['IDPROJECAO'] = id_projecao
        if situacao: params['SITUACAO'] = situacao

        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_carteira_projecao(cls, id_usuario: int, id_projecao: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_PROJECAO_ITEM WHERE IDPROJECAO = :IDPROJECAO AND IDPROJECAO IN (SELECT ID FROM TBCARTEIRA_PROJECAO PROJ WHERE PROJ.IDUSUARIO = :IDUSUARIO) """
            params = {'IDPROJECAO': id_projecao, 'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = """ DELETE FROM TBCARTEIRA_PROJECAO_ITEM WHERE IDPROJECAO IN (SELECT ID FROM TBCARTEIRA_PROJECAO PROJ WHERE PROJ.IDUSUARIO = :IDUSUARIO) """
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
            if commit:
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise

    def excluir(self, commit: bool = True):
        try:
            db.session.delete(self)
            if commit:
                db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise

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
