#lista de compras

lista_articulos = list()

print("Bienvenido a la lista de compras")

def agregar_articulo():
    # print("Agregar articulo"
    articulo = input("\nNombre del articulo a agregar: ")
    lista_articulos.append(articulo)
    print("Articulo agregado: " + articulo+"\n")

def remover_articulo():
    print()
    articulo = input("\nNombre del articulo a remover: ")
    lista_articulos.remove(articulo)
    print("Articulo removido: " + articulo + "\n")

def ver_articulos():
    print("\n---------- Lista de Compras ----------")
    for articulo in lista_articulos:
        print(articulo.capitalize())
    print("--------------------------------------\n")

while True:

    print("Estas son las operaciones que puedes realizar")
    print("1 - Agregar articulo")
    print("2 - Remover articulo")
    print("3 - Ver articulos")
    print("4 - Salir")

    operacion = int(input(": "))

    if operacion == 1:
        agregar_articulo()
    elif operacion == 2:
        remover_articulo()
    elif operacion == 3:
        ver_articulos()
    elif operacion == 4:
        break
    else:
        print("Ingrese una opcion valida")
        continue

print("Gracias por usar la lista de compras")
print("Vuelve pronto!")