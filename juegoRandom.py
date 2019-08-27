import random

#toDoList
#dar "vidas" al usuario
#dar "pistas" si numero es < o <
#opcion restart

def randomGame():
    intentos = 5
    numero = random.randint(1,10)

    print(numero)

    print("bienvenido a adivina el numero!")
    print("estoy pensando en un numero del 1 al 10")
    print("adivina cual es")
    while intentos>0:
        guess = int(input("Mi adivinanza es: "))

        if guess == numero:
            print("Felicitaciones, adivinaste el número!")
            break
        else:
            if guess > numero:
                print("oops, parece que te pasaste")
            else:
                print("oops, te has quedado corto!")
            print("Te quedan " + str(intentos-1) + " intentos")
            intentos -= 1

    print("Gracias por jugar")

randomGame()