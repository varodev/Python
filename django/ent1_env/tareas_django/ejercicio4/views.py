from django.shortcuts import render, HttpResponse
from modulo_sopa_letras.sopa_letras import leer_sopa_letras,leer_soluciones_sopa_letras

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

def mostrar_sopa_letras(request):
    html_tabla_sopa_letras = ""
    html_texto_resultado = ""

    resultados_sopa_letras = leer_soluciones_sopa_letras()

    sopa_letras = leer_sopa_letras()
    
    for elemento in sopa_letras:
        html_tabla_sopa_letras+="<tr>"
        for letra in elemento:
            html_tabla_sopa_letras+=f"<td>{letra}</td>"
        html_tabla_sopa_letras+="</tr>"

    html_tabla_sopa_letras = f"""<div id="tabla">
                           <table>{html_tabla_sopa_letras}</table>
                        </div>"""

    html_formulario_solucion_sopa = f"""
                    <form action="/sopa_letras">
                        <label for="palabra">Escriba la palabra encontrad:</label><br>
                        <input type="text" id="palabra" name="palabra" value="-"><br><br>
                        <input type="submit" value="Submit">
                        </form>
                    """

    if request.method == 'GET':
        if "palabra" in request.GET:
            if (request.GET["palabra"] is not None):
                print(resultados_sopa_letras)
                print(request.GET["palabra"])
                if request.GET["palabra"] in resultados_sopa_letras:
                    html_texto_resultado = f'<h1> {request.GET["palabra"]} está en la sopa de letras</h1>'
                else:
                    html_texto_resultado = f'<h1> {request.GET["palabra"]} NO está en la sopa de letras</h1>'
    
    texto_final_html = cabecera_html + menu_html + html_tabla_sopa_letras + html_formulario_solucion_sopa + html_texto_resultado+cierre_cuerpo_html
    return HttpResponse(texto_final_html)

    