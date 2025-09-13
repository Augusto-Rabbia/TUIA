# NLP_TP1 - Tiny Towns

## TUIA - Procesamiento del Lenguaje Natural · 2025

## Integrantes

- Eugenio Bravi
- Augusto Rabbia
- Manuel Spreutels

## Docentes

- Juan Pablo Manson
- Alan Geary
- Constantino Ferruci
- Dolores Sollberger

## Descripción general

Este trabajo práctico aplica técnicas de procesamiento del lenguaje natural (PLN) para analizar y extraer información de distintas fuentes relacionadas al juego _Tiny Towns_, disponible en [BoardGameGeek (BGG)](https://boardgamegeek.com/).  
A lo largo del proyecto se desarrollaron distintas etapas de scraping, limpieza y organización de datos para facilitar su futuro uso.

## Scrapping

### 1. Créditos y relaciones del juego

[Tiny Towns: Créditos del juego](https://boardgamegeek.com/boardgame/265736/tiny-towns/credits)  
**Objetivo:** Obtener de los créditos los distintos nombres alternativos del juego, año de lanzamiento, los mecanismos que incluye el juego y su descripción, los tipo de familia de juego en los que pertenece este juego y su descripción, y también obtuvimos las descripciones de los diseñadores, los publicadores, los artistas y los juegos en los que están asociados.

- **Librerías utilizadas:** `selenium`, `beautifulsoup4`
- **Qué se hace:**
  - Se extraen los creditos de la sección de creditos de [Tiny Towns](https://boardgamegeek.com/boardgame/265736/tiny-towns/credits)
  - Se scrapea los links de los créditos (diseñador, artista, editorial, etc.) para obtener:
    - Una descripción breve
    - Los juegos más populares
  - La información se guarda en un archivo CSV:
    - Ejemplo: `"Tiny Towns", "Designer", "Peter McPherson"`

### 2. Estadísticas del juego

[Tiny Towns: Estadísticas](https://boardgamegeek.com/boardgame/265736/tiny-towns/stats)
**Objetivo:** Recolectar datos tabulares de la ficha principal del juego. Se incluyen métricas como cantidad de jugadores, duración esperada, edad recomendada (oficial y por la comunidad), cantidad de votos, rankings, dificultad, precios en distintas tiendas y cantidad de expansiones disponibles.

- **Librerías utilizadas:** `selenium`, `beautifulsoup4`, `pandas`
- **Qué se hace:**
  - Se extraen rankings, cantidad de votos, dificultad, tiempo estimado de juego.
  - Se extraen los nombres de las tiendas y sus respectivos precios
  - Se extrae el número total de expansiones disponibles en la plataforma
  - También se obtienen datos como número de jugadores, duración estimada, edad recomendada (oficial y por comunidad)
  - Todos los datos se organizan en un `DataFrame` con columnas `Title` y `Value`, y se exportan a CSV

### 3. Top foros de Tiny Towns

[Tiny Towns: Página principal del juego](https://boardgamegeek.com/boardgame/265736/tiny-towns)

**Objetivo:** Obtener una información de las discusiones de la comunidad del juego, enfocándonos en las secciones `Rules`, `Variants`, `Strategy` y `Reviews`. Se scrapean los 10 foros con mayor de cada sección. De esta forma, asumimos que obtendremos la información de mayor calidad que se puede encontrar en los foros para un usuario.

- **Librerías utilizadas:** `selenium`, `beautifulsoup4`, `pandas`
- **Qué se hace:**
  - Se navega por las categorías: `Reviews`, `Rules`, `Strategy`, y `Variants`
  - En cada una, se toman los 10 hilos más relevantes y se extrae:
    - El título
    - El enlace
    - El texto completo del hilo (post inicial y respuestas)
  - Todo se guarda en un `DataFrame` con columnas `Category`, `Link to Post`, y `Conversation`

### 4. Reseñas externas en español.

[Misut Meeple - Reseña en español](https://misutmeeple.com/2020/03/resena-tiny-towns/)

**Objetivo:** Extraer de una página web una extensa reseña en español que pueda proporcionar interesantes justificaciones o sobre las opiniones de las distintas mecánicas del juego, y que cuente con una estructura dividida en secciones y subsecciones

- **Librerías utilizadas:** `selenium`, `beautifulsoup4`, `markdownify`
- **Qué se hace:**
  - Se toma una reseña de un blog externo en español
  - Se extrae el contenido principal y se convierte a Markdown para mantener el formato
  - Los textos resultantes se guardan en archivos `.txt`

### 5. Texto del manual oficial

[Reglamento PDF](https://www.alderac.com/wp-content/uploads/2025/03/TinyTowns_Rulebook.pdf)

**Objetivo:** Extraer el contenido del reglamento oficial del juego a partir del PDF que incluye información sobre las reglas, los componentes, el trasfondo narrativo y la estructura del juego. Este contenido resulta util para la extracción de conocimiento basado en reglas.

- **Librerías utilizadas:** `requests`, `pymupdf`, `re`
- **Qué se hace:**
  - Se descarga el PDF desde una URL
  - Se extrae el texto página por página
  - Se realiza una limpieza básica del texto con expresiones regulares
  - El resultado se guarda en un archivo `.txt`

### 6. Transcripciones de videos de YouTube

**Videos utilizados:**

- [Review ingles](https://www.youtube.com/watch?v=yF--uYWp0zw)
- [Review ingles](https://www.youtube.com/watch?v=WGhZ83B4MoQ)
- [Review español](https://www.youtube.com/watch?v=OyBCApqyUHg)
- [Review neerlandés](https://www.youtube.com/watch?v=Ko6waVAt1CU)

**Objetivo:** Obtener transcripciones automáticas de videos (tutoriales y reseñas) en distintos idiomas para ampliar la diversidad de idiomas. Las transcripciones permiten analizar cómo se explica el juego en distintos contextos y con un enfoque mas practico de lo que se puede obtener de una reseña de foro.

- **Librerías utilizadas:** `youtube_transcript_api`, `re`
- **Qué se hace:**
  - Se parte de una lista predefinida de videos sobre _Tiny Towns_
  - Se extraen las transcripciones disponibles en idiomas como español, inglés y neerlandés
  - Cada transcripción se guarda en un archivo `.txt` separado

## Análisis de datos

Luego, se realizó un análisis exploratorio de los datos obtenidos a través de gráficos con `Matplotlib`.

Entre otros, los análisis incluyeron conteo de clases en dataframes, conteos de caracteres y palabras, conteo e interpretación de frases según su longitud, y análisis de datos según su origen y su idioma.
