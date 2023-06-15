import servicios.MapaServicio as ms
import servicios.UbicacionMovilServicio as um
import servicios.UbicacionFijaServicio as uf
import servicios.serializacion as s
import entidades.linkedlist as l
import entidades.myqueue as q
import entidades.graph as g

def createTrip(P, ubicacion):
    if ubicacion[0] == "<":
        elementos = ubicacion.split(" ")
        direccion = []
        for elemento in elementos:
            elemento = elemento.strip("<>").split(",")
            direccion.append(elemento[0])
            try:
                direccion.append(int(elemento[1]))
            except:
                print("Direccion incorrecta, intente de nuevo")
    else:
        direccion = uf.searchUbiFija(ubicacion)
    if len(direccion) != 4:
        print("Ingrese una dirección válida")
        return
    ranking(P, direccion)
    

def ranking(persona,destino):
    dist = s.buscarArchivo("calculosIniciales")
    dicC = s.buscarArchivo("lista_autos")
    dicP = s.buscarArchivo("lista_personas")
    dirPersona = um.searchUbiMovil(dicP,persona, 13) #verificar
    if dirPersona != None:
        dirP = dirPersona[0]   #dir = [ex,dx,ey,dy]
        montoP = dirPersona[1]
        ranking = l.LinkedList()
        long = len(dist[1])
        llegada = int(dirP[2][1:])  #esquina "ey" de la persona (ultima)
        for i in range(0,len(dicC)): #para recorrer el hash de los autos
                if dicC[i] != None: #si en el slot i no esta vacia la lista
                    dirC = int(dicC[i].head.value[0][2][1:]) #esquina "ey" del auto (ultima)
                    if llegada == dirC:
                        dirC = int(dicC[i].head.value[0][0][1:])
                    monto = dicC[i].head.value[1]
                    slot = (dirC%long)-1
                    current = dist[1][slot].head 
                    long2 = l.length(dist[1][slot])
                    for j in range(0,long2): #busco en la lista del slot de donde sale el auto la distancia a la persona
                        if current.value[0] == llegada:
                            nombre = dicC[i].head.key
                            element = [nombre,current.value[1],monto] #esquina del auto y monto del auto
                            q.enqueue_priority(ranking,element,current.value[1]) #value[1] = distancia
                            break
                        else:
                            current = current.nextNode
        #l.printLista(ranking)
        viaje, lista = verificarMonto(ranking,montoP,dicC)
        if viaje == True:
            uber = lista.head.value[0]
            costo = lista.head.value[1]
            montoFinal = montoP - costo
#MUESTRO EL CAMINO MÁS CORTO Y LA DISTANCIA DE LA PERSONA A SU DESTINO ACÁ
            panelInteractivo(uber, montoFinal, dicP, dicC, destino, persona, lista, montoP)
    else: 
        print("La persona no existe, intente nuevamente.")

def verificarMonto(autos,monto,dicC):
    current = autos.head
    ranking = l.LinkedList() #guardo el ranking de los autos que la persona puede pagar de menor a mayor
    while current != None:
        costo = (current.value[1] + current.value[2])/4
        if monto > costo:
            value = [current.value[0],costo]
            q.enqueue(ranking,value)
            current = current.nextNode
        else:
            current = current.nextNode
    #l.printLista(ranking)
    current = ranking.head
    if l.length(ranking) >= 3:
        print("Ranking de los 3 autos más cercanos que puede pagar:")
        print(current.value[0],current.nextNode.value[0],current.nextNode.nextNode.value[0])
    else:
        print("Ranking de los autos disponibles que puede pagar:")
        if current != None:
            cont = 1
            while current!=None:
                direccionUber = um.searchUbiMovil(dicC,current.value[0],13)
                montoUber = direccionUber[1]
                direccionUber = direccionUber[0]
                direccionUber = "<" + direccionUber[0] + "," + str(direccionUber[1]) + ">, <" + direccionUber[2] + "," + str(direccionUber[3]) + ">"
                print(str(cont) + " - Auto " + current.value[0] + ": \n       Dirección: " + direccionUber + "\n       Monto: " + str(montoUber))
                current = current.nextNode
                cont += 1
            return True, ranking
        else:
            print("No está en condiciones de pagar ningún auto")
            return False, False


def panelInteractivo(uber, monto, dicP, dicC, destino, persona, lista, montoP):
        print("¿Desea aceptar el viaje?")
        print("1: Sí")
        print("2: No")
        print("Introduzca su opción:")
        fin = False
        while fin != True:
            try:

                opcion = preguntarOpcion()
                if opcion == 2:
                    print("Nos vemos pronto!")
                    fin = True

                elif opcion == 1:
                    print("Elija el auto con el que quiere realizar el recorrido (Auto recomendado " + uber + ")")
                    opcion = preguntarOpcion()
                    if opcion<=l.length(lista):
                        if opcion == 2:
                            uber = lista.head.nextNode.value[0]
                            costo = lista.head.nextNode.value[1]
                            monto = montoP - costo
                        elif opcion == 3:
                            uber = lista.head.nextNode.nextNode.value[0]
                            costo = lista.head.nextNode.nextNode.value[1]
                            monto = montoP - costo
                        print("El auto que realizara el recorrido es el", uber)
                        cambiarDirecciones(uber,monto, dicP, dicC, destino,persona)
                        print("Viaje realizado con éxito!")
                        fin = True

                if not fin:
                    print("La opción ingresada no es válida, intente nuevamente.")
            except ValueError:
                print("Error: El valor ingresado no es válido, intente nuevamente.")

def preguntarOpcion():
    try:
        opcion = int(input())
    except:
        opcion = None
    return opcion

    

def direccionPersona(dic, destino, persona, monto):
    m=13
    k = int(persona[1:]) % m -1 #slot
    if dic[k] == None:
        return None
    else: #busco key
        current = dic[k].head
        while current != None:
            if current.key == persona:
                value = [destino,monto]
                break
            current = current.nextNode
        current.value = value 
    s.serializarArchivo(dic, "lista_personas")
def direccionAuto(dic, destino, uber):
    m=13
    k = int(uber[1:]) % m -1 #slot
    if dic[k] == None:
        return None
    else: #busco key
        current = dic[k].head
        while current != None:
            if current.key == uber:
                value = destino
                break
            current = current.nextNode
        current.value = value
    s.serializarArchivo(dic, "lista_autos")
def cambiarDirecciones(uber, monto, dicP, dicC, destino, persona):
    direccionPersona(dicP, destino, persona, monto)
    direccionAuto(dicC, destino, uber)
    return






