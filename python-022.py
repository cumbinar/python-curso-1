'''Dados los datos A, B, C que representan números enteros diferentes, construya un algoritmo
para escribir los números en forma descendente.'''

a = int(input("Esciba un número entero: "))
b = int(input("Esciba un número entero: "))
c = int(input("Esciba un número entero: "))

if a > b > c:
    print("El orden de los números  es: ", a, ">", b, ">", c)

elif a > c > b:
    print("El orden de los números es: ", a, ">", c, ">", b)

elif b > a > c:
    print("El orden de los números  es: ", b, ">", a, ">", c)

elif b > c > a:
    print("El orden de los números es: ", b, ">", c, ">", a)

elif c > a > b:
    print("El orden de los números es: ", c, ">", a, ">", b)

elif c > b > a:
    print("El orden de los números es: ", b, ">", c, ">", a)
