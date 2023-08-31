def main():
    inversion_max = 0
    inversion_media = 0
    inversion_minima = 0
    lista_datos_usu = []
    lista_inversiones_usuarios = []
    intro_datos = input("¿Desea introducir datos de un usuario (si/no)?")

    while (intro_datos == "si"): 
        
        lista_datos_usu = construir_lista_inversion()
        lista_inversiones_usuarios.append(lista_datos_usu)
        intro_datos = input("¿Desea introducir datos de un usuario (si/no)?")

    print(lista_inversiones_usuarios)

def construir_lista_inversion():
    lista_datos_usuario = []
    inversion_max = input("Intro inversión max: \n")
    lista_datos_usuario.append(inversion_max)
    inversion_media = input("Intro inversión media: \n")
    lista_datos_usuario.append(inversion_media)
    inversion_minima = input("Intro inversión min: \n")
    lista_datos_usuario.append(inversion_minima)

    return lista_datos_usuario

if __name__ == "__main__":
    main()