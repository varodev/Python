#Ejemplos funciones matemáticas.

#IVA. Nos da un precio con IVA Incluido y tenemos que obtener la base imponible y el
# y el 21 %. Dos decimales.



print ("Inserte el precio del producto, con dos decimales: ")
precio=float(input())
base=round(precio/1.21,2)
IVA=round(base*0.21,2)
print("La base imponible es " + str(base))
print("El IVA 21% de " + str(precio) + " es " + str(IVA))
