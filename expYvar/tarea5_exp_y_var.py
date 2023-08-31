def main():
    PESO_i54 = 200
    PESO_x28 = 75
    COSTE_i54 = 6
    COSTE_x28 = 3
    numero_de_x28 = 0
    numero_de_i54 = 0
    peso_total = 0
    coste_total = 0

    numero_de_i54 = int(input("Cuántos i54 tiene?: "))
    numero_de_x28 = int(input("Cuántos x28 tiene?: "))

    peso_total = (numero_de_i54 * PESO_i54)+(numero_de_x28 * PESO_x28)
    coste_total = (numero_de_i54 * COSTE_i54)+(numero_de_x28 * COSTE_x28)

    print(f"El peso del paquete es {peso_total}")
    print(f"El coste del paquete es {coste_total}")

if __name__ == "__main__":
    main()