import time
from selenium import webdriver
# Se le da al usuario la posibilidad de eligir si desea llevar la prueba a travez de Alerts o Prints
print("Prueba de pagina iniciada")
print("Los mensajes de error del sistema se mostraran por consola")

value_type = input("Ingrese cualquier tecla para empezar: ")

print('')

# Inicia la prueba
driver = webdriver.Chrome('./chromedriver_linux64/chromedriver')  
driver.maximize_window()
driver.get('http://localhost:3000');
time.sleep(5) # Se espera unos segundos para poder apreciar la pagina

def main():
	pass
	openNav()
	openLogin()

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

def openNav():
	global driver 

	nav_bar = driver.find_element_by_class_name('bm-burger-button')
	nav_bar.click()
	time.sleep(5) # Se espera unos segundos para poder apreciar la pagina

def openLogin():
	global driver 
	login = driver.find_element_by_id('login')
	login.click()
	time.sleep(5) # Se espera unos segundos para poder apreciar la pagina
	

if __name__ == '__main__':
	main()