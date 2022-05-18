#crear un función para determinar si un número es mayor o si son iguales

def mayor(num1, num2):
    if  num1 < num2:
        print(str(num2)+ ' Es mayor que '+ str(num1))
    elif num2 < num1:
        print(str(num1) + ' Es mayor que ' + str(num2))
    else:
        print(str(num1)+ ' Es igual a '+ str(num2))    


num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

mayor(num1, num2)
