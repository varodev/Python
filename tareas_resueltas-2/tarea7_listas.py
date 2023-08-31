#Este programa recorre una lista de números en la que puede haber
#elementos repeticos y genera una lista en la que aparecen los números
#sin repetir
def main():
    lista_numeros = [3,5,67,2,2,32,3,5,5,3,3,44,55,2]
    lista_sin_dup = []

    for elemento in lista_numeros:
        if not(elemento in lista_sin_dup):
            lista_sin_dup.append(elemento)

    print(lista_numeros)
    print(lista_sin_dup)
        
if __name__ == "__main__":
    main()