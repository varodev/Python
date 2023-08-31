def main():
    lista_num_formato_texto = []
    lista_numeros = []
    media_linea = 0

    with open("mi_fichero_numeros.txt","r") as fichero_lectura:
        for linea in fichero_lectura:
            lista_num_formato_texto = linea.split(",")
            lista_numeros = convertir_lista_a_enteros(lista_num_formato_texto)
            media_linea = calcular_media_num_lista(lista_numeros)
            print(f"La media de la lista {lista_numeros} es: {media_linea}")

def convertir_lista_a_enteros(lista_num_texto):
    lista_salida  = []
    for elemento in lista_num_texto:
        numero = int(elemento)
        lista_salida.append(numero)
    return lista_salida

def calcular_media_num_lista(lista_num):
    suma = 0
    resultado = 0

    for elemento in lista_num:
        suma += elemento
    
    resultado = suma/(len(lista_num))

    return resultado


if __name__ == "__main__":
    main()


    






