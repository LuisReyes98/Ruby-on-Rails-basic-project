import time
from selenium import webdriver
# Se le da al usuario la posibilidad de eligir si desea llevar la prueba a travez de Alerts o Prints
print "Bienvenido al modulo para probar su pagina web"
print "Seleccione si prefiere trabajar con print o con alert de javascript"
print "1 - Print"
print "2 - Alert"

value_type = raw_input("Respuesta: ")

while not(int(value_type) == 1 or int(value_type) == 2):
	print "Ha seleccionado una opcion invalida, por favor eliga una delas opciones indicadas."
	print "Seleccione si prefiere trabajar con print o con alert de javascript"
	print "1 - Print"
	print "2 - Alert"
	value_type = raw_input("Respuesta: ")
	pass

print ''

# Inicia la prueba
driver = webdriver.Chrome('./chromedriver')  
driver.maximize_window()
driver.get('http://localhost:3000');
time.sleep(2) # Se espera unos segundos para poder apreciar la pagina
user_box = driver.find_element_by_id('user_email')
user_box.send_keys('demo@oildemo.com')
user_box.submit()
time.sleep(2)
# Se capta el erro de iniciar sesion y se indica
error_message = driver.find_element_by_id('error_message')

# se indica el password
time.sleep(2)
password_box = driver.find_element_by_id('user_password')
password_box.send_keys('demo123')
time.sleep(1)
password_box.submit()



time.sleep(3)

# nos dirigimos a la Vista de conductores en donde  realizaremos 
#Prueba de un textbox el cual esta deshabilitado
driver.find_element_by_id('drivers').click()
time.sleep(2)

driver.find_element_by_id('new-driver').click()
time.sleep(1)

# Se verifica si el primer text box esta habilitado
element = driver.find_element_by_name('backend_driver[username]')

print bool(element.get_attribute("disabled"))

if int(value_type) == 2:

	alert = driver.execute_script('alert("El elemento 1 esta deshabilitado:' + str(bool(element.get_attribute("disabled"))) + '")')
	time.sleep(1)
	alert = driver.switch_to.alert
	alert.accept()
else:
	print 'El elemento 1 esta deshabilitado: ' + str(bool(element.get_attribute("disabled")))

element2 = driver.find_element_by_name('backend_driver[email]')

if int(value_type) == 2:

	alert = driver.execute_script('alert("El elemento 2 esta deshabilitado:' + str(bool(element2.get_attribute("disabled"))) + '")')
	time.sleep(1)
	alert = driver.switch_to.alert
	alert.accept()
else:
	print 'El elemento 2 esta deshabilitado: ' + str(bool(element2.get_attribute("disabled")))


#Prueba de insertar y actualizar un registro

#para ello debemos ir  a la vista de estaciones

driver.find_element_by_id('stations_collapse').click()
time.sleep(1)
driver.find_element_by_id('stations_list').click()


time.sleep(2)
driver.find_element_by_id('new-register').click()
time.sleep(2)
driver.execute_script("document.getElementsByTagName('form')[0].submit();")


errors = driver.find_elements_by_id('error_messages')


time.sleep(2)

name_box = driver.find_element_by_id('name')
name_box.send_keys('Estacion de prueba')
time.sleep(2)
address_box = driver.find_element_by_id('address')
address_box.send_keys('Direccion Estacion de prueba')
time.sleep(2)
driver.execute_script("document.getElementsByTagName('form')[0].submit();")

time.sleep(2)
driver.find_element_by_id('edit').click()
name_box = driver.find_element_by_id('name')
name_box.clear()
name_box.send_keys("Estacion de prueba actualizando")
time.sleep(2)
driver.execute_script("document.getElementsByTagName('form')[0].submit();")

## Cerrar sesion
driver.find_element_by_id('user_collapse').click()
time.sleep(1)
driver.find_element_by_id('user_sign_out').click()
time.sleep(2)
driver.quit()

