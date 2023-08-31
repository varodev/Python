import webbrowser
import os

def main():
    crear_entrada = False
    diccionario_datos = {}
    nombre_fichero = ""

    crear_entrada = input("¿Desea añadir una nueva entrada al diccionario?s/n")
   
    while (crear_entrada == "s"):
        intro_elemento_en_diccionario(diccionario_datos)
        crear_entrada = input("¿Desea añadir una nueva entrada al diccionario?s/n")

    print(f"Diccionario final:  {diccionario_datos}")

    nombre_fichero = input("Intro nombre fichero html de salida\n")

    construir_fichero_html(diccionario_datos, nombre_fichero)

    fichero_html_salida = 'file:///' +os.getcwd()+'/' + nombre_fichero

    webbrowser.open_new(fichero_html_salida)
       
def intro_elemento_en_diccionario(diccionario):
    clave = input("Intro el nombre del equipo (clave), no puede haber repetidos\n")
    valor = input("Intro la puntuación asociada a la clave\n")

    diccionario[clave] = valor


def construir_fichero_html(diccionario, nombre_fichero):
    cabecera_html = """
                    <!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="utf-8">
                        <title>HTML</title>
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <style>
                            table, th, td {
                                border: 1px solid;
                                }
                        </style>
                    </head>
                        <body>
                        <h1> Tabla Liga </h1> 
                            <table>
                        \n"""
                            
    cierre_cuerpo_html = """
                    </table>
                    </body>
                    </html>"""
    
    
    with open(nombre_fichero,"w") as fichero_salida:
        fichero_salida.write(cabecera_html)

        for clave in diccionario:
                linea_fichero = "<tr><td>" + clave + "</td>" + "<td>" + (str(diccionario[clave]) + "</td> </tr>" + "\n")
                fichero_salida.write(linea_fichero)
        
        fichero_salida.write(cierre_cuerpo_html)      


if __name__ == "__main__":
    main()