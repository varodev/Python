#Cálculo de una matricula de la universidad.


"""
DESCUENTOS EN LA MATRÍCULA DE LA UNIVERSIDAD
Condiciones:
    - Familia numerosa: 10%.
    - Edad: Entre menor o igual a 20 años: 10%
            Mayor 20 años y menor de 30 años: 5%
            Mayor o igual de 30 años: 0%
    - Discapacidad mayor o igual al 33%: 100%
    - Discapacidad entre 10 y 32%: 50%
    - Distancia de la universidad: Mayor o igual a 20 km. 10%
    La matricula ordinaria anual es de 10.000 euros.
    Nos tiene que informar de los descuentos que ha tenido y el importe final,
    El importe no puede negativo.
"""
descuento=0
descuentosObtenidos="Descuentos:\n"
matriculaOrdinaria=10000
familiaNumerosa=0
edad=0
discapacidad=0
distancia=0
importeFinal=10000

print("******* MATRICULA DE UNIVERSIDAD 'LA BARATA'***********")

print("¿Es familia numerosa? \(Responder Si o No\)")
respuesta=input()
respuesta=respuesta.upper()
if respuesta=="SI":
    descuento+=10
    descuentosObtenidos+="Familia numerosa 10%\n"

print("Inserte su edad:")
respuesta=int(input())
if respuesta <= 20:
    descuento=descuento+10
    descuentosObtenidos+="Menor o igual a 20 años 10%\n"
if respuesta > 20 and respuesta < 30:
    descuento=descuento+5
    descuentosObtenidos+="Mayor 20 años y menor de 30 años 5%\n"

print("¿Tiene alguna discapacidad? \(Responder Si o No\)")
respuesta=input()
respuesta=respuesta.upper()
if respuesta=="SI":
    print("Inserte su discapacidad en porcentaje:")
    respuesta=int(input())
    if respuesta > 10 and respuesta < 33:
        descuento=descuento+50
        descuentosObtenidos+="Discapacidad entre el 10 y 32    50%\n"
    if respuesta >= 33:
        descuento=100
        descuentosObtenidos+="Discapacidad mayor o igual a 33   100%\n"

print("Distancia desde su residencia al campus \(en kilómetros\)")
respuesta=int(input())
if respuesta >= 20:
    descuento=descuento+10
    descuentosObtenidos+="Distancia hasta al campus superior o igual a 20 km 10%\n"

if descuento > 100:
    descuento = 100
importeFinal=importeFinal - (matriculaOrdinaria * descuento / 100) 
print("\n\nEl descuento total obtenido es de "+ str(descuento)+ "%")
print(descuentosObtenidos)
print("El importe final de su matricula es "+ str(importeFinal)+ " euros.")
