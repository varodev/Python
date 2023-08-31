
# ej.15c – Números pares e impares con función: 


def multiplicarDos(numero):
    resultado=numero*2
    return resultado

def comprobarPar(numero):
    if numero%2==0:
        return True
    else:
        return False

print("Inserte un número:")
minumero=int(input())
resultado=comprobarPar(minumero)
if resultado:
    print("El número " + str(minumero) + " es par")
else:
    print("El número " + str(minumero) + " es impar") 
