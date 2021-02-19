from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from arquivos.dicionarioDePaths import paths
from modulos.retornarNovasInspecoes import criarNovaInspecaoApartirDaAntiga

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
driver = webdriver.Chrome(executable_path='C:\\SeleniumWebDriver\\chromedriver.exe', options=options)
wait = WebDriverWait(driver, 20)

class HBSIS():
    def __init__(self):
        driver.get('http://frotas.hbsis.com.br/login')
        driver.find_element_by_xpath(paths['loginUsuario']).send_keys(17846319736)
        driver.find_element_by_xpath(paths['loginSenha']).send_keys(123456)
        driver.find_element_by_xpath(paths['loginConfirm']).click()

        acessarTabelaDeInspecao()

    def comecarInspecao(self, data, placa):
        self.placa = placa
        driver.implicitly_wait(5)
        clicarEmBotao(paths['botaoNovo'])
        escreverConferenteEselecionar()
        escreverData(data)
        clicarEmBotao(paths['botaoAvancar'])
        esperarElemento('placaVeiculo').send_keys(placa)
        clicarEmBotao(paths['placaSelecionada'])

    def lancarInspecao(self, inspecao):
        elements = driver.find_elements_by_class_name('label')
        pneusSemInspecao = []
        for element in elements:
            element.click()
            try:
                preencherCamposDaInspecao(inspecao.loc[element.text]) 
            except:
                pneusSemInspecao.append(element)

        return pneusSemInspecao

    def lancarPneusSemInspecao(self, elements, inspecoesDf):
        pneusSemInspecao = [element.text for element in elements]
        for element in elements:
            inspecaoDoPneu = inspecoesDf.loc[element.text]
            novaInspecaoDoPneu = criarNovaInspecaoApartirDaAntiga(inspecaoDoPneu, self.placa)
            print(novaInspecaoDoPneu                    )
            element.click()
            preencherCamposDaInspecao(novaInspecaoDoPneu)
            


def acessarTabelaDeInspecao():
    driver.implicitly_wait(2)
    while driver.current_url != 'http://frotas.hbsis.com.br/pneu-inspecao':
        try:
            action = ActionChains(driver)
            dropOutInspecao = esperarElemento('dropOutInspecao')
            dropOutInspecao.click()
            action.move_to_element(dropOutInspecao)
            action.click(esperarElemento('inspecaoLiBotao'))
            action.perform()
        except:
            acessarTabelaDeInspecao()


def preencherCamposDaInspecao(inspecaoDoPneu):
    preencherCamposDaCalibragem(inspecaoDoPneu['calibragem_encontrada'], inspecaoDoPneu['calibragem_ideal'])
    preencherSulcos(inspecaoDoPneu['sulcos'])
    selecionarAlinhamento(inspecaoDoPneu['alinhamento'])
    selecionarLaudo(inspecaoDoPneu['laudo'])
    clicarEmBotao(paths['adicionarInspecao'])


def esperarElemento(path):
    return wait.until(EC.element_to_be_clickable((By.XPATH, paths[path])))

def preencherCamposDaCalibragem(calibragem_encontrada, calibragem_realizada):
    wait.until(EC.element_to_be_clickable((By.XPATH, paths['calibragemEncontrada']))).send_keys(str(calibragem_encontrada))
    wait.until(EC.element_to_be_clickable((By.XPATH, paths['calibragemRealizada']))).send_keys(str(calibragem_realizada))

def preencherSulcos(sulcos):
    for i in range(1,5):
        wait.until(EC.element_to_be_clickable((By.XPATH, paths['sulcos'](i)))).send_keys(str(sulcos[i-1]))        

def selecionarAlinhamento(alinhamento):
    options = driver.find_element_by_xpath(paths['alinhamento']).find_elements_by_tag_name('option')
    for option in options:
        if option.text == alinhamento:
            option.click()
            break

def selecionarLaudo(laudo):
    options = driver.find_element_by_xpath(paths['laudo']).find_elements_by_tag_name('option')
    for option in options:
        if option.text == laudo:
            option.click()
            break

def clicarEmBotao(path):
    wait.until(EC.element_to_be_clickable((By.XPATH, path))).click()

def escreverConferenteEselecionar():
    wait.until(EC.element_to_be_clickable((By.XPATH, paths['conferenteInput']))).send_keys('TARCIS')
    wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'td'))).click()

def escreverData(data):
    wait.until(EC.element_to_be_clickable((By.XPATH, paths['dataInput']))).send_keys(data)
    wait.until(EC.element_to_be_clickable((By.XPATH, paths['dataInput']))).send_keys(Keys.TAB)
