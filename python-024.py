# asignar un valor booleano a una variable 

print(' Si una persona es mayor de 12 años, \n puede pasar a la montana rusa')
edad = int(input('¿Cuántos años tienes?:  '))

puedePasar = edad >= 12

if puedePasar: #si esto en True
    print('Puedes ingresar a la montaña rusa')
else:
    print('No puedes INGRESAR, hasta ser mayor de 12 años')
