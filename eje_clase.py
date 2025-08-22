class Vehiculo:
    """Clase padre que dara los atritbutos a sus hijos"""

    def __init__(self, nombre, modelo, ano):
        self.nombre = nombre
        self.modelo = modelo
        self.ano = ano

    def vehiculo_encender(self):
        """Metodo para encender el vehiculo"""
        print(f"El vehivulo {self.modelo} esta encendido ")

    def vehiculo_apagar(self):
        """Metodo para apagar el vehiculo"""
        print(f"El vehiculo {self.modelo} ha sido apagado")


class Carro(Vehiculo):
    """Clase hija carro"""

    def __init__(self, nombre, modelo, ano, capacidad):
        super().__init__(nombre, modelo, ano)
        self.capacidad = capacidad
        print(
            f"El carro {self.nombre}, modelo {self.modelo}, ano {self.ano}, tiene la capacidad de {self.capacidad} personas"
        )


class Moto(Vehiculo):
    """Clase hija moto"""

    def __init__(self, nombre, modelo, ano):
        super().__init__(nombre, modelo, ano)
        print(f"La moto {self.nombre}, modelo {self.modelo}, año {self.ano}")


# instacio mi clase

moto_1 = Moto("Bajaj", "Platino", 2008)
moto_1.vehiculo_encender()
moto_1.vehiculo_apagar()
carro_2 = Carro("Toyota", "Fortuner", 2020, 5)
carro_2.vehiculo_encender()
carro_2.vehiculo_apagar()
