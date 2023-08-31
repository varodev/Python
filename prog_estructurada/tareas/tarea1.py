def main():
    num_entrada = int(input("Intro numero: \n"))

    while (num_entrada > 0):
        print(calcular_factorial(num_entrada))
        num_entrada = int(input("Intro numero: \n"))

def calcular_factorial(numero):
    resultado = 1

    for i in range(1,numero+1):
        resultado = resultado * i
    return resultado



if __name__ == "__main__":
    main()