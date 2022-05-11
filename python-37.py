#Menu de selección 

while(True):
    print('1 Opción 1')
    print('2 Opción 2')
    print('3 Opción 3')
    print('4 Opción 4')
    print('5 Salir')

    opc = int(input('Seleccione la opción: '))

    if (opc == 1):
        print('Seleccionó la opción 1')
    elif(opc == 2):
        print('Seleccionó la opción 2')
    elif(opc == 3):
        print('Seleccionó la opción 3')
    elif(opc == 4):
        print('Seleccionó la opción 4')
    elif(opc == 5):
        print('Seleccionó la opción Salir')
        break

    else:
        print('ERROR')    

