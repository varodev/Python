from tratamiento_imagen import Imagen

def main():
    nombre_fichero = ""
    fichero_imagen_plano_1 = "imagenes/ventana.png"
    fichero_imagen_plano_2 = "imagenes/mar.jpg"
    
    
    imagen = hacer_mascara_imagen(fichero_imagen_plano_1, fichero_imagen_plano_2)

    if (input("Desea guardar la imagen en un fichero?\n") == "si"):
        nombre_fichero = input("Intro nombre fichero\n")
        imagen.grabar(nombre_fichero)

def hacer_mascara_imagen(path_imagen_plano_1, path_imagen_plano_2):
    pixel_imagen_plano_2 = None #Las variables para objetos complejos las podemos inicializar a None
    imagen_plano_1 = Imagen(path_imagen_plano_1)
    imagen_plano_2 = Imagen(path_imagen_plano_2)

    imagen_plano_1.mostrar()
    imagen_plano_2.mostrar()

    for pixel in imagen_plano_1:
        if es_pixel_claro(pixel):
            pixel_imagen_plano_2 = imagen_plano_2.get_pixel(pixel.x, pixel.y)
            pixel.red = pixel_imagen_plano_2.red
            pixel.green = pixel_imagen_plano_2.green
            pixel.blue = pixel_imagen_plano_2.blue

    imagen_plano_1.mostrar()
    return imagen_plano_1

def es_pixel_claro(pixel_a_chequear):
    UMBRAL_CLARO = 200
    resultado = False

    if ((pixel_a_chequear.red > UMBRAL_CLARO) and 
        (pixel_a_chequear.green > UMBRAL_CLARO) and
        (pixel_a_chequear.blue > UMBRAL_CLARO)):
        resultado  = True

    return resultado

if __name__ == "__main__":
    main()