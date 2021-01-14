from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

class App:
    
    def __init__(self): 

        self.arr_produtos = ['Celular Samsung', 'Fones']
        self.driver = webdriver.Chrome(
            executable_path=os.getcwd() + os.sep + 'chromedriver.exe'
        )
        self.url = 'https://www.mercadolivre.com.br/'

    def iniciar(self):

        for produto in self.arr_produtos:

            self.driver.get(self.url)

            time.sleep(2)

            input_pesquisa = self.driver.find_element_by_xpath("//input[@class='nav-search-input']")
            input_pesquisa.send_keys(produto)

            input_pesquisa.send_keys(Keys.ENTER)
            time.sleep(2)

            try:
                titulos = self.driver.find_elements_by_xpath("//h2[@class='ui-search-item__title']") 

                if not titulos:
                    titulos = self.driver.find_elements_by_xpath("//h2[@class='ui-search-item__title ui-search-item__group__element']") 
                    
            except:
                titulos = self.driver.find_elements_by_xpath("//h2[@class='ui-search-item__title']")

            precos = self.driver.find_elements_by_xpath("//div[@class='ui-search-price ui-search-price--size-medium ui-search-item__group__element']//div[@class='ui-search-price__second-line']//span[@class='price-tag ui-search-price__part']//span[@class='price-tag-fraction']")

            for titulo, preco in zip(titulos, precos):
                print(titulo.text + ' - R$ ' + preco.text)
                

app = App()
app.iniciar()
