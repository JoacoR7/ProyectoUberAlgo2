import entidades.UbicacionFija as uf
import servicios.CargarDireccionServicio as ds
import entidades.dictionary as dic
import servicios.UbicacionMovilServicio as um

dicuF = None  # Variable global para almacenar la estructura dicP

def load_fix_element(nombre,direccion):
    
    global dicuF
    if dicuF is None:
        dicuF = [None]*7 
    dic.printDic(dicuF)
    while searchUbiFija(dicuF,nombre) != False:
        print(nombre, "ya existe en el mapa, intente nuevamente: ")
        nombre = input()
    
    #AGREGO AL DIC
    pos = calcularPos(nombre)
    dic.insertInPos(dicuF, pos, nombre, direccion)
    dic.printDic(dicuF)


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

