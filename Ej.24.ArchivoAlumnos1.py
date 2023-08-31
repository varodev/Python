#Manejo de archivos.
#Crear un archivo con nombre alumnos.txt. Y donde vaya almacenando 5 alumnos, el nombre del
#alumno, el dni, y el teléfono. Cada campo separado por coma. Cada uno uno en una línea.

lista=[]
def datosAlumnos():
    print("Inserte nombre alumno:")
    nombre=input()
    print("Insertar dni:")
    dni=input()
    print("Insertar telefono:")
    telefono=input()
    alumno=nombre+","+dni+","+telefono+"\n"
    archivo=open("ej.24.archivoalumnos1.txt","a")
    archivo.write(alumno)
    archivo.close()


def mostrarArchivo():
    archivo=open("ej.24.archivoalumnos1.txt","r")
    for x in archivo:
        dato=x[0:len(x)-1] #Quitamos el sato de línea
        lista.append(dato)  #Insertar datos en una lista
    
#Inserta los alumnos
"""for x in range(3):
    datosAlumnos()
"""
#Muestra y los almacena en una lista
mostrarArchivo()
