##crear un programa que me pida los siguientes datos nombres, apellidos,dni, programa de
## estudio, de las unidades didacticas pedira los siguientes datos el nombre de la unidad
## y el promedio de la condicion se autocomplementar en relacion del promedio.
#el objeto trendra la siguiente estructura                                      
alumnos={
    "nombre":"jose"
    "apellidos":"alvarez escobar"
    "dni":31293672,
    "programa_de_estudios":"arquitectura",
    "unidades-didacticas":[
        {"lenguaje_de_programacion":{"promedio":15,"condicion":"aprovado"}},
        {"herramientas_desarrollo_software":{"promedio":12,"condicion","desaprovado"}}
    ]
}


def ingresar_unidades_didacticas():
    unidades = []
    while True:
        nombre_unidad = input("Ingrese el nombre de la unidad didáctica (o 'fin' para terminar): ")
        if nombre_unidad.lower() == 'fin':
            break
        promedio = float(input("Ingrese el promedio de la unidad: "))
        if promedio >= 10:
            condicion = "aprobado"
        else:
            condicion = "desaprobado"
        unidades.append({nombre_unidad: {"promedio": promedio, "condicion": condicion}})
    return unidades

def main():
    alumnos = []
    while True:
        alumno = {}
        alumno["nombre"] = input("Ingrese el nombre del alumno: ")
        alumno["apellidos"] = input("Ingrese los apellidos del alumno: ")
        alumno["dni"] = int(input("Ingrese el DNI del alumno: "))
        alumno["programa_de_estudios"] = input("Ingrese el programa de estudios: ")
        alumno["unidades_didacticas"] = ingresar_unidades_didacticas()
        alumnos.append(alumno)
        
        continuar = input("¿Desea agregar otro alumno? (s/n): ")
        if continuar.lower() != 's':
            break
    
    print("Información de los alumnos:")
    for alumno in alumnos:
        print(alumno)

if __name__ == "__main__":
    main()
