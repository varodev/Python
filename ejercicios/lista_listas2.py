#Sopa de letras

def main():
    sopa_letras = []

    with open("sopa_letras.txt") as fichero_entrada:
        for linea in fichero_entrada:
            lista_letras = linea[:-1].split(" ")
            sopa_letras.append(lista_letras)
            print(lista_letras)

    mostrar_diagonal_principal(sopa_letras)  
    print("----")
    mostrar_diagonal_secundaria(sopa_letras) 
    print("----")
    mostrar_primera_fila(sopa_letras)
    print("----")
    mostrar_ultima_fila(sopa_letras)

def mostrar_diagonal_principal(matriz):
    for i in range(len(matriz)):
        print(matriz[i][i])

def mostrar_diagonal_secundaria(matriz):
    for i in range(len(matriz)):
        print(matriz[(len(matriz)-1)-i][i])

def mostrar_primera_fila(matriz):
    for i in range(len(matriz)):
        print(matriz[0][i])

def mostrar_ultima_fila(matriz):
    for i in range(len(matriz)):
        print(matriz[len(matriz)-1][i])
if __name__ == "__main__":
    main()