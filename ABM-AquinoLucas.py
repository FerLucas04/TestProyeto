ListaUsuarios = []

while True:
    print("\n------ MENÚ ------")
    print("(1) Agregar Usuario")
    print("(2) Eliminar Usuario")
    print("(3) Modificar usuario")
    print("(4) Mostrar")
    print("(5) Salir")
    print("------------------")

    operador = input("Ingrese el número de la operación a realizar: ")
    if operador == "1":
        # Alta de usuario
        correo = input("Ingrese el correo personal del usuario (debe terminar en @gmail.com): ").lower().strip()
        if correo.endswith("@gmail.com"):
            encontro = False
            for valores in ListaUsuarios:
                if valores["email"] == correo:
                    encontro = True
                    print("El correo ya está registrado.")
                    break
            if encontro == False:
                contraseña = input("Ingrese una contraseña: ").strip() #quita los espacios
                ListaUsuarios.append({"email": correo, "password": contraseña})
                print("--")
                print(f"El usuario '{correo}' se ha agregado correctamente.")
                print("--")
        else:
            print("Error: solo se permiten correos personales de Gmail.")
           
    elif operador == "2":
        # Baja de usuario
        correo = input("Ingrese el correo del usuario a eliminar: ").lower().strip()
        encontro = False
        for valores in ListaUsuarios:
            if valores["email"] == correo: #valores contiene toda la fila actual, entonces borra toda esa fila
                ListaUsuarios.remove(valores)
                encontro = True
                print("--")
                print("Usuario eliminado correctamente.")
                print("--")
                break
        if encontro == False:
            print("Usuario no encontrado.")

    elif operador == "3":
        # Modificar usuario
        correo = input("Ingrese el correo del usuario a modificar: ").lower().strip()
        encontro = False
        for valores in ListaUsuarios:
            if valores["email"] == correo:
                nueva_contraseña = input("Ingrese la nueva contraseña: ").strip()
                valores["password"] = nueva_contraseña
                encontro = True
                print("--")
                print("Contraseña actualizada correctamente.")
                print("--")
                break
        if encontro == False:
            print("Correo de usuario no encontrado.")

    elif operador == "4":
        # Mostrar usuarios
        if ListaUsuarios == []:
            print("\nNo hay usuarios registrados.")
        else:
            print("\n***Usuarios Registrados:")
            for valores in ListaUsuarios:
                print(f"Correo: {valores['email']} - contraseña: {valores['password']}")

    elif operador == "5":
        # Salir
        print("--")
        print("PROGRAMA FINALIZADO - ADIOS!!!")
        print("--")
        break

    else:
        print("La opción es incorrecta. Intentelo de nuevo.")