import uber
import entidades.dictionary as d
import servicios.serializacion
import servicios.MapaServicio as ms
import servicios.UbicacionFijaServicio as uf
import servicios.UbicacionMovilServicio as um
import entidades.graph as g

import servicios.CargarDireccionServicio as cd
#servicios.serializacion.serializarPersonas(["A", "B", "C"])
cantidadV, aristas = servicios.serializacion.extraerMatriz()
map = ms.createMap(cantidadV, aristas)
g.shortestPath(map, 7, 4)
print("")


print(ms.existPath(map, 7, 4))



cd.cargarUbicacion(cantidadV,map)

#uber.menu()



ms.cálculosIniciales(map)

#TODO: arreglar inserción de grafo, aunque no salgan aristas de un vértice, colocar datos en el slot correspondiente (al menos la key)
