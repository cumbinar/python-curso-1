'''algoritmo tal que dado como dato el lado de un cubo, calcula el área de la base,
el área lateral(4 caras de los lados), el área total (todas las caras) y el volumen
(lado*lado*lado).'''

print('algoritmo tal que dado como dato el lado de un cubo,\n calcula el área de la base, el área lateral(4 caras de los lados), \n el área total(todas las caras) y el volumen(lado*lado*lado).')
nombre = input('Ingresa tu nombre y oprime enter ')

lado = int(input(nombre+ ' Ingresa el lado del cubo: '))
area_base = lado * lado
area_cuatro_lados = area_base * 4
area_seis_lados = area_base * 6
volumen = lado**3
print('El área de la base de un cubo de lado '+ str(lado) + ' es: '+ str(area_base))
print('El área de 4 caras del cubo de lado '+ str(lado) + ' es: '+ str(area_cuatro_lados))
print('El área de las 6 caras de un  cubo de lado '+ str(lado) + ' es: '+ str(area_seis_lados))
print('El volumen de un  cubo de lado '+ str(lado) + ' es: '+ str(volumen))