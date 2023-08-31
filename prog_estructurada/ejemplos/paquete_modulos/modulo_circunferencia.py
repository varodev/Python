import math

def calcular_area_circulo(radio_circunferencia):
    resultado = math.pi * (math.pow(radio_circunferencia, 2))

    return resultado

def calcular_longitud_circunferencia(radio_circunferencia):
    resultado = 2 * math.pi * radio_circunferencia
    return resultado  
    
def calcular_area_esfera(radio_esfera):
    resultado = 4 * math.pi * (math.pow(radio_esfera, 2))

    return resultado

