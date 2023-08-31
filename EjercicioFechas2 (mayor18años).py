#Hacer un programa que nos pida una fecha en concreto:
#El día, el mes y el año, en formato (DD/MM/AAAA). Y el programa devolverá el día
#de la semana en castellano.


#Mejora: Insertar la fecha de nacimiento (en el mismo formato) y nos diga si
#somos mayores de edad

import datetime

print("Inserta tu fecha de nacimiento en formato dd/mm/aaaa:"): #en este caso es obligatorio poner dia, mes y año.
diaNacimiento=input()
fecha1=diaNacimiento.split("/") #split segnifica cortar
fecha2=datetime.datetime(int(fecha1[2]),int(fecha1[1]),int(fecha1[0])) #[2]significa año, [1]significa mes,[0]significa dia
fecha3=datetime.datetime(int(fecha1[2])+18,int(fecha1[1]),int(fecha1[0]))
diaSemana=fecha2.strftime("%w")
listaDias=["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes", "Sábado"]

print("Naciste un " + listaDias[int(diaSemana)])

hoy=datetime.datetime.now()  #Muestra la fecha actual
hoy=datetime.datetime(hoy.year,hoy.month,hoy.day) #Muestra la fecha actual a las 0.00horas

if fecha3 <= hoy:
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")



