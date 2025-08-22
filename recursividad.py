"""/*
* EJERCICIO:
* Entiende el concepto de recursividad creando una función recursiva que imprima
* números del 100 al 0.
*
* DIFICULTAD EXTRA (opcional):
* Utiliza el concepto de recursividad para:
* - Calcular el factorial de un número concreto (la función recibe ese número).
* - Calcular el valor de un elemento concreto (según su posición) en la
*   sucesión de Fibonacci (la función recibe la posición)."""


def reversa(num: int):
    if num >= 0:
        print(num)
        reversa(num - 1)


reversa(100)


def factorial(num: int):
    if num < 0:
        print("Los números negativos no son validos")
        return 0
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(5))


def fibonacci(numero: int) -> int:
    if numero < 0:
        print("La posición debe ser mayor a cero")
        return 0
    elif numero == 1:
        return 0
    elif numero == 2:
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


print(fibonacci(5))
