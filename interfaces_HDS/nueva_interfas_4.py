# from tkinter import *
# ventana=Tk()
# ventana.title("yadiel")
# ventana.geometry("500x500")
# colum_izquierda=Frame()
# colum_izquierda.grid(row=0,column=0)
# colum_izquierda.config(width=200,height=5)
# etiqueta=Label(ventana,text="esta es la etiqueta")
# etiqueta.grid(row=0,column=1)

# ventana.mainloop()
 

# from tkinter import *

# def sumar():
#     try:
#         num1 = int(entry_numero1.get())
#         num2 = int(entry_numero2.get())
#         resultado.set(str(num1 + num2))
#     except ValueError:
#         resultado.set("Error")

# def limpiar():
#     entry_numero1.delete(0, END)
#     entry_numero2.delete(0, END)
#     resultado.set("")

# ventana = Tk()
# ventana.title("Calculadora Simple")

# label_numero1 = Label(ventana, text="Número 1:")
# label_numero1.grid(row=0, column=0)

# entry_numero1 = Entry(ventana)
# entry_numero1.grid(row=0, column=1)
# entry_numero1.insert(0, "0")

# label_numero2 = Label(ventana, text="Número 2:")
# label_numero2.grid(row=1, column=0)

# entry_numero2 = Entry(ventana)
# entry_numero2.grid(row=1, column=1)
# entry_numero2.insert(0, "0")

# resultado = StringVar()
# resultado_label = Label(ventana, text="Resultado:")
# resultado_label.grid(row=2, column=0)

# entry_resultado = Entry(ventana, textvariable=resultado)
# entry_resultado.grid(row=2, column=1)

# boton_sumar = Button(ventana, text="Sumar", command=sumar)
# boton_sumar.grid(row=3, column=0)

# boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
# boton_limpiar.grid(row=3, column=1)

# ventana.mainloop()

from tkinter import *

notas = []  # Lista para almacenar las notas ingresadas

def agregar_nota():
    try:
        nota = float(entry_nota.get())
        notas.append(nota)
        entry_nota.delete(0, END)  # Limpiar la entrada
    except ValueError:
        resultado.set("Error: Ingrese una nota válida")

def calcular_promedio():
    if notas:
        promedio = sum(notas) / len(notas)
        resultado.set(f"Promedio: {promedio:.2f}")
    else:
        resultado.set("Error: No hay notas para calcular el promedio")

ventana = Tk()
ventana.title("Calculadora de Promedio")

label_nota = Label(ventana, text="Nota:")
label_nota.grid(row=0, column=0)

entry_nota = Entry(ventana)
entry_nota.grid(row=0, column=1)

boton_agregar = Button(ventana, text="Agregar Nota", command=agregar_nota)
boton_agregar.grid(row=1, column=0)

boton_calcular = Button(ventana, text="Calcular Promedio", command=calcular_promedio)
boton_calcular.grid(row=1, column=1)

resultado = StringVar()
resultado_label = Label(ventana, textvariable=resultado)
resultado_label.grid(row=2, columnspan=2)

ventana.mainloop()
