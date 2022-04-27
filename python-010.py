
import math

'''dadas las coordenadas de 2 puntos en el plano cartesiano (x-y),
calcular la distancia entre los mismos.'''



#ingresar los datos

x1 = int(input( 'Ingrese el valor de de X del punto 1:  '))
y1 = int(input( 'Ingrese el valor de de Y del punto 1:  '))
x2 = int(input('Ingrese el valor de de X del punto 2:  '))
y2 = int(input( 'Ingrese el valor de de Y del punto 2:  '))

#calcular la distancia

distancia = math.sqrt((x1-x2)**2 + (y1-y2)**2)

print( 'La distancia entre los dos puntos es: ' + str(distancia))