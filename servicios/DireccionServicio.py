import entidades.Direccion as dir

def crearDireccion():
    d = dir.Direccion()
    print("Ingrese la esquina 1: ")
    ex = input()

    print("Ingrese la distancia a la esquina 1: ")
    dx = input()

    print("Ingrese la esquina 2: ")
    ey = input()

    print("Ingrese la distancia a la esquina 2: ")
    dy = input()

    esq = (ex,dx,ey,dy)


    c = existeDir(esq)  #si existe la direccion(calle) me devuelve el largo de la calle (c) y sino False

    if c != False:  
        if c == (dx+dy): #verifico que el largo de las esquinas sean correctas
            crear = True
        else:
            crear = False
    else:
        crear = False
    
    if crear == True:      
        return esq
    else:
        return crear   #FALSE


