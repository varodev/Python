#Ejemplo Diccionario
coche={"marca":"Ford",
             "modelo":"Mustang",
             "año": 1964,
             "color":"Bonito"}

coche["puertas"]=3 #Añadir clave y valor
z=coche.pop("color") #Eliminar item y guarda el valor dentro de una variable

coche["precio"]=30000
coche.popitem()# Elimina el último insertado. Elimina el item precio





for x in coche: #Devuelve clave
    print(x)

for x in coche.values(): #Devuelve valores
    print(x)

for x in coche.items(): #Devuelve clave y valor
    print(x)

for x,y in coche.items(): #Devuelve la clave, un string y el valor
    print("Hola ",x," es ",y)

for x,y in coche.items(): #Devuelve la clave, un string y el valor
    print(x+" es "+str(y))

x="modelo2"
if x in coche:
    print("La clave ",x," existe")
else:
    print("La clave no existe")


print("La longitud del diccionario 'coche' es ", len(coche))
        
    
