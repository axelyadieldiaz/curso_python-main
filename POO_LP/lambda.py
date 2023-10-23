# lambda una funcion que se autoejecuta
hola=lambda a,b:print(a+b)
#funcion normal
def suma(a,b):
    print(a+b)
suma(4,6)
hola(10,20)

# if ternario
ternario="soy verdad ternario" if True else "soy falso ternario"
print(ternario)
# if normal
if True:
    print("soy verdad")
else:
    print("soy mentira")


lista_alumnos=[
    {
        "nombre":"edwin",
        "edad":15,
        "hobby":"danza",
        "flaquita":"melody"
    },
    {
        "nombre":"del mar",
        "edad":30,
        "hobby":"saltar",
        "flaquita":"melody"
    },
    {
        "nombre":"orlando",
        "edad":14,
        "hobby":"ponchar",
        "flaquita":"sami"
    },
    {
        "nombre":"jory",
        "edad":50,
        "hobby":"aplicar",
        "flaquita":"sami"
    },
    {
        "nombre":"hans",
        "edad":13,
        "hobby":"quemarse",
        "flaquita":"hermana"
    }
]
print(f"todos mis alumnitos {lista_alumnos}")
fans_melody=list(filter(lambda par:par["flaquita"]=="melody",lista_alumnos))
print(f"loz que quieren con melody{fans_melody}")
#################################################################################
nuevo_objet=list(map(lambda par:{"nombre_alumno":par["nombre"],"germita":par["flaquita"]},lista_alumnos))
print(nuevo_objet)