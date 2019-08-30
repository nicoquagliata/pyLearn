#todo List
#2 poner formato de 12 horas (strftime.org)
#3 cambiar el formato de fecha

import datetime

def ver_instrucciones():
    print("estas son las operaciones:")
    print("1 - ver hora local")
    print("2 - ver fecha y hora")
    print("3 - ver hora en ny")
    print("4 - ver hora en sf")
    print("7 - ver hora en madrid")
    print("8 - ver hora en tokio")
    print("5 - ver instrucciones")
    print("6 - salir")


def ver_hora(zona_horaria):
    formato_de_hora = "%H:%M:%S"
    zona_horaria = datetime.timezone(datetime.timedelta(hours=zona_horaria))
    hora_actual = datetime.datetime.now(zona_horaria).time()
    hora_formateada = hora_actual.strftime(formato_de_hora)
    print("La hora exacta es: {} y la zona horaria {}".format(hora_formateada, zona_horaria))

def ver_fecha_hora():
    formato = "%d/%m/%y %H:%M:%S"
    zona_horaria = datetime.timezone(datetime.timedelta(hours=-3))
    fecha_actual = datetime.datetime.now(zona_horaria)
    fecha_formateada = fecha_actual.strftime(formato)
    print("La fecha exacta es: {}".format(fecha_formateada))

def ver_reloj():
    print("Bienvenido al reloj")
    ver_instrucciones()
    while True:
        try:
            operacion = int(input(": "))

        except ValueError:
            print("try again")

        else:
            if operacion==1:
                ver_hora(-3)
            elif operacion==2:
                ver_fecha_hora()
            elif operacion==3:
                ver_hora(-5)
            elif operacion==4:
                ver_hora(-8)
            elif operacion==5:
                ver_instrucciones()
            elif operacion==6:
                print("Adios!")
                break
            elif operacion == 7:
                ver_hora(+1)
            elif operacion == 8:
                ver_hora(+9)
            else:
                print("no reconozco esa operacion")

ver_reloj()