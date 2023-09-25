## averiguar funciones de python mas usadas, con sus ejemplos practicos 
1.- print() imprime texto en la consola.

```PYTHON
print("Hola, mundo!")
```

2.- input(): Lee la entrada del usuario desde la consola.

```PYTHON
nombre = input("Ingrese su nombre: ")
```

3.- len(): Calcula la longitud de una cadena o lista.

```PYTHON
cadena = "Python"  
longitud = len(cadena)
```

4.- range(): Genera una secuencia de números.

```PYTHON
numeros = list(range(1, 6))
```

5.- if/else: Estructuras de control condicional.
```PYTHON
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```
6.- for loop: Itera sobre una secuencia.
```PYTHON
frutas = ["manzana", "plátano", "naranja"]
for fruta in frutas:
    print(fruta)
```
7.- while loop: Itera mientras se cumple una condición.
```PYTHON
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```
8.- funciones: Define funciones reutilizables.
```PYTHON
def suma(a, b):
    return a + b

resultado = suma(3, 5)
```
9.- Listas: Estructuras de datos para almacenar elementos.
```PYTHON
numeros = [1, 2, 3, 4, 5]
```
10.- Diccionarios: Estructuras de datos clave-valor.
```PYTHON
persona = {"nombre": "Juan", "edad": 30}
```
11.- Métodos de cadena: Manipulación de cadenas.
```PYTHON
frase = "¡Hola, mundo!"
mayusculas = frase.upper()
```
12.- Métodos de lista: Operaciones en listas.
```PYTHON
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numeros.sort()
```
13.- Módulos y librerías: Importar funcionalidad adicional.
```PYTHON
import math
raiz_cuadrada = math.sqrt(25)
```
14.- Manejo de excepciones: Captura y manejo de errores.
```PYTHON
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("¡Error! No se puede dividir por cero.")
```
15.- Archivo de lectura/escritura: Leer y escribir en archivos.
```PYTHON
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
```

## averiguar sobre entornos virtuales en python

1. instalar 'virtualesv' (si no esta instalado):
Si aún no tienes virtualenv instalado, puedes hacerlo utilizando pip:
```PYTHON
pip install virtualenv
```
2. Crear un nuevo entorno virtual:
Para crear un nuevo entorno virtual, ejecuta el siguiente comando en tu terminal:
```PYTHON
virtualenv nombre_del_entorno
```
3. Activar el entorno virtual:
Dependiendo de tu sistema operativo, la forma de activar un entorno virtual varía:
En windows (cmd)
```PYTHON
nombre_del_entorno\Scripts\activate
```
En windows (powersell)
```PYTHON
.\nombre_del_entorno\Scripts\Activate.ps1
```
En macOS y linux:
```PYTHON
source nombre_del_entorno/bin/activate
```
4.  Instalar paquetes en el entorno virtual:
Con el entorno virtual activado, puedes usar pip para instalar bibliotecas específicas dentro de ese entorno. Por ejemplo:
```PYTHON
pip install nombre_de_paquete
```
5.  Desactivar el entorno virtual:
Puedes desactivar el entorno virtual en cualquier momento ejecutando el siguiente comando:
```PYTHON
deactivate
```
6. Eliminar un entorno virtual:
Si ya no necesitas un entorno virtual, simplemente puedes eliminar la carpeta que lo contiene.