# Agenda
agenda_telefonica = dict()


def mostrar_mensaje(mensaje):
    print("\n------------ Agenda Telefonica ------------------")
    print(mensaje)
    print("-------------------------------------------------\n")


def mensaje_salida():
    print("Gracias por usar la agenda")
    print("Vuelve pronto!")


def agregar_contacto():
    nombre = input("Nombre del nuevo contacto: ")
    numero = input("Numero del nuevo contacto:")
    agenda_telefonica[nombre] = numero
    mostrar_mensaje("Contacto agregado: " + nombre)


def remover_contacto():
    nombre = input("Nombre del contacto que deseas borrar: ")
    try:
        del agenda_telefonica[nombre]
    except KeyError:
        mostrar_mensaje("No existe el contacto: " + nombre)
    else:
        mostrar_mensaje("Contacto borrado: " + nombre)


def actualizar_contacto():
    nombre = input("Nombre del contacto a actualizar: ")
    numero = input("Nuevo numero del contacto: ")
    agenda_telefonica[nombre] = numero
    mostrar_mensaje("Contacto Actualizado: "+nombre)


def ver_contacto():
    nombre = input("Nombre del contacto: ")
    try:
        mostrar_mensaje(nombre + " - " + agenda_telefonica[nombre])
    except KeyError:
        mostrar_mensaje("Ese contacto no existe")


def ver_todos_contactos():
    if len(agenda_telefonica) == 0:
        mostrar_mensaje("no tienes contactos")
    else:
        mensaje = None
        for contacto in agenda_telefonica:
            numero = agenda_telefonica[contacto]
            if(mensaje is None):
                mensaje = "{} - {}".format(contacto.capitalize(), numero)
            else:
                mensaje += "\n{} - {}".format(contacto.capitalize(), numero)
        mostrar_mensaje(mensaje)


def iniciar_agenda():
    print("Bienvenido a la agenda")
    while True:
        print("Ingrese su opcion:")
        print("1 - Agregar contacto")
        print("2 - Remover contacto")
        print("3 - Actualizar contacto")
        print("4 - Ver un contacto")
        print("5 - Ver todos los contactos")
        print("6 - Salir")

        try:
            operacion = int(input(": "))
        except ValueError:
            print("Selecciona un numero del 1 al 6\n")
        else:
            if operacion == 1:
                agregar_contacto()
            elif operacion == 2:
                remover_contacto()
            elif operacion == 3:
                actualizar_contacto()
            elif operacion == 4:
                ver_contacto()
            elif operacion == 5:
                ver_todos_contactos()
            elif operacion == 6:
                mensaje_salida()
                break
            else:
                print("operacion desconocida, pruebe de nuevo")
                continue


iniciar_agenda()
