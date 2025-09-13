import json
import requests

# URL del archivo JSON
url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"

# Descargar el archivo JSON
respuesta = requests.get(url)
# print(respuesta.text) para ver el texto crudo
# Convertimos los datos en formato de texto plano a listas y diccionarios (json)
datos = respuesta.json()

# Escribimos el contenido de datos en "books.json"
with open("books.json", "w") as archivo_json:
    json.dump(datos, archivo_json)

# Ejecutar consultas a los datos
# Por ejemplo, supongamos que el archivo JSON contiene una lista de usuarios
# y queremos imprimir el nombre de cada usuario
#for book in data:
#    nombre = book["country"]
#    print(nombre)

# Obtener información sobre la estructura del archivo
num_objetos = len(datos)  # Número de objetos en el archivo

if num_objetos > 0:
    primer_objeto = datos[0]  # Obtener el primer objeto para analizar sus propiedades

    propiedades = list(primer_objeto.keys())  # Obtener las propiedades del primer objeto
    tipos_de_dato = {prop: type(primer_objeto[prop]) for prop in propiedades}  # Obtener el tipo de dato de cada propiedad

    print("Información sobre el archivo JSON:")
    print(f"Número de objetos: {num_objetos}")
    print("Propiedades del primer objeto:")
    for prop in propiedades:
        tipo = tipos_de_dato[prop].__name__
        print(f"- {prop}: {tipo}")
else:
    print("El archivo JSON no contiene ningún objeto.")