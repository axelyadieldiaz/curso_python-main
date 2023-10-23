# Programacion Orientado a Objetos(POO)
### en ingles es Object Orient Programing (OOP)
es un paradicma de programacion
> **paradigma** - es un modelo, patron o ejemplo que se debe seguir

POO es un modelo de como programar 
**objetivo** - el objetivo es organizar el codigo de manera que se asemeje a como pemsamos en la vida real

se basa en objetos
y el la POO un objeto es toda entidad que se puede escribir atravez de **atributos** y **funciones** que pueda realizar la entidad

```python
class celular:
    #atributos de tipo clase
    # que son iguales para todos los objetos
    # que se creen
    familia='smart phone'
    
    #atributos de intancia
    #son atributos propios del objeto 
    #creamos una funcion inicializadora
    def __init__(self,marca,modelo,imei,nroCelular):
        self.marca=marca
        self=modelo=modelo
        self.imei=imei
        self.nroCelular.nroCelular


    #funcionalidades
    def llamar(self,destino):
        return f'llamando a {destino}'

#objeto celular jory
llamandojory=Celular('poco','x5','243454565','4352323324') #instanciando mi clase - creando mi objeto celular
print(llamandojory.marca)
print(llamandojory.familia)
print(llamandojory.llamar('china'))

#objeto celular nadine
llamandonadine=Celular('alcatel','basico','2456785432','6433223423')
print(llamandonadine.marca)
print(llamandonadine.familia)
print(llamandonadine.llmar('ollanta'))

 ```

 ## tarea
 #### 1. crear una lista con con 10 objetos que contengan los datos de las tiendas comerciales
 > ejemplo:
 >
 
```python
 tiendas=[
    {
        "ruc":245678324,
        "nombre":"el pichilon",
        "categoria":["bodega"]
        "horario_atencion":{
            "dia":7am-12pm,
            "tarde":2pm-8pm
        }
        "gerente":"manuela"
    }
 ]
 ```
 #### observacion: 'las categorias sera 4: abarrotes, farmacia, bodega,restaurat'
 #### observacion 'los gerentes solo podran ser los siguientes : edwin, china, crhistian, nadine'

 ## realizar los siguientes ejercicios
 #### crear una clase para tiendas que tenga los siguientes metodos o casos de uso.
 1. crear un metodo que me filtre las tiendas que tiene cada gerente
 2. crear un metodo que me muestre los negocios que tienen mas de dos categorias 
3. crear un metodo que me muestre solo el nombre y ruc de las tiendas