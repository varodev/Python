print("-----------CALCULAR LETRA DEL DNI-----------")
print(" ")
dni=input("Introduzca los numeros de su DNI: ")	#Pedimos los numeros al usuario(lo guarda como string)
a=int(dni)					#Transformamos los numeros a int y lo almacenamos en la variable a
resto=a%23					#Almacenamos el resto de dividir el numero del dni entre 23 en la variable resto
letras="TRWAGMYFPDXBNJZSQVHLCKE"    #En letras almacenamos todas las letras posibles que puede tener un DNI en orden
print("La letra del DNI" +dni +" es:")
print(letras[resto])		    #Mostramos la posicion que ocupa el numero del resto en la variable letras
