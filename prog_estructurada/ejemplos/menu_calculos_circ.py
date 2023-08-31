import paquete_modulos.modulo_circunferencia

def main():
    radio_circ = 0
    resultado = 0
    opcion_elegida = 0

    while(opcion_elegida != 4):

        mostrar_menu()
        opcion_elegida = int(input("Elija una opción de menú: \n"))

        if (opcion_elegida == 1):
            radio_circ = int(input("Intro radio circunf: \n"))
            resultado = paquete_modulos.modulo_circunferencia.calcular_longitud_circunferencia(radio_circ)
            print(f"La longitud de la circunferencia es: {resultado}")
        elif(opcion_elegida == 2):
            radio_circ = int(input("Intro radio circulo: \n"))
            resultado = modulo_circunferencia.calcular_area_circulo(radio_circ)
            print(f"La superficie del circulo es: {resultado}")
        elif(opcion_elegida == 3):
            radio_circ = int(input("Intro radio esfera: \n"))
            resultado = modulo_circunferencia.calcular_area_circulo(radio_circ)
            print(f"La superficie de la esfera es: {resultado}")
        elif(opcion_elegida == 4):
            print("Adios")
        else:
            print("Opción errónea")

        
def mostrar_menu():
    print("""Programa calculos trigonométricos:
            1. Calcular longitud de la circunferencia
            2. Calcular área del círculo
            3. Calcular área de la esfera
            4. Salir
            """)

if __name__=="__main__":
    main()

    