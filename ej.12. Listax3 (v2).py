#Un programa que imprima una lista por 3.


numeros=[1,2,3,4,"5",6,7,8,9,10,11]

print(numeros[0]*3)
print(numeros[1]*3)
print(numeros[2]*3)
print(numeros[3]*3)
print(numeros[4]*3)
print(numeros[5]*3)
print(numeros[6]*3)
print(numeros[7]*3)
print(numeros[8]*3)
print(numeros[9]*3)
print(numeros[10]*3)


print ("Realizado con un for")


indice=0

for x in numeros:
    print(x*3)
    numeros[indice]=x*3
    indice+=1
