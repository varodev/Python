"""Realiza un programa que calcule el precio final a pagar por varias unidades 
de un mismo artículo, introduciendo por teclado el número de unidades, 
el precio de cada unidad y el tanto por ciento de IVA.

A continuación se pregunta al usuario si quiere terminar, debe responder true o false.
 Si responde true se repite la operación, si responde false finalizamos el programa.

Para leer y almacenar un booleano utilizaremos variableBooleana = lectorEntrada.nextBoolean();
"""

def main():
    precio_final = 0
    precio_unidad = 0
    numero_unidades = 0
    porcentaje_IVA = 0
    precio_sin_IVA = 0
    terminar = "no"

    while (terminar != "si"):
        precio_unidad = int(input("Intro el precio de cada unidad: \n"))
        numero_unidades = int(input("Intro num unidades: \n"))
        porcentaje_IVA  = int(input("Intro el porcentaje de IVA: \n"))

        precio_sin_IVA = (precio_unidad * numero_unidades);
        precio_final = precio_sin_IVA + (precio_sin_IVA * (porcentaje_IVA/100))
        print(f"El precio final de los productos es: {precio_final}")

        terminar = input("¿Desea terminar? si/no\n")
   


if __name__ == "__main__":
    main()