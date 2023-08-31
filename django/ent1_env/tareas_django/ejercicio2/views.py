from django.shortcuts import render, HttpResponse

import datetime


cabecera_html = """
                    <!DOCTYPE html>
                    <html lang="es">
                    <head>
                        <meta charset="utf-8">
                        <title>HTML</title>
                        <link rel="stylesheet" href="/static/css/tareas_django.css">
                    </head>
                        <body>"""                        
cierre_cuerpo_html = """
                    </body>
                    </html>"""
menu_html = """<div id="menu">
            <ul>
                <li> <a href="/amigos/"> Ejercicio 1 </a></li>
                <li> <a href="/imagenes/"> Ejercicio 2 </a></li>
                <li> <a href="/calculadora/"> Ejercicio 3 </a></li>
                <li> <a href="/sopa_letras/"> Ejercicio 4 </a></li>
            </ul>
            </div>
                """

def imagenes(request):
    fecha =  datetime.datetime.now()
    html_imagen_div_1 = """<div id="div_imagen_1">
                           <img src="/static/img/django_1.jpg" alt="Nosotros">
                        </div>"""

    html_fecha_1 = f"""
                    <div id="marco_fecha_1">
                        <p>
                            {fecha.strftime("%c")}
                        </p>
                    </div>
                    """

    html_imagen_div_2 = """<div id="div_imagen_2">
                           <img src="/static/img/django_2.jpg" alt="Nosotros">
                        </div>"""

    html_fecha_2 = f"""
                    <div id="marco_fecha_2">
                        <p>
                            {fecha.strftime("%x")}
                        </p>
                    </div>
                    """
    texto_final_html = cabecera_html + menu_html + html_imagen_div_1 + html_fecha_1 + html_imagen_div_2 + html_fecha_2 + cierre_cuerpo_html
    return HttpResponse(texto_final_html)

    