from collections import defaultdict
from datetime import timedelta
import random

rodasConvergentes = lambda placa: 'Convergente' if placa in caminhoesConvergentes else 'Divergente'
acertarDecimais = lambda numero: float('{:.2f}'.format(numero))

caminhoesConvergentes = ['MPE4353','MRH9080','MQJ3903','MRB6679','MRB6686','MRB6700','MRV5832','MRV5840','MSI9821','MSI9822','MPQ5377','MQC0210','OVF5826','OVK9112','OYD5653','MQQ6549','OCY1477','PPP5906','PPA5J10','RBC4J87','RBC5A23','RBC5A50','RBC5B44']

def checarSulco(sulco):
	if sulco == 0.0: return 0.0
	novoSulco = sulco + random.triangular(.2, .35) 
	sulcoAlternativo = sulco + random.triangular(.1, .4)
	return sulcoAlternativo if novoSulco <= 1.6 else novoSulco
	
def subtrairPorValorAletorio(sulcos):
	novoSulco = [acertarDecimais(checarSulco(sulco)) for sulco in sulcos]
	return novoSulco

def criarData(dataUltimaInspecao):
	diaDaInspecao = dataUltimaInspecao.day
	horarioAleatorio = [random.randint(7,11),random.randint(0,60),random.randint(0,60)]
	return dataUltimaInspecao + timedelta(days=random.randint(32-diaDaInspecao,35), 
		hours=horarioAleatorio[0], minutes=horarioAleatorio[1], seconds=horarioAleatorio[2])

def calibragemEncontrada(calibragemIdeal):
	calibragemMinima = calibragemIdeal - 5
	return random.randint(calibragemMinima, calibragemIdeal)

def darLaudoDoPneu(sulcos):
	valorMinimo = [(sulco <= 2.5) and (sulco > 0) for sulco in sulcos]
	return 'Remover Pneu' if True in valorMinimo else 'Pneu Ok'

def cirarNovaInspecaoApartirDaAntiga(inspecao):
	novasInspecao = inspecao.copy()
	dataInspecao = novasInspecao['data'][0]
	placa = novasInspecao.pop('placa')[0]

	novasInspecao['sulcos'] = novasInspecao['sulcos'].transform(subtrairPorValorAletorio)
	novasInspecao['data'] = criarData(dataInspecao)
	novasInspecao['calibragem_encontrada'] = novasInspecao['calibragem_ideal'].transform(calibragemEncontrada)
	novasInspecao['alinhamento'] = rodasConvergentes(placa)
	novasInspecao['laudo'] = novasInspecao['sulcos'].transform(darLaudoDoPneu)
	
	return novasInspecao


def retornarNovasInspecoes(caminhoes, inspecoesDoMesAnterior):
	novasInspecoes = defaultdict()
	for caminhao in caminhoes:
		try:
			inspecaoAnterior = inspecoesDoMesAnterior.groupby('placa').get_group(caminhao)
		except:
			continue
		
		novasInspecoes[caminhao] = cirarNovaInspecaoApartirDaAntiga(inspecaoAnterior)
	
	return novasInspecoes