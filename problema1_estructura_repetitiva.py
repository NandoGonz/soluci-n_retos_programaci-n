'''Se necesita diseñar un algoritmo que permita mostrar por
pantalla una cantidad de elementos de la serie de Fibonacci, para esto se
debe capturar un número entero positivo mayor que 1 por el teclado y
esa debe ser la cantidad elementos a mostrar'''
# Nombre: Luis Fernando Gonzalez Borja
# Grupo: 19
# Programa: Ingeniería de sistemas 
# Código fuente: Autoría propia

# Solicitamos el ingreso de un número mayor a 1.
# Nos aseguraremos de que el valor ingresado por teclado sea un número positivo. 

while True:
    try: 
        num = int(input("ingrese un número de elementos a mostrar: "))
        if num > 1:
            break
        else:
            print("ERROR no es un número positivo: ")
    except:
        print("ingrese un valor numérico: ")  
#generamos el número Fibonacci para buscar los elementos a mostrar.          
a,b= 0,1

for i in range(num):
    
# Mostramos en pantalla la cantidad de elementos.    
    print(a,  end = " " )
    a,b = b, a  + b
    
