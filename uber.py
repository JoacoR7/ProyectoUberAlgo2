def menu():
    opcion = 0
    while opcion != 9:
        print(" 1: Mostrar las personas\n", 
            "2: Mostrar los autos\n",
            "3:\n",
            "9: Salir")
        
        opcion = input()
        try:
            opcion = int(opcion)
        finally:
            opcion = opcion


        if opcion == 1:
            print("Personas")
        elif opcion == 2:
            print("Autos")
        elif opcion == 9:
            print("¡Nos vemos!")
        else:
            print("Opción incorrecta, por favor intente de nuevo")
        
