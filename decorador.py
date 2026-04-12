"""/*
* EJERCICIO:
* Explora el concepto de "decorador" y muestra cómo crearlo
* con un ejemplo genérico.
*
* DIFICULTAD EXTRA (opcional):
* Crea un decorador que sea capaz de contabilizar cuántas veces
* se ha llamado a una función y aplícalo a una función de tu elección."""


def decorador(fun):
    def n_fun(a, b):
        print("llamando la función")
        c = fun(a, b)
        print("se ha llamado")
        return c

    return n_fun


@decorador
def resta(a, b):
    print("entrando en la función")
    return a - b


resta(3, 5)
resta(3, 3)
resta(3, 6)

print("#" * 60)


def print_call(function):
    def print_function():
        print(f"La función {function.__name__} ha sido llamada")
        return function

    return print_function


@print_call
def example_function():
    pass


@print_call
def example_function2():
    pass


@print_call
def example_function3():
    pass


example_function()
example_function2()
example_function3()

# Extra
print("3" * 60)


def call_counter(function):
    def counter_function():
        counter_function.call_count += 1
        print(
            f"La funcion {function.__name__} se ha llamado {counter_function.call_count} veces."
        )
        return function

    counter_function.call_count = 0
    return counter_function


@call_counter
def example_function4():
    pass


@call_counter
def example_function5():
    pass


example_function4()
example_function4()
example_function4()
example_function4()
example_function4()
example_function5()

print("#" * 60)


def contar_fun(fun):
    def contador_fun():
        contador_fun.call += 1
        print(f"La función {fun.__name__} fue llamada {contador_fun.call} de veces")
        return fun

    contador_fun.call = 0
    return contador_fun


@contar_fun
def funcion1():
    pass


@contar_fun
def funcion2():
    pass


funcion1()
funcion1()
funcion1()
funcion2()
funcion1()
funcion1()
funcion1()
funcion2()
funcion2()
