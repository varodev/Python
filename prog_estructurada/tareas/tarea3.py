def main():
    longitud_lado = int(input("Intro la longitud del lado: \n"))
    caracter = input("Intro caracter: \n")

    for i in range(1,longitud_lado + 1):
        imprimir_linea_caracter(caracter, i)

    for j in range(longitud_lado,0,-1):
        imprimir_linea_caracter(caracter, j)
        

def imprimir_linea_caracter(caracter,num_carac_linea):
    linea = ""

    for i in range(num_carac_linea):
        linea = linea + caracter
    
    print(linea)

if __name__=="__main__":
    main()