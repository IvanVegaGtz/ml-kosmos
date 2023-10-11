# ml-kosmos
API REST sencilla que recibe una lista de oraciones en español y devuelva una lista de las entidades nombradas identificadas en cada oración. Para realizar la API se utilizó Flask y para el modelo de reconocimiento de entdades nombradas (en inglés NER) se utilizó Spacy, específicament el modelo es_core_news_sm.

## Requisitos
Las principales librerías utilizadas son:
- Python 3.11.4
- Flask 3.0.0
- Werkzeug 3.0.0
- spacy 3.7.1

En requeriments.txt se encuentra el ambiente con el que se creó la API, aunque no todas las librerías son necesarias, ya que se ocupó una lebrería que ya ocupo para tareas de PLN.

## Archivos

- api.png : Imagen del ejemplo de salida de la API
- app.py : Script para crear la API
- requests.py : Script para hacer solicitudes a la API
- requeriments : librerías del ambiente que se utilizó


## Preparar la API

1. Clonar el repositorio, desde la terminal escribir: git clone https://github.com/IvanVegaGtz/ml-kosmos.git
2. Ir a la directorio del repositorio e instalar las librerias: pip install -r rquirements.txt (de preferencia solo instalar flask y spacy y ver si es necesario otra librería, ya qe de lo contrario puede tardarse varios minutos)
3. Es importante descargar el modelo en español de spacy que se utiliza: python -m spacy download es_core_news_sm


## Ejecutar la API
1. Correr desde terminal ---> python app.py de esta manera la API estará preparada para recibir solicitudes.
2. Correr el script de requests ---> requests.py  para realizar solicitudes, si se dea probar oraciones modificar la variable data.
3. Al seguir los pasos correctamente se obtienen los resultados para el reconocimiento de entidades nombradas

## Ejemplo de la salida de la API
![Salida de API](https://github.com/IvanVegaGtz/ml-kosmos/blob/main/api.png)


