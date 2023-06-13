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
import servicios.RankingAutosServicio as r




datos = s.extraerEsquinasYCalles()
aristas = ms.obtenerAristas(datos[1])
esquinas = ms.obtenerEsquinas(datos[0])
map, mapAux = ms.crearMapa(esquinas, aristas)
s.serializarMapa(map)
mapa = s.buscarMapa()
print("")
datosDist = ms.calculosIniciales(mapa, mapAux)

um.load_movil_element("P1", "<e8,10> <e10,40>", 2000)
um.load_movil_element("P7", "<e10,10> <e8,40>", 20)
um.load_movil_element("P2", "<e1,0> <e3,50>", 4000)
um.load_movil_element("P3", "<e7,20> <e9,30>", 2500)
um.load_movil_element("P4", "<e1,15> <e2,85>", 500)
um.load_movil_element("C1", "<e1,10> <e4,40>", 200)
um.load_movil_element("C2", "<e1,60> <e2,40>", 50)
um.load_movil_element("C3", "<e2,0> <e6,50>", 110)
um.load_movil_element("C4", "<e9,35> <e10,15>", 20)
dicC, dicP = um.load_movil_element("C5", "<e5,10> <e7,40>", 25)

uf.load_fix_element("H1", '"<e8,20> <e10,30>"')
uf.load_fix_element("A1", '"<e2,50> <e7,50>"')
uf.load_fix_element("T5", '"<e2,10> <e6,40>"')
uf.load_fix_element("H4", '"<e3,30> <e2,20>"')
dicUf = uf.load_fix_element("S10", '"<e6,25> <e7,25>"')

#print("PERSONAS")
#g.printDic(dicP)
#print("AUTOS")
#g.printDic(dicC)


"python uber.py -create_trip <persona> <direccion>/<elemento>"

r.ranking("P7",dicC,dicP,datosDist)

