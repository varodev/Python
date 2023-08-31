from tratamiento_imagen import Imagen

def main():
    nombre_fichero = ""
    fichero_imagen = "imagenes/atard_rojo.jpg"
    porcentaje_osc_brillo = float(input("Intro porcentaje a oscurecer y brillo:\n"))
    
    imagen = oscurecer_imagen(fichero_imagen, porcentaje_osc_brillo)

    if (input("Desea guardar la imagen en un fichero?\n") == "si"):
        nombre_fichero = input("Intro nombre fichero\n")
        imagen.grabar(nombre_fichero)

def oscurecer_imagen(path_imagen, porcentaje):
    imagen = Imagen(path_imagen)
    imagen.mostrar()

    for pixel in imagen:
        if (pixel.x < (imagen.width//2)):
            pixel.red = (pixel.red) - ((pixel.red) * porcentaje)
            pixel.green = (pixel.green) - ((pixel.green) * porcentaje)
            pixel.blue = (pixel.blue) - ((pixel.blue) * porcentaje)
        else:
            pixel.red = (pixel.red) + ((pixel.red) * porcentaje)
            pixel.green = (pixel.green) + ((pixel.green) * porcentaje)
            pixel.blue = (pixel.blue) + ((pixel.blue) * porcentaje)

    imagen.mostrar()
    return imagen

if __name__ == "__main__":
    main()