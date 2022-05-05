'''Escriba un algoritmo que, dado un valor N, imprima cada uno de los términos de la serie 2,5,7,10,12,15,17,..., hasta antes de N. Además que calcule la suma de los términos.'''

n = int(input('Valor hasta donde se debe imprimir:  '))
valor = 2
pos = 1

while(valor < n ):
    print(valor)
    if(pos % 2 == 1):
        valor = valor + 3       
    else:
        valor = valor + 2     
    pos = pos + 1


