#Crea un programa que pida al usuario elegir:
#1- multiplicar
#2- dividir
#3- sumar
#4- restar

print("-----------CALCULADORA-----------")
print("Seleccione una opcion")
print(" 1) Multiplicar\n 2) Dividir\n 3) Sumar\n 4) Restar")
opc=input("Inserte una opcion del 1 al 4: ")
print(" ")
num1=input("Inserte el primer numero: ")
num2=input("Inserte el segundo numero: ")
print(" ")

if opc=="1":
	print("MULTIPLICAR")
	resul=float(num1)*float(num2)
	print("El resultado de multiplicar " + num1 +" y " + num2+" es: " + str(resul))
elif opc=="2":
	print("DIVIDIR")
	resul=float(num1)/float(num2)
	print("El resultado de dividir " + num1 +" y " + num2+" es: " + str(resul))
elif opc=="3":
	print("SUMAR")
	resul=float(num1)+float(num2)
	print("El resultado de sumar " + num1 +" y " + num2+" es: " + str(resul))
elif opc=="4":
	print("RESTAR")
	resul=float(num1)-float(num2)
	print("El resultado de restar " + num1 +" y " + num2+" es: " + str(resul))
else:
	print("ERROR!!! Opcion no valida, tiene que ser un numero entre 1 y 4")



    
