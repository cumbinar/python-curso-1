#separar una lista en pares e impares y ordenarla de menor a mayor

ejemplo = [ 4,55,6,88,70,11,23,45,67,44,59,11,10]
print('esta es la lista de entrada:')
print(ejemplo)

def separar_lista(lista):
    lista.sort() #ordena la lista de menor a mayor
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append (i)
        else:
            impares.append(i)   
    return pares, impares

pares, impares = separar_lista(ejemplo)  
print('Esta es la lista ordenada:')
print(ejemplo)
print('Lista de números pares:')
print(pares)
print('lista de números impares:')
print(impares)


