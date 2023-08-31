def main():
    diccionario_inversion = {}
    lista_inversores = ["Ana","Lucía","Nico","Pedro"]

    for elemento in lista_inversores:
        lista_datos = obtener_datos(elemento)
        diccionario_inversion[elemento] = lista_datos

    print(diccionario_inversion)

    mostrar_datos_inversores(diccionario_inversion)

    modificar_datos_inversores(diccionario_inversion)

    print(diccionario_inversion)

def obtener_datos(nombre):
    lista_salida = []

    intro_datos = input(f"Desea introducir un dato para {nombre} ? s/n  \n")

    while (intro_datos == "s"):
        dato = int(input("Introduzda interés inversión: "))
        lista_salida.append(dato)
        intro_datos = input(f"Desea introducir un dato para {nombre} ? s/n  \n")
    
    return lista_salida
    
def mostrar_datos_inversores(dicc_inversores):
    inversor = ""

    print(f"Inversores con datos: \n {dicc_inversores.keys()}: \n")
    inversor = input("Intro nombre inversor: s=salir\n")

    while inversor != "s":
        if (inversor in dicc_inversores):
            print(dicc_inversores[inversor])
            inversor = input("Intro nombre inversor: s=salir\n")

def modificar_datos_inversores(dicc_inversores):
    inversor = ""

    print(f"Inversores con datos: \n {dicc_inversores.keys()}: \n")
    inversor = input("Intro nombre inversor: s=salir\n")

    while inversor != "s":
        if (inversor in dicc_inversores):
            posicion_lista = int(input("intro posición de la lista de intereses a cambiar: "))
            valor_nuevo = int(input("Intro interés: \n"))
            dicc_inversores[inversor][posicion_lista] = valor_nuevo
        else:
            print("No existe ese inversor")

        inversor = input("Intro nombre inversor: s=salir\n")

    
if __name__ == "__main__":
    main()