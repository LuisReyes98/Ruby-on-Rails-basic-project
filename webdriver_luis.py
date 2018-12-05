import time
from selenium import webdriver
# Se le da al usuario la posibilidad de eligir si desea llevar la prueba a travez de Alerts o Prints
print("Bienvenido al modulo para probar su pagina web")
print("Seleccione si prefiere trabajar con print o con alert de javascript")
print("1 - Print")
print("2 - Alert")

value_type = input("Respuesta: ")

while not(int(value_type) == 1 or int(value_type) == 2):
	print("Ha seleccionado una opcion invalida, por favor eliga una delas opciones indicadas.")
	print("Seleccione si prefiere trabajar con print o con alert de javascript")
	print("1 - Print")
	print("2 - Alert")
	value_type = input("Respuesta: ")
	pass

print('')

# Inicia la prueba
driver = webdriver.Chrome('./chromedriver_linux64/chromedriver')  
driver.maximize_window()
driver.get('http://localhost:3000');
time.sleep(5) # Se espera unos segundos para poder apreciar la pagina

nav_bar = driver.find_element_by_id('slide_nav_bar')
nav_bar.click()
time.sleep(5) # Se espera unos segundos para poder apreciar la pagina



