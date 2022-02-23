# -*- coding: utf-8 -*-
from typing import List
import json
from flask import jsonify


def get_json_retorno_metodo(rslt: str = 'NOK', msg: str = ''):
    # return jsonify({"data": {"Resultado": rslt, "Mensagem": msg}})
    return json.dumps({"data": {"Resultado": rslt, "Mensagem": msg}})


def get_json_retorno_dados(rslt: str = 'NOK', msg: str = '', dados: dict = {}):
    # return jsonify({"data": {"Resultado": rslt, "Mensagem": msg, "Dados": dados}})
    return json.dumps({"data": {"Resultado": rslt, "Mensagem": msg, "Dados": dados}})


def get_json_retorno_lista(rslt: str = 'NOK', msg: str = '', lista: List[str] = []):
    # return jsonify({"data": {"Resultado": rslt, "Mensagem": msg, "Lista": lista}})
    return json.dumps({"data": {"Resultado": rslt, "Mensagem": msg, "Lista": lista}})


def get_json_retorno_lista_erro(rslt: str = 'NOK', msg: str = '', existe: str = 'NAO', lista: List[str] = []):
    # return jsonify({"data": {"Resultado": rslt, "Mensagem": msg, "Existe": existe, "Lista": lista}})
    return json.dumps({"data": {"Resultado": rslt, "Mensagem": msg, "Existe": existe, "Lista": lista}})


def get_json_retorno_lista_coment(rslt: str = 'NOK', msg: str = '', pag_atual: str = '', pag_total: str = '', lista: List[str] = []):
    # return jsonify({"data": {"Resultado": rslt, "Mensagem": msg, "PagAtual": pag_atual, "PagTotal": pag_total, "Lista": lista}})
    return json.dumps({"data": {"Resultado": rslt, "Mensagem": msg, "PagAtual": pag_atual, "PagTotal": pag_total, "Lista": lista}})


def get_json_retorno_card(rslt: str = 'NOK', msg: str = '', quant: str = '', val_atual: str = '', val_valorizacao: str = '', perc_valorizacao: str = '', dthr_ult_atualizacao: str = ''):
    # return jsonify({"data": {"Resultado": rslt, "Mensagem": msg, "Quant": quant, "ValAtual": val_atual, "ValValorizacao": val_valorizacao, "PercValorizacao": perc_valorizacao, "DataHoraUltAtualizacao": dthr_ult_atualizacao}})
    return json.dumps({"data": {"Resultado": rslt, "Mensagem": msg, "Quant": quant, "ValAtual": val_atual, "ValValorizacao": val_valorizacao, "PercValorizacao": perc_valorizacao, "DataHoraUltAtualizacao": dthr_ult_atualizacao}})


def get_json_retorno_grid(rslt: str = 'NOK', msg: str = '', lista: List = []):
    # return jsonify({"data": {"Resultado": rslt, "Mensagem": msg, "Lista": lista}})
    return json.dumps({"data": {"Resultado": rslt, "Mensagem": msg, "Lista": lista}})
