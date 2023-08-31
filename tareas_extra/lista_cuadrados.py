def main():
    lista_numeros = [3,4,2,6,7]
    print(lista_numeros)
    
    for elemento in lista_numeros:
        pintar_cuadrado(elemento)
        print("\n")
    
def pintar_cuadrado(longitud_lado):
    CARACTER = '#'
    for i in range(longitud_lado):
        imprimir_linea_caracter(CARACTER, longitud_lado)
       
        
def imprimir_linea_caracter(caracter,num_carac_linea):
    linea = ""

    for i in range(num_carac_linea):
        linea = linea + caracter
    
    print(linea)


if __name__ == "__main__":
    main()