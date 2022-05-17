#determinar si un número es primo. Método función co recursividad

'''Es importante tener en cuenta que Python pone un cierto límite a las veces que una función puede ser llamada recursivamente. En algunos casos podrías encontrarte con un RecursionError, indicando que has superado el límite. Por ejemplo 1009'''

num = int(input('Ingrese un número: '))

def es_primo(num, n=2):
    if n >= num:
        print(str(num) + " Es Primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print(str(num) + " No es Primo,", n, "es divisor")
        return False


es_primo(num)  

