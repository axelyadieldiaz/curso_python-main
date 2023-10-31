# # crear clase de usuario
# # esta clase tendra los siguientes metodos 
# # actualizar edad del usuario 
# # verificar si usuarios 
# # verificar si usuario esta registrado o existe en mis registros 
# # validar usuario y password
from bd import *

class Usuario:
    def __init__(self, bd_users):
        self.bd_users = bd_users

    def calcular_edad(self, dni):
        user = next((el for el in self.bd_users if el['dni'] == dni), None)
        if user:
            fecha_nacimiento = int(user['fecha_nacimiento'][6:])
            año_actual = 2023
            edad_actual = año_actual - fecha_nacimiento
            return edad_actual
        else:
            return 'Usuario no encontrado'

    def actualizar_edad(self, dni, clave, valor_nuevo):
        for user in self.bd_users:
            if user['dni'] == dni:
                user[clave] = valor_nuevo
                return 'Edad actualizada'
        return 'Usuario no encontrado'

    def usuario_existe(self, dni, usuario):
        user_exists = any(el['dni'] == dni and el['usuario'] == usuario for el in self.bd_users)
        if user_exists:
            return f'El usuario {usuario} existe'
        else:
            return f'El usuario {usuario} no existe'

    def login_usuario(self, usuario, password):
        user_login = next((el for el in self.bd_users if el['usuario'] == usuario and el['password'] == password), None)
        if user_login:
            return f'''
            Bienvenido a su perfil!
            
            Aquí están sus datos: 😊
            ---------------------------------------------------------------------------------------------------------------------
            {user_login}
            ---------------------------------------------------------------------------------------------------------------------
            '''
        else:
            return 'Su usuario y contraseña son incorrectos'

registro = Usuario(usuarios)

registro.actualizar_edad('4', 'edad', registro.calcular_edad('4'))
print(registro.usuario_existe('4', 'jory'))
print(registro.calcular_edad('4'))
print(registro.login_usuario('jory', 'a111'))
print(usuarios)
