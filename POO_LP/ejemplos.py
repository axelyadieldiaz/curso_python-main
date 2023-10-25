# crear un sistema de gestion control del stockl de productos.
# caso de uso
# historias de usuario
# producto ower
# baclog
# MVP
# prototipos de mierda

# entidad entitis
# la base de datos sobre lo que voy a trabajar
# averiguar formas normales (normalizacion de base de datos)
# productos=[
#     {
#         "id":1,
#         "codigo":"2023-A"
#         "nombre":"arroz",
#         "descripcion":"costeño costal x 100 k",
#         "stock":5,
#         "unidad":"costales",
#         "precio":125,
#         "moneda":"soles"
#     }
# ]
# # # caso de uso 
# class Producto:
#     # atributos de instancia
#     def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
#         self.nombre=nombre
#         self.descripcion=descripcion
#         self.stock=stock
#         self.unidad=unidad
#         self.precio=precio
#         self.moneda=moneda
#     # creacion de metodos
#     def mostrar_productos(self):
#         mensaje=f"""tienes
#         tienes {len(productos)}productos
#         los productos son:
#         {productos}
#         """

#         return mensaje
#     def regristrar_producto(self):
#         nuevo_id=len(productos)+1
#         producto_nuevo={
#             "id":nuevo_id,
#             "codigo":self.codigo,
#             "nombre":self.nombre,
#             "descripcion":self.descripcion,
#             "stock":self.stock,
#             "unidad":self.unidad,
#             "precio":self.precio,
#             "moneda":self.moneda
#         }
#         registrar_producto=productos.append(producto_nuevo)
#         return f"el siguiente producto se registro exitosamente{producto_nuevo}"
    
#     def mostrar_producto(self,id):
#         Producto_buscar=productos[id-1]
#         return Producto_buscar
    
#     def eliminar_producto(self,id):
#         producto_eliminar=productos.pop(id-1)
#         return f"el siguiente producto fue eliminado {producto_eliminar}"
    
#     def actualizar_producto(self,id,clave,valor):
#         ol=valor
#         producto_actualizar=list(filter(lambda obje: obje[clave]==id,productos))[0].update({clave:valor})
#         return "se actualizo"
#         # list funcion para crear lista

# ### programacion funcional en python
# ### metodo funcional filter retorna una lista con el elemento que se true de una lista 
# ### funciones anonimos o autoejecutadas en python se les conoce como funciones 
# ### lambda -> funcion anonima
# # su uso estructura
# # lambda a,b: retrun a+b # esta funcion se autoejecuta no se llama 
# # suma= lambda  a,b:return a+b # para ejecutar esta funcion necesito llamar a la variable suma
# prod=Producto("aceite","extra virgen",2,"botella x litro", 12.50)
# print(prod.regristrar_producto())
# print(prod.mostrar_productos())
# print(prod.actualizar_producto(125,"precio",130))
# # print(prod.mostrar_producto(1))
# # print(prod.eliminar_producto(2))
# print(prod.mostrar_productos())

# Lista de estudiantes (inicialmente vacía)
# estudiantes = []

# class Estudiante:
#     def __init__(self, nombre, edad, curso, promedio):
#         self.nombre = nombre
#         self.edad = edad
#         self.curso = curso
#         self.promedio = promedio

#     def mostrar_estudiantes(self):
#         mensaje = f"Tienes {len(estudiantes)} estudiantes registrados."
#         mensaje += "Los estudiantes son:"
#         for estudiante in estudiantes:
#             mensaje += f"Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Curso: {estudiante['curso']}, Promedio: {estudiante['promedio']}\n"
#         return mensaje

#     def registrar_estudiante(self):
#         nuevo_id = len(estudiantes) + 1
#         nuevo_estudiante = {
#             "id": nuevo_id,
#             "nombre": self.nombre,
#             "edad": self.edad,
#             "curso": self.curso,
#             "promedio": self.promedio
#         }
#         estudiantes.append(nuevo_estudiante)
#         return f"El siguiente estudiante se registró exitosamente:{nuevo_estudiante}"

#     def mostrar_estudiante(self, id):
#         if 1 <= id <= len(estudiantes):
#             estudiante = estudiantes[id - 1]
#             return f"Estudiante #{id}: Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Curso: {estudiante['curso']}, Promedio: {estudiante['promedio']}"
#         else:
#             return "ID de estudiante no válido."

#     def eliminar_estudiante(self, id):
#         if 1 <= id <= len(estudiantes):
#             estudiante_eliminado = estudiantes.pop(id - 1)
#             return f"El siguiente estudiante fue eliminado:{estudiante_eliminado}"
#         else:
#             return "ID de estudiante no válido."

#     def actualizar_estudiante(self, id, nombre, edad, curso, promedio):
#         if 1 <= id <= len(estudiantes):
#             estudiante_actualizado = estudiantes[id - 1]
#             estudiante_actualizado["nombre"] = nombre
#             estudiante_actualizado["edad"] = edad
#             estudiante_actualizado["curso"] = curso
#             estudiante_actualizado["promedio"] = promedio
#             return f"Estudiante actualizado:{estudiante_actualizado}"
#         else:
#             return "ID de estudiante no válido."

# # Ejemplo de uso
# estudiante1 = Estudiante("axel", 18, "Matemáticas", 95.5)
# estudiante2 = Estudiante("china", 20, "Historia", 89.0)
# print(estudiante1.registrar_estudiante())
# print(estudiante2.registrar_estudiante())
# print(estudiante1.mostrar_estudiantes())
# print(estudiante1.mostrar_estudiante(1))
# print(estudiante1.eliminar_estudiante(2))
# print(estudiante1.mostrar_estudiantes())
# print(estudiante1.actualizar_estudiante(1, "axel yadiel", 19, "Física", 92.5))
# print(estudiante1.mostrar_estudiantes())


from bd import *
class tiendas_comerciales:

    def tienda_gerente(self,bd_negocios, nombre_gerente):
        respuesta=list(filter(lambda el:el ["gerente"]==nombre_gerente, bd_negocios))
        return respuesta
    
    def tiendas_mas_categorias(self,bd_negocios):
        respuesta=list(filter(lambda el: len(el["categoria"])>2, bd_negocios))
        return respuesta

    def ruc_nombre(self,bd_negocios):
        respuesta=list(map(lambda el:{
            "nombre_negocio":el["nombre"],
            "ruc_negocio":el["ruc"]
        },bd_negocios))
        return respuesta
    
    def eliminar_negocio(self,bd_negocios,ruc):
        respuesta=list(filter(lambda el:el["ruc"] !=ruc,bd_negocios))
        return respuesta
######## tarea
## otro metodo para crear un nuevo producto
    def crea_negocio(self,ruc: int, nombre: str, categoria: str, horario_atencion: str, gerente:str):
        negocios.append({
        "ruc": ruc,
        "nombre": nombre,
        "categoria": categoria,
        "horario_atencion": horario_atencion,
        "gerente": gerente
        })
## otro metodo para actualizar el horario de atencion
    def actualizar_horario(self, ruc: int, horario_atencion: dict):
        (negocio.update({'horario_atencion': horario_atencion})for negocio in negocios if negocio["ruc"]==ruc)
        print(f'horario de atencion actualizado: {horario_atencion}')
gerente=tiendas_comerciales()
# print(gerente.tienda_gerente(negocios,"china"))
# print(gerente.tiendas_mas_categorias(negocios))
# print(gerente.ruc_nombre(negocios))
# print(gerente.eliminar_negocio(negocios,1234))
gerente.crea_negocio(ruc=518915, nombre="yadiel", categoria=["burdel"," las cariñosas"],horario_atencion={"dia": "8am-2pm"}, gerente="axel")
gerente.actualizar_horario(ruc=123456789, horario_atencion={"dia": "9am-6pm"})