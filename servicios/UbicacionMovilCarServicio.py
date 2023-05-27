import servicios.DireccionServicio as ds
import entidades.dictionary as dic

def crearUbiMovilC(dicC,cantidadV,mapa): #falta argumento nombre

    print("Ingrese el nombre de la ubicación Movil: ")    ## Esto hay que hacerlo afuera (en un menu por ejemplo)
    nombre = input()

    if existeUbicacion(dicC,nombre,13) != None:
        print(nombre, "ya existe en el mapa, intente nuevamente") #esto tmb

    dir = ds.crearDireccion(cantidadV,mapa)

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
    m = 13
    k = int(nombre[1:])
    k = k % m
    value = [dir, monto]                               ###ver
    dic.insertUbiMovil(m,dicC,k,nombre,value)
    dic.printDic(dicC)

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