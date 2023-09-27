# haciendo uso de la POO crear un objeto para entidad celular
class celular:
    marca="huawei"
    camara="806 píxeles"
    color="blanco"
    modelo="y9 prime"

    def encender(self):
        return "preciona el boton del costado"
    def mensaje(self):
        return "enviar y recibir mensajes"

respuesta=celular()
print(respuesta.marca)
print(respuesta.encender())
print(respuesta.mensaje(10))
# haciendo uso de la POO crear un objeto para entidad vehiculo
class Vehiculo:
    marca="ferrari"
    soat="un año"
    color="negro"
    modelo="SF90 Stradale"

    def motor(self):
        return "de 250 caballos"
    def velocidad(self):
        huevo=f"llega hasta los 350 K/M"
        return huevo

respuesta=Vehiculo()
print(respuesta.marca)
print(respuesta.motor())
print(respuesta.velocidad(10))

# haciendo uso de la POO crear un objeto para entidad avion

# haciendo uso de la POO crear un objeto para entidad dota2

#TKINTER - libreria de python para la creacion de interfacez graficas