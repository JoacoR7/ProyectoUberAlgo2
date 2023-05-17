import entidades.Direccion as dir


def crearDireccion():
    d = dir.Direccion()
    print("Ingrese la esquina 1: ")
    ex = input()
    d.setEx(ex)
    print("Ingrese la distancia a la esquina 1: ")
    dx = input()
    d.setDx(dx)
    print("Ingrese la esquina 2: ")
    ey = input()
    d.setEy(ey)
    print("Ingrese la distancia a la esquina 2: ")
    dy = input()
    d.setDy(dy)
    return d
