# entornos virtuales 
pyenv .- es una herramienta que nos permite instalar diferentes versiones de python y cambiar entre ellos segun los requerimientos del proyecto con el cual necesitamos trabajar.
pipenv .- Si queremos tener un gestor que nos unifique y gestione tanto Virtualenv como Pip podemos utilizar Pipenv. Pipenv funciona en Windows, Linux y Mac; y en todos los sistemas operativos funciona exactamente igual (cambiando la ruta donde se guardan las cosas).
pip .- es un manejador de paquetes es un comando que permite instalar paquetes de python en nuestros proyectos
venv .- manejador de entorno virtuales ya preinstalados en python
# para crear un entorno virtual
1. nos ubicamos en la carpeta que deseamos crear el entorno virtual
```bash
cd <ruta del archivo>
#ejemplo 
cd nombre_carpeta/entorno_uno
```

2. creamos en entorno virtual con el siguiente comando
```bash 
python -m venv <nombre de usuario entorno virtual>
#ejemplo
python -m venv mi_entorno
```

3. para activar el entorno virtual con el git bash como terminal predeterminada corremos el siguiente comando solo para windows.
```bash
source venv/Script/activate
```
> #### observacion:
> para poder ejecutarlo en powersell como terminal predeterminado ejecutar el siguiente comando.
```bash
venv\Scripts\Activate.ps1
```
## para instalar paquetes en nuestro entorno virtual
1. primero verificamos que no tengamos el paquete instalado y lo listamos con el siguiente comando.
debemos tener activado nuestro entorno virtual primero
```bash
pip list
```
2. luego instalaremos con el siguiente comando.
```bash
pip install <nombre del paquete>
#ejemplo
pip install pandas
```