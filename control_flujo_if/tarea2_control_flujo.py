
def main():
    resultado_conversion = 0
    conversion = input("Elija el tipo de conversión: 1: C-->F  2: F-->C \n")
    numGrados = int(input("Introduzca los grados: \n"))

    if (conversion == "1"):
        resultado_conversion = (numGrados *(9/5)) + 32
    elif (conversion == "2"):
        resultado_conversion = (numGrados-32)*(5/9)
    else:
        print("Tipo de conversión erronea")

    print(f"El resultado es: {resultado_conversion}")

if __name__ == "__main__":
    main()