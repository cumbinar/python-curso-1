# while en python

n = int(input("Ingrese un número para generar la sucesión de Fibonacci: "))

p1 = 0
p2 = 1
fibonacci = 0
contador = 0

while (contador <= n):

    print('Fibonacci ' + str(contador) + ' ' + str(fibonacci))
    p1 = p2
    p2 = fibonacci
    fibonacci = p1 + p2
    contador = contador + 1

