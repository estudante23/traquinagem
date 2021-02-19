import pandas as pd

with open(r'C:\Users\Frota\Documents\Projects\traquinagem\nomeDasColunas.txt') as fp:
	nomeDasColunas = fp.read().splitlines()

colunasParaRemover = ['centro_de_custo', 'modelo_pneu', 'conferente', 'dispersao','observacao', 'calibragem_encontrada', 'calibragem_realizada', 'sulco_min', 'eixo']

def transformarStringEmFloat(dataframe):
	colunasParaTransformar = ['sulco_1', 'sulco_2', 'sulco_3', 'sulco_4']
	for coluna in colunasParaTransformar:
		dataframe[coluna] = [float(valor.replace(',', '.')) for valor in dataframe[coluna].values]

	dataframe['sulcos'] = dataframe[colunasParaTransformar + ['posicao']].values.tolist()
	dataframe.drop(colunasParaTransformar, axis=1,inplace=True)

	return dataframe


def limparTransformarDataframe(dataframe):
	dataframe.columns = nomeDasColunas
	dataframe = dataframe.drop(colunasParaRemover, axis=1)
	dataframe.index = dataframe.pop('pneu_marcacao')
	dataframe.data = pd.to_datetime([data[0:10] for data in dataframe.data], dayfirst=True)
	dataframe = transformarStringEmFloat(dataframe)
	return dataframe