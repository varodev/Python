#Array de números pares comprendidos entre el 1 y el 100, en orden ascendente.

lista=[]

def comprobarPar(x):
    if x % 2 == 0:
        #si es par, devuelve true
        return True
    else:
        return False

for x in range (100):
    numero=x+1
    esPar=comprobarPar(numero)
    if esPar:
        lista.append(numero)
print(lista)


        

