import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
	global driver
	pass
	openNav()
	openLogin()

	email_box = driver.find_element_by_id('user_email')
	email_box.send_keys('demo@oildemo.com')
	email_box.submit()

	time.sleep(5) # Se espera unos segundos para poder apreciar la pagina
	openNav()
	openLogin()
	try:		
		if driver.find_element_by_class_name('alert') != None:
			print("Ocurrio un Error de Inicio de Sesión")
			pass
	except Exception as e:
		pass

	email_box = driver.find_element_by_id('user_email')
	email_box.send_keys('admin@admin.com')

	password_box = driver.find_element_by_id('user_password')
	password_box.send_keys('admin123')
	password_box.submit()

	time.sleep(5) # Se espera unos segundos para poder apreciar la pagina

	openNav()
	openLogin()
	try:		
		if driver.find_element_by_id('log_out') != None:
			print("Inicio de sesion exitoso")
			pass		
	except Exception as e:
		pass

	driver.find_element_by_class_name('modal-dialog').send_keys('u\'\ue00c\'');
	driver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
	time.sleep(5) # Se espera unos segundos para poder apreciar la pagina

	openNav()
	openThemes()

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

def openThemes():
	global driver 
	themes = driver.find_element_by_id('themes')
	themes.click()
	time.sleep(5) # Se espera unos segundos para poder apreciar la pagina	

def openCritics():
	global driver 
	critics = driver.find_element_by_id('critics')
	critics.click()
	time.sleep(5) # Se espera unos segundos para poder apreciar la pagina	

if __name__ == '__main__':
	main()