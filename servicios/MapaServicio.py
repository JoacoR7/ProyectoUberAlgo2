import entidades.myqueue as q
import entidades.linkedlist as l
import entidades.mystack as s
import entidades.algo1 as a
import entidades.dictionary as d
import entidades.graph as g
import servicios.serializacion as se
import copy
import re

def printMap(map):
    n = len(map.head)
    for i in range (0,n):
        if map.head[i] != None:
            print('Posicion ', i)
            l.printListaX2(map.head[i])

def calculosIniciales(map, mapAux):
    slots = map.head
    long = len(slots)
    datos = [[None]*long, [None]*long]
    for i in range(0,long):
        if slots[i] != None:
            key = slots[i].head.key
            lista = l.LinkedList()
            datos[1][i] = lista
        else:
            key = None
        datos[0][i] = key
    for i in range(0, long):
        inicio = slots[i]
        if inicio != None:
            inicio = inicio.head.key
            ma = copy.deepcopy(mapAux)
            for j in range(0, long):
                if i != j:
                    fin = slots[j]
                    found = True
                    fin = fin.head.key
                    if found:
                        dato = [0]*2
                        dato[0] = fin
                        _, distancia = g.shortestPath(map, ma, inicio, fin)
                        if distancia == None:
                            continue
                        dato[1] = distancia
                        l.add(datos[1][i],dato)
    print("")
    return datos

def obtenerAristas(secuencia):

    # Encontrar el índice de apertura y cierre de llaves
    indice_inicio = secuencia.find("{")
    indice_fin = secuencia.find("}")
    
    # Extraer la secuencia dentro de las llaves
    secuencia_dentro_llaves = secuencia[indice_inicio + 1:indice_fin]
    
    # Utilizar una expresión regular para dividir la secuencia en elementos individuales
    elementos = re.findall(r"<([^<>]+)>", secuencia_dentro_llaves)
    
    # Crear una matriz de 3 columnas
    matriz = []
    
    for elemento in elementos:
        valores = elemento.split(",")
        nuevos_valores = []
        for valor in valores:
            valor = valor.strip()
            if valor.startswith("e"):
                numero = valor[1:]
                nuevos_valores.append(numero)
            else:
                nuevos_valores.append(valor)
        matriz.append(nuevos_valores)

    return matriz

def obtenerEsquinas(secuencia):
    # Encontrar el índice de apertura y cierre de llaves
    indice_inicio = secuencia.find("{")
    indice_fin = secuencia.find("}")

    # Extraer la secuencia dentro de las llaves
    secuencia_dentro_llaves = secuencia[indice_inicio + 1:indice_fin]

    # Dividir la secuencia en elementos individuales
    elementos = secuencia_dentro_llaves.split(",")

    # Crear un array para almacenar los elementos
    array= []

    for elemento in elementos:
        array.append(elemento.strip())

    array = filtrarEsquinas(array)
    
    return array

def filtrarEsquinas(array):
    # Crear una nueva lista para almacenar los elementos modificados
    esquinasFiltradas = []

    for elemento in array:
        if 'e' in elemento:
            numero = elemento[1:]
            esquinasFiltradas.append(numero)
        else:
            esquinasFiltradas.append(elemento)

    return esquinasFiltradas

def crearMapa(datos):
    mapa = se.buscarArchivo("mapa")
    if mapa != None:
        print("Ya hay un mapa existente, ¿desea sobreescribir el archivo?")
        print("1: Sí\n2: No")
        opcion = input()
        if int(opcion) == 2:
            return
    datos = se.extraerEsquinasYCalles(datos)
    A = obtenerAristas(datos[1])
    V = obtenerEsquinas(datos[0])
    #length: cantidad de vértices
    length = len(V)
    dic = [None]*length
    hash = d.dictionary()
    hash.head = dic
    insertarEsquinas(hash, V, length)
    mapAux = copy.deepcopy(hash)
    insertarCalles(hash, A, length)
    se.serializarArchivo(hash, "mapa")
    se.serializarArchivo(mapAux, "mapaAux")
    datos = calculosIniciales(hash, mapAux)
    se.serializarArchivo(datos, "calculosIniciales")
    print("Mapa creado exitosamente")

def insertarEsquinas(map, V, length):
    for i in range(len(V)):
        esquina = V[i]
        esquina = int(esquina)
        slot = (esquina % length) - 1
        inserted = False
        node = d.dictionaryNode()
        node.key = esquina
        aristaAux = [None]*2
        node.value = aristaAux
        #Insertaremos las esquinas, realizamos linear probing para evitar colisiones
        while not inserted:
            if map.head[slot] == None:
                lista = l.LinkedList()
                lista.head = node
                map.head[slot] = lista 
                inserted = True
            else:
                slot += 1
                if slot == length:
                    slot = 0

def insertarCalles(map, A, length):
    for elemento in A:
        esquinaInicial = int(elemento[0])
        esquinaFinal = int(elemento [1])
        distancia = int(elemento[2])
        slot = encontrarSlot(map, esquinaInicial)
        inserted = False
        node = map.head[slot].head
        while not inserted:
            arista = node.value
            if arista[0] == None and arista[1] == None:
                arista[0] = esquinaFinal
                arista[1] = distancia
                inserted = True
            else:
                while True:
                    nodeAux = copy.deepcopy(node)
                    if node.nextNode == None:
                        node.nextNode = nodeAux
                        break
                    else:
                        node = node.nextNode
                node.nextNode.value[0] = esquinaFinal
                node.nextNode.value[1] = distancia
                inserted = True

def encontrarSlot(map, key):
    found  = False
    length = len(map.head)
    slot = (key % length) - 1
    cont = 0
    if slot == length:
        slot = 0
    elif slot == -1:
        slot = length-1
    while not found and cont < length:
        if map.head[slot].head.key != key:
            slot += 1
            cont += 1
            if slot == length:
                slot = 0
        else:
            found = True
    if found == False:
        return None
    else:
        return slot


                






def graph_Matriz1(LV, LA): 
    #los dos primeros componentes de las aristas me dice los vertices que se unen y el tercer componente el costo de la misma
    #ejemplo: #LA = [(0,1,1),(0,2,2),(1,3,3),(1,2,4),(0,3,4)]
    matriz = a.Array(len(LV),a.Array(len(LV),0))
    long = len(LA)
    for f in range(0,long):
        i = LA[f][0]
        j = LA[f][1]
        value = LA[f][2]
        matriz[i][j] = value   

    for i in range(0,len(LV)):
        for j in range(0,len(LV)):  
            if matriz[i][j] == None:
                matriz[i][j] = 0         
    return matriz


def cargarCalle(esquinas,LA):
    correcto = False
    print("A continuación cargará los datos de la calle: esquina 1, esquina 2 y su respectiva distancia")

    while correcto == False:
        e1 = input("Ingrese el nombre de la esquina 1:")
        if validarEsquina(e1) == True:
            if len(e1) == 2:
                pos1 = int(e1[1])
            else:
                pos1 = int(e1[1]+e1[2])
            if len(esquinas[pos1]) == 0:
                print("La esquina ingresada no existe, intente nuevamente")   #mostrar esquinas?
            else:
                correcto = True
    correcto = False 

    while correcto == False:
        e2 = input("Ingrese el nombre de la esquina 2:")
        if validarEsquina(e2) == True and existeEsquina(e2) == True:
            if len(e2) == 2:
                pos2 = int(e2[1])
            else:
                pos2 = int(e2[1]+e2[2])
            if len(esquinas[pos2]) == 0:
                print("La esquina ingresada no existe, intente nuevamente")   #mostrar esquinas?
            else:
                if e1 != e2: # verifico que no ingrese dos veces la misma esquina
                    correcto = True 
                else:
                    print("Las esquinas ingresadas son iguales, ingrese otra distinta a ", e1)

    c = input("Por último, ingrese la distancia entre las esquinas ingresadas:")

    while not c.isdigit(): # verifico que sea un numero
        print("El valor ingresado no es correcto. Recuerde que una distancia debe ser un numero mayor a cero")
        c = input("Ingrese nuevamente la distancia entre las esquinas ingresadas:")

    if c <= 0: # verifico que sea mayor a cero
        print("El valor ingresado no es correcto. Recuerde que una distancia debe ser un numero mayor a cero")
        while c <= 0:
            c = input("Ingrese nuevamente la distancia entre las esquinas ingresadas:")

    # verifco si la calle que quiero agregar "ex,ey" no existe ya en mano contraria ("ey,ex"), y en caso de que ya exista, 
    # los c deben ser =

    #LV = Array de esquinas
    LA.append(e1,e2,c)

def validarEsquina(esquina,esquinas):  #valido la "sintaxis" ingresada

    if (len(esquina) > 3) or len(esquina) == 0 or esquina[0] != "e" or esquina[1].isalpha == True: 
        print("La esquina ingresada no es válida. Recuerde que tiene la forma 'ex', siendo x un número como máximo 99")
        return False
    else:
        if len(esquina) == 3 and esquina[2].isalpha:
            return False
        else:
            return True

def existeEsquina(esquina,esquinas): 
    if len(esquina) == 2:
        pos = int(esquina[1])
        if len(esquinas[pos]) == 0:                                             #####ERROR 
            return False
        else:
            return True
    elif len(esquina) == 3:
        pos = int(esquina[1])+int(esquina[2])
        if len(esquinas[pos]) == 0:
            return False
        else:
            return True
        
def cargarEsquina():
    esquinas = []
    correcto = False
    while correcto == False:
        esquina = input("Ingrese el nombre de la esquina: ")
        if correcto != validarEsquina(esquina,esquinas): #valido la sintaxis del nombre (ex) 
            if existeEsquina(esquina,esquinas)==True: #verifico si la esquina ya existe
                correcto = True
            else:
                if len(esquina) == 2:
                    pos = int(esquina[1])
                    esquinas.insert(pos,esquina)
                else:
                    pos = int(esquina[1]+esquina[2])
                    esquinas.insert(esquina[1],esquina)
                correcto = True
    return esquinas