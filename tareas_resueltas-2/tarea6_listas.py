#A partir de una lista de palabras, se debe pedir al usuario 2 letras. Se recorre la lista y cuando 
# encontremos una palabra que contiene las dos letras la mostramos, dejamos de recorrer la lista 
# y finalizamos el programa. OJO! como tenemos que dejar de recorrer la lista antes de llegar al
#final no podemos un un for elemento in lista (Está prohibido usar break, es una mala práctica),
#en este caso necesitamos usar while que nos da un mayor control del fin del bucle.

def main():
    lista_ciudades = ["Sevilla", "Tarragona", "Cuenca", "Vitoria", "Vigo"]
    contador = 0
    encontrada = False

    letra1 = input("Introduzca una letra\n")
    letra2 = input ("Intoduzca la segunda letra \n")

    while( not(encontrada) and (contador < len(lista_ciudades)) ):
        if ( (lista_ciudades[contador].find(letra1) != -1) and 
           (lista_ciudades[contador].find(letra2) != -1) ):
            encontrada = True
            print(f"Se han encontrado las dos letras en una palabra: {lista_ciudades[contador]}")

        contador += 1

if __name__ == "__main__":
    main()