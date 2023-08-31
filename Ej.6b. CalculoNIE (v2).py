
print("-----------CALCULAR LETRA DEL NIE EXTRANJERO-----------")
print(" ")

#Almacena la letra:
letra=input("Introduzca la letra del DNI: ")			

#Almacena los 7 caracteres como string:
nie=input("Introduzca los numeros de su DNI: ")			

#Cambia la letra por un número:
if letra=="x":							
	letra=0
elif letra=="y":
	letra=1
elif letra=="z":
	letra=2
else:
	print("Letra no valida, ha de ser x,y,z")


#Pasamos el numero de la letra a string y le añadimos seguido el resto de números:
niefinal=str(letra)+nie					

#Pasamos todos los números juntos a int:
a=int(niefinal)							

#Dividimos los números entre 23 y nos guardamos el resto:
resto=a%23			

#En letras almacenamos todas las letras posibles que puede tener un DNI en orden:
letras="TRWAGMYFPDXBNJZSQVHLCKE"
print("Su letra es:")

#Mostramos la posicion que ocupa el numero del resto en la variable letras:
print(letras[resto])	
