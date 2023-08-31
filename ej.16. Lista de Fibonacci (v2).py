#Ejercicio lista
#Haz un programa que pida al usuario la cantidad de numeros que quiere que calcule el programa de fibonacci

cont1=0
cont2=1
num=0

print("----------------------------FIBONACCI---------------------------- ")
print(" ")
numero=input("Inserta la cantidad de numeros de fibonacci que deseas calcular: \n")
numero=int(numero)

if numero==0:		
	print("\nERROR!!! El numero ha de ser mayor que 0")
elif numero<0:
	print("\nERROR!!! El numero ha de ser positivo")
elif numero==1:
	lista=[0]
	print("\nSe ha almacenado el siguiente numero:")
	print(lista)
else:
	lista=[0,1]
	for x in range(numero-2):       #Le resto 2 por que el arraylist esta creado con dos numeros por defecto el 0 y el 1
		num=lista[cont1]+lista[cont2]
		lista.append(num)
		cont1+=1
		cont2+=1
	print("\nSe han almacenado los siguientes numeros:")
	print(lista)
