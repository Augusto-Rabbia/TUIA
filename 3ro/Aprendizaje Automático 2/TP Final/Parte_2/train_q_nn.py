import numpy as np
import pickle
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# --- Cargar Q-table entrenada ---
QTABLE_PATH = "flappy_birds_q_table.pkl"  # Cambia el path si es necesario
with open(QTABLE_PATH, "rb") as f:
    q_table = pickle.load(f)

# --- Preparar datos para entrenamiento ---
# Convertir la Q-table en X (estados) e y (valores Q para cada acción)
X = []  # Estados discretos
y = []  # Q-values para cada acción
for state, q_values in q_table.items():
    clase = np.argmax(q_values)  # Acción con mayor valor Q
    X.append(state)
    y.append(clase)

indices_shuffle = np.random.default_rng(seed=42).permutation(len(X))

scaler = StandardScaler()
X = np.array(X)[indices_shuffle]
X = scaler.fit_transform(X)
y = np.array(y)[indices_shuffle]
print(np.sum(y) / len(y))

with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)


# --- Definir la red neuronal ---
model = keras.Sequential(
    [
        keras.Input(shape=(X.shape[1],)),  # Tamaño del estado
        layers.Dense(64, activation="relu"),  # Capa oculta con 16 neuronas
        layers.Dense(32, activation="relu"),  # Capa oculta con 16 neuronas
        layers.Dense(16, activation="relu"),  # Otra capa oculta con 16 neuronas
        layers.Dense(
            1, activation="sigmoid"
        ),  # Capa de salida con una neurona por acción
    ]
)

model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# --- Entrenar la red neuronal ---

history = model.fit(X, y, epochs=1000)

# --- Mostrar resultados del entrenamiento ---

metrics = history.history
plt.figure(figsize=(16, 6))
plt.plot(history.epoch, metrics["loss"])
plt.legend(["loss"])
plt.ylim([0, max(plt.ylim())])
plt.xlabel("Epoch")
plt.ylabel("Loss [CrossEntropy]")

plt.subplot(1, 2, 2)
plt.plot(
    history.epoch,
    100 * np.array(metrics["accuracy"]),
)
plt.legend(["accuracy"])
plt.ylim([0, 100])
plt.xlabel("Epoch")
plt.ylabel("Accuracy [%]")
plt.show()


# --- Guardar el modelo ---
model.save("./flappy_q_nn_model.keras")
print("Modelo guardado como TensorFlow SavedModel en flappy_q_nn_model/")
