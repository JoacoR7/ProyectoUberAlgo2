import servicios.DireccionServicio as ds
import entidades.dictionary as dic

#como le paso cantidadV y map
#donde crear dicC y dicP

#falta: dicC,cantidadV,mapa

def load_movil_element(nombre,direccion): 

    while existeUbicacion(dicC,nombre,13) != None:
        print(nombre, "ya existe en el mapa, intente nuevamente: ")
        nombre = input()

    dir = ds.crearDireccion(cantidadV,mapa)   #       ---> consulta

    if dir == False:
        while dir == False:
            print("La ubicación ingresada es inválida, intente nuevamente")
            dir = ds.crearDireccion(cantidadV,mapa)
    
    while True:
        try:
            monto = float(input("Ingrese el monto: "))
            if monto <= 0:
                print("El monto debe ser un número mayor a cero, intente nuevamente.")
            else:
                break
        except ValueError:
            print("Error: El valor ingresado no es válido. Intente nuevamente.")

    #agrego al dic
    if nombre[0] == "C": addDicC(dicC,13)
    else: addDicP(dicP,13)

    def addDicC(dicC,m):
        k = int(nombre[1:])
        k = k % m
        value = [dir, monto]                               
        dic.insertUbiMovil(m,dicC,k,nombre,value)
        #dic.printDic(dicC)


    def addDicP(dicP,m):
        k = int(nombre[1:])
        value = [dir, monto]                               
        dic.insertUbiMovil(m,dicP,k,nombre,value)
        #dic.printDic(dicP)


#Para verificar si esa ubicacion ya existe (ej: si quieren agregar un C1 pero este ya está agregado)
def existeUbicacion(dic,nombre,m):
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
            return current.value