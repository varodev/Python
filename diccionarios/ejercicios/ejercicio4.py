
def main():
    modificar = ""

    diccionario_datos = construir_diccionario_desde_fichero()
    print("El diccionario leído es: \n")
    print(diccionario_datos)

    modificar = input("¿Desea modificar algún elemento del diccionario?s/n")
   
    while (modificar == "s"):
        modificar_elemento_diccionario(diccionario_datos)
        modificar = input("¿Desea modificar algún elemento del diccionario?s/n")

    print(f"Diccionario final:  {diccionario_datos}")

    grabar_diccionario_a_fichero(diccionario_datos)
       
def construir_diccionario_desde_fichero():
    diccionario = {}
    nombre_fichero = input("Intro nombre fichero \n")

    with open(nombre_fichero,"r") as fichero_lectura:
        for linea in fichero_lectura:
            lista_elementos = linea.split(",")
            diccionario[lista_elementos[0]] = int(lista_elementos[1])

    return diccionario

def modificar_elemento_diccionario(diccionario):
    valor = ""
    clave = input("Intro la clave del elemento a modificar: \n")
    if (clave in diccionario):
        valor = int(input("Intro nuevo valor asociado a la clave\n"))
        diccionario[clave] = valor
    else:
        print("No existe esa clave en el diccionario\n")

def grabar_diccionario_a_fichero(diccionario_datos):
    linea_fichero = ""

    nombre_fichero = input("Intro nombre fichero escritura\n")

    with open(nombre_fichero,"w") as fichero_escritura:
        for clave in diccionario_datos:
            linea_fichero = clave + "," + (str(diccionario_datos[clave]) + "\n")
            fichero_escritura.write(linea_fichero)

if __name__ == "__main__":
    main()