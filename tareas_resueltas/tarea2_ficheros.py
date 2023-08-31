def main():
    lista_palabras = []
    inversion  = 0
    max_inversion = 0
    lista_max_inversion = []

    with open("mi_fichero_texto.txt","r") as fichero_lectura:
        for linea in fichero_lectura:
            lista_palabras = linea.split(",")
            inversion = int(lista_palabras[3])

            if (inversion > max_inversion):
                max_inversion = inversion
                lista_max_inversion = lista_palabras.copy()

    print(f"""El nombre y apellidos del usuario con más dinero
          es {lista_max_inversion[0]} {lista_max_inversion[1]}""")
    

if __name__ == "__main__":
    main()


    






