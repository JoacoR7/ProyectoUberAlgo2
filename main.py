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