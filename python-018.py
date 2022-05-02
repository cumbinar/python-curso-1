'''Diseñar el algoritmo correspondiente a un programa que exprese en horas, minutos y
segundos un tiempo expresado en segundos.'''

segs = int(input('Ingrese el dato en segundos: '))
h = segs // 3600

resto = segs -(h * 3600)

m = resto // 60

s = resto - (m * 60)


print(str("{:0>2d}".format(h)) + ":"+str("{:0>2d}".format(m)) + ":" + str("{:0>2d})".format(s)))
print(str(h)+ ':'+str(m)+':'+str(s))
