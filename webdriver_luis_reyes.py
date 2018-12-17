import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Luis Reyes C.I:27097304
print("Prueba de pagina iniciada")
print("Los mensajes de error del sistema se mostraran por consola")

value_type = input("Ingrese cualquier tecla para empezar: ")

print('')

# Inicia la prueba
driver = webdriver.Chrome('./chromedriver_linux64/chromedriver')  
driver.maximize_window()
driver.get('http://localhost:3000');
time.sleep(5) # Se espera unos segundos para poder cargar

def main():
	global driver
	pass
	openNav()
	openLogin()

	email_box = driver.find_element_by_id('user_email')
	email_box.send_keys('demo@oildemo.com')
	email_box.submit()

	time.sleep(5) # Se espera unos segundos para poder cargar
	openNav()
	openLogin()
	checkError("Error de inicio de sesion")

	email_box = driver.find_element_by_id('user_email')
	email_box.send_keys('admin@admin.com')

	password_box = driver.find_element_by_id('user_password')
	password_box.send_keys('admin123')
	password_box.submit()

	time.sleep(5) # Se espera unos segundos para poder cargar

	openNav()
	openLogin()
	try:		
		if driver.find_element_by_id('log_out') != None:
			print("Inicio de sesion exitoso")
			pass		
	except Exception as e:
		pass

	close_modal = driver.find_element_by_id('close_modal')
	close_modal.click()
	time.sleep(5) # Se espera unos segundos para poder cargar

def themesTest():
	openNav()
	openThemes()

	new_theme = driver.find_element_by_id('new_theme')
	new_theme.click()
	time.sleep(5) # Se espera unos segundos para poder cargar

	theme_name = driver.find_element_by_id('frontend_theme_name')
	theme_name.submit()
	time.sleep(5) # Se espera unos segundos para poder cargar	
	checkError("Error de Formulario")

	theme_name = driver.find_element_by_id('frontend_theme_name')
	theme_name.send_keys('Peliculas Geniales')
	time.sleep(1) # Se espera unos segundos para poder cargar	

	theme_description = driver.find_element_by_id('frontend_theme_description')
	theme_description.click()
	theme_description.send_keys(Keys.CONTROL, "a")
	theme_description.send_keys('THIs is alot of text in order for this to work or it would say it is too short AAAAAAAAAAAAAAA')
	time.sleep(2) # Se espera unos segundos para poder cargar	
	theme_description.submit()
	time.sleep(2) # Se espera unos segundos para poder cargar	

def editTheme():
	global driver
	driver.find_element_by_id('edit_theme').click()
	time.sleep(5) # Se espera unos segundos para poder cargar	

	theme_name = driver.find_element_by_id('frontend_theme_name')
	theme_name.clear()
	theme_name.send_keys('Peliculas Geniales con Nombre cambiado totalmente original')
	time.sleep(1) # Se espera unos segundos para poder cargar		
	theme_name.submit()
	time.sleep(1) # Se espera unos segundos para poder cargar	

	pass
	

def checkError(mensaje):
	global driver 
	try:		
		if driver.find_element_by_class_name('alert') != None:
			print(mensaje)
			pass
	except Exception as e:
		pass

def openNav():
	global driver 
	nav_bar = driver.find_element_by_class_name('bm-burger-button')
	nav_bar.click()
	time.sleep(5) # Se espera unos segundos para poder cargar

def openLogin():
	global driver 
	login = driver.find_element_by_id('login')
	login.click()
	time.sleep(5) # Se espera unos segundos para poder cargar

def openThemes():
	global driver 
	themes = driver.find_element_by_id('themes')
	themes.click()
	time.sleep(5) # Se espera unos segundos para poder cargar	

def openCritics():
	global driver 
	critics = driver.find_element_by_id('critics')
	critics.click()
	time.sleep(5) # Se espera unos segundos para poder cargar	

def logOut():
	global driver
	time.sleep(5) # Se espera unos segundos para poder cargar		
	openNav()
	openLogin()
	driver.find_element_by_id('log_out').click()
	time.sleep(5) # Se espera unos segundos para poder cargar	
	openNav()
	openLogin()
	time.sleep(2)
	driver.quit()

	pass

if __name__ == '__main__':
	main()
	themesTest()
	editTheme()
	logOut() #Llamar siempre de ultimo
		