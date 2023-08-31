def main():
    #Es una práctica declarar variables y constantes al principio
    #Las constantes las ponemos en mayúscula
    JORNADAS_MENSUALES = 20 
    NUM_MESES_ANIO = 12

    salario_mensual = 0
    salario_anual = 0
    num_horas_jornada = 0
    coste_hora = 0

    num_horas_jornada = int(input("Introduzca el número de horas de su jornada laboral: \n"))
    coste_hora = int(input("Introduzca el coste por hora"))

    salario_mensual = (num_horas_jornada * coste_hora) * JORNADAS_MENSUALES
    salario_anual = salario_mensual * NUM_MESES_ANIO

    print(f"Salario mensual: {salario_mensual}. Salario anual: {salario_anual}")

if __name__ == "__main__":
    main()