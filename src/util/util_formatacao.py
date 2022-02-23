# -*- coding: utf-8 -*-

# prov_total = f"{prov_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def decimal_to_str(valor: float = 0.0) -> str:
    return "{0:,.2f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def decimal_cripto_to_str(valor: float = 0.0) -> str:
    return "{0:,.8f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def decimal_cripto_curto_to_str(valor: float = 0.0) -> str:
    return "{0:,.5f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def decimal_prov_to_str(valor: float = 0.0) -> str:
    return str(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def inteiro_to_str(valor: float = 0.0) -> str:
    return "{0:,.0f}".format(valor).replace(",", "X").replace(".", ",").replace("X", ".")

def decimal_resumido(valor, fator: float = 1000, convertStr: bool = True):
    try:
        valor = float(valor) if valor else 0.0
        if valor == 0.0:
            if convertStr:
                return '- '
            return float(valor)
        valor = (valor / fator)
        if fator == 1000:
            if convertStr:
                return decimal_to_str(valor=float(valor)) + ' M'
            return float(valor)
        elif fator == 1000000:
            if convertStr:
                return decimal_to_str(valor=float(valor)) + ' B'
            return float(valor)
        else:
            if convertStr:
                return decimal_to_str(valor=float(valor))
            return float(valor)
    except:
        return float(valor)

if (__name__ == '__main__'):


    print('12555.99', '=', decimal_to_str(valor=12555.99))

    # print()
    # print('decimal_to_str')
    # print('0.00', '=', decimal_to_str(valor=0.00))
    # print('1000.00', '=', decimal_to_str(valor=1000.00))
    # print('1000.5555555', '=', decimal_to_str(valor=1000.5555555))
    #
    # print()
    # print('inteiro_to_str')
    # print('0.00', '=', inteiro_to_str(valor=0.00))
    # print('1000.00', '=', inteiro_to_str(valor=1000.00))
    # print('1000.5555555', '=', inteiro_to_str(valor=1000.5555555))