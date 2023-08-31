from tkinter import *

window = Tk()
window.title("Tamaño ventana")
#window.geometry("600x300") #Ancho x alto en píxeles.
window.geometry("3000x1000")
lbl = Label(window, text="Hola", font=('Helvetica', 24,))
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Hola2", font=("Times", 15, "bold"))
lbl2.grid(column=1, row=1)
lbl3 = Label(window, text="Hola3", font=("Helvetica", 50,"italic"))
lbl3.grid(column=2, row=2)
custom_font_sans = ('Arial', 17, 'italic')
lbl4 = Label(window, text="Hola4", font=custom_font_sans)
lbl4.grid(column=3, row=3)

window.mainloop()
