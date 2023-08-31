#Programa que nos informa si un número entero es múltiplo de 2 y 3.

print("Inserte un número entero:")
numero=int(input())

esDivisible3=(numero%3==0) #Se almacena como booleano
esDivisible2=(numero%2==0) #Se almacena como booleano

if esDivisible3 and esDivisible2:
    print("Es múltiplo de 2 y 3")
if esDivisible3 and not esDivisible2:
    print("Es múltiplo de 3")
if not esDivisible3 and esDivisible2:
    print("Es múltiplo de 2")
if not esDivisible3 and not esDivisible2:
    print("No es múltiplo de 2 ni 3")

