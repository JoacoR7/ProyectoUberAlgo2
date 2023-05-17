import entidades.UbicacionFija as uf
import servicios.DireccionServicio as ds

def crearUbicacion():
    u = uf.UbicacionFija()
    print("Ingrese el nombre del lugar: ")
    nombre = input()
    u.setNombre(nombre) 
    direccion = ds.crearDireccion()
    u.setDireccion(direccion)
    return u







"""print("A continuación deberá especificar entre qué esquinas se encuentra el lugar")
    print("Ingrese la primer esquina:")
    esquina1 = input()
    print("Ingrese la segunda esquina:")
    esquina2 = input()
    print("¡Muchas gracias! Ahora ingrese a qué distancia se encuentra el lugar con respecto a cada esquina")
    print("Ingrese la distancia a la que se encuentra", nombre, " de la esquina 1")
    distancia1 = input()
    print("Ingrese la distancia a la que se encuentra", nombre, " de la esquina 2")
    distancia2 = input()"""



