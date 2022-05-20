#conjuntos- diccionarios -clave => valor

conjunto = set()

conjunto.add(78)

print(conjunto)  # imprime {78}

conjunto.add("Cumbi")

print(conjunto)  # imprime {'Cumbi', 78}

frutas = set()
frutas.add("Manzana")
print(frutas)
frutas.add('Pera')
frutas.add('Papaya')
print(frutas)  # imprime {'Manzana', 'Papaya', 'Pera'}

#conjunto con clave valor se conoce como diccionario

'''Un diccionario en Python es una colección de elementos, donde cada uno tiene una llave key y un valor value. Los diccionarios se pueden crear con paréntesis {} separando con una coma cada par key: value. En el siguiente ejemplo tenemos tres keys que son el nombre, la edad y el documento.'''

d1 = {
    "Nombre": "Sara",
    "Edad": 27,
    "Documento": 1003882
}
print(d1) #imprime {'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}


'''Otra forma equivalente de crear un diccionario en Python es usando dict() e introduciendo los pares key: value entre paréntesis.'''

d2 = dict([
    ('Nombre', 'Sara'),
    ('Edad', 27),
    ('Documento', 1003882),
])
print(d2) #Imprime {'Nombre': 'Sara', 'Edad': '27', 'Documento': '1003882'}


#También es posible usar el constructor dict() para crear un diccionario.

d3 = dict(Nombre='Sara',
          Edad=27,
          Documento=1003882)
print(d3) #Imprime {'Nombre': 'Sara', 'Edad': 27, 'Documento': 1003882}
