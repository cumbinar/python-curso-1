#Calculadora de áreas de superficie de: Rectángulo, Triángulo y Trapecio

#funcion que pide los datos, calcula el área del rectángulo y los muestra
def area_rectangulo():
    base = int(input('Ingrese la  BASE del  RECTÁNGULO:  '))
    altura = int(input('Ingrese la ALTURA del RECTÁNGULO:  '))
    area = base * altura
    print()
    print('El ÁREA Rectangular de base: '+ str(base)+ ' y altura '+str(altura)+ ',  es: '+str(area))
    print()
#funcion que pide los datos, calcula el área del triángulo y los muestra
def area_triangulo(): 
    base = int(input('Ingrese la BASE  del  TRIÁNGULO:  '))
    altura = int(input('Ingrese la ALTURA del TRIÁNGULO:  '))
    area = (base * altura)/2
    print()
    print('El ÁREA Triangular de base: '+ str(base)+ ' y altura '+str(altura)+ ',  es: '+str(area))
    print()
#funcion que pide los datos, calcula el área del trapecio y los muestra
def area_trapecio():
    lado_mayor = int(input('Ingrese el lado MAYOR del TRAPECIO:  '))
    lado_menor = int(input('Ingrese el lado MENOR del TRAPECIO:  '))
    altura = int(input('    Ingrese la ALTURA del TRAPECIO:  '))
    area = (lado_mayor + lado_menor) * altura / 2
    print()
    print('El ÁREA Trapezoidal de lado mayor: ' + str(lado_mayor) +', lado menor ' + str(lado_menor)+(' y altura ')+ str(altura) + ',  es: '+str(area))
    print()


#funcion que muestra opciones de un menu
def menu_areas():
    while(True):
        print('Para el área RECTANGULAR, digite:   1 ')
        print('Para el área TRIANGULAR,  digite:   2 ')
        print('Para el área TRAPEZOIDAL, digite:   3 ')
        print('Para terminar el proceso, digite:   4 ')
        print()
        opc = int(input('           Seleccione una opción:   '))
        print()

        match (opc):
            case 1:
                area_rectangulo()
            case 2:
                area_triangulo()
            case 3:
                area_trapecio() 
            case 4:
                print('Termina el proceso')
                print() 
                break   
            case _: 
                print('Opción no válida')      
menu_areas()