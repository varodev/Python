
#A partir de una lista de números interna se debe mostrar la suma de todos los números 
# múltiplos de 2 y de 4 a la vez. 
def main():
    sumatorio = 0
    lista_numeros = [23,44,2,1,6,7,23,8,12,44,22,54]

    for elemento in lista_numeros:
        if ( (elemento % 2) == 0) and((elemento % 4) == 0):
            sumatorio += elemento
            print(elemento)

    print(f"La suma de números múltiplos de 2 y 4 a la vez es: {sumatorio}")

if __name__ == "__main__":
    main()