"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo, y los empates se resuelvan de forma aleatoria.
Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from problem import OptProblem
from node import Node
from random import choice
from time import time
from math import log, floor


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Crear el nodo inicial
        actual = Node(problem.init, problem.obj_val(problem.init))

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual.state)

            # Buscar las acciones que generan el  mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local
            if diff[act] <= 0:

                self.tour = actual.state
                self.value = actual.value
                end = time()
                self.time = end-start
                return

            # Sino, moverse a un nodo con el estado sucesor
            else:
                actual = Node(problem.result(actual.state, act),
                              actual.value + diff[act])
                self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Crear el nodo inicial
        actual = Node(problem.init, problem.obj_val(problem.init))

        n = len(problem.init)
        maxResets = floor(max(1, -log(n, 25/24)+112))
        # Encontramos que con esta ecuación, nos suele dar una cantidad razonable
        # de repeticiones.
        self.value = actual.value
        self.tour = actual.state
        cantResets = 0
        while True:
            self.niters += 1
            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual.state)

            # Buscar las acciones que generan el  mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local
            if diff[act] <= 0:              
                if (actual.value > self.value):
                    self.tour = actual.state
                    self.value = actual.value

                # Repetimos hasta llegar a maxResets
                if (cantResets == maxResets):
                    end = time()
                    self.time = end-start
                    return
                else:
                    problem.random_reset()
                    actual = Node(problem.init, problem.obj_val(problem.init))
                cantResets += 1
            # Sino, moverse a un nodo con el estado sucesor
            else:
                actual = Node(problem.result(actual.state, act),
                              actual.value + diff[act])

class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Crear el nodo inicial
        actual = Node(problem.init, problem.obj_val(problem.init))

        tabu = []
        iterSinMejorar = 0
        n = len(problem.init) # Será el tamaño de la lista Tabú
        self.value = actual.value
        self.tour = actual.state
        while True:
            if (self.value < actual.value):
                iterSinMejorar = 0
            elif (iterSinMejorar > 2*n):
                end = time()
                self.time = end-start
                return
            else: 
                iterSinMejorar += 1
            self.niters += 1
            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual.state)

            acts = [act for act, val in diff.items() if act not in tabu]

            # Buscar las acciones que generan el  mayor incremento de valor obj
            # Pero solo entre aquellas acciones que no estén en la lista tabú
            vals_validos = [val for act, val in diff.items() if act not in tabu]
            max_acts = [act for act, val in diff.items() if val ==
                        max(vals_validos)]

            # Elegir una accion aleatoria
            act = choice(max_acts)
            
            # La añadimos a la lista tabú
            tabu.append(act)
            # La lista tabú tendrá tamaño n.
            # Si ya hicimos más de n iteraciones, eliminamos en
            # cada iteración el elemento más antiguo de la lista tabú
            if(self.niters > n):
                tabu.pop(0)
            # Retornar si estamos en un optimo local
            if diff[act] <= 0:
                if(self.value < actual.value):
                    self.value = actual.value
                    self.tour = actual.state
                
                actual = Node(problem.result(actual.state, act),
                          actual.value + diff[act])
                
            # Sino, moverse a un nodo con el estado sucesor
            else:
                actual = Node(problem.result(actual.state, act),
                              actual.value + diff[act])