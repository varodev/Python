from tratamiento_imagen import Imagen

def main():
    nombre_fichero = ""
    fichero_imagen = "imagenes/atard_rojo.jpg"
    cantidad_red_rgb = int(input("Cuánto quiere reducir el RGB?\n"))

    imagen = oscurecer_imagen(fichero_imagen, cantidad_red_rgb)

    if (input("Desea guardar la imagen en un fichero?\n") == "si"):
        nombre_fichero = input("Intro nombre fichero\n")
        imagen.grabar(nombre_fichero)

def oscurecer_imagen(path_imagen, cantidad_reduccion):
    imagen = Imagen(path_imagen)
    imagen.mostrar()

    for pixel in imagen:
        pixel.red = (pixel.red) - cantidad_reduccion
        pixel.green = (pixel.green) - cantidad_reduccion
        pixel.blue = (pixel.blue) - cantidad_reduccion

    imagen.mostrar()
    return imagen


if __name__ == "__main__":
    main()