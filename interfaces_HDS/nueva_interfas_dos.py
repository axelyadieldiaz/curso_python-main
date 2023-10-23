# # importamos TKinter
# from tkinter import *

# # instanciar la clase Tk()
# ventana=Tk()

# #creo mis dos widget de orden inferior con la clase Frame()   

# #instancio mi primer widget
# Widget_uno=Frame()
# # usar metodo para montar el frame
# Widget_uno.grid(row='0',column='0')
# Widget_uno.config(width='100',height='100')
# Widget_uno.config(background='blue')
# #el metodo grid recibe 2 parametros el numero de la columma y el
# #numero de la fila donde quiero ubicar mi widget 

# # creacion de segundo widget
# Widget_dos=Frame()
# Widget_dos.grid(row='2',column='0')
# Widget_dos.config(width='100',height='100')
# Widget_dos.config(background='red')
# # usar el metodo loop que la ventana permanesca abierta
# ventana.mainloop()
# import tkinter as tk

# # Crear la ventana principal
# ventana = tk.Tk()
# ventana.title("Cuadros con Tkinter")
# ventana.geometry("400x300")

# # Crear un Frame para los cuadrados azules
# frame_azules = tk.Frame(ventana)
# frame_azules.pack()

# # Cuadros azules
# azul1 = tk.Canvas(frame_azules, width=100, height=100, bg="blue")
# azul1.pack(side="left")
# azul2 = tk.Canvas(frame_azules, width=100, height=100, bg="blue")
# azul2.pack(side="left")

# # Rectángulo horizontal
# rectangulo = tk.Canvas(ventana, width=200, height=50, bg="green")  # Puedes cambiar el color a tu preferencia
# rectangulo.pack()
# rectangulo = tk.Canvas(ventana, width=200, height=50, bg="red")  # Puedes cambiar el color a tu preferencia
# rectangulo.pack()
# # Crear un Frame para los cuadrados rojos pequeños
# frame_rojos = tk.Frame(ventana)
# frame_rojos.pack()

# # Cuadros rojos debajo del rectángulo
# rojo1 = tk.Canvas(frame_rojos, width=50, height=50, bg="red")
# rojo1.pack(side="left")
# rojo2 = tk.Canvas(frame_rojos, width=50, height=50, bg="red")
# rojo2.pack(side="left")
# rojo3 = tk.Canvas(frame_rojos, width=50, height=50, bg="red")
# rojo3.pack(side="left")
# rojo4 = tk.Canvas(frame_rojos, width=50, height=50, bg="red")
# rojo4.pack(side="left")

# # Iniciar la aplicación
# ventana.mainloop()


# ejercicio 3
# from tkinter import *
# ventana = Tk()
# #Creo mis dos widges de orden inferior con al clase Frame()
# widget_uno = Frame()
# # usar metodo para montar el frame
# widget_uno.grid(row = '0', column = '0', padx=5, pady=1, columnspan=2)
# widget_uno.config(width = '100', height = '100')
# widget_uno.config(bg='black')
# #El método grid recibe dos parametros el numero de la columna y el numero de la fila donde quiero ubicar widget

# widget_dos = Frame()
# # usar metodo para montar el frame
# widget_dos.grid(row = '0', column =  '2', padx=5, pady=1, columnspan=2)
# widget_dos.config(width = '100', height = '100')
# widget_dos.config(bg='blue')

# widget_tres = Frame()
# widget_tres.grid(row = '1', column = '2', padx=5, pady=1, columnspan=2)
# widget_tres.config(width = '100', height = '100')
# widget_tres.config(bg='red')

# widget_cuatro = Frame()
# widget_cuatro.grid(row = '1', column = '0', padx=5, pady=1, columnspan=2)
# widget_cuatro.config(width = '100', height = '100')
# widget_cuatro.config(bg='yellow')

# widget_tres = Frame()
# widget_tres.grid(row = '2', column = '2', padx=5, pady=1, columnspan=2)
# widget_tres.config(width = '100', height = '100')
# widget_tres.config(bg='orange')

# widget_cuatro = Frame()
# widget_cuatro.grid(row = '2', column = '0', padx=5, pady=1, columnspan=2)
# widget_cuatro.config(width = '100', height = '100')
# widget_cuatro.config(bg='violet')
# ventana.mainloop()

#ejercicio 4
# from tkinter import *
# ventana = Tk()
# #Creo mis dos widges de orden inferior con al clase Frame()
# widget_uno = Frame()
# # usar metodo para montar el frame
# widget_uno.grid(row = '0', column = '0',rowspan=2, padx=1, pady=1)
# widget_uno.config(width = '100', height = '200')
# widget_uno.config(bg='black')

# widget_dos = Frame()
# # usar metodo para montar el frame
# widget_dos.grid(row = '0', column = '1', padx=5 , pady=1)
# widget_dos.config(width = '100', height = '100')
# widget_dos.config(bg='red')

# widget_tres = Frame()
# # usar metodo para montar el frame
# widget_tres.grid(row = '1', column = '1', padx=5, pady=1)
# widget_tres.config(width = '100', height = '100')
# widget_tres.config(bg='violet')

# widget_uno = Frame()
# # usar metodo para montar el frame
# widget_uno.grid(row = '2', column = '0',rowspan=2, padx=1, pady=1, columnspan=2)
# widget_uno.config(width = '200', height = '100')
# widget_uno.config(bg='green')
# ventana.mainloop()

#ejercicio 5
# from tkinter import *
# ventana = Tk()
# #creacion de etiquetas
# ventana.geometry("400x500")
# #creo mis dos wigdets de orden inferior con la clase Frame()
# Widget_uno=Frame()
# Widget_uno.grid(row=0,column=0)
# Widget_uno.config(width=400,height=50)
# Widget_uno.config(bg='green')
# #creacion de etiquetas
# etiqueta=Label(ventana,text='ingrasa su nombre')
# etiqueta.grid(row=1,column=0)
# #creacion de cuadros de texto
# cuadro_texto=Entry()
# cuadro_texto.grid(row=2,column=0)
# #usar el metodo loop para que la ventana permanesca abierta
# ventana.mainloop()

#ejercicio 6
from tkinter import *
ventana = Tk()

Widget_uno = Frame()

etiqueta_nombre_apellido = Label(ventana, text='nombre y apellidos')
entrada_nombre_apellido = Entry(ventana)

etiqueta_DNI = Label(ventana, text='DNI')
entrada_DNI = Entry(ventana)

etiqueta_celular = Label(ventana, text='celular')
entrada_celular = Entry(ventana)

etiqueta_nombre_apellido.grid(row=0, column=0, padx=10, pady=10, sticky='w')
entrada_nombre_apellido.grid(row=0, column=1, padx=10, pady=10) 

etiqueta_DNI.grid(row=1, column=0, padx=10, pady=10, sticky='w')
entrada_DNI.grid(row=1, column=1, padx=10, pady=10)  

etiqueta_celular.grid(row=2, column=0, padx=10, pady=10, sticky='w')
entrada_celular.grid(row=2, column=1, padx=10, pady=10)  

Widget_uno = Frame()

Widget_uno.grid(row=3, column=0, padx=5,pady=5, rowspan=10, columnspan=2)
Widget_uno.config(width=300, height=200)
Widget_uno.config(background='sky blue')
ventana.mainloop()

