import re

def agregar_articulo():
    articulo = input("Articulo que quieres agregar: ")

    existe = chequear_articulo(articulo)
    if existe:
        print("Ese articulo ya esta en la lista")
    else:
        archivo_lista = open("lista.txt", "a")
        archivo_lista.write("{}\n".format(articulo))
        archivo_lista.close()

def remover_articulo():
    articulo = input("Articulo que quieres eliminar: ")
    articulo = "{}\n".format(articulo)

    lista = open("lista.txt", "r")
    lista_compras = lista.read()
    lista.close()

    lista_compras = lista_compras.replace(articulo, "")

    archivo_lista = open("lista.txt", "w")
    archivo_lista.write(lista_compras)
    archivo_lista.close()


def chequear_articulo(articulo):
    lista = open("lista.txt", "r")
    lista_compras = lista.read()
    chequear = re.search("\n{}\n".format(articulo), lista_compras)
    lista.close()
    if chequear:
        return True
    else:
        return False


def ver_lista():
    lista = open("lista.txt", "r")
    print(lista.read())
    lista.close()



def ver_opciones():
    print("Por favor elige una opcion:")
    print("1 - Agregar articulo a la lista")
    print("2 - Remover articulo de la lista")
    print("3 - Ver lista")
    print("4 - Ver opciones")
    print("5 - Salir")


def lista_de_compras():
    print("bienvenido a la lista de compras!")
    ver_opciones()

    while True:
        try:
            opcion = int(input("Ingresa tu opción (4-ver opciones): "))

        except ValueError:
            print("Por favor introduce un número valido")

        else:
            if opcion == 1:
                agregar_articulo()
            elif opcion == 2:
                remover_articulo()
            elif opcion == 3:
                ver_lista()
            elif opcion == 4:
                ver_opciones()
            elif opcion == 5:
                print("Gracias por jugar con nosotros")
                break
            else:
                print("Ingrese una opcion valida")
                continue


lista_de_compras()