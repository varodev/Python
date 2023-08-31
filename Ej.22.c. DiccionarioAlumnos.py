#Ejercicio diccionario
#Objetivo: Almacenar datos de alumnos.
#Campos: DNI, Nombre y apellidos, Fecha de nacimiento en formato por ej:
#07/Diciembre/2000., dirección, código postal, población y teléfono.

#Menú del programa:
    #Tecla i para insertar un nuevo alumno.
    #Tecla m para modificar un alumno. (se modifica insertando el DNI)
    #Tecla e para eliminar un alumno.
    #Techa l para listar un alumno.
    #Tecla s para salir del programa.

#Nota: El mes hay que insertarlo en formato numeral del 1 al 12, pero se tiene
#que almacenar con el nombre del mes.

#Parte 2. Verificar el dni con su letra correspondiente.

#Parte 3. Guardar y leer archivo en un archivo.


alumnos ={}
dni=""

def cabecera():
    print("#"*80+"\n")
    print(" "*20+"BASE DE DATOS DE ALUMNOS\n")
    print("#"*80+"\n")
    main()

def main():
    print("\nInserte una opción para gestionar base de datos")
    print("  'i' para insertar un nuevo alumno")
    print("  'm' para modificar un alumno")
    print("  'e' para eliminar un alumno")
    print("  'l' para listar un alumno")
    print("  's' para salir del programa")  
    opcion=input()
    if opcion == "i":
        insertar()
    elif opcion == "m":
        modificar()
    elif opcion == "e":
        eliminar()
    elif opcion == "l":
        listar()
    elif opcion == "s":
        salir()
    else:
        print("\nPor favor, teclee una opción válida.")
        main()

def submenu(dni):
    print("\nInserte una opción para modificar el alumno")
    print("  '1' para modificar el nombre")
    print("  '2' para modificar la fecha de nacimiento")
    print("  '3' para modificar la direccion")
    print("  '4' para modificar el código postal")
    print("  '5' para modificar la población")
    print("  '6' para modificar el teléfono")
    print("  'v' para volver")  

    opcion=input()

    if opcion == "1":
        cambio=input("Inserte el nuevo nombre:\n")
        alumno[dni][0]=cambio
        submenu(dni)
    elif opcion == "2":
        cambio=input("Inserte la nueva fecha de nacimiento (dd/mm/yyyy):\n")
        alumno[dni][1]=cambio
        submenu(dni)
    elif opcion == "3":
        cambio=input("Inserte la nueva dirección:\n")
        alumno[dni][2]=cambio
        submenu(dni)
    elif opcion == "4":
        cambio=input("Inserte el nuevo código postal:\n")
        alumno[dni][3]=cambio
        submenu(dni)
    elif opcion == "5":
        cambio=input("Inserte la nueva población:\n")
        alumno[dni][4]=cambio
        submenu(dni)
    elif opcion == "6":
        cambio=input("Inserte el nuevo teléfono:\n")
        alumno[dni][5]=cambio
        submenu(dni)
    elif opcion == "v":
        main()
    else:
        print("\nPor favor, teclee una opción válida.")
        submenu(dni)

def insertar():
    print("Inserte el DNI del alumno a insertar: ")
    main()

def modificar():
    print("Inserte el DNI del alumno a modificar o 'v' para salir: ")
    dni=input()
    if dni == 'v':
        main()
    elif dni in alumnos:
        submenu(dni)
    else:
        print("DNI no valido\n")
        modificar()

def eliminar():
    print("Inserte el DNI del alumno a eliminar: ")
    main()
def listar():
    print("Inserte el DNI del alumno a listar: ")
    main()
def salir():
    print("Saliendo... ")


cabecera()


