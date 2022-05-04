'''Suponga que se desea obtener la suma de los gastos que se hicieron en un viaje, pero no sabemos exactamente cuántos fueron. Elabore un programa que permita ingresar en forma repetitiva cada uno de los gastos del viaje. Para identificar que no hay más entradas de datos, se debe ingresar un valor negativo, es decir, que si se ingresa un valor negativo entonces debe finalizar el programa, mostrando el total de los gastos del viaje.'''

acum = 0
negativo = True

while(negativo):
     gasto = int(input('Cuánto gastó?:  '))
     if (gasto<0):
         negativo = False
     else:
         acum = acum + gasto  

print('Los gastos son:  ' + str(acum)+ ' Pesos')