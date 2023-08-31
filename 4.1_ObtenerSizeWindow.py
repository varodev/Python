from tkinter import *
import ctypes
#Conseguir ancho de pantalla del usuario
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
print(ancho, alto)

window=Tk()
window.title("Tamaño de ventana máxima")
window.geometry(str(ancho)+"x"+str(alto))
