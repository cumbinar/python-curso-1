#funciones
# esta es una función básica de suma

def suma(a, b):
  return a + b

result = suma(1, 2)

print(result)  # result = 3

numero1 = int(input('Ingrese un número entero:  '))
numero2 = int(input('Ingrese OTRO número entero:  '))

result2 = suma(numero1, numero2) #la función se puede reurilizar

print(result2)
