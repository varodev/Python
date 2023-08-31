#Numeros primos del 1 al 100
numero=0
lista=[]
lista.clear()

def comprobarPar(x):
    if x % 2 == 0:
        #Si es par, devuelve true
        return True
    else:
        return False

def imprimirNumero(y):
    for x in range(y):
        #if 
        print(x+2)

      

for x in range (100):
    numero=x+1
    esPrimo=comprobarPar(numero)
    if esPrimo:
        lista.append(numero)

"""
listanumerosprimos=[]

def Numeroprimo(y):
    for z in range (y):
        if y%z==0:
            return True

for x in range (100):
    if Numeroprimo(x):
        listanumerosprimos.append(x)

print(listanumerosprimos)
"""
