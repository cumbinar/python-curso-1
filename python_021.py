
'''Determine si un año ingresado por teclado es o no bisiesto. Las reglas para determinar si un
año bisiesto son las siguientes: Un año es bisiesto si es divisible entre 4, pero no debe ser
divisible entre 100; sin embargo, si un año es divisible entre 100 y además es divisible entre
400, también resulta bisiesto.'''


print('DETERMINAR SI UN AÑO EN BISIESTO')

anual = int(input('Ingrese el año:  '))

if ((anual % 4) != 0 and (anual % 100) != 0):
    print(str(anual) + ' no es bisiesto')
else:
    print(str(anual) + ' Es BISIESTO ')
