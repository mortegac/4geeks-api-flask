<p align="center">
  <img src="https://assets.breatheco.de/apis/img/images.php?blob&random&cat=icon&tags=4geeks,128">
</p>

<p>
    <h2 align="center"> Ejercicio creando mi primera API</h2>
    <h3 align="center"> usando Flask</h3>
    <h3 align="center"> 4Geeks Academy</h3>
</p>




En este ejercicio realizamos un ejemplo de una API en Flask que tenga los métodos http:

- GET
- GET/:id
- POST
- PUT/:id
- DELETE/:id

## Lecturas
- [API Rest](https://content.breatheco.de/lesson/understanding-rest-apis)

- [Flask](https://content.breatheco.de/es/lesson/building-apis-with-python-flask)


<h2>Instalación:</h2>

1. Asegurate de tener [python](https://www.python.org/downloads/) instalado y [pip](https://pip.pypa.io/en/stable/installing/)

2. Crear el entorno virtual

`Intrucción para OSX o Linux`
```
python3 -m venv venv
```

`Intrucción para Windows 10`
```
py -3 -m venv venv
```


3.- Activar el entorno virtual creado
```
. venv/bin/activate

```
4.- Instalar Flask como dependencia en el proyecto utilizando `pip`

```
pip install Flask
```

5.- Crear la aplicación para que Flask la reconozca

```
export FLASK_APP=server.py
```

6.- Ejecutar la app 

```
flask run
```


## Plugins Visual Studio Code para consumir endPoint de la API

- [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)


