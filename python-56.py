#Agenda con registros concatenados con formato csv

def ingresar_contacto(listanombres, listatelefonos):
    nombre = input('Ingrese el Nombre: ')
    telefono = int(input('Ingrese el número de teléfono: '))
    listanombres.append(nombre)
    listatelefonos.append(telefono)
    return listanombres, listatelefonos


def mostrar_contactos(listanombres, listatelefonos):
    for i in range(len(listanombres)):
       
        print('Nombre: '+listanombres[i] +'  Teléfono: '+str(listatelefonos[i]))  

def presentar_menu():
    listanombres = []
    listatelefonos = []
    while(True):
        print('AGENDA DE CONTACTOS') 
        print('1. Ingresar Contacto') 
        print('2. Mostrar Contactos')
        print('3. Salir')
        opc = int(input('Seleccione una opción: '))  
        match (opc):
            case 1:
                listanombres, listatelefonos = ingresar_contacto(listanombres, listatelefonos)
            case 2:
                mostrar_contactos(listanombres, listatelefonos)
            case 3:
                break
            case _:
                print('Opción no Válida')

presentar_menu()                
                      



