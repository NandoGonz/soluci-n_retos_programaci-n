"""Crea una clase llamada Persona que tenga:

Atributos: nombre, edad.

Método que muestre un mensaje con el nombre y la edad. """


class Persona:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        """Método para presentar la información en la instancia de la clase """
        if self.edad == 1:
            print(f"Hola me llamo {self.nombre} y tengo {self.edad} año")
        else:
            print(f"Hola me llamo {self.nombre} y tengo {self.edad} años")


p1 = Persona("Emiro", 2)
p1.presentarse()

"""🔹 Ejercicio 2: Clase Círculo

Crea una clase llamada Circulo que tenga:

Atributo: radio.

Métodos:

calcular_area() → devuelve el área del círculo.

calcular_perimetro() → devuelve el perímetro del círculo.

📌 Fórmulas:

Área = π * radio²

Perímetro = 2 * π * radio. """

import math


class Circulo:
    def __init__(self, radio: int):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio**2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


area = Circulo(8)
print(f"El área del círculo es: {area.calcular_area():.2f}")
print(f"El perímetro del círculo es: {area.calcular_perimetro():.2f}")


##############################################################################

"""🔹 Ejercicio 3: Clase Cuenta Bancaria

Crea una clase llamada CuentaBancaria que tenga:

Atributos: titular, saldo.

Métodos:

depositar(cantidad) → aumenta el saldo.

retirar(cantidad) → disminuye el saldo (solo si hay dinero suficiente).

mostrar_saldo() → muestra el saldo actual.

📌 Ejemplo esperado:

c1 = CuentaBancaria("Luis", 1000)
c1.depositar(500)
c1.retirar(200)
c1.mostrar_saldo()   # Saldo actual: 1300. """


class CuentaBancaria:

    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad: float):
        self.saldo += cantidad
        print(
            f" ✅ Se ha realizado el deposito por {cantidad:.2f} correctamente, su saldo es de {self.saldo}"
        )

    def retirar(self, cantidad: float):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(
                f" ✅ Se ha retirado la suma de ${cantidad} de forma correcta, su saldo es de {self.saldo}"
            )
        else:
            print(
                f"❌ No se pudo realizar el retiro por ${cantidad} su saldo es de ${self.saldo} "
            )

    def mostrar_saldo(self):
        print(f"El saldo en su cuenta es: ${self.saldo}")


c1 = CuentaBancaria("Jose", 1000)
c1.depositar(500)
c1.retirar(200)
c1.mostrar_saldo()

##################################################################

"""🔹 Ejercicio 4: Clase Estudiante

Crea una clase Estudiante que tenga:

Atributos: nombre, calificaciones (lista).

Método:

promedio() → que devuelva el promedio de sus calificaciones.

📌 Ejemplo esperado:

e1 = Estudiante("Ana", [4.0, 3.5, 5.0])
print(e1.promedio())   # 4.16 """


class Estudiante:
    def __init__(self, nombre: str, calificaciones: list):
        self.nombre = nombre
        self.calificaciones = calificaciones

    def promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)


e1 = Estudiante("Nando", [5.0, 3.5, 4.5])
print(f"El promedio del alumno {e1.nombre} {e1.promedio():.2f}")

#####################################################

"""Ejercicio 5: Clase Vehículo

Crea una clase Vehiculo que tenga:

Atributos: marca, modelo, año.

Método:

mostrar_info() → imprime toda la información del vehículo.

Luego crea otra clase llamada Coche que herede de Vehiculo y tenga un atributo adicional puertas.

📌 Ejemplo esperado:

c1 = Coche("Toyota", "Corolla", 2020, 4)
c1.mostrar_info()
# Marca: Toyota, Modelo: Corolla, Año: 2020, Puertas: 4 """


class Vehiculo:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_info(self):
        return f"La marca del carro es {self.marca} es modelo {self.modelo} y es del año {self.ano}"


class Coche(Vehiculo):
    def __init__(self, marca: str, modelo: str, ano: int, puertas: int):
        super().__init__(marca, modelo, ano)
        self.puerta = puertas

    def mostrar_info(self):
        return super().mostrar_info() + f" y tiene {self.puerta} puertas"


coche1 = Coche("Toyota", "Supra", 1996, 4)
print(f"{coche1.mostrar_info()}")
# print(f"Marca del coche {coche1.marca}, Modelo {coche1.modelo}, año del coche{coche1.ano} y el cohe tiene {coche1.puerta} puertas")
