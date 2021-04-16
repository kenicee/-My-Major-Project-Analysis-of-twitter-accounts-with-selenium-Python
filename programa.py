from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common import exceptions 
import json 
import pyautogui
import time
import io
import os 

# driver options
otps= Options()
otps.add_argument("user-agent=Mozilla/5.0 (X11; linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)")
chrome_options = webdriver.ChromeOptions()
experimentalFlags = ['calculate-native-win-occlusion@2']
chromeLocalStatePrefs = { 'browser.enabled_labs_experiments' : experimentalFlags}
chrome_options.add_experimental_option('localState',chromeLocalStatePrefs)

#Driver path and go to the page
driver_path = 'C:\\Users\\frigh\\OneDrive\\Escritorio\\python\\chromedriver.exe'
otps.add_argument('--no-sandbox')
driver = webdriver.Chrome(driver_path)
driver.get('https://twitter.com/home')

#localize inputs //ignore
input_user =WebDriverWait(driver, 15).until(
(EC.presence_of_element_located((By.XPATH, "//input[@name='session[username_or_email]' and @dir='auto']")))
)
input_pass = driver.find_element(By.XPATH, '//input[@name="session[password]"]')

#send the keys and login
nombre= ""
#user
input_user.send_keys(nombre)
password = ""
#password
input_pass.send_keys(password)
boton = driver.find_element(By.XPATH, '//main//div[@data-testid="LoginForm_Login_Button"]//div[@dir="auto"]')
boton.click()


#if doesnt exist the account or exits but there was a problem 
def existeerror():
    try:
        bloque = WebDriverWait(driver, 1).until(
        (EC.presence_of_element_located((By.XPATH, '//div[@data-testid="emptyState"]')))
        )
        print ("no existe")
    except:
        print ("existe pero hay error")
        pop3 = nombre
        bloqueadas.append(pop3)
        print (len(bloqueadas))
#another confirmation method or if it exists
def noexiste1():
    try:
        bloque = WebDriverWait(driver, 4).until(
        (EC.presence_of_element_located((By.XPATH, '//div[@data-testid="emptyState"]')))
        )
        pop7 = nombre
        noexiste.append(pop7)
        print ("no existe")
        print (len(noexiste))
    except:
        print ("existe")
#go to the "people" Secction
def peton():
    people = WebDriverWait(driver, 8).until(
    (EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a')))
    ).click()
#click on the account
def buscar():
    try:
        peton()
    except:
        brow = WebDriverWait(driver, 8).until(
        (EC.presence_of_element_located((By.XPATH, '//div[@role="option"]')))
        ).click()    
        people = WebDriverWait(driver, 8).until(
        (EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a')))
        ).click()
#if the account is private skip
def bloqued():  
    try:
        bloque = WebDriverWait(driver, 4).until(
        (EC.presence_of_element_located((By.XPATH, '//div[@data-testid="emptyState"]')))
        )
        cuenpriv= nombre
        priv.append(cuenpriv)
        print ("esta priv")
        print (len(priv))
    except:
        print ("no esta priv")
#first analysis
def analisis1():
    try:
        seguidores = WebDriverWait(driver, 5).until(
        (EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[4]/div[2]/a/span[1]/span')))
        )
        seguidos = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[4]/div[1]/a/span[1]/span')
        entrada = ','
        salida = '.'
        cambio = str.maketrans(entrada, salida)
        pp2 = seguidores.text
        juana5 = pp2.translate(cambio)
        seguidores1 = float(juana5)
        cambio2 = str.maketrans(entrada, salida)
        pp3 = seguidos.text
        juana8 = pp3.translate(cambio)
        seguidos1 = float(juana8)
        if seguidos1 > 0 and seguidores1 >= 30:
            pop = nombre
            pepo = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/a/time').text
            main[pop]= pepo
            print ("Encontre:")
            print (len(main))

        else:
            pop2 = nombre
            print ('Encontre pero no sirve:')
            nosirven.append(pop2)
            print (len(nosirven))
    except:
        print ("No encontre :C")
#second analysis
def analisis2():
    try:
        seguidos = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[1]/a/span[1]/span')
        seguidores = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span')
        entrada = ','
        salida = '.'
        cambio = str.maketrans(entrada, salida)
        pp2 = seguidores.text
        juana5 = pp2.translate(cambio)
        seguidores1 = float(juana5)
        cambio2 = str.maketrans(entrada, salida)
        pp3 = seguidos.text
        juana8 = pp3.translate(cambio)
        seguidos1 = float(juana8)
        if seguidos1 > 0 and seguidores1 >= 30:
            pop = nombre
            pepo = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/div[1]/div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/a/time').text
            main[pop]= pepo
            print ("Pero yo si encontre:")
            print (len(main))


        else:
            pop2 = nombre
            print ('Pero yo si encontre pero no sirve vamos:')
            nosirven.append(pop2)
            print (len(nosirven))
    except:
        print ("------------------------")

#variable list and dictionary
archivo = open('cuentas.txt')
main = {}
sirven = []
saberfechas= []

nosirven = []
bloqueadas = []

priv = []

nosirven = []
noexiste = []
nombre = archivo.readline()
#read the accounts in the file 
for nombre in archivo:
    try:
        driver.get("https://twitter.com/explore")
        busqueda = WebDriverWait(driver, 8).until(
        (EC.presence_of_element_located((By.XPATH, "//input[@data-testid='SearchBox_Search_Input']")))
        )
        #busca la cuenta y envia el nombre de la cuenta
        busqueda.click()
        busqueda.send_keys(nombre)
        buscar()
        entrar =WebDriverWait(driver, 8).until(
        (EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div/div/div/section/div/div/div[1]/div/div/div/div[1]/div/a')))
        )
        entrar.click()
        time.sleep(4)
        bloqued()
        analisis1()
        analisis2()
    except:
        noexiste1()
        existeerror()
        print ("salteado")
        continue
    
with open("facu.txt", "w", encoding='utf-8') as output_file:
    output_file.write(str(main))

#write information in files.txt
archivo.close()
archivo2 = open('nosirven.txt')
with open("nosirven.txt", "w", encoding='utf-8') as output_file:
    output_file.write(str(nosirven))
archivo2.close()
archivo3 = open('bloqueadas.txt')
with open("bloqueadas.txt", "w", encoding='utf-8') as output_file:
    output_file.write(str(bloqueadas))
archivo3.close()
print (bloqueadas)
