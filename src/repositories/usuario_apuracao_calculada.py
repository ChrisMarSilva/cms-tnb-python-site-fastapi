# -*- coding: utf-8 -*-
import sys
import os
import datetime as dt
import time
import asyncio
# from threading import Thread
import sqlalchemy.orm as _orm
from app.models.usuario_apuracao import UsuarioApuracao
from app.models.usuario_config import UsuarioConfig
from app.models.usuario_acao_empresa_lancamento import UsuarioACAOEmpresaLancamento
from app.models.usuario_fii_fundoimob_lancamento import UsuarioFiiFundoImobLancamento
from app.models.usuario_etf_indice_lancamento import UsuarioETFIndiceLancamento
from app.models.usuario_bdr_empresa_lancamento import UsuarioBDREmpresaLancamento
from app.models.usuario_acao_empresa_operacao import UsuarioACAOEmpresaOperacao
from app.models.usuario_etf_indice_operacao import UsuarioETFIndiceOperacao
from app.models.usuario_bdr_empresa_operacao import UsuarioBDREmpresaOperacao
from app.models.usuario_cripto_lancamento import UsuarioCriptoLancamento
# from app.models.log_erro import LogErro
from app.util.util_formatacao import decimal_to_str
from app.util.util_datahora import pegar_data_atual, converter_str_to_datetime, converter_datetime_str


class UsuarioApuracaoCalculadaRepository:

    @classmethod
    async def gerar_todos(cls, db: _orm.Session, id_usuario: int) -> None:
        try:

            # cls.gerar(id_usuario=id_usuario, tp_apuracao='C') # C - ACAO Comum
            # cls.gerar(id_usuario=id_usuario, tp_apuracao='D') # D - ACAO DayTrade
            # cls.gerar(id_usuario=id_usuario, tp_apuracao='F') # F - FII
            # cls.gerar(id_usuario=id_usuario, tp_apuracao='E') # E - ETF Comum
            # cls.gerar(id_usuario=id_usuario, tp_apuracao='G') # G - ETF DayTrade
            # cls.gerar(id_usuario=id_usuario, tp_apuracao='I') # I - BDR Comum
            # cls.gerar(id_usuario=id_usuario, tp_apuracao='J') # J - BDR Day Trade
            # cls.gerar(id_usuario=id_usuario, tp_apuracao='K') # K - Cripto

            loop = asyncio.new_event_loop()  # get_event_loop
            try:
                asyncio.set_event_loop(loop)
                tasks = [
                    asyncio.Task(cls, db: _orm.gerar_async(id_usuario=id_usuario, tp_apuracao='C')),  # C - ACAO Comum
                    asyncio.Task(cls, db: _orm.gerar_async(id_usuario=id_usuario, tp_apuracao='D')),  # D - ACAO DayTrade
                    asyncio.Task(cls, db: _orm.gerar_async(id_usuario=id_usuario, tp_apuracao='F')),  # F - FII
                    asyncio.Task(cls, db: _orm.gerar_async(id_usuario=id_usuario, tp_apuracao='E')),  # E - ETF Comum
                    asyncio.Task(cls, db: _orm.gerar_async(id_usuario=id_usuario, tp_apuracao='G')),  # G - ETF DayTrade
                    asyncio.Task(cls, db: _orm.gerar_async(id_usuario=id_usuario, tp_apuracao='I')),  # I - BDR Comum
                    asyncio.Task(cls, db: _orm.gerar_async(id_usuario=id_usuario, tp_apuracao='J')),  # J - BDR Day Trade
                    asyncio.Task(cls, db: _orm.gerar_async(id_usuario=id_usuario, tp_apuracao='K')),  # K - Cripto
                ]
                results = loop.run_until_complete(asyncio.gather(*tasks))
            finally:
                try:
                    loop.close()
                except:
                    pass

        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            pass

    @classmethod
    @asyncio.coroutine
    async def gerar_async(cls, db: _orm.Session, id_usuario: int, tp_apuracao: str, calc_vlr_superior: str = None) -> None:
        cls.gerar(id_usuario=id_usuario, tp_apuracao=tp_apuracao, calc_vlr_superior=calc_vlr_superior)

    @classmethod
    async def gerar(cls, db: _orm.Session, id_usuario: int, tp_apuracao: str, calc_vlr_superior: str = None) -> None:
        try:

            dt_atual = pegar_data_atual(istext=False)
            ano_atual = converter_datetime_str(data=dt_atual, fmt='%Y')
            mes_atual = converter_datetime_str(data=dt_atual, fmt='%m')

            if cls.get_total(id_usuario=id_usuario, categoria=tp_apuracao, ano_mes_ini=str(ano_atual+mes_atual)) > 0:
                return

            if tp_apuracao == 'C' and not calc_vlr_superior:
                config = UsuarioConfig.get_by_tipo(id_usuario=id_usuario, tipo='APURACAO_COMPENSAR_PREJUIZO')
                calc_vlr_superior = config.valor if config else 'S'

            if tp_apuracao == "C": calc_vlr_superior = calc_vlr_superior  # Acao Comum
            elif tp_apuracao == "D": calc_vlr_superior= "N"  # Acao DayTrade
            elif tp_apuracao == "F": calc_vlr_superior = "N"  # FII
            elif tp_apuracao == "E": calc_vlr_superior = "N"  # ETF Comum
            elif tp_apuracao == "G": calc_vlr_superior = "N"  # ETF DayTrade
            elif tp_apuracao == "I": calc_vlr_superior = "N"  # BDR Comum
            elif tp_apuracao == "J": calc_vlr_superior = "N"  # BDR DayTrade
            elif tp_apuracao == "K": calc_vlr_superior = "N"  # Cripto
            if not calc_vlr_superior: calc_vlr_superior = "N"

            rows = UsuarioApuracao.get_all(id_usuario=id_usuario, tipo='M', categoria=tp_apuracao)
            lista_apuracao = [[str(row.ano_mes), float(row.valor) if row.valor else 0.0] for row in rows]

            lista_acao_lanc = []
            lista_acao_oper = []
            if tp_apuracao == "C" or tp_apuracao == "D":  # Acoes C-Comum e D-DayTrade
                rows = UsuarioACAOEmpresaLancamento.buscar_todos(id_usuario=id_usuario, tipo="V", troca="N")
                lista_acao_lanc = [[int(row['ID']), str(row['DATA'])[0:6], float(row['VLRTXIRRF']) if row['VLRTXIRRF'] else 0.0] for row in rows]
                rows = UsuarioACAOEmpresaOperacao.buscar_todos(id_usuario=id_usuario, categoria=tp_apuracao, tipo="V", troca="N")
                lista_acao_oper = [[int(row['ID']), int(row['IDLANC']), str(row['DATA'])[0:6], float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0, float(UsuarioACAOEmpresaOperacao.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO'])))] for row in rows]

            lista_fii_lanc = []
            if tp_apuracao == 'F':  # FII F-Fundo
                rows = UsuarioFiiFundoImobLancamento.buscar_todos(id_usuario=id_usuario, tipo="V", troca="N")
                lista_fii_lanc = [[int(row['ID']), str(row['DATA'])[0:6], float(row['VLRTXIRRF']) if row['VLRTXIRRF'] else 0.0, float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0, float(UsuarioFiiFundoImobLancamento.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO'])))] for row in rows]

            lista_etf_lanc = []
            lista_etf_oper = []
            if tp_apuracao == 'E' or tp_apuracao == 'G':  # ETF E-Comum e G-DayTrade
                rows = UsuarioETFIndiceLancamento.buscar_todos(id_usuario=id_usuario, tipo="V", troca="N")
                lista_etf_lanc = [[int(row['ID']), str(row['DATA'])[0:6], float(row['VLRTXIRRF']) if row['VLRTXIRRF'] else 0.0] for row in rows]
                rows = None
                if tp_apuracao == "E": rows = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, categoria='C', tipo="V", troca="N")
                if tp_apuracao == "G": rows = UsuarioETFIndiceOperacao.buscar_todos(id_usuario=id_usuario, categoria='D', tipo="V", troca="N")
                lista_etf_oper = [[int(row['ID']), int(row['IDLANC']), str(row['DATA'])[0:6], float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0, float(UsuarioETFIndiceOperacao.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO'])))] for row in rows]

            lista_bdr_lanc = []
            lista_bdr_oper = []
            if tp_apuracao == 'I' or tp_apuracao == 'J':  # BDR I-Comum e J-DayTrade
                rows = UsuarioBDREmpresaLancamento.buscar_todos(id_usuario=id_usuario, tipo="V", troca="N")
                lista_bdr_lanc = [[int(row['ID']), str(row['DATA'])[0:6], float(row['VLRTXIRRF']) if row['VLRTXIRRF'] else 0.0] for row in rows]
                rows = None
                if tp_apuracao == "I": rows = UsuarioBDREmpresaOperacao.buscar_todos(id_usuario=id_usuario, categoria='C', tipo="V", troca="N")
                if tp_apuracao == "J": rows = UsuarioBDREmpresaOperacao.buscar_todos(id_usuario=id_usuario, categoria='D', tipo="V", troca="N")
                lista_bdr_oper = [[int(row['ID']), int(row['IDLANC']), str(row['DATA'])[0:6], float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0, float(UsuarioBDREmpresaOperacao.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO'])))] for row in rows]

            lista_cripto_lanc = []
            if tp_apuracao == 'K':  # CRIPTO K-Cripto
                rows = UsuarioCriptoLancamento.buscar_todos(id_usuario=id_usuario, tipo="V")
                lista_cripto_lanc = [[int(row['ID']), str(row['DATA'])[0:6], 0.0, float(row['TOTVLRCUSTO']) if row['TOTVLRCUSTO'] else 0.0, float(UsuarioCriptoLancamento.calcular_vlr_valorizacao(tipo=row['TIPO'], quant=float(row['QUANT']), vlr_preco_medio=float(row['VLRPRECOMEDIO']), tot_vlr_custo=float(row['TOTVLRCUSTO'])))] for row in rows]

            anos = []
            try:

                anos.append(ano_atual + mes_atual)
                if lista_apuracao: anos.append(min(str(row[0]) for row in lista_apuracao))
                if lista_acao_lanc: anos.append(min(str(row[1]) for row in lista_acao_lanc))
                if lista_fii_lanc: anos.append(min(str(row[1]) for row in lista_fii_lanc))
                if lista_etf_lanc: anos.append(min(str(row[1]) for row in lista_etf_lanc))
                if lista_bdr_lanc: anos.append(min(str(row[1]) for row in lista_bdr_lanc))
                if lista_cripto_lanc: anos.append(min(str(row[1]) for row in lista_cripto_lanc))

                menor = min(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')
                maior = max(int(str(ano)[:4]) for ano in anos if ano and str(ano).strip() != '')

            except:
                menor = None
                maior = None

            lista = []
            vlr_saldo = 0.0

            for ano in range(menor, maior+1):
                for mes in range(1, 13):

                    if int(ano) == int(ano_atual) and int(mes) > int(mes_atual): break

                    vlr_apurado = 0.0
                    vlr_venda = 0.0
                    vlr_a_compensar = 0.0
                    vlr_resultado = 0.0
                    vlr_imposto_a_pagar = 0.0
                    vlr_imposto_pago = 0.0
                    vlr_imposto_devido = 0.0
                    ano_mes = str(ano) + str(mes).zfill(2)

                    if (tp_apuracao == "C" or tp_apuracao == "D") and lista_acao_oper:  # Acoes C-Comum e D-DayTrade
                        for oper in lista_acao_oper:
                            if str(oper[2]) == str(ano_mes):
                                vlr_apurado += float(oper[4])
                                vlr_venda += float(oper[3])
                                vlr_imposto_pago += sum(float(row[2]) for row in lista_acao_lanc if str(row[1]) == str(ano_mes) and int(row[0]) == int(oper[1]))

                    elif tp_apuracao == 'F' and lista_fii_lanc:  # FII F-Fundo
                        for oper in lista_fii_lanc:
                            if str(oper[1]) == str(ano_mes):
                                vlr_apurado += float(oper[4])
                                vlr_venda += float(oper[3])
                                vlr_imposto_pago += float(oper[2])

                    elif (tp_apuracao == 'E' or tp_apuracao == 'G') and lista_etf_oper:  # ETF E-Comum e G-DayTrade
                        for oper in lista_etf_oper:
                            if str(oper[2]) == str(ano_mes):
                                vlr_apurado += float(oper[4])
                                vlr_venda += float(oper[3])
                                vlr_imposto_pago += sum(float(row[2]) for row in lista_etf_lanc if str(row[1]) == str(ano_mes) and int(row[0]) == int(oper[1]))

                    elif (tp_apuracao == 'I' or tp_apuracao == 'J') and lista_bdr_oper:  # BDR I-Comum e J-DayTrade
                        for oper in lista_bdr_oper:
                            if str(oper[2]) == str(ano_mes):
                                vlr_apurado += float(oper[4])
                                vlr_venda += float(oper[3])
                                vlr_imposto_pago += sum(float(row[2]) for row in lista_bdr_lanc if str(row[1]) == str(ano_mes) and int(row[0]) == int(oper[1]))

                    elif tp_apuracao == 'K' and lista_cripto_lanc:  # CRIPTO K-Cripto
                        for oper in lista_cripto_lanc:
                            if str(oper[1]) == str(ano_mes):
                                vlr_apurado += float(oper[4])
                                vlr_venda += float(oper[3])
                                vlr_imposto_pago += float(oper[2])

                    if lista_apuracao:
                        vlr = sum(float(row[1]) for row in lista_apuracao if str(row[0]) == str(ano_mes))
                        vlr_apurado += vlr
                        vlr_venda += vlr

                    if vlr_apurado <= 0.0:
                        vlr_saldo += vlr_apurado
                    elif vlr_apurado > 0.0:
                        if calc_vlr_superior == "N":
                            vlr_saldo += vlr_apurado
                        elif calc_vlr_superior == "S" and vlr_venda > 20000.00:
                            vlr_saldo += vlr_apurado

                    if vlr_saldo < 0.00: vlr_a_compensar = vlr_saldo
                    if vlr_saldo > 0.00: vlr_resultado  = vlr_saldo

                    if tp_apuracao == "C" and vlr_resultado > 0.00 and vlr_venda > 20000.0: vlr_imposto_a_pagar = (vlr_resultado * 15.0) / 100  # Acao Comum
                    elif tp_apuracao == "D" and vlr_resultado > 0.0: vlr_imposto_a_pagar = (vlr_resultado * 20.0) / 100  # Acao DayTrade
                    elif tp_apuracao == "F" and vlr_resultado > 0.0: vlr_imposto_a_pagar = (vlr_resultado * 20.0) / 100  # FII
                    elif tp_apuracao == "E" and vlr_resultado > 0.0: vlr_imposto_a_pagar = (vlr_resultado * 15.0) / 100  # ETF Comum
                    elif tp_apuracao == "G" and vlr_resultado > 0.0: vlr_imposto_a_pagar = (vlr_resultado * 20.0) / 100  # ETF DayTrade
                    elif tp_apuracao == "I" and vlr_resultado > 0.0: vlr_imposto_a_pagar = (vlr_resultado * 15.0) / 100  # BDR Comum
                    elif tp_apuracao == "J" and vlr_resultado > 0.0: vlr_imposto_a_pagar = (vlr_resultado * 20.0) / 100  # BDR DayTrade
                    elif tp_apuracao == "K" and vlr_resultado > 0.00 and vlr_venda > 35000.0: # Cripto
                        if vlr_resultado  <= 5000000: vlr_imposto_a_pagar = (vlr_resultado * 15.0) / 100   # Até R$ 5 milhões = 15%
                        elif vlr_resultado > 5000000  and vlr_resultado <= 10000000: vlr_imposto_a_pagar = (vlr_resultado * 17.5) / 100   # De R$ 5 milhões a R$ 10 milhões = 17,5%
                        elif vlr_resultado > 10000000 and vlr_resultado <= 30000000: vlr_imposto_a_pagar = (vlr_resultado * 20.0) / 100   # De R$ 10 milhões a R$ 30 milhões = 20%
                        elif vlr_resultado > 30000000: vlr_imposto_a_pagar = (vlr_resultado * 22.5) / 100   # Acima de R$ 30 milhões              22,5%

                    if vlr_imposto_a_pagar > 0.0: vlr_imposto_devido = vlr_imposto_a_pagar - vlr_imposto_pago

                    apur_calc = UsuarioApuracaoCalculada()
                    apur_calc.id_usuario = id_usuario
                    apur_calc.categoria = tp_apuracao
                    apur_calc.ano_mes = ano_mes
                    apur_calc.vlr_venda = float(vlr_venda)
                    apur_calc.vlr_lucro_apurado = float(vlr_apurado)
                    apur_calc.vlr_prejuizo_compensar = float(vlr_a_compensar)
                    apur_calc.vlr_base_calculo = float(vlr_resultado)
                    apur_calc.vlr_ir_devido = float(vlr_imposto_devido)
                    apur_calc.vlr_ir_pago = float(vlr_imposto_pago)
                    apur_calc.vlr_ir_pagar = float(vlr_imposto_a_pagar)
                    lista.append(apur_calc)

                    if vlr_saldo > 0.0: vlr_saldo = 0.0
                    if tp_apuracao == "K": vlr_saldo = 0.0  # Cripto # não compensar prejuizo

            cls.excluir_tudo_por_categoria(id_usuario=id_usuario, categoria=tp_apuracao, commit=True)
            db.add_all(lista)
            db.commit()

        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            pass

    @classmethod
    async def get_all(cls, db: _orm.Session, id_usuario: int = None, categoria: str = None, ano_mes_ini: str = None, ano_mes_fim: str = None):
        try:
            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if categoria: filters.append(cls, db: _orm.categoria == categoria)
            if ano_mes_ini: filters.append(cls, db: _orm.ano_mes >= ano_mes_ini)
            if ano_mes_fim: filters.append(cls, db: _orm.ano_mes <= ano_mes_fim)
            return cls.query.filter(*filters).order_by(cls, db: _orm.ano_mes).all()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def get_total(cls, db: _orm.Session, id_usuario: int = None, categoria: str = None, ano_mes_ini: str = None, ano_mes_fim: str = None):
        try:
            filters = []
            if id_usuario: filters.append(cls, db: _orm.id_usuario == id_usuario)
            if categoria: filters.append(cls, db: _orm.categoria == categoria)
            if ano_mes_ini: filters.append(cls, db: _orm.ano_mes >= ano_mes_ini)
            if ano_mes_fim: filters.append(cls, db: _orm.ano_mes <= ano_mes_fim)
            return cls.query.filter(*filters).count()
        except Exception as e:
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo_por_categoria(cls, db: _orm.Session, id_usuario: int, categoria: str, commit: bool = True):
        try:
            query = "DELETE FROM TBAPURACAO_CALCULADA WHERE IDUSUARIO = :IDUSUARIO AND CATEGORIA = :CATEGORIA"
            params = {'IDUSUARIO': id_usuario, 'CATEGORIA': categoria}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir_tudo(cls, db: _orm.Session, id_usuario: int, commit: bool = True):
        try:
            query = "DELETE FROM TBAPURACAO_CALCULADA WHERE IDUSUARIO = :IDUSUARIO"
            params = {'IDUSUARIO': id_usuario}
            db.execute(query, params)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def salvar(cls, db: _orm.Session, commit: bool = True):
        try:
            db.add(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise

    @classmethod
    async def excluir(cls, db: _orm.Session, commit: bool = True):
        try:
            db.delete(self)
            if commit: db.commit()
        except Exception as e:
            db.rollback()
            #  LogErro.registrar(texto=str(e), arqv=str(os.path.basename(__file__).replace('.py', '') + '.' + __class__.__name__), linha=int(sys.exc_info()[-1].tb_lineno))
            raise
