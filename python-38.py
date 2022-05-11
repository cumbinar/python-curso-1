#calculadora básica con funciones y match(op):

from pickletools import read_bytes1


def sumar(a, b):
    res = a + b
    print('El resultado de la SUMA es: ' + str(res))

def restar(a, b):
    res = a - b
    print('El resultado de la RESTA es: ' + str(res))

def multiplicar(a, b):
    res = a * b
    print('El resultado de la MULTIPLICACIÓN es: ' + str(res))

def dividir(a, b):
    if(b != 0):
        res = a / b
        print('El resultado de la DIVISIÓN es: ' + str(res))
    else:
        print('NO es posible dividir entre CERO')    

print('Para SUMAR digite el número 1')
print('Para RESTAR digite el número 2')
print('Para MULTIPLICAR digite el número 3')
print('Para DIVIDIR digite el número 4')
print('Para SALIR digite el número 5')


opc = int(input('Seleeccione una opción: '))



match(opc):
    case 1:
        a = int(input('Ingrese el PRIMER número: '))
        b = int(input('Ingrese el SEGUNDO número: '))
        sumar(a, b)

    case 2:
        a = int(input('Ingrese el PRIMER número: '))
        b = int(input('Ingrese el SEGUNDO número: '))
        restar(a,b)

    case 3:
        a = int(input('Ingrese el PRIMER número: '))
        b = int(input('Ingrese el SEGUNDO número: '))
        multiplicar(a, b)

    case 4:
        a = int(input('Ingrese el PRIMER número: '))
        b = int(input('Ingrese el SEGUNDO número: '))
        dividir(a, b)

    case 5:
        print('Fin del cálculo')
        opc = False
    case _:
        print('ERROR')
       

