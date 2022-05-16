#continue en un while, se salta una puesto

contador = 0

while contador < 5:
    contador = contador + 1
    if contador == 3:
        continue
    print('El valor del contador es: ' + str(contador))
    

