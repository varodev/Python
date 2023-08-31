def main():
    lista_palabras = []
    inversion  = 0
    umbral_inversion = int(input("Intro umbral inversion: \n"))


    with open("mi_fichero_texto.txt","r") as fichero_lectura, \
            open ("mi_fichero_salida.txt","w") as fichero_escritura:
        for linea in fichero_lectura:
            lista_palabras = linea.split(",")
            inversion = int(lista_palabras[3])

            if (inversion > umbral_inversion):
                fichero_escritura.write(linea)
                
if __name__ == "__main__":
    main()


    






