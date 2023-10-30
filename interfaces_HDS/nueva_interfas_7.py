# from tkinter import *

# ventana = Tk()
# ventana.title("Calculadora")
# ventana.geometry("350x300")

# # Funciones para realizar las operaciones de suma y resta
# def calcular():
#     num1 = float(entrada_num1.get())
#     num2 = float(entrada_num2.get())
#     if operacion.get() == "Sumar":
#         resultado.set(int(num1 + num2))
#     elif operacion.get() == "Restar":
#         resultado.set(int(num1 - num2))

# # Cuadros de entrada y etiquetas en el lado izquierdo (uno al lado del otro)
# etiqueta_num1 = Label(ventana, text='Número 1')
# etiqueta_num1.grid(row=0, column=0, padx=10, pady=10)
# entrada_num1 = Entry(ventana)
# entrada_num1.grid(row=0, column=1, padx=10, pady=10)

# etiqueta_num2 = Label(ventana, text='Número 2')
# etiqueta_num2.grid(row=1, column=0, padx=10, pady=10)
# entrada_num2 = Entry(ventana)
# entrada_num2.grid(row=1, column=1, padx=10, pady=10)

# # Opciones de suma y resta al lado de los cuadros de entrada

# operacion = StringVar()
# operacion.set("Sumar")  # Valor por defecto

# radio_sumar = Radiobutton(ventana, text="Sumar", variable=operacion, value="Sumar")
# radio_restar = Radiobutton(ventana, text="Restar", variable=operacion, value="Restar")

# radio_sumar.grid(row=1, column=2, padx=10, pady=10, sticky='w')
# radio_restar.grid(row=2, column=2, padx=10, pady=10, sticky='w')

# # Resultado en un cuadro de entrada
# etiqueta_resultado = Label(ventana, text='Resultado')
# etiqueta_resultado.grid(row=3, column=0, padx=10, pady=10)
# resultado = IntVar()
# entrada_resultado = Entry(ventana, textvariable=resultado, state='readonly')
# entrada_resultado.grid(row=3, column=1, padx=10, pady=10)

# # Botón de calcular en el centro
# boton_calcular = Button(ventana, text="Calcular", command=calcular)
# boton_calcular.grid(row=4, column=0, columnspan=3, pady=10)

# ventana.mainloop()

from tkinter import *

def calcular():
    num1 = float(entrada_num1.get())
    num2 = float(entrada_num2.get())
    if operacion.get() == "Sumar":
        resultado.set(int(num1 + num2))
    elif operacion.get() == "Restar":
        resultado.set(int(num1 - num2))
    elif operacion.get() == "Multiplicar":
        resultado.set(int(num1 * num2))
    elif operacion.get() == "Dividir":
        if num2 != 0:
            resultado.set(float(num1 / num2))
        else:
            resultado.set("Error: División por cero")

def limpiar():
    entrada_num1.delete(0, END)
    entrada_num2.delete(0, END)
    resultado.set("")
    operacion.set("Sumar") 

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("350x300")

etiqueta_num1 = Label(ventana, text='Número 1')
etiqueta_num1.grid(row=0, column=0, padx=10, pady=10)
entrada_num1 = Entry(ventana)
entrada_num1.grid(row=0, column=1, padx=10, pady=10)

etiqueta_num2 = Label(ventana, text='Número 2')
etiqueta_num2.grid(row=1, column=0, padx=10, pady=10)
entrada_num2 = Entry(ventana)
entrada_num2.grid(row=1, column=1, padx=10, pady=10)

operacion = StringVar()
operacion.set("Sumar")

radio_sumar = Radiobutton(ventana, text="Sumar", variable=operacion, value="Sumar")
radio_restar = Radiobutton(ventana, text="Restar", variable=operacion, value="Restar")
radio_multiplicar = Radiobutton(ventana, text="Multiplicar", variable=operacion, value="Multiplicar")
radio_dividir = Radiobutton(ventana, text="Dividir", variable=operacion, value="Dividir")

radio_sumar.grid(row=1, column=2, padx=10, pady=10, sticky='w')
radio_restar.grid(row=2, column=2, padx=10, pady=10, sticky='w')
radio_multiplicar.grid(row=3, column=2, padx=10, pady=10, sticky='w')
radio_dividir.grid(row=4, column=2, padx=10, pady=10, sticky='w')

etiqueta_resultado = Label(ventana, text='Resultado')
etiqueta_resultado.grid(row=5, column=0, padx=10, pady=10)
resultado = IntVar()
entrada_resultado = Entry(ventana, textvariable=resultado, state='readonly')
entrada_resultado.grid(row=5, column=1, padx=10, pady=10)

boton_calcular = Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=6, column=0, padx=10, pady=10)

boton_limpiar = Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.grid(row=6, column=1, padx=10, pady=10)

ventana.mainloop()
