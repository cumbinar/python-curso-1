#Range o secuencia numérica

a = range(5)
print(a)
print(a[3])

for i in a:
    print(str(a[i]) + ' Cumbi')

for i in range(5):  #crea un rango de cero a antes del 5
    print('Hola Cumbi')

for i in range(8, 15): #crea un rango del 8 a antes del 15
    print(i)


for i in range(0, 16, 3): #genera un rango entre el 0 y antes del 16 con un paso de 3
    print(i)

   