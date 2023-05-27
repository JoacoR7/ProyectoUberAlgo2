import uber
import servicios.serializacion
import servicios.MapaServicio as ms
import servicios.UbicacionFijaServicio as uf
import servicios.UbicacionMovilCarServicio as um

#servicios.serializacion.serializarPersonas(["A", "B", "C"])
cantidadV, aristas = servicios.serializacion.extraerMatriz()
map = ms.createMap(cantidadV, aristas)
print(ms.existPath(map, 7, 4))


dicC = [None]*13
dicF = [None]*7
um.crearUbiMovilC(dicC,cantidadV,map)
uf.crearUbiFija(dicF,cantidadV,map)

#uber.menu()

