#elif 

edad = int(input('Ingrese la edad del paciente:  '))

if (edad <= 0):
    print('La edad debe ser mayor que cero')
    print('Ejecute el programa nuevamente')
elif(edad <= 5):
    print('El paciente es Bebé')
elif(edad <= 14):
    print('El paciente es Niño')
elif(edad <= 18):
    print('El paciente es Adolescente')
elif(edad <= 60):
    print('El paciente es Adulto')
else:
    print('El paciente es Cucho')
