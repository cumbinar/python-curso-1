#Obtener el promedio de 4 números enteros y verificar cuál es el menor y cuál es el mayor

acumulado = 0
menor = 0
mayor = 0

for i in range(4):
    numero = int(input('Ingrese un número entero:  '))
    acumulado += numero
    if (i == 0):
        menor = numero
        mayor = numero
    else:
        if(numero < menor):
            menor = numero 
        if(numero > mayor):
            mayor = numero       

promedio = acumulado/4

print('El promedio de las notas es: ' + str(promedio))
print('El número menor es: ' + str(menor))
print('El número Mayor es: ' + str(mayor))

