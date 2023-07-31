lista=[]
indice=0
palabra=""
while len (lista)<5:
    dato=input("ingrese un dato: ")
    lista.append(dato)
for texto in range(0,len(lista)):
    if lista[texto] == "disco":
        palabra=lista[texto]
        indice=texto
print(f"""el texto disco se encuentra en el indice hola {indice}
      y el texto es {palabra}""")
