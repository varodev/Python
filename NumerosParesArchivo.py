#Objetivo. Crear un archivo con los números pares del 0 al 1000, separados
#por comas. El nombre del archivo va a ser pares.info

#Opción 1 - Carlos
archivo=open("pares.info","w")
for x in range(1000):
    if x%2==0:
        archivo.write(str(x)+",")
archivo.close()

#Opción 2 - Blanca
archivo=open("paresBlanca.info","w")
contador=2
for x in range(500):
        archivo.write(str(contador)+",")
        #contador=contador+2
        contador+=2
archivo.close()

#Opción 3 - Julian
archivo=open("paresJulian.info","w")
for x in range(0,1000,2):
        archivo.write(str(x)+",")
archivo.close()
