#Manejo de archivos.
import os #Importar libreria del sistema operativo

#LEER ARCHIVOS
#file=open("archivo1.txt","r")
#print(file.read()) #Lee el archivo y lo muestra por pantalla
#print(file.read(4))#Lee los primeros cuatro caracteres del archivo.
#print(file.readline()) #Leerme la primera línea del archivo
#print(file.readline()) #Me lee la segunda línea
#for x in file: #Imprimiría todo el archivo, línea por línea.
#    print(x)
#file.close() #Cerrar archivo


#CREAR ARCHIVOS.
#file2=open("archivoCreadoPrueba.txt","x")
#print("Archivo creado")
#file2.close()

#Crear cinco archivos llamados log1.txt, log2.txt, ..., log5.txt
"""for x in range(5):
    file=open("log"+str(x)+".txt","x")
    file.close()"""
#Nota: No se pueden crear archivos que ya están creados.

#ESCRIBIR EN ARCHIVOS
#Opción 1. Con Write "w" .Crea si no existe y sobreescribe el contenido.
file3=open("ej.25.creararchivo1.txt","w")
file3.write("Adios")
file3.write("Adios2")
file3.close()
file4=open("ej.25.creararchivo2.txt","w")
file4.write("Adios")
file4.close()
file4=open("ej.25.creararchivo2.txt","w")
file4.write("Adios2")
file4.write(".\nHoy esta lloviendo")
file4.close()

#Opción 2. Con append "a". Crea si no existe y añade el contenido.
file3=open("ej.25.creararchivo1.txt","a")
file3.write("\nAñadiendo otro un nuevo texto")
file3.close()

#ELIMINAR ARCHIVO
#os.remove("archivo1.txt")

if os.path.exists("ej.25.creararchivo3.txt"):
    os.remove("ej.25.creararchivo3.txt")
else:
    print("El archivo no existe")
