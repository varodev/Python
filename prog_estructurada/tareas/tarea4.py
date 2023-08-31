def main():
    num_entrada = int(input("Intro numero: \n"))

    while (num_entrada > 0):
        resultado = sumar_digitos(num_entrada)
        print(f"Las suma de los dígitos del número {num_entrada} es {resultado}")
        num_entrada = int(input("Intro numero: \n"))

def sumar_digitos(numero):
    resultado = 0

    while (numero > 0):
        resultado = resultado + (numero % 10)
        numero = numero // 10
    return resultado

if __name__=="__main__":
    main()