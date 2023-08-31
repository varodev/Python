
def main():
    lista_equipos = ["R. Vallecano","Numancia", "Teruel"]

    equipo_a_buscar  = input("¿Qué equipo quiere buscar en la lista?\n")

    if (equipo_a_buscar in lista_equipos):
        print("El equipo está en la lista")
    else:
        print("El equipo no está en la lista")

if __name__ == "__main__":
    main()