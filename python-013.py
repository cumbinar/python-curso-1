# Entrar tres calificaciones, sacar promedio y mostrar respuesta según el caso

nota1 = float(input('Ingrese la primera nota:  '))
nota2 = float(input('Ingrese la segunda nota:  '))
nota3 = float(input('Ingrese la tercera nota:  '))

promedio = (nota1 + nota2 + nota3)/3

if (promedio >= 3.0):
    print('Pasó la asignatura')
else:
    if (promedio >= 2):
        print('Puedes habilitar')
    else:
        print('Pierde la asignatura')

