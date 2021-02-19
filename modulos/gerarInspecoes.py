import pandas as pd
import re
from modulos.retornarNovasInspecoes import retornarNovasInspecoes


with open('arquivos\\frota.txt') as fp:
	frota = fp.read().splitlines()
	frota = [re.sub('-', '', placa) if '-' in placa else placa for placa in frota]


def encontrarVeiculosNaoInspecionados(inspecoes, mes):
	inspecionados = inspecoes.loc[inspecoes.data.dt.month == mes]['placa'].unique()
	naoInspecionados = list(set([placa if placa not in inspecionados else None for placa in frota]))
	naoInspecionados.remove(None)
	return naoInspecionados

def criarNovasInspecoes(inspecoesDf, mes):
	inspecaoAnterior = inspecoesDf.loc[inspecoesDf.data.dt.month == mes-1]
	veiculosNaoInspecionados = encontrarVeiculosNaoInspecionados(inspecoesDf, mes)
	novasInspecoes = retornarNovasInspecoes(veiculosNaoInspecionados, inspecaoAnterior)
	return novasInspecoes