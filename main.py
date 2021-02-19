import pandas as pd
from modulos.gerarInspecoes import criarNovasInspecoes
from modulos.limparCsv import limparTransformarDataframe
from acessarHbsis import HBSIS

dataframe = pd.read_csv('pneu-inspecao.csv', sep=';', encoding='iso-8859-1')
inspecoesDf = limparTransformarDataframe(dataframe)
novasInspecoes = criarNovasInspecoes(inspecoesDf, 9)
hbsis = HBSIS()


for placa, inspecao in novasInspecoes.items():
	if placa == 'QRL9J45':
		data = inspecao.pop('data')[0].strftime('%d/%m/%Y %H:%M:%S')
		hbsis.comecarInspecao(data, placa)
		pneusSemInspecao = hbsis.lancarInspecao(inspecao)

		if pneusSemInspecao != []:
			hbsis.lancarPneusSemInspecao(pneusSemInspecao, inspecoesDf)
