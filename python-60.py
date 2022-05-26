import os


#LIMPIAR PANTALLA

def crear_linea():
    print("="*50)

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

    for pos, contacto in enumerate(lista_contactos):

        print(str(pos)+" " + contacto["nombres"] + " " + contacto["apellidos"])


#MOSTRAR UN CONTACTO

# Preguntar por la posición

# Mostrar todos los datos del contacto + edad + todos los numeros

def mostrar_contacto(lista_contactos):

    mostrar_contactos(lista_contactos)

    pos = int(input("Ingrese posición de contacto a mostrar: "))

    if (pos < 0 or pos >= len(lista_contactos)):

        print("No se puede mostrar contacto")

    else:

        print("Nombre:    "+lista_contactos[pos]["nombres"])

        print("Apellidos: "+lista_contactos[pos]["apellidos"])

        print("Edad:      "+str(lista_contactos[pos]["edad"]))

        for i in lista_contactos[pos]["listatelefonos"]:

            print("Telefono:   "+str(i))


#EDITAR UN CONTACTO

# Preguntar por la posición

# Preguntar por nombres, apellidos, edad

# Hacer un ciclo para preguntar por los números de teléfono

def editar_contacto(lista_contactos):

    mostrar_contactos(lista_contactos)

    pos = int(input("Ingrese posición de contacto a editar: "))

    contacto = crear_contacto()

    lista_contactos[pos] = contacto

    return lista_contactos


#BUSCAR UN CONTACTO

# Preguntar la subcadena a buscar en los nombres

# Si encuentra uno, imprimir con la posición

def buscar_contacto(lista_contactos):

    subcadena = input("Ingrese parte del nombre a buscar: ")

    subcadena = subcadena.lower()

    for pos, contacto in enumerate(lista_contactos):

        if (contacto["nombres"].lower().count(subcadena) > 0):

            print(str(pos)+" " +
                  contacto["nombres"] + " " + contacto["apellidos"])


#BORRAR UN CONTACTO

# Preguntar por la posición

# Borrar


def presentar_menu():

    listaregistros = []

    while (True):

        crear_linea()

        print("MENU DE CONTACTOS")
        crear_linea()

        print("1. Ingresar contacto")

        print("2. Mostrar lista de contactos")

        print("3. Mostrar un contacto")

        print("4. Editar un contacto")

        print("5. Buscar un contacto")

        print("9. Salir")

        opc = int(input("Seleccione opción: "))

        crear_linea()

        match (opc):

            case 1:

                listaregistros = ingresar_contacto(listaregistros)

            case 2:

                mostrar_contactos(listaregistros)

            case 3:

                mostrar_contacto(listaregistros)

            case 4:

                listaregistros = editar_contacto(listaregistros)

            case 5:

                buscar_contacto(listaregistros)

            case 9:

                break

            case _:

                pass


presentar_menu()
