# organizar información listas diccionarios

listanombres = ['juan', 'cumbi', 'suzo']
listaapellidos = ['guevara', 'melo', 'tara']

contactos = [ listanombres, listaapellidos] # lista de listas

print  (contactos[0] [2] + ' '+contactos[1][1])


registro = 'Eduardo;Guevara;Melo;19408240;62'

lista = registro.split(';')
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

contacto1 = 'Cumbi;Guevara;Melo'
contacto2 = 'Pedro;Pinto;Pico'
contacto3 = 'Juan;Rico;Tara'

listaregistro = [contacto1, contacto2, contacto3]
print(listaregistro[0].split(';'))
print(listaregistro[1].split(';'))
print(listaregistro[0].split(';'))
