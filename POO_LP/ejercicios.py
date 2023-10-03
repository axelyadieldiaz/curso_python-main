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
class avion:
    aerolineas="avianca"
    color="blanco"
    motores="cuantro motores"

    def motor(self):
        return "el Boeing 737"
    def velocidad(self):
        return "de 885/933 Km/h"

respuesta=celular()
print(respuesta.marca)
print(respuesta.motor())
print(respuesta.velocidad(10))
# haciendo uso de la POO crear un objeto para entidad dota2
class heroe:
    nombre="Jinx"
    rol="tirador"
    edad=19

    def habilidad_pasiva(self):
        return "gran aumento de velocidad de movimiento y velocidad de ataque"
    
    def habilidad_q(self):
        return "¡Cambiazo!: Jinx modifica sus ataques básicos al alternar entre Pium Pium, su ametralladora, y Espinas, su lanzacohetes."
    
    def habilidad_w(self):
        return "¡Zap!: Jinx usa a Chispita, su pistola de rayos, para disparar un rayo que ralentiza e inflige daño al primer enemigo que golpea, revelándolo."
    
    def habilidad_e(self):
        return "¡Mascafuegos!: Jinx lanza una hilera de granadas paralizantes que explotan tras 5 s y envuelven en llamas a los enemigos circundantes."
    
    def habilidad_r(self):
        return "¡Supermegacohete mortal!: Jinx dispara un supercohete por todo el mapa que va aumentando su daño a medida que avanza"

print(heroe.nombre)
# haciendo uso de POO crear un objeto para una pc 
class pc:
    componentes="teclado, mouse"
    color="negro"

    def prender(self):
        return "preciona el boton de encendido"
    def teclado(self):
        return "escribe lo que quieras"
    
print(pc.componentes)
# haciendo uso de POO crear un objeto para una improsora
class impresora:
    color="blanco"
    tinta="negro,amarillo,azul,rojo"

    def imprimir(self):
        return "imprime una hoja"
    def escan(self):
        return "escanea el documento que desees"
    
print(impresora.tinta)
# haciendo eso de la POO crear un objeto para emitir una factura
class factura:
    nombre="nombre del cliente"
    DNI= "12343536"
    RUC= "9743895349"

    def producto(self):
        return "el nombre del producto comprado"
    def IGV(self):
        return "impuesto general de la venta"
    
print(factura.nombre)
