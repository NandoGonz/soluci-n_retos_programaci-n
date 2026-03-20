num = int(input("ingrese un numero: "))
for i in range(1, num):
    if i % 2 != 0:
        print(f"{i} es primo")
