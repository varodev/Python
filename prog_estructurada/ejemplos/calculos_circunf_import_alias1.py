import paquete_modulos.modulo_circunferencia as calculos_trigonometricos

def main():
    long_circunf = 0
    radio_circunf = int(input("Intro el radio de la circunf: \n"))

    long_circunf = calculos_trigonometricos.calcular_longitud_circunferencia(radio_circunf)
    print(f"La longitud de la circunferencia es: {long_circunf}")

if __name__=="__main__":
    main()

    