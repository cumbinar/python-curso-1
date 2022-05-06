#Obtener promedio de tres notas con for in range

acumulado = 0

for i in range(3):
    nota = float(input('Ingrese una nota:  '))
    acumulado += nota

promedio = acumulado/3

print('El promedio de las notas es: '+ str(promedio))