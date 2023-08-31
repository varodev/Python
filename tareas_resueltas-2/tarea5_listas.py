
#A partir de una lista de ciudades se deben mostrar aquellas que contengan la letra “s” 
# y detallar cuántas son. 
# Utilizad la función find (https://www.w3schools.com/python/ref_string_find.asp)
def main():
    contador = 0
    lista_ciudades = ["Zamora","Huelva","Teruel","Castellón","Palencia"]

    for elemento in lista_ciudades:
        if (elemento.find("s") != -1):
            print(elemento)
            contador +=1

    print(f"El número de ciudades que tienen la letra s es {contador}")

if __name__ == "__main__":
    main()