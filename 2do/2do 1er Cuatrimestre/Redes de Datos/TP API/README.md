# Observaciones


## Requerimientos

Python 3.11  
Antes de ejecutar, instalar los siguientes repositorios:
- requests
`pip install requests`
- fastapi 
`pip install fastapi`
- uvicorn 
`pip install uvicorn`

## Cómo ejecutar

### Ejecución del servidor

Ejecutar el siguiente comando en una terminal: `uvicorn --host [IP] api:app --reload`  
Donde [IP] puede ser 127.0.0.1 para que sea accesible únicamente de forma local (mismo dispositivo),
o 0.0.0.0 para que pueda ser visto por otros dispositivos en la red.

### Manejo del cliente

Ejecutar el siguiente comando en una terminal: `python cliente.py`
En el cliente se pedirá ingresar la ip del servidor, si fue ejecutado con [IP] = 0.0.0.0,
esta será la ipv4 del dispositivo host. Luego de esto, el manejo del cliente es intuitivo.
