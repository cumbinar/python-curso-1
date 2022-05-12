#multiasignación y return


def retornar_nombre_y_edad():
    nombre = 'Cumbi'
    edad = 50
    return nombre, edad

n, e = retornar_nombre_y_edad()

print(n+' tiene '+ str(e)+ ' años')

