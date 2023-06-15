import entidades.dictionary as dic
import re
import servicios.serializacion as s 
import servicios.MapaServicio as ms

dicuF = None  # Variable global para almacenar la estructura dicP

def load_fix_element(nombre,direccion):
    global dicuF
    mapa = s.buscarMapa()
    #ms.printMap(mapa)
    dir = direccion
    direccion = existeDir(mapa,direccion)
    if direccion != False:

        if dicuF is None:
            dicuF = [None]*7 

        if searchUbiFija(dicuF,nombre) != False:
            print(nombre, "ya existe en el mapa, intente nuevamente. ")
        else:
            #AGREGO AL DIC
            pos = calcularPos(nombre)
            dic.insertInPos(dicuF, pos, nombre, direccion)
    else:
        print("La dirección: ", dir, " no existe.")
    return dicuF


def searchUbiFija(dic,nombre): #dado el nombre de la ubicacion, busca la dirección (si es que existe)
    pos = calcularPos(nombre)
    if dic[pos] == None:
        return False
    else: #busco key
        current = dic[pos].head
        while current != None:
            if current.key == nombre:
                break
            current = current.nextNode
        if current == None:
            return False
        else:
            return current.value #devuelve la dirección

def calcularPos(nombre):
    letra = nombre[0]
    if letra == "A":
        pos = 0
    elif letra == "E":
        pos = 1
    elif letra == "H":
        pos = 2
    elif letra == "I":
        pos = 3
    elif letra == "K":
        pos = 4
    elif letra == "S":
        pos = 5
    elif letra == "T":
        pos = 6
    return pos

def existeDir(mapa,dir):

    patron = r"<(\w+),\s*([-+]?\d*\.\d+|\d+)>"
    rdo = re.findall(patron, dir)

    ex = rdo[0][0]
    dx = float(rdo[0][1])
    ey = rdo[1][0]
    dy = float(rdo[1][1])

    esq = [ex,ey]
    key = esq[0]
    key = int(key[1:])
    slot = ms.encontrarSlot(mapa, key)

    key1 = esq[1]
    key1 = int(key1[1:])
    slot1 = ms.encontrarSlot(mapa, key1)

    if slot != None and slot1 != None:
        if mapa.head[slot] == None:
            c = False
        else:
            current = mapa.head[slot].head 
            while current != None:
                if current.value[0] == int((esq[1])[1:]):
                    c = float(current.value[1])
                    break
                current = current.nextNode
            if current == None:
                c = False
        
        if mapa.head[slot1] == None:
            c = False
        else:
            current = mapa.head[slot1].head 
            while current != None:
                if current.value[0] == int((esq[0])[1:]):
                    c1 = float(current.value[1])
                    break
                current = current.nextNode
            if current == None:
                c1 = False

        if c != False:
            if c == dx+dy: #verifico que el largo de las esquinas sean correctas
                crear = True
            else:
                crear = False
            direccion = [ex,dx,ey,dy]
        elif c1 != False:
            if c1 == dx+dy: #verifico que el largo de las esquinas sean correctas
                crear = True
            else:
                crear = False
            direccion = [ey,dy,ex,dx]
        else:
            crear = False
            
        if crear == True:      
            return direccion
        else:
            return crear   #FALSE
    else:
        return False