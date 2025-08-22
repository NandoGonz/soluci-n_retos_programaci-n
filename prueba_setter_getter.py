"""Haremos uso de los metodos setter y getter, de forma maual y usando decoradores"""


class Persona:
    """Clase persona"""

    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad

    def get_edad(self):
        """Método para usar el getter de forma manual"""
        return self._edad

    def set_edad(self, n_edad: int):
        """Método para usa el setter de forma manual"""
        if n_edad > 0:
            self._edad = n_edad
        else:
            print("La edad no puede ser negativa")

    def saludar(self):
        """Métdodo para mostrar la información de la clase Persona"""
        return f"Hola mi nombres es {self._nombre} y tengo {self._edad} años"


p1 = Persona("Nando", 28)
print(p1.saludar())
print(p1.get_edad())  # hago un llamado a mi metodo setter
p1.set_edad(29)  # hago uso de forma interna de mi metodo getter
print(p1.get_edad())
print(p1.saludar())
p1.set_edad(-6)


# usando decoradores


class Person:
    """Clase person"""

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def age(self):
        """Método con decoradro para el getter"""
        return self._age

    @age.setter
    def age(self, new_age: int):
        """Método con decorador para el setter"""
        if new_age > 0:
            self._age = new_age
        else:
            print("La edad no puede ser negativa")

    def greeting(self):
        """Método para presentar los atributos del onjeto en instancia"""
        return f"Hola mi nombres es {self._name} y tengo {self._age} años # 2"


p2 = Person("Fernando", 29)
print(p2.age)  # @property o getter
print(p2.greeting())
p2.age = 32  # @edad.setter
print(p2.age)
print(p2.greeting())
p2.age = -4
