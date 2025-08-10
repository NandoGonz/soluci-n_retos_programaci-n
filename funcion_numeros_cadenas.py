'''Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.'''


def convertidor_tex_num(text_1, text_2):
    count = 0
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print(text_1, text_2)
        elif numbers % 3 == 0:
            print(text_1)
        elif numbers % 5 == 0:
            print(text_2)
        else:
            print(numbers)
            count += 1
    return count




print(convertidor_tex_num("text_1", "text_2"))