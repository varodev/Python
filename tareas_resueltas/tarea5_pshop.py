from tratamiento_imagen import Imagen

def main():
    x_pixel = 0
    y_pixel = 0
    fichero_imagen_plano_1 = "imagenes/atardecer.jpg"
    fichero_imagen_plano_2 = "imagenes/colores.jpeg"
    tam_bloque = int(input("Intro tamaño del cuadrado:\n"))
    
    imagen = insertar_cuadrados_imagen(fichero_imagen_plano_1,fichero_imagen_plano_2,tam_bloque)

    if (input("Desea guardar la imagen en un fichero?\n") == "si"):
        nombre_fichero = input("Intro nombre fichero\n")
        imagen.grabar(nombre_fichero)

def insertar_cuadrados_imagen(path_imagen_plano_1,path_imagen_plano_2,tam_bloque):
    salir = False
    x_pixel = 0
    y_pixel = 0
    pixel = None
    imagen_plano_1 = Imagen(path_imagen_plano_1)
    imagen_plano_2 = Imagen(path_imagen_plano_2)

    imagen_plano_1.mostrar()
    imagen_plano_2.mostrar()

    while (not salir):
        for cont_x in range(x_pixel,x_pixel + tam_bloque):
            for cont_y in range(y_pixel, y_pixel + tam_bloque):
                if (cont_x < imagen_plano_1.width) and (cont_x < imagen_plano_1.width): 
                    pixel = imagen_plano_2.get_pixel(cont_x,cont_y)
                    imagen_plano_1.set_rgb(cont_x, cont_y,pixel.red,pixel.green,pixel.blue)
                else:
                    salir = True
                
        imagen_plano_1.mostrar()
        x_pixel += 2 * tam_bloque

        if (x_pixel > imagen_plano_1.width):
            salir = True

    return imagen_plano_1

if __name__ == "__main__":
    main()