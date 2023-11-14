from tkinter import *
from funciones_cal import *

def clear_pantalla():
    pantalla.delete(0, END)

def calcular_resultado():
    expresion = pantalla.get()
    try:
        resultado = eval(expresion)
        clear_pantalla()
        pantalla.insert(0, str(resultado))
    except Exception:
        clear_pantalla()
        pantalla.insert(0, "Error")

root = Tk()
root.title("Calculadora")
root.geometry("296x265")
root.resizable(0, 0)

pantalla = Entry(root, width=22, bg="#86A789", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, columnspan=4, padx=4, pady=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "C":
        btn = Button(root, text=button, width=6, height=3, bg="white", borderwidth=0, cursor="hand2", command=clear_pantalla)
    elif button == "=":
        btn = Button(root, text=button, width=6, height=3, bg="white", borderwidth=0, cursor="hand2", command=calcular_resultado)
    else:
        btn = Button(root, text=button, width=6, height=3, bg="white", borderwidth=0, cursor="hand2", command=lambda b=button: pantalla.insert(END, b))
    
    btn.grid(row=row_val, column=col_val, padx=1, pady=1)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
