from paquete_modulos.modulo_circunferencia import calcular_longitud_circunferencia as calc_long_circ

def main():
    long_circunf = 0
    radio_circunf = int(input("Intro el radio de la circunf: \n"))

    long_circunf = calc_long_circ(radio_circunf)
    print(f"La longitud de la circunferencia es: {long_circunf}")

if __name__=="__main__":
    main()

    