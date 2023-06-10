import uber
import entidades.dictionary as d
import servicios.serializacion as s
import servicios.MapaServicio as ms
import servicios.UbicacionFijaServicio as uf
import servicios.UbicacionMovilServicio as um
import entidades.graph as g

import servicios.CargarDireccionServicio as cd
#servicios.serializacion.serializarPersonas(["A", "B", "C"])
datos = s.extraerEsquinasYCalles()
aristas = ms.obtenerAristas(datos[1])
esquinas = ms.obtenerEsquinas(datos[0])
map, mapAux = ms.crearMapa(esquinas, aristas)
s.serializarMapa(map)
mapa = s.buscarMapa()
print("")
ms.printMap(map)
ms.printMap(mapAux)
#g.shortestPath(map, mapAux, 7, 4) 
print("")


#print(ms.existPath(map, 7, 4))



cd.cargarUbicacion(cantidadV,map)

#uber.menu()



ms.cálculosIniciales(map)

#TODO: arreglar inserción de grafo, aunque no salgan aristas de un vértice, colocar datos en el slot correspondiente (al menos la key)
#servicios.serializacion.serializarPersonas(["A", "B", "C"])

