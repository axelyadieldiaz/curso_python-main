## Crear un programa que me pida edad de una persona, 
# si la edad es mayor a 18 que muestre un menssaje 'Eres mayor de edad'
#caso contrario que muestre un mensaje 'Eres menor de edad'.


nombre=input(' Ingrese su nombre: ')
edad = int(input("Ingresa tu edad: "))
if edad>=18:
        print( nombre + ' ' + 'Eres mayor de edad')
else:
    print(nombre + ' ' +'Eres menor de edad')
    
 



# Una tienda comercial desea hacer un descuento del 20%, crear un programa  que me determine si el cliente se hace acreedor
#del descuento teniendo en cuenta los  siiguiente: si el cliente realiza una compra de ygual o mayor a s/. 1000 soles  mostrar un mensaje que diga 
# 'GANASTE EL DESCUENTO DE20%, AHORA PAGARAS <mostar el total de   la compra menos el descuento>' en caso la compra o supere los S/.1000 soles  entonses 
#mostrar un mensaje que diga'NO APLICAS AL DESCUENTO <mostar el monto de la compra'



NOM_TIENDA= "COMERCIAL JUELICIANA "
NOM_CLIENTE=input ('Ingrese su nmbre: ')
MONT_COMPRA= int(input('Ingresa el monto de compra: '))
if MONT_COMPRA>= 1000:
        descuento = MONT_COMPRA * 0.2
        total_pagar = MONT_COMPRA - descuento
        print(f"¡GANASTE EL DESCUENTO DE 20%! Ahora pagarás {total_pagar} soles.")
else:
        print(f"NO APLICAS AL DESCUENTO. El monto de la compra es de {MONT_COMPRA} soles.")

        
# crear un programa que me pida 5 veces un nombre y por cada vez que lo pida muestre la cantidad de veces
# que ingreso el nombre
nombre = input("Ingresa un nombre: ")

conteo = 0

for i in range(5):
    if nombre == input("Ingresa un nombre: "):
        conteo += 1


print(f"El nombre '{nombre}' se ingresó {conteo} veces.")



# crear un programa que pida un numero y lo evalue con el numero premiado si el numero ingresado es el 
# premiado el programa finalizara si el numero ingresado es incorrecto el programa seguira pidiendo el numero premiado 
# Número premiado (puedes cambiarlo según tus preferencias)
numero_premiado = 42

while True:

    numero_ingresado = int(input("Ingresa un número: "))


    if numero_ingresado == numero_premiado:
        print("¡Felicidades! Has ingresado el número premiado.")
        break  


    print("Número incorrecto. Inténtalo de nuevo.")
