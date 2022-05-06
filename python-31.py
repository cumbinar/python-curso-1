#ciclos definidos encontrar cuántos cincos hay en un rango

cont = 0

for i in range(7, 56):
    if (i % 5 == 0 and i % 10 != 0 ):
        cont += 1
    if (i >= 50 and i <= 59):
        cont+=1

print('la cantidad de cincos encontrados es: '+ str(cont))            