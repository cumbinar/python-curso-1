#Calculadora de áreas de superficie de: Rectángulo, Triángulo y Trapecio

#funcion que pide los datos, calcula el área del rectángulo y los muestra
def area_rectangulo():
    largo = int(input('Ingrese el LARGO del RECTÁNGULO:  '))
    ancho = int(input('Ingrese el ANCHO del RECTÁNGULO:  '))
    area = largo * ancho
    print('El área del triángulo es:  '+ str(area))

#funcion que pide los datos, calcula el área del triángulo y los muestra
def area_triangulo(): 
    pass
#funcion que pide los datos, calcula el área del trapecio y los muestra
def area_trapecio():
    lado_mayor = int(input('Ingrese el lado MAYOR del TRAPECIO:  '))
    lado_menor = int(input('Ingrese el lado MENOR del TRAPECIO:  '))
    alto = int(input('Ingrese la ALTURA del TRAPECIO:  '))
    area = (lado_mayor + lado_menor) * alto / 2
    print('El área del TRAPECIO es:  ' + str(area))


#funcion que muestra opciones de un menu
def menu_areas():
    while(True):
        print('Para el área RECTANGULAR, digite:   1 ')
        print('Para el área TRIANGULAR,  digite:   2 ')
        print('Para el área TRAPEZOIDAL, digite:   3 ')
        print('Para terminar el proceso, digite:   4 ')
        opc = int(input('Seleccione una opción:  '))

        match (opc):
            case 1:
                area_rectangulo()
            case 2:
                area_triangulo()
            case 3:
                area_trapecio() 
            case 4:
                print('Termina el proceso') 
                break   
            case _: 
                print('Opción no válida')      
menu_areas()