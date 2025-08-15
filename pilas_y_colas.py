"""
*EJERCICIO:
*Implementa los mecanismos de introducción y recuperación de elementos propios de las
*pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
*o lista (dependiendo de las posibilidades de tu lenguaje).

*DIFICULTAD EXTRA (opcional):
*- Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
*  de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
*  que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
*  Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
*  el nombre de una nueva web.
*- Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
*  impresora compartida que recibe documentos y los imprime cuando así se le indica.
*  La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
*  interpretan como nombres de documentos."""

# Ultimo en ser agregado, primero en ser eliminado (pilas -> stack)

pilas = []
"""Las pilas (stacks) siguen el principio LIFO (Last In, First Out)"""
pilas.append("Nando")
pilas.append("Adrian")
pilas.append("Kristina")
pilas.append("Emiro")

"""De forma manual"""

"""stack = pilas[len(pilas) - 1]
del pilas[len(pilas) - 1]
print(stack)"""

print(pilas)

print(pilas.pop())
print(pilas)
print(pilas.pop())
print(pilas)
print(pilas.pop())
print(pilas)
print(pilas.pop())
print(pilas)


# Primero en ser agregado, primero en ser eliminado (colas ->queues )
pilas = []
"""las colas (queues) siguen el principio FIFO (First In, First Out)"""
pilas.append("Nando")
pilas.append("Adrian")
pilas.append("Kristina")
pilas.append("Emiro")

# De forma manual
"""queue = pilas[0]
del pilas[0]
print(queue)

queue = pilas[0]
del pilas[0]

print(queue)"""

print(pilas)

print(pilas.pop(0))
print(pilas)
print(pilas.pop(0))
print(pilas)
print(pilas.pop(0))
print(pilas)
print(pilas.pop(0))
print(pilas)


def navegador():
    webs = []

    while True:
        hacer = input("Esriba el nombre de una url o adelante/atras/salir: ")

        if hacer == "salir":
            break
        elif hacer == "adelante":
            pass
        elif hacer == "atras":
            webs.pop()
        else:
            webs.append(hacer)
        if len(webs) > 0:

            print(f"Has ingresado a la página web: {webs[len(webs) - 1]}")
        else:
            print("Estás en la pagina de inicio")


# navegador()


def imprimir():
    queue = []
    while True:
        accion = input("Agrege un documento o imprimir/salir: ")
        if accion == "salir":
            break
        elif accion == "imprimir":
            if len(queue) > 0:
                print(f"Se esta imprimiendo el documento: {queue.pop(0)}")
        else:
            queue.append(accion)
        print(f"Lsta de documentos a imprimir: {queue}")


imprimir()
