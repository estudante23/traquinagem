from collections import defaultdict
from datetime import timedelta
import random
from calendar import Calendar

calendario = Calendar().monthdayscalendar(2020, 9)
domingos = [semana[-1] if semana[-1] != 0 else None for semana in calendario]

rodasConvergentes = lambda placa: 'Convergente' if placa in caminhoesConvergentes else 'Divergente'
acertarDecimais = lambda numero: float('{:.2f}'.format(numero))

caminhoesConvergentes = ['MPE4353','MRH9080','MQJ3903','MRB6679','MRB6686','MRB6700','MRV5832','MRV5840','MSI9821','MSI9822','MPQ5377','MQC0210','OVF5826','OVK9112','OYD5653','MQQ6549','OCY1477','PPP5906','PPA5J10','RBC4J87','RBC5A23','RBC5A50','RBC5B44']

def checarSulco(sulco):
	if sulco == 0.0: return 0.0
	novoSulco = sulco + random.triangular(.15, .25) 
	sulcoAlternativo = sulco + random.triangular(.1, .4)
	return sulcoAlternativo if novoSulco <= 1.6 else novoSulco
	
def subtrairPorValorAletorio(sulcos):
	posicao = sulcos.pop(-1)
	novoSulco = [acertarDecimais(checarSulco(sulco)) for sulco in sulcos]
	return novoSulco if posicao != 'Estepe' else sulcos

def criarData(dataUltimaInspecao):
	diaDaInspecao = dataUltimaInspecao.day
	horarioAleatorio = [random.randint(7,11),random.randint(0,59),random.randint(0,59)]
	novaData = dataUltimaInspecao + timedelta(days=random.randint(32-diaDaInspecao,34), 
		hours=horarioAleatorio[0], minutes=horarioAleatorio[1], seconds=horarioAleatorio[2])
	return novaData + timedelta(days=1) if novaData in domingos else novaData

def calibragemEncontrada(calibragemIdeal):
	return random.randint(calibragemIdeal - 4, calibragemIdeal)

def darLaudoDoPneu(sulcos):
	valorMinimo = [(sulco <= 2.5) and (sulco > 0) for sulco in sulcos]
	return 'Remover imediatamente' if True in valorMinimo else 'Pneu OK'

def criarNovaInspecaoApartirDaAntiga(inspecao, placa):
	novasInspecoes = inspecao.copy()

	novasInspecoes['sulcos'] = novasInspecoes['sulcos'].transform(subtrairPorValorAletorio)
	novasInspecoes['calibragem_encontrada'] = novasInspecoes['calibragem_ideal'].transform(calibragemEncontrada)
	novasInspecoes['alinhamento'] = rodasConvergentes(placa)
	novasInspecoes['laudo'] = novasInspecoes['sulcos'].transform(darLaudoDoPneu)
	
	return novasInspecoes


def retornarNovasInspecoes(caminhoes, inspecoesDoMesAnterior):
	novasInspecoes = defaultdict()
	for caminhao in caminhoes:
		try:
			inspecaoAnterior = inspecoesDoMesAnterior.groupby('placa').get_group(caminhao)
		except:
			continue
		
		data = criarData(inspecaoAnterior.pop('data')[0])
		novasInspecoes[caminhao] = (data.strftime('%d/%m/%Y %H:%M:%S'), criarNovaInspecaoApartirDaAntiga(inspecaoAnterior, caminhao))
	
	return novasInspecoes