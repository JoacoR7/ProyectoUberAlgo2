import uber
import entidades.dictionary as d
import servicios.serializacion as s
import servicios.MapaServicio as ms
import servicios.UbicacionFijaServicio as uf
import servicios.UbicacionMovilServicio as um
import entidades.graph as g
import servicios.UbicacionFijaServicio as uf
#servicios.serializacion.serializarPersonas(["A", "B", "C"])
from entidades.borrar import *




map, mapAux = ms.crearMapa()
mapa = s.buscarMapa()
print("")

datoss = ms.calculosIniciales(mapa, mapAux)
print(datoss)


camino, distF = g.shortestPath(mapa,mapAux, 47,9)
print(distF)
