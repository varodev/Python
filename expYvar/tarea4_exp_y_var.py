def main():
    dinero_inicial = 0
    interes = 0
    intereses_anuales = 0
    dinero_total_final = 0
    años = 0

    print ("Inntroduzca el dinero que tiene:")
    dinero_inicial = int(input())

    print ("Introduzca el interés:")
    interes = int(input())

    print ("Introduzca el número de años:")
    años = int(input())

    intereses_anuales = (dinero_inicial*(interes/100))

    ganancia_anual = intereses_anuales + dinero_inicial

    dinero_total_final = ganancia_anual * años

    print(f"El dineo que tiene al final es: {dinero_total_final}")

if __name__ == "__main__":
    main()