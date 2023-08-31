
def main():
    PRECIO_MAS_DE_10 = 15000
    PRECIO_MENOS_DE_10 = 20000
    DESCUENTO_MENOR_30 = 0.1
    precio_unidad = 0
    descuento_aplicable = 0
    precio_total_bruto = 0
    precio_total = 0

    numero_molinos = int(input("Introduzca el número de molinos a comprar: \n"))
    edad_comprador = int(input("Intro edad comprador: \n"))

    if (numero_molinos >= 10):
        precio_unidad = PRECIO_MAS_DE_10
    else:
        precio_unidad = PRECIO_MENOS_DE_10
    
    if (edad_comprador < 30):
        descuento_aplicable = DESCUENTO_MENOR_30
        
    precio_total_bruto = numero_molinos * precio_unidad
    precio_total = precio_total_bruto - (precio_total_bruto * descuento_aplicable)

    print(f"El precio total final es {precio_total}")

if __name__ == "__main__":
    main()