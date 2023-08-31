import mysql.connector
from mysql.connector import Error
import webbrowser
import os

def insertarSerie(codigoSerie,titulo,numTemporadas,enlace,miConexBBDD,miCursor):

    try:
        consultaBBDD = ("INSERT INTO series VALUES ({},'{}',{},'{}')")
        miCursor.execute(consultaBBDD.format(codigoSerie,titulo,numTemporadas,enlace))
        miConexBBDD.commit() #Comprobar que es coherente la inserccion.
        print(f"Se han insertado {miCursor.rowcount} registros")

    except Error as errorProducido:
        print(f"Se ha producido un error al insertar una serie en la BBDD:{errorProducido}")

    finally:
        miCursor.close()
        miConexBBDD.close()



def insertarActor(codigoPersona,nombre,apellidos,fecNac,nacionalidad,miConexBBDD,miCursor,titulo,rol):

    try:
        consultaBBDD = ("INSERT INTO personas VALUES ({},'{}','{}','{}','{}')")
        miCursor.execute(consultaBBDD.format(codigoPersona,nombre,apellidos,fecNac,nacionalidad))
        miConexBBDD.commit() #Comprobar que es coherente la inserccion.
        print(f"Se han insertado {miCursor.rowcount} registros")
        insertar_tercera_tabla(titulo,codigoPersona,rol,miConexBBDD,miCursor)
    except Error as errorProducido:
        print(f"Se ha producido un error al insertar una persona en la BBDD:{errorProducido}")

    finally:
        miCursor.close()
        miConexBBDD.close()




def insertar_tercera_tabla(titulo,cod_actor,rol,miConexBBDD,miCursor):
    try:
        cod_serie = buscar_codigo_serie(titulo,miCursor,miConexBBDD)
        consultaBBDD = ("INSERT INTO seriespersonas VALUES ({},{},'{}')")
        miCursor.execute(consultaBBDD.format(cod_serie,cod_actor,rol))
        miConexBBDD.commit() #Comprobar que es coherente la inserccion.
        print(f"Se han insertado {miCursor.rowcount} registros")

    except Error as errorProducido:
        print(f"Se ha producido un error al insertar una persona en la BBDD:{errorProducido}")

def buscar_codigo_serie(titulo,miCursor,miConexBBDD):
    try:
        consulta = f"SELECT cod_serie FROM series WHERE titulo = '{titulo}'"
        miCursor.execute(consulta)
        datos = miCursor.fetchall()
        tupla_serie = datos[0]
        cod_serie = tupla_serie[0]


    except Error as errorProducido:
        print(f"Se ha producido un error, no tenemos esa serie en la BBDD:{errorProducido}")
        miCursor.close()
        miConexBBDD.close()

    return cod_serie

def consultarDatos(consulta,miConexBBDD,miCursor):

    try:
        miCursor.execute(consulta)
        datos = miCursor.fetchall()

    except Error as errorProducido:
        print(f"Se ha producido un error al acceder a las series de la BBDD:{errorProducido}")

    finally:
        miCursor.close()
        miConexBBDD.close()

    return datos


def construirListadoSeries(consulta,miConexBBDD,miCursor):

    try:
        miCursor.execute(consulta)
        datos = miCursor.fetchall()
        

    except Error as errorProducido:
        print(f"Se ha producido un error al acceder a las series de la BBDD:{errorProducido}")

    finally:
        miCursor.close()
        miConexBBDD.close()

    if (datos == []):
        print("No disponemos de esa serie")
    else:
        construir_Fichero(datos)


def construir_Fichero(datos):
        nombreFichero = input("Nombre del fichero:\n")
        #Para guardar el fichero
        fichero_html = 'file:///' +os.getcwd()+ '/' + nombreFichero + ".html"

        cabeceraHtml="""
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
                </head>
                <body>
                <h1>Listado de series:</h1>
                <table border = "1">"""
        cuerpoHtml = """ 
                </table>
                </body>
                </html>"""   

        with open(nombreFichero + ".html" ,"w") as fichero_salida:
            fichero_salida.write(cabeceraHtml)
            fichero_salida.write("<tr><th>Titulo</th><th>Numero de Temporadas</th><th>Enlace</th><tr>")
            for elemento in datos:
                #titulo,numTemporadas,director,listaActores,enlace
                titulo = elemento[1]
                numTemporadas = str(elemento[2])
                enlace = elemento[3]
                fichero_salida.write("<tr><td>" + titulo + "</td><td>" + numTemporadas + "</td><td>" +  enlace + "</td></tr>")
            fichero_salida.write(cuerpoHtml)

        webbrowser.open_new(fichero_html)


def buscarSerieActor(consulta,miConexBBDD,miCursor):
    try:
        miCursor.execute(consulta)
        datos = miCursor.fetchall()

    except Error as errorProducido:
        print(f"Se ha producido un error al acceder a la BBDD:{errorProducido}")

    finally:
        miCursor.close()
        miConexBBDD.close()
        
    return datos



def buscarSerieActorPagina(consulta,miConexBBDD,miCursor):
    try:
        miCursor.execute(consulta)
        datos = miCursor.fetchall()

    except Error as errorProducido:
        print(f"Se ha producido un error al acceder a la BBDD:{errorProducido}")

    finally:
        miCursor.close()
        miConexBBDD.close()
    
    if (datos == []):
            print("No disponemos de esa serie")
    else:
        construir_Fichero_Serie_Actor(datos)

def construir_Fichero_Serie_Actor(datos):
    nombreFichero = input("Nombre del fichero:\n")
    #Para guardar el fichero
    fichero_html = 'file:///' +os.getcwd()+ '/' + nombreFichero + ".html"

    cabeceraHtml="""
        <!DOCTYPE html>
        <html lang="es">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            </head>
            <body>
            <h1>Listado de series:</h1>
            <table border = "1">"""
    cuerpoHtml = """ 
            </table>
            </body>
            </html>"""   
        
    with open(nombreFichero + ".html" ,"w") as fichero_salida:
        fichero_salida.write(cabeceraHtml)
        for elemento in datos:
            #titulo,numTemporadas,director,listaActores,enlace
            titulo = elemento[0]
            enlace = elemento[1]
            fichero_salida.write("<tr><td>" + titulo + "</td><td><a href='" + enlace + "'>Enlace</a></td></tr>")
        fichero_salida.write(cuerpoHtml)

    webbrowser.open_new(fichero_html)


