#match case 
print('Selecciona el color de la bandera: 1 = Amarillo, 2 = Azul, 3 = Rojo')
posicion = int(input('Ingresa número del color de la bandera de colombia:  '))

match posicion:
    case 1:
        print('Seleccionaste el color Amarillo')
    case 2:
        print('Seleccionaste el color Azul')
    case 3:
        print('Seleccionaste el color Rojo')
    case _:
        print('No corresponde a la bandera1')
