from paquete_modulos.modulo_circunferencia import calcular_longitud_circunferencia

def main():
    long_circunf = 0
    radio_circunf = int(input("Intro el radio de la circunf: \n"))

    long_circunf = calcular_longitud_circunferencia(radio_circunf)
    print(f"La longitud de la circunferencia es: {long_circunf}")

if __name__=="__main__":
    main()

    