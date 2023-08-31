
def main():
    anio_usuario = int(input("Intro el año: \n"))
    es_bisiesto = False

    while (anio_usuario != 0):
        es_bisiesto = comprobar_si_anio_bisiesto(anio_usuario)

        if (es_bisiesto):
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")

        anio_usuario = int(input("Intro el año: \n"))


def comprobar_si_anio_bisiesto(anio_entrada):
    resultado = False

    if  (((anio_entrada%4) == 0) and (anio_entrada%100!=0)) or ((anio_entrada % 400) == 0):
        resultado = True
    else:
        resultado = False 
    
    return resultado

if __name__=="__main__":
    main()

    