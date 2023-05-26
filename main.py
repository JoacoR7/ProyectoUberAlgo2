import uber
import servicios.serializacion
import servicios.MapaServicio as ms
import servicios.UbicacionFijaServicio as uf

#servicios.serializacion.serializarPersonas(["A", "B", "C"])
cantidadV, aristas = servicios.serializacion.extraerMatriz()
map = ms.createMap(cantidadV, aristas)
print(ms.existPath(map, 7, 4))
uf.crearUbiFija(cantidadV,map)
uf.crearUbiFija(cantidadV,map)
#uber.menu()