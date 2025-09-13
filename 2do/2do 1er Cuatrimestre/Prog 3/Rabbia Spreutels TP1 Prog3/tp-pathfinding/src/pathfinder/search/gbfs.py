from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        explored = {} 
        # Add the node to the explored dictionary
        explored[node.state] = True
        colaP = PriorityQueueFrontier()
        colaP.add(node)
        while True:
            if colaP.is_empty():
                return NoSolution(explored)

            # Remove a node from the frontier
            node = colaP.pop()

            if node.state in explored and node.state != grid.start:
                continue

            # Mark the node as explored
            explored[node.state] = True

            # Return if the node contains a goal state
            if node.state == grid.end:
                return Solution(node, explored)
            
            # Greedy Breadth first search
            neighbours = grid.get_neighbours(node.state)
            for neighbour in neighbours:
                new_state = neighbours[neighbour]
                
                if new_state not in explored:
                    # distancia de manhattan
                    dist = abs(new_state[0]-grid.end[0]) + abs(new_state[1]-grid.end[1])
                    new_node = Node("", new_state, node.cost + grid.get_cost(new_state))
                    new_node.parent = node
                    new_node.action = neighbour
                    colaP.add(new_node, dist)