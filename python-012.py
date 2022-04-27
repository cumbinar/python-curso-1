# Estructuras de control

#Algoritmo que pide igresar dos números y los compara, imprime según el caso de

a1 = int(input('Ingresa un número entero: '))
b1 = int(input('Imgrese el segundo número entero: '))

if a1 == b1:
    print(str(a1) + ' es igual que ' + str(b1))
elif a1 < b1:
    print(str(a1) + ' es menor que ' + str(b1))
else:
    print(str(a1) + ' es mayor que ' + str(b1))

