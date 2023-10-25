# en nombre siempre debera ser un  singular y con la primera letra mayuscula
# class Perro:
#     nombre="boby"
#     edad="2 meses"
#     color="cheqche"
#     raza="chusterrier"

#     def ladrar(self):
#         return "gua gua mascota"
#     def corre(self,pasos):
#         huevo=f"corriste {pasos}, pasos"
#         return huevo

# respuesta=Perro()
# print(respuesta.nombre)
# print(respuesta.ladrar())
# print(respuesta.corre(10))

class Tienda:
    def __init__(self, nombre, gerente):
        self.nombre = nombre
        self.gerente = gerente

# Lista de tiendas
tiendas = [
    Tienda("El Pichilón", "Nadine"),
    Tienda("La Botica", "Cristian"),
    Tienda("Supermercado XYZ", "Edwin"),
    Tienda("Cafetería del Sol", "China"),
    Tienda("La Farmacéutica", "Cristian"),
    Tienda("Mini Market A1", "Nadine"),
    Tienda("Restaurante Sabores", "China"),
    Tienda("La Esquina", "Edwin"),
    Tienda("Farmacia Rápida", "Cristian"),
    Tienda("Bodega Económica", "Edwin")
]

# Método para filtrar tiendas por gerente
def tiendas_por_gerente(gerente):
    return [tienda.nombre for tienda in tiendas if tienda.gerente == gerente]

# Método para mostrar tiendas con más de un gerente
def tiendas_con_mas_de_dos_gerentes():
    gerente_count = {}
    for tienda in tiendas:
        gerente_count[tienda.nombre] = gerente_count.get(tienda.nombre, 0) + 1
    return [nombre for nombre, count in gerente_count.items() if count > 1]

# Ejemplos de uso
print("1. Tiendas de Cristian:")
cristian_tiendas = tiendas_por_gerente("Cristian")
print(cristian_tiendas)

print("\n2. Tiendas con más de un gerente:")
mas_de_dos_gerentes = tiendas_con_mas_de_dos_gerentes()
print(mas_de_dos_gerentes)
