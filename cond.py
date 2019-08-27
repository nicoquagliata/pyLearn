def pedirPizza():
    print("Pedir Pizza!!!")


### pedirPizza()

def verificar_edad(edad):
    if edad >= 21:
        print("Puedes entrar al bar".upper())
        print("Y también puedes beber")
    elif edad >= 18:
        print("Puedes entrar al bar")
    else:
        print("No puedes entrar al bar")


edad1 = 18
edad2 = 21

verificar_edad(edad1)
verificar_edad(edad2)

def capitalize (str):
    return str.upper()