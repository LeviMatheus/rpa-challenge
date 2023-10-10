# region Imports
from selenium import webdriver
# Importando o gerenciador de driver do chrome
# Para instalar use: pip install webdriver_manager
from webdriver_manager.chrome import ChromeDriverManager
# Importando os serviços do Selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
# Importando a biblioteca de tempo para usarmos delays
import time
# Importando a biblioteca do sistema operacional para usarmos alguns métodos de diretórios
import os
# Importando a biblioteca openpyxl pois facilita diversas operações com Excel
import openpyxl
# Importando a minha própria biblioteca para Logs
from logger import Logger
#endregion

# region Configurações Selenium

# Instanciando minha classe de logs
log = Logger()
# Vincula o driver do Chrome e instala se precisar
servico_chrome = Service(ChromeDriverManager().install(),
                         port=2435, service_args=['--log-level=INFO'])
# Configuração para definir o diretório de downloads
pasta_downloads = os.path.expanduser("~\Downloads")
print(f"Pasta de download: {pasta_downloads} \n")
# Configurando as opções do Selenium
opcoes = Options()
opcoes.page_load_strategy = 'normal'
# Mudando a pasta de downloads padrão
opcoes.add_experimental_option("prefs", {
    "download.default_directory": f"{pasta_downloads}"
})
# Inicia uma sessão webdriver, e vincula a uma variável navegador
navegador = webdriver.Chrome(service=servico_chrome, options=opcoes)

# endregion

# region Abrir navegador na url Challenge

# Declarando a url da página do Challenge
url_challenge = "https://rpachallenge.com/"

# Navegando usando o método get do Selenium
log.log(f'Abrindo o navegador na url {url_challenge} \n')
navegador.get(url_challenge)

# Aguardando a página ser carregada
log.log('Aguardando a página carregar \n')
# Para tempos fixos eu poderia usar time.sleep(5) também
navegador.implicitly_wait(5)

# Procurando o logo do site para garantir que abriu a página corretamente
log.log(f'Procurando o logo do RPA Challenge para garantir que abriu \n')
logo_challenge = navegador.find_element(
    By.XPATH, "//a[contains(text(),'RPA Challenge')]")

# Configurando o timeout de 10 segundos das atividades de encontrar elementos
espera = WebDriverWait(navegador, timeout=10)
# Aguardando o elemento aparecer
espera.until(lambda d: logo_challenge.is_displayed())

# endregion

# region Iniciar e Baixar planilha
log.log(f'Procurando o botão de Start e iniciando \n')
bt_start = navegador.find_element(
    By.XPATH, "//button[contains(text(),'Start')]")
espera.until(lambda d: bt_start.is_displayed())
bt_start.click()

# Pausa entre o início e o download
navegador.implicitly_wait(1)

log.log(f'Procurando o botão de download da planilha \n')
bt_download = navegador.find_element(
    By.XPATH, "//a[contains(text(),'Download')]")
espera.until(lambda d: bt_download.is_displayed())
bt_download.click()

# Aguardando dinamicamente o download ser concluído
tempo_de_espera = 15
while tempo_de_espera > 0:
    if "challenge.xlsx" in os.listdir(pasta_downloads):
        log.log("O arquivo challenge.xlsx foi baixado com sucesso! \n")
        break
    time.sleep(1)
    tempo_de_espera -= 1
else:
    log.log("O arquivo challenge.xlsx não foi baixado dentro do tempo limite. \n")
    quit()

# Pausa fixa para poder deixar o processo mais estável de que encontrou o arquivo
time.sleep(5)

# endregion

# region Ler o relatório baixado
caminho_arquivo_excel = os.path.join(pasta_downloads, "challenge.xlsx")
# Carregando todo o workbook relatório para uma variável
workbook = openpyxl.load_workbook(caminho_arquivo_excel)
# Selecionando a única aba existente
planilha_atual = workbook.active

log.log(f"Aba {planilha_atual.title} do relatório lido com sucesso")
# endregion

# region Preencher campos

try:
    for indice,linha in enumerate(planilha_atual.values):
        # Ignorar cabeçalho
        if indice == 0:
            # Pulando o cabeçalho do relatório
            log.log("Pulando a leitura do cabeçalho do relatório")
            continue
        # Aqui eu faço o unpack das celulas para poder escrever depois
        # Poderia usar o Pandas também, transformando em um dataframe
        first_name, last_name, company_name, role, address, email, phone_number, _ = linha
        if first_name is None:
            break
        else:
            # Endereço
            log.log(f'Procurando o campo de endereço e digitando \n')
            input_endereco=navegador.find_element(
                By.XPATH, "//input[@ng-reflect-name='labelAddress']")
            espera.until(lambda d: input_endereco.is_displayed())
            input_endereco.click()
            input_endereco.send_keys(address)
            # SE EU QUISER COLETAR O TEXTO DO ELEMENTO
            # texto_endereco = input_endereco.text

            # Nome
            log.log(f'Procurando o campo de nome e digitando \n')
            input_endereco= navegador.find_element(By.XPATH, "//input[@ng-reflect-name='labelFirstName']")
            espera.until(lambda d: input_endereco.is_displayed())
            input_endereco.click()
            input_endereco.send_keys(first_name)

            # Sobrenome
            log.log(f'Procurando o campo de sobrenome e digitando \n')
            input_endereco=navegador.find_element(
                By.XPATH, "//input[@ng-reflect-name='labelLastName']")
            espera.until(lambda d: input_endereco.is_displayed())
            input_endereco.click()
            input_endereco.send_keys(last_name)

            # Email
            log.log(f'Procurando o campo de email e digitando \n')
            input_endereco = navegador.find_element(
                By.XPATH, "//input[@ng-reflect-name='labelEmail']")
            espera.until(lambda d: input_endereco.is_displayed())
            input_endereco.click()
            input_endereco.send_keys(email)

            # Cargo
            log.log(f'Procurando o campo de cargo e digitando \n')
            input_endereco = navegador.find_element(
                By.XPATH, "//input[@ng-reflect-name='labelRole']")
            espera.until(lambda d: input_endereco.is_displayed())
            input_endereco.click()
            input_endereco.send_keys(role)

            # Telefone
            log.log(f'Procurando o campo de telefone e digitando \n')
            input_endereco = navegador.find_element(
                By.XPATH, "//input[@ng-reflect-name='labelPhone']")
            espera.until(lambda d: input_endereco.is_displayed())
            input_endereco.click()
            input_endereco.send_keys(phone_number)

            # Nome da empresa
            log.log(f'Procurando o campo de empresa e digitando \n')
            input_endereco = navegador.find_element(
                By.XPATH, "//input[@ng-reflect-name='labelCompanyName']")
            espera.until(lambda d: input_endereco.is_displayed())
            input_endereco.click()
            input_endereco.send_keys(company_name)

            # Click enviar
            log.log(f'Procurando o botão de enviar e clicando \n')
            input_endereco= navegador.find_element(By.XPATH, "//input[@value='Submit']")
            espera.until(lambda d: input_endereco.is_displayed())
            input_endereco.click()

            # Pausar para o processo não correr rápido demais
            log.log(f'Linha {linha} concluída, aguardando 2 segundos para preencher novamente \n')
            time.sleep(2)

except Exception as err:
    # Aqui eu poderia criar uma rotina para tratar a exceção de preencher os campos, como tentar novamente ou algo do tipo
    log.log(f"Falha ao tentar preencher campos do RPA Challenge. Erro:  {err}")
    quit()
finally:
    # Aqui eu poderia criar uma rotina para tratar a exceção de preencher os campos, como tentar novamente ou algo do tipo
    log.log(f"Fim preenchimento dos campos")

# endregion

# region Rotina do fim do processo

time.sleep(5)
log.log(f'Processo finalizado. Os logs da execução foram gerados \n')

# Fechar a sessão atual do navegador
navegador.quit()
# Fechar a planilha
workbook.close()

# endregion
