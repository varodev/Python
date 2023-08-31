import datetime

x = datetime.datetime.now()
print(x)



y = datetime.datetime(2015,1,1) #AAAA/MM/DD
print(y)

x.strftime("%a") #Imprime día de la semana abreviada en ingles.
x.strftime("%A") #Imprime día de la semana NO abreviada en ingles.
x.strftime("%w") #Imprime día de la semana empezando por 0 y domingo.
z=x.strftime("%w")
