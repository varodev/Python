
import datetime                         #Libreria para trabajar con fechas

x=datetime.datetime.now()               #Muestra la fecha actual
print (x)

y=datetime.datetime(2015,1,1)           #año,mes,dia
print (y)

print(x-y)                              #Muestran los dias que han pasado desde x a y (dias,horas y segundos)

x.year          #Muestra el año actual
x.month         #Muestra el mes actual
x.day           #Muestra el dia actual

x.strftime("%a")        #Dice el dia abreviado
x.strftime("%A")        #Dice el dia
x.strftime("%w")        #Dice el dia de la semana de forma numerica(0=dominfo lunes=1, martes=2...)
x.strftime("%B")        #Mes
x.strftime("%Y")        #Año
