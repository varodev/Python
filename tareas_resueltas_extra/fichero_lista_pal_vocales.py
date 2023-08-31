
def main():
    lista_palabras_linea = []
    lista_pal_mas_de_dos_vocales = []
    contador_lineas = 0
    NUM_VOCALES = 3

    with open("mi_fichero_texto.txt","r") as fichero_lectura:
        for linea in fichero_lectura:
            lista_palabras_linea = linea.split(" ")
            lista_pal_mas_de_dos_vocales = obtener_pal_vocales(lista_palabras_linea,NUM_VOCALES)
            contador_lineas+=1
            print((f"""La lista de palabras con más de dos vocales de la linea {contador_lineas} es: 
            {lista_pal_mas_de_dos_vocales}"""))

#Devuelve una lista con las palabras de lista_palabras que tienen más de umbral_vocales vocales
def obtener_pal_vocales(lista_palabras,umbral_vocales):
    lista_salida = []

    for elemento in lista_palabras:
        if (contar_vocales(elemento) >= umbral_vocales):  
            lista_salida.append(elemento)
    
    return lista_salida

#Cuenta las vocales que tiene el texto de entrada
def contar_vocales(texto_entrada):
    lista_vocales = ["a","e","i","o","u"]
    contador_vocales = 0

    #Pasamos todo a minúsculas porque vamos a buscar sólo vocales minúsculas
    texto_minusculas = texto_entrada.lower()

    for vocal in lista_vocales:
        contador_vocales += texto_minusculas.count(vocal)
    
    return contador_vocales

if __name__ == "__main__":
    main()

