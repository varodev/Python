#Ejercicio Lista

#Una lista números impares desde 1 al 100


lista1=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
lista2=[]
listaimpares=[]
for x in range(101):
    if(x%2!=0):
        listaimpares.append(x)
        print(x)
