def main():
    lista_datos_usuario = crear_lista_usuario()
    print(f"La lista creada por el usuario es: {lista_datos_usuario}")
    lista_factoriales = crear_lista_factorial(lista_datos_usuario)
    print(f"La lista de factoriales es: {lista_factoriales}")

def crear_lista_usuario():
    lista_datos = []
    finalizar = False

    while (not finalizar):
        dato = input("Indique elemento a introducir en la lista: \n")
        if (dato == "FIN"):
            finalizar = True
        else:
            lista_datos.append(int(dato))
        
    return lista_datos

def crear_lista_factorial(lista_numeros):
    lista_salida = []

    for elemento in lista_numeros:
        factorial_num = calcular_factorial(elemento)
        lista_salida.append(factorial_num)
    
    return lista_salida

def calcular_factorial(numero):
    resultado = 1

    for i in range(1,numero+1):
        resultado = resultado * i
    return resultado

if __name__ == "__main__":
    main()