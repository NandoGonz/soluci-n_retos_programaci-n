class Vehiculo:
    def __init__(self, nombre, modelo, ano):
        self.nombre = nombre 
        self.modelo = modelo
        self.ano = ano
    
    def vehiculo_encender(self):
        print("El vehivulo esta encendido")
        
    def vehiculo_apagar(self):
        print("El vehiculo ha sido apagado")

class Carro(Vehiculo):
    def __init__(self, nombre, modelo, ano, capacidad):
        super().__init__(nombre, modelo, ano)
        self.capacidad = capacidad
        print(f"El carro {self.nombre}, modelo {self.modelo}, ano {self.ano}, tiene la capacidad de {self.capacidad} personas")


class Moto(Vehiculo):
    def __init__(self, nombre, modelo, ano):
        super().__init__(nombre, modelo, ano)
        print(f"La moto {self.nombre}, modelo {self.modelo}, ano {self.ano}")
# instacio mi clase

moto_1 = Moto("Bajaj", "Platino", 2008)
moto_1.vehiculo_encender()
moto_1.vehiculo_apagar()
carro_2 = Carro("Toyota", "Fortuner", 2020, 5)
carro_2.vehiculo_encender()
carro_2.vehiculo_apagar()