'''Dados los datos A, B, C que representan números enteros diferentes, construya un algoritmo
para escribir los números en forma descendente.'''

a = int(input('Ingrese el primer número: '))
b = int(input('Ingrese el segundo número: '))
c = int(input('Ingrese el tercer número: '))

if (a>b) and (a>c):
    n1 = a
    if (b>c):
        n2 = b
        n3 = c
    else:
        n2 = c
        n3 = b

if(b>a)and(b>c):
    n1 = b
    if (a>c):
        n2 = a
        n3 = c
    else:
        n2 = c
        n3 = a

if(c > a) and (c > b):
    n1 = c
    if (a > b):
        n2 = a
        n3 = b
    else:
        n2 = b
        n3 = a

print('los números ingresados son: ' + str(a)+' '+ str(b)+' '+ str(c))

print('Los números ordenados de mayor a menor son: ')
print(n1)
print(n2)
print(n3)
