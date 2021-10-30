"""Template robot with Python."""
from inspect import ArgSpec
from re import S
from openpyxl.workbook.workbook import Workbook
import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox import firefox_profile
from time import sleep 
import openpyxl
from openpyxl import workbook
import csv
import collections





class Robocorp():   


    driver = webdriver.Chrome()

    def web(self):
        
        self.driver.implicitly_wait(10)
        self.driver.get('https://www.tiendainglesa.com.uy/')
        self.driver.maximize_window()
         
        
   

    def socursal(self):
        driver = self.driver
        self.ciudad = driver.find_element_by_xpath('//*[@id="MPW0057TXTSTORE_0003"]')
        self.ciudad.click()
        sleep(10)    




    def barra_busqueda(self):
        driver = self.driver   
        self.buscador = driver.find_element_by_xpath('//*[@id="MPW0010W0015IDSEARCH1Container"]/div/div[1]/input')
        self.buscador.click()
        self.buscador.send_keys('Notebook')
        self.click_icono = driver.find_element_by_xpath('//*[@id="MPW0010W0015IDSEARCH1Container"]/div/div[1]/div[2]')
        self.driver.implicitly_wait(5)
        self.click_icono.click()
        


  
    def extraer_articulos(self):
        driver = self.driver    
        articulos=[]
        articulo={
            'descripcion':"",'precio':""
        }
        
        i=1
        for i in range(1,21):
            self.descrip = driver.find_element_by_xpath(f'/html/body/form/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div/div[{i}]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[3]/a/span').text
            self.precio = driver.find_element_by_xpath(f'/html/body/form/div[2]/div[2]/div/div[3]/div/div/div/div[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div/div[{i}]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div[3]/div[1]/div/div/span').text
            articulo['precio']=self.precio
            articulo['descripcion']=self.descrip
            articulos.append(articulo)
            
        
        return articulos
         
           


    def generar_archivo_excel(self,articulos):

        wb = openpyxl.Workbook()
        hoja = wb.active
        hoja.append(articulos)
        wb.save('productos_1.xlsx')

       



    def gernerar_archivo_csv(self,articulos):
        driver = self.driver
        archivo = open('archivo_reporte.csv','w')
    
        with archivo:
            writer = csv.writer(archivo)
            writer.writerows(articulos)
            sleep(1)
 

    


def run_robocorp():
     Robocorp().web()
     Robocorp().socursal()
     Robocorp().barra_busqueda()
     articule = Robocorp().extraer_articulos()
     Robocorp().gernerar_archivo_csv(articule)
     


if __name__ == "__main__":
    run_robocorp()
