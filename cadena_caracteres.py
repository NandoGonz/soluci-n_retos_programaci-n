'''*
 * EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas'''

# Maniulación de cadenas 

c1 = "Hola".upper()
c2 = "Python".lower()

# Puerdo crear un variable para realizar la concatenacion dentri de ella+
# Podemos acceder a estos metodos de forma directa usando el metodo print()
c_concatenada = c1 + " " + c2
print(c_concatenada)
# Puedo realizar la concatenación dentro de un print
print(c1 + " " + c2)

# Repeticion de cadenas 
c3 = "Nando"
repetididor_c = c3 * 3
print(repetididor_c)
print(c3 * 3)

# Indesxación (acceder caracter por caracter)
print(c3[3])

#Segmectacion o slicing 
print(c3[2:])
print(c3[::-1])
# Saber la cantidad de caracteres 
print(len(c1)) 

# Reempazando texto cin metedo replace()
texto = "Hola mundo, Hola mundo"
c5 = texto.replace("mundo", "Amigos")
print(f"el valor c5 es {c5}")

# creando subcadenas a partir de una cadena de texto con el metodo split()
texto1 = "estoy usando funciones nativas en python, siga la practica"
partes1 = texto1.split()
print(partes1)
print(texto1.split())

# separador iterable join() convierte estrucuturas de datos en cadena de caracteres
colores = ["red", "green", "blue"]
cadena_unida = ",".join(colores)
print(colores)
print(cadena_unida)
print(type(cadena_unida))

colore_tupla = ("red","green", "blue")
cadena_tupla = ",".join(colore_tupla)
print(cadena_tupla)
print(type(colore_tupla))



def revisar(palabra1: str, palabra2: str):
    
    # Palindromos
    print(f"¿{palabra1} es un palindromo?: {palabra1 == palabra1[::-1]}")
    print(f" ¿{palabra2} es un palindromo?: {palabra2 == palabra2[::-1]}")
    
    # Anagrama
    print(f" ¿{palabra1} es un anagrama de {palabra2} ?: {sorted(palabra1) == sorted(palabra2)}") 
    
    # Isograma usamos tuplas para verificar si es un isograma o no

    def isograma(palabra: str) -> bool:
    
        palabra_dict = dict()
        for letra in palabra:
            palabra_dict[letra] = palabra_dict.get(letra, 0) + 1 
            
        isograma = True
        valor = list(palabra_dict.values())
        contador_palabra = valor[0]
        for palabra_contador in valor:
            if palabra_contador != contador_palabra:
                isograma = False
                break
        return isograma
    
    #print(f"¿{palabra1} es un isograma ?: {isograma(palabra1)}")
    print(f"¿{palabra2} es un isograma ?: {isograma(palabra2)}")
        

    
revisar("radar", "pythonpythonpython")
#revisar("amor", "roma")