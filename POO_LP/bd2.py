# crear una lista de objetos
# cada objeto tedra los datos de una persona 
# nombre, edad, f_nacimiento, dni, usuario, password
# minimo 5 registros maximo 10 registros
usuarios=[{
    "dni":12345678,
    "nombre":"moises",
    "f_nacimiento":"12/10/2000",
    "edad":"",
    "usuario":"admin",
    "password":"1234"
    },{}]

class Persona:
    def __init__(self, dni, nombre, f_nacimiento, edad, usuario, password):
        self.dni = dni
        self.nombre = nombre
        self.f_nacimiento = f_nacimiento
        self.edad = edad
        self.usuario = usuario
        self.password = password

personas = [
    Persona(12345678, "Moisés", "12/10/2000", 19, "admin", "1234"),
    Persona(87654321, "China", "05/03/1995", 18, "maria95", "clave123"),
    Persona(98765432, "Edwin", "15/09/1990", 20, "juan90", "contraseña456"),
    Persona(23456789, "nando", "20/07/1998", 21, "ana98", "secreto789"),
    Persona(34567890, "yerald", "02/12/1985", 19, "luis85", "password123")
]

for persona in personas:
    print(f"DNI: {persona.dni}, Nombre: {persona.nombre}, Fecha de Nacimiento: {persona.f_nacimiento}, Edad: {persona.edad}, Usuario: {persona.usuario}, Contraseña: {persona.password}")
