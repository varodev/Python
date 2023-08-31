import math

def main():
    superficie_esfera = 0
    redondeo_inferior = 0
    redondeo_superior = 0
    radio_circ = int(input("Intro radio circunferencia: \n"))

    superficie_esfera = (4 * math.pi * math.pow(radio_circ,2))
    redondeo_inferior = math.floor(superficie_esfera)
    redondeo_superior = math.ceil(superficie_esfera)

    print(f"La superficie de la esfera es: {superficie_esfera}")
    print(f"Redondeado al inferior entero: {redondeo_inferior}")
    print(f"Redondeado al superior entero: {redondeo_superior}")

if __name__=="__main__":
    main()