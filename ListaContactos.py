ListaContactos = {}


while True:
    print("\n------ MENÚ ------")
    print(" (1) Agregar Contacto")
    print(" (2) Eliminar Contacto")
    print(" (3) Modificar Contacto")
    print(" (4) Buscar Contacto")
    print(" (5) Mostrar Contactos")
    print(" (6) Salir")
    print("------------------")


    operador = input("Ingrese el número de opción a realizar: ")
    if operador == "1":  #AGREGAR CONTACTO
        while True:
            nombre = input("\nIngrese el nombre del conctacto: ")
            if not nombre.isalpha():
                print("El nombre no puede contener números o caracteres especiales. Ingréselo nuevamente")
            else:
                break
               
        while True:
            dni = input("Ingrese el DNI del conctacto (*sin puntos*): ")
            if dni.isdigit() and dni not in ListaContactos:
                dni = int(dni)
                break
            else:
                print("El DNI ingresado no es válido. Ingréselo nuevamente")
        while True:
            telefono = input("Ingrese el número telefónico del contacto: ").strip()
            if telefono.isdigit():
                telefono = int(telefono)
                break
            else:
                print("El número ingresado no es válido, Ingréselo nuevamente")
        while True:
            correo = input("Ingrese el correo del contacto: ").lower().strip()
            if correo.endswith("@gmail.com"):
                break
            else:
                print("El correo ingresado no es válido. Ingréselo nuevamente")
       
        print("--")
        ListaContactos[dni]={"Nombre": nombre,
                            "DNI": dni,
                            "Telefono": telefono,
                            "Email": correo}
        print(f"{ListaContactos[dni]} /// Agregado exitosamente!")


    elif operador =="2":   #ELIMINAR CONTACTO
        while True:
            if ListaContactos == {}:
                print("\nNo posee contactos para eliminar")
                break
           
            dni = input("Ingrese el dni del contacto a eliminar: ").strip()
            dni = int(dni)
            if dni in ListaContactos:
                del ListaContactos[dni]
                print("--")
                print("Contacto eliminado correctamente.")
                break
            else:
                print("Contacto no encontrado. Ingréselo nuevamente")


    elif operador =="3":   #MODIFICAR CONTACTO
        while True:
            if ListaContactos == {}:
                print("\nNo cuenta con contactos para modificar")
                break
            else:
                dni = input("Ingrese el DNI del contacto a modificar: ")
                if dni.isdigit():
                    dni = int(dni)
           
            if dni in ListaContactos:
                print(f"\nDatos del contacto con DNI {dni} :")
                print(ListaContactos[dni])
                print("\nLista de datos actualizables: ")
                print("  (1)Nombre")
                print("  (2)DNI")
                print("  (3)Teléfono")
                print("  (4)Email")
                operador2 = input("\nIngrese el número de una opcion para continuar: ")


                encontro = False
                if operador2 == "1":
                    print(f"Nombre actual del contacto: '{ListaContactos[dni]["Nombre"]}'")
                    while True:
                        nombre2 = input("Ingrese el nuevo Nombre: ")
                        if nombre2.isalpha():
                            ListaContactos[dni]["Nombre"] = nombre2
                            print("--")
                            print("Nombre modificado correctamente.")
                            encontro = True
                            break
                        else:
                            print("Nombre inválido. Ingréselo nuevamente")
                    if encontro == True:
                        break
               
                elif operador2 == "2":
                    print(f"DNI actual del contacto: '{dni}'")
                    while True:
                        dni2 = input("Ingrese el nuevo DNI: ")
                        if dni2.isdigit():
                            dni2 = int(dni2)
                            auxiliar = ListaContactos[dni]
                            ListaContactos[dni2] = auxiliar
                            ListaContactos[dni2]["DNI"] = dni2
                            del ListaContactos[dni]
                            dni = dni2
                            print("--")
                            print("DNI modificado correctamente.")
                            encontro = True
                            break
                        else:
                            print("DNI inválido. No puede contener puntos. Ingréselo nuevamente")
                    if encontro == True:
                        break


                elif operador2 == "3":
                    print(f"Teléfono actual del contacto: '{ListaContactos[dni]["Telefono"]}'")
                    while True:
                        telefono2 = input("Ingrese el nuevo Teléfono: ")
                        if telefono2.isdigit():
                            ListaContactos[dni]["Telefono"] = telefono2
                            print("--")
                            print("Teléfono modificado correctamente.")
                            print("--")
                            encontro = True
                            break
                        else:
                            print("Teléfono inválido. Ingréselo nuevamente")
                    if encontro == True:
                        break
                           
                elif operador2 == "4":
                    print(f"Correo actual del contacto: '{ListaContactos[dni]["Email"]}'")
                    while True:
                        correo2 = input("Ingrese el nuevo Correo del contacto: ")
                        if correo.endswith("@gmail.com"):
                            ListaContactos[dni]["Email"] = correo2
                            print("--")
                            print(f"Correo modificado correctamente.")
                            encontro = True
                            break
                        else:
                            print("Correo inválido. Ingréselo nuevamente")
                    if encontro == True:
                        break
            else:
                print("DNI no encontrado. Ingréselo nuevamente\n")


    elif operador =="4":  #BUSCAR CONTACTO
        while True:
            if ListaContactos == {}:
                print("\nNo posee contactos para buscar")
                break


            dni = input("Ingrese el DNI del contacto que desea buscar: ")
            dni = int(dni)
            if dni in ListaContactos:
                print(f"\nLos datos del contacto con DNI '{dni}' son: ")
                print(ListaContactos[dni])
                break
            else:
                print("El DNI ingresado no fue encontrado. Ingréselo nuevamente")


    elif operador =="5":   #MOSTRAR TODOS LOS CONTACTOS
        if ListaContactos == {}:
            print("\nNo posee contactos para mostrar")
        else:
            print("\nContactos actuales: ")
            for dni in ListaContactos:
                print(ListaContactos[dni])


    elif operador =="6":   #CERRAR EL PROGRAMA
        print("\nPROGRAMA FINALIZADO - ADIÓS!!!\n")
        exit()


    else:
        print("--")
        print("Opción no valida. Ingréselo nuevamente")