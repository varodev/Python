def main():
    linea = ""
    caracter_linea = input("Qué caracter quiere usar para la figura? \n")
    tamanio_lado = int(input("Intro el tamaño del lado: \n"))

    for i in range(tamanio_lado):
        for j in range(tamanio_lado):
            linea = linea + caracter_linea
        print(linea)
        linea = ""
   
if __name__=="__main__":
    main()

    