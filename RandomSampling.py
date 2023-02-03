
import random


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x        

class MapNodes:
    def __init__(self, map_dimensions, obstacles):
        self.map_height, self.map_width = map_dimensions

        # Nodes
        # self.nodes = []

        # Initialize obstacles
        self.obstacles = obstacles

    def addNode(self):
        node_x = random.randint(0, self.map_width)
        node_y = random.randint(0, self.map_height)
        node = Node(node_x, node_y)
        if self.isFree(node):
            return node

    def addEdge(self, node1, node2):
        pass

    def removeNode(self):
        pass

    def removeEdge(self):
        pass

    def distance(self, node1, node2):
        return ((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2) ** 0.5

    def nearestNNodes(self, nodes, ref_node, n):
        # Return n nearest nodes
        distances = []
        for node in nodes:
            distances.append(self.distance(ref_node, node))
        sorted_nodes = [x for _, x in sorted(zip(distances, nodes))]
        return sorted_nodes[:n]

    def isFree(self, node):
        # Check if node is in obstacle
        for obstacle in self.obstacles:
            if obstacle.collidepoint(node.x, node.y):
                return False
        return True

    def crossObstacle(self, node1, node2):
        # Create intermediate nodes
        for i in range(0, 100):
            x = node1.x + i * (node2.x - node1.x) / 100
            y = node1.y + i * (node2.y - node1.y) / 100
            node = Node(x, y)

            # Check if intermediate nodes are in obstacle
            if not self.isFree(node):
                return True
        return False


    def connect(self):
        pass

    def step(self):
        pass

    def pathToGoal(self):
        pass

    def getPathCoordinates(self):
        pass

    def bias(self):
        pass

    def expand(self):
        pass

    def cost(self):
        pass