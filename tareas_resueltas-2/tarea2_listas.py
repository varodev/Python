
def main():
    lista_numeros = [1,4,5,8,9,13]
    sumatorio = 0

    for elemento in lista_numeros:
        sumatorio+=elemento
    
    print(f"La suma es {sumatorio}")

if __name__ == "__main__":
    main()