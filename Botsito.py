# Librerias
import time
import openpyxl
import pandas
import pandas as pd

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
# return self.find_element(by=By.CLASS_NAME, value=name)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID, "didomi-notice-agree-button")))
driver.find_element(By.ID, 'didomi-notice-agree-button').click()  # click en la ventana emergente

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID, "userAvatarImage")))
driver.find_element(By.ID, 'userAvatarImage').click()  # click en la imagen de login

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID, "email")))  # espera que el cuadro "email" aparezca
driver.find_element(By.ID, 'email').send_keys(user)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.ID, "password")))
driver.find_element(By.ID, 'password').send_keys(pwd)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#page > main > div.section_login > div.wrapper > section > article > div > form > div.form_button > button")))
driver.find_element(By.CSS_SELECTOR,
                    '#page > main > div.section_login > div.wrapper > section > article > div > form > div.form_button > button').click()

xpath_box_find = '/html/body/div[5]/nav/div[2]/div[1]/div[3]/div[1]/div[1]/form/label/input'
WebDriverWait(driver, 6)\
    .until(EC.element_to_be_clickable((By.XPATH, xpath_box_find )))
driver.find_element(By.XPATH, xpath_box_find).send_keys('Bogota')       #Envia el valor de "Bogota" en la caja de busqueda

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/nav/div[2]/div[1]/div[3]/div[1]/div[1]/ul/li[1]')))
driver.find_element(By.XPATH, '/html/body/div[5]/nav/div[2]/div[1]/div[3]/div[1]/div[1]/ul/li[1]').click()  #click en el boton de busqueda

cuadro_valores = '/html/body/div[5]/main/div[4]/div/section[3]/section/div/article/div[1]/div[2]/div[2]/div[1]/p[1]'
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, cuadro_valores)))
driver.find_element(By.XPATH, '/html/body/div[5]/main/div[4]/div/section[3]/section/div/article/section/ul/li[2]').click()  #click en la pestaña "por horas"


WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/main/div[4]/div/section[3]/section/div[1]/ul'))) #en espera de que los datos seran cargados
info_weather = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[4]/div/section[3]/section/div[1]/ul')  #guarda los datos en una variable
info_weather = info_weather.text

#print (info_weather)
tiempo_hoy = info_weather.split('Mañana')[0].split('\n')[1:-1]

#print (tiempo_hoy)

horas = list()
temperature = list()
vel_viento = list()
#medida = list()

for i in range(0, len(tiempo_hoy), 4):
    horas.append(tiempo_hoy[i])
    #temperature.append(tiempo_hoy[i+1])
    ##vel_viento.append(tiempo_hoy[i+2])
    #medida.append(tiempo_hoy[i]).

#linea inicial
#final linea

df = pd.DataFrame({'Horas': horas, 'Temperatura': temperature})#, 'Vel. del viento': vel_viento})#, 'medidas': medida})
print (df)
df.to_csv('tiempo_hoy.csv', index=False)
        
#df.to_csv('tiempo_hoy.csv', index=False)

driver.quit()

