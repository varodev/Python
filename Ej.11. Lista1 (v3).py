#Modificar este código para que se guarden los números más 1000 como string.
#Es decir, lista1=["1000", "1001, ...


lista1=["0","1","2","3","4","5","6","7","8","9"]
lista2=["10","11","12","13","14","15","16","17","18","19"]
lista3=["20","21","22","23","24","25","26","27","28","29"]
liston=[lista1,lista2,lista3]

contador1=0
contador2=0

for x in liston:
    print(x)

for y in x:
    z=int(y)+1000
    print(z)
    liston[contador1][contador2]=str(z)

contador2+=1
contador1+=1
contador2=0

#for (x=0;x<len(lista1);x++){
    

        
