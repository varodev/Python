"""
Realizad un programa que pida al usuario dos números. El programa mostrará todos
 los números entre esos dos que sean divisibles por 4 pero no por 5
"""

def main():
    numero_menor = int(input("Intro num menor: \n"))
    numero_mayor = int(input("Intro número mayor: \n"))

    for contador in range(numero_menor, numero_mayor):
        if ((contador % 4) == 0) and (not((contador%5) == 0)):
            print((contador))

if __name__ == "__main__":
    main()


