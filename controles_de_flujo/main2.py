# frutas=[]
# while len(frutas)<5:
#     nuevafruta=input("ingresa una fruta: ")
#     if nuevafruta in frutas:
#         print("esta fruta ya existe huevonaso ingresa otro pendejo")
#     else:
#         frutas.append(nuevafruta)

# def textolargo(array):
#     longitudtexto=0
#     mostrarfruta=""
#     for index in range(0,len(array)):
#         if len(array[index]) > longitudtexto:
#             longitudtexto=len(array[index])
#             mostrarfruta=array[index]
#     return mostrarfruta

# print(textolargo(frutas))

def agregar_empresa(empresas):
    nombre = input("Ingrese el nombre de la empresa: ")
    ruc = input("Ingrese el RUC de la empresa: ")
    direccion = input("Ingrese la dirección de la empresa: ")
    sucursales = int(input("Ingrese el número de sucursales de la empresa: "))
    horario_dia = input("Ingrese el horario de atención en el día: ")
    horario_noche = input("Ingrese el horario de atención en la noche: ")

    empresas.append({
        "nombre": nombre,
        "ruc": ruc,
        "direccion": direccion,
        "sucursales": sucursales,
        "horario_dia": horario_dia,
        "horario_noche": horario_noche
    })

# Programa principal
if __name__ == "__main__":
    empresas = []

    while True:
        print("\n1. Agregar empresa")
        print("2. Salir")

        opcion = input("Seleccione una opción (1/2): ")

        if opcion == "1":
            agregar_empresa(empresas)
        elif opcion == "2":
            break
        else:
            print("Opción inválida. Intente nuevamente.")
