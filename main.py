import uber
import entidades.dictionary as d
import servicios.serializacion as s
import servicios.MapaServicio as ms
import servicios.UbicacionFijaServicio as uf
import servicios.UbicacionMovilServicio as um
import entidades.graph as g
import servicios.UbicacionFijaServicio as uf
#servicios.serializacion.serializarPersonas(["A", "B", "C"])
import servicios.RankingAutosServicio as r



ms.crearMapa("C:\\Users\\Usuario\\Documents\\GitHub\\ProyectoUberAlgo2\\mapa3")
mapa = s.buscarArchivo("mapa")
mapaAux = s.buscarArchivo("mapaAux")


um.load_movil_element("P1", "<e8,10> <e10,40>", 2000)
um.load_movil_element("P7", "<e10,10> <e8,40>", 20)
um.load_movil_element("P2", "<e1,0> <e3,50>", 4000)
um.load_movil_element("P3", "<e7,20> <e9,30>", 2500)
um.load_movil_element("P4", "<e4,10> <e9,40>", 500)
um.load_movil_element("C1", "<e14,60> <e9,40>", 200)
um.load_movil_element("C2", "<e14,70> <e9,30>", 200)
um.load_movil_element("C3", "<e2,0> <e6,50>", 110)
um.load_movil_element("C4", "<e9,35> <e10,15>", 20)

uf.load_fix_element("H1", '"<e20,5> <e47,55>"')
uf.load_fix_element("A1", '"<e2,50> <e7,50>"')
uf.load_fix_element("T5", '"<e2,10> <e6,40>"')
uf.load_fix_element("H4", '"<e3,30> <e2,20>"')


#print("PERSONAS")
#g.printDic(dicP)
#print("AUTOS")
#g.printDic(dicC)


"python uber.py -create_trip <persona> <direccion>/<elemento>"
destino = ["e20",5,"e47",55]
#r.ranking("P4", destino)
#print(um.searchUbiMovil(dicC,"C4"))
#print(um.searchUbiMovil(dicP,"P7"))
#"<e20,5> <e47,55>"


r.createTrip("P4", "H1")

