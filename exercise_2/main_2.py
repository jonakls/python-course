#
# Ejercicio 2
# 

# Contexto: Distintos tipos de datos con operadores logicos en funciones

# <ID, Letra>
diccionario = {
    0: "¿",
    1: "Hola",
    2: "Mundo",
    3: "Como",
    4: "Estan",
    5: "?"
}

def mostrar_diccionario(diccionario):
    print("""
    DICCIONARIO
    """)
    for i in range(6):
        print(diccionario[i])


mostrar_diccionario(diccionario)