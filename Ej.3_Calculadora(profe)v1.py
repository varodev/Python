from tkinter import *

def pintar(caracter):
    global operacion
    operacion=operacion+caracter
    resultado['text']=operacion

operacion=""
ventana=Tk()
ventana.title("Ejercicio 3. Calculadora")
ventana.geometry("800x1090")
#ventana.configure(background="Gray")
#ventana.wm_attributes('-alpha', 0.7)

imagen= PhotoImage(file="calculadora.png")
imagen2= PhotoImage(file="vacio.png")
fondo=Label(ventana,image=imagen).place(x=0,y=0)

resultado=Label(ventana,text="Resultado",width=100, height=7).place(x=30,y=50)
boton1=Button(ventana,text="1", command=pintar("1")).place(x=220,y=440)
boton2=Button(ventana,text="2", command=pintar("2")).place(x=240,y=440)
ventana.mainloop()
