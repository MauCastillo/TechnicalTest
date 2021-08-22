# TechnicalTest
 This is a technical test using django framework

Ejecución del proyecto
Se encuentra en el repositorio: https://github.com/MauCastillo/TechnicalTest.git
Se instalan la dependencias:
$ python3 -m venv env
$ source env/bin/activate
$  pip install -r requirements.txt

Se realiza la migración de los modelos en este caso utilice sqLite no hay necesidad de una conexión a un base datos externa
$ cd finca
$ python3 manage.py migrate
Crear un super usuario para el administrador de Django:
python3 manage.py createsuperuser --email admin@example.com --username admin
Ejecutar el proyecto
$ python3 manage.py runserver

Endpoints:
Método PUT y PATH pueden recibir los mismo parámetros en el cuerpo la diferencia está que el método PATH puede actualizar un único atributo del modelo y el PUT actualiza el modelo.

El método DELETE sigue la misma estructura de URL y esta elimina el registro que tenga el id = pk

El método POST Es la misma url sin incluir un valor en [pk] y recibe los mismo tipos de datos que seran datallados a continuacion


completo con todos los atributos:
http://127.0.0.1:8000/properties/[pk]/
Body data: 
"title": string,
 "image": string:url
"city": int,
"price": int,
 "category": int,
"sqft": int
"baths": int,
beds": int,
 

http://127.0.0.1:8000/categories/[pk]/
Body data:
"slug": "string"

http://127.0.0.1:8000/cities/[pk]/
 "slug": string,
 "state": int
"Zip": init


http://127.0.0.1:8000/states/[pk]/
Body data:
"slug": "string"
http://127.0.0.1:8000/property_types/[pk]/
Body data:
"slug": "string"
http://127.0.0.1:8000/transactions/[pk]/
"slug": string,
 "propertyTypes": [ "http://127.0.0.1:8000/property_types/1/"]
http://127.0.0.1:8000/reviews/[pk]/
Body data:
"feedback": string
"rating": int
"avatar":url:string
