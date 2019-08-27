import random

numero = random.randint(1,10)

print(numero)

print("bienvenido a adivina el numero!")
print("estoy pensando en un numero del 1 al 10")
print("adivina cual es")
while True:
    guess = int(input("El numero es: "))

    if guess == numero:
        print("adivinaste")
        break
    else:
        print("fallaste, intentalo de nuevo")

print("Gracias por jugar")