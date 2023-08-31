"""
Mostrar por consola un cuadrado de XxY asteriscos, pidiendo X e Y al usuario

   ********************
   ********************
   ********************
   ********************
   ********************
   ********************
"""
def main():
    linea = ""
    num_filas = int(input("Intro num filas\n "))
    num_columnas  = int(input("Intro num columnas:\n"))

    for i in range(num_filas):
        for j in range(num_columnas):
            linea = linea + "*"
        print(linea)
        linea = ""


if __name__ == "__main__":
    main()
