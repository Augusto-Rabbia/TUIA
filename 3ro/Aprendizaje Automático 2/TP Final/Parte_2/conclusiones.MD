# TP Final NLP - Ejercicio 2

Integrantes:

- Bravi Eugenio
- Rabbia Augusto
- Spreutels Manuel

Dentro del repositorio se debe incluir un archivo conclusiones.md (usando Markdown) con:
Descripción de la ingeniería de características sobre el estado del juego (discretización).
Análisis y comparación de los resultados obtenidos para los diferentes agentes.

# Análisis y comparación

## Agente Q-learning:

El agente Q-learning tiene un rendimiento prácticamente perfecto cuando es puesto a prueba. Este modelo destaca por su eficiencia computacional, ya que requiere significativamente menos recursos en comparación con el agente basado en redes neuronales (NN). El proceso de entrenamiento del agente Q-learning consiste en la creación, definición y actualización iterativa de la Q-table. En la practica este agente utiliza el estado del jugador para buscar un valor en la Q-table y tomar una decision, esta simplicidad permite que el agente funcione de manera rápida y efectiva.

### Elección e ingeniería de características

Las características utilizadas sobre el estado del juego fueron elegidas a través de cierto grado de intuición, y prueba y error: Nos preguntabamos si cierta característica nos sería de utilidad a nosotros si fueramos los jugadores. Si la respuesta era que sí, la añadíamos, si no, no era añadida. Sin embargo, a partir de esta idea, removimos, por ejemplo, la variable de distancia relativa al tubo superior, intuyendo que bastaba con estar encima pero cerca del tubo inferior. Sin embargo, esto resultaba en un performance pobre, por lo que en el modelo final, se añadió esta variable del estado. Finalmente, trabajamos con las siguientes características:

- Velocidad del jugador en el eje y (`player_vel`): Discretizada para tener 5 valores posibles, dos representando velocidades negativas (bajando), una "neutral", y otras dos positivas (subiendo).
- Distancia relativa del jugador al tubo superior e inferior en el eje y (`player_relative_pipe_top`, `player_relative_pipe_bottom`): Discretizada a 10 valores posibles, con 5 inferiores y 5 superiores.
- Distancia del jugador a los próximos tubos en el eje x (`player_distance_pipe_bins`): Discretizada a 10 valores posibles representando cuán lejos se está con 0 representando que se está encima del tubo, y 10 representando que el próximo tubo está a una pantalla de distancia.

## Agente NN:

El agente basado en redes neuronales (NN) también logra un desempeño perfecto tras su entrenamiento, siendo capaz de emular con precisión absoluta el comportamiento de el modelo Q-learning. Sin embargo, este resultado tiene un costo significativo en términos de recursos y tiempo. No sólo es impráctico el necesitar una Q-table como dataset para entrenemiento, sino que tanto el entrenamiento de las redes neuronales como su ejecución resultan sumamente costosos: Este modelo, a diferencia del modelo de Q-learning, genera un cuello de botella significativo, siendo imposible su ejecución en tiempo real, reduciendo la velocidad de ejecución del juego a unos pocos frames por segundo.

Esto demuestra el fuerte que tienen los modelos de aprendizaje por refuerzo en este tipo de problemas: Son capaces de aprender problemas secuenciales a través de la experiencia y sin la necesidad de datos etiquetados de manera previa. Todo esto mientras mantienen la ventaja de ser altamente eficientes en la toma de decisiones para problemas sencillos como el juego de Flappy Bird.
