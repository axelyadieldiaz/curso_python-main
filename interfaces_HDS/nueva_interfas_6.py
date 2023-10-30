# # primero importar la libreria 
from tkinter import*

# instanciamos nuestra clase tk()
ventana=Tk() # clase para crear una ventana
ventana.title("clase radiobutton") # haciendo uso del metodo title para el titulo de mi ventana
ventana.geometry("400x300") #haciendo uso del metodo geometry para asignarle un tamaño de ventana

# instanciar mi clase label
etiqueta=Label(ventana, text=" radio buttos") #clase para crear una etiqueta 
# inidcar la parte de mi ventana que deseo que se muestre 
# puedo usar los metodos grid o pack
etiqueta.config(foreground="#EB6828", font=50)
etiqueta.pack()

info=IntVar()

def mostrar_seleccion():
    seleccion  = info.get()
    if seleccion == 1:
        resultado.config(text="Seleccionaste: Masculino")
    elif seleccion == 0:
        resultado.config(text="Seleccionaste: Femenino")
    else:
        resultado.config(text="Ninguna selección")

# instaciar la clase radiobutton
radioMasculino=Radiobutton(ventana, text="masculino", value="1",variable=info)
radioMasculino.pack()
radioFemenino=Radiobutton(ventana, text="femenino", value="0",variable=info)
radioFemenino.pack()

# instanciar la clase button
boton=Button(ventana, text="enviar", command=mostrar_seleccion)
boton.pack()

resultado = Label(ventana, text="")
resultado.pack()

# llamar al metodo de tk que me permite tener perisistentecia al mostrar la ventana 
ventana.mainloop()

