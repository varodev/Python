from django.shortcuts import render, HttpResponse


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

def amigos(request):
    contenido_html = """<ul>
                            <li>Pedro</li>
                            <li>Luci</li>
                            <li>Lucas</li>
                            </ul>"""

    texto_html = cabecera_html + menu_html + contenido_html + cierre_cuerpo_html
    return HttpResponse(texto_html)

