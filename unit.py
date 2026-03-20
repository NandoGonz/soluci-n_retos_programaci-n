"""En este reto tengo que calcular el nivel de felicidad  de cada compañero del equipo y
calcular de forma individual de cada miembro <= 5 'Get Out Now!'
pero si es mayor 'Nice Work Champ!', tengo que mostrar el mensaje solo con ingresar
el nombre del compañero de trabajo y tengo que mostrar la punuacion del jefe es el doble del grupo

salidad esperadas({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5,
'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura'), 'Get Out Now!')

({'tim':1, 'jim':3, 'randy':9, 'sandy':6, 'andy':7
'katie':6, 'laura':9, 'saajid':9, 'alex':9, 'john':9, 'mr':8}, 'katie'), 'Nice Work Champ!')

{'tim':2, 'jim':4, 'randy':0, 'sandy':5, 'andy':8,
'katie':6, 'laura':2, 'saajid':2, 'alex':3, 'john':2, 'mr':8}, 'john'), 'Get Out Now!')
al ingresar el nombre de un compañero y tambien debemos usar los diccionarios dados"""

"""
def outed(meet, boos):
    pass


people = {
    "tim": 0,
    "jim": 2,
    "randy": 0,
    "sandy": 7,
    "andy": 0,
    "katie": 5,
    "laura": 1,
    "saajid": 2,
    "alex": 3,
    "john": 2,
    "mr": 0,
}
"""
"""n = int(input(()))
num = 1
for i in range(1, n + 1):
    num *= i

    print(num)
"""


def recur(n):
    if n == 0:
        return 1
    recursivo = recur(n - 1)
    resultado = n * recursivo
    return resultado


print(recur(1))
