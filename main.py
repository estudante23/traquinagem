import pandas as pd
from gerarInspecoes import criarNovasInspecoes
from acessarHbsis import HBSIS
dataframe = pd.read_csv(r'C:\Users\Frota\Downloads\pneu-inspecao.csv', sep=';', encoding='iso-8859-1')


hbsis = HBSIS()
novasInspecoes = criarNovasInspecoes(dataframe, 9)

for placa, inspecao in novasInspecoes.items():
	data = inspecao.data[0]
	hbsis.comecarInspecao(data.strftime('%d/%m/%Y %H:%M:%S'))
	hbsis.registrarPlaca(placa)
	validacao, pneus = hbsis.validarIgualdadeDosPneus(list(inspecao.index))
	
	if validacao == False:
		print('Função se houver diferença')
	else:
		print('Continuar normal')
