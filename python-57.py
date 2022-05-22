#Agenda con Nombre y Teléfono, estructura diccionario, clave: valor

def ingresar_contacto(listaregistros):
    nombre = input('Ingrese el Nombre: ')
    telefono = int(input('Ingrese el número de teléfono: '))
    
    #ahora se crea el diccionario llamado registro con clave: valor
    registro = {
        "nombre": nombre, 
        "telefono": telefono
        }

    listaregistros.append(registro)
    return listaregistros


def mostrar_contactos(listaregistros):
    print('CONTACTOS REGISTRADOS')
    print()
    #print(i)
    #print(listaregistros)
    for j in listaregistros:
        print('NOMBRE: '+ j["nombre"]+'  TELÉFONO: '+ str(j["telefono"]))
    print()
           


def presentar_menu():
    listaregistros = []
    while(True):
        print('Menú--AGENDA DE CONTACTOS')
        print()
        print('1. Ingresar Contacto')
        print('2. Mostrar Contactos')
        print('3. Salir')
        print()
        opc = int(input('Seleccione una opción: '))
        print()
        match (opc):
            case 1:
                listaregistros = ingresar_contacto(listaregistros)
            case 2:
                mostrar_contactos(listaregistros)
            case 3:
                break
            case _:
                print('Opción no Válida')
                print()


presentar_menu()

