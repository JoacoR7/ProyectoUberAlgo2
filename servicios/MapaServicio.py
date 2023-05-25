import entidades.graph as g
import entidades.myqueue as q
import entidades.linkedlist as l
import entidades.mystack as s
import entidades.algo1 as a

"""
Dudas:
    1* los numeros de las esquinas PUEDEN SER CUALQUIER NUMERO
"""

def menuMapa():
    opcion = 0
    esquinas = None
    LA = []
    while opcion != 3:
        print(" 1: Cargar ubicación fija\n", 
            "2: Cargar ubicación móvil\n",
            "3: Salir")
        
        opcion = input()
        try:
            opcion = int(opcion)
        except ValueError:
            pass
        finally:
            opcion = opcion

        if opcion == 1:
            esquinas = cargarEsquina()
            print("¡Listo! Esquina cargada.")
        elif opcion == 2:
            if esquinas == None:
                print("Primero debe cargar las esquinas")
            else:
                calles = cargarCalle(esquinas,LA)
                print("¡Listo! Calle cargada.")
        elif opcion == 3:
            graph_Matriz1(esquinas, LA) #creo el mapa
            print("Map created successfully.")
        else:
            print("Opción inválida, por favor intente de nuevo, recuerde ingresar un número del 1 al 3")


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


