# Predictor de lluvia


Para ejecutar el modelo de predicción de lluvia, seguir los siguientes pasos:

1. Hacer un build de la imagen con el comando `docker build -t [NOMBRE DE LA IMAGEN (a elección)] [DIRECTORIO DONDE SE ENCUENTRA EL DOCKERFILE] `

2. Ejecutar el contenedor con el comando `docker run -it --rm --name [NOMBRE DEL DOCKER EN EJECUCIÓN (a elección)] -v "[DIRECTORIO DONDE SE ENCUENTRA EL ARCHIVO PARA LA INFERENCIA]:/app" [NOMBRE DE LA IMAGEN (elegido en el paso anterior)] python inferencia.py [NOMBRE DEEL ARCHIVO A INFERIR (.csv)] [NOMBRE DEL ARCHIVO CON LOS RESULTADOS (.csv)]`
