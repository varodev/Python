#Signo zodiacal
import datetime

fNacimiento=0
def insertarFecha():
    try:
        global fNacimiento
        print("\nInserte una fecha en formato DD/MM/AAAA:\n")
        fecha=input()
        fecha=fecha.split("/")
        fNacimiento=datetime.datetime(int(fecha[2]),int(fecha[1]),int(fecha[0]))
    except:
        print("Fecha no válida.\n")
        insertarFecha()

def salir():
    print("Adios ...")



def main():
    insertarFecha()
    inicioAcuario=datetime.datetime(fNacimiento.year,1,20)
    inicioPiscis=datetime.datetime(fNacimiento.year,2,19)
    inicioAries=datetime.datetime(fNacimiento.year,3,21)
    inicioTauro=datetime.datetime(fNacimiento.year,4,20)
    inicioGeminis=datetime.datetime(fNacimiento.year,5,21)
    inicioCancer=datetime.datetime(fNacimiento.year,6,21)
    inicioLeo=datetime.datetime(fNacimiento.year,7,23)
    inicioVirgo=datetime.datetime(fNacimiento.year,8,23)
    inicioLibra=datetime.datetime(fNacimiento.year,9,23)
    inicioEscorpio=datetime.datetime(fNacimiento.year,10,23)
    inicioSagitario=datetime.datetime(fNacimiento.year,11,22)
    inicioCapricornio=datetime.datetime(fNacimiento.year,12,22)

    if fNacimiento<inicioAcuario:
        print("Eres Capricornio")
    elif fNacimiento<inicioPiscis:
        print("Eres Acuario")
    elif fNacimiento<inicioAries:
        print("Eres Piscis")
    elif fNacimiento<inicioTauro:
        print("Eres Aries")
    elif fNacimiento<inicioGeminis:
        print("Eres Tauro")
    elif fNacimiento<inicioCancer:
        print("Eres Geminis")
    elif fNacimiento<inicioLeo:
        print("Eres Cancer")
    elif fNacimiento<inicioVirgo:
        print("Eres Leo")
    elif fNacimiento<inicioLibra:
        print("Eres Virgo")
    elif fNacimiento<inicioEscorpio:
        print("Eres Libra")
    elif fNacimiento<inicioSagitario:
        print("Eres Escorpio")
    elif fNacimiento<inicioCapricornio:
        print("Eres Sagitario")
    else:
        print("Eres Capricornio")
    x=input("Pulse 'q' para salir y cualquier otra tecla para continuar.\n")
    if x != "q":
        main()

main()
