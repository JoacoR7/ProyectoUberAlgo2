import uber
import servicios.serializacion
import servicios.MapaServicio as ms
import entidades.graph as g

#servicios.serializacion.serializarPersonas(["A", "B", "C"])
cantidadV, aristas = servicios.serializacion.extraerMatriz()
map = ms.createMap(cantidadV, aristas)
print(ms.existPath(map, 7, 4))

g.shortestPath(map, 7, 4)

#uber.menu()