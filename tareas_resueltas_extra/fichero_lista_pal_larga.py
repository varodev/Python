def main():
    palabra_mas_larga = ""
    lista_palabras_linea = []
    lista_palabras_largas = []

    with open("mi_fichero_texto.txt","r") as fichero_lectura:
        for linea in fichero_lectura:
            lista_palabras_linea = linea.split(" ")
            palabra_mas_larga = obtener_pal_mas_larga_lista(lista_palabras_linea)
            lista_palabras_largas.append(palabra_mas_larga)

        print((f"La lista de palabras más largas es: {lista_palabras_largas}"))
        
def obtener_pal_mas_larga_lista(lista_palabras):
    pal_resultado = ""

    for elemento in lista_palabras:
        if (len(pal_resultado) < len (elemento)):
            pal_resultado = elemento

    return pal_resultado


if __name__ == "__main__":
    main()