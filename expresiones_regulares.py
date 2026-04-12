"""EJERCICIO:
Utilizando tu lenguaje, explora el concepto de expresiones regulares,
creando una que sea capaz de encontrar y extraer todos los números
de un texto. DIFICULTAD EXTRA (opcional):
Crea 3 expresiones regulares (a tu criterio) capaces de:
- Validar un email.
- Validar un número de teléfono.
- Validar una url."""

import re

TEXTO = """Al voltear, vio 0 seres diminutos, 1 gran 2opo, 3 ratones, 4 mariposas,
5 estrellasfugaces,6 nubes de algodón, 7 soles brillantes, 8 lunas gemelas
y 9 cometas danzando a su alrededor."""

# Para extraer los números usaremso el método re.findaall
# se utiliza para buscar todas las coincidencias de un patrón (expresión regular) dentro de un texto

search_num = re.findall(r"\d+", TEXTO)
print(search_num)

# se utiliza para sustituir todas las coincidencias de un patrón de expresión regular en una cadena por un nuevo texto
r2 = re.sub(r"2", "dos", "Tengo 2 gatos y 3 perros")
print(r2)
r2 = re.sub(r"3", "tres", r2)
print(r2)


def validar_email(email):
    usuario = r"[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+"
    arroba = r"@"
    dominio = r"[a-zA-Z0-9-]+"
    tld = r"(?:\.[a-zA-Z0-9-]+)*"

    email_regex = rf"^{usuario}{arroba}{dominio}{tld}$"

    return re.match(email_regex, email) is not None


print(validar_email("gonzalez12345@hotmail.com"))
print(validar_email("gonzalez12345@gmail.com"))
print(validar_email("gonzalez.com"))
print(validar_email("1234.lok"))
print(validar_email("@@@"))
print("#" * 60)


def validar_telefono(num_tel):
    num = r"^\d+$"
    return bool(re.match(num, num_tel))


print(validar_telefono("3013209757"))
print(validar_telefono("301320975/&7"))

# forma optima
"""
def validate_email(email):
    return bool(re.match(r"^[\w.+-]+@[\w]+\.[a-zA-Z]+$, email))
print(validate_email('lascosas@gmail.com))

def validate_phone(phone):
    return bool(re.match(r'^\+?[\d\s]{3,12}$, phone'))
print(validate_phone('43096873))

validate_url(url):
    return bool(re.match(r'^http[s]://(www.)?[\w]\.[a-zA-Z]$))
print(validate_url('https://nando.com))
"""
