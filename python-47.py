#determinar si un número es primo, método for n in range(2, num)

num = int(input('Ingrese un número: ' ))

def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print(str(num) + " No es primo", n, "es divisor")
            return False
    print(str(num) + " Es primo")
    return True
es_primo(num)