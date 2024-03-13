from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def criar_email(numero_inicial, numero_final):
    # Inicializar o navegador
    driver = webdriver.Chrome(executable_path='caminho_para_seu_chromedriver')
    driver.get('https://accounts.google.com/signup')
    time.sleep(2)

    for i in range(numero_inicial, numero_final + 1):
        email = 'phnegocios0' + str(i) + '@gmail.com'
        senha = 'Phng@' + str(i)

        # Preencher o formulário
        driver.find_element_by_id('firstName').send_keys('Seu')
        driver.find_element_by_id('lastName').send_keys('Nome')
        driver.find_element_by_id('username').send_keys(email)
        driver.find_element_by_name('Passwd').send_keys(senha)
        driver.find_element_by_name('ConfirmPasswd').send_keys(senha)
        
        # Clicar em Próxima etapa
        driver.find_element_by_id('accountDetailsNext').click()
        time.sleep(2)

        # Realizar outras ações conforme necessário, como adicionar um número de telefone, etc.

        # Finalizar a criação de conta
        driver.find_element_by_id('submitbutton').click()
        time.sleep(5)  # Tempo para a conta ser criada

        # Voltar para a página inicial para criar a próxima conta
        driver.get('https://accounts.google.com/signup')
        time.sleep(2)

    driver.quit()

# Chamando a função para criar emails de 110 até 250
criar_email(110, 250)
