import pickle
import entidades.linkedlist
import entidades.algo1


#Busco el archivo el archivo serializado y devuelvo su contenido (si es que existe el archivo)
def buscarArchivo(nombre):
    try:
        fichero = open(nombre, "rb")
    except FileNotFoundError:
        return None
    contenido = pickle.load(fichero)
    fichero.close()
    return contenido

#Guardo el contenido en un archivo serializado
def serializarArchivo(contenido, nombre):
    try:
        fichero = open(nombre, "wb")
        pickle.dump(contenido, fichero)
    finally:
        fichero.close()



"""def borrarPersonas():
    if obtenerPersonas() != None:
        fichero = open("lista_personas")
        del(fichero)
    else:
        print("No se encontró el archivo")"""

#Busco un archivo de texto
def abrirArchivo(name):
    try:
        fichero = open(name)
        found = True
    except FileNotFoundError:
        found = False
        fichero = None
    finally:
        return found, fichero

#Extraigo los datos del archivo de texto
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

def extraerEsquinasYCalles(datos):
    if datos[-4:] != ".txt":
        datos = datos + ".txt"
    _, fichero = abrirArchivo(datos)
    if fichero != None:
        contenido =  fichero.readlines()
        fichero.close()
        return contenido
    
    return None



