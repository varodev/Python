#Escribe un programa que contenga una lista, la muestre, 
# le pida al usuario dos posiciones de la lista e intercambie 
# los valores de las posiciones indicadas por el usuario.Repite la operación
#hasta que el usuario diga no
def main():
    lista = [4,5,6,7,8,9,10,11,12]
    almacen = 0

    while (input("Desea intercambiar elementos de la lista?\n") != "no"):
        print(lista)

        posicion_1 = int(input("Introduzca posición 1, comenzando en 0 \n"))
        posicion_2 = int(input("Introduzca posición 2, comenzando en 0 \n"))

        if (posicion_1 < len(lista) and posicion_2 < len(lista)):
            almacen = lista[posicion_1]

            lista[posicion_1] = lista[posicion_2]
            lista[posicion_2] = almacen
        else:
            print("Posición fuera de rango")

        print(lista)
        
if __name__ == "__main__":
    main()