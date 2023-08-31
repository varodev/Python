#Sopa de letras
NUM_LINEA_FIN_SOPA = 7

def leer_sopa_letras():
    
    sopa_letras = []
    contador = 0

    with open("/Users/juanluisballesterosfernande/Documents/JROtero/JROtero/clases/DAW/DAW-21-22/presencial/FundProgramación/ejemplosSintaxis/django/ent1_env/tareas_django/static/txt/sopa_letras.txt") as fichero_entrada:
        for linea in fichero_entrada:
            if contador < NUM_LINEA_FIN_SOPA:
                lista_letras = linea[:-1].split(" ")
                sopa_letras.append(lista_letras)

            contador+=1
    return sopa_letras

def leer_soluciones_sopa_letras():
    solucion_sopa_letras = []
    contador = 0

    with open("/Users/juanluisballesterosfernande/Documents/JROtero/JROtero/clases/DAW/DAW-21-22/presencial/FundProgramación/ejemplosSintaxis/django/ent1_env/tareas_django//static/txt/sopa_letras.txt") as fichero_entrada:
        for linea in fichero_entrada:
            if contador > NUM_LINEA_FIN_SOPA:
                solucion_sopa_letras.append(linea[:-1])
            
            contador+=1

    return solucion_sopa_letras
