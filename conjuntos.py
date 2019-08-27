#mejoras
#ver conjuntos
#modificar conjuntos

def union_conjuntos(conjunto_a,conjunto_b):
    print("\nla union de A y B es: {}\n\n".format(conjunto_a | conjunto_b))


def interseccion_conjuntos(conjunto_a,conjunto_b):
    print("\nla intersección de A y B es: {}\n\n".format(conjunto_a & conjunto_b))


def diferencia_conjuntos(conjunto_a,conjunto_b):
    try:
        operacion = int(input("elige la diferencia (1. A - B | 2. B - A: "))
    except ValueError:
        print("no se reconoce esa opcion")
        diferencia_conjuntos(conjunto_a, conjunto_b)
    else:
        if operacion == 1:
            print("\nla intersección de A y B es: {}\n\n".format(conjunto_a - conjunto_b))
        elif operacion == 2:
            print("\nla intersección de B y A es: {}\n\n".format(conjunto_b - conjunto_a))
        else:
            print(("no se reconoce esa opcion"))
            diferencia_conjuntos(conjunto_a,conjunto_b)


def diferencia_simetrica_conjuntos(conjunto_a,conjunto_b):
    print("\nla diferencia simetrica de A y B es: {}\n\n".format(conjunto_a ^ conjunto_b))


def ver_conjuntos(conjunto_a,conjunto_b):
    print("Conjunto A: {}".format(conjunto_a))
    print("Conjunto B: {}".format(conjunto_b))

def ver_instrucciones():
    print("Operaciones que puede realizar:")
    print("1 - unir conjuntos")
    print("2 - interseccion de conjuntos")
    print("3 - diferencia de conjuntos")
    print("4 - diferencia simetrica de conjuntos")
    print("5 - ver conjuntos")
    print("6 - ver instrucciones")
    print("7 - salir")


def calculadora_conjuntos():
    print("Bienvenido a los conjuntos")
    print("introduce los elementos de los conjuntos separados por espacios")
    print("ejemplo: 1 3 5 8 0 2\n")

    conjunto_a = set(input("Conjunto A: ").split())
    conjunto_b = set(input("Conjunto B: ").split())

    ver_instrucciones()
    while True:
        try:
            operacion = int(input(": "))

        except ValueError:
            print("no se reconoce esa opcion")

        else:
            if operacion == 1:
                union_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 2:
                interseccion_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 3:
                diferencia_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 4:
                diferencia_simetrica_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 5:
                ver_conjuntos(conjunto_a,conjunto_b)
            elif operacion == 6:
                ver_instrucciones()
            elif operacion == 7:
                print("adiós")
                break
            else:
                print("no se reconoce esa opción")






calculadora_conjuntos()