import uber
import servicios.serializacion
import servicios.MapaServicio as ms
import entidades.graph as g

cantidadV, aristas = servicios.serializacion.extraerMatriz()
map = ms.createMap(cantidadV, aristas)
print(ms.existPath(map, 7, 4))

g.shortestPath(map, 7, 4)
print("")

ms.cálculosIniciales(map)

#TODO: arreglar inserción de grafo, aunque no salgan aristas de un vértice, colocar datos en el slot correspondiente (al menos la key)