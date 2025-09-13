from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        expandidos = set()
        # Add the node to the explored dictionary
        explored[node.state] = True
        cola = QueueFrontier()
        cola.add(node)
        expandidos.add(node.state)
        while True:
            if cola.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = cola.remove()
            
            
            # Mark the node as explored
            explored[node.state] = True

            # Return if the node contains a goal state
            #if node.state == grid.end:
            #    return Solution(node, explored)
            
            # BFS
            neighbours = grid.get_neighbours(node.state)
            for neighbour in neighbours:
                new_state = neighbours[neighbour]
                
                if new_state not in expandidos:
                    
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                    new_node.parent = node
                    new_node.action = neighbour
                    # Return if the node contains a goal state
                    if new_state == grid.end:
                        return Solution(new_node, explored)
                    expandidos.add(new_state)
                    cola.add(new_node)
