#AGENDA DE TELÉFONOS, USANDO FUNCIONES

#CREAR UN CONTACTO

# Preguntar por nombres, apellidos, edad

# Hacer un ciclo para preguntar por los números de teléfono

# Retornar una estrcutura de tipo DICC

def crear_contacto():

    contacto = {}

    contacto["nombres"] = input("Ingrese nombres: ")

    contacto["apellidos"] = input("Ingrese apellidos: ")

    contacto["edad"] = int(input("Ingrese edad: "))

    contacto["listatelefonos"] = []

    while (True):

        tel = int(input("Ingrese número de teléfono o 0 para salir: "))

        if (tel == 0):

            break

        else:

            contacto["listatelefonos"].append(tel)

    print(contacto)

    return contacto


#INGRESAR UN CONTACTO

# Crear un contacto

# Añadirlo a una lista

def ingresar_contacto(lista_contactos):

    contacto = crear_contacto()

    lista_contactos.append(contacto)

    return lista_contactos


#MOSTRAR TODOS LOS CONTACTOS

# Presentar un número [posición], nombre y apellido

def mostrar_contactos(lista_contactos):

    for i in range(len(lista_contactos)):

        print(str(
            i)+" " + lista_contactos[i]["nombres"] + " " + lista_contactos[i]["apellidos"])


#MOSTRAR UN CONTACTO

# Preguntar por la posición

# Mostrar todos los datos del contacto + edad + todos los numeros


#EDITAR UN CONTACTO

# Preguntar por la posición

# Preguntar por nombres, apellidos, edad

# Hacer un ciclo para preguntar por los números de teléfono


#BORRAR UN CONTACTO

# Preguntar por la posición

# Borrar


def presentar_menu():

    listaregistros = []

    while (True):

        print("MENU DE CONTACTOS")

        print("1. Ingresar contacto")

        print("2. Mostrar lista de contactos")

        print("9. Salir")

        opc = int(input("Seleccione opción: "))

        match (opc):

            case 1:

                listaregistros = ingresar_contacto(listaregistros)

            case 2:

                mostrar_contactos(listaregistros)

            case 9:

                break

            case _:

                pass


presentar_menu()
