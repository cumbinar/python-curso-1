#agenda con nombres y teléfonos con correspondencia de listas

def ingresar_contacto(listanombres, listatelefonos):
    #operaciones
    nombre = input('Digite el nombre a agregar: ')
    telefono = input('Ingrese el número de teléfono: ')
    listanombres.append(nombre)
    listatelefonos.append(telefono)
    return listanombres, listatelefonos
    

def mostrar_contactos(listanombres, listatelefonos):
    for i in range(len(listanombres)): #el [i] va hasta la longitud del string
        print('Nombre: ' + listanombres[i] + ', -- Teléfono: ' + str(listatelefonos[i]))

def presentar_menu():
    listanombres = []
    listatelefonos = []
    while(True):    
        print('MENU DE CONTACTOS')
        print('1: Ingresar Contacto: ')
        print('2: Mostrar Contactos: ')
        print('3: Salir: ')

        opc = int(input('Seleccione una Opción: '))
        match(opc):
            case 1:
                listanombres, listatelefonos = ingresar_contacto(listanombres, listatelefonos)
            case 2:
                mostrar_contactos(listanombres, listatelefonos)
            case 3:
                break
            case _:
                pass

presentar_menu()
