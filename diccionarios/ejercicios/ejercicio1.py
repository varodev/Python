""" Crear un diccionario con varios elementos que permitan almacenar la edad de algunos alumn@s de la clase, 
añadir elementos, borrar elementos, cambiar la edad de un alumn@... directamente en el programa """
def main():
    edades_alumnos = {}

    edades_alumnos["Andrea"] = 18
    edades_alumnos["Ana"] = 19
    edades_alumnos["Lucas"] = 22

    if ("Lucas" in  edades_alumnos):
        del edades_alumnos["Lucas"]

    edades_alumnos["Andrea"]+=3

    edades_alumnos["Andrea"] = 25
    
    print(edades_alumnos)

if __name__ == "__main__":
    main()