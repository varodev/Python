def main():
    cif_usuario = input("Intro CIF: \n")

    parte_numerica = cif_usuario[:8]
    letra = cif_usuario[8:]

    print(f"Parte numérica: {parte_numerica}. Letra: {letra}")

if __name__=="__main__":
    main()