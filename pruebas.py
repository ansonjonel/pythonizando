# -*- coding: utf-8 -*-
mensajeGui="hello fthfds world"
print(mensajeGui)
print	"mensavcxelllllllllllllll"
print "casa"
mi_cadena_multilinea = """

------------


Esta es una cadena
de varias lineas
"""
print mi_cadena_multilinea

precio = 7435.28

total = 34543.959

print (total / precio)

mi_tupla = ('cadena de texto', 15, 2.8, 'otro dato', 25)
mi_lista = ['cadena de texto', 15, 2.8, 'otro dato', 25]
mi_diccionario = {'clave_1': 4, 'clave_2': 77, 'clave_7': 'gevfdasa'}
mi_lista[2] = 33.3

print mi_tupla[-2]
print mi_lista[2]
print mi_diccionario ['clave_2']
print "En el Ñágara encontré un Ñandú"

anio = 2001
while anio <= 2012:
	print "Informes del Año", str(anio)
	anio += 1

mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio']
for nombre in mi_lista:
	print nombre

mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo')
for color in mi_tupla:
	print color

for anio in range(2001, 2013):
	print "Informes del Año", str(anio)

def mi_funcion():
	return "Hola Mundo---"

frase = mi_funcion()
print frase

def saludar(nombre, mensaje='Hola'):
	print mensaje, nombre

saludar(mensaje="Buen día", nombre="Juancho")

#######################################################################33

def recorrer_parametros_arbitrarios(parametro_fijo, *ema):
	print parametro_fijo
	# Los parámetros arbitrarios se corren como tuplas
	for argumento in ema:
		print argumento
recorrer_parametros_arbitrarios('Fixed', 'arbitrario 1', 'arbitrario 2', 'arbitrario 3')

###########################################################################################


def recorrer_parametros_arbitrarios_2(parametro_fijo, *arbitrarios, **kwords):
	print parametro_fijo
	for argumento in arbitrarios:
		print argumento
# Los argumentos arbitrarios tipo clave, se recorren como los diccionarios
	for clave in kwords:
		print "El valor de", clave, "es", kwords[clave]

recorrer_parametros_arbitrarios_2("Fixed", "arbitrario 1", "arbitrario 2", "arbitrario 3", clave1="valor uno", clave2="valor dos")

###########################################################################################

def calcular(importe, descuento):
	return importe - (importe * descuento / 100)

datos = [1500, 10]
print calcular(*datos)

###########################################################################################

def calcular(importe, descuento):
	return importe - (importe * descuento / 100)

datos = {"descuento": 10, "importe": 1500}
print calcular(**datos)

################################################################################

def funcion():
	return "Hola Mundo"

def saludar3(nombre, mensaje='Hola\b'):
	print mensaje,nombre
	print funcion()

saludar3("pepa")



################################################################################

def guaraira():
	return "TAPIRAPECÓ"
def guaraira1():
	return "TAPIRAPECÓ1"
def guaraira2():
	return "TAPIRAPECÓ2"
def guaraira3():
	return "TAPIRAPECÓ3"

def llamada_de_retorno(func=""):
	"""Llamada de retorno a nivel global"""
	return globals()[func]()

print llamada_de_retorno("guaraira")
print llamada_de_retorno("guaraira1")
print llamada_de_retorno("guaraira2")
print llamada_de_retorno("guaraira3")

print "\naqui"
print guaraira2()
print llamada_de_retorno("guaraira3")
nombre_de_la_funcion = "guaraira3"
print locals()[nombre_de_la_funcion]()
print "aqui\n"

##################################################################################


nombre_de_la_funcion = "guaraira"
print locals()[nombre_de_la_funcion]()

#################################################################################


def averga(nombre):
	return "Hola " + nombre

def llamada_de_retorno(func=""):
	"""Llamada de retorno a nivel global"""
	return globals()[func]("Laura")

print "soy global"
print llamada_de_retorno("averga")
print ("\n")


# Llamada de retorno a nivel local
nombre_de_la_funcion = "averga"
print "soy local:"
print locals()[nombre_de_la_funcion]("Vitico Castillo")
print locals()["averga"]("Facundo")
print locals()["averga"]("pericles")

print "hola anson jonel"


###########################################################################################33

def funcion(nombre):
	return "Hola " + nombre

def llamada_de_retorno(func=""):
	if func in globals():
		if callable(globals()[func]):
			return globals()[func]("Petronila Mata")
	else:
		return "Función no encontrada"

print llamada_de_retorno("funcion")
nombre_de_la_funcion = "funcion"

if nombre_de_la_funcion in locals():
	if callable(locals()[nombre_de_la_funcion]):
		print locals()[nombre_de_la_funcion]("Cacica Isabel")
	else:
		print "Función no encontrada"