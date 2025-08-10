"""* EJERCICIO:
* - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
*   en tu lenguaje.
* - Utiliza operaciones de inserción, borrado, actualización y ordenación.
*
* DIFICULTAD EXTRA (opcional):
* Crea una agenda de contactos por terminal.
* - Debes implementar funcionalidades de búsqueda, inserción, actualización
*   y eliminación de contactos.
* - Cada contacto debe tener un nombre y un número de teléfono.
* - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
*   y a continuación los datos necesarios para llevarla a cabo.
* - El programa no puede dejar introducir números de teléfono no numéricos y con más
*   de 11 dígitos (o el número de dígitos que quieras).
* - También se debe proponer una operación de finalización del programa."""

my_list = [
    1,
    2,
    3,
    0,
    8,
    6,
    7,
]

my_list.append("jajajaja")
# my_list = list(sorted(my_list)) # no soporta int y str en la misma lista

my_list.reverse()
my_list[2] = True
my_list.remove(3)
my_list.insert(0, 20)

print(type(my_list))
print(my_list)

# el metodo pop() remueve el ultimo elemento de la lista
# el metodo pop(indice) eliima el valor del indice y devuelve el valor asociado
ultimo_elemento = my_list.pop(3)
print(my_list)
print(ultimo_elemento)

# metodo index
indice_risa = my_list.index("jajajaja")
print(indice_risa)
print(len(my_list))


# dicionario
my_dict = {"padre": "Luis", "madre": "Adriana", "hija": "Kristina", "hijo": "Emiro"}

# cambiando el valor de una llave, una forma de cambiar el valor de una llave en especifio
cambio_valor = my_dict["madre"] = "Cristina"

# metodo get(clave) muestra el valor de la llave seleccionada
clave_padre = my_dict.get("padre")

# agregando clave y valores con el metodo update
# Creando un diccionario nuevo
nuevos_integrantes = {"abuela": " Mayerlis", "abuela2": "Monica"}
my_dict.update(nuevos_integrantes)
# udando el metodo update() directamente
my_dict.update([("abuelo2", "Hector"), ("tio", "Jairo")])
abuelo1 = my_dict.pop("abuelo2")
my_dict.pop("padre")
print(list(my_dict.keys()))
print(list(my_dict.values()))
print(clave_padre)
print(cambio_valor)
print(my_dict)
# El metodo items() devuelve una vista de lo dares clave-valor del dict
print(my_dict.items())

# Tuplas
# se definen con parectecis
my_tuple1 = (2, "Nando", True, 0.34)
my_tuple2 = (7, "Adriana", False, 0.39)

# concatenmación de tuplas
my_tuple = my_tuple1 + my_tuple2

# repétición
repetidor = my_tuple2 * 2


print(my_tuple)
print(repetidor)
print(True in my_tuple2)
# verificador de pertenencia
print(True in my_tuple1)
# rebanada podemos estraer elementos de la tupla o subconjuhntos de esta(slicing)
print(my_tuple2[2:4])
# desmquetado asignamos elementos de la tupla a variables
a, b, c, e = my_tuple2
print(a, b, c, e)
print(b, c, e)
# indexacion
print(my_tuple.index(False))


# devolución de datos por medio de un metodo creado
def obtener_datos():
    return (1, "Kristina", False)


d1, d2, d3 = obtener_datos()
print(d1, d2, d3)

my_set = {True, 45, 0.15, "Alonso", 0.32}

# Existen muchas formas de eliminar un elemento de un set
# my_set.discard(True)
# my_set.remove("Alonso")
# removido = my_set.pop() # Al parecer elimina un valor flotante y cada vez que se ejecute eliminara el mismo
# my_set.clear() # Elimina todos los elmentos y devuelve el set vacio

# Usando el metodo conjunto() y su variacion
my_set2 = {False, "Fernando", 1.50, 3, 20}
union_sets = my_set.union(my_set2)
union_sets2 = my_set | my_set2

# Agregando elemento add()
print(my_set.add("Emiro"))
print(my_set)
print(f"Esta es la union de: {my_set} con {my_set2} y es: {union_sets}")
print(f"Esta es la forma 2 de la union de: {my_set} con {my_set2} y es: {union_sets2}")

# Aplicando el metodo interseccion y su variacion
my_set = {True, 45, 0.15, "Alonso", 0.32}
my_set2 = {False, "Fernando", 0.15, 3, 20}

# Buscamos la interseccion
interseccion = my_set.intersection(my_set2)
interseccion2 = my_set & my_set2

print(interseccion)
print(interseccion2)

# Aplicando la diferencia simetrica y su variante
diferencia_simetrica = my_set.symmetric_difference(my_set2)

# Otra forma de usar la difirencia simetrica
diferencia_simetrica2 = my_set ^ my_set2

print(diferencia_simetrica)
print(diferencia_simetrica2)

# Solución a ejercico extra
# Creo mi estructura de control
agenda_contactos = {}


# Creare un menú para mostrar los metodos que se pueden utilizar
def menu():
    print("######################################################")
    print("1. Buscar contacto")
    print("2. Agregar contacto")
    print("3. Actulizar contacto")
    print("4. Eliminar contacto")
    print("5. Mostrar agenda")
    print("0. Salir")
    print("######################################################")


# Creare un metodo de búsqueda
def busqueda():
    nombre = input("Ingresa el nombre del contacto: ")
    if nombre in agenda_contactos:
        print(
            f"El contacto {nombre} se encuentra registrado con el numero {agenda_contactos[nombre]}"
        )
    else:
        print(f"No hay un contacto registrado con el nombre {nombre}")


# Creare un metodo para agregar un elemento nuevo a la estructura de contol
def agregar_nuevo():

    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingrese el numero de telefono: ")
    if (
        telefono.isdigit() and len(telefono) > 0 and len(telefono) < 11
    ):  # para aplicar esta linea debe ser una cadena de texto la variable
        agenda_contactos[nombre] = telefono
        print(
            f" ✅ El contacto {nombre} fue registrado de manera exitosa con el número{agenda_contactos[nombre]}"
        )
    else:
        print(
            "ERROR: ⚠️  Debe ingresar un número de telefono con menos de 11 caracteres ⚠️ "
        )


# Creo un metodo para actualizar la estructura de control
def actualizar():

    nombre = input("Ingresa el nombre del contacto a actualizar: ")
    telefono = input("Ingrese el nuevo numero de telefono: ")
    if nombre in agenda_contactos:
        if (
            telefono.isdigit() and len(telefono) > 0 and len(telefono) < 11
        ):  # para aplicar esta linea debe ser una cadena de texto la variable
            agenda_contactos[nombre] = telefono
            print(
                f" El contacto {nombre} fue agregado exitosamente con el número {telefono} en agenda de contactos"
            )
        else:
            print(
                "ERROR: ⚠️  Debe ingresar un número de telefono con menos de 11 caracteres ⚠️ "
            )
    else:
        print("El contacto no existe")


# Creo un metodo para eliminar elementos de la estructura de control
def eliminar():

    nombre = input("Ingresa el nombre del contacto: ")
    if nombre in agenda_contactos:
        del agenda_contactos[nombre]
        print(f"El contacto {nombre} fue eliminado")
    else:
        print("El contacto no existe")


def mostrar_agenda():

    if agenda_contactos:
        print("📒 Agenda de contactos:")
        for nombre, telefono in agenda_contactos.items():
            print(f"📌 {nombre}: {telefono}")
    else:
        print("La agenda está vacía.")


def main():

    while True:
        menu()
        try:
            opcion = int(input("Ingrese una opción: "))

            match opcion:
                case 1:
                    busqueda()

                case 2:
                    agregar_nuevo()

                case 3:
                    actualizar()

                case 4:
                    eliminar()

                case 5:
                    mostrar_agenda()

                case 0:
                    print("Gracias por usar su agenda de confianza")
                    break

        except ValueError:
            print("Por favor ingrese un valor dentro del rango mostrado")


if __name__ == "__main__":
    main()
