"""* EJERCICIO:
Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
atributos y una función que los imprima (teniendo en cuenta las posibilidades
de tu lenguaje).
Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
utilizando su función.
DIFICULTAD EXTRA (opcional):
Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
en el ejercicio número 7 de la ruta de estudio)
- Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
retornar el número de elementos e imprimir todo su contenido."""


class Sicaria:
    def __init__(self, nombre: str, edad: int, hijos: int, estudia: str):
        self.nombre = nombre
        self.edad = edad
        self.hijos = hijos
        self.estudia = estudia

    def mostrar_info(self):
        print(
            f"Tiene {self.hijos} hijos, está estudiando {self.estudia}, tiene {self.edad} años y se llama {self.nombre}"
        )

    def cumplir_anos(self):
        self.edad += 1


sica1 = Sicaria("Yamilet", 30, 7, "Psicología")
sica1.mostrar_info()
sica1.cumplir_anos()
sica1.mostrar_info()

# LIFO


class Stack:
    def __init__(self):
        self.stack = []

    def agregar(self, elemento):
        self.stack.append(elemento)

    def eliminar(self):
        if len(self.stack) > 0:
            self.stack.pop()

    def mostrar(self):
        print(self.stack)
        print(len(self.stack))


pila1 = Stack()
pila1.agregar("a")
pila1.agregar("b")
pila1.agregar("c")
pila1.mostrar()
pila1.eliminar()
pila1.mostrar()
pila1.eliminar()
pila1.mostrar()
pila1.eliminar()
pila1.mostrar()
pila1.eliminar()
pila1.mostrar()


# FIFO


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def insertar(self, elemento):
        self.queue.append(elemento)

    def suprimir(self):
        if len(self.queue) > 0:
            self.queue.pop(0)

    def mostrar_queue(self):
        print(self.queue)
        print(len(self.queue))


pila2 = Queue()
pila2.insertar(5)
pila2.insertar(4)
pila2.insertar(3)
pila2.mostrar_queue()
pila2.suprimir()
pila2.mostrar_queue()
pila2.suprimir()
pila2.mostrar_queue()
pila2.suprimir()
pila2.mostrar_queue()
pila2.suprimir()
pila2.mostrar_queue()
