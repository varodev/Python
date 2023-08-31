# A partir de una lista de números interna el programa debe recorrerla, mostrar cada número
#  junto a la posición que ocupan, aquellos números que sean mayores de 10 se deben mostrar divididos por 2

def main():
    lista_numeros = [2,45,64,6,66,7]
    contador = 0
    numero_a_mostrar = 0

    for elemento in lista_numeros:
        numero_a_mostrar = elemento

        if (elemento > 10):
            numero_a_mostrar = elemento / 2

        print(f"Posición {contador} ---> {numero_a_mostrar}")

        contador += 1

if __name__ == "__main__":
    main()