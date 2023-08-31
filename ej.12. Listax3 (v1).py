#Un programa que imprima una lista multiplicada por 3


numeros=[1,2,3,4,5,6,7,8,9,10,11]


cont=0

for x in numeros:	
	numeros[cont]=x*3
	cont+=1
print(numeros)