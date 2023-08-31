#Cuenta las vocales que tiene el texto de entrada
def contar_vocales(texto_entrada):
    cadena_vocales = "aeiou"
    contador_vocales = 0

    #Pasamos todo a minúsculas porque vamos a buscar sólo vocales minúsculas
    texto_minusculas = texto_entrada.lower()

    for contador in range(5):
        contador_vocales += texto_minusculas.count(vocal)
    
    return contador_vocales

#Indicar si el texto es largo. Consideramos texto largo si tiene más de 10 palabras.
def es_texto_largo(texto_entrada):
    texto_largo = False
    
    #Las palabras que tiene son el número de blancos + 1     
    if (texto_entrada.count(" ") > 10 ):
        texto_largo = True

    return texto_largo

# Devolver los N primeros caracteres del texto. Se debe comprobar si el texto tiene más de 
# N caracteres, en caso contrario se devolverá un error. La función debe devolver un texto 
# que incluya el número N. 
def obtener_n_primeros_caracteres(texto_entrada, num_caracteres):
    texto_salida = ""

    if (len(texto_entrada) < num_caracteres):
        texto_salida = "Error, el texto tiene menos de {} caracteres" 
    else: 
        texto_salida = "Los {} primeros caracteres son los siguientes" + texto_entrada[:num_caracteres]
       
    return (texto_salida.format(num_caracteres))

