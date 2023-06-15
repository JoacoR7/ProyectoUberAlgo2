import sys
import servicios.UbicacionMovilServicio as um
import servicios.UbicacionFijaServicio as uf
import servicios.MapaServicio as ms
import servicios.RankingAutosServicio as rs
import servicios.serializacion as se

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        print("Comandos: -h, -help, -load_movil_element, -load_fix_element, -create_trip, -create_map")
    else:
        command = args[1]
        if command == "-create_map":
            ms.crearMapa(args[2])
        elif command == "-h" or command == "-help":
            print("-load_movil_element: carga de ubicacion móvil")
            print("-load_fix_element: carga de ubicación fija")
            print("-create_trip: realizar viaje hacia alguna dirección")
            print("-create_map: ingresar mapa")
        else:
            mapa = se.buscarArchivo("mapa")
            if mapa == None:
                print("No hay ningún mapa cargado, antes de realizar cualquier operación, por favor cargue el mapa")
                command = None
            else:
                if command == "-load_movil_element":
                    um.load_movil_element(args[2], args[3], args[4])
                elif command == "-load_fix_element":
                    uf.load_fix_element(args[2], args[3])
                elif command == "-create_trip":
                    rs.createTrip(args[2], args[3])
                else:
                    print('Ingrese el comando "-h" o "-help" para más información')
