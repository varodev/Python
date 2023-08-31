
def main():
    diccionario_lenguajes = {}
    salir = False

    while (not salir):
        opcion = input("""\n Introduzca una de las siguientes opciones: 
            1: Introducir un dato en el diccionario
            2: Borrar un elemento del diccionario
            3: Mostrar el valor asociado a una clave del diccionario
            4: Modificar el valor asociado a una clave de diccionario
            5: Mostrar el diccionario
            6: Salir
            """)
    
        if (opcion == "1"):
            intro_elemento_en_diccionario(diccionario_lenguajes)
        elif (opcion == "2"):
            borrar_elemento_diccionario(diccionario_lenguajes)
        elif (opcion == "3"):
            mostrar_elemento_diccionario(diccionario_lenguajes)
        elif (opcion == "4"):
            modificar_elemento_diccionario(diccionario_lenguajes)
        elif (opcion == "5"):
            print(diccionario_lenguajes)
        elif (opcion == "6"):
            salir = True
        else:
            print(f"Opción errónea")

def intro_elemento_en_diccionario(diccionario):
    clave = input("Intro el nombre del alumno (clave), no puede haber repetidos\n")
    valor = input("Intro el valor asociado a la clave\n")

    diccionario[clave] = valor

def borrar_elemento_diccionario(diccionario):
    clave_borrar = input("Intro el nombre del alumno (clave) a borrar\n")
    if (clave in diccionario):
        del(diccionario[clave_borrar])
    else:
        print("No existe esa clave en el diccionario\n")

def mostrar_elemento_diccionario(diccionario):
    clave = input("Intro la clave del elemento a mostrar: \n")
    if (clave in diccionario):
        print(diccionario[clave])
    else:
        print("No existe esa clave en el diccionario\n")

def modificar_elemento_diccionario(diccionario):
    valor = ""
    clave = input("Intro la clave del elemento a modificar: \n")
    if (clave in diccionario):
        valor = input("Intro nuevo valor asociado a la clave\n")
        diccionario[clave] = valor
    else:
        print("No existe esa clave en el diccionario\n")

        
if __name__ == "__main__":
    main()