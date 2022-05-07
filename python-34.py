#for i in range(): Imprimir figuras con caracters 

lado = int(input('Ingrese el lado del cuadrado:  '))


for i in range(lado):
    print('M'*lado)

print('')


for i in range(lado):
     print('O')


print('')

contador = 1
for i in range(lado):
    print('S'*contador)
contador = contador + 1


print('')

contador = lado
for i in range(lado):
    print('P'*contador)
    contador -= 1


print('')


contador = lado
for i in range(lado):
    print(' ' * i + 'X'*contador)
    contador -= 1

print('')


for i in range(lado):
    if(i == 0 or i == lado-1):
        print('H'*lado)
    else:
        print('H')


print('')


for i in range(lado):
      if(i == 0 or i == lado-1):
        print('O'*lado)
      else:
        print('O' + ' '*(lado-2) + 'O')
