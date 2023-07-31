import tomadedatos
while len (tomadedatos.lista)<5:
    dato=input("ingrese un dato: ")
    tomadedatos.lista.append(dato)
for texto in range(0,len(tomadedatos.lista)):
    if tomadedatos.lista[texto] == "disco":
        palabra=tomadedatos.lista[texto]
        indice=texto