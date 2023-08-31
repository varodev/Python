#Array de números impares comprendidos entre el 1 y el 100, en orden ascendente.

lista=[]

def comprobarPrimo(entero):
    esPrimo=True
    for x in range (entero - 2):
        #print(x+2)
        if entero%(x+2)==0:
            esPrimo=False
    return esPrimo


for x in range(100):
    numero=x+1
    esPrimo=comprobarPrimo(numero)
    if esPrimo:
        lista.append(numero)
print(lista)


        

