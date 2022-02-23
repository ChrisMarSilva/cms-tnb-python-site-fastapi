# -*- coding: utf-8 -*-
import datetime as dt
import pytz

def get_datetime(ano: int=None, mes: int=None, dia: int=None):
    if ano is None or mes is None or dia is None:
        tz = pytz.timezone('America/Sao_Paulo')
        return dt.datetime.now(tz=tz) # today
    return dt.datetime(ano, mes, dia).date()

def pegar_data(istext: bool=True, fmt: str='%Y%m%d', ano: int=None, mes: int=None, dia: int=None):
    return converter_datetime_str(data=get_datetime(ano=ano, mes=mes, dia=dia), istext=istext, fmt=fmt)

def pegar_data_atual(istext: bool=True, fmt: str='%Y%m%d'):  # %d/%m/%Y
    return converter_datetime_str(data=get_datetime(), istext=istext, fmt=fmt)

def pegar_hora_atual(istext: bool=True, fmt: str='%H%M%S'): # %H:%M:%S
    return converter_datetime_str(data=get_datetime(), istext=istext, fmt=fmt)

def pegar_data_hora_atual(istext: bool=True, fmt: str='%Y%m%d%H%M%S'):
    return converter_datetime_str(data=get_datetime(), istext=istext, fmt=fmt)

def converter_datetime_str(data, istext: bool=True, fmt: str= '%Y%m%d'): # : dt.datetime
    try:
        return data.strftime(fmt) if istext else data
    except:
        return ''

def converter_str_to_datetime(data: str='', fmt: str='%Y%m%d'):
    try:
        return dt.datetime.strptime(data, fmt)
    except:
        return ''

def adicionar_meses(meses: int=0):
    from dateutil.relativedelta import relativedelta
    return relativedelta(months=meses)

def adicionar_dias(dias: int=0):
    return dt.timedelta(days=dias)

def adicionar_minutos(minutos: int=0):
    return dt.timedelta(minutes=minutos)

def adicionar_segundos(segundos: int=0):
    return dt.timedelta(seconds=segundos)

def buscar_nome_mes_resumido(mes: int) -> str:
    if mes == 1: return "JAN"
    if mes == 2: return "FEV"
    if mes == 3: return "MAR"
    if mes == 4: return "ABR"
    if mes == 5: return "MAI"
    if mes == 6: return "JUN"
    if mes == 7: return "JUL"
    if mes == 8: return "AGO"
    if mes == 9: return "SET"
    if mes == 10: return "OUT"
    if mes == 11: return "NOV"
    if mes == 12: return "DEZ"
    return ""

def buscar_nome_semana(semana: int):
    if semana == 0: return "Segunda-Feira"
    if semana == 1: return "Terça-Feira"
    if semana == 2: return "Quarta-Feira"
    if semana == 3: return "Quinta-Feira"
    if semana == 4: return "Sexta-Feira"
    if semana == 5: return "Sábado"
    if semana == 6: return "Domingo"

if (__name__ == '__main__'):
    try:

        # from locale import setlocale, LC_ALL
        # from calendar import mdays, monthrange
        # setlocale(LC_ALL, '')
        # setlocale(LC_ALL, 'pt_BR.utf-8')
        # dt = dt.datetime.now()
        # mes_atual = int(dt.strftime('%m'))
        # ultimo_dia_mes = mdays[mes_atual]
        # formatacao1 = dt.strftime('%A, %d de %B de %Y') # sábado, 13 de julho de 2019
        # formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S') # 13/07/2019 11:21:20
        # print(formatacao1, formatacao2)
        # print(mes_atual, mdays[mes_atual])
        #
        # print(monthrange(2020,2))  # Retorna uma tupla contendo o número do dia na semana (0-6)# e último dia de fevereiro de 2020
        #
        # # Saída - (5, 29)
        # # O 5 significa que é um sábado
        # # O 29 significa que este é o último dia do mês
        # # O número do dia na semana vai de 0 a 6 (segunda é 0, domingo é 6).
        # # Caso queira retornar apenas um valor, você pode fazer o desempacotamento, assim:
        # dia_semana, ultimo_dia = monthrange(2020, 2)
        # dia_semana, ultimo_dia = monthrange(2020, 2)
        # print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)
        # ultimos_dias_de_meses_do_ano_atual = [monthrange(dt.datetime.now().year, mes)[1] for mes in range(1, 13)] # Você também pode criar uma lista, assim como mdays, contendo todos os últimos dias de meses do ano atual:
        # print(ultimos_dias_de_meses_do_ano_atual)         # Saída: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        pass

    except Exception as e:
        raise
    finally:
        pass

