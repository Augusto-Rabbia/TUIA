# TP1 NLP Parte 2

## TUIA - Procesamiento del Lenguaje Natural · 2025

Augusto Rabbia

## Docentes

- Juan Pablo Manson
- Alan Geary
- Constantino Ferruci
- Dolores Sollberger

## Descripción general

Esta segunda etapa del trabajo práctico consiste en aplicar un análisis de un conjunto de datos del juego de mesa [Parks](https://boardgamegeek.com/boardgame/266524/parks).

Estos datos fueron recolectados, parseados y parcialmente procesados por otro equipo parte del aula para su utilización durante esta etapa.

## Lectura de datos

Se extraen los datos del archivo zip `datos_Parks.zip`, se examinan los archivos, y luego se extraen y organizan los datos de 3 tipos:
- Información
- Relaciones
- Estadísticas

## Análisis similitud de frases en un fragmento de datos

Se extrae el fragmento de la sección de información en el archivo `descripcion_juego.txt`. Se realiza splitting con `RecursiveCharacterTextSplitter` de `langchain`, y se obtiene un embedding de las frases resultantes con `Universal Sentence Encoder`.

Se analiza la similitud de los utilizando distancia euclediana, similitud de coseno, de Jaccard y de Dice.

Luego, se realiza una visualización de los embeddings realizando PCA y t-SNE para reducción de dimensionalidad a un espacio bidimensional.

## Análisis de entidades con POS y NER

Se extrae el texto de `reglas_pdf_ingles.txt` y se realiza splitting con `RecursiveCharacterTextSplitter` para obtener frases a analizar con GLiNER. Los labels utilizados fueron `place`, `tools`, `person`, `board game piece` 

En total, 69 entidades únicas fueron identificadas en la totalidad del texto.

Se realizó un análisis de similitud de los conjuntos de entidades de las frases utilizando la similitud de Jaccard y de Dice.

## Clasificación del idioma de cada archivo

Se realizó clasificación del idioma de cada archivo utilizando la libería `langdetect`, y los resultados fueron escritos en un dataframe de `Pandas`.

## Análisis de sentimiento de reseñas

Se extrajo el texto de todas las reseñas disponibles. Se realizó splitting del texto con `RecursiveCharacterTextSplitter` y análisis de sentimiento de cada frase con el modelo de análisis de sentimientos de **Bert**.

Para cada reseña, se construyó un puntaje final promediando el puntaje asignado a sus subfrases.

## Clasificador de consultas

Se fabrica un conjunto de datos de queries sobre el juego de mesa Parks, generado con el modelo GPT-4o de [ChatGPT](https://chatgpt.com/). Se realiza embedding con `Universal Sentence Encoder` y se entrena un modelo de Regresión Logística de `scikit-learn` y un modelo de red neuronal con `tensorflow` para la predicción de la categoría a la que pertenece la consulta entre `Informacion`, `Estadisticas` y `Relaciones`.

Luego, se evalúa el performance de cada modelo con `classification_report`.



