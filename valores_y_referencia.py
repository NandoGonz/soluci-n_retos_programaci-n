"""/*
* EJERCICIO:
* - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
*   su tipo de dato.
* - Muestra ejemplos de funciones con variables que se les pasan "por valor" y
*   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
* (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
*
* DIFICULTAD EXTRA (opcional):
* Crea dos programas que reciban dos parámetros (cada uno) definidos como
* variables anteriormente.
* - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
*   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
*   se asigna a dos variables diferentes a las originales. A continuación, imprime
*   el valor de las variables originales y las nuevas, comprobando que se ha invertido
*   su valor en las segundas.
*   Comprueba también que se ha conservado el valor original en las primeras."""

# Asignación por valor

a = 5
b = a
b = 4

b += a

print(a)
print(b)

# por valor en str

palabra1 = "hola".title()
palabra2 = palabra1
palabra2 = palabra2 + " " + "python".title()

print(palabra1)
print(palabra2)

# Por referencia

colores1 = ["amarillo", "azul", "rojo"]
colores2 = colores1
colores2.append("fucsia")
colores2[0] = "verde"

print(colores1)
print(colores2)

diccionario1 = {"altura": 78, "edad": 4}
diccionario2 = diccionario1
diccionario2["sexo"] = 4

print(diccionario1)
print(diccionario2)


def datos_por_valor(x):
    """En esta funcion se usan datos por valor"""
    x += 9
    return x


valor_fuera = 45

print(datos_por_valor(9))
print(f" Este valor esta por fuera de la fucnion: {valor_fuera}")


def datos_por_referencia(lista):
    lista.append(7)

    nueva_lista = lista
    print(lista)
    print(nueva_lista)


nueva_lista_2 = [30, 78]
datos_por_referencia(nueva_lista_2)
print(nueva_lista_2)


# Extra


def inversor(valor_a, valor_b):
    # Demos crear una variable para asignar el valor de una poder realizar la modificacion
    aux = valor_a
    valor_a = valor_b
    valor_b = aux
    return valor_a, valor_b


valor_c = 45
valor_d = 15
valor_e, valor_f = inversor(valor_c, valor_d)
print(f"{valor_c} {valor_d}")
print(f"{valor_e} {valor_f}")

# Por refencia


def inversor_ref(list1: list, list2: list):
    """Mantiene los valores de una lista y los invierte"""
    aux_list = list1
    list1 = list2
    list2 = aux_list
    # Ahora modificaremos el valor de una lista y esto afecta a todas
    list1.append(7)
    aux_list.append(8)
    return list1, list2


list3 = [67, 90]
list4 = [3, 45]
list5, list6 = inversor_ref(list3, list4)
print(f"{list3} -- {list4}")
print(f"{list5} -- {list6}")
