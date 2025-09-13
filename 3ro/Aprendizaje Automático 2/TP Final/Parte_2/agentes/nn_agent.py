from agentes.base import Agent
import numpy as np
import tensorflow as tf
import pickle


class NNAgent(Agent):
    """
    Agente que utiliza una red neuronal entrenada para aproximar la Q-table.
    La red debe estar guardada como TensorFlow SavedModel.
    """

    def __init__(
        self,
        actions,
        game=None,
        model_path="flappy_q_nn_model.keras",
        scaler_path="scaler.pkl",
    ):
        super().__init__(actions, game)
        # Cargar el modelo entrenado
        self.model = tf.keras.models.load_model(model_path)
        with open(scaler_path, "rb") as f:
            self.scaler = pickle.load(f)
        self.state_bins = {
            # Ejemplo de discretización, ajustar según el entorno:
            "player_vel_bins": 5,  # 5 valores posibles
            "player_relative_pipe_top_bins": 10,  # 10 valores posibles de distancia al tubo superior
            "player_relative_pipe_bottom_bins": 10,  # 10 valores posibles de distancia al tubo inferior
            "player_distance_pipe_bins": 10,  # 10 valores posibles de distancia al tubo, del 0 al 9
        }

    def discretize_state(self, state):
        """
        Discretiza el estado continuo en un estado discreto (tupla).
        """

        player_vel_bin = int(
            np.round((state["player_vel"] + 10) / 5)
        )  # La velocidad va del -10 y 10, llevada primero a 0-20,
        # y luego mapeada a 0-4

        dist_relative_pipe_top = int(
            (
                (state["next_pipe_top_y"] - state["player_y"] + self.game.height / 2)
                / self.game.height
            )
            * (self.state_bins["player_relative_pipe_top_bins"] - 1)
        )

        dist_relative_pipe_bottom = int(
            (
                (state["next_pipe_bottom_y"] - state["player_y"] + self.game.height / 2)
                / self.game.height
            )
            * (self.state_bins["player_relative_pipe_bottom_bins"] - 1)
        )

        dist_relative_pipe = int(
            (
                np.clip(
                    state["next_pipe_dist_to_player"] / self.game.width,
                    0,
                    1,
                )
            )
            * (self.state_bins["player_distance_pipe_bins"] - 1)
        )  # Mapeado a 0-4

        return (
            player_vel_bin,
            dist_relative_pipe_top,
            dist_relative_pipe_bottom,
            dist_relative_pipe,
        )

    def act(self, state):
        """
        Debe transformar el estado al formato de entrada de la red y devolver la acción con mayor Q.
        """

        discrete_state = np.array(self.discretize_state(state)).reshape(1, -1)
        model_input = self.scaler.transform(discrete_state)

        q_values = self.model.predict(model_input)
        q_value = self.actions[int(np.round(q_values))]

        return q_value
