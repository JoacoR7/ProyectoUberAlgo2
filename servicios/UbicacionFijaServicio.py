import entidades.UbicacionFija as uf
import servicios.DireccionServicio as ds
import entidades.dictionary as dic

#dic = [None]*7

def crearUbiFija():
    print("Ingrese el nombre de la ubicación fija: ")
    nombre = input()
    dir = ds.crearDireccion()
    
    if dir != False:
        pos = calcularPos(nombre)
        dic.insertInPos(dic, pos, nombre, dir)
    else:
        print("Dirección inválida")                   ###ver

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


#search que dada una direccion, devolver si se encuentra algo ahí??

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
