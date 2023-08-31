
# Multiplicar una lista.

lista=[]
suma=0
multiplicacion=1
for x in range (10):
    numero=input("Inserte el número: ")
    numero=int(numero)
    lista.append(numero)
for x in lista:
    suma=suma + x
    multiplicacion=multiplicacion*x
resultadoSuma=suma   
print("Suma: " + str(resultadoSuma))
print("Multiplicacion: " + str(multiplicacion))
