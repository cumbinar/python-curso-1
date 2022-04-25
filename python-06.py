#Condicional if else para saber si ers mayor de edad

nombre = input('Ingresa tu nombre y oprime enter ')
edad = int(input('Ingresa tu edad y oprime enter '))


if edad >= 18:
    print( nombre+ ' Eres mayor de edad')
else:
    print(nombre+ ' eres menor de edad')