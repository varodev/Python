#Ejercicio lista
#Haz un programa que imprima lista de fibonacci hasta el 7000

lista=[0,1]
cont1=0
cont2=1
num=0

for x in range(71):
	if(num<=7000):
		num=lista[cont1]+lista[cont2]
		lista.append(num)
		cont1+=1
		cont2+=1
print(lista)
		
