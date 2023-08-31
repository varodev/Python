
def calcular_ganancia_bono(dinero, interes):
    return ( (dinero * ( interes**3)) + ( 2*(interes**4))  )

def calcular_interes_inversion(dinero, anios):
    return (((dinero/20000)) * anios)

def calcular_dividendos_accionista(dinero_invertido, anios):
    return (dinero_invertido * (anios/25))