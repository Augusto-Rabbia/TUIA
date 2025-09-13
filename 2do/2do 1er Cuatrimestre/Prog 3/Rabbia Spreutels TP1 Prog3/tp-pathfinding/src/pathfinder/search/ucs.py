from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        # El dict alcanzados tendrá los nodos alcanzados por
        # el algoritmo como keys y como value, tendrá el coste
        # para que siempre tenga guardada la forma menos costosa
        alcanzados = dict()
        # Add the node to the explored dictionary
        explored[node.state] = True
        colaP = PriorityQueueFrontier()
        colaP.add(node)
        alcanzados[node.state] = 0
        # UCS
        while True:
            if colaP.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = colaP.pop()
            # Mark the node as explored
            explored[node.state] = True

            # Return if the node contains a goal state
            if node.state == grid.end:
                return Solution(node, explored)
            
            # Go right
            neighbours = grid.get_neighbours(node.state)
            for neighbour in neighbours:
                new_state = neighbours[neighbour]
                costo = node.cost + grid.get_cost(new_state)
                if new_state not in alcanzados or costo < alcanzados[new_state]:
                    alcanzados[new_state] = costo
                    new_node = Node("", new_state, costo)
                    new_node.parent = node
                    new_node.action = neighbour
                    colaP.add(new_node, new_node.cost)
