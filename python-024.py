# asignar un valor booleano a una variable 

print(' Si una persona es mayor de 12 años, \n puede pasar a la montana rusa')
print('')
edad = int(input('¿Cuántos años tienes?:  '))

puedePasar = edad >= 12
hijoDelMaquinista = 'si'

if puedePasar:  # si esto en True
    print('Puedes ingresar a la montaña rusa')
else:
    hijo = input('¿Eres hijo Del maquinista?: ')
    if hijo == hijoDelMaquinista:
        print('Ingresa porque eres hijo Del maquinista')
    else:
        print('No puedes INGRESAR, hasta ser mayor de 12 años')

print('')