#calculadora básica con funciones y match(opc):

def sumar(a, b):
    res = a + b
    print()
    print('El RESULTADO de SUMAR '+ str(a)+' más ' + str(b)+ ' es '  + str(res))

def restar(a, b):
    res = a - b
    print()
    print('El RESULTADO de la RESTAR ' + str(a) +' menos ' + str(b) + ' es ' + str(res))

def multiplicar(a, b):
    res = a * b
    print()
    print('El RESULTADO de MULTIPLICAR '+ str(a)+' por ' + str(b)+ ' es ' + str(res))

def dividir(a, b):
    if(b != 0):
        res = a / b
        print()
        print('El RESULTADO de DIVIDIR ' + str(a)+' entre ' + str(b) + ' es ' + str(res))
    else:
        print()
        print('NO es POSIBLE dividir ' +  str(a) + ' entre CERO ')


while(True):
    print()
    print('Para SUMAR digite:       1')
    print('Para RESTAR digite:      2')
    print('Para MULTIPLICAR digite: 3')
    print('Para DIVIDIR digite:     4')
    print('Para SALIR digite:       5')
    print()

    opc = int(input('Seleeccione una opción: '))

    match(opc):
        case 1:
            a = int(input('Ingrese el PRIMER  número para SUMAR: '))
            b = int(input('Ingrese el SEGUNDO número para SUMAR: '))
            sumar(a, b)
          

        case 2:
            a = int(input('Ingrese el PRIMER  número para RESTAR: '))
            b = int(input('Ingrese el SEGUNDO número para RESTAR: '))
            restar(a,b)

        case 3:
            a = int(input('Ingrese el PRIMER número  MULTIPLICAR: '))
            b = int(input('Ingrese el SEGUNDO número MULTIPLICAR: '))
            multiplicar(a, b)

        case 4:
            a = int(input('Ingrese el PRIMER  número para DIVIDIR: '))
            b = int(input('Ingrese el SEGUNDO número para DIVIDIR: '))
            dividir(a, b)

        case 5:
            print()
            print('Fin del cálculo')
            print()
            break
        case _:
            print()
            print('ERROR')
            print()
       

