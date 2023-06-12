import servicios.UbicacionFijaServicio as uf
import entidades.dictionary as dic
import servicios.serializacion as s
import servicios.MapaServicio as ms

dicC = None
dicP = None  # Variable global para almacenar la estructura dicP

def load_movil_element(nombre, direccion, monto):

    mapa = s.buscarMapa()
    dir = direccion
    direccion = uf.existeDir(mapa,direccion)
    if direccion != False:

        global dicP  # Declaro que estoy utilizando la variable global dicP
        global dicC

        if dicP is None:
            dicP = [None] * 13  # Creo la estructura dicP solo la primera vez
        
        if dicC is None:
            dicC = [None] * 13  # Creo la estructura dicC solo la primera vez

        if nombre[0] == "C": 
            dic = dicC
        else: 
            dic = dicP
        if searchUbiMovil(dic,nombre,13) != None: #verifico que el nombre no exista
            print(nombre, "ya existe en el mapa, intente nuevamente. ")
        else:
            while True:
                try:
                    monto = float(monto)
                    if monto <= 0:
                        print("El monto debe ser un número mayor a cero, intente nuevamente.")
                        return
                    else:
                        break
                except ValueError:
                    print("Error: El valor ingresado no es válido.")
                    return

            #agrego al dic
            if nombre[0] == "C": 
                addDicC(dicC,13,nombre,monto,direccion)
            else: 
                addDicP(dicP,13,nombre,monto,direccion)
    else:
        print("La dirección: ", dir, " no existe.")

def addDicC(dicC,m,nombre,monto,dir):
        k = int(nombre[1:])
        k = (k % m)-1
        value = [dir, monto]                               
        dic.insertUbiMovil(m,dicC,k,nombre,value)


def addDicP(dicP,m,nombre,monto,dir):
        k = int(nombre[1:])
        k = (k % m)-1
        value = [dir, monto]                               
        dic.insertUbiMovil(m,dicP,k,nombre,value)

#Para verificar si esa ubicacion ya existe (ej: si quieren agregar un C1 pero este ya está agregado)
def searchUbiMovil(dic,nombre,m):
    k = int(nombre[1:]) % m #slot
    if dic[k] == None:
        return None
    else: #busco key
        current = dic[k].head
        while current != None:
            if current.key == nombre:
                break
            current = current.nextNode
        if current == None:
            return None
        else:
            return current.value[0] #devuelvo direccion y monto
        
