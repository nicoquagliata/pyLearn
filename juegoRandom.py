import random

#toDoList
#pruebas de error

def randomGame():
    intentos = 5
    numero = random.randint(1,10)

    print(numero)

    print("bienvenido a adivina el numero!")
    print("estoy pensando en un numero del 1 al 10")
    print("Puedes adivinar cual es? Tienes {} intentos...".format(intentos))
    while intentos>0:
        try:
            guess = int(input("Mi adivinanza es: "))

        except ValueError:
            print("Por favor introduce un número del 1 al 10")

        else:
            intentos -= 1

            if guess == numero:
                print("Felicitaciones, adivinaste el número!")

                reintentar = input("Jugar nuevamente: si/no ")

                if reintentar.lower() == "si":
                    randomGame()
                else:
                    break
            elif guess > numero:
                print("oops, parece que te pasaste")
            else:
                print("oops, te has quedado corto!")

            if intentos > 0:
                print("Te quedan {} intentos de {}".format(intentos, "5"))

    else:
        print("Se te acabaron los intentos, el numero era {}".format(numero))
        print("Gracias por jugar\n")
        reintentar = input("Jugar nuevamente: si/no ")

        if reintentar.lower() == "si":
            randomGame()

randomGame()