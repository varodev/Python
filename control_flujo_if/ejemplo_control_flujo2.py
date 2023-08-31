
#Escribir un programa para una empresa de videojuegos que quiere poner el precio de las suscripciones
#  en función de la edad del usuario. El programa debe preguntar al usuario la edad y mostrar el 
# precio de la suscripción. Si el cliente es menor de 14 años puede entrar gratis, si tiene entre
#  14 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad_usuario = int(input("Qué edad tienes?"))

if (edad_usuario < 14):
    print("Puedes entrar gratis")
elif ( (edad_usuario > 14) and (edad_usuario < 18)):
    print("Debes pagar 5 euros")
else:
    print("Debes pagar 10 euros")