# REPASO PYTHON


## TIPOS DE DATOS
  **Tipos  de datos primitivos**
 ```python
 'a' # string cadena texto
 'hola' # esto tambien es un string
 'hola soy un string y te saludo' # cadena larga
 ```
**OBSERVACION :**  *Todo lo que este entre comillas  es un* **string**.

```python
'100'
'false'
"hola"
```
*Aun string puede estar entre comillas dobles ("") o comillas simples (´´)*
```python
100 # esto es un tipo de dato numerico entero intiger 
2.1  # Esto es un dato de tipo numerico de tipo flotante Float
```





## VARIABLES
*Es donde almacenamos nuestro tipo de dato,estos datos pueden **mutar cambiar o modificarse** como creamos una variable para almacenar nuestros datos.*
1. Darle un nombre **significativo** o relacionado al dato que estamos almacenando.
2. Indicar el tipo de dato esta relacionado → asignacion =.
3. Indicar el tipo de dato que se va almacenar → darle el dato a guardar.

```python
# primero el dato lo voy a pedir la edad a nadine
edad_nadine=18

#El nombre de un alumno
 nombre_alumno='Edwin'
```

## OPERADORES
1. Existen los operadores aritmetico
 * suma 
 * resta
 * multiplicacion
 * divicion
  
 **SUMA**
```PYTHON
Suma = 45+12
```
**RESTA**
```PYTHON
Resta = 45-12
```
**MULTIPLICACION**
```PYTHON
Multiplicacion =45*12
```
**DIVICION**
```PYTHON
 Divcion = 45/12
```

```PYTHON
operacion=(45+12+23)/4
op=15+12+14+13/4
#Presedencia de operadores
```
### OPERADORES DE  DE USO ESPECIAL
```PYTHON
# OPERADOR DE USO ESPECIAL (SUMA)
suma=45+47 # Operador suma resultado 87
suma='45' + 12 # Operador  concatenacion resultado 4512
saludo= 'Hola'+'Mundo' # concatenacion HolaMundo
saludo2='Hola'+''+'Mundo' # concatenar Hola Mundo
# OPERADOR DE USO ESPECIAL (MULTIPLICAR)
saludos='hola'*2 #holahola
saludo1s='hola '*2 #hola hola
```


## DATOS ESTRUCTURADOS

## LISTAS
Se puede almacenar distintos tipos de datos en una sola lista separados por coma.

```PYTHON
 Lista=['nombre',10, False]
 Lista_amigos=['jory','ñawi','adan','chinita']
```
## OBJETOS

Tambien al ygual que las listas almacenas distintos tipos de dstos, pero con un orden.

Para almacenar datos de un objeto nesesitamos especificar in indice y un valor indice →valor
```PYTHON
{
    'nombre':'jory',
    'edad':54
    'sexo' : 'todos los dias'
}
###################################
#combinar ambas estructura de datos
alumno={
    'nombre':'jory',
    'edad':54
    'amigos': [ 'antony','edwin','china'],
    'direccion':{
        'departamento': 'ayacucho',
        'provincia': 'lucanas',
        'distrito': 'puquio',
        'jiron': ' cusco',
        'numero':125

    }
}
 alumnos=[{},{},{}]
```
## CONTROLES DEN FLUJO
### DECISIONES
Solo se ejecuta el codigo si cumple la condicion es verdadera,  podemas hacer si la condicion sea falsa se ejeute otro codigo.

**SINTAXIS**

Primero especificar el codigo que ejecutara si cumple una condicion
```PYTHON
if <condicion>:
    ## El codigo que deseamos ejecutar si la condicion es verdad
    print('Ejecuta esto')
## Aqui estamos fuera del if o del si este codigo siemprese ejecutara no depende del if
print('Esto siempre ejecutara')
#---------------------------------------------------------------------
# Si queremos que se ejecute un codigo en caso sea falso
if <condicion falsa>:
    print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
```
**EJEMPLITOS**

```PYTHON
if 15>18:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```
```PYTHON
if 15*2==30:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```
```PYTHON
condicion= True
if  condicion:
        print('Solo imprime si es verdad')
else:
    print('Solo imprime si es falso')
    
```



## CICLOS
**EXISTEN  DOS TIPOS**

* Cuando sabemos la cantidad de veses que vamos a repetir algo.
Para este caso existe el **FOR**. Sintaxis despues de la palabra reservada **FOR**  deberemos crear una variable que almacene el numero que iremos intentando.luego tendremos que indicar el rango a intentar a los elementos a intentar.
```PYTHON
for i in range(1,5):
    print(i)
```
```PYTHON
vocales=['a','e','i','o','u']
for i in vocales:
    print (i)
```
```PYTHON
numeros=['45','12','78','1','2']
for i in numeros:
    print (i)
```


* Cuando no sabesmos la cantidad de veses que vamos a repetir algo.

condicion=true
while condicion:
    print ("hola")
    texto=input("ingresa tu nombre o salir para terminar elprograma: ")
    if texto=="salir"
    condicion=false
    








## ESTRUCTURAS DE FLUJO

## FUNCIONES 
existen 2 tipos de funciones 
## propias del leguaje 
que ya bienen creadas e insertadas en python y etan listas para ser usadas
## estructura de uso de una funcion
tiene el nombre seguido del parentesis,
dentro de la parentesis podremos pasarles datos que necesita la funcion para 
ejecutarse 
## esta es un funcion que nos sirve para mostrar por consola datos
```PYTHON
print("hola")
## len nos devuelve un numero
print(len([1,5,6,7,8]))
### este es una funcion que se detiene a esperar que el usuario introdusca informacion
### entre parentesis podremos escribir mensaje que indique que accion realizara el usuario
input("ingresa ingresa")

# esta funcion nos muestra el numero mayor de una lista
lista=[45,12,78,3,24,50]
numero_mayor=max([45,12,78,3,24,50])
print(numero_mayor)

# esta funcion nos muestra el numero menor de una lista 
lista=[45,12,78,3,24,50]
numero_menor=min([45,12,78,3,24,50])
print(numero_menor)

# funcion para convertir un string a un numero entero
int('100') # ->> 100 ->> entero
numero_string='100'
print(type(numero_string))
numero_entero=int(numero_string)
print(type(numero_entero))

# funcion para convertir un entero a un string 
str(100) # ->> '100' ->> string

# funcion de python que nos permite agregar elementos al final de una lista
lista=[15,12,78]
lista.pop()
print(lista)

#funcion de python que nos permite agregar elemtos en cualquier pocision de mi lista para eso se le tiene que pasar dos parametros, primero indicarle el indice y segundo el dato que se va a agregar
lista_nombres=['jory','nadine','bichota']
lista_nombres.insert(1,'satan')
print(lista_nombres)

# funcion de python que nos permite eliminar elementos de cualquier pocision de una lista, esta funcion recibe solo el elemento que deseamos eliminar 
lista=[4,5,6,8,7]
lista.remove(6)
print(lista)

# fucion que nos permite dividir en una lista de cadena
cadena='hola como estan'
lista=cadena.split()
print(lista)
url='www.golle.com/id=70133573'
id=url.split('=').pop()
print(id)

### 2. funciones creadas
# una funcion son mini programas tambien se le conoce como modulos o fragmentos de codigo de uso exclusivo
# funciones propias
# pasos para crear una funcion propia
# 1. hacer uso de la palabra recervada def
# 2. definir un nombre de  funcion que describa que tarea va a realizar
# 3. establecer los parametros que resivira la funcion entre parenresis ().
# 4. establecer que valor o dato va retornar mi funcion con la palabra reservada retrun
#> observacion =>> tambien podemos hacer uso de la funcion print () para retornar un mensaje en nuestra funcion.
def saludo():
    print('hola este es un saludo')

# como hacemos uso de la funcion??
# nombre de la funcion y parentesis

## funcion con parametros

def mi_print(texto):
    print(texto)

# print('hola este es print de python')
# mi_print('hola este es mi print creado')

def suma(a,b):
    total=a+b
    return total

mi_print(suma(45,12)) =>>>>>>> 57

################################################
#ejemplo
# para que se usa esta funcion
# para mostrar el valor maximo de una lista
lista=[12,4,45,78,3,1]
max(lista) # ===>>> 78

def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
            numero_mayor=numero
    return numero_mayor
mi_print(mi_max(lista))
```
```PYTHON
# funciones con muchos parametros 
def funcion(*muchos_parametros):
    total=0
    for numero in muchos_parametros:
        total=total+numero
    return total
print(funcion(45,23,65,32,124))

def datos(*args):
    nombre=args[0]
    apellidos=args[1]
    edad=args[2]
    return f'mi nombre es,{nombre},{apellidos} y mi edad es,{edad}'
print(datos('edwin','apellidos','34'))
