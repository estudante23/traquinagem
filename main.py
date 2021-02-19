import pandas as pd
from gerarInspecoes import criarNovasInspecoes
from acessarHbsis import HBSIS
dataframe = pd.read_csv('pneu-inspecao.csv', sep=';', encoding='iso-8859-1')


novasInspecoes = criarNovasInspecoes(dataframe, 9)
hbsis = HBSIS()


for placa, inspecao in novasInspecoes.items():
	data = inspecao.pop('data')[0]
	hbsis.comecarInspecao(data.strftime('%d/%m/%Y %H:%M:%S'))
	hbsis.registrarPlaca(placa)
	validacao, pneus, elements = hbsis.validarIgualdadeDosPneus(list(inspecao.index))

	if validacao == False:
		hbsis.preencherCamposDaInspecao(elements, inspecao)
		print('Função se houver diferença')
	else:
		hbsis.preencherCamposDaInspecao(elements, inspecao)
		print('Continuar normal')
