#if and 

edad = int(input('Ingrese la edad del paciente:  '))

if (edad < 0):
    print('La edad debe ser mayor que cero')
    print('Ejecute el programa nuevamente')
if(edad > 0 and edad <= 5):
    print('El paciente es Bebé')
if(edad > 5 and edad <= 14):
    print('El paciente es Niño')
if(edad > 14 and edad <= 18):
    print('El paciente es Adolescente')
if(edad > 18 and edad <= 60):
    print('El paciente es Adulto')
if(edad > 60):
    print('El paciente es Cucho')
