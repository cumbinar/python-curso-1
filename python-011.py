'''algoritmo que dado el nombre de un dinosaurio, su peso y su longitud, expresados
estos dos últimos en libras y yardas, respectivamente, escriba el nombre del dinosaurio, su
peso expresado en kilogramos y su longitud expresada en metros. 1 metro=1.09361 yardas
y 1 kilogramo=2.20462 libras.'''

kiloEnLibras = 2.20462
metroEnYardas = 1.09361
nombre = input('Ingresa el nombre del dinosaurio: ')
peso = float(input('Ingrese el valor del peso en libras:  '))
longitud = float(input('Ingrese el valor de la longitud en yardas:  '))

pesoEnKilos = peso / kiloEnLibras
longitudEnMetros = longitud / metroEnYardas

print('El dinosaurio llamado ' + (nombre) + ', Pesa ' + str(pesoEnKilos) + ' Kilos, y mide '+ str(longitudEnMetros)+ ' Metros')