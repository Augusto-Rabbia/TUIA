from agentes.base import Agent
import numpy as np
from collections import defaultdict
import pickle
import random


class QAgent(Agent):
    """
    Agente de Q-Learning.
    Completar la discretización del estado y la función de acción.
    """

    def __init__(
        self,
        actions,
        game=None,
        learning_rate=0.1,
        discount_factor=0.99,
        epsilon=0,
        epsilon_decay=0.995,
        min_epsilon=0.01,
        load_q_table_path="flappy_birds_q_table.pkl",
    ):
        super().__init__(actions, game)
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        if load_q_table_path:
            try:
                with open(load_q_table_path, "rb") as f:
                    q_dict = pickle.load(f)
                self.q_table = defaultdict(lambda: np.zeros(len(self.actions)), q_dict)
                print(f"Q-table cargada desde {load_q_table_path}")
            except FileNotFoundError:
                print(
                    f"Archivo Q-table no encontrado en {load_q_table_path}. Se inicia una nueva Q-table vacía."
                )
                self.q_table = defaultdict(lambda: np.zeros(len(self.actions)))
        else:
            self.q_table = defaultdict(lambda: np.zeros(len(self.actions)))

        self.state_bins = {
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
        Elige una acción usando epsilon-greedy sobre la Q-table.
        COMPLETAR: Implementar la política epsilon-greedy.
        """

        if random.random() < self.epsilon:
            return random.choice(self.actions)
        else:
            discrete_state = self.discretize_state(state)
            # print(discrete_state)
            if discrete_state not in self.q_table:
                self.q_table[discrete_state] = np.zeros(len(self.actions))
            q_values = self.q_table[discrete_state]
            q_value = self.actions[np.argmax(q_values)]
            # print(self.actions)
            return q_value
        # Sugerencia:
        # - Discretizar el estado
        # - Con probabilidad epsilon elegir acción aleatoria
        # - Si no, elegir acción con mayor Q-value
        raise NotImplementedError("Completar la función de selección de acción (act)")

    def update(self, state, action, reward, next_state, done):
        """
        Actualiza la Q-table usando la regla de Q-learning.
        """
        discrete_state = self.discretize_state(state)
        discrete_next_state = self.discretize_state(next_state)
        action_idx = self.actions.index(action)
        # Inicializar si el estado no está en la Q-table
        if discrete_state not in self.q_table:
            self.q_table[discrete_state] = np.zeros(len(self.actions))
        if discrete_next_state not in self.q_table:
            self.q_table[discrete_next_state] = np.zeros(len(self.actions))
        current_q = self.q_table[discrete_state][action_idx]
        max_future_q = 0
        if not done:
            max_future_q = np.max(self.q_table[discrete_next_state])
        new_q = current_q + self.lr * (reward + self.gamma * max_future_q - current_q)
        self.q_table[discrete_state][action_idx] = new_q

    def decay_epsilon(self):
        """
        Disminuye epsilon para reducir la exploración con el tiempo.
        """
        self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)

    def save_q_table(self, path):
        """
        Guarda la Q-table en un archivo usando pickle.
        """
        import pickle

        with open(path, "wb") as f:
            pickle.dump(dict(self.q_table), f)
        print(f"Q-table guardada en {path}")

    def load_q_table(self, path):
        """
        Carga la Q-table desde un archivo usando pickle.
        """
        import pickle

        try:
            with open(path, "rb") as f:
                q_dict = pickle.load(f)
            self.q_table = defaultdict(lambda: np.zeros(len(self.actions)), q_dict)
            print(f"Q-table cargada desde {path}")
        except FileNotFoundError:
            print(
                f"Archivo Q-table no encontrado en {path}. Se inicia una nueva Q-table vacía."
            )
            self.q_table = defaultdict(lambda: np.zeros(len(self.actions)))
