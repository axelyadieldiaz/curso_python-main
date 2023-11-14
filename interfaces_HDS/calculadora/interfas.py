from tkinter import *
from funciones_cal import *
# configuracion basica de la ventana 
root = Tk()
root.title("calculadora")
root.geometry("300x375")
root.resizable(0,0)

# pantalla que muestra los numeros ingresados y el resultdo
pantalla=Entry(root,width=22, # asigna el color de fondo
               bg="#86A789", # asigna el color de fondo
               fg="white", # asigna el fonod de letra 
               borderwidth=0, # tamaño del borde de mi cuadro de texto 
               font=("arial",18,"bold")) # asignamos el tipo de tamaño de fuente
pantalla.grid(row=0,columnspan=4,padx=4,pady=4)

bton_1 = Button(root,text="1",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(1,pantalla)).grid(row=1,column=0,padx=1,pady=1)
bton_2 = Button(root,text="2",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(2,pantalla)).grid(row=1,column=1,padx=1,pady=1)
bton_3 = Button(root,text="3",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(3,pantalla)).grid(row=1,column=2,padx=1,pady=1)
bton_4 = Button(root,text="4",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(4,pantalla)).grid(row=2,column=0,padx=1,pady=1)
bton_5 = Button(root,text="5",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(5,pantalla)).grid(row=2,column=1,padx=1,pady=1)
bton_6 = Button(root,text="6",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(6,pantalla)).grid(row=2,column=2,padx=1,pady=1)
bton_7 = Button(root,text="7",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(7,pantalla)).grid(row=3,column=0,padx=1,pady=1)
bton_8 = Button(root,text="8",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(8,pantalla)).grid(row=3,column=1,padx=1,pady=1)
bton_9 = Button(root,text="9",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(9,pantalla)).grid(row=3,column=2,padx=1,pady=1)

botn_igual=Button(root,text="=")
botn_igual= Button(root,text="=",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:igual(pantalla)).grid(row=4,column=0,padx=1,pady=1)
##
botn_punto= Button(root,text=".",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(".",pantalla)).grid(row=4,column=2,padx=1,pady=1)
botn_cero= Button(root,text="0",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:enviar_boton(0,pantalla)).grid(row=4,column=1,padx=1,pady=1)
# crear botones de operaciones 
botn_suma= Button(root,text="+",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:operacion("+",pantalla)).grid(row=1,column=3,padx=1,pady=1)
botn_resta= Button(root,text="-",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:operacion("-",pantalla)).grid(row=2,column=3,padx=1,pady=1)
botn_multiplicar= Button(root,text="*",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:operacion("*",pantalla)).grid(row=3,column=3,padx=1,pady=1)
botn_dividir= Button(root,text="/",width=6,height=3,bg="white",borderwidth=0,cursor="hand2",command=lambda:operacion("/",pantalla)).grid(row=4,column=3,padx=1,pady=1)

botn_limpiar= Button(root,text="limpiar",width=40,height=3,bg="deep sky blue",fg="black",borderwidth=0,cursor="hand2",command=lambda:limpiar(pantalla)).grid(row=5,column=0,columnspan=4,padx=1,pady=1)

root.mainloop()