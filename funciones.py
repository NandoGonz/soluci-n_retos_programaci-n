# FUNCION NORMAL
def saludar():
    print("Hola, estimados")
    
saludar()    


# FUNCION CON RETURN
def saludar_return():
    return "Luis"


saludar = saludar_return()
print(f"Bienvenido {saludar}")

# FUNCION CON ARGUMENTOS
def saludar_argumeto(nombre):
    print(f"BIENVENIDO {nombre}")
    
saludar_argumeto("Emiro") 
    
    
# funcion con argumento prederterminado
def prede_saludar_argumetno(nombre = "Visitante"):
    print(f"Welcome {nombre} gracias por su visita")    
    
    
prede_saludar_argumetno()

# funcion con retorno y argumentos 
def retorno_argumento_saludo(nombre, apellido): 
    return f"{nombre} {apellido}"   

print(retorno_argumento_saludo(f"luis", "gonzalez"))


# retorno de varios valores podemos crear variables que tiene funcionde un iterador 
def varios_retornos_saludo():
    return "Hola", "Python"

saludo, name = varios_retornos_saludo() 
print(saludo)
print(name)
    
    
# funciones con un número varibale de argumentos, colocaremos un * delante del parametro de nuestra fucion
def arg_variable_saludo(*names):
    # usaremos un ciclo for para recorrer los arguentos que igresaremos
    for name in names:
        print(f"Bienvenido {name}")
        
        
arg_variable_saludo("luis", "gonzalez", "sigue dando lo mejor", "cree en tí")


'''funciones con un numero variable de argumentos con palabras clave usando ** delante del parametro y esto nos da entender que cada argumento tendra una clave y un valor. Usamos la palabra reservada items() para recorrer cada llave y valor'''   
def variable_clave_valor_saludo(**names):
    for parametro in names.items():
        print(f"{name} {parametro}")
        
variable_clave_valor_saludo(
    lenguaje = "Python", 
    nombre = "Luis", 
    alias = "NAN2ELMANK", 
    edad = 39
    )        

# para crear una funcion dentro de otra debemos llamar la funcion interna dentro de la externa
def mayor_func():
    def menor_func():
        print("Funciones anidadas xd")
    menor_func()
    
mayor_func()        
    


