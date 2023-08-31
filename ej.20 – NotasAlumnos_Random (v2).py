
#ej.20 – Notas de alumnos con Random (v2)

def buscarAlumno():
	alumno=input("Inserte el alumno a buscar:\n")
	existe=False
	cont=0
	for x in listAlumnos:
		cont=cont+1
		if x == alumno:
			existe=True
			break
	if existe:
		print("\nEl alumno existe.\n")
		print("En la posicion." +str(cont-1) +"\n")
	else:
		print("El alumno no existe.\n")
	main()
	
def modificarNota():
	alumno=input("Inserte el alumno a modificar su nota:\n")
	existe=False
	cont=0
	for x in listAlumnos:
		cont=cont+1
		if x == alumno:
			existe=True
			break
	if existe:
		print("\nEl alumno existe. En la posicion." +str(cont-1) +"\n")
		print("Su nota es: " +str(listNotas[cont-1]))
		notaModificada=float(input("Inserte la nueva nota:\n"))
		listNotas[cont-1]=notaModificada
		print("Nota modificada. su nota es: " +str(listNotas[cont-1]))
	else:
		print("ERROR!!! El alumno no existe.\n")
	main()
	
def mediaNota():
	suma=0
	for x in listNotas:
		suma=x+suma
	media=suma/len(listNotas)
	print("La nota media es: " +str(media))
	main()
	
def mediaSuspensos():
	suma=0
	cont=0
	for x in listNotas:
		if x < 5 :
			suma=suma+x
			cont=cont+1
	media=suma/cont
	print("La nota media por debajo de 5 es: " +str(media))
	main()
	
def mejorAlumno():
	mejorNota=0
	cont=0
	posicion=0
	for x in listNotas:
		cont=cont+1
		if x > mejorNota:
			mejorNota=x
			posicion=cont
	print("La mejor nota es: " +str(mejorNota) +" En la posicion " +str(posicion))
	print("La ha obtenido el alumno:" +str(listAlumnos[posicion-1]))
	main()
	
def peorAlumno():
	peorNota=10
	cont=0
	posicion=0
	for x in listNotas:
		cont=cont+1
		if x < peorNota:
			peorNota=x
			posicion=cont
	print("La peor nota es: " +str(peorNota) +" En la posicion " +str(posicion))
	print("La ha obtenido el alumno:" +str(listAlumnos[posicion-1]))
	main()
	
def salir():
	print("Adios, gracias por utilizar el programa")

def main():
	#Menu
	print(" ")
	print("#"*30)
	print("OPCIONES:")
	print("#"*30)
	print("\n1- Buscar un alumno")
	print("2- Modificar su nota")
	print("3- Realizar la media de las notas")
	print("4- Realizar la media de las notas menores a 5")
	print("5- Mostrar el alumno que mejores notas ha sacado")
	print("6- Mostrar el alumno que peores notas ha sacado ")
	print("\nSeleccione una opcion o pulse 'q' para salir")
	opcion=input()
	
	if opcion=="1":
		buscarAlumno()
	elif opcion=="2":
		modificarNota()
	elif opcion=="3":
		mediaNota()
	elif opcion=="4":
		mediaSuspensos()
	elif opcion=="5":
		mejorAlumno()
	elif opcion=="6":
		peorAlumno()
	elif opcion=="q":
		salir()
	else:
		print("ERROR!!! Inserte una opcion  valida.\n")
		main()

listAlumnos=[]
listNotas=[]

#Pedimos los datos de los 20 alumnos "nombre y notas"
for x in range (20):
	print("\n----DATOS DEL ALUMNO Nº " +str(x+1) +"----")
	alumno=input("Nombre del alumno: ")
	nota= float(input("Nota del alumno: "))
	listAlumnos.append(alumno)
	listNotas.append(nota)
main()
