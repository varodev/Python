#Calcular la hipotenusa de un triángulo rectángulo dado los dos catetos,
#con dos decimales.

import math


def main():
    try:
        c1=float(input("Introduzca la longitud del primer cateto: "))
        c2=float(input("Introduzca la longitud del segundo cateto: "))
        global h
        h=round(math.sqrt((c1*c1)+(c2*c2)),2)

    except:
        print("Número no válido")
        main()


main()
print("La hipotenusa es ", h)
