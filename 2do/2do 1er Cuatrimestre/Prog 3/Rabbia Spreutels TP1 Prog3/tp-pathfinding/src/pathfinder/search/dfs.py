from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)
        pila = StackFrontier()
        # Initialize the explored dictionary to be empty
        explored = {} 
        # Add the node to the explored dictionary
        explored[node.state] = True
        pila.add(node)
        while True:
            if pila.is_empty():
                return NoSolution(explored)
            
            # Remove a node from the frontier
            node = pila.remove()
            
            if node.state in explored and node.state != grid.start:
                continue
            # Mark the node as explored
            explored[node.state] = True

            # Return if the node contains a goal state
            if node.state == grid.end:
                return Solution(node, explored)
            
            # DFS
            neighbours = grid.get_neighbours(node.state)
            for neighbour in neighbours:
                new_state = neighbours[neighbour]
                
                if new_state not in explored:
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                    new_node.parent = node
                    new_node.action = neighbour
                    pila.add(new_node)