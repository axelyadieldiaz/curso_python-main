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

## 1. crear un objeto CLASE laptop con dos atributos de clase y 5 atributos de instancia
# debera tener hasta 3 funcionalidades como minimo
#crear tres objetos instancia de clase distintos
### ojo: solo utilizar lo que hemos echo en clase
class laptop:
    familia1='intel CORE'
    familia2='16.5 pulgadas'

    def __init__(self,marca,modelo,microprocesador,memoria_RAM,HDMI):
        self.marca=marca
        self=modelo=modelo
        self.microprocesador=microprocesador
        self.memoria_RAM=memoria_RAM
        self.HDMI=HDMI

    def encerder(self,):
        print(f'laptop {self.modelo} se esta encendiendo...')
    def apagar(self,):
        print(f'la laptop {self.modelo}se esta apagando...')
    
    def mostrar_informacion(self):
        print(f'imformacion de la laptop {self.modelo}:')
        print(f'marca: {self.marca}')
        print(f'modelo: {self.modelo}')
        print(f'memoria_RAM: {self.memoria_RAM}')
        print(f'HDMI: {self.HDMI}')


laptop1 = laptop("dell XPS 13", 1300, 15, 512, 13.3, "plateado")
laptop2 = laptop("HP Spectre x360", 1300, 10, 256, 15.6, "gris")
laptop3 = laptop("lenovo trinkpad", 900, 12, 256, 15, "negro")

laptop1.encerder()
laptop1.mostrar_informacion()
laptop1.apagar()

laptop2.encerder()
laptop2.mostrar_informacion()
laptop2.apagar()

laptop3.encerder()
laptop3.mostrar_informacion()
laptop3.apagar()


## crear una clase puesto de mercado que tenga un atributo de clase 5 atributos de instancia y 5 funcionalidades
# debera crear 4 instancias de la clase mercado
## ejemplo puesto mechita, puesto la gringa, puesto ojo de uva
class Mercado:
    medida="establecimiento"

    def _init_(self,nombre_puesto,sexo,color,tipo_de_puesto,productos):
        self.nombre_puesto=nombre_puesto
        self.sexo=sexo
        self.color=color
        self.tipo_de_puesto=tipo_de_puesto
        self.productos=productos

    def entrada_de_cliente(self,nombre):
        return f"el cliente {nombre} entro"
    
    def compro(self,client,product):
        return f"{client} compro este producto: {product}"
    
    def salir(self,client):
        return f"el client {client} salio por la puerta"
    
# objeto 1
clientvirgen=Mercado("puesto mechita","femeninio","azul","comida","cebiche")
print(clientvirgen.tipo_de_puesto)
print(clientvirgen.productos)
print(clientvirgen.entrada_de_cliente("orlando"))
print(clientvirgen.compro("orlando","cebiche"))
# objeto 2
clientjona=Mercado("la gringa","femeninio","rosa","venta de celulares","S23 Ultra")
print(clientjona.tipo_de_puesto)
print(clientjona.productos)
print(clientjona.entrada_de_cliente("jhonatan devorador de mundos"))
print(clientjona.compro("jhonatan","S23 Ultra"))
# objeto 3
clientjona=Mercado("la gringa","femeninio","rosa","venta de celulares","S23 Ultra")
print(clientjona.tipo_de_puesto)
print(clientjona.productos)
print(clientjona.entrada_de_cliente("jhonatan devorador de mundos"))
print(clientjona.salir("hans"))
# objeto 4
clientchina=Mercado("los facheros","masculino","naranja","venta de ropa","zapatos")
print(clientchina.tipo_de_puesto)
print(clientchina.productos)
print(clientchina.entrada_de_cliente("jhonatan devorador de mundos"))
print(clientchina.salir("china"))