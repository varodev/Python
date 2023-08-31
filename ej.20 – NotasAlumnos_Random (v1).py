import random
#print (random.randrange(10))#Enteros aleatorios del 0 al 9

def main():
    print("1 "+texto1+"\n2 "+texto2+"\n3 "+texto3+"\n4 "+texto4+"\n5 "+texto5+"\n6 "+texto6)
    print("\nPor favor, inserte una opción o 'q' para salir\n")
    opcion=input()
    if opcion == "1":
        buscarAlumno()
    elif opcion == "2":
        modificarNota()
    elif opcion == "3":
        mediaNota()
    elif opcion == "4":
        mediaBajasNotas()
    elif opcion == "5":
        mejorAlumno()
    elif opcion == "6":
        peorAlumno()
    elif opcion == "q":
        salir()
    else:
        print("\nInserte una opción válida\n")
        main()

def buscarAlumno():
    alumno=input("Inserte el alumno a buscar: \n")
    existe=False
    contador=0
    for x in listaalumnos:
        contador+=1
        if x == alumno:
            existe=True
            break
    if existe:
        print("\nEl alumno existe en la posicion " + str(contador) + "\n")
    else:
        print("\nEl alumno no existe\n")
 
    main()

def modificarNota():
    alumno=input("Inserte el alumno a modificar su nota: \n")
    existe=False
    contador=0
    for x in listaalumnos:
        contador+=1
        if x == alumno:
            existe=True
            break
    if existe:
        print("El alumno está en la posición " + str(contador-1) + " de la lista")    
        print("Su nota es "+ str(listanotas[contador-1]))
        notaModificada=float(input("Inserte la nueva nota.\n"))
        listanotas[contador-1]=notaModificada
        print("La nueva nota es "+ str(listanotas[contador-1]))
        print(listanotas)
    else:
        print("\nEl alumno no existe\n")
    main()
    
def mediaNota():
    suma=0
    for x in listanotas:
      suma=x+suma
    media=suma/len(listanotas)  
    print("\nLa nota media es "+str(media)+"\n")
    main()

def mediaBajasNotas():
    suma=0
    contador=0
    for x in listanotas:
      if x < 5:  
          suma=x+suma
          contador+=1
    media=suma/contador  
    print("La nota media por debajo de 5 es "+str(media)+"\n")
    main()

def mejorAlumno():
    mejornota=0
    contador=0
    posicion=0
    for x in listanotas:
        contador+=1
        if x > mejornota:
            mejornota=x
            posicion=contador
    print("La mejor nota es "+ str(mejornota)+ " y la obtenido el alumno "+ listaalumnos[posicion-1])
    main()

def peorAlumno():
    peornota=10
    contador=0
    posicion=0
    for x in listanotas:
        contador+=1
        if x < peornota:
            peornota=x
            posicion=contador
    print("La peor nota es "+ str(peornota)+ " y la obtenido el alumno "+ listaalumnos[posicion-1])
     

def salir():
    print("\nSaliendo")

print("#"*60)
print("25. Que gestiona las notas de una clase de 20 alumnos de los cuales sabemos el nombre y la nota.")
print("El programa debe ser capaz de:\n")
texto1="Buscar un alumno"
texto2="Modificar su nota"
texto3="Realizar la media de todas las notas"
texto4="Realizar la media de las notas menores de 5"
texto5="Mostrar el alumno con mejores notas"
texto6="Mostrar el alumno con peores notas"
#print("1 "+texto1+"\n2 "+texto2+"\n3 "+texto3+"\n4 "+texto4+"\n5 "+texto5+"\n6 "+texto6)
listaalumnos=[]
listanotas=[]
for x in range(20):
    alumno=input("Nombre del alumno nº" + str(x+1)+". ")
    nota=input("Nota del alumno nº" + str(x+1)+": ")
    listaalumnos.append(alumno)
    listanotas.append(nota)
#    listaalumnos.append("alumno"+str(x+1))
#    listanotas.append(float(random.randrange(10)))
#    listanotas.append(float(str(random.randrange(10))+"."+str(random.randrange(10))))
"""    nota1=float(random.randrange(11))
    if nota1!=10:
        nota1+=random.randrange(10)/10"""
print(listaalumnos)
print(listanotas)
main()


"""
COMPARAR
import random
#print (random.randrange(10))#Enteros aleatorios del 0 al 9

def main():
    print("1 "+texto1+"\n2 "+texto2+"\n3 "+texto3+"\n4 "+texto4+"\n5 "+texto5+"\n6 "+texto6)
    print("\nPor favor, inserte una opción o 'q' para salir\n")
    opcion=input()
    if opcion == "1":
        buscarAlumno()
    elif opcion == "2":
        modificarNota()
    elif opcion == "3":
        mediaNota()
    elif opcion == "4":
        mediaBajasNotas()
    elif opcion == "5":
        mejorAlumno()
    elif opcion == "6":
        peorAlumno()
    elif opcion == "q":
        salir()
    else:
        print("\nInserte una opción válida\n")
        main()

def buscarAlumno():
    alumno=input("Inserte el alumno a buscar: \n")
    existe=False
    contador=0
    for x in listaalumnos:
        contador+=1
        if x == alumno:
            existe=True
            break
    if existe:
        print("\nEl alumno existe en la posicion " + str(contador) + "\n")
    else:
        print("\nEl alumno no existe\n")
 
    main()

def modificarNota():
    alumno=input("Inserte el alumno a modificar su nota: \n")
    existe=False
    contador=0
    for x in listaalumnos:
        contador+=1
        if x == alumno:
            existe=True
            break
    if existe:
        print("El alumno está en la posición " + str(contador-1) + " de la lista")    
        print("Su nota es "+ str(listanotas[contador-1]))
        notaModificada=float(input("Inserte la nueva nota.\n"))
        listanotas[contador-1]=notaModificada
        print("La nueva nota es "+ str(listanotas[contador-1]))
        print(listanotas)
    else:
        print("\nEl alumno no existe\n")
    main()
    
def mediaNota():
    suma=0
    for x in listanotas:
      suma=x+suma
    media=suma/len(listanotas)  
    print("\nLa nota media es "+str(media)+"\n")
    main()

def mediaBajasNotas():
    suma=0
    contador=0
    for x in listanotas:
      if x < 5:  
          suma=x+suma
          contador+=1
    media=suma/contador  
    print("La nota media por debajo de 5 es "+str(media)+"\n")
    main()

def mejorAlumno():
    mejornota=0
    contador=0
    posicion=0
    for x in listanotas:
        contador+=1
        if x > mejornota:
            mejornota=x
            posicion=contador
    print("La mejor nota es "+ str(mejornota)+ " y la obtenido el alumno "+ listaalumnos[posicion-1])
    main()

def peorAlumno():
    peornota=10
    contador=0
    posicion=0
    for x in listanotas:
        contador+=1
        if x < peornota:
            peornota=x
            posicion=contador
    print("La peor nota es "+ str(peornota)+ " y la obtenido el alumno "+ listaalumnos[posicion-1])
     

def salir():
    print("\nSaliendo")

print("#"*60)
print("25. Que gestiona las notas de una clase de 20 alumnos de los cuales sabemos el nombre y la nota.")
print("El programa debe ser capaz de:\n")
texto1="Buscar un alumno"
texto2="Modificar su nota"
texto3="Realizar la media de todas las notas"
texto4="Realizar la media de las notas menores de 5"
texto5="Mostrar el alumno con mejores notas"
texto6="Mostrar el alumno con peores notas"
#print("1 "+texto1+"\n2 "+texto2+"\n3 "+texto3+"\n4 "+texto4+"\n5 "+texto5+"\n6 "+texto6)
listaalumnos=[]
listanotas=[]
for x in range(20):
    alumno=input("Nombre del alumno nº" + str(x+1)+". ")
    nota=input("Nota del alumno nº" + str(x+1)+": "))
    listaalumnos.append(alumno)
    listanotas.append(nota)
#    listaalumnos.append("alumno"+str(x+1))
#    listanotas.append(float(random.randrange(10)))
#    listanotas.append(float(str(random.randrange(10))+"."+str(random.randrange(10))))
    nota1=float(random.randrange(11))
    if nota1!=10:
        nota1+=random.randrange(10)/10
print(listaalumnos)
print(listanotas)
main()
"""



