def main():
    cadenaEntrada = input("Introduzca una cadena ")

    #OJO, hacemos la división entera
    numero_mitad = len(cadenaEntrada)//2
 
    parte1 = cadenaEntrada[:numero_mitad]
    parte2 = cadenaEntrada[numero_mitad:]

    print(f"{parte1}$$${parte2}")


if __name__=="__main__":
    main()