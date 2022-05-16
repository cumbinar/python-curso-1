
#Recursividad: una función se llama a si misma

'''En este ejemplo, tri_recursion() es una función que hemos definido para llamarse a sí misma ("recursión"). Usamos la variable k como los datos, que decrementa ( -1 ) cada vez que recursamos. La recursión termina cuando la condición no es mayor que 0 (es decir, cuando es 0).'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print("este es el valor de k: "+ str(k))
    print(result)
  else:
    result = 0
  return result


print("\n\nRecursion Example Results")
tri_recursion(4)
