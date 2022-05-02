'''Calcular el costo de envío de un paquete, con base en el volumen; si
la altura es mayor a 30 centímetros, se adiciona $2000 al costo,
si el costo es mayor a $10000, se cobra iva del 19%'''


alto = float(input('Ingrese la ALTURA del paquete '))
ancho = float(input('Ingrese al Ancho del paquete '))
profundo = float(input('Ingrese la Profundidad del paquete '))

volumen = alto*ancho*profundo

costo = volumen*5

iva = 0

if(alto > 30):
   costo = costo + 2000

if (costo > 10000):
    costo = costo +(costo * 0.19)
    iva = costo * 0.19

print('El volumen del paquete es ' + str(volumen)+ ' Centímetros cúbicos')
print('El iva del envío es de ' + str(iva) + ' Pesos')
print('El costo de envío del paquete es de '+ str(costo)+ ' Pesos')
