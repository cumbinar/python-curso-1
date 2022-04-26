''''elevar al cuadrado la suma de dos números y el resultado dividirlo entre 3'''

import math


a = int(input('ingresa el primer número y enter '))
b = int(input('ingresa el segundo número y enter '))

resultado = float((a+b)**2)/3

print('El resultado es  ' + str(resultado))

import math
redondeo = math.ceil(resultado)
print(redondeo)