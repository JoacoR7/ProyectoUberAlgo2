import servicios.UbicacionMovilServicio as um
import servicios.UbicacionFijaServicio as uf
import re

def cargarUbicacion(v,mapa):
    fin = False
    print("A continuación podrá cargar ubicaciones fijas y móviles")
    while fin == False:
        print("¿Qué tipo de ubicación desea cargar? (ingrese la opción correspondiente)\n",
        "1: Ubicación Móvil\n", 
        "2: Ubicación Fija\n", 
        "3: Ninguna")
        
        opcion = input()
        try:
            opcion = int(opcion)
        finally:
            opcion = opcion

        if opcion == 1:
            print('Nombre:')
            nombre = input()
            print('Dirección ("<ex,dx> <ey,dy>"):')
            direccion = input()
            direccion = existeDir(v,mapa,direccion) 
            if direccion != False:
                um.load_movil_element(nombre,direccion)
            else:
                print("La dirección ingresada no existe, intente nuevamente")
        elif opcion == 2:
            print("Nombre:")
            nombre = input()
            print('Dirección ("<ex,dx> <ey,dy>"):')
            direccion = input()
            direccion = existeDir(v,mapa,direccion) 
            if direccion != False:
                uf.load_fix_element(nombre,direccion)
            else:
                print("La dirección ingresada no existe, intente nuevamente")
        elif opcion == 3:
            fin == True
            print("¡Ubicaciones creadas!")
        else:
            print("Opción incorrecta, por favor intente de nuevo")



def existeDir(v,mapa,dir): #v=cant vertices     dir = {<ex, 10>, <ey, 5>} 
    #patron = r"<(\w+),\s*([-+]?\d*\.\d+|\d+)>"
    #rdo = re.findall(patron, dir)

    patron = r"<(\w+),\s*([-+]?\d*\.\d+|\d+)>"
    rdo = re.findall(patron, dir)

    ex = rdo[0][0]
    dx = float(rdo[0][1])
    ey = rdo[1][0]
    dy = float(rdo[1][1])

    print("ex:", ex)
    print("ey:", ey)
    print("dx:", dx)
    print("dy:", dy)

    esq = [ex,ey]
    key = esq[0]
    key = int(key[1:])
    slot = (key % v)-1
    if slot == -1:
        slot = 6
    if mapa.head[slot] == None:
        c = False
    else:
        current = mapa.head[slot].head 
        while current != None:
            if current.value[0] == int((esq[1])[1]):
                c = float(current.value[1])
                break
            current = current.nextNode
        if current == None:
            c = False

    if c != False:  
        if c == dx+dy: #verifico que el largo de las esquinas sean correctas
            crear = True
        else:
            crear = False
    else:
        crear = False
    
    if crear == True:      
        return [ex,dx,ey,dy]
    else:
        return crear   #FALSE




