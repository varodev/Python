#Array de números comprendidos entre el 1 y el 100, en orden descendente.

lista=[]
for x in range (100):
    lista.append(x+1)
lista.reverse()
print(lista)
