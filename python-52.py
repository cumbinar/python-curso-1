#listas

numeros = [1, 2, 38, 4]
nombres = [ 'Eduardo', 'Juán', 'Pedro', 'Roberto']

print(numeros)
print(numeros[2])
print(nombres)
print(nombres[2])

numeros.append(555)
print(numeros)

nombres.append('CUMBI')
print(nombres)

numeros.insert(0, 8896)
print(numeros)

nombres.insert(3, 'Filomena')
print(nombres)

nombres[0] = 'Ruperto'
print(nombres)

for i in nombres:
    print('Nombre registrado: '+i)


nombres2 = len(nombres)
print(nombres2)

def imprimirNombres(nombres):
    for i in nombres:
        print('Nombre registrado en la LISTA: '+i)

imprimirNombres(nombres) 

nombres.pop(2) #elimina el de la posición 2
print(nombres)

imprimirNombres(nombres)

nombres.append('Filomena')
print(nombres)
nombres.remove('Filomena')

imprimirNombres(nombres)

lugar = nombres.index('Filomena')
print(lugar)




