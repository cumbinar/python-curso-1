#separar una lista en pares e impares

ejemplo = [ 4,55,6,88,70,11,23,45,67,44,59,11,10]

def separar_lista(lista):
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append (i)
        else:
            impares.append(i)   
    return pares, impares

pares, impares = separar_lista(ejemplo)  
print(ejemplo)
print(pares)
print(impares)


