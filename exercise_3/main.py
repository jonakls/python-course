#
# Ejercicio 3
# 

# Contexto: Aplicacion de un crowd simple con distintas funciones


def inicio_programa():
    print("""
    CALCULADORA BASICA

    ESCRIBA EL PRIMER NUMERO
    """)
    a = int(input())
    print("""
    ESCRIBA EL SEGUNDO NUMERO
    """)
    b = int(input())
    print("RESULTADO: ", menu(a, b))


def menu(a, b):
    print("""
    CALCULADORA BASICA
    1. Sumar
    2. Restar
    3. Dividir
    4. Multiplicar

    ESCRIBA EL NUMERO DE LA OPERACION QUE DESEA REALIZAR
    """)
    option = int(input())

    result = 0
    if option == 1:
        return a + b
    elif option == 2:
        return a - b
    elif option == 3:
        if b == 0:
            print("ERROR: El segundo numero no puede ser 0")
            return result
        return a / b
    elif option == 4:
        return a * b
    else:
        print("Opcion no valida")
        return result

inicio_programa()
