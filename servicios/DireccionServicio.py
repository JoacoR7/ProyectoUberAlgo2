import servicios.UbicacionFijaServicio as uf
import entidades.linkedlist as l
def crearDireccion(v,mapa):
    print("Ingrese la esquina 1: ")
    ex = input()

    print("Ingrese la distancia a la esquina 1: ")
    dx = input()

    print("Ingrese la esquina 2: ")
    ey = input()


    print("Ingrese la distancia a la esquina 2: ")
    dy = input()

    esq = [ex,ey]


    c = existeDir(v,mapa,esq)  #si existe la direccion(calle) me devuelve el largo de la calle (c) y sino False

    if c != False:  
        if c == (int(dx)+int(dy)): #verifico que el largo de las esquinas sean correctas
            crear = True
        else:
            crear = False
    else:
        crear = False
    
    if crear == True:      
        return [ex,dx,ey,dy]
    else:
        return crear   #FALSE

def existeDir(v,mapa,esq):
    key = esq[0]
    key = int(key[1:])
    slot = (key % v)-1

    if mapa.head[slot] == None:
        return False
    else:
        current = mapa.head[slot].head 
        while current != None:
            if current.value[0] == int((esq[1])[1]):
                return current.value[1]
                break
            current = current.nextNode
        if current == None:
            return False

