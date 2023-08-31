from tkinter import *

window = Tk()

canv = Canvas(window, width=200, height=200)
canv.pack()

boton=Button(canv,text="Boton")
boton.place(x=00,y=50)

#canv.create_line(0, 0, 200, 100)
#canv.create_line(0, 100, 200, 0, fill="green", dash=(3,3)

canv.create_rectangle(50, 25, 150, 75, fill="blue")

canv.create_oval(50, 100, 150, 150, fill="lime")
window.mainloop()
