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