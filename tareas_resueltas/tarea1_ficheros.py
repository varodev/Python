def main():
    palabra_mas_larga = ""
    palabra_mas_larga_linea = ""

    with open("mi_fichero_texto.txt","r") as fichero_lectura:
        for linea in fichero_lectura:
            palabra_mas_larga_linea = obtener_palabra_mas_larga(linea)
            
            if (len(palabra_mas_larga_linea) > len(palabra_mas_larga)):
                palabra_mas_larga = palabra_mas_larga_linea

    print(f"La palabra más larga es {palabra_mas_larga} ")

def obtener_palabra_mas_larga(linea_entrada):
    palabra_salida = ""
    lista_palabras = linea_entrada.split(" ") #las palabras estarán separadas por blanco
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_salida):
            palabra_salida = palabra
    
    return palabra_salida

if __name__ == "__main__":
    main()


    






