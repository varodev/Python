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

def calculadora(request):
    numero_1 = 0
    numero_2 = 0
    operacion = ""
    resultado = 0

    if request.method == 'GET':
        if "numero_1" in request.GET and "numero_2" in request.GET and "operacion" in request.GET:
            if ( (request.GET["numero_1"] is not None) and (request.GET["numero_2"] is not None) ):
                numero_1 = int(request.GET["numero_1"])
                numero_2 = int(request.GET["numero_2"])

                operacion = request.GET["operacion"]
                if (operacion == "+"):
                    resultado = numero_1 + numero_2
                elif(operacion == "-"):
                    resultado = numero_1 - numero_2
                elif(operacion == "*"):
                    resultado = numero_1 * numero_2
                elif(operacion == "/"):
                    resultado = numero_1 / numero_2
                else:
                    resultado = 0
    
    html_caja_resultados = f"""<div id="div_resultado">
                           <h1>{resultado}</h1>
                        </div>"""

    html_formulario_operacion = f"""
                    <form action="/calculadora">
                        <label for="num1">Número 1:</label><br>
                        <input type="text" id="num1" name="numero_1" value="0"><br><br>
                        <label for="num2">Número 2:</label><br>
                        <input type="text" id="num2" name="numero_2" value="0"><br><br>
                        <label for="op">Selecciona operación:</label><br>
                        <select name="operacion" id="op">
                            <option value="+">+</option>
                            <option value="-">-</option>
                            <option value="*">*</option>
                            <option value="/">/</option>
                        </select><br>

                        <input type="submit" value="Submit">
                        </form>
                    """

    
    texto_final_html = cabecera_html + menu_html + html_caja_resultados + html_formulario_operacion + cierre_cuerpo_html
    return HttpResponse(texto_final_html)

    