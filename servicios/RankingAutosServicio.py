import servicios.MapaServicio as ms
import servicios.UbicacionMovilServicio as um
import entidades.linkedlist as l
import entidades.myqueue as q
def ranking(persona,dicC,dicP,dist):
    dirPersona = um.searchUbiMovil(dicP,persona) #verificar?
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
        verificarMonto(ranking,montoP)
    else: 
        print("La persona no existe, intente nuevamente.")

def verificarMonto(autos,monto):
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
        print("Ranking de los autos que puede pagar:")
        if current != None:
            while current!=None:
                print(current.value[0])
                current = current.nextNode
        else:
            print("No está en condiciones de pagar ningún auto")
            return
    if current != None:
        uber = ranking.head.value[0]
        costo = ranking.head.value[1]
        panelInteractivo(uber, monto, costo)


def panelInteractivo(uber,monto,costo):
        print("¿Desea aceptar el viaje?")
        print("No: Opción 1")
        print("Sí: Opción 2")
        print("Introduzca su opción:")
        fin = False
        while fin != True:
                try:
                    opcion = int(input())
                    if opcion == 1:
                        print("Nos vemos pronto!")
                        fin == True
                    elif opcion == 2:
                        print("El auto que realizara el recorrido es el ", uber)
                        nuevoMonto = monto - costo
                        fin == True
                        #cambiar direcciones y todo eso
                    else: 
                        print("La opción ingresada no es válida, intente nuevamente.")
                except ValueError:
                    print("Error: El valor ingresado no es válido, intente nuevamente.")







