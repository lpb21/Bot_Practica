# Librerias
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import openpyxl
import pandas
import pandas as pd
import csv
import os

excel_credenciales = r'C:\Users\Leo\Documents\Documents\Leo\Bot_Practica\ejemplo.xlsx'

s = Service('C:\Program Files (x86)\chromedriver.exe')

# opciones de navegacion
options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
df = pandas.read_excel(excel_credenciales)
user = df['usuario'][0]
pwd = df['contraseña'][0]

driver_path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(service=s)

wait = WebDriverWait(driver, 8)
# inicializa el navegador
driver.get("https://eltiempo.es/")

# driver.find_element_by_class_name('didomi-notice-agree-button').click()

# hace referencia al time out si no se ejecuta en "5", el programa se detiene .replace(' ','.')
# WebDriverWait(driver, 12)\
# .until(EC.element_to_be_clickable(By.CSS_SELECTOR,
# 'button.didomi-components-button didomi-button didomi-dismiss-button didomi-components-button--color didomi-button-highlight highlight-button'.replace(' ', '.')))\
# .click()
# return self.find_element(by=By.CLASS_NAME, value=name)

wait.until(EC.presence_of_element_located((By.ID, "didomi-notice-agree-button")))
driver.find_element(By.ID, 'didomi-notice-agree-button').click()  # click en la ventana emergente
wait.until(EC.presence_of_element_located((By.ID, "userAvatarImage")))
driver.find_element(By.ID, 'userAvatarImage').click()  # click en la imagen de login

wait.until(EC.presence_of_element_located((By.ID, "email")))  # espera que el cuadro "email" aparezca
driver.find_element(By.ID, 'email').send_keys(user)
driver.find_element(By.ID, 'password').send_keys(pwd)

driver.find_element(By.CSS_SELECTOR,
                    '#page > main > div.section_login > div.wrapper > section > article > div > form > div.form_button > button').click()

xpath_box_find = '/html/body/div[5]/nav/div[2]/div[1]/div[3]/div[1]/div[1]/form/label/input'
WebDriverWait(driver, 6)\
    .until(EC.element_to_be_clickable((By.XPATH, xpath_box_find)))
driver.find_element(By.XPATH, xpath_box_find).send_keys('Bogota')       #Envia el valor de "Bogota" en la caja de busqueda

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/nav/div[2]/div[1]/div[3]/div[1]/div[1]/ul/li[1]')))
driver.find_element(By.XPATH, '/html/body/div[5]/nav/div[2]/div[1]/div[3]/div[1]/div[1]/ul/li[1]').click()  #click en el boton de busqueda

wait.until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/main/div[4]/div/section[3]/section/div/article/section/ul/li[5]/a/span')))
driver.find_element(By.XPATH, '/html/body/div[5]/main/div[4]/div/section[3]/section/div/article/section/ul/li[2]').click()  #click en la pestaña "por horas"

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/main/div[4]/div/section[3]/section/div[1]/ul'))) #en espera de que los datos sean cargados
info_weather = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[4]/div/section[3]/section/div[1]/ul')  #guarda los datos en una variable
info_weather = info_weather.text

#toma como separador el string de "mañana" y despues toma el salto de linea "\n"
tiempo_hoy = info_weather.split('Mañana')[0].split('\n')[1:-1]

horas = list()
temperature = list()
vel_viento = list()
#medida = list()

ArrayTiempo = []
for i in range(0, len(tiempo_hoy), 5):
    Data = [tiempo_hoy[i], tiempo_hoy[i+1], tiempo_hoy[i+2] + tiempo_hoy[i+3]]
    ArrayTiempo.append(Data)

#print (ArrayTiempo)
myFile = open("DataTiempo.txt", 'w', newline='', encoding="utf-8")
with myFile:
    writer = csv.writer(myFile, delimiter=",")
    writer.writerows(ArrayTiempo)
#print (ArrayTiempo)

index = 0;

for i in ArrayTiempo:
    print(index, 'Hora', 'temperatura', 'Vel viento')
    print(i, end=" ")
    index = index + 1;

#for i in range(0, len(ArrayTiempo), 4):
    #horas.append(tiempo_hoy[i])
    #temperature.append(tiempo_hoy[i+1])
    ##vel_viento.append(tiempo_hoy[i+2])
    #medida.append(tiempo_hoy[i]).
myFile.close()

driver.quit()

