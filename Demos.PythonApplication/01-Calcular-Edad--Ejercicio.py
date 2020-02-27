from datetime import datetime, timedelta

print("Dime tu fecha de Nacimiento (dd-mm-yyyy):")
respuesta = input()

fecha_actual = datetime.now()
fecha_nacimiento = datetime.strptime(respuesta, "%d-%m-%Y")
faltan = 0
dias = (fecha_actual - fecha_nacimiento).days
años = dias // 365

if (fecha_nacimiento.month > fecha_actual.month): 
    años -= 1

if (fecha_nacimiento.month == fecha_actual.month) & (fecha_nacimiento.day > fecha_actual.day):
    años -= 1
    faltan = fecha_nacimiento.day - fecha_actual.day

if (faltan == 0): print(f"Tienes {años} años")
else: print(f"Tienes {años} años, pero te falta {faltan} días para los {(años + 1)}")
