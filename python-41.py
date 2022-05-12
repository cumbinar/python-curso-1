#multiasignación, return y función dentro de otra función


def retornar_nombre_y_edad():
    nombre = 'Cumbi'
    edad = devolver_edad()
    return nombre, edad


def devolver_edad():
    return 21

def main():
    n, e = retornar_nombre_y_edad()
    print(str(n)+' tiene ' + str(e) + ' años')

main()