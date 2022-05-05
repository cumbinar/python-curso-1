n = int(input('Valor hasta donde debo imprimir:  '))

'''Escriba un algoritmo que, dado un valor N, imprima cada uno de los términos de la serie 2,5,7,10,12,15,17,..., hasta antes de N. Además que calcule la suma de los términos.'''
valor = 2
pos = 1

print(valor)
while(pos < n ):
    if(pos % 2 == 1):
        valor = valor + 3
        if(valor < n):
            print(valor)
    else:
        valor = valor + 2
        if(valor < n): 
            print(valor)   
    pos = pos + 1


