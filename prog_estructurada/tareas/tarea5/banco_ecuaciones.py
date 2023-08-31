#from modulos.modulo_ecuaciones import calcular_ganancia_bono
import modulos.modulo_ecuaciones as ecuaciones
interes = 2
anios = 5

dinero_cliente = 0
ganancia_bono = 0
intereses_inversion = 0
dividendos = 0
salir = False

while (not salir):
    opcion = input("""\n Introduzca una de las siguientes opciones: 
            a: Calcular ganancia del Bono
            b: Calcular el interés de la inversión
            c: Calcular los dividendos
            d: Salir
            """)
    
    if (opcion == "a"):
        dinero_cliente = int(input("Introduca el dinero del cliente: \n"))
        ganancia_bono = ecuaciones.calcular_ganancia_bono(dinero_cliente,interes) 
        print(f"Para la cantidad {dinero_cliente} euros tenemos unas ganancias en bonos de {ganancia_bono} euros \n")
    elif (opcion == "b"):
        dinero_cliente = int(input("Introduca el dinero del cliente: \n"))
        intereses_inversion = ecuaciones.calcular_interes_inversion(dinero_cliente,anios)
        print(f"Para la cantidad {dinero_cliente} euros tenemos unos intereseses de inversión de {intereses_inversion} \n")
    elif (opcion == "c"):
        dinero_cliente = int(input("Introduca el dinero del cliente: \n"))
        dividendos = ecuaciones.calcular_dividendos_accionista(dinero_cliente,anios)
        print(f"Para la cantidad {dinero_cliente} euros tenemos unos dividendos de {dividendos} euros \n")
    elif (opcion == "d"):
        salir = True
    else:
        print(f"Opción errónea")

    
    
    
    
    