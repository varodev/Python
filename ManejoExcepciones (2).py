#Manejo de excepciones

try:
    print("Inserte un número:\n")
    a=int(input())
    print(a)
except NameError:
    print("El número no es válido, por favor, insertelo de nuevo")
except ValueError:
    print("Esto es una excepción de ValueError")
else:
    print("No hay excepción")
finally:
    print("Esto siempre se ejecuta")
    
