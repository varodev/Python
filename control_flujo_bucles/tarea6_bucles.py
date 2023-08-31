"""Realizad un programa que vaya pidiendo números al usuario hasta llegar a 10 números pedidos.
 Cada vez que el usuario introduzca un número le irá mostrando la media de los números 
 introducidos hasta ese momento.
"""

def main():
    numero_usuario = 0
    suma = 0
    media = 0

    for i in range(1,11):
        numero_usuario = int(input("Intro num: \n"))
        suma += numero_usuario
        media = suma/i

        print(f"Ha introducido {i} números, la suma es {suma} y la media {media}")

if __name__ == "__main__":
    main()