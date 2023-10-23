# from tkinter import*
# ventana= Tk()
# ventana.geometry("300x500")
# ventana.title("ventana suma")

# def captura_dato():
#     text=text_nombre.get()
#     mensaje=Label(ventana,text=f"hola,{text}")
#     mensaje.pack()

# etiqueta=Label(ventana,text="introduce tu nombre")
# etiqueta.pack()

# text_nombre=Entry(ventana)
# text_nombre.config(background="blue",foreground="yellow")
# text_nombre.pack()

# boton_capturar=Button(ventana,
# text="enviar",command=captura_dato)
# boton_capturar.pack()

# ventana.mainloop()

# from tkinter import *
# ventana = Tk()
# ventana.geometry("300x200")
# ventana.title("Verificar Edad")

# def verificar_edad():
#     edad = int(text_edad.get())
#     resultado = ""
    
#     if edad >= 65:
#         resultado = "Ya eres un abuelo."
#     elif edad >= 18:
#         resultado = "Eres mayor de edad."
#     else:
#         resultado = "Eres menor de edad."

#     mensaje.config(text=f"{resultado}")

# etiqueta_edad = Label(ventana, text="Introduce tu edad:")
# etiqueta_edad.pack()

# text_edad = Entry(ventana)
# text_edad.pack()

# boton_verificar = Button(ventana, text="Verificar Edad", command=verificar_edad)
# boton_verificar.pack()

# mensaje = Label(ventana, text="")
# mensaje.pack()

# ventana.mainloop()

from tkinter import *

ventana = Tk()
ventana.geometry("400x300")
ventana.title("Verificar Usuario y Contraseña")

def verificar_usuario_contraseña():
    usuario = text_usuario.get()
    contraseña = text_contraseña.get()
    
    if usuario == contraseña:
        resultado = "Su Usuario y Contraseña son correctos."
    else:
        resultado = "Su Usuario y Contraseña no son correctos, vuelve a intentarlo."
    
    mensaje.config(text=resultado)

etiqueta_usuario = Label(ventana, text="Introduce tu usuario:")
etiqueta_usuario.pack()

text_usuario = Entry(ventana)
text_usuario.pack()

etiqueta_contraseña = Label(ventana, text="Introduce tu contraseña:")
etiqueta_contraseña.pack()

text_contraseña = Entry(ventana, show="*") 
text_contraseña.pack()

boton_verificar = Button(ventana, text="Verificar Usuario y Contraseña", command=verificar_usuario_contraseña)
boton_verificar.pack()

mensaje = Label(ventana, text="")
mensaje.pack()

ventana.mainloop()

