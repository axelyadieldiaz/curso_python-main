# en nombre siempre debera ser un  singular y con la primera letra mayuscula
class Perro:
    nombre="boby"
    edad="2 meses"
    color="cheqche"
    raza="chusterrier"

    def ladrar(self):
        return "gua gua mascota"
    def corre(self,pasos):
        huevo=f"corriste {pasos}, pasos"
        return huevo

respuesta=Perro()
print(respuesta.nombre)
print(respuesta.ladrar())
print(respuesta.corre(10))