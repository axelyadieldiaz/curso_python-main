# ## Crear un programa que me pida edad de una persona, 
# # si la edad es mayor a 18 que muestre un menssaje 'Eres mayor de edad'
# #caso contrario que muestre un mensaje 'Eres menor de edad'.


# nombre=input(' Ingrese su nombre: ')
# edad = int(input("Ingresa tu edad: "))
# if edad>=18:
#         print( nombre + ' ' + 'Eres mayor de edad')
# else:
#     print(nombre + ' ' +'Eres menor de edad')
    
 



# # Una tienda comercial desea hacer un descuento del 20%, crear un programa  que me determine si el cliente se hace acreedor
# #del descuento teniendo en cuenta los  siiguiente: si el cliente realiza una compra de ygual o mayor a s/. 1000 soles  mostrar un mensaje que diga 
# # 'GANASTE EL DESCUENTO DE20%, AHORA PAGARAS <mostar el total de   la compra menos el descuento>' en caso la compra o supere los S/.1000 soles  entonses 
# #mostrar un mensaje que diga'NO APLICAS AL DESCUENTO <mostar el monto de la compra'



# NOM_TIENDA= "COMERCIAL JUELICIANA "
# NOM_CLIENTE=input ('Ingrese su nmbre: ')
# MONT_COMPRA= int(input('Ingresa el monto de compra: '))
# if MONT_COMPRA>= 1000:
#         descuento = MONT_COMPRA * 0.2
#         total_pagar = MONT_COMPRA - descuento
#         print(f"¡GANASTE EL DESCUENTO DE 20%! Ahora pagarás {total_pagar} soles.")
# else:
#         print(f"NO APLICAS AL DESCUENTO. El monto de la compra es de {MONT_COMPRA} soles.")

        
# # crear un programa que me pida 5 veces un nombre y por cada vez que lo pida muestre la cantidad de veces
# # que ingreso el nombre
# nombre = input("Ingresa un nombre: ")

# conteo = 0

# for i in range(5):
#     if nombre == input("Ingresa un nombre: "):
#         conteo += 1


# print(f"El nombre '{nombre}' se ingresó {conteo} veces.")



# # crear un programa que pida un numero y lo evalue con el numero premiado si el numero ingresado es el 
# # premiado el programa finalizara si el numero ingresado es incorrecto el programa seguira pidiendo el numero premiado 
# # Número premiado (puedes cambiarlo según tus preferencias)
# numero_premiado = 42

# while True:

#     numero_ingresado = int(input("Ingresa un número: "))


#     if numero_ingresado == numero_premiado:
#         print("¡Felicidades! Has ingresado el número premiado.")
#         break  


#     print("Número incorrecto. Inténtalo de nuevo.")


# # 5.- crea una funcion por cada operador aritmetico uqe resiva dos parametros y
# # retorne el resultado de la operacion, OJO, crearse una funcion que nos permita 
# # imprimir el resultado
# def mi_print(texto):
#       print(texto)

# def suma(a,b):
#       return a+b
# def resta(a,b):
#       return a-b
# def multi(a,b):
#       return a*b
# def divi(a,b):
#       return a/b

# mi_print(suma(4,5))
# mi_print(resta(4,5))
# mi_print(multi(4,5))
# mi_print(divi(4,5))

# 6. escribe una funcion que reciba un numero entero positivo y devuelva su factorial
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# numero = 10
# resultado = factorial(numero)
# print(f"El factorial de {numero} es igual a {resultado}")

# escribir una funcion que resiva como parametros una lista de numeros y retorne una nueva
#lista con el cuadro de cada numero de la lista ingresada

def cuadrados_de_lista(lista_numeros):
    # Creamos una nueva lista para almacenar los cuadrados
    cuadrados = []
    
    # Iteramos a través de la lista de números y calculamos el cuadrado de cada uno
    for numero in lista_numeros:
        cuadrado = numero ** 2
        cuadrados.append(cuadrado)
    
    return cuadrados

# Ejemplo de uso:
numeros = [1, 2, 3, 4, 5]
cuadrados = cuadrados_de_lista(numeros)
print("Lista de números:", numeros)
print("Cuadrados de la lista:", cuadrados)


#8 escribir un programa que reciba una cadena de caracteres y devuelva un
#  objeto con cada palabra que contiene y su frecuencia
def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()

    # Crear un diccionario para almacenar las frecuencias
    frecuencia_palabras = {}

    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        # Limpiar la palabra de caracteres especiales y convertirla a minúsculas
        palabra = palabra.strip('.,!?()[]{}"\'').lower()

        # Si la palabra ya está en el diccionario, incrementa su frecuencia
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            # Si la palabra no está en el diccionario, agrégala con frecuencia 1
            frecuencia_palabras[palabra] = 1

    return frecuencia_palabras

# Solicitar al usuario que ingrese una cadena de caracteres
cadena = input("Ingrese una cadena de caracteres: ")

# Obtener el objeto con la frecuencia de palabras
frecuencia = contar_palabras(cadena)

# Mostrar las palabras y sus frecuencias
for palabra, frecuencia in frecuencia.items():
    print(f'Palabra: "{palabra}", Frecuencia: {frecuencia}')


# crear un enterno virtual con venv de python e instalar
# el framewrok dejando para la creacion de app web
# crear entorno
# activar entorno
# instalar el paquete
