## bucles
# condicion=0
# while condicion<11:
#     print("condicion")
#     condicion=condicion+1

# hola=0
# while hola<17:
#     print("hola")
#     hola=hola+1

# edad=0
# while edad != 20:
#     edad=int(input("ingrese su edad: "))

# nombre=""
# while nombre != "si":
#     nombre=input("ingresa tu nombre: ")

# while True:
#     nombre=input('como te llamas:')
#     if nombre == 'si':
#         break

# for numero in range(1,20):
#     print(numero)

# vocales=['a','e','i','o','u']
# for numero in range(0,5):
#     print(vocales[numero])

# for voca in vocales:
#     print(vocales)

## crear una lista de cinco colores cada color que interes
## tendras que mostrar por consola, solo cuando encuentre el
## color rojo mostrara el mensaje de 
## color encontrado y se terminara la ejecucion

# colores = ['azul','naranja','negro','rojo','blanco']
# for color in colores:
#     if color == "rojo":
#         print("color encontrado.")
#         break
#     print(color)

# lista=[]
# print(lista)
# primerdato=input('ingresa una fruta: ')
# lista.append(primerdato)
# print(lista)
# segundodato=input('ingrese su segunda fruta: ')
# lista.append(segundodato)
# print(lista)

## crear un programa que me deje ingresar datos de una lista vacia
##en caso el usuario ingrese la palabra 'si'el programa dejara
##de pedir datos y me mkostrara la lista con todos los datos ingresados
# lista_datos = []

# while True:
#     entrada = input("Ingrese un dato (o escriba 'si' para finalizar): ")

#     if entrada == "si":
#         break

#     lista_datos.append(entrada)

# print("Lista de datos ingresados:")
# print(lista_datos)

#lista=[]
#while len (lista) < 5:
   #ingresaDato=input("ingresa un dato: ")
   #lista.append(ingresaDato)
   #print(lista)

#def llenar_espacios(texto):
    #espacios_restantes = 5 - len(texto)
    #if espacios_restantes <= 0:
        #return texto
    #else:
        #return texto + ' ' * espacios_restantes

#datos = []
#for i in range(5):
    #dato = input("Ingresa un dato: ")
    ##datos.append(llenar_espacios(dato))

#print("Datos ingresados:")
#print (datos)


# pedir al usuario un numero luego generar la tabla de multiplicar de dicho
# numero del 1 hasta el 12
#tablaDe=int(input("ingrese un numero: "))
#for numero in range(1, 13):
    #resultado=numero*tablaDe
    #print(f"{numero} * {tablaDe} = {resultado}")

# hacer un program que me pidad un numero y me calcule su factorial
#def calcular_factorial(numero):
    #if numero == 0:
        #return 0
    #else:
        #factorial = 1
        #for i in range(1, numero + 1):
            #factorial *= i
        #return factorial

#numero = int(input("Ingresa un número: "))
#factorial_resultante = calcular_factorial(numero)
#print("El factorial de", numero, "es:", factorial_resultante)

#ejemplo 2
#numero2=int(input("ingrese el numero: "))
#factorial=1
#if numero2 == 0:
    #print("el factorial de 0 es 0")
#else:
    #for num in range(1,numero2+1):
        #factorial=factorial*num
    #print(factorial)

###pedir a  un usuario una lista de 5 elementos si en la lista se ingresa o contiene
##la palabra disco mostrar la palabra y la ubicacion de su indice positivo

#lista=[]
#while len (lista) < 5:
   #ingresaDato=input("ingresa un dato: ")
   #lista.append(ingresaDato)
#indice=lsta.index("disco")
#print(ilista[indice])
#print("se encuentra en el indice numero: ",indice)

# lista=[]
# indice=0
# palabra=""
# while len (lista)<5:
#     dato=input("ingrese un dato: ")
#     lista.append(dato)
# for texto in range(0,len(lista)):
#     if lista[texto] == "disco":
#         palabra=lista[texto]
#         indice=texto
# print(f"""el texto disco se encuentra en el indice hola {indice}
#       y el texto es {palabra}""")

# el objeto trabaja con clave y valor 
# objeto={"alumno":"jory","edad":50,"amigos":["mirella","anthony"]}
# objeto["alumno"]="moises"
# objeto["edad"]=25
# objeto["sexo"]="todos los dias"
# lista=[{"nombre":"jory"},{"nombre":"moises"},{"nombre":"edwin"}]
# for indice,list in enumerate (lista):
#     print(indice)
# objeto={}
# objeto["nombre"]=input("ingrese su nombre: ")
# objeto['apellido']=input("ingrese su apellido: ")
# objeto["edad"]=int(input("ingrese su edad: "))
# objeto['sexo']=input('ingrese M si eres hombre y F si eres mujer: ')
# print(objeto)

# lista=[]
# while True:
#     objeto={}
#     objeto["animal"]=input("ingrese que animal es: ")
#     objeto["nombre"]=input("ingresa en nombre como llamas a tu animal: ")
#     objeto["edad"]=int(input("ingresa el tiempo que esta contigo: "))
#     objeto["sexo"]=input("ingresa M si es macho y H si es hembra: ")
#     lista.append(objeto)
#     condicion=input("si desea salir escriba:salir, si desea continuar escriba:continuar: ")
#     if condicion == 'salir':
#         break
# print(lista)

# lista=[]
# while len (lista)<5:
#     objeto={}
#     objeto['nombre']=input('ingrese su nombre: ')
#     objeto['apellidos']=input('ingrese sus dos apellidos: ')
#     objeto['edad']=int(input('ingresa tu edad: '))
#     objeto['comida']=[]
#     while len(objeto['comida'])<3:
#         comida=input('ingrese su comida favorita: ')
#         objeto['comida'].append(comida)
#     lista.append(objeto)
#     condicion=input("si desea salir escriba:salir, si desea continuar escriba:continuar: ")
#     if condicion == 'salir':
#         break
# print(lista)

# empresa={}
# empresa['nombre']=input('ingresa el nombre de la empresa: ')
# empresa['ruc']=int(input('ingresa el ruc de la empresa: '))
# empresa['direccion']=input('ingresa la direcion de la empresa: ')
# empresa['sucursales']=[]
# while len(empresa['sucursales'])<2:
#     sucursal=input('ingrese el nombre de la sucursal: ')
#     empresa['sucursales'].append(sucursal)
# empresa['horario']={}
# empresa['horario']['dia']=input('ingresa el harario del dia: ')
# empresa['horario']['tarde']=input('ingresa el harario de la tarde: ')

# print(empresa)

# nombre=input('ingrese el nombre de la empresa: ')
# ruc=input('ingrese el ruc: ')
# direccion=input('ingresa la direccion. ')
# sucursales=[]
# for indice in range(0,3):
#     sucursal=input('ingresa la sucursal: ')
#     sucursales.append(sucursal)
# empresa={'nombre':nombre,
#          'ruc':ruc,
#          'direccion':direccion,
#          'sucursales':sucursales,
#          'horario':{
#              'dia':
#              'tarde'
#          }}

# nombre=input('ingrese el nombre de la empresa: ')
# ruc=input('ingrese el ruc: ')
# direccion=input('ingresa la direccion. ')
# sucursales=input('ingrese la sucursales separado por comas: '). split(',')
# horario_dia=input('ingrese el horario de dia: ')
# horario_tarde=input('ingrese el horario de la tarde: ')
# empresa={'nombre':nombre,
#          'ruc':ruc,
#          'direccion':direccion,
#          'sucursales':sucursales,
#          'horario':{
#              'dia':horario_dia,
#              'tarde':horario_tarde
#          }}
# print(empresa)
empresas=[]
while len(empresas)<3:
    nombre=input('ingrese el nombre de la empresa: ')
    ruc=input('ingrese el ruc: ')
    direccion=input('ingresa la direccion. ')
    sucursales=input('ingrese la sucursales separado por comas: '). split(',')
    horario_dia=input('ingrese el horario de dia: ')
    horario_tarde=input('ingrese el horario de la tarde: ')
    empresa={'nombre':nombre,
            'ruc':ruc,
            'direccion':direccion,
            'sucursales':sucursales,
            'horario':{
                'dia':horario_dia,
                'tarde':horario_tarde
            }}
    empresas.append(empresa)
print(empresa)