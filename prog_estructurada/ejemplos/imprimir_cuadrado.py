def main():
    caracter_linea = input("Qué caracter quiere usar para la figura? \n")
    tamanio_lado = int(input("Intro el tamaño del lado: \n"))

    for i in range(tamanio_lado):
        imprimir_linea_caracteres(tamanio_lado,caracter_linea)
        
def imprimir_linea_caracteres(longitud_linea,caracter):
    linea = ""
    
    #Componemos una cadena de los carateres que nos indican
    for i in range(longitud_linea):
        linea = linea + caracter

    print(linea)
   
if __name__=="__main__":
    main()

    