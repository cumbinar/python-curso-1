#Agenda con diccionario

def ingresar_contacto(listaregistros):
    nombre = input('Ingrese el Nombre: ')
    telefono = int(input('Ingrese el número de teléfono: '))
    registro = {
        'nombre': nombre, 
        'telefono': telefono
        }
    listaregistros.append(registro)
    return listaregistros


def mostrar_contactos(listaregistros):
    for i in listaregistros:
        print('CONTACTOS REGISTRADOS')
        #print(i)
        #print(listaregistros)
        for j in listaregistros:
            print('NOMBRE: '+ j['nombre']+'  TELÉFONO: '+ str(j['telefono']))
           


def presentar_menu():
    listaregistros = []
    while(True):
        print('AGENDA DE CONTACTOS')
        print('1. Ingresar Contacto')
        print('2. Mostrar Contactos')
        print('3. Salir')
        opc = int(input('Seleccione una opción: '))
        match (opc):
            case 1:
                listaregistros = ingresar_contacto(listaregistros)
            case 2:
                mostrar_contactos(listaregistros)
            case 3:
                break
            case _:
                print('Opción no Válida')


presentar_menu()

