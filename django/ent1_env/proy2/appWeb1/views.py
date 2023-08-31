# Create your views here.

from django.shortcuts import render, HttpResponse
import datetime
import os

cabecera_html = """
                    <!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="utf-8">
                        <title>HTML</title>
                        <link rel="stylesheet" href="/static/css/proy2.css">
                    </head>
                        <body>"""                        
cierre_cuerpo_html = """
                    </body>
                    </html>"""

menu_html = """
            <ul>
                <li> <a href="/"> Inicio </a></li>
                <li> <a href="/about/"> Nosotros </a></li>
                <li> <a href="/imagen/"> Nuestra Imagen </a></li>
            </ul>

                """

def home(request):
    contenido_html = "<h1>Mi primera app con Menú</h1>"
    texto_html = cabecera_html + menu_html + contenido_html + cierre_cuerpo_html
    return HttpResponse(texto_html)

def nosotros(request):
    contenido_html = "<h1>¡Somos DAW 1!</h1>"
    texto_html = cabecera_html + menu_html + contenido_html + cierre_cuerpo_html
    return HttpResponse(texto_html)

def nuestra_imagen(request):
    fecha =  datetime.datetime.now()
    html_imagen = '<img src="/static/img/nuestra_imagen.jpg" alt="Nosotros">'

    html_fecha = f"""
                    <div id="marco_fecha">
                       {fecha}
                    </div>
                    """
    texto_html = cabecera_html + menu_html + html_imagen + html_fecha + cierre_cuerpo_html
    return HttpResponse(texto_html)

    