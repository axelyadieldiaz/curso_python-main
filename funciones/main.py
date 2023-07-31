##lista=["a","e","i"]

##for indice,valor in enumerate(lista):
##    if valor == "i":
##        print(valor,indice)
## crear una lista que almacene los numeros del 1 al 10, 
##crear una funcion que me oermita recibir como parametro una lista
# la funcion teb¿ndra que retornar un nuevo aray con los numeros pares que sea ingresado 
# por parametro

# lista=[1,2,3,4,5,6,7,8,9,10]

# def numeros_pares(array):
#     nueva_lista=[]
#     for _,num in enumerate(array):
#         if num%2==0:
#             nueva_lista.append(num)
#     return nueva_lista
# print(numeros_pares(lista))

# texto="hola como estas"
# print(list(texto))
# print(texto.split(""))

## hacer un programa que pida al usuario un texto,
# y evaluar con sus funciones la cantidad de vocales a que tiene el texto

def contar_vocales(texto):
    texto = texto.lower()
    vocales = ["a","e","i","o","u"]
    contador_vocales = 0

    for letra in texto:
        if letra in vocales:
            contador_vocales += 1
    
    return contador_vocales

texto_usuario = input("ingresa un texto: ")

cantidad_vocales = contar_vocales(texto_usuario)

print(f"El texto ingresado tiene {cantidad_vocales} vocales.")

