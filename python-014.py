#ingresar la edad y clasificarlo según unos criterios 

edad = int(input('Ingrese la edad del paciente:  '))

if (edad <=0):
    print('La edad debe ser mayor que cero')
else:
    if(edad <=5):
        print('El paciente es Bebé')
    else:
        if(edad <= 14):
            print('El paciente es Niño')
        else:
            if(edad <= 18):
                print('El paciente es Adolescente')
            else:
                if(edad <= 60):
                    print('El paciente es Adulto')
                else:
                    print('El paciente es Cucho')
        
