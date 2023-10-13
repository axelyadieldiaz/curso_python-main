#1. inport tkinter -> libreria para la creacion de interfaces grafica
from tkinter import *

# la libreria tkinter tiene tres grandes clases para la creacion de interfaces
# TK() -> el mas usado
# TKK()
# Tcl()

#2. instanciar TK() como generador de interfaz grafica
nueva_ventana=Tk()

#3. frame es tambien una clase Frame() para crear un Frame tengo que primero instanciarlo
menu_principal=Frame()
#montamos o inicializamos al frame
menu_principal.pack()
# haciendo uso del metodo config le damos en tamaño
menu_principal.config(width='200',height='200')
# haciendo uso del metodo config le asignamos un color
menu_principal.config(background='blue')
# metodo de TK() que mantiene la ejecucion del programa en un bucle
nueva_ventana.mainloop()
