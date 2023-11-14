# from rich import print

# class mascota:
#     def __init__(self):
#         self.nombre=None
#         self.edad=None
#         self.tipo_animal=None
#     def hablar(self,sonido):
#         return sonido 
#     def datos_mascotas(self,nombre,edad,tipo_animal):
#         self.nombre=nombre
#         self.edad=edad
#         self.tipo_animal=tipo_animal
# #repaso de programacion orientada a objetos 
# class perro(mascota):
#     def atacar(self):
#         return "ñadra y muerde"
# class gato(mascota):
#     pass

# perro_boby=perro()
# perro_boby.datos_mascotas("boby",14,"perro")
# print(f"[bold blue]"+perro_boby.hablar("gauu guauu"))
# print("[blod blue]"+perro_boby.atacar())
# print("[blod blue]"+perro_boby.nombre+" "+perro_boby.tipo_animal)


# class persona:
#     def __init__(self,nombre:str,edad:int,sexo:str):
#         self.nombre=nombre
#         self.edad=edad
#         self.sexo=sexo
#     def comen(self,plato_favorito:str):
#         return f"yo {self.nombre} estoy comiendo mi {plato_favorito}"
    
#     def cagan(self):
#         return "pipi popo"
    
# class estudiante(persona):
#     def __init__(self, nombre: str, edad: int, sexo: str,carrera_profecional:str):
#         super().__init__(nombre, edad, sexo)
#         self.carrera_profecional=carrera_profecional
#     def estudiar(self):
#         return "estoy estudiando POO"

# class trabajador(persona):
#     def __init__(self, nombre: str, edad: int, sexo: str,profesion:str):
#         super().__init__(nombre, edad, sexo)
#         self.profesion=profesion
#     def trabajar():
#         return "estoy en mi trabajo"
    
# class vehiculo:
#     def __init__(self,marca:str,modelo:str,color:str,ruedas:int):
#         self.modelo=modelo
#         self.color=color
#         self.ruedas=ruedas
#     def prender(self,plato_favorito:str):
#         return f"yo {self.nombre} estoy comiendo mi {plato_favorito}"
    
#     def apagar(self):
#         return "pipi popo"
#     def retroceder(self):
#         return "pipi popo"
    
# class estudiante(vehiculo):
#     def __init__(self, nombre: str, edad: int, sexo: str,carrera_profecional:str):
#         super().__init__(nombre, edad, sexo)
#         self.carrera_profecional=carrera_profecional
#     def estudiar(self):
#         return "estoy estudiando POO"

# class trabajador(vehiculo):
#     def __init__(self, nombre: str, edad: int, sexo: str,profesion:str):
#         super().__init__(nombre, edad, sexo)
#         self.profesion=profesion
#     def trabajar():
#         return "estoy en mi trabajo"
    
class Vehiculo:
    def __init__(self, marca: str, modelo: str, color: str, ruedas: int):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.ruedas = ruedas

    def prender(self, plato_favorito: str):
        return f"Yo {self.marca} {self.modelo} estoy comiendo mi {plato_favorito}"

    def apagar(self):
        return "pipi popo"

    def avanzar(self):
        return "avanzando"

    def retroceder(self):
        return "retrocediendo"

class Auto(Vehiculo):
    def __init__(self, marca: str, modelo: str, color: str, ruedas: int, rpm: int):
        super().__init__(marca, modelo, color, ruedas)
        self.rpm = rpm

    def vehiculo_nitro(self):
        return "¡Usando nitro para aumentar la velocidad!"
    
class Omnibus(Vehiculo):
    def __init__(self, marca: str, modelo: str, color: str, ruedas: int, numero_asientos: int):
        super().__init__(marca, modelo, color, ruedas)
        self.numero_asientos = numero_asientos

    def recojer_pasajero(self):
        return "Recogiendo pasajeros"

omnibus1 = Omnibus("Mercedes", "Sprinter", "Blanco", 6, 20)
print(omnibus1.prender("sandwich"))
print(omnibus1.avanzar())
print(omnibus1.recojer_pasajero())

omnibus2 = Omnibus("Volvo", "XC60", "Gris", 4, 30)
print(omnibus2.prender("frutas"))
print(omnibus2.avanzar())
print(omnibus2.recojer_pasajero())


auto1 = Auto("Toyota", "Corolla", "Azul", 4, 2000)
print(auto1.prender("arroz"))
print(auto1.avanzar())
print(auto1.vehiculo_nitro())

auto2 = Auto("Ford", "Focus", "Rojo", 4, 1800)
print(auto2.prender("ensalada"))
print(auto2.avanzar())
print(auto2.vehiculo_nitro())
