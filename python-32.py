#Ciclo definido Tabla de multiplicar

numero = int(input('Ingrese el número de la tabla a calcular:  '))

for i in range(1, 11):
    res = i * numero 
    print(str(numero)+ ' X ' + str(i) + ' = ' + str(res))