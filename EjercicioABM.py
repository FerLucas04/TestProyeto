print("--------ABM de Pizzas--------")
ListPizzas = []
PizzasValidas = ["muzarella", "napolitana", "fugazzeta", "jamon", "jamón", "jamon y queso", "especial", "capresse", 
    "calabresa", "cuatro quesos", "hawaiana", "provolone", "vegetariana", "pollo", "champiñones", "panceta", "rúcula",
    "pepperoni", "aceitunas", "pesto", "margarita", "cebolla", "jamon y morron", "jamón y morrón", "fugazza"]

#bucle para iterar varias veces el menú principal
while True:
    while True:     #Menú principal

        print("\n----------- MENÚ -----------")
        print("- CARGAR")
        print("- ELIMINAR")
        print("- MODIFICAR\n")
        #operador = input("Ingrese la operación a realizar (CARGAR, ELIMINAR, MODIFICAR): ").lower()
        operador = input("Ingrese la operación a realizar: ").lower()
        print("")
        if operador == "exit":
            print("PROGRAMA APAGADO")
            print("------ADIOS!!!------")
            exit()

        if operador in ["cargar", "eliminar", "modificar"]:
            print("--------------")
            print(f"OPERACION SELECCIONADA: {operador.upper()}") #upper para colocar la operación en mayús.
            print("RECORDATORIO: para finalizar cualquier operación ingrese FIN o, para salir ingrese EXIT")
            print("--------------")
            break
        else:
            print("--------------")
            print("OPERACION INCORRECTA, por favor hágalo de nuevo")
            print("--------------")

    if operador =="cargar":   #AGREGAR PIZZAS
        contador = 1
        while True: #bucle para agregar una o más pizzas
            pizzas = str(input(f"Ingrese la pizza número {contador}: ")).lower()
            if pizzas == "fin":
                print("OPERACION FINALIZADA")
                print("Las pizzas actuales son:")
                print(ListPizzas)
                print("--------------")
                break
            elif pizzas == "exit":  #cerrar el programa
                #print("PROGRAMA APAGADO")
                print("\n PROGRAMA APAGADO")
                print("------ADIOS!!!------")
                exit()

            if pizzas in PizzasValidas:
            #if pizzas.isalpha() and pizzas in PizzasValidas: #verifica que el usuario ingrese una cadena de letras
                ListPizzas.append(pizzas)
                print(f"La pizza de {pizzas} a sido agregada correctamente!!")
                contador += 1
            else:
                print("Nombre NO VÁLIDO. Ingreselo de nuevo")        

    if operador =="eliminar":   #ELIMINAR PIZZAS
        salir = True
        while salir == True: #bucle para eliminar una o más pizzas
            if len(ListPizzas)== 0 :
                print("No hay pizzas por eliminar")
                break
       
            pizzas = str(input("Ingrese la pizza a eliminar: ")).lower()
            if pizzas.isalpha():  #verifica que el usuario ingrese una cadena de letras
                while True:
                   
                    if pizzas == "exit":  #condicional cerrar el programa
                        print("\n PROGRAMA APAGADO")
                        print("------ADIOS!!!------")
                        bandera = exit
                        exit()  #cierra todo el código
                    elif pizzas == "fin": #condicional para cerra la operación
                        print("OPERACION FINALIZADA")
                        print("--------------")
                        salir = False
                        break
                    elif not pizzas.isalpha():
                        print("Nombre NO VÁLIDO. Ingreselo de nuevo")
                   
                    for i in range(len(ListPizzas)):
                        if ListPizzas[i] == pizzas:
                            print(f"Se eliminó la pizza de {pizzas} con exito")
                            ListPizzas.pop(i)
                            print("Pizzas actuales:")
                            print(ListPizzas)
                            break
                        else:
                            print("No se encontró la pizza ingresada")
                    pizzas = str(input("Ingrese otra pizza a eliminar: ")).lower()                          

    if operador =="modificar":   #MODIFICAR PIZZAS

        while pizzas =="fin": #bucle para modificar una o más pizzas
            if len(ListPizzas)== 0 :
                print("No hay pizzas por modificar")
                break
       
            pizzas = str(input("Ingrese la pizza a modificar: ")).lower()          
            if pizzas.isalpha(): #verifica que el usuario ingrese una cadena de letras
                while True:
                    if pizzas == "exit":  #condicional cerrar el programa
                            print("\n PROGRAMA APAGADO")
                            print("------ADIOS!!!------")
                            bandera = exit
                            exit()  #cierra todo el código
                    elif pizzas == "fin": #condicional para cerra la operación
                        print("OPERACION FINALIZADA")
                        print("--------------")
                        break
                    elif not pizzas.isalpha():
                        print("Nombre NO VÁLIDO. Ingreselo de nuevo")
                    elif pizzas not in PizzasValidas:
                        print("Nombre NO VÁLIDO. Ingreselo de nuevo")
                   
                    for i in range(len(ListPizzas)):
                        if ListPizzas[i] == pizzas:
                            Upizza = pizzas   #varibale para guardar la ultima pizza y mostrarla en el print
                            while True:
                                pizzas = input("Ingrese la nueva pizza: ").lower()
                                if pizzas in PizzasValidas and pizzas != Upizza:
                                    print(f"Se modificó a pizza de {Upizza} por {pizzas} con exito")
                                    ListPizzas[i] = pizzas
                                    break
                                else:
                                    print("El nombre de pizza no es válido u es igual a la pizza a modificar")
                    pizzas = input("\nIngrese otra pizza a modificar: ").lower()