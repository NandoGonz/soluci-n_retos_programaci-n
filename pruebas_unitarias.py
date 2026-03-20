"""* EJERCICIO:
* Crea una función que se encargue de sumar dos números y retornar
* su resultado.
* Crea un test, utilizando las herramientas de tu lenguaje, que sea
* capaz de determinar si esa función se ejecuta correctamente.
*
* DIFICULTAD EXTRA (opcional):
* Crea un diccionario con las siguientes claves y valores:
* "name": "Tu nombre"
* "age": "Tu edad"
* "birth_date": "Tu fecha de nacimiento"
* "programming_languages": ["Listado de lenguajes de programación"]
* Crea dos test:
* - Un primero que determine que existen todos los campos.
* - Un segundo que determine que los datos introducidos son correctos."""

import unittest
from datetime import datetime, date

# def suma(n1, n2):
#     return n1 + n2


# print(suma(5, 4))

# assert suma(5, 4) == 9


"""class TestSuma(unittest.TestCase):
    def test_1(self):
        resultado = suma(5, 4)
        self.assertAlmostEqual(resultado, 9)

    def test_2(self):
        resultado = suma(5, 4)
        self.assertAlmostEqual(resultado, 10)"""


# Podemso hacer nuestro test de un aform amás corta
"""class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertAlmostEqual(suma(5, 4), 9)
        self.assertAlmostEqual(suma(5, 5), 10)
        self.assertAlmostEqual(suma(5, 5), 11)

    # con el with podemos hacer pruebas de typo, estudar más el tema.
    def test_suma_typr(self):
        with self.assertRaises(ValueError):
            suma(5, 4)
        with self.assertRaises(ValueError):
            suma("o", 7)"""


"""datos = {
    "name": "Luis",
    "age": 19,
    "birth_date": "15/06/1996",
    "programming_languages": ["Python", "React", "MySQL"],
}"""

"""
class TestDict(unittest.TestCase):
    def setUp(self):
        self.data = datos

    def test_valor_dict(self):
        self.assertIn("Luis", self.data["name"])

    def test_lenguage_dict(self):
        self.assertEqual(
            self.data["programming_languages"], ["Python", "React", "MySQL"]
        )

    def test_age_dict(self):
        self.assertEqual(self.data["age"], 19)

    def test_birth_date_dict(self):
        self.assertIn("15/06/1996", self.data["birth_date"])"""

# mouredev explicación.


class TestData(unittest.TestCase):

    def setUp(self):
        self.data = {
            "name": "Luis",
            "age": 19,
            "birth_date": datetime.strptime(
                "15-06-96", "%d-%m-%y"
            ).date(),  # 2 ulti num año
            "programming_languages": ["Python", "React", "MySQL"],
        }

    def test_fields_exist(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("birth_date", self.data)
        self.assertIn("programming_languages", self.data)

    def test_data_is_correct(self):
        self.assertIsInstance(self.data["name"], str)
        self.assertIsInstance(self.data["age"], int)
        self.assertIsInstance(self.data["birth_date"], date)
        self.assertIsInstance(self.data["programming_languages"], list)


if __name__ == "__main__":
    unittest.main()
