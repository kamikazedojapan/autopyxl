from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Acessar o site
driver = webdriver.Chrome()
driver.get('https://url.com')

# Extrair todos os títulos
dados1 = driver.find_elements(By.XPATH,"tag[@attibuto='']")

# Extrair os preços
dados2 = driver.find_elements(By.XPATH,"//tag[@attibuto=''']")

# Inserir os títulos e preços na planilhas
book = openpyxl.Workbook()
celulares = book['Sheet']
celulares['A1'].value = 'Coluna1'
celulares['B1'].value = 'Coluna2'

for dado1, dado2 in zip(dados1, dados2):
    celulares.append([dado1.text, dado2.text])

book.save('Planilha.xlsx')