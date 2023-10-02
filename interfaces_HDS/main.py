import tkinter as tk

# Función para realizar la operación seleccionada
def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operador = operador_var.get()
    
    if operador == "+":
        resultado.set(num1 + num2)
    elif operador == "-":
        resultado.set(num1 - num2)
    elif operador == "*":
        resultado.set(num1 * num2)
    elif operador == "/":
        if num2 != 0:
            resultado.set(num1 / num2)
        else:
            resultado.set("Error: División por cero")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Calculadora")

# Variables para almacenar números y resultado
entry_num1 = tk.Entry(ventana)
entry_num2 = tk.Entry(ventana)
resultado = tk.StringVar()
resultado.set("Resultado: ")

# Menú desplegable para seleccionar operador
operadores = ["+", "-", "*", "/"]
operador_var = tk.StringVar()
operador_var.set(operadores[0])
menu_operador = tk.OptionMenu(ventana, operador_var, *operadores)

# Botón para calcular
calcular_btn = tk.Button(ventana, text="Calcular", command=calcular)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, textvariable=resultado)

# Colocar widgets en la ventana
entry_num1.grid(row=0, column=0)
menu_operador.grid(row=0, column=1)
entry_num2.grid(row=0, column=2)
calcular_btn.grid(row=1, column=0, columnspan=3)
resultado_label.grid(row=2, column=0, columnspan=3)

# Iniciar el bucle principal
ventana.mainloop()
