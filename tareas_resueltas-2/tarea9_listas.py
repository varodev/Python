#Escribe un programa que reciba una lista y genere una lista 
# con los elementos en orden inverso.
def main():
    lista = [1,2,3,4,5,6,7,8,9,0]
    lista_inversa = invertir_lista(lista)
    print(lista_inversa)

def invertir_lista(lista_entrada):
    lista_salida = []

    for contador in range(len(lista_entrada)):
        elemento = lista_entrada.pop()
        lista_salida.append(elemento)

    return lista_salida




        
if __name__ == "__main__":
    main()