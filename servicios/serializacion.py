import pickle
import entidades.linkedlist
import entidades.algo1

def serializarPersonas(P):
    try:
        fichero = open("lista_personas", "wb")
        pickle.dump(P, fichero)
    finally:
        fichero.close()

def buscarPersonas():
    try:
        fichero = open("lista_personas")
        found = True
    except FileNotFoundError:
        found = False
    finally:
        if found == True:
            fichero.close()
        return found

def borrarPersonas():
    if buscarPersonas():
        fichero = open("lista_personas")
        del(fichero)
    else:
        print("No se encontró el archivo")

def serializarAutos(A):
    try:
        fichero = open("lista_autos", "wb")
        pickle.dump(A, fichero)
    finally:
        fichero.close()

def buscarAutos():
    try:
        fichero = open("lista_autos")
        found = True
    except FileNotFoundError:
        found = False
    finally:
        if found == True:
            fichero.close()
        return found

def borrarAutos():
    if buscarAutos():
        fichero = open("lista_autos")
        del(fichero)
    else:
        print("No se encontró el archivo")

def serializarMapa(M):
    try:
        fichero = open("mapa", "wb")
        pickle.dump(M, fichero)
    finally:
        fichero.close()

def buscarMapa():
    try:
        fichero = open("mapa")
        found = True
    except FileNotFoundError:
        found = False
    finally:
        if found == True:
            fichero.close()
        return found

def borrarMapa():
    if buscarMapa():
        fichero = open("mapa")
        del(fichero)
    else:
        print("No se encontró el archivo")

def serializarUbiFija(U):
    try:
        fichero = open("ubicaciones_fijas", "wb")
        pickle.dump(U, fichero)
    finally:
        fichero.close()

def buscarUbiFija():
    try:
        fichero = open("ubicaciones_fijas")
        found = True
    except FileNotFoundError:
        found = False
    finally:
        if found == True:
            fichero.close()
        return found

def borrarUbiFija():
    if buscarUbiFija():
        fichero = open("ubicaciones_fijas")
        del(fichero)
    else:
        print("No se encontró el archivo")

def buscarArchivo(name):
    try:
        fichero = open(name + ".txt")
        found = True
    except FileNotFoundError:
        found = False
        fichero = None
    finally:
        return found, fichero

def extraerDatos():
    _, fichero = buscarArchivo("datos")
    if fichero != None:
        lista =  fichero.readlines()
        fichero.close()
        return lista
    
    return None

def extraerMatriz():
    _, matriz = buscarArchivo("matriz")
    if matriz != None:
        filas = matriz.readlines()
        listaAristas = entidades.linkedlist.LinkedList()
        for i, fila in enumerate(filas):
            x = fila.split(", ", len(filas))
            del x[len(filas)]
            extraerAristas(i+1, x, listaAristas)
    return len(filas), listaAristas

            

def extraerAristas(fila, secuencia, listaAristas):
    columna = 1
    for peso in secuencia:
        try:
            peso = int(peso)
        except ValueError:
            print("Secuencia incorrecta")
            return
        if peso != 0:
            arista = entidades.algo1.Array(3)
            arista[0] = fila
            arista[1] = columna
            arista[2] = peso
            entidades.linkedlist.add(listaAristas, arista)
        columna += 1

def extraerEsquinasYCalles():
    _, fichero = buscarArchivo("datos2")
    if fichero != None:
        lista =  fichero.readlines()
        fichero.close()
        return lista
    
    return None



