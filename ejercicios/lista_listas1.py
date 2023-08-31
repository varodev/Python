def main():
    inversion_max = 0
    inversion_media = 0
    inversion_minima = 0
    lista_datos_usuario = []
    lista_inversiones_usuarios = []
    intro_datos = input("¿Desea introducir datos de un usuario (si/no)?")

    while (intro_datos == "si"): 
        inversion_max = input("Intro inversión max: \n")
        lista_datos_usuario.append(inversion_max)
        inversion_media = input("Intro inversión media: \n")
        lista_datos_usuario.append(inversion_media)
        inversion_minima = input("Intro inversión min: \n")
        lista_datos_usuario.append(inversion_minima)

        lista_inversiones_usuarios.append(lista_datos_usuario.copy())
        lista_datos_usuario.clear()

        intro_datos = input("¿Desea introducir datos de un usuario (si/no)?")

    print(lista_inversiones_usuarios)


if __name__ == "__main__":
    main()