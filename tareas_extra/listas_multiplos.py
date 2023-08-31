
def main():
    lista_numeros = [4,3,78,45,6,99]
    finalizar = False
    
    while (not finalizar):
        num_usuario = int(input("Intro número del que quiere sus múltiplos: \n"))
        if (num_usuario == 0):
            finalizar = True
        else:
            lista_multiplos = generar_lista_multiplos((lista_numeros), num_usuario)
            print(f"La lista de números interna es: {lista_numeros}")
            print(f"La lista de múltipos de {num_usuario} es: {lista_multiplos}")


def generar_lista_multiplos(lista_num, numero):
    lista_salida = []
    for elemento in lista_num:
        if (elemento % numero) == 0:
            lista_salida.append(elemento)
    
    return lista_salida

if __name__ == "__main__":
    main()