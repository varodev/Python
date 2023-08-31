#Crea un programa que pida al usuario elegir:
#1- multiplicar
#2- dividir
#3- sumar
#4- restar

print("Inserte la operación a realizar")
print("1) Multiplicar\n2) Dividir\n3) Sumar\n4) Restar")
operacion=input("Inserte la operación del 1 al 4:\n")
primero=input("Inserte el primer número:\n")
segundo=input("Inserte el segundo número:\n")

#Aqui va el código que tenéis que hacer:      
      
if operacion=="1":
    resultado=float(primero)*float(segundo)
    print("El resultado de multiplicar el número "+primero+" y el número "+segundo+ " es "+str(resultado))
if operacion=="2":
    resultado=float(primero)/float(segundo)
    print("El resultado de dividir el número "+primero+" y el número "+segundo+ " es "+str(resultado))
if operacion=="3":
    resultado=float(primero)+float(segundo)
    print("El resultado de sumar el número "+primero+" y el número "+segundo+ " es "+str(resultado))
if operacion=="4":
    resultado=float(primero)-float(segundo)
    print("El resultado de restar el número "+primero+" y el número "+segundo+ " es "+str(resultado))





    
