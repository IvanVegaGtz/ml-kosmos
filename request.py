import requests
import json

# Establecemos la URL de la API
url = 'http://localhost:5000/ner'  

# data contiene las oraciones que queremos analizar
data = {
    "oraciones": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera.",
        "La empresa Telmex de Carlos Slim fue fundada en el 1 de enero de 1947 en la Ciudad de México ",
        "Kosmos es una plataforma digital que permite crear procesos financieros totalmente digitales en tiempo real, sin la necesidad de código "
        ""
    ]
}

# Realiza la solicitud POST a la API
response = requests.post(url, json=data)

# Verficamos que se haya realizado la solicitud con éxito
if response.status_code == 200:
    # SI la solicitud se completó satisfactoriamente se procesa la respuesta JSON
    response_data = response.json()
    # Imprimimos el resultado 
    print(json.dumps(response_data, indent=4, ensure_ascii=False))
else:
    # Si la solicitud falló se muestra un mensaje de error
    print("Error al realizar la solicitud:", response.status_code, response.text)
