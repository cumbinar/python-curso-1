#encontrar cuántas letras a, hay en un texto

texto = input('Ingrese el texto a analizar: ')
cont=0
for i in texto:
    if (i == 'a' or i == 'á' or i == 'Á' or i == 'á'):
        cont+=1

print("la cantidad de letras a, en el texto es: " + str(cont))        