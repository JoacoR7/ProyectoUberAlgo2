import pickle

def serializarPersonas(P):
    try:
        fichero = open("lista_personas", "wb")
        pickle.dump(P, fichero)
    finally:
        fichero.close()

def buscarPersonas():
    try:
        fichero = open("lista_personas")
        found = True
    except FileNotFoundError:
        found = False
    finally:
        if found == True:
            fichero.close()
        return found

def borrarPersonas():
    if buscarPersonas():
        fichero = open("lista_personas")
        del(fichero)
    else:
        print("No se encontró el archivo")

def serializarAutos(A):
    try:
        fichero = open("lista_autos", "wb")
        pickle.dump(A, fichero)
    finally:
        fichero.close()

def buscarAutos():
    try:
        fichero = open("lista_autos")
        found = True
    except FileNotFoundError:
        found = False
    finally:
        if found == True:
            fichero.close()
        return found

def borrarAutos():
    if buscarAutos():
        fichero = open("lista_autos")
        del(fichero)
    else:
        print("No se encontró el archivo")

def serializarMapa(M):
    try:
        fichero = open("mapa", "wb")
        pickle.dump(M, fichero)
    finally:
        fichero.close()

def buscarMapa():
    try:
        fichero = open("mapa")
        found = True
    except FileNotFoundError:
        found = False
    finally:
        if found == True:
            fichero.close()
        return found

def borrarMapa():
    if buscarMapa():
        fichero = open("mapa")
        del(fichero)
    else:
        print("No se encontró el archivo")

def serializarUbiFija(U):
    try:
        fichero = open("ubicaciones_fijas", "wb")
        pickle.dump(U, fichero)
    finally:
        fichero.close()

def buscarUbiFija():
    try:
        fichero = open("ubicaciones_fijas")
        found = True
    except FileNotFoundError:
        found = False
    finally:
        if found == True:
            fichero.close()
        return found

def borrarUbiFija():
    if buscarUbiFija():
        fichero = open("ubicaciones_fijas")
        del(fichero)
    else:
        print("No se encontró el archivo")
