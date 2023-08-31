#Hacer un programa que nos pida una fecha en concreto:
#El día, el mes y el año. Y el programa le devolveras el día
#de la semana en castellano.

import datetime


dia=int(input("Inserte el día del mes:\n"))
mes=int(input("Inserte el mes:\n"))
anio=int(input("Inserte el año:\n"))

hoy=datetime.datetime.now()
fechahoy=datetime.datetime(hoy.year,hoy.month,hoy.day)
fecha=datetime.datetime(anio,mes,dia)

if fechahoy> fecha:
    texto="fué"
elif fechahoy < fecha:
    texto="será"
else:
    texto="es"

diaSemana=int(fecha.strftime("%w"))
semana=["domingo","lunes","martes","miércoles","jueves","viernes","sábado"]
print("La fecha "+str(dia)+"/"+str(mes)+"/"+str(anio)+ " "+texto+" "+ semana[diaSemana])

print(fecha)
print(fechahoy)


