#
# Ejercicio 2
# 

# Contexto: Distintos tipos de datos con operadores logicos en funciones

def sumar(a, b) :
	return a + b

def restar(a, b) :
	return a - b

def divir(a, b) :
	if b == 0:
		return "Numero b no es valido"
	
	return a / b

def multiplicar(a, b) :
	return a * b

def list_operations(list):
	print("""

	OPERACIONES CON LISTAS

	""")
	list.clear()
	print("Lista vacia: " + str(list))
	list.append(0)
	list.append(1)
	list.append(2)
	list.append(3)
	print("Lista con elementos añadidos: " + str(list))
	print("Lista de tamaño: " + str(len(list)))
	print("Sobrescribe dato (" + str(list.pop(1)) + ") por el dato: 8")
	list.insert(1, 8)
	print("Lista con elementos sobrescritos: " + str(list))
	list.sort()
	# Ordena lista
	print("Lista ordenada: " + str(list))

def inicio():

	print("""

	OPERACIONES BASICAS

	""")

	numero_a = 5
	numero_b = 7

	# Lista con varios numeros
	lista_numeros = [1, 2, 3, 4]
	lista_numero_2 = [5, 6, 7, 8]
	# Conversion a tupla
	tupla_numeros = tuple(lista_numeros)
	tupla_numeros_2 = tuple(lista_numero_2)

	print("Suma: " + str(sumar(numero_a, numero_b)))
	print("Resta:" + str(restar(numero_a, numero_b)))
	print("Division: " + str(divir(numero_a, numero_b)))
	print("Multiplicacion: " + str(multiplicar(numero_a, numero_b)))

	print("Lista:" + str(lista_numeros))
	print("Tupla:" + str(tupla_numeros))

	print("Lista[0]: " + str(lista_numeros[0]))
	print("Tupla[0]: " + str(tupla_numeros[0]))

	print("Lista[0:2]: " + str(lista_numeros[0:2]))
	print("Tupla[0:2]: " + str(tupla_numeros[0:2]))

	print("Junte de listas:" + str(lista_numeros + lista_numero_2))

	print("Junte de tuplas:" + str(tupla_numeros + tupla_numeros_2))

	list_operations(lista_numeros)

inicio()