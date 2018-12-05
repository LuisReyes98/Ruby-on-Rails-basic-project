import time
from selenium import webdriver
# Se le da al usuario la posibilidad de eligir si desea llevar la prueba a travez de Alerts o Prints
print("Prueba de pagina iniciada")
print("Seleccione si prefiere mensajes por consola o cuadros de dialogo")
print("1 - Consola")
print("2 - Dialogo")

value_type = input("Respuesta: ")

while not(int(value_type) == 1 or int(value_type) == 2):
	print("Ha seleccionado una opcion invalida, por favor eliga una delas opciones indicadas.")
	print("Seleccione si prefiere mensajes por consola o cuadros de dialogo")
	print("1 - Consola")
	print("2 - Dialogo")
	value_type = input("Respuesta: ")
	pass

print('')

# Inicia la prueba
driver = webdriver.Chrome('./chromedriver_linux64/chromedriver')  
driver.maximize_window()
driver.get('http://localhost:3000');
time.sleep(5) # Se espera unos segundos para poder apreciar la pagina

nav_bar = driver.find_element_by_class_name('bm-burger-button')
nav_bar.click()
time.sleep(5) # Se espera unos segundos para poder apreciar la pagina

login = driver.find_element_by_id('login')
login.click()
time.sleep(5) # Se espera unos segundos para poder apreciar la pagina

email_box = driver.find_element_by_id('user_email')
email_box.send_keys('demo@oildemo.com')
email_box.submit()

time.sleep(5) # Se espera unos segundos para poder apreciar la pagina

if driver.find_element_by_class_name('alert'):
	if value_type == 1:
		print("Ocurrio un Error de Logeo")
		pass
	pass

print('Termine')


