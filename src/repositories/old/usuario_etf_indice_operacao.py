# -*- coding: utf-8 -*-
import sys
import os
from app.banco import db
from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str, inteiro_to_str
from app.util.util_datahora import converter_str_to_datetime, converter_datetime_str


class UsuarioETFIndiceOperacao(db.Model):

    __tablename__ = "TBETF_OPERACAO"

    id = db.Column('ID', db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column('IDUSUARIO', db.Integer, db.ForeignKey('TBUSUARIO.ID'), nullable=False, index=True)
    id_indice = db.Column('IDINDICE', db.Integer, db.ForeignKey('TBETF_INDICE.ID'), nullable=False, index=True)
    id_corretora = db.Column('IDCORRETORA', db.Integer, db.ForeignKey('TBCORRETORA.ID'), nullable=True)
    id_lancamento = db.Column('IDLANC', db.Integer, db.ForeignKey('TBETF_LANCAMENTO.ID'), nullable=False, index=True)
    tipo = db.Column('TIPO', db.String(1), nullable=False, index=True)
    categoria = db.Column('CATEGORIA', db.String(1), nullable=False, index=True)
    data = db.Column('DATA', db.String(8), nullable=False, index=True)
    quant = db.Column('QUANT', db.Float(20, 10), nullable=False)
    quant_acumulado = db.Column('QUANTACUMULADO', db.Float(20, 10), nullable=True, index=True)
    vlr_custo = db.Column('VLRCUSTO', db.Float(20, 10), nullable=False)
    tot_vlr_custo = db.Column('TOTVLRCUSTO', db.Float(17, 2), nullable=True)
    vlr_preco_medio = db.Column('VLRPRECOMEDIO', db.Float(20, 10), nullable=True)
    tot_vlr_valorizacao = db.Column('TOTVLRVALORIZACAO', db.Float(17, 2), nullable=True)
    perc_valorizacao = db.Column('PERCVALORIZACAO', db.Float(17, 2), nullable=True)
    troca = db.Column('TROCA', db.String(1), nullable=True)
    situacao = db.Column('SITUACAO', db.String(1), nullable=False, index=True)

    def __init__(self, id: int = None, id_usuario: int = None, id_indice: int = None, id_corretora: int = None,
                 id_lancamento: int = None, tipo: str = None, categoria: str = None, data: str = None,
                 quant: float = 0.0, quant_acumulado: float = 0.0, vlr_custo: float = 0.0, tot_vlr_custo: float = 0.0,
                 vlr_preco_medio: float = 0.0, tot_vlr_valorizacao: float = 0.0, perc_valorizacao: float = 0.0,
                 troca: str = 'N', situacao: str = None):
        self.id = id
        self.id_usuario = id_usuario
        self.id_indice = id_indice
        self.id_corretora = id_corretora
        self.id_lancamento = id_lancamento
        self.tipo = tipo
        self.categoria = categoria
        self.data = data
        self.quant = quant
        self.quant_acumulado = quant_acumulado
        self.vlr_custo = vlr_custo
        self.tot_vlr_custo = tot_vlr_custo
        self.vlr_preco_medio = vlr_preco_medio
        self.tot_vlr_valorizacao = tot_vlr_valorizacao
        self.perc_valorizacao = perc_valorizacao
        self.troca = troca
        self.situacao = situacao

    @classmethod
    def get_all(cls, id_usuario: int = None, id_indice: int = None, dt_ini: str = None, dt_fim: str = None, categoria: str = None, tipo: str = None):
        try:

            filters = []
            if id_usuario: filters.append(cls.id_usuario == id_usuario)
            if id_indice: filters.append(cls.id_indice == id_indice)
            if dt_ini: filters.append(cls.data >= dt_ini)
            if dt_fim: filters.append(cls.data <= dt_fim)
            if categoria: filters.append(cls.categoria == categoria)
            if tipo: filters.append(cls.tipo == tipo)

            return cls.query.filter(*filters).order_by(cls.id).all()

        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def find_by_id(cls, id: int):
        try:
            return cls.query.filter_by(id=id).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def find_by_usuario(cls, id_usuario: int):
        try:
            return cls.query.filter_by(id_usuario=id_usuario).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def find_by_indice(cls, id_indice: int):
        try:
            return cls.query.filter_by(id_indice=id_indice).all()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_menor_ano(cls, id_usuario: int = None):
        try:
            return db.session.query(db.func.min(cls.data)).filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def get_maior_ano(cls, id_usuario: int = None):
        try:
            return db.session.query(db.func.max(cls.data)).filter_by(id_usuario=id_usuario).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_todos(cls, id_usuario: int = None, codigo: str = None, dt_ini: str = None, dt_fim: str = None, categoria: str = None, tipo: str = None, troca: str = None):

        query = """ SELECT O.ID, 
                           O.IDLANC, 
                           O.IDUSUARIO, 
                           O.IDINDICE     AS IDINDICE, 
                           A.CODIGO       AS CODIGOINDICE, 
                           A.SITUACAO     AS SITUACAOINDICE, 
                           O.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           O.TIPO, 
                           O.CATEGORIA, 
                           O.DATA, 
                           O.QUANT, 
                           O.QUANTACUMULADO, 
                           O.VLRCUSTO, 
                           O.TOTVLRCUSTO, 
                           O.VLRPRECOMEDIO, 
                           O.TOTVLRVALORIZACAO, 
                           O.PERCVALORIZACAO, 
                           O.TROCA, 
                           O.SITUACAO 
                    FROM TBETF_OPERACAO       O
                      INNER JOIN TBETF_INDICE A ON ( A.ID = O.IDINDICE    )
                      LEFT  JOIN TBCORRETORA  C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
                """

        if codigo: query += " AND A.CODIGO = :CODIGO "
        if dt_ini: query += " AND O.DATA >= :DATAINICIO "
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        if categoria: query += " AND O.CATEGORIA = :CATEGORIA "
        if tipo: query += " AND O.TIPO = :TIPO "
        if troca: query += " AND IFNULL(O.TROCA, 'N') = :TROCA "
        query += " ORDER BY O.DATA, O.CATEGORIA, O.TIPO, O.ID "

        params = {}
        params['IDUSUARIO'] = id_usuario
        if codigo: params['CODIGO'] = codigo
        if dt_ini: params['DATAINICIO'] = dt_ini
        if dt_fim: params['DATAFIM'] = dt_fim
        if categoria: params['CATEGORIA'] = categoria
        if tipo: params['TIPO'] = tipo
        if troca: params['TROCA'] = troca

        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise


    @classmethod
    def buscar_por_id(cls, id_usuario: int = None, id: int = None):
        query = """ SELECT O.ID, 
                           O.IDLANC, 
                           O.IDUSUARIO, 
                           O.IDINDICE     AS IDINDICE, 
                           A.CODIGO       AS CODIGOINDICE, 
                           A.SITUACAO     AS SITUACAOINDICE, 
                           O.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           O.TIPO, 
                           O.CATEGORIA, 
                           O.DATA, 
                           O.QUANT, 
                           O.QUANTACUMULADO, 
                           O.VLRCUSTO, 
                           O.TOTVLRCUSTO, 
                           O.VLRPRECOMEDIO, 
                           O.TOTVLRVALORIZACAO, 
                           O.PERCVALORIZACAO, 
                           O.TROCA, 
                           O.SITUACAO 
                    FROM TBETF_OPERACAO       O
                      INNER JOIN TBETF_INDICE A ON ( A.ID = O.IDINDICE    )
                      LEFT  JOIN TBCORRETORA  C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.ID        = :ID
                      AND O.IDUSUARIO = :IDUSUARIO
                """
        params = {'ID': id, 'IDUSUARIO': id_usuario}
        try:
            return db.session.execute(query, params).first()
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_por_codigo(cls, id_usuario: int = None, codigo: str = None):
        query = """ SELECT O.ID, 
                           O.IDLANC, 
                           O.IDUSUARIO, 
                           O.IDINDICE     AS IDINDICE, 
                           A.CODIGO       AS CODIGOINDICE, 
                           A.SITUACAO     AS SITUACAOINDICE, 
                           O.IDCORRETORA  AS IDCORRETORA, 
                           C.NOME         AS NOMECORRETORA, 
                           O.TIPO, 
                           O.CATEGORIA, 
                           O.DATA, 
                           O.QUANT, 
                           O.QUANTACUMULADO, 
                           O.VLRCUSTO, 
                           O.TOTVLRCUSTO, 
                           O.VLRPRECOMEDIO, 
                           O.TOTVLRVALORIZACAO, 
                           O.PERCVALORIZACAO, 
                           O.TROCA, 
                           O.SITUACAO 
                    FROM TBETF_OPERACAO       O
                      INNER JOIN TBETF_INDICE A ON ( A.ID = O.IDINDICE    )
                      LEFT  JOIN TBCORRETORA  C ON ( C.ID = O.IDCORRETORA )
                    WHERE O.IDUSUARIO = :IDUSUARIO
                      AND A.CODIGO    = :CODIGO
                    ORDER BY O.DATA, O.TIPO 
                """
        params = {'IDUSUARIO': id_usuario, 'CODIGO': codigo}
        try:
            return db.session.execute(query, params)
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_quant_ativo(cls, id_usuario: int = None):
        query = """ SELECT COUNT(1) AS QTDE FROM TBETF_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.SITUACAO = 'A' """
        params = {'IDUSUARIO': id_usuario}
        try:
            rows = db.session.execute(query, params).first()
            return int(rows[0]) if rows and rows[0] and int(rows[0]) > 0 else 0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_preco_medio(cls, id_usuario: int = None, id_indice: int = None, dt_fim: str = None):
        query = """ SELECT O.VLRPRECOMEDIO FROM TBETF_OPERACAO O WHERE O.ID = ( SELECT MAX(OO.ID) FROM TBETF_OPERACAO OO WHERE OO.IDUSUARIO = :IDUSUARIO and OO.IDINDICE = :IDINDICE AND OO.QUANTACUMULADO > 0 AND OO.SITUACAO = 'A' """
        if dt_fim: query += " AND OO.DATA <= :DATAFIM "
        query += " ) "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_preco_medio_antes(cls, id_usuario: int = None, id_indice: int = None, dt_fim: str = None):
        query = """ SELECT O.VLRPRECOMEDIO FROM TBETF_OPERACAO O WHERE O.ID = ( SELECT MAX(OO.ID) FROM TBETF_OPERACAO OO WHERE OO.IDUSUARIO = :IDUSUARIO and OO.IDINDICE = :IDINDICE AND OO.QUANTACUMULADO > 0 AND OO.SITUACAO = 'A' """
        if dt_fim: query += " AND OO.DATA < :DATAFIM "
        query += " ) "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_total_compra(cls, id_usuario: int = None, id_indice: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.QUANT) AS QTDE FROM TBETF_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDINDICE = :IDINDICE AND O.TIPO = 'C' """
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_total_bonus(cls, id_usuario: int = None, id_indice: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.QUANT) AS QTDE FROM TBETF_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDINDICE = :IDINDICE AND O.TIPO = 'B' """
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_total_venda(cls, id_usuario: int = None, id_indice: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.QUANT) AS QTDE FROM TBETF_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDINDICE = :IDINDICE AND O.TIPO = 'V' """
        if id_lanc: query += " AND O.ID <> :ID "
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if id_lanc: params['ID'] = id_lanc
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_valor_total_compra(cls, id_usuario: int = None, id_indice: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBETF_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDINDICE = :IDINDICE AND O.TIPO = 'C' """
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_valor_total_bonus(cls, id_usuario: int = None, id_indice: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBETF_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDINDICE = :IDINDICE AND O.TIPO = 'B' """
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def buscar_valor_total_venda(cls, id_usuario: int = None, id_indice: int = None, id_lanc: int = None, dt_fim: str = None):
        query = """ SELECT SUM(O.TOTVLRCUSTO) AS TOTVLRCUSTO FROM TBETF_OPERACAO O WHERE O.IDUSUARIO = :IDUSUARIO AND O.IDINDICE = :IDINDICE AND O.TIPO = 'V' """
        if id_lanc: query += " AND O.ID <> :ID "
        if dt_fim: query += " AND O.DATA <= :DATAFIM "
        params = {}
        params['IDUSUARIO'] = id_usuario
        params['IDINDICE'] = id_indice
        if id_lanc: params['ID'] = id_lanc
        if dt_fim: params['DATAFIM'] = dt_fim
        try:
            rows = db.session.execute(query, params).first()
            return float(rows[0]) if rows and rows[0] and rows[0] > 0.0 else 0.0
        except Exception as e:
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def resetar_ativos(cls, id_usuario: int, id_indice: int, commit: bool = True):
        try:
            query = "DELETE FROM TBETF_OPERACAO WHERE IDINDICE = :IDINDICE AND IDUSUARIO = :IDUSUARIO "
            params = {'IDUSUARIO': id_usuario, 'IDINDICE': id_indice}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo_indice(cls, id_usuario: int, id_indice: int, commit: bool = True):
        try:
            query = "DELETE FROM TBETF_OPERACAO WHERE IDINDICE = :IDINDICE AND IDUSUARIO = :IDUSUARIO"
            params = {'IDINDICE': id_indice, 'IDUSUARIO': id_usuario}
            db.session.execute(query, params)
            if commit: db.session.commit()
        except Exception as e:
            db.session.rollback()
            LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    def excluir_tudo(cls, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBETF_OPERACAO WHERE IDUSUARIO = :IDUSUARIO"
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

    def calc_preco_medio(self, qtde_atual: float = 0.0, preco_medio_atual: float = 0.0):
        self.vlr_preco_medio = 0.0
        if str(self.tipo) == 'C' or str(self.tipo) == 'B':
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

    def quant_acumulado_format(self) -> str:
        return inteiro_to_str(valor=self.quant_acumulado)

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

    def categoria_descr(self) -> str:
        return self.descricao_categoria(categoria=self.categoria)

    def situacao_descr(self) -> str:
        return self.descricao_situacao(situacao=self.situacao)

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
        elif tipo == 'B': return 'Bonificação'
        elif tipo == 'D': return 'Desdobramento'
        elif tipo == 'G': return 'Grupamento'
        elif tipo == 'P': return 'Projetado'
        else: return 'Desconhecido'

    @classmethod
    def descricao_categoria(cls, categoria: str) -> str:
        if categoria == 'C':
            return 'Comum'
        elif categoria == 'D':
            return 'Day-Trade'
        else:
            return 'Desconhecida'

    @classmethod
    def descricao_situacao(cls, situacao: str) -> str:
        if situacao == 'A':
            return 'Ativo'
        elif situacao == 'F':
            return 'Finalizada'
        else:
            return 'Desconhecida'

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass

    def __repr__(self):
        return '<UsuarioEmpresaOperacao {str(self.id)}>'
