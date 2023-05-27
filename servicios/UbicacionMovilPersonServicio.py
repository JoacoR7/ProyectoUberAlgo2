import servicios.DireccionServicio as ds
import entidades.dictionary as dic
import servicios.UbicacionMovilCarServicio as uf

def crearUbiMovilP(dicP,cantidadV,mapa):

    print("Ingrese el nombre de la ubicación Movil: ")    ## Esto hay que hacerlo afuera (en un menu por ejemplo)
    nombre = input()

    if uf.existeUbicacion(dicP,nombre,13) != None:
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
    value = [dir, monto]                               
    dic.insertUbiMovil(m,dicP,k,nombre,value)

    dic.printDic(dicP)