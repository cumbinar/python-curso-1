#encontrar la hipotenusa a partir de dos lados


a = int(input())
b = int(input())

total = a**2 + b**2

import math
h = math.sqrt(total)

print(h)