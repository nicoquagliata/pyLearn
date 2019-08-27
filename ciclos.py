manzanas = 10

while manzanas >0:
    print("manzanas numero " + str(manzanas))
    manzanas -= 1

print("no hay mas manzanas")

numeros = [0,1,2,3,4,5,6,7,8,9]

for numero in numeros:
    if numero > 7:
        print("rompo el ciclo")
        break
    if numero%2 == 0:
        print("salto el ciclo")
        continue
    print(numero)