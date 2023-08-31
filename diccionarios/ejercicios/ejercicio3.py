""" Observa que el diccionario se pasa por REFERENCIA a los métodos"""
def main():
    lista_puntuaciones = [23,487,784,3647,927,8723,2323]
    lista_nicks = ["arot","muki","nit","ares","ghot","nuka","nert"]
    diccionario_puntuaciones = {}
    salir = False

    for contador in range(len(lista_puntuaciones)):
        diccionario_puntuaciones[lista_nicks[contador]] = lista_puntuaciones[contador]

    while (not salir):
        opcion = input("""\n Introduzca una de las siguientes opciones: 
            1: Mostrar el diccionario
            2: Modificar el valor asociado a una clave de diccionario
            3: Salir
            """)
    
        if (opcion == "1"):
            print(diccionario_puntuaciones)
        elif (opcion == "2"):
            modificar_elemento_diccionario(diccionario_puntuaciones)
        elif (opcion == "3"):
            salir = True
        else:
            print(f"Opción errónea")

def modificar_elemento_diccionario(diccionario):
    valor = ""
    clave = input("Intro la clave del elemento a modificar: \n")
    if (clave in diccionario):
        valor = int(input("Intro nuevo valor asociado a la clave\n"))
        diccionario[clave] = valor
    else:
        print("No existe esa clave en el diccionario\n")


if __name__ == "__main__":
    main()