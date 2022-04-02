# -*- coding: utf-8 -*-
import sys
import os
import datetime as dt
import time
import asyncio
from threading import Thread
import sqlalchemy.orm as _orm
from src.models.acao_empresa_ativo import ACAOEmpresaAtivoModel
from src.models.fii_fundoimob import FiiFundoImobModel
from src.models.etf_indice import ETFIndiceModel
from src.models.bdr_empresa import BDREmpresaModel
from src.models.cripto_empresa import CriptoEmpresaModel
from src.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamentoModel
from src.models.usuario_acao_empresa_operacao import UsuarioACAOEmpresaOperacaoModel
from src.models.usuario_fii_fundoimob_lancamento import UsuarioFiiFundoImobLancamentoModel
from src.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamentoModel
from src.models.usuario_etf_indice_operacao import UsuarioETFIndiceOperacaoModel
from src.models.usuario_bdr_empresa_lancamento import UsuarioBDREmpresaLancamentoModel
from src.models.usuario_bdr_empresa_operacao import UsuarioBDREmpresaOperacaoModel
from src.models.usuario_cripto_lancamento import UsuarioCriptoLancamentoModel
from src.models.usuario_carteira import UsuarioCarteiraModel
from src.models.usuario_carteira_acao import UsuarioCarteiraAcaoModel
from src.models.usuario_carteira_fii import UsuarioCarteiraFiiModel
from src.models.usuario_carteira_etf import UsuarioCarteiraEtfModel
from src.models.usuario_carteira_bdr import UsuarioCarteiraBdrModel
from src.models.usuario_carteira_cripto import UsuarioCarteiraCriptoModel
# # from app.models.log_erro import LogErro


class UsuarioCarteiraRepository:

    @classmethod
    async def zerar(cls, db: _orm.Session, id_usuario: int, codigo: str = None) -> None:
        try:
            params = {'IDUSUARIO': id_usuario}

            db.execute(" DELETE FROM TBAPURACAO_CALCULADA WHERE IDUSUARIO = :IDUSUARIO ", params)

            db.execute(" UPDATE TBCARTEIRA_ATIVO SET QUANT = 0, QUANTBONUS = 0, VLRPRECOMEDIO = 0.00, SITUACAO = 'F' WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) ", params)
            db.execute(" UPDATE TBLANCAMENTO     SET QUANTPEND = QUANT, SITUACAO = 'P' WHERE IDUSUARIO = :IDUSUARIO ", params)
            db.execute(" DELETE FROM TBOPERACAO WHERE IDUSUARIO = :IDUSUARIO ", params)

            db.execute(" UPDATE TBCARTEIRA_FUNDO SET QUANT = 0, QUANTBONUS = 0, VLRPRECOMEDIO = 0.00, SITUACAO = 'F' WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) ", params)
            db.execute(" UPDATE TBFII_LANCAMENTO SET QUANT = QUANTORIG, TOTVLRCUSTO = 0.00, VLRPRECOMEDIO = 0.00, TOTVLRVALORIZACAO = 0.00, PERCVALORIZACAO = 0.00, SITUACAO = 'P' WHERE IDUSUARIO = :IDUSUARIO ", params)

            db.execute(" UPDATE TBCARTEIRA_INDICE SET QUANT = 0, QUANTBONUS = 0, VLRPRECOMEDIO = 0.00, SITUACAO = 'F' WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) ", params)
            db.execute(" UPDATE TBETF_LANCAMENTO  SET QUANTPEND = QUANT, SITUACAO = 'P' WHERE IDUSUARIO = :IDUSUARIO ", params)
            db.execute(" DELETE FROM TBETF_OPERACAO WHERE IDUSUARIO = :IDUSUARIO ", params)

            db.execute(" UPDATE TBCARTEIRA_BDR    SET QUANT = 0, QUANTBONUS = 0, VLRPRECOMEDIO = 0.00, SITUACAO = 'F' WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) ", params)
            db.execute(" UPDATE TBBDR_LANCAMENTO  SET QUANTPEND = QUANT, SITUACAO = 'P' WHERE IDUSUARIO = :IDUSUARIO ", params)
            db.execute(" DELETE FROM TBBDR_OPERACAO WHERE IDUSUARIO = :IDUSUARIO ", params)

            db.execute(" UPDATE TBCARTEIRA_CRIPTO   SET QUANT = 0, VLRPRECOMEDIO = 0.00, SITUACAO = 'F' WHERE IDCARTEIRA IN ( SELECT ID FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO ) ", params)
            db.execute(" UPDATE TBCRIPTO_LANCAMENTO SET QUANT = QUANTORIG, TOTVLRCUSTO = 0.00, VLRPRECOMEDIO = 0.00, TOTVLRVALORIZACAO = 0.00, PERCVALORIZACAO = 0.00, SITUACAO = 'P' WHERE IDUSUARIO = :IDUSUARIO ", params)

            db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            pass

    @classmethod
    async def gerar(cls, db: _orm.Session, id_usuario: int, codigo: str = None) -> None:
        try:

            # print(dt.datetime.now(), 'UsuarioCarteira - Gerar - ASYNC - INICIO')
            # start = time.time()

            # id_carteira = cls.__gerar_default(id_usuario=id_usuario)
            # cls.__gerar_acao(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)
            # cls.__gerar_fii(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)
            # cls.__gerar_etf(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)
            # cls.__gerar_bdr(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)
            # cls.__gerar_cripto(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)

            id_carteira = cls.__gerar_default(id_usuario=id_usuario)

            loop = asyncio.new_event_loop() # get_event_loop
            try:
                asyncio.set_event_loop(loop)
                # loop.run_until_complete(teste_01())
                tasks = [asyncio.Task(cls.__gerar_acao(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)),
                         asyncio.Task(cls.__gerar_fii(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)),
                         asyncio.Task(cls.__gerar_etf(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)),
                         asyncio.Task(cls.__gerar_bdr(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)),
                         asyncio.Task(cls.__gerar_cripto(id_carteira=id_carteira, id_usuario=id_usuario, codigo=codigo)),
                         ]
                loop.run_until_complete(asyncio.gather(*tasks))
            finally:
                loop.close()

            #diff = int((time.time() - start) * 1000)
            #print(dt.datetime.now(), 'UsuarioCarteira - Gerar - ASYNC - FIM =', diff)

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            pass


    @classmethod
    async def __gerar_default(cls, db: _orm.Session, id_usuario: int) -> int:
        try:

            carteira = UsuarioCarteiraModel.buscar_por_tipo_default(id_usuario=id_usuario)
            if carteira:
                return int(carteira['ID'])

            carteira = UsuarioCarteiraModel()
            carteira.id_usuario = id_usuario
            carteira.descricao = 'Meu Portfólio'
            carteira.tipo = 'D'  # D-Default
            carteira.situacao = 'A'  # A-Ativo
            carteira.salvar()

            return int(carteira.id)

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise


    @classmethod
    @asyncio.coroutine
    async def __gerar_acao(cls, db: _orm.Session, id_carteira: int, id_usuario: int, codigo: str = None) -> None:
        try:

            # print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_acao - INICIO')

            rows = ACAOEmpresaAtivoModel.buscar_pendentes_situacao(id_usuario=id_usuario, codigo=codigo)
            for row in rows:
                codigo = str(row['CODIGO'])
                id_ativo = int(row['ID'])
                cls.__gerar_acao_oper_day_trade(id_usuario=id_usuario, codigo=codigo)
                cls.__gerar_acao_oper_comum(id_usuario=id_usuario, codigo=codigo)
                cls.__calc_acao_preco_medio_day_trade(id_usuario=id_usuario, id_ativo=id_ativo, codigo=codigo)
                qtde_compra, qtde_bonus, qtde_venda, preco_medio = cls.__calc_acao_preco_medio_comum(id_usuario=id_usuario, id_ativo=id_ativo, codigo=codigo)
                cls.__gerar_acao_carteira_ativo(id_carteira=id_carteira, id_usuario=id_usuario, id_ativo=id_ativo, codigo=codigo, qtde_compra=qtde_compra, qtde_bonus=qtde_bonus, qtde_venda=qtde_venda, preco_medio=preco_medio)

            # await asyncio.sleep(20)
            # print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_acao - FIM')

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_acao_oper_day_trade(cls, db: _orm.Session, id_usuario: int, codigo: str) -> None:
        try:

            rows = UsuarioACAOEmpresaLancamento.buscar_lista_datas_day_trade(id_usuario=id_usuario, codigo=str(codigo))
            for row in rows:
                dt_lanc = str(row['DATA'])

                lista_compras = UsuarioACAOEmpresaLancamento.buscar_por_data(id_usuario=id_usuario, codigo=str(codigo), data=str(dt_lanc), tipo='C') # C-Compra
                for lanc_compra in lista_compras:
                    compra_id_lanc = str(lanc_compra['ID'])
                    compra_id_ativo = int(lanc_compra['IDATIVO'])
                    compra_id_corretora = int(lanc_compra['IDCORRETORA']) if lanc_compra['IDCORRETORA'] else None
                    compra_quant = int(lanc_compra['QUANT']) if lanc_compra['QUANT'] else 0
                    compra_quant_pend = int(lanc_compra['QUANTPEND']) if lanc_compra['QUANTPEND'] else 0
                    compra_vlr_custo = float(lanc_compra['VLRCUSTO']) if lanc_compra['VLRCUSTO'] else 0.0
                    compra_troca = str(lanc_compra['TROCA']) if lanc_compra['TROCA'] else 'N'

                    lista_vendas = UsuarioACAOEmpresaLancamento.buscar_por_data(id_usuario=id_usuario, codigo=str(codigo), data=str(dt_lanc), tipo='V')  # V-Venda
                    for lanc_venda in lista_vendas:
                        venda_id_lanc = str(lanc_venda['ID'])
                        venda_id_ativo = int(lanc_venda['IDATIVO'])
                        venda_id_corretora = int(lanc_venda['IDCORRETORA']) if lanc_venda['IDCORRETORA'] else None
                        venda_quant = int(lanc_venda['QUANT']) if lanc_venda['QUANT'] else 0
                        venda_quant_pend = int(lanc_venda['QUANTPEND']) if lanc_venda['QUANTPEND'] else 0
                        venda_vlr_custo = float(lanc_venda['VLRCUSTO']) if lanc_venda['VLRCUSTO'] else 0.0
                        venda_troca = str(lanc_venda['TROCA']) if lanc_venda['TROCA'] else 'N'

                        if int(venda_quant_pend) == int(compra_quant):  # venda 100 = Compra 100
                            compra_quant = 0.0
                            oper = UsuarioACAOEmpresaOperacao(id_usuario=id_usuario)
                            oper.id_ativo = int(compra_id_ativo)
                            oper.id_corretora = compra_id_corretora
                            oper.id_lancamento = int(compra_id_lanc)
                            oper.tipo = 'C' # C-Compra
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(compra_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = compra_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            oper = UsuarioACAOEmpresaOperacao(id_usuario=id_usuario)
                            oper.id_ativo = int(venda_id_ativo)
                            oper.id_corretora = venda_id_corretora
                            oper.id_lancamento = int(venda_id_lanc)
                            oper.tipo = 'V' # V-Venda
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(venda_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = venda_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            UsuarioACAOEmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(compra_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            UsuarioACAOEmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(venda_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            break  # Finaliza Loop lancVenda

                        elif int(venda_quant_pend) < int(compra_quant): # venda 100 < Compra 200
                            compra_quant -= int(venda_quant_pend)

                            oper = UsuarioACAOEmpresaOperacao(id_usuario=id_usuario)
                            oper.id_ativo = int(compra_id_ativo)
                            oper.id_corretora = compra_id_corretora
                            oper.id_lancamento = int(compra_id_lanc)
                            oper.tipo = 'C'  # C-Compra
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = int(compra_quant_pend) - int(venda_quant_pend)
                            oper.vlr_custo = float(compra_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = compra_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            oper = UsuarioACAOEmpresaOperacao(id_usuario=id_usuario)
                            oper.id_ativo = int(venda_id_ativo)
                            oper.id_corretora = venda_id_corretora
                            oper.id_lancamento = int(venda_id_lanc)
                            oper.tipo = 'V' # V-Venda
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(venda_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = venda_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            UsuarioACAOEmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(compra_id_lanc), qtd_pend=int(compra_quant_pend) - int(venda_quant_pend), situacao='A')  # A-Ativo
                            UsuarioACAOEmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(venda_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            venda_quant_pend = 0

                        if int(venda_quant_pend) > int(compra_quant):  # venda 200 > Compra 100
                            compra_quant = 0.0

                            oper = UsuarioACAOEmpresaOperacao(id_usuario=id_usuario)
                            oper.id_ativo = int(compra_id_ativo)
                            oper.id_corretora = compra_id_corretora
                            oper.id_lancamento = int(compra_id_lanc)
                            oper.tipo = 'C' # C-Compra
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(compra_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(compra_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = compra_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            oper = UsuarioACAOEmpresaOperacao(id_usuario=id_usuario)
                            oper.id_ativo = int(venda_id_ativo)
                            oper.id_corretora = venda_id_corretora
                            oper.id_lancamento = int(venda_id_lanc)
                            oper.tipo = 'V' # V-Venda
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(compra_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(venda_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = venda_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            UsuarioACAOEmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(compra_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            UsuarioACAOEmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(venda_id_lanc), qtd_pend=int(venda_quant_pend) - int(compra_quant_pend), situacao='A')  # A-Ativo
                            break  # Finaliza Loop lancVenda

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_acao_oper_comum(cls, db: _orm.Session, id_usuario: int, codigo: str) -> None:
        try:

            lancs = UsuarioACAOEmpresaLancamento.buscar_por_qtde_pend_maior_que_zero(id_usuario=id_usuario, codigo=str(codigo))

            rows = UsuarioACAOEmpresaLancamento.buscar_desdobro_grupamento(id_usuario=id_usuario, codigo=str(codigo))
            lista_desdobro_grupamento = [{'DATA': str(row['DATA']), 'TIPO': str(row['TIPO']), 'QUANT': float(row['QUANT']), 'ID': int(row['ID'])} for row in rows]

            for lanc in lancs:

                id_lanc = str(lanc['ID'])
                id_ativo = int(lanc['IDATIVO'])
                id_corretora = int(lanc['IDCORRETORA']) if lanc['IDCORRETORA'] else None
                dt_lanc = str(lanc['DATA'])
                quant_pend = int(lanc['QUANTPEND']) if lanc['QUANTPEND'] else 0
                tipo = str(lanc['TIPO'])
                vlr_custo = float(lanc['VLRCUSTO']) if lanc['VLRCUSTO'] else 0.0
                troca = str(lanc['TROCA']) if lanc['TROCA'] else 'N'

                oper = UsuarioACAOEmpresaOperacao(id_usuario=id_usuario)
                oper.id_ativo = int(id_ativo)
                oper.id_corretora = id_corretora
                oper.id_lancamento = int(id_lanc)
                oper.tipo = str(tipo)
                oper.categoria = "C"  # C-Comum
                oper.data = str(dt_lanc)
                oper.quant = int(quant_pend)
                oper.quant_acumulado = 0.0
                oper.vlr_custo = float(vlr_custo)
                oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                oper.vlr_preco_medio = 0.0
                oper.tot_vlr_valorizacao = 0.0
                oper.perc_valorizacao = 0.0
                oper.troca = troca
                oper.situacao = "A"  # A-Ativa

                for item in lista_desdobro_grupamento:
                    if str(oper.data) < str(item['DATA']):
                        if str(str(item['TIPO'])) == 'D':
                            oper.quant = float(oper.quant) * float(item['QUANT'])
                            oper.vlr_custo = float(oper.vlr_custo) / float(item['QUANT'])
                        elif str(str(item['TIPO'])) == 'G':
                            oper.quant = float(oper.quant) / float(item['QUANT'])
                            oper.vlr_custo = float(oper.vlr_custo) * float(item['QUANT'])
                        oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                    UsuarioACAOEmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(item['ID']), qtd_pend=0, situacao='A')  # A-Ativo

                oper.salvar()

                UsuarioACAOEmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(id_lanc), qtd_pend=0, situacao='A')  # A-Ativo

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __calc_acao_preco_medio_day_trade(cls, db: _orm.Session, id_usuario: int, id_ativo: int, codigo: str) -> None:
        try:

            rows = UsuarioACAOEmpresaOperacao.get_all(id_usuario=id_usuario, id_ativo=int(id_ativo), categoria='D')  # D-DayTarde
            dt_atual = ""
            qtde_atual = 0.0
            preco_medio_atual = 0.0
            for row in rows:
                if str(dt_atual) != str(row.data):
                    dt_atual = str(row.data)
                    qtde_atual = 0.0
                    preco_medio_atual = 0.0
                qtde_atual, preco_medio_atual = row.calc_preco_medio(qtde_atual=float(qtde_atual), preco_medio_atual=float(preco_medio_atual))
                if str(row.tipo) == 'V' or str(row.tipo) == 'P':
                    row.calc_vlr_valorizacao()
                    row.calc_perc_valorizacao()
                row.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __calc_acao_preco_medio_comum(cls, db: _orm.Session, id_usuario: int, id_ativo: int, codigo: str):
        try:

            qtde_atual, preco_medio_atual, vlr_tot_bonus, qtde_compra, qtde_bonus, qtde_venda, preco_medio = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

            rows = UsuarioACAOEmpresaOperacao.get_all(id_usuario=id_usuario, id_ativo=int(id_ativo), categoria='C')  # C-Comun
            for row in rows:

                qtde_atual, preco_medio_atual = row.calc_preco_medio(qtde_atual=float(qtde_atual), preco_medio_atual=float(preco_medio_atual))
                preco_medio = preco_medio_atual
                row.quant_acumulado = float(qtde_atual)

                if str(row.tipo) == 'C':
                    qtde_compra += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                elif str(row.tipo) == 'B':
                    qtde_bonus += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                    vlr_tot_bonus += float(row.tot_vlr_custo) if row.tot_vlr_custo and row.tot_vlr_custo > 0.0 else 0.0
                elif str(row.tipo) == 'V' or str(row.tipo) == 'P':
                    row.calc_vlr_valorizacao()
                    row.tot_vlr_valorizacao += float(vlr_tot_bonus)
                    row.calc_perc_valorizacao()
                    qtde_venda += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                    if float(qtde_compra) + float(qtde_bonus) == float(qtde_venda):
                        qtde_compra, qtde_bonus, qtde_venda, preco_medio, vlr_tot_bonus = 0.0, 0.0, 0.0, 0.0, 0.0
                    if float(qtde_atual) == 0.0:
                        vlr_tot_bonus = 0.0

                row.salvar()

            return qtde_compra, qtde_bonus, qtde_venda, preco_medio

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_acao_carteira_ativo(cls, db: _orm.Session, id_carteira: int, id_usuario: int, id_ativo: int, codigo: str, qtde_compra: float, qtde_bonus: float, qtde_venda: float, preco_medio: float) -> None:
        try:

            row = UsuarioCarteiraAcao.buscar_por_ativo(id_usuario=id_usuario, id_ativo=int(id_ativo))

            if row:
                cart_ativo = UsuarioCarteiraAcao.get_by_id(id=int(row['ID']))

            else:
                cart_ativo = UsuarioCarteiraAcao()
                cart_ativo.id_carteira = int(id_carteira)
                cart_ativo.id_ativo = int(id_ativo)
                cart_ativo.vlr_preco_teto = 0.0
                cart_ativo.percent_balac = 0.0
                cart_ativo.nota_balac = 0

            if cart_ativo:
                cart_ativo.quant = int(qtde_compra) - int(qtde_venda)
                cart_ativo.quant_bonus = int(qtde_bonus)
                cart_ativo.vlr_preco_medio = float(preco_medio)
                cart_ativo.situacao = 'F' if int(qtde_compra) + int(qtde_bonus) - int(qtde_venda) <= 0 else 'A'  # A-Ativo # F-Finalizado
                cart_ativo.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise




    @classmethod
    @asyncio.coroutine
    async def __gerar_fii(cls, db: _orm.Session, id_carteira: int, id_usuario: int, codigo: str = None) -> None:
        try:

            # print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_fii - INICIO')

            rows = FiiFundoImob.buscar_pendentes_situacao(id_usuario=id_usuario, codigo=codigo)
            for row in rows:
                codigo = str(row['CODIGO'])
                id_fundo = int(row['ID'])
                cls.__gerar_fii_oper_comum(id_usuario=id_usuario, id_fundo=id_fundo, codigo=codigo)
                qtde_compra, qtde_bonus, qtde_venda, preco_medio = cls.__calc_fii_preco_medio_comum(id_usuario=id_usuario, id_fundo=id_fundo, codigo=codigo)
                cls.__gerar_fii_carteira_indice(id_carteira=id_carteira, id_usuario=id_usuario, id_fundo=id_fundo, codigo=codigo, qtde_compra=qtde_compra, qtde_bonus=qtde_bonus, qtde_venda=qtde_venda, preco_medio=preco_medio)

            #await asyncio.sleep(20)
            #print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_fii - FIM')

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_fii_oper_comum(cls, db: _orm.Session, id_usuario: int, id_fundo: int, codigo: str) -> None:
        try:

            rows = UsuarioFiiFundoImobLancamento.buscar_desdobro_grupamento(id_usuario=id_usuario, codigo=str(codigo))
            lista_desdobro_grupamento = [{'DATA': str(row['DATA']), 'TIPO': str(row['TIPO']), 'QUANT': float(row['QUANT']), 'ID': int(row['ID'])} for row in rows]

            lancs = UsuarioFiiFundoImobLancamento.get_all(id_usuario=id_usuario, id_fundo=int(id_fundo))
            for lanc in lancs:

                lanc.quant = lanc.quant_orig
                lanc.calc_custo()
                lanc.tot_vlr_custo = (float(lanc.quant) * float(lanc.vlr_custo)) if lanc.quant > 0.0 and float(lanc.vlr_custo) > 0.0 else 0.0

                for item in lista_desdobro_grupamento:
                    if str(lanc.data) < str(item['DATA']):
                        if str(str(item['TIPO'])) == 'D':
                            lanc.quant = float(lanc.quant) * float(item['QUANT'])
                            lanc.vlr_custo = float(lanc.vlr_custo) / float(item['QUANT'])
                        elif str(str(item['TIPO'])) == 'G':
                            lanc.quant = float(lanc.quant) / float(item['QUANT'])
                            lanc.vlr_custo = float(lanc.vlr_custo) * float(item['QUANT'])
                        lanc.tot_vlr_custo = (float(lanc.quant) * float(lanc.vlr_custo)) if lanc.quant > 0.0 and float(lanc.vlr_custo) > 0.0 else 0.0
                    UsuarioFiiFundoImobLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(item['ID']), situacao='A')  # A-Ativo

                lanc.situacao = "A"  # A-Ativa
                lanc.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __calc_fii_preco_medio_comum(cls, db: _orm.Session, id_usuario: int, id_fundo: int, codigo: str):
        try:

            qtde_atual, preco_medio_atual, vlr_tot_bonus, qtde_compra, qtde_bonus, qtde_venda, preco_medio = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

            rows = UsuarioFiiFundoImobLancamento.get_all(id_usuario=id_usuario, id_fundo=int(id_fundo))
            for row in rows:

                qtde_atual, preco_medio_atual = row.calc_preco_medio(qtde_atual=float(qtde_atual), preco_medio_atual=float(preco_medio_atual))
                preco_medio = preco_medio_atual

                if str(row.tipo) == 'C':
                    qtde_compra += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                elif str(row.tipo) == 'B':
                    qtde_bonus += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                    vlr_tot_bonus += float(row.tot_vlr_custo) if row.tot_vlr_custo and row.tot_vlr_custo > 0.0 else 0.0
                elif str(row.tipo) == 'V' or str(row.tipo) == 'P':
                    row.calc_vlr_valorizacao()
                    row.tot_vlr_valorizacao += float(vlr_tot_bonus)
                    row.calc_perc_valorizacao()
                    qtde_venda += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                    if float(qtde_compra) + float(qtde_bonus) == float(qtde_venda):
                        qtde_compra, qtde_bonus, qtde_venda, preco_medio, vlr_tot_bonus = 0.0, 0.0, 0.0, 0.0, 0.0
                    if float(qtde_atual) == 0.0:
                        vlr_tot_bonus = 0.0

                row.situacao = 'A'  # A-Ativo
                row.salvar()

            return qtde_compra, qtde_bonus, qtde_venda, preco_medio

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_fii_carteira_indice(cls, db: _orm.Session, id_carteira: int, id_usuario: int, id_fundo: int, codigo: str, qtde_compra: float, qtde_bonus: float, qtde_venda: float, preco_medio: float) -> None:
        try:

            row = UsuarioCarteiraFii.buscar_por_ativo(id_usuario=id_usuario, id_fundo=int(id_fundo))

            if row:
                cart_fundo = UsuarioCarteiraFii.get_by_id(id=int(row['ID']))

            else:
                cart_fundo = UsuarioCarteiraFii()
                cart_fundo.id_carteira = int(id_carteira)
                cart_fundo.id_fundo = int(id_fundo)
                cart_fundo.vlr_preco_teto = 0.0
                cart_fundo.percent_balac = 0.0
                cart_fundo.nota_balac = 0

            if cart_fundo:
                cart_fundo.quant = int(qtde_compra) - int(qtde_venda)
                cart_fundo.quant_bonus = int(qtde_bonus)
                cart_fundo.vlr_preco_medio = float(preco_medio)
                cart_fundo.situacao = 'F' if int(qtde_compra) + int(qtde_bonus) - int(qtde_venda) <= 0 else 'A'  # A-Ativo # F-Finalizado
                cart_fundo.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise




    @classmethod
    @asyncio.coroutine
    async def __gerar_etf(cls, db: _orm.Session, id_carteira: int, id_usuario: int, codigo: str = None) -> None:
        try:

            #print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_etf - INICIO')

            rows = ETFIndice.buscar_pendentes_situacao(id_usuario=id_usuario, codigo=codigo)
            for row in rows:
                codigo = str(row['CODIGO'])
                id_indice = int(row['ID'])
                cls.__gerar_etf_oper_day_trade(id_usuario=id_usuario, codigo=codigo)
                cls.__gerar_etf_oper_comum(id_usuario=id_usuario, codigo=codigo)
                cls.__calc_etf_preco_medio_day_trade(id_usuario=id_usuario, id_indice=id_indice, codigo=codigo)
                qtde_compra, qtde_bonus, qtde_venda, preco_medio = cls.__calc_etf_preco_medio_comum(id_usuario=id_usuario, id_indice=id_indice, codigo=codigo)
                cls.__gerar_etf_carteira_indice(id_carteira=id_carteira, id_usuario=id_usuario, id_indice=id_indice, codigo=codigo, qtde_compra=qtde_compra, qtde_bonus=qtde_bonus, qtde_venda=qtde_venda, preco_medio=preco_medio)

            #await asyncio.sleep(15)
            #print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_etf - FIM')

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_etf_oper_day_trade(cls, db: _orm.Session, id_usuario: int, codigo: str) -> None:
        try:

            rows = UsuarioETFIndiceLancamento.buscar_lista_datas_day_trade(id_usuario=id_usuario, codigo=str(codigo))
            for row in rows:
                dt_lanc = str(row['DATA'])

                lista_compras = UsuarioETFIndiceLancamento.buscar_por_data(id_usuario=id_usuario, codigo=str(codigo), data=str(dt_lanc), tipo='C') # C-Compra
                for lanc_compra in lista_compras:
                    compra_id_lanc = str(lanc_compra['ID'])
                    compra_id_indice = int(lanc_compra['IDINDICE'])
                    compra_id_corretora = int(lanc_compra['IDCORRETORA']) if lanc_compra['IDCORRETORA'] else None
                    compra_quant = int(lanc_compra['QUANT']) if lanc_compra['QUANT'] else 0
                    compra_quant_pend = int(lanc_compra['QUANTPEND']) if lanc_compra['QUANTPEND'] else 0
                    compra_vlr_custo = float(lanc_compra['VLRCUSTO']) if lanc_compra['VLRCUSTO'] else 0.0
                    compra_troca = str(lanc_compra['TROCA']) if lanc_compra['TROCA'] else 'N'

                    lista_vendas = UsuarioETFIndiceLancamento.buscar_por_data(id_usuario=id_usuario, codigo=str(codigo), data=str(dt_lanc), tipo='V')  # V-Venda
                    for lanc_venda in lista_vendas:
                        venda_id_lanc = str(lanc_venda['ID'])
                        venda_id_indice = int(lanc_venda['IDINDICE'])
                        venda_id_corretora = int(lanc_venda['IDCORRETORA']) if lanc_venda['IDCORRETORA'] else None
                        venda_quant = int(lanc_venda['QUANT']) if lanc_venda['QUANT'] else 0
                        venda_quant_pend = int(lanc_venda['QUANTPEND']) if lanc_venda['QUANTPEND'] else 0
                        venda_vlr_custo = float(lanc_venda['VLRCUSTO']) if lanc_venda['VLRCUSTO'] else 0.0
                        venda_troca = str(lanc_venda['TROCA']) if lanc_venda['TROCA'] else 'N'

                        if int(venda_quant_pend) == int(compra_quant):  # venda 100 = Compra 100
                            compra_quant = 0.0
                            oper = UsuarioETFIndiceOperacao(id_usuario=id_usuario)
                            oper.id_indice = int(compra_id_indice)
                            oper.id_corretora = compra_id_corretora
                            oper.id_lancamento = int(compra_id_lanc)
                            oper.tipo = 'C' # C-Compra
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(compra_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = compra_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            oper = UsuarioETFIndiceOperacao(id_usuario=id_usuario)
                            oper.id_indice = int(venda_id_indice)
                            oper.id_corretora = venda_id_corretora
                            oper.id_lancamento = int(venda_id_lanc)
                            oper.tipo = 'V' # V-Venda
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(venda_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = venda_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            UsuarioETFIndiceLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(compra_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            UsuarioETFIndiceLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(venda_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            break  # Finaliza Loop lancVenda

                        elif int(venda_quant_pend) < int(compra_quant): # venda 100 < Compra 200
                            compra_quant -= int(venda_quant_pend)

                            oper = UsuarioETFIndiceOperacao(id_usuario=id_usuario)
                            oper.id_indice = int(compra_id_indice)
                            oper.id_corretora = compra_id_corretora
                            oper.id_lancamento = int(compra_id_lanc)
                            oper.tipo = 'C' # C-Compra
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = int(compra_quant_pend) - int(venda_quant_pend)
                            oper.vlr_custo = float(compra_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = compra_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            oper = UsuarioETFIndiceOperacao(id_usuario=id_usuario)
                            oper.id_indice = int(venda_id_indice)
                            oper.id_corretora = venda_id_corretora
                            oper.id_lancamento = int(venda_id_lanc)
                            oper.tipo = 'V' # V-Venda
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(venda_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = venda_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            UsuarioETFIndiceLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(compra_id_lanc), qtd_pend=int(compra_quant_pend) - int(venda_quant_pend), situacao='A')  # A-Ativo
                            UsuarioETFIndiceLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(venda_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            venda_quant_pend = 0

                        if int(venda_quant_pend) > int(compra_quant):  # venda 200 > Compra 100
                            compra_quant = 0.0

                            oper = UsuarioETFIndiceOperacao(id_usuario=id_usuario)
                            oper.id_indice = int(compra_id_indice)
                            oper.id_corretora = compra_id_corretora
                            oper.id_lancamento = int(compra_id_lanc)
                            oper.tipo = 'C' # C-Compra
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(compra_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(compra_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = compra_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            oper = UsuarioETFIndiceOperacao(id_usuario=id_usuario)
                            oper.id_indice = int(venda_id_indice)
                            oper.id_corretora = venda_id_corretora
                            oper.id_lancamento = int(venda_id_lanc)
                            oper.tipo = 'V' # V-Venda
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(compra_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(venda_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = venda_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            UsuarioETFIndiceLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(compra_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            UsuarioETFIndiceLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(venda_id_lanc), qtd_pend=int(venda_quant_pend) - int(compra_quant_pend), situacao='A')  # A-Ativo
                            break  # Finaliza Loop lancVenda

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_etf_oper_comum(cls, db: _orm.Session, id_usuario: int, codigo: str) -> None:
        try:

            rows = UsuarioETFIndiceLancamento.buscar_desdobro_grupamento(id_usuario=id_usuario, codigo=str(codigo))
            lista_desdobro_grupamento = [{'DATA': str(row['DATA']), 'TIPO': str(row['TIPO']), 'QUANT': float(row['QUANT']), 'ID': int(row['ID'])} for row in rows]

            lancs = UsuarioETFIndiceLancamento.buscar_por_qtde_pend_maior_que_zero(id_usuario=id_usuario, codigo=str(codigo))
            for lanc in lancs:

                id_lanc = str(lanc['ID'])
                id_indice = int(lanc['IDINDICE'])
                id_corretora = int(lanc['IDCORRETORA']) if lanc['IDCORRETORA'] else None
                dt_lanc = str(lanc['DATA'])
                quant_pend = int(lanc['QUANTPEND']) if lanc['QUANTPEND'] else 0
                tipo = str(lanc['TIPO'])
                vlr_custo = float(lanc['VLRCUSTO']) if lanc['VLRCUSTO'] else 0.0
                troca = str(lanc['TROCA']) if lanc['TROCA'] else 'N'

                oper = UsuarioETFIndiceOperacao(id_usuario=id_usuario)
                oper.id_indice = int(id_indice)
                oper.id_corretora = id_corretora
                oper.id_lancamento = int(id_lanc)
                oper.tipo = str(tipo)
                oper.categoria = "C"  # C-Comum
                oper.data = str(dt_lanc)
                oper.quant = int(quant_pend)
                oper.quant_acumulado = 0.0
                oper.vlr_custo = float(vlr_custo)
                oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                oper.vlr_preco_medio = 0.0
                oper.tot_vlr_valorizacao = 0.0
                oper.perc_valorizacao = 0.0
                oper.troca = troca
                oper.situacao = "A"  # A-Ativa

                for item in lista_desdobro_grupamento:
                    if str(oper.data) < str(item['DATA']):
                        if str(str(item['TIPO'])) == 'D':
                            oper.quant = float(oper.quant) * float(item['QUANT'])
                            oper.vlr_custo = float(oper.vlr_custo) / float(item['QUANT'])
                        elif str(str(item['TIPO'])) == 'G':
                            oper.quant = float(oper.quant) / float(item['QUANT'])
                            oper.vlr_custo = float(oper.vlr_custo) * float(item['QUANT'])
                        oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                    UsuarioETFIndiceLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(item['ID']), qtd_pend=0, situacao='A')  # A-Ativo

                oper.salvar()

                UsuarioETFIndiceLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(id_lanc), qtd_pend=0, situacao='A')  # A-Ativo

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __calc_etf_preco_medio_day_trade(cls, db: _orm.Session, id_usuario: int, id_indice: int, codigo: str) -> None:
        try:

            dt_atual = ""
            qtde_atual, preco_medio_atual = 0.0, 0.0

            rows = UsuarioETFIndiceOperacao.get_all(id_usuario=id_usuario, id_indice=int(id_indice), categoria='D')  # D-DayTarde
            for row in rows:
                if str(dt_atual) != str(row.data):
                    dt_atual = str(row.data)
                    qtde_atual, preco_medio_atual = 0.0, 0.0
                qtde_atual, preco_medio_atual = row.calc_preco_medio(qtde_atual=float(qtde_atual), preco_medio_atual=float(preco_medio_atual))
                if str(row.tipo) == 'V' or str(row.tipo) == 'P':
                    row.calc_vlr_valorizacao()
                    row.calc_perc_valorizacao()
                row.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __calc_etf_preco_medio_comum(cls, db: _orm.Session, id_usuario: int, id_indice: int, codigo: str):
        try:

            qtde_atual, preco_medio_atual, vlr_tot_bonus, qtde_compra, qtde_bonus, qtde_venda, preco_medio = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

            rows = UsuarioETFIndiceOperacao.get_all(id_usuario=id_usuario, id_indice=int(id_indice), categoria='C')  # C-Comun
            for row in rows:

                qtde_atual, preco_medio_atual = row.calc_preco_medio(qtde_atual=float(qtde_atual), preco_medio_atual=float(preco_medio_atual))
                preco_medio = preco_medio_atual
                row.quant_acumulado = float(qtde_atual)

                if str(row.tipo) == 'C':
                    qtde_compra += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                elif str(row.tipo) == 'B':
                    qtde_bonus += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                    vlr_tot_bonus += float(row.tot_vlr_custo) if row.tot_vlr_custo and row.tot_vlr_custo > 0.0 else 0.0
                elif str(row.tipo) == 'V' or str(row.tipo) == 'P':
                    row.calc_vlr_valorizacao()
                    row.tot_vlr_valorizacao += float(vlr_tot_bonus)
                    row.calc_perc_valorizacao()
                    qtde_venda += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                    if float(qtde_compra) + float(qtde_bonus) == float(qtde_venda):
                        qtde_compra, qtde_bonus, qtde_venda, preco_medio, vlr_tot_bonus = 0.0, 0.0, 0.0, 0.0, 0.0
                    if float(qtde_atual) == 0.0:
                        vlr_tot_bonus = 0.0

                row.salvar()

            return qtde_compra, qtde_bonus, qtde_venda, preco_medio

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_etf_carteira_indice(cls, db: _orm.Session, id_carteira: int, id_usuario: int, id_indice: int, codigo: str, qtde_compra: float, qtde_bonus: float, qtde_venda: float, preco_medio: float) -> None:
        try:

            row = UsuarioCarteiraEtf.buscar_por_ativo(id_usuario=id_usuario, id_indice=int(id_indice))

            if row:
                cart_indice = UsuarioCarteiraEtf.get_by_id(id=int(row['ID']))

            else:
                cart_indice = UsuarioCarteiraEtf()
                cart_indice.id_carteira = int(id_carteira)
                cart_indice.id_indice = int(id_indice)
                cart_indice.vlr_preco_teto = 0.0
                cart_indice.percent_balac = 0.0
                cart_indice.nota_balac = 0

            if cart_indice:
                cart_indice.quant = int(qtde_compra) - int(qtde_venda)
                cart_indice.quant_bonus = int(qtde_bonus)
                cart_indice.vlr_preco_medio = float(preco_medio)
                cart_indice.situacao = 'F' if int(qtde_compra) + int(qtde_bonus) - int(qtde_venda) <= 0 else 'A'  # A-Ativo # F-Finalizado
                cart_indice.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise





    @classmethod
    @asyncio.coroutine
    async def __gerar_bdr(cls, db: _orm.Session, id_carteira: int, id_usuario: int, codigo: str = None) -> None:
        try:

            # print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_bdr - INICIO')

            rows = BDREmpresa.buscar_pendentes_situacao(id_usuario=id_usuario, codigo=codigo)
            for row in rows:
                codigo = str(row['CODIGO'])
                id_bdr = int(row['ID'])
                cls.__gerar_bdr_oper_day_trade(id_usuario=id_usuario, codigo=codigo)
                cls.__gerar_bdr_oper_comum(id_usuario=id_usuario, codigo=codigo)
                cls.__calc_bdr_preco_medio_day_trade(id_usuario=id_usuario, id_bdr=id_bdr, codigo=codigo)
                qtde_compra, qtde_bonus, qtde_venda, preco_medio = cls.__calc_bdr_preco_medio_comum(id_usuario=id_usuario, id_bdr=id_bdr, codigo=codigo)
                cls.__gerar_bdr_carteira_ativo(id_carteira=id_carteira, id_usuario=id_usuario, id_bdr=id_bdr, codigo=codigo, qtde_compra=qtde_compra, qtde_bonus=qtde_bonus, qtde_venda=qtde_venda, preco_medio=preco_medio)

            # await asyncio.sleep(10)
            # print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_bdr - FIM')

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_bdr_oper_day_trade(cls, db: _orm.Session, id_usuario: int, codigo: str) -> None:
        try:

            rows = UsuarioBDREmpresaLancamento.buscar_lista_datas_day_trade(id_usuario=id_usuario, codigo=str(codigo))
            for row in rows:
                dt_lanc = str(row['DATA'])

                lista_compras = UsuarioBDREmpresaLancamento.buscar_por_data(id_usuario=id_usuario, codigo=str(codigo), data=str(dt_lanc), tipo='C') # C-Compra
                for lanc_compra in lista_compras:
                    compra_id_lanc = str(lanc_compra['ID'])
                    compra_id_bdr = int(lanc_compra['IDBDR'])
                    compra_id_corretora = int(lanc_compra['IDCORRETORA']) if lanc_compra['IDCORRETORA'] else None
                    compra_quant = int(lanc_compra['QUANT']) if lanc_compra['QUANT'] else 0
                    compra_quant_pend = int(lanc_compra['QUANTPEND']) if lanc_compra['QUANTPEND'] else 0
                    compra_vlr_custo = float(lanc_compra['VLRCUSTO']) if lanc_compra['VLRCUSTO'] else 0.0
                    compra_troca = str(lanc_compra['TROCA']) if lanc_compra['TROCA'] else 'N'

                    lista_vendas = UsuarioBDREmpresaLancamento.buscar_por_data(id_usuario=id_usuario, codigo=str(codigo), data=str(dt_lanc), tipo='V')  # V-Venda
                    for lanc_venda in lista_vendas:
                        venda_id_lanc = str(lanc_venda['ID'])
                        venda_id_bdr = int(lanc_venda['IDBDR'])
                        venda_id_corretora = int(lanc_venda['IDCORRETORA']) if lanc_venda['IDCORRETORA'] else None
                        venda_quant = int(lanc_venda['QUANT']) if lanc_venda['QUANT'] else 0
                        venda_quant_pend = int(lanc_venda['QUANTPEND']) if lanc_venda['QUANTPEND'] else 0
                        venda_vlr_custo = float(lanc_venda['VLRCUSTO']) if lanc_venda['VLRCUSTO'] else 0.0
                        venda_troca = str(lanc_venda['TROCA']) if lanc_venda['TROCA'] else 'N'

                        if int(venda_quant_pend) == int(compra_quant):  # venda 100 = Compra 100
                            compra_quant = 0.0
                            oper = UsuarioBDREmpresaOperacao(id_usuario=id_usuario)
                            oper.id_bdr = int(compra_id_bdr)
                            oper.id_corretora = compra_id_corretora
                            oper.id_lancamento = int(compra_id_lanc)
                            oper.tipo = 'C' # C-Compra
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(compra_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = compra_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            oper = UsuarioBDREmpresaOperacao(id_usuario=id_usuario)
                            oper.id_bdr = int(venda_id_bdr)
                            oper.id_corretora = venda_id_corretora
                            oper.id_lancamento = int(venda_id_lanc)
                            oper.tipo = 'V' # V-Venda
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(venda_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = venda_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            UsuarioBDREmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(compra_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            UsuarioBDREmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(venda_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            break  # Finaliza Loop lancVenda

                        elif int(venda_quant_pend) < int(compra_quant): # venda 100 < Compra 200
                            compra_quant -= int(venda_quant_pend)

                            oper = UsuarioBDREmpresaOperacao(id_usuario=id_usuario)
                            oper.id_bdr = int(compra_id_bdr)
                            oper.id_corretora = compra_id_corretora
                            oper.id_lancamento = int(compra_id_lanc)
                            oper.tipo = 'C' # C-Compra
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = int(compra_quant_pend) - int(venda_quant_pend)
                            oper.vlr_custo = float(compra_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = compra_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            oper = UsuarioBDREmpresaOperacao(id_usuario=id_usuario)
                            oper.id_bdr = int(venda_id_bdr)
                            oper.id_corretora = venda_id_corretora
                            oper.id_lancamento = int(venda_id_lanc)
                            oper.tipo = 'V' # V-Venda
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(venda_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(venda_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = venda_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            UsuarioBDREmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(compra_id_lanc), qtd_pend=int(compra_quant_pend) - int(venda_quant_pend), situacao='A')  # A-Ativo
                            UsuarioBDREmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(venda_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            venda_quant_pend = 0

                        if int(venda_quant_pend) > int(compra_quant):  # venda 200 > Compra 100
                            compra_quant = 0.0

                            oper = UsuarioBDREmpresaOperacao(id_usuario=id_usuario)
                            oper.id_bdr = int(compra_id_bdr)
                            oper.id_corretora = compra_id_corretora
                            oper.id_lancamento = int(compra_id_lanc)
                            oper.tipo = 'C' # C-Compra
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(compra_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(compra_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = compra_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            oper = UsuarioBDREmpresaOperacao(id_usuario=id_usuario)
                            oper.id_bdr = int(venda_id_bdr)
                            oper.id_corretora = venda_id_corretora
                            oper.id_lancamento = int(venda_id_lanc)
                            oper.tipo = 'V' # V-Venda
                            oper.categoria = "D"  # D-DayTarde
                            oper.data = str(dt_lanc)
                            oper.quant = int(compra_quant_pend)
                            oper.quant_acumulado = 0.0
                            oper.vlr_custo = float(venda_vlr_custo)
                            oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                            oper.vlr_preco_medio = 0.0
                            oper.tot_vlr_valorizacao = 0.0
                            oper.perc_valorizacao = 0.0
                            oper.troca = venda_troca
                            oper.situacao = "F"  # F-Finalizada
                            oper.salvar()

                            UsuarioBDREmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(compra_id_lanc), qtd_pend=0, situacao='A')  # A-Ativo
                            UsuarioBDREmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(venda_id_lanc), qtd_pend=int(venda_quant_pend) - int(compra_quant_pend), situacao='A')  # A-Ativo
                            break  # Finaliza Loop lancVenda

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_bdr_oper_comum(cls, db: _orm.Session, id_usuario: int, codigo: str) -> None:
        try:

            lancs = UsuarioBDREmpresaLancamento.buscar_por_qtde_pend_maior_que_zero(id_usuario=id_usuario, codigo=str(codigo))

            rows = UsuarioBDREmpresaLancamento.buscar_desdobro_grupamento(id_usuario=id_usuario, codigo=str(codigo))
            lista_desdobro_grupamento = [{'DATA': str(row['DATA']), 'TIPO': str(row['TIPO']), 'QUANT': float(row['QUANT']), 'ID': int(row['ID'])} for row in rows]

            for lanc in lancs:

                id_lanc = str(lanc['ID'])
                id_bdr = int(lanc['IDBDR'])
                id_corretora = int(lanc['IDCORRETORA']) if lanc['IDCORRETORA'] else None
                dt_lanc = str(lanc['DATA'])
                quant_pend = int(lanc['QUANTPEND']) if lanc['QUANTPEND'] else 0
                tipo = str(lanc['TIPO'])
                vlr_custo = float(lanc['VLRCUSTO']) if lanc['VLRCUSTO'] else 0.0
                troca = str(lanc['TROCA']) if lanc['TROCA'] else 'N'

                oper = UsuarioBDREmpresaOperacao(id_usuario=id_usuario)
                oper.id_bdr = int(id_bdr)
                oper.id_corretora = id_corretora
                oper.id_lancamento = int(id_lanc)
                oper.tipo = str(tipo)
                oper.categoria = "C"  # C-Comum
                oper.data = str(dt_lanc)
                oper.quant = int(quant_pend)
                oper.quant_acumulado = 0.0
                oper.vlr_custo = float(vlr_custo)
                oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                oper.vlr_preco_medio = 0.0
                oper.tot_vlr_valorizacao = 0.0
                oper.perc_valorizacao = 0.0
                oper.troca = troca
                oper.situacao = "A"  # A-Ativa

                for item in lista_desdobro_grupamento:
                    if str(oper.data) < str(item['DATA']):
                        if str(str(item['TIPO'])) == 'D':
                            oper.quant = float(oper.quant) * float(item['QUANT'])
                            oper.vlr_custo = float(oper.vlr_custo) / float(item['QUANT'])
                        elif str(str(item['TIPO'])) == 'G':
                            oper.quant = float(oper.quant) / float(item['QUANT'])
                            oper.vlr_custo = float(oper.vlr_custo) * float(item['QUANT'])
                        oper.tot_vlr_custo = (float(oper.quant) * float(oper.vlr_custo)) if oper.quant > 0.0 and float(oper.vlr_custo) > 0.0 else 0.0
                    UsuarioBDREmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(item['ID']), qtd_pend=0, situacao='A')  # A-Ativo

                oper.salvar()

                UsuarioBDREmpresaLancamento.atualizar_qtd_pend_situacao(id_usuario=id_usuario, id_lanc=int(id_lanc), qtd_pend=0, situacao='A')  # A-Ativo

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __calc_bdr_preco_medio_day_trade(cls, db: _orm.Session, id_usuario: int, id_bdr: int, codigo: str) -> None:
        try:

            rows = UsuarioBDREmpresaOperacao.get_all(id_usuario=id_usuario, id_bdr=int(id_bdr), categoria='D')  # D-DayTarde
            dt_atual = ""
            qtde_atual = 0.0
            preco_medio_atual = 0.0
            for row in rows:
                if str(dt_atual) != str(row.data):
                    dt_atual = str(row.data)
                    qtde_atual = 0.0
                    preco_medio_atual = 0.0
                qtde_atual, preco_medio_atual = row.calc_preco_medio(qtde_atual=float(qtde_atual), preco_medio_atual=float(preco_medio_atual))
                if str(row.tipo) == 'V' or str(row.tipo) == 'P':
                    row.calc_vlr_valorizacao()
                    row.calc_perc_valorizacao()
                row.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __calc_bdr_preco_medio_comum(cls, db: _orm.Session, id_usuario: int, id_bdr: int, codigo: str):
        try:

            qtde_atual, preco_medio_atual, vlr_tot_bonus, qtde_compra, qtde_bonus, qtde_venda, preco_medio = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0

            rows = UsuarioBDREmpresaOperacao.get_all(id_usuario=id_usuario, id_bdr=int(id_bdr), categoria='C')  # C-Comun
            for row in rows:

                qtde_atual, preco_medio_atual = row.calc_preco_medio(qtde_atual=float(qtde_atual), preco_medio_atual=float(preco_medio_atual))
                preco_medio = preco_medio_atual
                row.quant_acumulado = float(qtde_atual)

                if str(row.tipo) == 'C':
                    qtde_compra += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                elif str(row.tipo) == 'B':
                    qtde_bonus += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                    vlr_tot_bonus += float(row.tot_vlr_custo) if row.tot_vlr_custo and row.tot_vlr_custo > 0.0 else 0.0
                elif str(row.tipo) == 'V' or str(row.tipo) == 'P':
                    row.calc_vlr_valorizacao()
                    row.tot_vlr_valorizacao += float(vlr_tot_bonus)
                    row.calc_perc_valorizacao()
                    qtde_venda += float(row.quant) if row.quant and row.quant > 0.0 else 0.0
                    if float(qtde_compra) + float(qtde_bonus) == float(qtde_venda):
                        qtde_compra, qtde_bonus, qtde_venda, preco_medio, vlr_tot_bonus = 0.0, 0.0, 0.0, 0.0, 0.0
                    if float(qtde_atual) == 0.0:
                        vlr_tot_bonus = 0.0

                row.salvar()

            return qtde_compra, qtde_bonus, qtde_venda, preco_medio

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_bdr_carteira_ativo(cls, db: _orm.Session, id_carteira: int, id_usuario: int, id_bdr: int, codigo: str, qtde_compra: float, qtde_bonus: float, qtde_venda: float, preco_medio: float) -> None:
        try:

            row = UsuarioCarteiraBdr.buscar_por_ativo(id_usuario=id_usuario, id_bdr=int(id_bdr))

            if row:
                cart_ativo = UsuarioCarteiraBdr.get_by_id(id=int(row['ID']))

            else:
                cart_ativo = UsuarioCarteiraBdr()
                cart_ativo.id_carteira = int(id_carteira)
                cart_ativo.id_bdr = int(id_bdr)
                cart_ativo.vlr_preco_teto = 0.0
                cart_ativo.percent_balac = 0.0
                cart_ativo.nota_balac = 0

            if cart_ativo:
                cart_ativo.quant = int(qtde_compra) - int(qtde_venda)
                cart_ativo.quant_bonus = int(qtde_bonus)
                cart_ativo.vlr_preco_medio = float(preco_medio)
                cart_ativo.situacao = 'F' if int(qtde_compra) + int(qtde_bonus) - int(qtde_venda) <= 0 else 'A'  # A-Ativo # F-Finalizado
                cart_ativo.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise




    @classmethod
    @asyncio.coroutine
    async def __gerar_cripto(cls, db: _orm.Session, id_carteira: int, id_usuario: int, codigo: str = None) -> None:
        try:

            #print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_cripto - INICIO')

            rows = CriptoEmpresa.buscar_pendentes_situacao(id_usuario=id_usuario, codigo=codigo)
            for row in rows:
                codigo = str(row['CODIGO'])
                id_cripto = int(row['ID'])
                cls.__gerar_cripto_oper_comum(id_usuario=id_usuario, id_cripto=id_cripto, codigo=codigo)
                qtde_compra, qtde_venda, preco_medio = cls.__calc_cripto_preco_medio_comum(id_usuario=id_usuario, id_cripto=id_cripto, codigo=codigo)
                cls.__gerar_cripto_carteira_indice(id_carteira=id_carteira, id_usuario=id_usuario, id_cripto=id_cripto, codigo=codigo, qtde_compra=qtde_compra, qtde_venda=qtde_venda, preco_medio=preco_medio)

            #await asyncio.sleep(5)
            #print(dt.datetime.now(), 'UsuarioCarteira - Gerar - __gerar_cripto - FIM')

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_cripto_oper_comum(cls, db: _orm.Session, id_usuario: int, id_cripto: int, codigo: str) -> None:
        try:

            lancs = UsuarioCriptoLancamento.get_all(id_usuario=id_usuario, id_cripto=int(id_cripto))
            for lanc in lancs:
                lanc.quant = lanc.quant_orig
                lanc.calc_custo()
                lanc.tot_vlr_custo = (float(lanc.quant) * float(lanc.vlr_custo)) if float(lanc.quant) > 0.0 and float(lanc.vlr_custo) > 0.0 else 0.0
                lanc.situacao = "A"  # A-Ativa
                lanc.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __calc_cripto_preco_medio_comum(cls, db: _orm.Session, id_usuario: int, id_cripto: int, codigo: str):
        try:

            qtde_atual, preco_medio_atual, qtde_compra, qtde_venda, preco_medio = 0.0, 0.0, 0.0, 0.0, 0.0

            rows = UsuarioCriptoLancamento.get_all(id_usuario=id_usuario, id_cripto=int(id_cripto))
            for row in rows:

                qtde_atual, preco_medio_atual = row.calc_preco_medio(qtde_atual=float(qtde_atual), preco_medio_atual=float(preco_medio_atual))
                preco_medio = preco_medio_atual

                if str(row.tipo) == 'C':
                    qtde_compra += float(row.quant) if row.quant and float(row.quant) > 0.0 else 0.0
                elif str(row.tipo) == 'V' or str(row.tipo) == 'P':
                    row.calc_vlr_valorizacao()
                    row.calc_perc_valorizacao()
                    qtde_venda += float(row.quant) if row.quant and float(row.quant) > 0.0 else 0.0
                    if float(qtde_compra) == float(qtde_venda):
                        qtde_compra, qtde_venda, preco_medio = 0.0, 0.0, 0.0

                row.situacao = 'A'  # A-Ativo
                row.salvar()

            return qtde_compra, qtde_venda, preco_medio

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def __gerar_cripto_carteira_indice(cls, db: _orm.Session, id_carteira: int, id_usuario: int, id_cripto: int, codigo: str, qtde_compra: float, qtde_venda: float, preco_medio: float) -> None:
        try:

            row = UsuarioCarteiraCripto.buscar_por_ativo(id_usuario=id_usuario, id_cripto=int(id_cripto))

            if row:
                cart_cripto = UsuarioCarteiraCripto.get_by_id(id=int(row['ID']))

            else:
                cart_cripto = UsuarioCarteiraCripto()
                cart_cripto.id_carteira = int(id_carteira)
                cart_cripto.id_cripto = int(id_cripto)
                cart_cripto.vlr_preco_teto = 0.0
                cart_cripto.percent_balac = 0.0
                cart_cripto.nota_balac = 0

            if cart_cripto:
                cart_cripto.quant = float(qtde_compra) - float(qtde_venda)
                cart_cripto.vlr_preco_medio = float(preco_medio)
                cart_cripto.situacao = 'F' if cart_cripto.quant <= 0.0 else 'A'  # A-Ativo # F-Finalizado
                cart_cripto.salvar()

        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise




    @classmethod
    async def get_all(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(MODEL).filter_by(id_usuario=id_usuario, situacao='A').order_by(MODEL.tipo, cls.descricao).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_id(cls, db: _orm.Session, id: int):
        try:
            return db.query(MODEL).filter_by(id=id, situacao='A').first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_usuario(cls, db: _orm.Session, id_usuario: int, id: int):
        try:
            return db.query(MODEL).filter_by(id_usuario=id_usuario, id=id, situacao='A').first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_descricao(cls, db: _orm.Session, id_usuario: int, descricao: str):
        try:
            return db.query(MODEL).filter_by(id_usuario=id_usuario, descricao=descricao, situacao='A').first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_by_tipo(cls, db: _orm.Session, id_usuario: int, tipo: str = 'D'):
        try:
            return db.query(MODEL).filter_by(id_usuario=id_usuario, tipo=tipo).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_lista_nome(cls, db: _orm.Session, id_usuario: int):
        try:
            return db.query(MODEL).filter_by(id_usuario=id_usuario, tipo='P', situacao='A').order_by(MODEL.tipo, cls.descricao).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_todos(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT C.ID, C.DESCRICAO, C.TIPO, C.SITUACAO FROM TBCARTEIRA C WHERE C.IDUSUARIO = :IDUSUARIO AND C.SITUACAO = 'A' ORDER BY C.TIPO, C.DESCRICAO """
        params = {'IDUSUARIO': id_usuario}
        try:
            try:
                return db.execute(query, params)
            except Exception as e:
                db.rollback()
                db.close()
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_id(cls, db: _orm.Session, id_usuario: int, id: int = None):
        query = """ SELECT C.ID, C.DESCRICAO, C.TIPO, C.SITUACAO FROM TBCARTEIRA C WHERE C.IDUSUARIO = :IDUSUARIO AND C.ID = :ID AND C.SITUACAO = 'A' """
        params = {'IDUSUARIO': id_usuario, 'ID': id}
        try:
            try:
                return db.execute(query, params).first()
            except Exception as e:
                db.rollback()
                db.close()
                return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_nome(cls, db: _orm.Session, id_usuario: int, nome: str = None):
        query = """ SELECT C.ID, C.DESCRICAO, C.TIPO, C.SITUACAO FROM TBCARTEIRA C WHERE C.IDUSUARIO = :IDUSUARIO AND C.DESCRICAO = :DESCRICAO AND C.SITUACAO = 'A' """
        params = {'IDUSUARIO': id_usuario, 'DESCRICAO': nome}
        try:
            try:
                return db.execute(query, params).first()
            except Exception as e:
                db.rollback()
                db.close()
                return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_por_tipo_default(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT C.ID, C.DESCRICAO, C.TIPO, C.SITUACAO FROM TBCARTEIRA C WHERE C.IDUSUARIO = :IDUSUARIO AND C.TIPO = 'D' """
        params = {'IDUSUARIO': id_usuario}
        try:
            return db.execute(query, params).first()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def buscar_lista_nome(cls, db: _orm.Session, id_usuario: int):
        query = """ SELECT C.ID, C.DESCRICAO FROM TBCARTEIRA C WHERE C.IDUSUARIO = :IDUSUARIO AND C.TIPO = 'P' AND C.SITUACAO = 'A' ORDER BY C.TIPO, C.DESCRICAO """
        params = {'IDUSUARIO': id_usuario}
        try:
            try:
                return db.execute(query, params)
            except Exception as e:
                db.rollback()
                db.close()
                return db.execute(query, params)
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_por_id(cls, db: _orm.Session, id_usuario: int, id_portfolio: int, commit: bool = True):
        try:
            query = "DELETE FROM TBCARTEIRA WHERE IDUSUARIO = :IDUSUARIO AND ID = :ID"
            params = {'IDUSUARIO': id_usuario, 'ID': id_portfolio}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, row: UsuarioCarteiraModel, commit: bool = True):
        try:
            db.add(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, row: UsuarioCarteiraModel, commit: bool = True):
        try:
            db.delete(row)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
