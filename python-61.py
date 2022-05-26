#Otra versión de agenda con funciones y diccionarios

import os


def linea():
    print("="*30)


def pedirdatos():
    print(agenda)
    nombre = input("Nombre del contacto: ")
    if nombre in agenda:
        print("%s: ya existe su número de teléfono es %s " %(nombre, agenda[nombre]))
        opcion = input("Pulsa 's' si quieres modificarlo!!!. Otra tecla para continuar. ")
        if opcion == "s" or opcion == "S":
            numero = input("Digita el nuevo número de teléfono: ")
            agenda[nombre] = numero
            print()
    else:
        numero = input("Digita el número de teléfono: ")
        agenda[nombre] = numero
        print()


def busqueda():
    cadena = input("Nombre del contacto a buscar: ")
    for nombre, numero in agenda.items():
        if nombre.startswith(cadena):
            print("El número de teléfono de %s es el %s " %(nombre, agenda[nombre]))


def borrar():
    nombre = input("Nombre del contacto para borrar: ")
    if nombre in agenda:
        opcion = input("Pulsa 's' si quieres borrarlo!!!. Otra tecla para continuar. ")
        if opcion == "s" or opcion == "S":
            del agenda[nombre]
    else:
        print("No existe el contacto ")


def listar():
    print()
    for nombre, numero in agenda.items():
        print(nombre, "->", numero)


agenda = {}
while True:
    linea()
    print("1 => Añadir/modificar")
    print("2 => Buscar")
    print("3 => Borrar")
    print("4 => Listar")
    print("5 => Salir")
    linea()

    opcion = int(input("selecciona una opción: "))
    if opcion == 1:
        pedirdatos()

    elif opcion == 2:
        busqueda()

    elif opcion == 3:
        borrar()

    elif opcion == 4:
        listar()

    elif opcion == 5:
        print("Termina el proceso")
        break
    else:
        print("Opción incorrecta, elija otra")
