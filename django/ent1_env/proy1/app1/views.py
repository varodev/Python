from django.shortcuts import render, HttpResponse
import datetime
import os

# Create your views here.

def home(request):
    return HttpResponse("<h1>Mi primera app Django</h1>")

def nosotros(request):
    return HttpResponse("<h1>¡Somos DAW 1!</h1>")

def nuestra_imagen(request):
    cabecera_html = """
                    <!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="utf-8">
                        <title>HTML</title>
                        <link rel="stylesheet" href="/static/css/proy1.css">
                    </head>
                        <body>"""                        
    cierre_cuerpo_html = """
                    </body>
                    </html>"""
    fecha =  datetime.datetime.now()
    html_imagen = '<img src="/static/img/nuestra_imagen.jpg" alt="Nosotros">'

    html_fecha = f"""
                    <div id="marco_fecha">
                       {fecha}
                    </div>
                    """
    texto_final_html = cabecera_html + html_imagen + html_fecha + cierre_cuerpo_html
    return HttpResponse(texto_final_html)

def prueba(request):
    cont_tabla = ""
    for elemento in request.META.items():
        cont_tabla += f"""<tr><td>{elemento[0]} </td><td>{elemento[1]}</td></tr>"""

    return HttpResponse("<table>" + cont_tabla + "</table>")

def consulta(request):
    cabecera_html = """
                    <!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="utf-8">
                        <title>HTML</title>
                        <link rel="stylesheet" href="/static/css/proy1.css">
                    </head>
                        <body>"""                        
    cierre_cuerpo_html = """
                    </body>
                    </html>"""
    formulario_html =  """
                        <form action="/saludar">
                        <label for="fname">First name:</label><br>
                        <input type="text" id="fname" name="nombre" value="Pepa"><br>
                        <input type="submit" value="Submit">
                        </form>
    
                        """
    

    texto_final_html = cabecera_html + formulario_html + cierre_cuerpo_html

    return HttpResponse(texto_final_html)

def saludar(request):
    cabecera_html = """
                    <!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="utf-8">
                        <title>HTML</title>
                        <link rel="stylesheet" href="/static/css/proy1.css">
                    </head>
                        <body>"""  
    
    cierre_cuerpo_html = """
                    </body>
                    </html>"""

    nombre_usuario = ""

    if request.method == 'GET':
        #Comprobamos si en el diccionario request.GET hay una clave "nombre"
        if "nombre" in request.GET:
            if (request.GET["nombre"] is not None): 
                nombre_usuario = request.GET["nombre"]


    contenido_pagina =  cabecera_html + "<h1> Hola " + nombre_usuario + "</h1>" + cierre_cuerpo_html           
    
    texto_final_html = cabecera_html + contenido_pagina + cierre_cuerpo_html

    return HttpResponse(texto_final_html)