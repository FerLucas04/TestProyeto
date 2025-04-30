ListaContactos = {}
#Nombre, DNI, Teléfono y email

print("\n------ MENÚ ------")
print("(1) Agregar Contacto")
print("(2) Eliminar Contacto")
print("(3) Modificar Contacto")
print("(4) Buscar Contacto")
print("(5) Mostrar Contactos")
print("(6) Salir")
print("------------------")

operador = input("Ingrese el número de opción a realizar")

if operador == "1":
    while True:
        nombre = input("Ingrese el nombre del conctacto")
        if nombre.isalpha():
            break
        else:
            print("El nombre no puede contener números o caracteres especiales. Ingréselo nuevamente")
    dni = input("Ingrese el DNI del conctacto")